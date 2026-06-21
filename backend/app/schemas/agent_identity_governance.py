from pydantic import BaseModel


class GovernanceFrameworkResponse(BaseModel):
    purpose: str
    scope: list[str]
    non_goals: list[str]
    safety_boundaries: list[str]
    linked_modules: list[str]


class GovernanceControlDomain(BaseModel):
    domain_id: str
    description: str
    controls: list[str]


class AgentIdentityGovernanceEvaluationRequest(BaseModel):
    assessment_id: str = "AGENT-GOVERNANCE-ASSESSMENT-001"
    environment: str = "local"
    target_environment: str = "future_production"
    reviewer_id: str = "system"
    controls: dict[str, bool]
    linked_agent_id: str | None = None
    linked_partner_id: str | None = None
    linked_policy_audit_event_id: str | None = None
    linked_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_readiness_audit_event_id: str | None = None
    linked_review_case_id: str | None = None
    notes: str | None = None


class AgentProductionReadinessRequest(BaseModel):
    assessment_id: str = "AGENT-PRODUCTION-READINESS-001"
    target_environment: str = "future_production"
    reviewer_id: str = "system"
    controls: dict[str, bool]
    linked_agent_id: str | None = None
    linked_partner_id: str | None = None
    linked_policy_audit_event_id: str | None = None
    linked_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_readiness_audit_event_id: str | None = None
    linked_review_case_id: str | None = None


class AgentIdentityGovernanceEvaluationResponse(BaseModel):
    assessment_id: str
    environment: str
    target_environment: str
    governance_decision: str
    governance_score: int
    governance_level: str
    satisfied_controls: list[str]
    missing_controls: list[str]
    failed_controls: list[str]
    critical_blockers: list[str]
    conditional_requirements: list[str]
    human_review_required: bool
    evidence_required: bool
    review_case_required: bool
    production_access_blocked: bool
    external_access_blocked: bool
    custodian_access_blocked: bool
    secret_access_blocked: bool
    sensitive_operations_blocked: bool
    cloud_deployment_blocked: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    linked_agent_id: str | None = None
    linked_partner_id: str | None = None
    linked_policy_audit_event_id: str | None = None
    linked_abuse_audit_event_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    linked_readiness_audit_event_id: str | None = None
    linked_review_case_id: str | None = None
    recommended_next_actions: list[str]
    safety_notice: str
    created_at: str


class AgentGovernanceSummaryRequest(BaseModel):
    assessment_id: str
    governance_decision: str
    governance_score: int
    governance_level: str
    critical_blockers: list[str] | None = None
    missing_controls: list[str] | None = None
    reviewer_id: str = "system"


class AgentGovernanceSummaryResponse(BaseModel):
    assessment_id: str
    summary_title: str
    summary: str
    governance_decision: str
    governance_score: int
    governance_level: str
    critical_blockers: list[str]
    missing_controls: list[str]
    recommended_next_actions: list[str]
    audit_safe: bool
    no_secret_material_included: bool
    safety_notice: str
