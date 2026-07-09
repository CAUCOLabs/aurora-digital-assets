from typing import Literal

from pydantic import BaseModel, Field


class SoftwareDeliveryIssueEvaluationRequest(BaseModel):
    issue_key: str
    issue_type: str = "Story"
    project_key: str | None = None
    requirement_quality: int = Field(ge=0, le=100)
    acceptance_criteria_readiness: int = Field(ge=0, le=100)
    test_coverage_readiness: int = Field(ge=0, le=100)
    evidence_readiness: int = Field(ge=0, le=100)
    traceability_score: int = Field(ge=0, le=100)
    trust_readiness: int = Field(ge=0, le=100)
    quality_gate: str
    risk_level: str = "medium"
    ai_analysis_available: bool = False
    suggested_test_cases_count: int = 0
    linked_parent: bool = False
    linked_epic: bool = False
    linked_subtasks_count: int = 0
    linked_issues_count: int = 0
    blocking_risks: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    environment: str = "local"
    reviewer_id: str | None = None


class SoftwareDeliveryIssueEvaluationResponse(BaseModel):
    issue_key: str
    project_key: str | None = None
    governance_decision: str
    governance_score: int
    governance_level: str
    quality_gate: str
    satisfied_controls: list[str]
    missing_controls: list[str]
    blocking_reasons: list[str]
    recommended_next_actions: list[str]
    evidence_required: bool
    review_required: bool
    release_blocked: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class SoftwareDeliveryProjectEvaluationRequest(BaseModel):
    project_key: str
    issue_count: int
    average_requirement_quality: int = Field(ge=0, le=100)
    average_acceptance_criteria_readiness: int = Field(ge=0, le=100)
    average_test_coverage_readiness: int = Field(ge=0, le=100)
    average_evidence_readiness: int = Field(ge=0, le=100)
    average_traceability_score: int = Field(ge=0, le=100)
    average_trust_readiness: int = Field(ge=0, le=100)
    blocked_issues_count: int
    review_required_issues_count: int
    high_risk_issues_count: int
    critical_risks: list[str] = Field(default_factory=list)
    environment: str = "local"
    reviewer_id: str | None = None


class SoftwareDeliveryProjectEvaluationResponse(BaseModel):
    project_key: str
    governance_decision: str
    project_score: int
    project_level: str
    blocking_reasons: list[str]
    missing_controls: list[str]
    recommended_next_actions: list[str]
    evidence_required: bool
    review_required: bool
    release_blocked: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class SoftwareDeliveryReleaseGateRequest(BaseModel):
    release_id: str
    project_key: str
    project_score: int = Field(ge=0, le=100)
    average_trust_readiness: int = Field(ge=0, le=100)
    average_evidence_readiness: int = Field(ge=0, le=100)
    average_traceability_score: int = Field(ge=0, le=100)
    average_test_coverage_readiness: int = Field(ge=0, le=100)
    blocked_issues_count: int
    high_risk_issues_count: int
    unresolved_critical_risks: list[str] = Field(default_factory=list)
    evidence_package_ready: bool = False
    human_review_completed: bool = False
    change_control_approved: bool = False
    regulatory_disclaimer_present: bool = False
    environment: str = "local"
    reviewer_id: str | None = None


class SoftwareDeliveryReleaseGateResponse(BaseModel):
    release_id: str
    project_key: str
    release_gate_decision: str
    release_score: int
    release_level: str
    blocking_reasons: list[str]
    missing_controls: list[str]
    recommended_next_actions: list[str]
    evidence_required: bool
    review_required: bool
    release_blocked: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class SoftwareDeliveryGovernanceSummaryRequest(BaseModel):
    target_id: str
    target_type: Literal["issue", "project", "release"]
    governance_decision: str
    governance_score: int
    reviewer_id: str | None = None


class SoftwareDeliveryGovernanceSummaryResponse(BaseModel):
    summary_id: str
    title: str
    target_id: str
    target_type: str
    summary_points: list[str]
    risk_notes: list[str]
    required_next_steps: list[str]
    safety_notice: str
    created_at: str
