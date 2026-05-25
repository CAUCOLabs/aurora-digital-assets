from pydantic import BaseModel


class BuySellEvaluateRequest(BaseModel):
    side: str
    asset: str
    amount: float
    source_account_id: str


class BuySellEstimate(BaseModel):
    side: str
    asset: str
    market_price_eur: float
    gross_eur: float
    fee_eur: float
    spread_eur: float
    net_eur: float
    estimated_asset_amount: float


class BuySellEvaluateResponse(BaseModel):
    decision: str
    risk_level: str
    reasons: list[str]
    case_required: bool
    case_type: str | None
    case_id: str | None = None
    user_message: str
    audit_event_type: str
    estimate: BuySellEstimate | None
