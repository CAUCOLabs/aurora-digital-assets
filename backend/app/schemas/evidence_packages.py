from typing import Any, Literal

from pydantic import BaseModel, Field


EvidenceItemStatus = Literal["included", "missing", "reviewer_required", "optional"]
EvidencePackageSeverity = Literal["low", "medium", "high", "critical"]
EvidencePackageStatus = Literal["draft", "ready", "incomplete", "escalated"]
EvidencePackageSourceType = Literal["alert", "review_case", "case", "audit_event"]
EvidencePackageType = Literal[
    "internal_review",
    "audit",
    "regulator",
    "investigation",
]


class EvidenceItem(BaseModel):
    item_id: str
    title: str
    category: str
    status: EvidenceItemStatus
    description: str
    source_module: str
    required: bool


class EvidenceTimelineEvent(BaseModel):
    event_id: str
    timestamp: str
    event_type: str
    title: str
    description: str
    source_module: str


class EvidencePackage(BaseModel):
    package_id: str
    title: str
    source_alert_id: str | None = None
    source_case_id: str | None = None
    source_audit_event_id: str | None = None
    source_module: str | None = None
    backend_decision: str | None = None
    correlation_id: str | None = None
    traceability_summary: str | None = None
    audit_context: dict[str, Any] | None = None
    linked_audit_events: list[str] = Field(default_factory=list)
    risk_type: str
    severity: EvidencePackageSeverity
    status: EvidencePackageStatus
    readiness_score: int
    summary: str
    included_evidence: list[EvidenceItem]
    missing_evidence: list[EvidenceItem]
    triggered_controls: list[str]
    reviewer_notes: list[str]
    decision_rationale: str
    timeline: list[EvidenceTimelineEvent]
    recommended_next_action: str
    created_at: str


class EvidencePackageTemplate(BaseModel):
    template_id: str
    title: str
    use_case: str
    description: str
    required_items: list[str]


class GenerateEvidencePackageRequest(BaseModel):
    source_type: EvidencePackageSourceType
    source_id: str
    package_type: EvidencePackageType
    reviewer_id: str | None = None


class EvidenceReadinessCheck(BaseModel):
    ready: bool
    score: int
    blockers: list[str]
    warnings: list[str]
    recommended_actions: list[str]


class GenerateEvidencePackageResponse(BaseModel):
    package: EvidencePackage
    readiness_check: EvidenceReadinessCheck
    export_available: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    source_type: EvidencePackageSourceType
    source_id: str
    source_audit_event_id: str | None = None
    traceability_summary: str | None = None
    evidence_items: list[EvidenceItem] = Field(default_factory=list)
    linked_audit_events: list[str] = Field(default_factory=list)
    recommended_next_steps: list[str] = Field(default_factory=list)
    user_message: str
