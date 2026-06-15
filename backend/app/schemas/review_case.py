from pydantic import BaseModel, Field


class ReviewCase(BaseModel):
    case_id: str
    created_at: str
    case_type: str
    title: str
    status: str
    risk_level: str
    reasons: list[str]
    customer: str
    action_type: str
    asset: str
    amount: float
    network: str
    destination_address: str
    wallet_type: str
    reviewer_decision: str | None = None
    reviewer_notes: str | None = None
    persisted: bool = False
    source_module: str | None = None
    source_id: str | None = None
    source_action_id: str | None = None
    reviewer_id: str | None = None
    recommended_next_action: str | None = None
    audit_event_id: str | None = None
    correlation_id: str | None = None
    metadata: dict = Field(default_factory=dict)


class ReviewCaseDecisionRequest(BaseModel):
    decision: str
    notes: str | None = None
