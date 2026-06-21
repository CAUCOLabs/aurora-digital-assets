from pydantic import BaseModel


class AgentPolicyDefinition(BaseModel):
    policy_category: str
    description: str


class AgentPolicyDecisionType(BaseModel):
    decision_type: str
    blocks_operation: bool
    description: str


class AgentPolicyEvaluationRequest(BaseModel):
    agent_id: str
    policy_context: str
    requested_action: str
    permission_id: str | None = None
    resource_type: str = "generic_resource"
    resource_id: str | None = None
    environment: str = "local"
    agent_status: str | None = None
    passport_decision: str | None = None
    permission_decision: str | None = None
    sensitive_action_type: str | None = None
    revocation_decision: str | None = None
    linked_review_case_id: str | None = None
    linked_review_case_status: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    amount_eur: float = 0
    emergency_override_requested: bool = False
    human_review_confirmed: bool = False
    reviewer_id: str = "system"


class AgentPolicyContextRequest(BaseModel):
    agent_id: str
    context_type: str
    requested_action: str
    sensitive_action_type: str | None = None
    permission_id: str | None = None
    operation_type: str | None = None
    resource_type: str = "generic_resource"
    resource_id: str | None = None
    environment: str = "local"
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    amount_eur: float = 0
    emergency_override_requested: bool = False
    human_review_confirmed: bool = False
    reviewer_id: str = "system"


class AgentPolicyEvaluationResponse(BaseModel):
    agent_id: str
    policy_context: str
    requested_action: str
    environment: str
    policy_decision: str
    allowed: bool
    operation_paused: bool
    human_review_required: bool
    audit_required: bool
    evidence_required: bool
    review_case_required: bool
    sensitive_action_blocked: bool
    secret_access_blocked: bool
    custodian_access_blocked: bool
    withdrawal_execution_blocked: bool
    external_tool_access_blocked: bool
    emergency_override_blocked: bool
    risk_score: int
    risk_level: str
    applied_policies: list[str]
    blocking_reasons: list[str]
    recommended_next_actions: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class AgentPolicyDecisionExplanationRequest(BaseModel):
    policy_decision: str
    agent_id: str | None = None
    requested_action: str | None = None
    blocking_reasons: list[str] = []
    applied_policies: list[str] = []
    reviewer_id: str = "system"


class AgentPolicyDecisionExplanationResponse(BaseModel):
    policy_decision: str
    explanation: str
    blocking_reasons: list[str]
    applied_policies: list[str]
    recommended_next_actions: list[str]
    safety_notice: str
    audit_safe: bool
    no_secret_material_included: bool
