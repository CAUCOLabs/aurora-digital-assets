from datetime import datetime, timezone

from app.schemas.agent_permissions import AgentPermissionEvaluationRequest
from app.schemas.agent_registry import AgentRegistryDetail
from app.schemas.agent_sensitive_action_guard import (
    AgentSensitiveActionDefinition,
    AgentSensitiveActionGuardRequest,
    AgentSensitiveActionGuardResponse,
    AgentSensitiveActionGuardRule,
    AgentSensitiveApprovalContextRequest,
    AgentSensitiveApprovalContextResponse,
)
from app.services.agent_actions_service import ACTION_TYPES
from app.services.agent_passport_service import agent_passport_service
from app.services.agent_permissions_service import agent_permissions_service
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service
from app.services.review_case_service import review_case_service


AGENT_SENSITIVE_ACTION_TYPES = [
    "request_sensitive_operation_approval",
    "suggest_risk_decision",
    "create_review_case",
    "create_evidence_package",
    "request_data_export",
    "request_key_rotation",
    "request_custodian_integration_review",
    "request_cloud_kubernetes_change",
    "attempt_secret_access",
    "attempt_custodian_api_access",
    "attempt_withdrawal_trigger",
    "attempt_withdrawal_approval",
    "attempt_permission_change",
    "attempt_record_modification",
]

SECRET_ACTIONS = {"attempt_secret_access"}
CUSTODIAN_ACTIONS = {"attempt_custodian_api_access"}
WITHDRAWAL_EXECUTION_ACTIONS = {
    "attempt_withdrawal_trigger",
    "attempt_withdrawal_approval",
}
POLICY_BLOCKED_ACTIONS = {
    "attempt_permission_change",
    "attempt_record_modification",
}
REVIEW_LIFECYCLE_BLOCKING_STATUSES = {
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
}
BLOCKED_AGENT_STATUSES = {"suspended", "revoked", "expired", "unknown"}

GUARD_SAFETY_NOTICE = (
    "Local deterministic agent sensitive action guard only. No real action was "
    "executed, no external system was called, no custody or blockchain action "
    "occurred, no withdrawal approval was granted, and no secret value was "
    "stored or exposed."
)


class AgentSensitiveActionGuardService:
    """Policy join for agent identity, passport, permissions, review, and status."""

    def list_rules(self) -> list[AgentSensitiveActionGuardRule]:
        return [
            AgentSensitiveActionGuardRule(
                rule_id="agent_status_must_be_active",
                description="Suspended, revoked, expired, or unknown agents cannot participate.",
                guard_decision="block_by_agent_status",
                applies_to_action_types=AGENT_SENSITIVE_ACTION_TYPES,
                requires_human_review=False,
                blocks_operation=True,
            ),
            AgentSensitiveActionGuardRule(
                rule_id="passport_must_be_valid_or_human_confirmed",
                description="Passport review findings pause sensitive participation until human review.",
                guard_decision="block_by_passport",
                applies_to_action_types=AGENT_SENSITIVE_ACTION_TYPES,
                requires_human_review=True,
                blocks_operation=True,
            ),
            AgentSensitiveActionGuardRule(
                rule_id="permission_policy_must_allow_action",
                description="Permission policy denial blocks the action inside the prototype.",
                guard_decision="block_by_permission_policy",
                applies_to_action_types=AGENT_SENSITIVE_ACTION_TYPES,
                requires_human_review=False,
                blocks_operation=True,
            ),
            AgentSensitiveActionGuardRule(
                rule_id="secret_custodian_and_withdrawal_execution_are_always_blocked",
                description="Secret access, custodian API access, and withdrawal execution cannot be performed by agents.",
                guard_decision="block_sensitive_action",
                applies_to_action_types=sorted(
                    SECRET_ACTIONS | CUSTODIAN_ACTIONS | WITHDRAWAL_EXECUTION_ACTIONS
                ),
                requires_human_review=False,
                blocks_operation=True,
            ),
            AgentSensitiveActionGuardRule(
                rule_id="active_review_or_revocation_context_blocks_participation",
                description="Active review cases or revocation audit context keep the operation paused.",
                guard_decision="block_by_review_case_status",
                applies_to_action_types=AGENT_SENSITIVE_ACTION_TYPES,
                requires_human_review=True,
                blocks_operation=True,
            ),
        ]

    def list_sensitive_actions(self) -> list[AgentSensitiveActionDefinition]:
        actions = []
        for action_type in AGENT_SENSITIVE_ACTION_TYPES:
            action = ACTION_TYPES[action_type]
            actions.append(
                AgentSensitiveActionDefinition(
                    sensitive_action_type=action.action_type,
                    default_permission_id=action.default_permission_id,
                    base_risk_score=action.base_risk_score,
                    sensitive=action.sensitive,
                    blocked_by_default=action.blocked_by_default,
                )
            )
        return actions

    def evaluate(
        self,
        request: AgentSensitiveActionGuardRequest,
    ) -> AgentSensitiveActionGuardResponse:
        created_at = datetime.now(timezone.utc).isoformat()
        agent_id = request.agent_id.strip().upper()
        action_type = request.sensitive_action_type.strip().lower()
        environment = request.environment.strip().lower() or "local"
        operation_type = request.operation_type.strip().lower() or (
            "generic_sensitive_operation"
        )
        resource_type = request.resource_type.strip().lower() or "generic_resource"
        action = self._get_action(action_type)
        permission_id = (
            request.permission_id.strip().lower()
            if request.permission_id
            else action.default_permission_id
        )

        agent = self._get_agent_or_none(agent_id)
        agent_status = agent.status if agent is not None else "unknown"
        passport_decision = "passport_missing"
        passport_valid = False
        permission_decision = "permission_not_evaluated"
        permission_reasons: list[str] = []

        if agent is not None:
            passport = agent_passport_service.validate_passport(agent.agent_id)
            passport_decision = passport.passport_decision
            passport_valid = passport.passport_valid
            if agent_status not in BLOCKED_AGENT_STATUSES:
                permission_response = agent_permissions_service.evaluate(
                    AgentPermissionEvaluationRequest(
                        agent_id=agent.agent_id,
                        permission_id=permission_id,
                        resource_type=resource_type,
                        resource_id=request.resource_id,
                        environment=environment,
                        action_context="agent_sensitive_action_guard",
                        reviewer_id=request.reviewer_id,
                    )
                )
                permission_decision = permission_response.decision
                permission_reasons = permission_response.blocking_reasons

        review_status = self._review_status(request.linked_review_case_id)
        guard_decision, blocking_reasons = self._guard_decision(
            agent_found=agent is not None,
            agent_status=agent_status,
            passport_decision=passport_decision,
            passport_valid=passport_valid,
            permission_decision=permission_decision,
            permission_reasons=permission_reasons,
            sensitive_action_type=action_type,
            environment=environment,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_review_case_id=request.linked_review_case_id,
            review_status=review_status,
            human_review_confirmed=request.human_review_confirmed,
            emergency_override_requested=request.emergency_override_requested,
        )

        allowed = guard_decision == "allow_agent_participation"
        human_review_required = guard_decision == "require_human_review"
        risk_score = self._risk_score(
            base_score=action.base_risk_score,
            amount_eur=request.amount_eur,
            environment=environment,
            agent_status=agent_status,
            permission_decision=permission_decision,
            guard_decision=guard_decision,
        )
        risk_level = self._risk_level(risk_score)
        audit_event_id = self._audit_event_id(agent_id, action_type)
        correlation_id = self._correlation_id(agent_id)
        review_case_required = (
            human_review_required
            or guard_decision == "block_by_review_case_status"
            or risk_level in {"high", "critical"}
        )
        evidence_required = risk_level in {"medium", "high", "critical"}

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_sensitive_action_guard",
            action="evaluate_agent_sensitive_action",
            object_type="agent_sensitive_action",
            object_id=f"{agent_id}:{action_type}",
            decision=guard_decision,
            severity=risk_level,
            risk_score=risk_score,
            summary="Agent sensitive action guard evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            evidence_reference=request.linked_evidence_package_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "agent_status": agent_status,
                "passport_decision": passport_decision,
                "permission_id": permission_id,
                "permission_decision": permission_decision,
                "sensitive_action_type": action_type,
                "operation_type": operation_type,
                "resource_type": resource_type,
                "resource_id": request.resource_id,
                "asset": request.asset,
                "destination_type": request.destination_type,
                "destination_id": request.destination_id,
                "environment": environment,
                "review_status": review_status,
                "blocking_reasons": blocking_reasons,
                "safety_notice": GUARD_SAFETY_NOTICE,
            },
        )

        return AgentSensitiveActionGuardResponse(
            agent_id=agent_id,
            agent_name=agent.agent_name if agent is not None else None,
            agent_type=agent.agent_type if agent is not None else None,
            agent_status=agent_status,
            sensitive_action_type=action_type,
            operation_type=operation_type,
            permission_id=permission_id,
            resource_type=resource_type,
            resource_id=request.resource_id,
            environment=environment,
            guard_decision=guard_decision,
            allowed=allowed,
            human_review_required=human_review_required,
            operation_paused=not allowed,
            sensitive_action_blocked=self._sensitive_action_blocked(
                guard_decision,
                action_type,
            ),
            secret_access_blocked=self._secret_access_blocked(
                guard_decision,
                action_type,
            ),
            custodian_access_blocked=self._custodian_access_blocked(
                guard_decision,
                action_type,
            ),
            withdrawal_execution_blocked=self._withdrawal_execution_blocked(
                guard_decision,
                action_type,
            ),
            external_tool_access_blocked=self._external_tool_access_blocked(
                guard_decision,
                action_type,
            ),
            passport_required=True,
            permission_evaluation_required=True,
            revocation_check_required=True,
            review_case_required=review_case_required,
            evidence_required=evidence_required,
            risk_score=risk_score,
            risk_level=risk_level,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            linked_review_case_id=request.linked_review_case_id,
            linked_evidence_package_id=request.linked_evidence_package_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            blocking_reasons=blocking_reasons,
            recommended_next_action=self._recommended_next_action(guard_decision),
            safety_notice=GUARD_SAFETY_NOTICE,
            created_at=created_at,
        )

    def evaluate_sensitive_approval_context(
        self,
        request: AgentSensitiveApprovalContextRequest,
    ) -> AgentSensitiveApprovalContextResponse:
        guard_request = AgentSensitiveActionGuardRequest(
            agent_id=request.agent_id,
            sensitive_action_type="request_sensitive_operation_approval",
            operation_type=request.operation_type,
            permission_id="request_sensitive_operation_approval",
            resource_type="sensitive_approval_request",
            resource_id=request.actor_id,
            amount_eur=request.amount_eur,
            asset=request.asset,
            destination_type=request.destination_type,
            destination_id=request.destination_id,
            environment="local",
            linked_review_case_id=request.linked_review_case_id,
            linked_evidence_package_id=request.linked_evidence_package_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            reviewer_id=request.reviewer_id,
            human_review_confirmed=False,
        )
        guard = self.evaluate(guard_request)
        recommendation = self._sensitive_approval_recommendation(guard)
        return AgentSensitiveApprovalContextResponse(
            agent_guard=guard,
            sensitive_approval_recommendation=recommendation,
            operation_paused_by_agent_guard=guard.operation_paused,
            operation_paused_until_human_review=guard.human_review_required,
            audit_event_id=guard.audit_event_id,
            correlation_id=guard.correlation_id,
            safety_notice=GUARD_SAFETY_NOTICE,
        )

    def _guard_decision(
        self,
        *,
        agent_found: bool,
        agent_status: str,
        passport_decision: str,
        passport_valid: bool,
        permission_decision: str,
        permission_reasons: list[str],
        sensitive_action_type: str,
        environment: str,
        linked_revocation_audit_event_id: str | None,
        linked_review_case_id: str | None,
        review_status: str | None,
        human_review_confirmed: bool,
        emergency_override_requested: bool,
    ) -> tuple[str, list[str]]:
        reasons: list[str] = []
        if linked_revocation_audit_event_id:
            reasons.append(
                "linked_revocation_audit_event_requires_human_governance_review"
            )

        if not agent_found:
            return "block_by_agent_status", reasons + ["agent_registration_not_found"]
        if agent_status in BLOCKED_AGENT_STATUSES:
            return "block_by_agent_status", reasons + [f"agent_status_{agent_status}"]
        if linked_revocation_audit_event_id:
            return "block_by_revocation_status", reasons
        if sensitive_action_type in SECRET_ACTIONS:
            return "block_secret_access", reasons + [
                "secret_access_prohibited_for_agents"
            ]
        if sensitive_action_type in CUSTODIAN_ACTIONS:
            return "block_custodian_access", reasons + [
                "custodian_access_prohibited_for_agents"
            ]
        if sensitive_action_type in WITHDRAWAL_EXECUTION_ACTIONS:
            return "block_withdrawal_execution", reasons + [
                "withdrawal_execution_prohibited_for_agents"
            ]
        if sensitive_action_type in POLICY_BLOCKED_ACTIONS:
            return "block_by_permission_policy", reasons + [
                "permission_or_record_modification_prohibited_for_agents"
            ]
        if environment == "production":
            return "block_sensitive_action", reasons + [
                "production_environment_prohibited"
            ]
        if linked_review_case_id and review_status in REVIEW_LIFECYCLE_BLOCKING_STATUSES:
            return "block_by_review_case_status", reasons + [
                f"linked_review_case_status_{review_status}"
            ]
        if not passport_valid and passport_decision == "passport_requires_review":
            reasons.append(f"agent_passport_{passport_decision}")
            if not human_review_confirmed:
                return "require_human_review", reasons
        elif not passport_valid:
            reasons.append(f"agent_passport_{passport_decision}")
            if not human_review_confirmed:
                return "block_by_passport", reasons
        if permission_decision in {
            "blocked_by_agent_status",
            "blocked_by_passport",
        }:
            return permission_decision, permission_reasons
        if permission_decision in {
            "blocked_by_policy",
            "blocked_sensitive_action",
            "blocked_custody_execution",
            "blocked_secret_access",
        }:
            return "block_by_permission_policy", permission_reasons
        if permission_decision in {"denied", "permission_not_evaluated"}:
            return "block_by_permission_policy", permission_reasons or [
                "permission_not_available"
            ]
        if emergency_override_requested:
            return "require_human_review", ["emergency_override_requires_review"]
        if permission_decision == "requires_human_approval" and not human_review_confirmed:
            return "require_human_review", ["human_review_required"]
        if not human_review_confirmed and sensitive_action_type.startswith("request_"):
            return "require_human_review", ["sensitive_request_requires_review"]
        return "allow_agent_participation", reasons

    def _risk_score(
        self,
        *,
        base_score: int,
        amount_eur: float,
        environment: str,
        agent_status: str,
        permission_decision: str,
        guard_decision: str,
    ) -> int:
        score = base_score
        if amount_eur >= 5000:
            score += 15
        elif amount_eur >= 1000:
            score += 8
        if environment == "production":
            score += 15
        if agent_status in BLOCKED_AGENT_STATUSES:
            score += 20
        if permission_decision != "allowed":
            score += 10
        if guard_decision.startswith("block"):
            score += 15
        elif guard_decision == "require_human_review":
            score += 8
        return min(score, 100)

    def _risk_level(self, risk_score: int) -> str:
        if risk_score <= 39:
            return "low"
        if risk_score <= 64:
            return "medium"
        if risk_score <= 84:
            return "high"
        return "critical"

    def _recommended_next_action(self, guard_decision: str) -> str:
        if guard_decision == "allow_agent_participation":
            return "continue_only_with_standard_sensitive_approval_controls_no_real_action_executed"
        if guard_decision == "require_human_review":
            return "pause_operation_and_route_agent_context_to_human_review"
        return "block_agent_participation_and_preserve_audit_trail"

    def _sensitive_approval_recommendation(
        self,
        guard: AgentSensitiveActionGuardResponse,
    ) -> str:
        if guard.allowed:
            return "continue_standard_approval"
        if guard.human_review_required:
            return "pause_for_agent_review"
        if guard.withdrawal_execution_blocked or guard.guard_decision in {
            "block_sensitive_action",
            "block_by_review_case_status",
        }:
            return "block_sensitive_operation"
        return "block_agent_sensitive_action"

    def _sensitive_action_blocked(
        self,
        guard_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return guard_decision.startswith("block") or sensitive_action_type in (
            SECRET_ACTIONS
            | CUSTODIAN_ACTIONS
            | WITHDRAWAL_EXECUTION_ACTIONS
            | POLICY_BLOCKED_ACTIONS
        )

    def _secret_access_blocked(
        self,
        guard_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return (
            guard_decision == "block_secret_access"
            or sensitive_action_type in SECRET_ACTIONS
        )

    def _custodian_access_blocked(
        self,
        guard_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return (
            guard_decision == "block_custodian_access"
            or sensitive_action_type in CUSTODIAN_ACTIONS
        )

    def _withdrawal_execution_blocked(
        self,
        guard_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return (
            guard_decision == "block_withdrawal_execution"
            or sensitive_action_type in WITHDRAWAL_EXECUTION_ACTIONS
        )

    def _external_tool_access_blocked(
        self,
        guard_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return guard_decision.startswith("block") or sensitive_action_type in (
            SECRET_ACTIONS | CUSTODIAN_ACTIONS | WITHDRAWAL_EXECUTION_ACTIONS
        )

    def _review_status(self, linked_review_case_id: str | None) -> str | None:
        if not linked_review_case_id:
            return None
        return review_case_service.get_lifecycle_status(linked_review_case_id)

    def _get_agent_or_none(self, agent_id: str) -> AgentRegistryDetail | None:
        try:
            return agent_registry_service.get_agent(agent_id)
        except ValueError:
            return None

    def _get_action(self, action_type: str):
        if action_type not in AGENT_SENSITIVE_ACTION_TYPES:
            raise ValueError("Agent sensitive action type was not found.")
        return ACTION_TYPES[action_type]

    def _audit_event_id(self, agent_id: str, sensitive_action_type: str) -> str:
        return (
            "AUD-AGENT-SENSITIVE-GUARD-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(sensitive_action_type)}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _slug(self, value: str) -> str:
        return value.strip().upper().replace("_", "-")


agent_sensitive_action_guard_service = AgentSensitiveActionGuardService()
