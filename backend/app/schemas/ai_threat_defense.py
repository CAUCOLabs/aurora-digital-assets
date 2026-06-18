from datetime import datetime
from typing import Literal

from pydantic import BaseModel


ThreatExposureLevel = Literal["public", "internal", "restricted", "future"]
ThreatSensitivityLevel = Literal["low", "medium", "high", "critical"]
AIThreatDefenseSeverity = Literal["low", "medium", "high", "critical"]
AIThreatDefenseDecision = Literal[
    "monitor",
    "harden",
    "escalate",
    "block",
    "review_required",
]


class ThreatSurface(BaseModel):
    surface_id: str
    name: str
    category: str
    description: str
    exposure_level: ThreatExposureLevel
    sensitivity_level: ThreatSensitivityLevel
    related_modules: list[str]
    defensive_controls: list[str]
    audit_event_required: bool
    review_case_required: bool
    evidence_package_required: bool


class AIThreatScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    affected_surface_categories: list[str]
    weak_signals: list[str]
    expected_decision: str


class AIThreatDefenseEvaluationRequest(BaseModel):
    scenario_id: str
    actor_type: str = "unknown"
    suspected_automation: bool = False
    documentation_exposure: bool = False
    endpoint_enumeration: bool = False
    permission_anomaly: bool = False
    sensitive_operation_chain: bool = False
    secret_exposure_signal: bool = False
    evidence_tampering_signal: bool = False
    cloud_or_kubernetes_signal: bool = False
    custodian_integration_signal: bool = False


class AIThreatDefenseEvaluationResponse(BaseModel):
    scenario_id: str
    risk_score: int
    severity: AIThreatDefenseSeverity
    decision: AIThreatDefenseDecision
    affected_surfaces: list[str]
    weak_signals: list[str]
    defensive_controls: list[str]
    preventive_controls: list[str]
    detective_controls: list[str]
    corrective_controls: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    review_case_required: bool
    review_case_id: str | None = None
    recommended_next_actions: list[str]
    created_at: datetime
