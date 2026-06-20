from pydantic import BaseModel


class AgentActionTypeDefinition(BaseModel):
    action_type: str
    label: str
    default_permission_id: str
    base_risk_score: int
    sensitive: bool
    blocked_by_default: bool


class AgentActionRecordRequest(BaseModel):
    agent_id: str
    action_type: str
    permission_id: str
    resource_type: str = "generic_resource"
    resource_id: str | None = None
    environment: str = "local"
    action_context: str = "agent_action_record"
    request_id: str | None = None
    source_context: str = "local_prototype"
    reviewer_id: str = "system"
    declared_outcome: str | None = None


class AgentActionRecordResponse(BaseModel):
    action_event_id: str
    agent_id: str
    agent_name: str
    agent_type: str
    agent_status: str
    passport_id: str | None = None
    permission_id: str
    action_type: str
    resource_type: str
    resource_id: str | None = None
    environment: str
    request_id: str | None = None
    source_context: str
    permission_decision: str
    action_outcome: str
    allowed: bool
    human_approval_required: bool
    evidence_required: bool
    review_case_required: bool
    risk_score: int
    risk_level: str
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_id: str | None = None
    review_case_id: str | None = None
    blocking_reasons: list[str]
    recommended_next_action: str
    safety_notice: str
    created_at: str
