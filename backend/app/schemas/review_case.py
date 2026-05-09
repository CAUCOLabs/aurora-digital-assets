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


class ReviewCaseDecisionRequest(BaseModel):
    decision: str
    notes: str | None = None
