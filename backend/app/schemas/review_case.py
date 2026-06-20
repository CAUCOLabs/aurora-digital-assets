from typing import Literal

from pydantic import BaseModel, Field


ReviewCaseLifecycleStatus = Literal[
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
    "mitigated",
    "closed",
]
ReviewCaseActionType = Literal[
    "reviewer_note",
    "evidence_reviewed",
    "mitigation_requested",
    "mitigation_started",
    "mitigation_verified",
    "risk_accepted",
    "case_closed",
]


class ReviewCase(BaseModel):
    case_id: str
    created_at: str
    case_type: str
    title: str
    status: str
    risk_level: str
    reasons: list[str]
    customer: str
    action_type: str
    asset: str
    amount: float
    network: str
    destination_address: str
    wallet_type: str
    reviewer_decision: str | None = None
    reviewer_notes: str | None = None
    persisted: bool = False
    source_module: str | None = None
    source_id: str | None = None
    source_action_id: str | None = None
    reviewer_id: str | None = None
    recommended_next_action: str | None = None
    audit_event_id: str | None = None
    correlation_id: str | None = None
    metadata: dict = Field(default_factory=dict)


class ReviewCaseDecisionRequest(BaseModel):
    decision: str
    notes: str | None = None


class ReviewCaseLifecycleTransitionRequest(BaseModel):
    case_id: str | None = None
    target_status: ReviewCaseLifecycleStatus
    reviewer_id: str
    decision_note: str
    mitigation_action: str | None = None
    evidence_package_id: str | None = None
    risk_acceptance: bool = False


class ReviewCaseLifecycleTransitionResponse(BaseModel):
    case_id: str
    previous_status: str
    new_status: str
    transition_allowed: bool
    lifecycle_stage: str
    reviewer_id: str
    decision_note: str
    mitigation_action: str | None = None
    linked_evidence_package: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    recommended_next_status: str | None = None
    recommended_actions: list[str] = Field(default_factory=list)
    created_at: str


class ReviewCaseActionRequest(BaseModel):
    action_type: ReviewCaseActionType
    actor_id: str
    note: str


class ReviewCaseAction(BaseModel):
    action_id: str
    case_id: str
    action_type: ReviewCaseActionType
    actor_id: str
    note: str
    created_at: str
    audit_event_id: str | None = None


class ReviewCaseCloseRequest(BaseModel):
    reviewer_id: str
    decision_note: str
    final_decision: str
    evidence_package_id: str | None = None
    risk_acceptance: bool = False


class ReviewCaseLifecycleSummary(BaseModel):
    case_id: str
    current_status: str
    allowed_next_statuses: list[str]
    lifecycle_progress_percent: int
    actions: list[ReviewCaseAction]
    linked_evidence_packages: list[str]
    linked_audit_events: list[str]
    final_decision: str | None = None
    closure_ready: bool


class CreateReviewCaseFromEvidencePackageRequest(BaseModel):
    package_id: str
    source_audit_event_id: str
    correlation_id: str
    reviewer_id: str
    priority: str


class CreateReviewCaseFromEvidencePackageResponse(BaseModel):
    case_id: str
    title: str
    source_package_id: str
    source_audit_event_id: str
    correlation_id: str
    source_module: str | None = None
    case_type: str
    priority: str
    severity: str
    status: str
    assigned_team: str
    review_reason: str
    linked_audit_event: str | None = None
    linked_evidence_package: str | None = None
    linked_audit_events: list[str]
    linked_evidence_packages: list[str]
    recommended_actions: list[str]
    traceability_summary: str | None = None
    audit_event_created: bool
    audit_event_id: str
    created_at: str
