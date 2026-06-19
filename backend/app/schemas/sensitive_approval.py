from typing import Any, Literal

from pydantic import BaseModel, Field


SensitiveActorType = Literal["customer", "staff", "reviewer", "admin"]
SensitivityLevel = Literal["low", "medium", "high", "critical"]
StepUpMethod = Literal[
    "mobile_approval_simulated",
    "strong_reauthentication_simulated",
    "dual_control_simulated",
    "not_required",
]
MobileApprovalStatus = Literal["pending", "approved", "rejected", "expired"]
BackendRiskDecision = Literal[
    "approved",
    "pending_review",
    "blocked",
    "step_up_required",
]


class SensitiveOperation(BaseModel):
    operation_id: str
    operation_type: str
    title: str
    description: str
    actor_type: SensitiveActorType
    sensitivity_level: SensitivityLevel
    approval_required: bool
    step_up_method: StepUpMethod
    risk_triggers: list[str]
    possible_outcomes: list[str]


class SensitiveApprovalRequest(BaseModel):
    operation_type: str
    actor_id: str
    actor_type: SensitiveActorType
    amount_eur: float | None = None
    asset: str | None = None
    destination_type: str | None = None
    destination_id: str | None = None
    is_new_destination: bool = False
    customer_confirmed: bool = False
    mobile_approval_status: MobileApprovalStatus = "pending"
    device_trusted: bool = True
    session_age_minutes: int = 5
    risk_context: dict[str, Any] = Field(default_factory=dict)
    linked_ai_threat_case_id: str | None = None
    ai_threat_guard_required: bool = False
    ai_threat_guard_status: str | None = None
    ai_threat_guard_reason: str | None = None
    linked_secret_guard_case_id: str | None = None
    secret_guard_required: bool = False
    secret_guard_status: str | None = None
    secret_guard_reason: str | None = None
    linked_custodian_guard_case_id: str | None = None
    custodian_guard_required: bool = False
    custodian_guard_status: str | None = None


class SensitiveApprovalResponse(BaseModel):
    operation_id: str
    operation_type: str
    actor_id: str
    actor_type: SensitiveActorType
    approval_required: bool
    step_up_method: StepUpMethod
    mobile_approval_status: MobileApprovalStatus
    backend_risk_decision: BackendRiskDecision
    risk_level: SensitivityLevel
    risk_score: int
    reasons: list[str]
    user_message: str
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    review_case_required: bool
    review_case_id: str | None = None
    recommended_next_action: str
    ai_threat_guard_applied: bool = False
    ai_threat_case_id: str | None = None
    ai_threat_case_status: str | None = None
    ai_threat_guard_decision: str | None = None
    ai_threat_guard_reason: str | None = None
    operation_paused_until_review: bool = False
    required_lifecycle_status: str | None = None
    secret_guard_applied: bool = False
    secret_guard_case_id: str | None = None
    secret_guard_case_status: str | None = None
    secret_guard_decision: str | None = None
    secret_guard_reason: str | None = None
    operation_paused_by_secret_guard: bool = False
    secret_guard_required_lifecycle_status: str | None = None
    custodian_guard_applied: bool = False
    custodian_guard_case_id: str | None = None
    custodian_guard_case_status: str | None = None
    custodian_guard_decision: str | None = None
    operation_paused_by_custodian_guard: bool = False
    custodian_guard_required_lifecycle_status: str | None = None
    created_at: str


class SensitiveApprovalScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    operation_type: str
    sample_payload: dict[str, Any]
    expected_decision: BackendRiskDecision
