from typing import Literal

from pydantic import BaseModel


ApiSecurityControlCategory = Literal[
    "batching",
    "rate_limit",
    "authorization",
    "schema_exposure",
    "mutation_control",
    "token_security",
    "audit_logging",
    "step_up_authentication",
]
ApiSecuritySurfaceType = Literal[
    "graphql",
    "rest",
    "auth",
    "payments",
    "digital_assets",
    "customer_access",
]
ApiSurfaceKind = Literal["graphql", "rest", "auth", "internal_api"]
ApiSecuritySeverity = Literal["low", "medium", "high", "critical"]
ApiSecurityDecision = Literal[
    "allow",
    "block",
    "review_required",
    "step_up_required",
    "audit_only",
]
ApiSecurityEventStatus = Literal[
    "new",
    "blocked",
    "under_review",
    "escalated",
    "closed",
]
ApiSecuritySurfaceStatus = Literal[
    "monitored",
    "restricted",
    "hardened",
    "review_required",
]
ApiSensitiveOperationCategory = Literal[
    "pin",
    "transfer",
    "recovery",
    "token",
    "beneficiary",
    "account_lookup",
    "wallet_withdrawal",
    "staff_access",
]


class ApiSecurityControl(BaseModel):
    control_id: str
    title: str
    category: ApiSecurityControlCategory
    description: str
    protected_operations: list[str]
    decision_model: str
    evidence_outputs: list[str]
    enabled: bool


class ApiSecurityEvent(BaseModel):
    event_id: str
    title: str
    api_surface: ApiSecuritySurfaceType
    operation_name: str
    risk_type: str
    severity: ApiSecuritySeverity
    decision: ApiSecurityDecision
    status: ApiSecurityEventStatus
    triggered_controls: list[str]
    business_action: str
    summary: str
    recommended_action: str
    audit_event: str
    created_at: str
    affected_object: str | None = None


class ApiSecuritySurface(BaseModel):
    surface_id: str
    name: str
    surface_type: ApiSurfaceKind
    risk_summary: str
    sensitive_operations: list[str]
    controls_applied: list[str]
    status: ApiSecuritySurfaceStatus


class ApiSensitiveOperation(BaseModel):
    operation_id: str
    name: str
    category: ApiSensitiveOperationCategory
    risk_level: ApiSecuritySeverity
    required_controls: list[str]
    audit_required: bool
    step_up_required: bool
    batching_allowed: bool


class ApiSecurityScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    risk_indicators: list[str]
    expected_decision: ApiSecurityDecision
    recommended_controls: list[str]


class EvaluateApiSecurityScenarioRequest(BaseModel):
    scenario_id: str
    operation_name: str
    attempts: int
    object_authorized: bool
    batching_detected: bool
    sensitive_fields_requested: bool


class EvaluateApiSecurityScenarioResponse(BaseModel):
    risk_score: int
    severity: ApiSecuritySeverity
    decision: ApiSecurityDecision
    triggered_controls: list[str]
    audit_event_required: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    recommended_action: str
    explanation: str
