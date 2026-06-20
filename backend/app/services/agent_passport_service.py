from datetime import datetime, timezone

from app.schemas.agent_passport import (
    AgentPassportResponse,
    AgentPassportTemplate,
)
from app.schemas.agent_registry import AgentRegistryDetail
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service


PASSPORT_SAFETY_NOTICE = (
    "Local deterministic agent passport only. No real execution rights, "
    "custodian access, blockchain execution, sensitive approval, external API "
    "access, or credential material are granted or stored."
)

CREDENTIAL_REFERENCE_POLICY = (
    "No raw credentials stored. No API keys stored. No tokens stored. Only "
    "future credential references, fingerprints, vault references, or rotation "
    "status may be represented. This prototype stores no credential material."
)

BASE_RESTRICTIONS = [
    "no_autonomous_execution",
    "no_secret_access",
    "no_private_key_access",
    "no_custody_execution",
    "no_blockchain_transaction_execution",
    "no_real_custodian_api_access",
    "no_sensitive_operation_approval",
    "human_review_required_for_sensitive_actions",
]

CAPABILITIES_BY_AGENT_ID = {
    "AGENT-COMPLIANCE-ASSISTANT-001": [
        "navigate_compliance_evidence",
        "summarize_review_cases",
        "read_audit_event_metadata",
        "suggest_compliance_follow_up",
    ],
    "AGENT-RISK-ANALYST-001": [
        "summarize_risk_cases",
        "read_sensitive_approval_metadata",
        "suggest_risk_triage",
        "navigate_review_lifecycle",
    ],
    "AGENT-CUSTODIAN-INTEGRATION-001": [
        "evaluate_custodian_readiness_metadata",
        "navigate_custodian_guardrails",
        "suggest_integration_review_follow_up",
        "read_custodian_evidence_metadata",
    ],
}

CAPABILITIES_BY_AGENT_TYPE = {
    "compliance_assistant": [
        "navigate_compliance_evidence",
        "summarize_review_cases",
        "read_audit_event_metadata",
        "suggest_compliance_follow_up",
    ],
    "risk_analyst_agent": [
        "summarize_risk_cases",
        "read_sensitive_approval_metadata",
        "suggest_risk_triage",
        "navigate_review_lifecycle",
    ],
    "custodian_integration_agent": [
        "evaluate_custodian_readiness_metadata",
        "navigate_custodian_guardrails",
        "suggest_integration_review_follow_up",
        "read_custodian_evidence_metadata",
    ],
}

TYPE_RESTRICTIONS = {
    "custodian_integration_agent": [
        "integration_blocked_until_controls_verified",
        "custodian_guardrail_review_required",
    ],
    "high_risk_operation_agent": [
        "high_risk_operation_execution_blocked",
        "human_approval_required",
        "review_case_required_before_activation",
    ],
}

BLOCKED_STATUSES = {"suspended", "revoked", "expired"}
REVIEW_RISK_LEVELS = {"high", "critical"}


class AgentPassportService:
    """Deterministic passport layer for locally registered prototype agents."""

    def list_templates(self) -> list[AgentPassportTemplate]:
        template_types = sorted(
            set(CAPABILITIES_BY_AGENT_TYPE) | set(TYPE_RESTRICTIONS)
        )
        return [
            AgentPassportTemplate(
                agent_type=agent_type,
                default_declared_capabilities=CAPABILITIES_BY_AGENT_TYPE.get(
                    agent_type,
                    [],
                ),
                explicit_restrictions=self._restrictions_for_type(agent_type),
                review_required=agent_type
                in {"custodian_integration_agent", "high_risk_operation_agent"},
                safety_notice=PASSPORT_SAFETY_NOTICE,
            )
            for agent_type in template_types
        ]

    def get_passport(self, agent_id: str) -> AgentPassportResponse:
        agent = self._get_agent(agent_id)
        return self._build_passport(agent, audit_event_created=False)

    def generate_passport(
        self,
        agent_id: str,
        reviewer_id: str = "system",
    ) -> AgentPassportResponse:
        agent = self._get_agent(agent_id)
        passport = self._build_passport(agent, audit_event_created=False)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=passport.audit_event_id,
            actor_id=reviewer_id,
            actor_type="staff",
            source_module="agent_passport",
            action="generate_agent_passport",
            object_type="agent_passport",
            object_id=passport.passport_id,
            decision=passport.passport_decision,
            severity=agent.risk_level,
            summary="Agent passport generated in local deterministic prototype.",
            correlation_id=passport.correlation_id,
            metadata={
                "agent_id": agent.agent_id,
                "agent_type": agent.agent_type,
                "status": agent.status,
                "environment": agent.environment,
                "passport_valid": passport.passport_valid,
                "blocking_reasons": passport.blocking_reasons,
                "safety_notice": PASSPORT_SAFETY_NOTICE,
            },
        )
        return passport.model_copy(
            update={"audit_event_created": audit_event is not None}
        )

    def validate_passport(self, agent_id: str) -> AgentPassportResponse:
        agent = self._get_agent(agent_id)
        return self._build_passport(agent, audit_event_created=False)

    def _get_agent(self, agent_id: str) -> AgentRegistryDetail:
        return agent_registry_service.get_agent(agent_id)

    def _build_passport(
        self,
        agent: AgentRegistryDetail,
        audit_event_created: bool,
    ) -> AgentPassportResponse:
        decision, blocking_reasons = self._passport_decision(agent)
        created_at = datetime.now(timezone.utc).isoformat()
        passport_valid = decision == "passport_valid"
        review_required = decision == "passport_requires_review"

        return AgentPassportResponse(
            passport_id=self._passport_id(agent.agent_id),
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            owner_user_id=agent.owner_user_id,
            owner_organization=agent.owner_organization,
            issuing_authority=agent.issuing_authority,
            human_accountable_party=agent.human_accountable_party,
            environment=agent.environment,
            status=agent.status,
            risk_level=agent.risk_level,
            purpose=agent.purpose,
            model_reference=agent.model_reference,
            automation_engine=agent.automation_engine,
            connected_tools=agent.connected_tools,
            declared_capabilities=self._capabilities_for_agent(agent),
            explicit_restrictions=self._restrictions_for_type(agent.agent_type),
            allowed_environment_scope=agent.allowed_environment_scope,
            credential_reference_policy=CREDENTIAL_REFERENCE_POLICY,
            audit_required=True,
            evidence_required=review_required or decision == "passport_status_blocked",
            review_required=review_required,
            sensitive_action_allowed=False,
            autonomous_execution_allowed=False,
            external_tool_access_allowed=False,
            custody_execution_allowed=False,
            secrets_access_allowed=False,
            passport_decision=decision,
            passport_valid=passport_valid,
            blocking_reasons=blocking_reasons,
            audit_event_created=audit_event_created,
            audit_event_id=self._audit_event_id(agent.agent_id),
            correlation_id=self._correlation_id(agent.agent_id),
            recommended_next_action=self._recommended_next_action(decision),
            safety_notice=PASSPORT_SAFETY_NOTICE,
            created_at=created_at,
            expires_at=agent.expires_at,
        )

    def _passport_decision(
        self,
        agent: AgentRegistryDetail,
    ) -> tuple[str, list[str]]:
        blocking_reasons: list[str] = []

        if agent.status in BLOCKED_STATUSES:
            blocking_reasons.append(f"agent_status_{agent.status}")
            return "passport_status_blocked", blocking_reasons

        if self._is_expired(agent.expires_at):
            blocking_reasons.append("agent_registration_expired")
            return "passport_status_blocked", blocking_reasons

        review_reasons = []
        if agent.environment == "production":
            review_reasons.append("production_environment_requires_review")
        if agent.risk_level in REVIEW_RISK_LEVELS:
            review_reasons.append(f"{agent.risk_level}_risk_requires_review")
        if agent.agent_type == "custodian_integration_agent":
            review_reasons.append("custodian_integration_agent_requires_review")
        if agent.agent_type == "high_risk_operation_agent":
            review_reasons.append("high_risk_operation_agent_requires_review")

        if review_reasons:
            return "passport_requires_review", review_reasons

        if agent.status != "active":
            return "passport_invalid_agent", ["agent_is_not_active"]

        if agent.environment == "local" and agent.risk_level in {"low", "medium"}:
            return "passport_valid", []

        return "passport_requires_review", ["agent_requires_human_governance_review"]

    def _is_expired(self, expires_at: str | None) -> bool:
        if expires_at is None:
            return False
        try:
            parsed = datetime.fromisoformat(expires_at)
        except ValueError:
            return True
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed <= datetime.now(timezone.utc)

    def _capabilities_for_agent(self, agent: AgentRegistryDetail) -> list[str]:
        return CAPABILITIES_BY_AGENT_ID.get(
            agent.agent_id,
            CAPABILITIES_BY_AGENT_TYPE.get(agent.agent_type, []),
        )

    def _restrictions_for_type(self, agent_type: str) -> list[str]:
        return BASE_RESTRICTIONS + TYPE_RESTRICTIONS.get(agent_type, [])

    def _passport_id(self, agent_id: str) -> str:
        return f"PASS-{agent_id.removeprefix('AGENT-')}"

    def _audit_event_id(self, agent_id: str) -> str:
        return f"AUD-AGENT-PASSPORT-GENERATED-{agent_id.removeprefix('AGENT-')}"

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _recommended_next_action(self, decision: str) -> str:
        if decision == "passport_valid":
            return "record_passport_and_continue_to_future_permission_review_before_any_action"
        if decision == "passport_requires_review":
            return "route_agent_passport_to_human_governance_review_before_any_permission_grant"
        if decision == "passport_status_blocked":
            return "block_agent_activity_and_preserve_passport_audit_trail"
        return "verify_agent_registration_before_creating_or_using_passport"


agent_passport_service = AgentPassportService()
