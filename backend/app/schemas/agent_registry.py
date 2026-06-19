from datetime import datetime

from pydantic import BaseModel, Field


class AgentTypeDefinition(BaseModel):
    type_id: str
    label: str
    default_risk_level: str
    description: str
    sensitive_by_default: bool


class AgentStatusDefinition(BaseModel):
    status: str
    description: str
    allowed_to_act: bool


class AgentRegistrationRequest(BaseModel):
    agent_name: str
    agent_type: str
    owner_user_id: str
    owner_organization: str
    issuing_authority: str = "aurora_local_registry"
    human_accountable_party: str
    environment: str = "local"
    risk_level: str = "medium"
    purpose: str
    model_reference: str | None = None
    automation_engine: str | None = None
    allowed_environment_scope: list[str] = Field(default_factory=list)
    connected_tools: list[str] = Field(default_factory=list)
    expires_at: datetime | None = None
    reviewer_id: str = "system"


class AgentRegistrationResponse(BaseModel):
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
    allowed_environment_scope: list[str]
    connected_tools: list[str]
    created_at: str
    expires_at: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    registry_decision: str
    recommended_next_action: str
    safety_notice: str


class AgentRegistrySummary(BaseModel):
    agent_id: str
    agent_name: str
    agent_type: str
    owner_user_id: str
    owner_organization: str
    human_accountable_party: str
    environment: str
    status: str
    risk_level: str
    created_at: str
    expires_at: str | None = None


class AgentRegistryDetail(BaseModel):
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
    allowed_environment_scope: list[str]
    connected_tools: list[str]
    created_at: str
    expires_at: str | None = None
    safety_notice: str


class AgentStatusUpdateRequest(BaseModel):
    target_status: str
    reviewer_id: str = "system"
    decision_note: str | None = None


class AgentStatusUpdateResponse(BaseModel):
    agent_id: str
    previous_status: str
    new_status: str
    status_update_allowed: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    recommended_next_action: str
    created_at: str
