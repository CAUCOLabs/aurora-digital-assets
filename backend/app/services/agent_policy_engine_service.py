from datetime import datetime, timezone

from app.schemas.agent_permissions import AgentPermissionEvaluationRequest
from app.schemas.agent_policy_engine import (
    AgentPolicyContextRequest,
    AgentPolicyDecisionExplanationRequest,
    AgentPolicyDecisionExplanationResponse,
    AgentPolicyDecisionType,
    AgentPolicyDefinition,
    AgentPolicyEvaluationRequest,
    AgentPolicyEvaluationResponse,
)
from app.services.agent_passport_service import agent_passport_service
from app.services.agent_permissions_service import agent_permissions_service
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service
from app.services.review_case_service import review_case_service


POLICY_CATEGORIES = [
    ("identity_policy", "Validates local agent identity and registration status."),
    ("passport_policy", "Validates local agent passport decision state."),
    ("permission_policy", "Evaluates permission decision and permission risk."),
    ("sensitive_action_policy", "Blocks or pauses sensitive agent action types."),
    ("revocation_policy", "Applies linked revocation and revocation decision controls."),
    ("evidence_policy", "Requires evidence when risk or linked evidence context applies."),
    ("review_case_policy", "Applies linked review case lifecycle controls."),
    ("environment_policy", "Restricts production-like environments in the prototype."),
    ("emergency_override_policy", "Prevents emergency override bypass of blocked actions."),
    ("prototype_safety_policy", "Enforces local prototype safety boundaries."),
]

DECISION_TYPES = [
    ("policy_allow", False, "Policy allows the request."),
    ("policy_allow_with_audit", False, "Policy allows the request with audit recording."),
    ("policy_require_human_review", False, "Policy requires human review before continuing."),
    ("policy_pause_operation", True, "Policy pauses the operation pending review."),
    ("policy_block_agent", True, "Policy blocks the agent from participation."),
    ("policy_block_sensitive_action", True, "Policy blocks the sensitive action."),
    ("policy_block_secret_access", True, "Policy blocks secret access."),
    ("policy_block_custodian_access", True, "Policy blocks custodian access."),
    ("policy_block_withdrawal_execution", True, "Policy blocks withdrawal execution."),
    ("policy_block_external_tool_access", True, "Policy blocks external tool access."),
    ("policy_block_by_status", True, "Policy blocks because of agent status."),
    ("policy_block_by_passport", True, "Policy blocks because of passport state."),
    ("policy_block_by_revocation", True, "Policy blocks because of revocation context."),
    ("policy_block_by_review_case", True, "Policy blocks because of review case status."),
    ("policy_block_by_environment", True, "Policy blocks because of environment."),
    ("policy_block_emergency_override", True, "Policy blocks emergency override."),
    ("policy_invalid_context", True, "Policy input context is invalid or incomplete."),
]

DECISION_PRIORITY = [
    "policy_block_secret_access",
    "policy_block_withdrawal_execution",
    "policy_block_custodian_access",
    "policy_block_by_revocation",
    "policy_block_by_status",
    "policy_block_by_passport",
    "policy_block_by_review_case",
    "policy_block_by_environment",
    "policy_block_emergency_override",
    "policy_block_sensitive_action",
    "policy_pause_operation",
    "policy_require_human_review",
    "policy_allow_with_audit",
    "policy_allow",
]

BLOCKED_STATUSES = {"suspended", "revoked", "quarantined", "expired"}
SECRET_ACTIONS = {"attempt_secret_access"}
CUSTODIAN_ACTIONS = {"attempt_custodian_api_access"}
WITHDRAWAL_ACTIONS = {"attempt_withdrawal_trigger", "attempt_withdrawal_approval"}
SENSITIVE_BLOCKED_ACTIONS = {
    "attempt_permission_change",
    "attempt_record_modification",
}
HUMAN_REVIEW_ACTIONS = {
    "request_key_rotation",
    "request_data_export",
    "request_cloud_kubernetes_change",
    "request_sensitive_operation_approval",
}
PRODUCTION_LIKE_ENVIRONMENTS = {"production", "future_production"}
ACTIVE_REVIEW_STATUSES = {"open", "under_review"}
BLOCKING_REVOCATION_DECISIONS = {
    "revocation_required",
    "quarantine_required",
    "suspension_required",
}
STATUS_REVOCATION_DECISIONS = {"already_suspended", "already_revoked"}

BASE_RISK_SCORES = {
    "read_metadata": 25,
    "create_report": 35,
    "create_review_case": 45,
    "create_evidence_package": 45,
    "suggest_risk_decision": 55,
    "request_sensitive_operation_approval": 70,
    "request_data_export": 75,
    "request_key_rotation": 80,
    "request_custodian_integration_review": 75,
    "request_cloud_kubernetes_change": 80,
    "attempt_secret_access": 100,
    "attempt_custodian_api_access": 95,
    "attempt_withdrawal_trigger": 100,
    "attempt_withdrawal_approval": 100,
    "attempt_permission_change": 90,
    "attempt_record_modification": 90,
}

POLICY_SAFETY_NOTICE = (
    "Local deterministic agent policy evaluation only. No real action executed, "
    "no sensitive operation approved, no external API called, no secrets stored "
    "or exposed, and no custody, blockchain, or withdrawal execution occurred."
)

EXPLANATION_SAFETY_NOTICE = (
    "Audit-safe deterministic policy explanation only. No secrets are included, "
    "no secret material is stored or exposed, and no external system is called."
)


class AgentPolicyEngineService:
    """Central deterministic policy evaluator for local agent governance."""

    def list_policies(self) -> list[AgentPolicyDefinition]:
        return [
            AgentPolicyDefinition(policy_category=category, description=description)
            for category, description in POLICY_CATEGORIES
        ]

    def list_decision_types(self) -> list[AgentPolicyDecisionType]:
        return [
            AgentPolicyDecisionType(
                decision_type=decision,
                blocks_operation=blocks_operation,
                description=description,
            )
            for decision, blocks_operation, description in DECISION_TYPES
        ]

    def evaluate(
        self,
        request: AgentPolicyEvaluationRequest,
    ) -> AgentPolicyEvaluationResponse:
        agent_id = request.agent_id.strip().upper()
        policy_context = request.policy_context.strip().lower()
        requested_action = request.requested_action.strip().lower()
        sensitive_action_type = (
            request.sensitive_action_type.strip().lower()
            if request.sensitive_action_type
            else requested_action
        )
        environment = request.environment.strip().lower() or "local"
        agent_status = (request.agent_status or self._agent_status(agent_id)).strip().lower()
        passport_decision = (
            request.passport_decision or self._passport_decision(agent_id)
        ).strip().lower()
        permission_decision = (
            request.permission_decision
            or self._permission_decision(
                agent_id=agent_id,
                permission_id=request.permission_id,
                resource_type=request.resource_type,
                resource_id=request.resource_id,
                environment=environment,
                reviewer_id=request.reviewer_id,
            )
        ).strip().lower()
        linked_review_case_status = (
            request.linked_review_case_status
            or self._review_case_status(request.linked_review_case_id)
        )
        if linked_review_case_status is not None:
            linked_review_case_status = linked_review_case_status.strip().lower()
        revocation_decision = (
            request.revocation_decision.strip().lower()
            if request.revocation_decision
            else None
        )

        risk_score = self._risk_score(
            requested_action=requested_action,
            sensitive_action_type=sensitive_action_type,
            agent_status=agent_status,
            passport_decision=passport_decision,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_review_case_status=linked_review_case_status,
            emergency_override_requested=request.emergency_override_requested,
            environment=environment,
            amount_eur=request.amount_eur,
        )
        risk_level = self._risk_level(risk_score)

        candidates, applied_policies, blocking_reasons = self._candidate_decisions(
            agent_status=agent_status,
            passport_decision=passport_decision,
            permission_decision=permission_decision,
            sensitive_action_type=sensitive_action_type,
            revocation_decision=revocation_decision,
            linked_review_case_status=linked_review_case_status,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_evidence_package_id=request.linked_evidence_package_id,
            environment=environment,
            emergency_override_requested=request.emergency_override_requested,
            human_review_confirmed=request.human_review_confirmed,
            risk_level=risk_level,
        )

        if not candidates:
            candidates.append("policy_allow_with_audit")
            applied_policies.append("prototype_safety_policy")

        policy_decision = self._strongest_decision(candidates)
        allowed = policy_decision in {"policy_allow", "policy_allow_with_audit"}
        operation_paused = not allowed
        human_review_required = policy_decision == "policy_require_human_review"
        audit_required = True
        evidence_required = (
            risk_level in {"high", "critical"}
            or request.linked_evidence_package_id is not None
            or not allowed
        )
        review_case_required = (
            risk_level == "critical"
            or policy_decision in {
                "policy_require_human_review",
                "policy_pause_operation",
                "policy_block_by_review_case",
                "policy_block_by_revocation",
            }
        )
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event_id = self._audit_event_id(agent_id, requested_action)
        correlation_id = self._correlation_id(agent_id)

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_policy_engine",
            action="evaluate_agent_policy",
            object_type="agent_policy_evaluation",
            object_id=f"{agent_id}:{requested_action}",
            decision=policy_decision,
            severity=risk_level,
            risk_score=risk_score,
            summary="Agent policy evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            evidence_reference=request.linked_evidence_package_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "policy_context": policy_context,
                "requested_action": requested_action,
                "permission_id": request.permission_id,
                "permission_decision": permission_decision,
                "sensitive_action_type": sensitive_action_type,
                "agent_status": agent_status,
                "passport_decision": passport_decision,
                "revocation_decision": revocation_decision,
                "linked_review_case_status": linked_review_case_status,
                "linked_revocation_audit_event_id": (
                    request.linked_revocation_audit_event_id
                ),
                "environment": environment,
                "applied_policies": applied_policies,
                "blocking_reasons": blocking_reasons,
                "safety_notice": POLICY_SAFETY_NOTICE,
            },
        )

        return AgentPolicyEvaluationResponse(
            agent_id=agent_id,
            policy_context=policy_context,
            requested_action=requested_action,
            environment=environment,
            policy_decision=policy_decision,
            allowed=allowed,
            operation_paused=operation_paused,
            human_review_required=human_review_required,
            audit_required=audit_required,
            evidence_required=evidence_required,
            review_case_required=review_case_required,
            sensitive_action_blocked=self._sensitive_action_blocked(
                policy_decision,
                sensitive_action_type,
            ),
            secret_access_blocked=self._secret_access_blocked(
                policy_decision,
                sensitive_action_type,
            ),
            custodian_access_blocked=self._custodian_access_blocked(
                policy_decision,
                sensitive_action_type,
            ),
            withdrawal_execution_blocked=self._withdrawal_execution_blocked(
                policy_decision,
                sensitive_action_type,
            ),
            external_tool_access_blocked=self._external_tool_access_blocked(
                policy_decision,
                sensitive_action_type,
            ),
            emergency_override_blocked=self._emergency_override_blocked(
                policy_decision,
                request.emergency_override_requested,
                blocking_reasons,
            ),
            risk_score=risk_score,
            risk_level=risk_level,
            applied_policies=self._dedupe(applied_policies),
            blocking_reasons=self._dedupe(blocking_reasons),
            recommended_next_actions=self._recommended_next_actions(policy_decision),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            safety_notice=POLICY_SAFETY_NOTICE,
            created_at=created_at,
        )

    def evaluate_context(
        self,
        request: AgentPolicyContextRequest,
    ) -> AgentPolicyEvaluationResponse:
        return self.evaluate(
            AgentPolicyEvaluationRequest(
                agent_id=request.agent_id,
                policy_context=request.context_type,
                requested_action=request.requested_action,
                permission_id=request.permission_id,
                resource_type=request.resource_type,
                resource_id=request.resource_id,
                environment=request.environment,
                sensitive_action_type=request.sensitive_action_type,
                linked_review_case_id=request.linked_review_case_id,
                linked_evidence_package_id=request.linked_evidence_package_id,
                linked_revocation_audit_event_id=(
                    request.linked_revocation_audit_event_id
                ),
                amount_eur=request.amount_eur,
                emergency_override_requested=request.emergency_override_requested,
                human_review_confirmed=request.human_review_confirmed,
                reviewer_id=request.reviewer_id,
            )
        )

    def explain_decision(
        self,
        request: AgentPolicyDecisionExplanationRequest,
    ) -> AgentPolicyDecisionExplanationResponse:
        policy_decision = request.policy_decision.strip().lower()
        return AgentPolicyDecisionExplanationResponse(
            policy_decision=policy_decision,
            explanation=self._explanation(policy_decision, request.requested_action),
            blocking_reasons=request.blocking_reasons,
            applied_policies=request.applied_policies,
            recommended_next_actions=self._recommended_next_actions(policy_decision),
            safety_notice=EXPLANATION_SAFETY_NOTICE,
            audit_safe=True,
            no_secret_material_included=True,
        )

    def _candidate_decisions(
        self,
        *,
        agent_status: str,
        passport_decision: str,
        permission_decision: str,
        sensitive_action_type: str,
        revocation_decision: str | None,
        linked_review_case_status: str | None,
        linked_revocation_audit_event_id: str | None,
        linked_evidence_package_id: str | None,
        environment: str,
        emergency_override_requested: bool,
        human_review_confirmed: bool,
        risk_level: str,
    ) -> tuple[list[str], list[str], list[str]]:
        candidates: list[str] = []
        applied: list[str] = []
        reasons: list[str] = []

        applied.append("identity_policy")
        if agent_status == "unknown":
            candidates.append("policy_invalid_context")
            reasons.append("agent_context_unknown")
        elif agent_status in BLOCKED_STATUSES:
            candidates.append("policy_block_by_status")
            reasons.append(f"agent_status_{agent_status}")

        applied.append("passport_policy")
        if passport_decision in {"passport_status_blocked", "passport_invalid_agent"}:
            candidates.append("policy_block_by_passport")
            reasons.append(f"agent_passport_{passport_decision}")
        elif passport_decision == "passport_requires_review" and not human_review_confirmed:
            candidates.append("policy_require_human_review")
            reasons.append("agent_passport_requires_review")

        applied.append("permission_policy")
        if permission_decision == "blocked_secret_access":
            candidates.append("policy_block_secret_access")
            reasons.append("secrets_access_prohibited")
        elif permission_decision == "blocked_custody_execution":
            candidates.append("policy_block_custodian_access")
            reasons.append("custodian_access_prohibited")
        elif permission_decision == "blocked_sensitive_action":
            candidates.append("policy_block_sensitive_action")
            reasons.append("sensitive_action_prohibited")
        elif permission_decision == "blocked_by_agent_status":
            candidates.append("policy_block_by_status")
            reasons.append("permission_blocked_by_agent_status")
        elif permission_decision == "blocked_by_passport":
            candidates.append("policy_block_by_passport")
            reasons.append("permission_blocked_by_passport")
        elif permission_decision == "requires_human_approval" and not human_review_confirmed:
            candidates.append("policy_require_human_review")
            reasons.append("permission_requires_human_approval")

        applied.append("sensitive_action_policy")
        if sensitive_action_type in SECRET_ACTIONS:
            candidates.append("policy_block_secret_access")
            reasons.append("secrets_access_prohibited")
        elif sensitive_action_type in CUSTODIAN_ACTIONS:
            candidates.append("policy_block_custodian_access")
            reasons.append("custodian_access_prohibited")
        elif sensitive_action_type in WITHDRAWAL_ACTIONS:
            candidates.append("policy_block_withdrawal_execution")
            reasons.append("withdrawal_execution_prohibited")
        elif sensitive_action_type in SENSITIVE_BLOCKED_ACTIONS:
            candidates.append("policy_block_sensitive_action")
            reasons.append("sensitive_action_prohibited")
        elif sensitive_action_type in HUMAN_REVIEW_ACTIONS and not human_review_confirmed:
            candidates.append("policy_require_human_review")
            reasons.append("sensitive_action_requires_human_review")

        applied.append("revocation_policy")
        if linked_revocation_audit_event_id:
            candidates.append("policy_block_by_revocation")
            reasons.append("linked_revocation_audit_event")
        if revocation_decision in BLOCKING_REVOCATION_DECISIONS:
            candidates.append("policy_block_by_revocation")
            reasons.append(f"revocation_decision_{revocation_decision}")
        elif revocation_decision in STATUS_REVOCATION_DECISIONS:
            candidates.append("policy_block_by_status")
            reasons.append(f"revocation_decision_{revocation_decision}")

        if linked_evidence_package_id:
            applied.append("evidence_policy")

        if linked_review_case_status:
            applied.append("review_case_policy")
            if (
                linked_review_case_status in ACTIVE_REVIEW_STATUSES
                and risk_level == "critical"
            ):
                candidates.append("policy_block_by_review_case")
                reasons.append(f"linked_review_case_status_{linked_review_case_status}")
            elif linked_review_case_status in {"mitigated", "closed"}:
                candidates.append("policy_allow_with_audit")

        applied.append("environment_policy")
        if environment in PRODUCTION_LIKE_ENVIRONMENTS:
            if sensitive_action_type in {"request_cloud_kubernetes_change"}:
                candidates.append("policy_block_by_environment")
                reasons.append(f"environment_{environment}_blocked")
            elif not human_review_confirmed:
                candidates.append("policy_require_human_review")
                reasons.append(f"environment_{environment}_requires_review")

        if emergency_override_requested:
            applied.append("emergency_override_policy")
            reasons.append("emergency_override_not_allowed")
            if any(candidate.startswith("policy_block") for candidate in candidates):
                candidates.append("policy_block_emergency_override")
            elif not human_review_confirmed:
                candidates.append("policy_require_human_review")

        applied.append("prototype_safety_policy")
        if sensitive_action_type in SECRET_ACTIONS:
            candidates.append("policy_block_secret_access")
        elif sensitive_action_type in CUSTODIAN_ACTIONS:
            candidates.append("policy_block_custodian_access")
        elif sensitive_action_type in WITHDRAWAL_ACTIONS:
            candidates.append("policy_block_withdrawal_execution")
        elif sensitive_action_type in SENSITIVE_BLOCKED_ACTIONS:
            candidates.append("policy_block_sensitive_action")
        elif environment in PRODUCTION_LIKE_ENVIRONMENTS and sensitive_action_type in {
            "request_cloud_kubernetes_change",
        }:
            candidates.append("policy_block_by_environment")

        return candidates, self._dedupe(applied), self._dedupe(reasons)

    def _risk_score(
        self,
        *,
        requested_action: str,
        sensitive_action_type: str,
        agent_status: str,
        passport_decision: str,
        linked_revocation_audit_event_id: str | None,
        linked_review_case_status: str | None,
        emergency_override_requested: bool,
        environment: str,
        amount_eur: float,
    ) -> int:
        score = BASE_RISK_SCORES.get(
            sensitive_action_type,
            BASE_RISK_SCORES.get(requested_action, 50),
        )
        if agent_status in BLOCKED_STATUSES:
            score += 25
        if passport_decision in {"passport_status_blocked", "passport_invalid_agent"}:
            score += 20
        if linked_revocation_audit_event_id:
            score += 20
        if linked_review_case_status in ACTIVE_REVIEW_STATUSES:
            score += 20
        if emergency_override_requested:
            score += 15
        if environment in PRODUCTION_LIKE_ENVIRONMENTS:
            score += 15
        if amount_eur > 5000:
            score += 10
        return min(score, 100)

    def _risk_level(self, risk_score: int) -> str:
        if risk_score <= 39:
            return "low"
        if risk_score <= 64:
            return "medium"
        if risk_score <= 84:
            return "high"
        return "critical"

    def _strongest_decision(self, candidates: list[str]) -> str:
        for decision in DECISION_PRIORITY:
            if decision in candidates:
                return decision
        if "policy_invalid_context" in candidates:
            return "policy_invalid_context"
        return "policy_allow"

    def _sensitive_action_blocked(
        self,
        policy_decision: str,
        sensitive_action_type: str,
    ) -> bool:
        return policy_decision.startswith("policy_block") or sensitive_action_type in (
            SECRET_ACTIONS | CUSTODIAN_ACTIONS | WITHDRAWAL_ACTIONS | SENSITIVE_BLOCKED_ACTIONS
        )

    def _secret_access_blocked(self, policy_decision: str, action: str) -> bool:
        return policy_decision == "policy_block_secret_access" or action in SECRET_ACTIONS

    def _custodian_access_blocked(self, policy_decision: str, action: str) -> bool:
        return (
            policy_decision == "policy_block_custodian_access"
            or action in CUSTODIAN_ACTIONS
        )

    def _withdrawal_execution_blocked(self, policy_decision: str, action: str) -> bool:
        return (
            policy_decision == "policy_block_withdrawal_execution"
            or action in WITHDRAWAL_ACTIONS
        )

    def _external_tool_access_blocked(self, policy_decision: str, action: str) -> bool:
        return policy_decision.startswith("policy_block") or action in (
            SECRET_ACTIONS | CUSTODIAN_ACTIONS | WITHDRAWAL_ACTIONS
        )

    def _emergency_override_blocked(
        self,
        policy_decision: str,
        emergency_override_requested: bool,
        blocking_reasons: list[str],
    ) -> bool:
        return emergency_override_requested and (
            policy_decision.startswith("policy_block")
            or "emergency_override_not_allowed" in blocking_reasons
        )

    def _recommended_next_actions(self, policy_decision: str) -> list[str]:
        if policy_decision in {"policy_allow", "policy_allow_with_audit"}:
            return ["record_policy_audit_event_only_no_real_action_executed"]
        if policy_decision == "policy_require_human_review":
            return ["pause_operation_and_route_to_human_review"]
        if policy_decision == "policy_invalid_context":
            return ["verify_agent_identity_and_policy_context_before_retry"]
        return ["block_request_and_preserve_audit_trail"]

    def _explanation(self, policy_decision: str, requested_action: str | None) -> str:
        action = requested_action or "requested action"
        if policy_decision == "policy_block_secret_access":
            return f"Policy blocked secret access for {action} in the local prototype."
        if policy_decision == "policy_block_custodian_access":
            return f"Policy blocked custodian access for {action} in the local prototype."
        if policy_decision == "policy_block_withdrawal_execution":
            return f"Policy blocked withdrawal execution for {action} in the local prototype."
        if policy_decision == "policy_require_human_review":
            return f"Policy requires human review before {action} can continue."
        if policy_decision in {"policy_allow", "policy_allow_with_audit"}:
            return f"Policy allows {action} with deterministic audit controls."
        return f"Policy decision {policy_decision} was applied to {action}."

    def _agent_status(self, agent_id: str) -> str:
        try:
            return agent_registry_service.get_agent(agent_id).status
        except ValueError:
            return "unknown"

    def _passport_decision(self, agent_id: str) -> str:
        try:
            return agent_passport_service.validate_passport(agent_id).passport_decision
        except ValueError:
            return "passport_missing"

    def _permission_decision(
        self,
        *,
        agent_id: str,
        permission_id: str | None,
        resource_type: str,
        resource_id: str | None,
        environment: str,
        reviewer_id: str,
    ) -> str:
        if permission_id is None:
            return "not_evaluated"
        try:
            return agent_permissions_service.evaluate(
                AgentPermissionEvaluationRequest(
                    agent_id=agent_id,
                    permission_id=permission_id,
                    resource_type=resource_type,
                    resource_id=resource_id,
                    environment=environment,
                    action_context="agent_policy_engine",
                    reviewer_id=reviewer_id,
                )
            ).decision
        except ValueError:
            return "not_evaluated"

    def _review_case_status(self, case_id: str | None) -> str | None:
        if case_id is None:
            return None
        return review_case_service.get_lifecycle_status(case_id)

    def _audit_event_id(self, agent_id: str, requested_action: str) -> str:
        return (
            "AUD-AGENT-POLICY-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(requested_action)}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _slug(self, value: str) -> str:
        return value.strip().upper().replace("_", "-")

    def _dedupe(self, values: list[str]) -> list[str]:
        deduped = []
        for value in values:
            if value not in deduped:
                deduped.append(value)
        return deduped


agent_policy_engine_service = AgentPolicyEngineService()
