from datetime import datetime

from pydantic import BaseModel, Field


class AgentPermissionDefinition(BaseModel):
    permission_id: str
    label: str
    category: str
    risk_level: str
    description: str
    sensitive: bool
    human_approval_required: bool
    evidence_required: bool
    review_case_required: bool
    allowed_for_agent_types: list[str]
    prohibited_for_agent_types: list[str]
    blocked_by_default: bool


class AgentPermissionProfile(BaseModel):
    agent_type: str
    allowed_permissions: list[str]
    denied_or_restricted_permissions: list[str]
    safety_notice: str


class AgentPermissionsForAgentResponse(BaseModel):
    agent_id: str
    agent_name: str
    agent_type: str
    agent_status: str
    passport_id: str | None = None
    profile: AgentPermissionProfile
    allowed_permissions: list[str]
    denied_or_restricted_permissions: list[str]
    safety_notice: str


class AgentPermissionEvaluationRequest(BaseModel):
    agent_id: str
    permission_id: str
    resource_type: str = "generic_resource"
    resource_id: str | None = None
    environment: str = "local"
    action_context: str = "permission_evaluation"
    reviewer_id: str = "system"


class AgentPermissionEvaluationResponse(BaseModel):
    agent_id: str
    agent_name: str
    agent_type: str
    agent_status: str
    passport_id: str | None = None
    permission_id: str
    permission_label: str
    permission_category: str
    permission_risk_level: str
    resource_type: str
    resource_id: str | None = None
    environment: str
    decision: str
    allowed: bool
    human_approval_required: bool
    evidence_required: bool
    review_case_required: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    blocking_reasons: list[str]
    recommended_next_action: str
    safety_notice: str
    created_at: str


class AgentPermissionGrantPreviewRequest(BaseModel):
    permission_id: str
    scope: list[str] = Field(default_factory=list)
    environment: str = "local"
    expires_at: datetime | None = None
    reviewer_id: str = "system"
    justification: str | None = None


class AgentPermissionGrantPreviewResponse(BaseModel):
    agent_id: str
    permission_id: str
    grant_preview_decision: str
    scope: list[str]
    environment: str
    expires_at: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    required_controls: list[str]
    blocking_reasons: list[str]
    recommended_next_action: str
    safety_notice: str
    created_at: str
