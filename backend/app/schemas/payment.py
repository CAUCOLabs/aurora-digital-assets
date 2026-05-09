from pydantic import BaseModel


class DigitalAssetPaymentEvaluateRequest(BaseModel):
    recipient_name: str
    invoice_number: str
    reference_number: str
    amount_eur: float
    payment_asset: str
    source_account_id: str


class DigitalAssetPaymentEstimate(BaseModel):
    invoice_amount_eur: float
    payment_asset: str
    estimated_asset_amount: float
    conversion_rate_eur: float
    service_fee_eur: float
    settlement_fee_eur: float
    total_estimated_cost_eur: float
    recipient_settlement: str


class DigitalAssetPaymentEvaluateResponse(BaseModel):
    decision: str
    risk_level: str
    reasons: list[str]
    case_required: bool
    case_type: str | None
    case_id: str | None = None
    user_message: str
    audit_event_type: str
    estimate: DigitalAssetPaymentEstimate | None
