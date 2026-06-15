from typing import Any, Literal

from pydantic import BaseModel, Field


AuditActorType = Literal["staff", "system", "customer", "service"]


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
    actor_id: str | None = None
    actor_type: AuditActorType | None = None
    source_module: str | None = None
    action: str | None = None
    object_type: str | None = None
    object_id: str | None = None
    severity: str | None = None
    risk_score: int | None = None
    summary: str | None = None
    evidence_reference: str | None = None
    review_case_id: str | None = None
    correlation_id: str | None = None
    immutable_note: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
