from pydantic import BaseModel


class HumanApprovalIntegrityRulesResponse(BaseModel):
    rules: list[str]
    safety_notice: str


class HumanApprovalIntegrityRiskSignalsResponse(BaseModel):
    risk_signals: list[str]
    safety_notice: str


class HumanApprovalIntegrityEvaluationRequest(BaseModel):
    reviewer_id: str
    operation_type: str
    approval_context: str = "sensitive_operation_review"
    actor_id: str | None = None
    actor_type: str | None = None
    amount_eur: float = 0
    asset: str | None = None
    destination_type: str | None = None
    destination_id: str | None = None
    environment: str = "local"
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_audit_event_id: str | None = None
    linked_agent_policy_audit_event_id: str | None = None
    linked_agent_abuse_audit_event_id: str | None = None
    linked_agent_revocation_audit_event_id: str | None = None
    linked_secret_guard_case_id: str | None = None
    linked_custodian_guard_case_id: str | None = None
    linked_ai_threat_case_id: str | None = None
    critical_system_block_active: bool = False
    emergency_override_requested: bool = False
    reviewer_is_case_owner: bool = False
    reviewer_is_actor: bool = False
    reviewer_has_conflict: bool = False
    second_reviewer_id: str | None = None
    second_reviewer_independent: bool = False
    approvals_last_24h: int = 0
    sensitive_approvals_last_24h: int = 0
    override_attempts_last_24h: int = 0
    same_destination_approvals_last_7d: int = 0
    outside_working_hours: bool = False
    reviewer_note: str | None = None


class HumanApprovalIntegrityEvaluationResponse(BaseModel):
    reviewer_id: str
    operation_type: str
    approval_context: str
    integrity_decision: str
    integrity_score: int
    integrity_level: str
    approval_allowed: bool
    operation_paused: bool
    second_reviewer_required: bool
    escalation_required: bool
    post_approval_audit_required: bool
    dual_control_satisfied: bool
    segregation_of_duties_satisfied: bool
    critical_override_blocked: bool
    emergency_override_blocked: bool
    detected_signals: list[str]
    blocking_reasons: list[str]
    recommended_next_actions: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_audit_event_id: str | None = None
    safety_notice: str
    created_at: str


class HumanSensitiveApprovalIntegrityRequest(BaseModel):
    reviewer_id: str
    operation_type: str
    actor_id: str
    actor_type: str = "customer"
    amount_eur: float = 0
    asset: str | None = None
    destination_type: str | None = None
    destination_id: str | None = None
    customer_confirmed: bool = False
    mobile_approval_status: str = "not_requested"
    device_trusted: bool = False
    session_age_minutes: int = 0
    critical_system_block_active: bool = False
    emergency_override_requested: bool = False
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_agent_abuse_audit_event_id: str | None = None
    linked_agent_revocation_audit_event_id: str | None = None
    second_reviewer_id: str | None = None
    second_reviewer_independent: bool = False
    reviewer_is_actor: bool = False
    reviewer_has_conflict: bool = False
    sensitive_approvals_last_24h: int = 0
    override_attempts_last_24h: int = 0
    outside_working_hours: bool = False


class HumanSensitiveApprovalIntegrityResponse(BaseModel):
    human_integrity: HumanApprovalIntegrityEvaluationResponse
    sensitive_approval_recommendation: str
    operation_paused_by_human_integrity_guard: bool
    operation_paused_until_second_reviewer: bool
    operation_paused_until_compliance_review: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str


class HumanDualControlPreviewRequest(BaseModel):
    primary_reviewer_id: str
    second_reviewer_id: str | None = None
    operation_type: str
    priority: str = "medium"
    critical_system_block_active: bool = False
    primary_reviewer_has_conflict: bool = False
    second_reviewer_independent: bool = False
    reviewer_is_actor: bool = False
    emergency_override_requested: bool = False


class HumanDualControlPreviewResponse(BaseModel):
    primary_reviewer_id: str
    second_reviewer_id: str | None = None
    operation_type: str
    dual_control_required: bool
    dual_control_satisfied: bool
    independence_satisfied: bool
    preview_decision: str
    approval_allowed: bool
    operation_paused: bool
    blocking_reasons: list[str]
    recommended_next_actions: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str
