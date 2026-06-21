from pydantic import BaseModel


class AgentSensitiveActionGuardRule(BaseModel):
    rule_id: str
    description: str
    guard_decision: str
    applies_to_action_types: list[str]
    requires_human_review: bool
    blocks_operation: bool


class AgentSensitiveActionDefinition(BaseModel):
    sensitive_action_type: str
    default_permission_id: str
    base_risk_score: int
    sensitive: bool
    blocked_by_default: bool


class AgentSensitiveActionGuardRequest(BaseModel):
    agent_id: str
    sensitive_action_type: str
    operation_type: str = "generic_sensitive_operation"
    permission_id: str | None = None
    resource_type: str = "generic_resource"
    resource_id: str | None = None
    amount_eur: float = 0
    asset: str | None = None
    destination_type: str | None = None
    destination_id: str | None = None
    environment: str = "local"
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    reviewer_id: str = "system"
    human_review_confirmed: bool = False
    emergency_override_requested: bool = False


class AgentSensitiveActionGuardResponse(BaseModel):
    agent_id: str
    agent_name: str | None = None
    agent_type: str | None = None
    agent_status: str
    sensitive_action_type: str
    operation_type: str
    permission_id: str | None = None
    resource_type: str
    resource_id: str | None = None
    environment: str
    guard_decision: str
    allowed: bool
    human_review_required: bool
    operation_paused: bool
    sensitive_action_blocked: bool
    secret_access_blocked: bool
    custodian_access_blocked: bool
    withdrawal_execution_blocked: bool
    external_tool_access_blocked: bool
    passport_required: bool
    permission_evaluation_required: bool
    revocation_check_required: bool
    review_case_required: bool
    evidence_required: bool
    risk_score: int
    risk_level: str
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    blocking_reasons: list[str]
    recommended_next_action: str
    safety_notice: str
    created_at: str


class AgentSensitiveApprovalContextRequest(BaseModel):
    agent_id: str
    operation_type: str
    actor_id: str
    actor_type: str = "agent"
    amount_eur: float = 0
    asset: str | None = None
    destination_type: str | None = None
    destination_id: str | None = None
    customer_confirmed: bool = False
    mobile_approval_status: str = "not_requested"
    device_trusted: bool = False
    session_age_minutes: int = 0
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    reviewer_id: str = "system"


class AgentSensitiveApprovalContextResponse(BaseModel):
    agent_guard: AgentSensitiveActionGuardResponse
    sensitive_approval_recommendation: str
    operation_paused_by_agent_guard: bool
    operation_paused_until_human_review: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
