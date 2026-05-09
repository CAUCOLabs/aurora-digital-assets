from pydantic import BaseModel


class ReportSummary(BaseModel):
    report_id: str
    report_type: str
    title: str
    description: str
    status: str
    generated_from: str
    item_count: int


class TaxSummary(BaseModel):
    year: int
    total_purchases_eur: float
    total_sales_eur: float
    digital_asset_payments_eur: float
    external_transfers_count: int
    pending_review_cases: int
    estimated_realized_gain_loss_eur: float
    disclaimer: str


class EvidencePackageRequest(BaseModel):
    case_id: str | None = None
    year: int | None = None


class EvidencePackageResponse(BaseModel):
    package_id: str
    status: str
    included_audit_events: int
    included_review_cases: int
    message: str
