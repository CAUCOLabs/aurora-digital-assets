from fastapi import APIRouter

from app.schemas.report import (
    EvidencePackageRequest,
    EvidencePackageResponse,
    ReportSummary,
    TaxSummary,
)
from app.services.reporting_service import ReportingService


router = APIRouter(prefix="/reports", tags=["reports"])
reporting_service = ReportingService()


@router.get("", response_model=list[ReportSummary])
def list_reports() -> list[ReportSummary]:
    return reporting_service.list_reports()


@router.get("/tax-summary/{year}", response_model=TaxSummary)
def get_tax_summary(year: int) -> TaxSummary:
    return reporting_service.get_tax_summary(year)


@router.post("/evidence-package", response_model=EvidencePackageResponse)
def create_evidence_package(
    request: EvidencePackageRequest,
) -> EvidencePackageResponse:
    return reporting_service.create_evidence_package(request)
