from pydantic import BaseModel


class ReadinessControlDefinition(BaseModel):
    control_id: str
    group: str
    criticality: str
    description: str


class PartnerTypeDefinition(BaseModel):
    partner_type: str
    description: str


class ExternalPartnerReadinessRequest(BaseModel):
    partner_id: str
    partner_name: str
    partner_type: str
    environment: str = "local"
    intended_integration_scope: str = "metadata_only_review"
    agent_id: str | None = None
    agent_type: str | None = None
    controls: dict[str, bool]
    linked_agent_passport_id: str | None = None
    linked_agent_policy_audit_event_id: str | None = None
    linked_agent_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_review_case_id: str | None = None
    reviewer_id: str = "system"


class CustodianAgentReadinessRequest(BaseModel):
    partner_id: str
    partner_name: str
    agent_id: str
    environment: str = "local"
    controls: dict[str, bool]
    linked_agent_passport_id: str | None = None
    linked_agent_policy_audit_event_id: str | None = None
    linked_agent_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_review_case_id: str | None = None
    reviewer_id: str = "system"


class ExternalPartnerReadinessPreviewRequest(BaseModel):
    partner_type: str
    intended_integration_scope: str = "metadata_only_review"
    controls: dict[str, bool]
    environment: str = "local"
    reviewer_id: str = "system"


class ExternalPartnerReadinessResponse(BaseModel):
    partner_id: str
    partner_name: str
    partner_type: str
    environment: str
    intended_integration_scope: str
    agent_id: str | None = None
    readiness_decision: str
    readiness_score: int
    readiness_level: str
    missing_controls: list[str]
    failed_controls: list[str]
    satisfied_controls: list[str]
    critical_blockers: list[str]
    conditional_requirements: list[str]
    sensitive_operations_blocked: bool
    external_access_blocked: bool
    custodian_access_blocked: bool
    secret_exchange_blocked: bool
    human_review_required: bool
    evidence_required: bool
    review_case_required: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    linked_agent_passport_id: str | None = None
    linked_agent_policy_audit_event_id: str | None = None
    linked_agent_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_review_case_id: str | None = None
    recommended_next_actions: list[str]
    safety_notice: str
    created_at: str
