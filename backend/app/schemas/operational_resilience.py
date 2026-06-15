from typing import Literal

from pydantic import BaseModel


ServiceCategory = Literal[
    "payments",
    "authentication",
    "digital_assets",
    "core_banking",
    "reporting",
    "staff_operations",
    "external_dependency",
]
ServiceStatus = Literal["healthy", "degraded", "outage", "maintenance", "paused"]
CustomerImpact = Literal["none", "low", "medium", "high", "severe"]
CurrentMode = Literal["normal", "degraded", "read_only", "paused", "fallback"]
DependencyType = Literal[
    "internal",
    "external",
    "network",
    "authentication",
    "payment_rail",
    "custody",
    "reporting",
]
DependencyHealth = Literal["healthy", "degraded", "outage", "unknown"]
FallbackStatus = Literal["available", "active", "unavailable", "testing"]
IncidentSeverity = Literal["low", "medium", "high", "critical"]
IncidentStatus = Literal["open", "investigating", "mitigated", "resolved"]
FailureType = Literal[
    "service_degradation",
    "outage",
    "dependency_failure",
    "traffic_spike",
    "maintenance_failure",
    "fallback_activation",
]
ResilienceDecision = Literal[
    "normal_operations",
    "degraded_mode",
    "activate_fallback",
    "pause_sensitive_operations",
    "escalate_incident",
]


class ServiceHealthStatus(BaseModel):
    service_id: str
    name: str
    category: ServiceCategory
    status: ServiceStatus
    availability_percent: float
    customer_impact: CustomerImpact
    fallback_available: bool
    current_mode: CurrentMode
    recommended_action: str


class DependencyStatus(BaseModel):
    dependency_id: str
    name: str
    dependency_type: DependencyType
    status: DependencyHealth
    affected_services: list[str]
    risk_summary: str


class FallbackMode(BaseModel):
    fallback_id: str
    title: str
    status: FallbackStatus
    description: str
    allowed_operations: list[str]
    paused_operations: list[str]
    activation_reason: str | None = None


class ResilienceControl(BaseModel):
    control_id: str
    title: str
    category: str
    description: str
    activated: bool
    evidence_outputs: list[str]


class IncidentTimelineEvent(BaseModel):
    event_id: str
    timestamp: str
    event_type: str
    title: str
    description: str
    source_module: str


class ResilienceIncident(BaseModel):
    incident_id: str
    title: str
    affected_service: str
    severity: IncidentSeverity
    status: IncidentStatus
    failure_type: FailureType
    customer_impact: CustomerImpact
    summary: str
    controls_activated: list[str]
    fallback_mode: str
    paused_operations: list[str]
    available_operations: list[str]
    recommended_action: str
    audit_evidence: list[str]
    timeline: list[IncidentTimelineEvent]
    created_at: str


class EvaluateResilienceScenarioRequest(BaseModel):
    scenario_id: str
    affected_service: str
    dependency_status: str
    customer_impact: str


class EvaluateResilienceScenarioResponse(BaseModel):
    resilience_score: int
    severity: IncidentSeverity
    decision: ResilienceDecision
    controls_activated: list[str]
    available_operations: list[str]
    paused_operations: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    recommended_action: str
    explanation: str
