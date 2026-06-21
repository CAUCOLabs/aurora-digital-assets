from datetime import datetime

from pydantic import BaseModel


class AgentAbuseSignalDefinition(BaseModel):
    signal_category: str
    description: str
    default_weight: int


class AgentAbusePatternDefinition(BaseModel):
    pattern_id: str
    description: str


class AgentAbuseDetectionRequest(BaseModel):
    agent_id: str
    detection_context: str = "agent_governance"
    agent_status: str | None = None
    passport_decision: str | None = None
    permission_decision: str | None = None
    policy_decision: str | None = None
    sensitive_action_type: str | None = None
    requested_action: str | None = None
    revocation_decision: str | None = None
    linked_review_case_id: str | None = None
    linked_review_case_status: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    environment: str = "local"
    denied_attempt_count: int = 0
    blocked_policy_count: int = 0
    emergency_override_count: int = 0
    post_suspension_attempt_count: int = 0
    reviewer_id: str = "system"


class AgentAbuseDetectionResponse(BaseModel):
    agent_id: str
    detection_context: str
    abuse_detected: bool
    abuse_decision: str
    abuse_score: int
    abuse_level: str
    detected_signals: list[str]
    matched_patterns: list[str]
    recommended_actions: list[str]
    sensitive_actions_blocked: bool
    secret_access_blocked: bool
    custodian_access_blocked: bool
    withdrawal_execution_blocked: bool
    external_tool_access_blocked: bool
    review_case_required: bool
    evidence_required: bool
    revocation_recommended: bool
    quarantine_recommended: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    linked_review_case_id: str | None = None
    linked_evidence_package_id: str | None = None
    linked_revocation_audit_event_id: str | None = None
    safety_notice: str
    created_at: str


class AgentAbuseSequenceEvent(BaseModel):
    event_id: str
    event_type: str
    decision: str | None = None
    action_type: str | None = None
    permission_id: str | None = None
    risk_level: str | None = None
    timestamp: datetime | None = None
    blocked: bool = False


class AgentAbuseSequenceRequest(BaseModel):
    agent_id: str
    events: list[AgentAbuseSequenceEvent]
    environment: str = "local"
    reviewer_id: str = "system"


class AgentAbuseSequenceResponse(AgentAbuseDetectionResponse):
    sequence_event_count: int
    high_risk_event_count: int
    blocked_event_count: int
    critical_event_count: int


class AgentAbuseResponseRecommendationRequest(BaseModel):
    agent_id: str
    abuse_decision: str
    abuse_level: str
    detected_signals: list[str] = []
    reviewer_id: str = "system"


class AgentAbuseResponseRecommendationResponse(BaseModel):
    agent_id: str
    abuse_decision: str
    abuse_level: str
    recommended_response: str
    recommended_actions: list[str]
    escalation_required: bool
    revocation_recommended: bool
    quarantine_recommended: bool
    safety_notice: str
    audit_safe: bool
