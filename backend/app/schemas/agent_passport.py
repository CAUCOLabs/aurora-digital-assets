from pydantic import BaseModel


class AgentPassportTemplate(BaseModel):
    agent_type: str
    default_declared_capabilities: list[str]
    explicit_restrictions: list[str]
    review_required: bool
    safety_notice: str


class AgentPassportGenerateRequest(BaseModel):
    agent_id: str
    reviewer_id: str = "system"


class AgentPassportResponse(BaseModel):
    passport_id: str
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
    model_reference: str | None = None
    automation_engine: str | None = None
    connected_tools: list[str]
    declared_capabilities: list[str]
    explicit_restrictions: list[str]
    allowed_environment_scope: list[str]
    credential_reference_policy: str
    audit_required: bool
    evidence_required: bool
    review_required: bool
    sensitive_action_allowed: bool
    autonomous_execution_allowed: bool
    external_tool_access_allowed: bool
    custody_execution_allowed: bool
    secrets_access_allowed: bool
    passport_decision: str
    passport_valid: bool
    blocking_reasons: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    recommended_next_action: str
    safety_notice: str
    created_at: str
    expires_at: str | None = None
