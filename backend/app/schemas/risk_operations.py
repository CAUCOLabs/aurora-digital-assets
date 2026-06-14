from typing import Literal

from pydantic import BaseModel


MetricStatus = Literal["normal", "attention", "warning", "critical"]
RiskSourceModule = Literal[
    "financial_crime",
    "compliance_intelligence",
    "evidence_packages",
    "operational_resilience",
    "compliance_review",
    "reports",
]
RiskPriority = Literal["low", "medium", "high", "urgent"]
RiskActionStatus = Literal[
    "new",
    "in_progress",
    "blocked",
    "ready",
    "escalated",
    "closed",
]
TimelineSeverity = Literal["low", "medium", "high", "critical"]
EscalationType = Literal[
    "financial_crime",
    "operational_resilience",
    "evidence_gap",
    "compliance_review",
]
OperatingMode = Literal[
    "normal",
    "elevated_monitoring",
    "restricted_operations",
    "incident_command",
]


class RiskOperationsLink(BaseModel):
    label: str
    route: str
    entity_id: str | None = None


class RiskOperationsMetric(BaseModel):
    metric_id: str
    label: str
    value: str
    status: MetricStatus
    description: str
    source_module: RiskSourceModule


class RiskActionItem(BaseModel):
    action_id: str
    title: str
    source_module: RiskSourceModule
    source_id: str
    priority: RiskPriority
    status: RiskActionStatus
    risk_type: str
    summary: str
    required_action: str
    missing_evidence: list[str]
    related_links: list[RiskOperationsLink]
    created_at: str


class UnifiedTimelineEvent(BaseModel):
    event_id: str
    timestamp: str
    source_module: RiskSourceModule
    event_type: str
    severity: TimelineSeverity
    title: str
    description: str
    related_entity_id: str
    recommended_action: str


class EscalationSummary(BaseModel):
    summary_id: str
    title: str
    severity: TimelineSeverity
    escalation_type: EscalationType
    open_items: int
    blocked_items: int
    ready_items: int
    summary: str
    recommended_action: str


class RiskOperationsOverview(BaseModel):
    generated_at: str
    metrics: list[RiskOperationsMetric]
    highest_priority: RiskPriority
    operating_mode: OperatingMode
    summary: str
    recommended_focus: list[str]
