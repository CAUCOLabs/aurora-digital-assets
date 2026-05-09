from pydantic import BaseModel, Field


class AuditEvent(BaseModel):
    event_id: str
    timestamp: str
    module: str
    action_type: str
    status: str
    risk_level: str | None = None
    decision: str | None = None
    reasons: list[str] = Field(default_factory=list)
    case_id: str | None = None
    user_message: str | None = None
