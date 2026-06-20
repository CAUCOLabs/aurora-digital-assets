from datetime import datetime, timezone

from app.schemas.agent_actions import (
    AgentActionRecordRequest,
    AgentActionRecordResponse,
    AgentActionTypeDefinition,
)
from app.schemas.agent_permissions import AgentPermissionEvaluationRequest
from app.schemas.agent_registry import AgentRegistryDetail
from app.services.agent_passport_service import agent_passport_service
from app.services.agent_permissions_service import (
    PERMISSION_CATALOG,
    agent_permissions_service,
)
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service


ACTION_SAFETY_NOTICE = (
    "Local deterministic action audit only. No real action executed. No "
    "external API called. No secrets stored or exposed. No custody, blockchain, "
    "or withdrawal execution performed."
)

ACTION_OUTCOMES = {
    "allowed",
    "denied",
    "requires_human_approval",
    "blocked_by_agent_status",
    "blocked_by_passport",
    "blocked_by_permission_policy",
    "blocked_sensitive_action",
    "blocked_secret_access",
    "blocked_custody_execution",
    "recorded_only",
}

BLOCKED_AGENT_STATUSES = {"suspended", "revoked", "expired"}
SECRET_ACTIONS = {"attempt_secret_access"}
CUSTODY_ACTIONS = {"attempt_custodian_api_access"}
SENSITIVE_BLOCKED_ACTIONS = {
    "attempt_withdrawal_trigger",
    "attempt_withdrawal_approval",
}
POLICY_BLOCKED_ACTIONS = {
    "attempt_permission_change",
    "attempt_record_modification",
}


def _action_type(
    action_type: str,
    label: str,
    default_permission_id: str,
    base_risk_score: int,
    *,
    sensitive: bool = False,
    blocked_by_default: bool = False,
) -> AgentActionTypeDefinition:
    return AgentActionTypeDefinition(
        action_type=action_type,
        label=label,
        default_permission_id=default_permission_id,
        base_risk_score=base_risk_score,
        sensitive=sensitive,
        blocked_by_default=blocked_by_default,
    )


ACTION_TYPES = {
    "read_audit_event": _action_type(
        "read_audit_event",
        "Read audit event",
        "read_audit_events",
        25,
    ),
    "read_evidence_package": _action_type(
        "read_evidence_package",
        "Read evidence package",
        "access_compliance_evidence",
        35,
    ),
    "read_review_case": _action_type(
        "read_review_case",
        "Read review case",
        "create_review_cases",
        35,
    ),
    "create_report": _action_type(
        "create_report",
        "Create report",
        "create_reports",
        35,
    ),
    "create_review_case": _action_type(
        "create_review_case",
        "Create review case",
        "create_review_cases",
        45,
    ),
    "create_evidence_package": _action_type(
        "create_evidence_package",
        "Create evidence package",
        "create_evidence_packages",
        45,
    ),
    "suggest_risk_decision": _action_type(
        "suggest_risk_decision",
        "Suggest risk decision",
        "suggest_risk_decisions",
        55,
        sensitive=True,
    ),
    "request_sensitive_operation_approval": _action_type(
        "request_sensitive_operation_approval",
        "Request sensitive operation approval",
        "request_sensitive_operation_approval",
        70,
        sensitive=True,
    ),
    "request_data_export": _action_type(
        "request_data_export",
        "Request data export",
        "export_data",
        75,
        sensitive=True,
    ),
    "request_key_rotation": _action_type(
        "request_key_rotation",
        "Request key rotation",
        "rotate_keys",
        80,
        sensitive=True,
    ),
    "request_custodian_integration_review": _action_type(
        "request_custodian_integration_review",
        "Request custodian integration review",
        "access_compliance_evidence",
        75,
        sensitive=True,
    ),
    "request_cloud_kubernetes_change": _action_type(
        "request_cloud_kubernetes_change",
        "Request cloud Kubernetes change",
        "change_cloud_kubernetes_configuration",
        80,
        sensitive=True,
    ),
    "attempt_secret_access": _action_type(
        "attempt_secret_access",
        "Attempt secret access",
        "access_secrets",
        100,
        sensitive=True,
        blocked_by_default=True,
    ),
    "attempt_custodian_api_access": _action_type(
        "attempt_custodian_api_access",
        "Attempt custodian API access",
        "access_custodian_apis",
        95,
        sensitive=True,
        blocked_by_default=True,
    ),
    "attempt_withdrawal_trigger": _action_type(
        "attempt_withdrawal_trigger",
        "Attempt withdrawal trigger",
        "trigger_withdrawals",
        100,
        sensitive=True,
        blocked_by_default=True,
    ),
    "attempt_withdrawal_approval": _action_type(
        "attempt_withdrawal_approval",
        "Attempt withdrawal approval",
        "approve_withdrawals",
        100,
        sensitive=True,
        blocked_by_default=True,
    ),
    "attempt_permission_change": _action_type(
        "attempt_permission_change",
        "Attempt permission change",
        "modify_user_permissions",
        90,
        sensitive=True,
        blocked_by_default=True,
    ),
    "attempt_record_modification": _action_type(
        "attempt_record_modification",
        "Attempt record modification",
        "delete_or_modify_records",
        90,
        sensitive=True,
        blocked_by_default=True,
    ),
}


class AgentActionsService:
    """Deterministic audit layer for prototype agent action attempts."""

    def __init__(self) -> None:
        self._events: dict[str, AgentActionRecordResponse] = {}
        self._seed_demo_events()

    def list_action_types(self) -> list[AgentActionTypeDefinition]:
        return [ACTION_TYPES[action_type] for action_type in sorted(ACTION_TYPES)]

    def list_recent(self) -> list[AgentActionRecordResponse]:
        self._seed_demo_events()
        return sorted(
            self._events.values(),
            key=lambda event: event.created_at,
            reverse=True,
        )

    def get_event(self, action_event_id: str) -> AgentActionRecordResponse:
        self._seed_demo_events()
        event = self._events.get(action_event_id.strip().upper())
        if event is None:
            raise ValueError("Agent action event was not found.")
        return event

    def record(self, request: AgentActionRecordRequest) -> AgentActionRecordResponse:
        agent = self._get_agent(request.agent_id)
        action = self._get_action_type(request.action_type)
        self._validate_permission(request.permission_id)
        passport = agent_passport_service.validate_passport(agent.agent_id)
        permission_decision = request.declared_outcome or "recorded_only"
        outcome, reasons = self._enforced_action_outcome(
            agent=agent,
            action_type=action.action_type,
            permission_decision=permission_decision,
            permission_reasons=[],
        )
        response = self._build_response(
            agent=agent,
            passport_id=passport.passport_id,
            request=request,
            permission_decision=permission_decision,
            action_outcome=outcome,
            blocking_reasons=reasons,
            audit_event_created=False,
        )
        return self._record_audit_event(
            response=response,
            reviewer_id=request.reviewer_id,
        )

    def evaluate_and_record(
        self,
        request: AgentActionRecordRequest,
    ) -> AgentActionRecordResponse:
        agent = self._get_agent(request.agent_id)
        action = self._get_action_type(request.action_type)
        self._validate_permission(request.permission_id)
        permission_response = agent_permissions_service.evaluate(
            AgentPermissionEvaluationRequest(
                agent_id=request.agent_id,
                permission_id=request.permission_id,
                resource_type=request.resource_type,
                resource_id=request.resource_id,
                environment=request.environment,
                action_context=request.action_context,
                reviewer_id=request.reviewer_id,
            )
        )
        outcome, reasons = self._enforced_action_outcome(
            agent=agent,
            action_type=action.action_type,
            permission_decision=permission_response.decision,
            permission_reasons=permission_response.blocking_reasons,
        )
        response = self._build_response(
            agent=agent,
            passport_id=permission_response.passport_id,
            request=request,
            permission_decision=permission_response.decision,
            action_outcome=outcome,
            blocking_reasons=reasons,
            audit_event_created=False,
        )
        return self._record_audit_event(
            response=response,
            reviewer_id=request.reviewer_id,
        )

    def _seed_demo_events(self) -> None:
        if self._events:
            return
        demo_requests = [
            AgentActionRecordRequest(
                agent_id="AGENT-COMPLIANCE-ASSISTANT-001",
                action_type="read_audit_event",
                permission_id="read_audit_events",
                resource_type="audit_event",
                resource_id="AUD-DEMO",
                request_id="REQ-DEMO-AGENT-ACTION-001",
                declared_outcome="allowed",
            ),
            AgentActionRecordRequest(
                agent_id="AGENT-RISK-ANALYST-001",
                action_type="request_sensitive_operation_approval",
                permission_id="request_sensitive_operation_approval",
                resource_type="sensitive_operation",
                resource_id="SOP-DEMO",
                request_id="REQ-DEMO-AGENT-ACTION-002",
                declared_outcome="requires_human_approval",
            ),
            AgentActionRecordRequest(
                agent_id="AGENT-CUSTODIAN-INTEGRATION-001",
                action_type="attempt_custodian_api_access",
                permission_id="access_custodian_apis",
                resource_type="future_custodian_api",
                resource_id="CUSTODIAN-DEMO",
                request_id="REQ-DEMO-AGENT-ACTION-003",
                declared_outcome="blocked_by_agent_status",
            ),
        ]
        for request in demo_requests:
            event = self._build_demo_event(request)
            self._events[event.action_event_id] = event

    def _build_demo_event(
        self,
        request: AgentActionRecordRequest,
    ) -> AgentActionRecordResponse:
        agent = self._get_agent(request.agent_id)
        passport = agent_passport_service.validate_passport(agent.agent_id)
        action = self._get_action_type(request.action_type)
        outcome, reasons = self._enforced_action_outcome(
            agent=agent,
            action_type=action.action_type,
            permission_decision=request.declared_outcome or "recorded_only",
            permission_reasons=[],
        )
        return self._build_response(
            agent=agent,
            passport_id=passport.passport_id,
            request=request,
            permission_decision=request.declared_outcome or "recorded_only",
            action_outcome=outcome,
            blocking_reasons=reasons,
            audit_event_created=False,
            created_at="2026-06-20T00:00:00+00:00",
        )

    def _build_response(
        self,
        *,
        agent: AgentRegistryDetail,
        passport_id: str | None,
        request: AgentActionRecordRequest,
        permission_decision: str,
        action_outcome: str,
        blocking_reasons: list[str],
        audit_event_created: bool,
        created_at: str | None = None,
    ) -> AgentActionRecordResponse:
        action = self._get_action_type(request.action_type)
        risk_score = self._risk_score(
            action=action,
            permission_id=request.permission_id,
            permission_decision=permission_decision,
            agent_status=agent.status,
            environment=request.environment,
        )
        risk_level = self._risk_level(risk_score)
        audit_event_id = self._audit_event_id(agent.agent_id, action.action_type)
        return AgentActionRecordResponse(
            action_event_id=self._action_event_id(
                agent.agent_id,
                action.action_type,
            ),
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            agent_status=agent.status,
            passport_id=passport_id,
            permission_id=request.permission_id,
            action_type=action.action_type,
            resource_type=request.resource_type,
            resource_id=request.resource_id,
            environment=request.environment,
            request_id=request.request_id,
            source_context=request.source_context,
            permission_decision=permission_decision,
            action_outcome=action_outcome,
            allowed=action_outcome == "allowed",
            human_approval_required=action_outcome == "requires_human_approval",
            evidence_required=self._evidence_required(risk_level),
            review_case_required=self._review_case_required(risk_level),
            risk_score=risk_score,
            risk_level=risk_level,
            audit_event_created=audit_event_created,
            audit_event_id=audit_event_id,
            correlation_id=self._correlation_id(agent.agent_id),
            evidence_package_id=self._evidence_package_id(
                audit_event_id,
                risk_level,
            ),
            review_case_id=self._review_case_id(
                agent.agent_id,
                action.action_type,
                risk_level,
                action_outcome,
            ),
            blocking_reasons=blocking_reasons,
            recommended_next_action=self._recommended_next_action(action_outcome),
            safety_notice=ACTION_SAFETY_NOTICE,
            created_at=created_at or datetime.now(timezone.utc).isoformat(),
        )

    def _record_audit_event(
        self,
        *,
        response: AgentActionRecordResponse,
        reviewer_id: str,
    ) -> AgentActionRecordResponse:
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=response.audit_event_id,
            actor_id=reviewer_id,
            actor_type="staff",
            source_module="agent_actions",
            action="record_agent_action_attempt",
            object_type="agent_action",
            object_id=response.action_event_id,
            decision=response.action_outcome,
            severity=response.risk_level,
            risk_score=response.risk_score,
            summary="Agent action attempt recorded in local deterministic prototype.",
            correlation_id=response.correlation_id,
            evidence_reference=response.evidence_package_id,
            review_case_id=response.review_case_id,
            metadata={
                "agent_id": response.agent_id,
                "agent_type": response.agent_type,
                "agent_status": response.agent_status,
                "permission_id": response.permission_id,
                "permission_decision": response.permission_decision,
                "action_type": response.action_type,
                "resource_type": response.resource_type,
                "resource_id": response.resource_id,
                "request_id": response.request_id,
                "source_context": response.source_context,
                "blocking_reasons": response.blocking_reasons,
                "safety_notice": response.safety_notice,
            },
        )
        recorded = response.model_copy(
            update={"audit_event_created": audit_event is not None}
        )
        self._events[recorded.action_event_id] = recorded
        return recorded

    def _enforced_action_outcome(
        self,
        *,
        agent: AgentRegistryDetail,
        action_type: str,
        permission_decision: str,
        permission_reasons: list[str],
    ) -> tuple[str, list[str]]:
        if agent.status in BLOCKED_AGENT_STATUSES:
            return "blocked_by_agent_status", [f"agent_status_{agent.status}"]
        if action_type in SECRET_ACTIONS:
            return "blocked_secret_access", ["secrets_access_prohibited"]
        if action_type in CUSTODY_ACTIONS:
            return "blocked_custody_execution", ["custodian_api_access_prohibited"]
        if action_type in SENSITIVE_BLOCKED_ACTIONS:
            return "blocked_sensitive_action", ["agent_sensitive_action_prohibited"]
        if action_type in POLICY_BLOCKED_ACTIONS:
            return "blocked_by_permission_policy", [
                "permission_or_record_modification_prohibited"
            ]
        if permission_decision == "blocked_by_policy":
            return "blocked_by_permission_policy", permission_reasons
        if permission_decision in ACTION_OUTCOMES:
            return permission_decision, permission_reasons
        return "recorded_only", permission_reasons

    def _risk_score(
        self,
        *,
        action: AgentActionTypeDefinition,
        permission_id: str,
        permission_decision: str,
        agent_status: str,
        environment: str,
    ) -> int:
        score = action.base_risk_score
        if permission_decision != "allowed":
            score += 10
        if agent_status in BLOCKED_AGENT_STATUSES:
            score += 20
        if environment.strip().lower() == "production":
            score += 15
        permission = PERMISSION_CATALOG.get(permission_id.strip().lower())
        if permission is not None and permission.risk_level == "critical":
            score += 15
        elif permission is not None and permission.risk_level == "high":
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

    def _evidence_required(self, risk_level: str) -> bool:
        return risk_level in {"medium", "high", "critical"}

    def _review_case_required(self, risk_level: str) -> bool:
        return risk_level in {"high", "critical"}

    def _evidence_package_id(
        self,
        audit_event_id: str,
        risk_level: str,
    ) -> str | None:
        if risk_level in {"high", "critical"}:
            return f"EP-FROM-{audit_event_id}"
        return None

    def _review_case_id(
        self,
        agent_id: str,
        action_type: str,
        risk_level: str,
        action_outcome: str,
    ) -> str | None:
        if risk_level != "critical" or action_outcome == "allowed":
            return None
        return (
            "CASE-AGENT-ACTION-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(action_type)}"
        )

    def _recommended_next_action(self, action_outcome: str) -> str:
        if action_outcome == "allowed":
            return "record_action_audit_event_only_no_real_action_executed"
        if action_outcome == "requires_human_approval":
            return "route_agent_action_to_human_review_before_any_action"
        return "block_agent_action_attempt_and_preserve_audit_trail"

    def _get_agent(self, agent_id: str) -> AgentRegistryDetail:
        return agent_registry_service.get_agent(agent_id)

    def _get_action_type(self, action_type: str) -> AgentActionTypeDefinition:
        action = ACTION_TYPES.get(action_type.strip().lower())
        if action is None:
            raise ValueError("Agent action type was not found.")
        return action

    def _validate_permission(self, permission_id: str) -> None:
        if permission_id.strip().lower() not in PERMISSION_CATALOG:
            raise ValueError("Agent permission was not found.")

    def _action_event_id(self, agent_id: str, action_type: str) -> str:
        return (
            "ACT-AGENT-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(action_type)}"
        )

    def _audit_event_id(self, agent_id: str, action_type: str) -> str:
        return (
            "AUD-AGENT-ACTION-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(action_type)}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _slug(self, value: str) -> str:
        return value.strip().upper().replace("_", "-")


agent_actions_service = AgentActionsService()
