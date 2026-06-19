from dataclasses import dataclass
from datetime import datetime, timezone
import re

from app.schemas.agent_registry import (
    AgentRegistrationRequest,
    AgentRegistrationResponse,
    AgentRegistryDetail,
    AgentRegistrySummary,
    AgentStatusDefinition,
    AgentStatusUpdateRequest,
    AgentStatusUpdateResponse,
    AgentTypeDefinition,
)
from app.services.audit_service import audit_service


AGENT_STATUSES = {
    "active": AgentStatusDefinition(
        status="active",
        description="Registered locally and eligible for future permission review.",
        allowed_to_act=True,
    ),
    "suspended": AgentStatusDefinition(
        status="suspended",
        description="Temporarily blocked from future action until reviewed.",
        allowed_to_act=False,
    ),
    "revoked": AgentStatusDefinition(
        status="revoked",
        description="Registration is revoked and must not be used for future action.",
        allowed_to_act=False,
    ),
    "expired": AgentStatusDefinition(
        status="expired",
        description="Registration has expired and requires re-registration.",
        allowed_to_act=False,
    ),
}

RISK_LEVELS = {"low", "medium", "high", "critical"}
ENVIRONMENTS = {"local", "staging", "production"}
REGISTRY_SAFETY_NOTICE = (
    "Local registry only. No autonomous execution granted. No permissions "
    "granted yet. No real external tool access. No secrets stored. No custodian "
    "or blockchain execution."
)


AGENT_TYPES = {
    "compliance_assistant": AgentTypeDefinition(
        type_id="compliance_assistant",
        label="Compliance Assistant",
        default_risk_level="medium",
        description="Supports compliance summaries, evidence navigation, and review preparation.",
        sensitive_by_default=False,
    ),
    "risk_analyst_agent": AgentTypeDefinition(
        type_id="risk_analyst_agent",
        label="Risk Analyst Agent",
        default_risk_level="high",
        description="Supports deterministic risk review and internal case triage.",
        sensitive_by_default=True,
    ),
    "reporting_agent": AgentTypeDefinition(
        type_id="reporting_agent",
        label="Reporting Agent",
        default_risk_level="medium",
        description="Supports approved internal reporting summaries and audit-safe exports.",
        sensitive_by_default=False,
    ),
    "customer_support_agent": AgentTypeDefinition(
        type_id="customer_support_agent",
        label="Customer Support Agent",
        default_risk_level="medium",
        description="Supports customer support workflows without autonomous financial action.",
        sensitive_by_default=False,
    ),
    "security_monitoring_agent": AgentTypeDefinition(
        type_id="security_monitoring_agent",
        label="Security Monitoring Agent",
        default_risk_level="high",
        description="Supports defensive monitoring and escalation workflows.",
        sensitive_by_default=True,
    ),
    "development_assistant": AgentTypeDefinition(
        type_id="development_assistant",
        label="Development Assistant",
        default_risk_level="medium",
        description="Supports local prototype implementation and documentation work.",
        sensitive_by_default=False,
    ),
    "admin_automation_agent": AgentTypeDefinition(
        type_id="admin_automation_agent",
        label="Admin Automation Agent",
        default_risk_level="critical",
        description="Represents high-risk administrative automation requiring strict review.",
        sensitive_by_default=True,
    ),
    "external_partner_agent": AgentTypeDefinition(
        type_id="external_partner_agent",
        label="External Partner Agent",
        default_risk_level="high",
        description="Represents partner-bound automation requiring ownership and boundary checks.",
        sensitive_by_default=True,
    ),
    "custodian_integration_agent": AgentTypeDefinition(
        type_id="custodian_integration_agent",
        label="Custodian Integration Agent",
        default_risk_level="critical",
        description="Represents future custodian readiness work without custody execution.",
        sensitive_by_default=True,
    ),
    "read_only_research_agent": AgentTypeDefinition(
        type_id="read_only_research_agent",
        label="Read-only Research Agent",
        default_risk_level="low",
        description="Supports read-only research over approved internal prototype material.",
        sensitive_by_default=False,
    ),
    "high_risk_operation_agent": AgentTypeDefinition(
        type_id="high_risk_operation_agent",
        label="High-risk Operation Agent",
        default_risk_level="critical",
        description="Represents sensitive operation automation that requires human review.",
        sensitive_by_default=True,
    ),
}


@dataclass
class AgentRecord:
    agent_id: str
    agent_name: str
    agent_type: str
    owner_user_id: str
    owner_organization: str
    issuing_authority: str
    human_accountable_party: str
    environment: str
    status: str
    risk_level: str
    purpose: str
    model_reference: str | None
    automation_engine: str | None
    allowed_environment_scope: list[str]
    connected_tools: list[str]
    created_at: str
    expires_at: str | None


class AgentRegistryService:
    """Local deterministic registry for accountable prototype automation."""

    def __init__(self) -> None:
        self._agents = self._demo_agents()

    def list_types(self) -> list[AgentTypeDefinition]:
        return list(AGENT_TYPES.values())

    def list_statuses(self) -> list[AgentStatusDefinition]:
        return list(AGENT_STATUSES.values())

    def list_agents(self) -> list[AgentRegistrySummary]:
        return [
            self._summary(agent)
            for agent in sorted(self._agents.values(), key=lambda item: item.agent_id)
        ]

    def get_agent(self, agent_id: str) -> AgentRegistryDetail:
        agent = self._agents.get(agent_id.strip().upper())
        if agent is None:
            raise ValueError("Agent registration was not found.")
        return self._detail(agent)

    def register(
        self,
        request: AgentRegistrationRequest,
    ) -> AgentRegistrationResponse:
        self._validate_registration_request(request)

        agent_type = request.agent_type.strip().lower()
        environment = request.environment.strip().lower()
        risk_level = request.risk_level.strip().lower()
        created_at = datetime.now(timezone.utc).isoformat()
        agent_id = self._agent_id(agent_type, request.agent_name)
        decision = self._registration_decision(agent_type, environment, risk_level)

        agent = AgentRecord(
            agent_id=agent_id,
            agent_name=request.agent_name.strip(),
            agent_type=agent_type,
            owner_user_id=request.owner_user_id.strip(),
            owner_organization=request.owner_organization.strip(),
            issuing_authority=request.issuing_authority.strip(),
            human_accountable_party=request.human_accountable_party.strip(),
            environment=environment,
            status="active",
            risk_level=risk_level,
            purpose=request.purpose.strip(),
            model_reference=request.model_reference,
            automation_engine=request.automation_engine,
            allowed_environment_scope=[
                item.strip().lower()
                for item in request.allowed_environment_scope
                if item.strip()
            ],
            connected_tools=[
                item.strip() for item in request.connected_tools if item.strip()
            ],
            created_at=created_at,
            expires_at=(
                request.expires_at.isoformat() if request.expires_at else None
            ),
        )
        self._agents[agent_id] = agent

        audit_event_id = self._registration_audit_event_id(agent_id)
        correlation_id = self._correlation_id(agent_id)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_registry",
            action="register_agent",
            object_type="agent_registration",
            object_id=agent_id,
            decision=decision,
            severity=risk_level,
            summary="Agent registered in local deterministic prototype registry.",
            correlation_id=correlation_id,
            metadata={
                "agent_type": agent_type,
                "environment": environment,
                "owner_user_id": agent.owner_user_id,
                "human_accountable_party": agent.human_accountable_party,
                "safety_notice": REGISTRY_SAFETY_NOTICE,
            },
        )

        return AgentRegistrationResponse(
            **self._response_fields(agent),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            registry_decision=decision,
            recommended_next_action=self._registration_next_action(decision),
            safety_notice=REGISTRY_SAFETY_NOTICE,
        )

    def update_status(
        self,
        agent_id: str,
        request: AgentStatusUpdateRequest,
    ) -> AgentStatusUpdateResponse:
        normalized_agent_id = agent_id.strip().upper()
        agent = self._agents.get(normalized_agent_id)
        if agent is None:
            raise ValueError("Agent registration was not found.")

        target_status = request.target_status.strip().lower()
        if target_status not in AGENT_STATUSES:
            raise ValueError("Unknown agent status.")

        previous_status = agent.status
        agent.status = target_status
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event_id = self._status_audit_event_id(normalized_agent_id, target_status)
        correlation_id = self._correlation_id(normalized_agent_id)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_registry",
            action="update_agent_status",
            object_type="agent_registration",
            object_id=normalized_agent_id,
            decision="status_updated",
            severity=agent.risk_level,
            summary="Agent status updated in local deterministic prototype registry.",
            correlation_id=correlation_id,
            metadata={
                "previous_status": previous_status,
                "new_status": target_status,
                "decision_note": request.decision_note,
                "safety_notice": REGISTRY_SAFETY_NOTICE,
            },
        )

        return AgentStatusUpdateResponse(
            agent_id=normalized_agent_id,
            previous_status=previous_status,
            new_status=target_status,
            status_update_allowed=True,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            recommended_next_action=self._status_next_action(target_status),
            created_at=created_at,
        )

    def _demo_agents(self) -> dict[str, AgentRecord]:
        created_at = "2026-06-19T00:00:00+00:00"
        agents = [
            AgentRecord(
                agent_id="AGENT-COMPLIANCE-ASSISTANT-001",
                agent_name="Aurora Compliance Assistant",
                agent_type="compliance_assistant",
                owner_user_id="user-compliance-demo",
                owner_organization="Aurora Demo Bank",
                issuing_authority="aurora_local_registry",
                human_accountable_party="Head of Compliance",
                environment="local",
                status="active",
                risk_level="medium",
                purpose="Assist with compliance review summaries and evidence navigation.",
                model_reference=None,
                automation_engine=None,
                allowed_environment_scope=["local"],
                connected_tools=["audit_events", "evidence_packages", "review_cases"],
                created_at=created_at,
                expires_at=None,
            ),
            AgentRecord(
                agent_id="AGENT-RISK-ANALYST-001",
                agent_name="Aurora Risk Analyst Agent",
                agent_type="risk_analyst_agent",
                owner_user_id="user-risk-demo",
                owner_organization="Aurora Demo Bank",
                issuing_authority="aurora_local_registry",
                human_accountable_party="Risk Operations Lead",
                environment="local",
                status="active",
                risk_level="high",
                purpose="Assist with deterministic risk review and case triage.",
                model_reference=None,
                automation_engine=None,
                allowed_environment_scope=["local"],
                connected_tools=["risk_operations", "sensitive_approval", "review_cases"],
                created_at=created_at,
                expires_at=None,
            ),
            AgentRecord(
                agent_id="AGENT-CUSTODIAN-INTEGRATION-001",
                agent_name="Aurora Custodian Integration Readiness Agent",
                agent_type="custodian_integration_agent",
                owner_user_id="user-security-demo",
                owner_organization="Aurora Demo Bank",
                issuing_authority="aurora_local_registry",
                human_accountable_party="Security Architecture Lead",
                environment="local",
                status="suspended",
                risk_level="critical",
                purpose=(
                    "Evaluate future custodian integration readiness without "
                    "executing custody operations."
                ),
                model_reference=None,
                automation_engine=None,
                allowed_environment_scope=["local"],
                connected_tools=[
                    "custodian_integration_guardrails",
                    "evidence_packages",
                    "review_cases",
                ],
                created_at=created_at,
                expires_at=None,
            ),
        ]
        return {agent.agent_id: agent for agent in agents}

    def _validate_registration_request(self, request: AgentRegistrationRequest) -> None:
        required_values = {
            "agent_name": request.agent_name,
            "owner_user_id": request.owner_user_id,
            "owner_organization": request.owner_organization,
            "human_accountable_party": request.human_accountable_party,
            "purpose": request.purpose,
        }
        missing = [field for field, value in required_values.items() if not value.strip()]
        if missing:
            raise ValueError(f"Missing required agent registration field: {missing[0]}.")

        if request.agent_type.strip().lower() not in AGENT_TYPES:
            raise ValueError("Unknown agent type.")
        if request.environment.strip().lower() not in ENVIRONMENTS:
            raise ValueError("Unknown agent environment.")
        if request.risk_level.strip().lower() not in RISK_LEVELS:
            raise ValueError("Unknown agent risk level.")

    def _registration_decision(
        self,
        agent_type: str,
        environment: str,
        risk_level: str,
    ) -> str:
        if environment == "production":
            return "registration_requires_review"
        if agent_type == "high_risk_operation_agent":
            return "registration_requires_review"
        if agent_type == "custodian_integration_agent" and risk_level == "critical":
            return "registration_requires_review"
        return "registration_allowed"

    def _registration_next_action(self, decision: str) -> str:
        if decision == "registration_requires_review":
            return (
                "route_agent_registration_to_human_governance_review_before_any_permission_grant"
            )
        return "record_local_agent_registration_and_verify_permissions_before_any_action"

    def _status_next_action(self, status: str) -> str:
        if status in {"revoked", "suspended"}:
            return "block_future_actions_and_preserve_audit_trail"
        if status == "active":
            return "verify_permissions_before_allowing_any_action"
        return "treat_permissions_as_expired_and_require_re_registration_if_needed"

    def _agent_id(self, agent_type: str, agent_name: str) -> str:
        return f"AGENT-{self._slug(agent_type)}-{self._slug(agent_name)}"[:96]

    def _registration_audit_event_id(self, agent_id: str) -> str:
        return f"AUD-AGENT-REGISTERED-{agent_id.removeprefix('AGENT-')}"

    def _status_audit_event_id(self, agent_id: str, target_status: str) -> str:
        return (
            f"AUD-AGENT-STATUS-{agent_id.removeprefix('AGENT-')}-"
            f"{target_status.upper()}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _slug(self, value: str) -> str:
        normalized = re.sub(r"[\s_]+", "-", value.strip().upper())
        normalized = re.sub(r"[^A-Z0-9-]", "", normalized)
        normalized = re.sub(r"-+", "-", normalized).strip("-")
        return normalized or "UNSPECIFIED"

    def _summary(self, agent: AgentRecord) -> AgentRegistrySummary:
        return AgentRegistrySummary(
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            owner_user_id=agent.owner_user_id,
            owner_organization=agent.owner_organization,
            human_accountable_party=agent.human_accountable_party,
            environment=agent.environment,
            status=agent.status,
            risk_level=agent.risk_level,
            created_at=agent.created_at,
            expires_at=agent.expires_at,
        )

    def _detail(self, agent: AgentRecord) -> AgentRegistryDetail:
        return AgentRegistryDetail(
            **self._response_fields(agent),
            safety_notice=REGISTRY_SAFETY_NOTICE,
        )

    def _response_fields(self, agent: AgentRecord) -> dict[str, object]:
        return {
            "agent_id": agent.agent_id,
            "agent_name": agent.agent_name,
            "agent_type": agent.agent_type,
            "owner_user_id": agent.owner_user_id,
            "owner_organization": agent.owner_organization,
            "issuing_authority": agent.issuing_authority,
            "human_accountable_party": agent.human_accountable_party,
            "environment": agent.environment,
            "status": agent.status,
            "risk_level": agent.risk_level,
            "purpose": agent.purpose,
            "model_reference": agent.model_reference,
            "automation_engine": agent.automation_engine,
            "allowed_environment_scope": agent.allowed_environment_scope,
            "connected_tools": agent.connected_tools,
            "created_at": agent.created_at,
            "expires_at": agent.expires_at,
        }


agent_registry_service = AgentRegistryService()
