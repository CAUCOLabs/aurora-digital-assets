from typing import Literal

from pydantic import BaseModel


Severity = Literal["low", "medium", "high", "critical"]
RecommendedDecision = Literal["allow", "review_required", "escalate", "block"]
ReviewPriority = Literal["low", "medium", "high", "urgent"]
EvidenceRequirementStatus = Literal["included", "missing", "reviewer_required"]


class RiskExplanation(BaseModel):
    explanation_id: str
    alert_id: str
    alert_title: str
    risk_type: str
    severity: Severity
    risk_summary: str
    reasoning: str
    triggered_controls: list[str]
    supporting_evidence: list[str]
    missing_evidence: list[str]
    reviewer_questions: list[str]
    recommended_decision: RecommendedDecision
    evidence_package_ready: bool


class ReviewerGuidance(BaseModel):
    guidance_id: str
    title: str
    category: str
    description: str
    checklist: list[str]
    reviewer_action: str


class EvidenceRequirement(BaseModel):
    requirement_id: str
    title: str
    category: str
    description: str
    status: EvidenceRequirementStatus
    required: bool


class DecisionPathStep(BaseModel):
    step_number: int
    title: str
    description: str


class ExplainAlertRequest(BaseModel):
    alert_id: str
    include_evidence_requirements: bool = True


class ExplainAlertResponse(BaseModel):
    alert_id: str
    explanation: RiskExplanation
    decision_path: list[DecisionPathStep]
    evidence_requirements: list[EvidenceRequirement]
    reviewer_next_steps: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str


class PrepareReviewCaseRequest(BaseModel):
    alert_id: str
    reviewer_id: str | None = None
    priority: ReviewPriority


class PrepareReviewCaseResponse(BaseModel):
    case_preview_id: str
    alert_id: str
    priority: ReviewPriority
    case_title: str
    case_summary: str
    included_evidence: list[str]
    required_evidence: list[str]
    recommended_assignment: str
    ready_for_review: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
