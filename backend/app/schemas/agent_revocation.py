from pydantic import BaseModel


class AgentRevocationEvaluationRequest(BaseModel):
    agent_id: str
    trigger_source: str = "manual_review"
    trigger_reference_id: str | None = None
    reason: str
    environment: str = "local"
    reviewer_id: str = "system"
    notes: str | None = None


class AgentRevocationEvaluationResponse(BaseModel):
    agent_id: str
    agent_name: str | None = None
    agent_type: str | None = None
    current_agent_status: str
    reason: str
    trigger_source: str
    trigger_reference_id: str | None = None
    environment: str
    revocation_decision: str
    recommended_actions: list[str]
    target_agent_status: str
    sensitive_actions_blocked: bool
    external_tool_access_blocked: bool
    custodian_access_blocked: bool
    secret_access_blocked: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    review_case_required: bool
    evidence_required: bool
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    blocking_reasons: list[str]
    safety_notice: str
    created_at: str


class AgentRevocationApplyPreviewRequest(BaseModel):
    agent_id: str
    target_action: str
    reason: str
    reviewer_id: str = "system"
    trigger_reference_id: str | None = None
    environment: str = "local"
    notes: str | None = None


class AgentRevocationApplyPreviewResponse(BaseModel):
    agent_id: str
    current_agent_status: str
    target_action: str
    target_agent_status: str
    preview_decision: str
    state_mutation_performed: bool
    required_controls: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    blocking_reasons: list[str]
    safety_notice: str
    created_at: str


class AgentRevocationStatusResponse(BaseModel):
    agent_id: str
    agent_name: str
    agent_type: str
    current_agent_status: str
    revocation_supported: bool
    status_source: str
    safety_notice: str
