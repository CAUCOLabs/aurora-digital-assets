from pydantic import BaseModel


RISK_DECISION_AUTO_APPROVED = "auto_approved"
RISK_DECISION_PENDING_REVIEW = "pending_review"
RISK_DECISION_AUTO_REJECTED = "auto_rejected"
RISK_DECISION_BLOCKED = "blocked"
RISK_DECISION_ESCALATED = "escalated"

RISK_LEVEL_LOW = "low"
RISK_LEVEL_MEDIUM = "medium"
RISK_LEVEL_HIGH = "high"
RISK_LEVEL_CRITICAL = "critical"
RISK_LEVEL_INVALID = "invalid"


class RiskDecisionResponse(BaseModel):
    decision: str
    risk_level: str
    reasons: list[str]
    case_required: bool
    case_type: str | None
    user_message: str
    audit_event_type: str
