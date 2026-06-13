from typing import Literal

from pydantic import BaseModel


EvidenceItemStatus = Literal["included", "missing", "reviewer_required", "optional"]
EvidencePackageSeverity = Literal["low", "medium", "high", "critical"]
EvidencePackageStatus = Literal["draft", "ready", "incomplete", "escalated"]
EvidencePackageSourceType = Literal["alert", "review_case"]
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
    user_message: str
