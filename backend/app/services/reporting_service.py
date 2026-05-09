from app.schemas.audit_event import AuditEvent
from app.schemas.report import (
    EvidencePackageRequest,
    EvidencePackageResponse,
    ReportSummary,
    TaxSummary,
)
from app.schemas.review_case import ReviewCase
from app.services.audit_service import AuditService, audit_service
from app.services.review_case_service import (
    ReviewCaseService,
    review_case_service,
)


class ReportingService:
    """Builds simulated reports from persisted prototype evidence."""

    _package_sequence = 0

    def __init__(
        self,
        audit_log: AuditService | None = None,
        review_cases: ReviewCaseService | None = None,
    ) -> None:
        self.audit_log = audit_log or audit_service
        self.review_cases = review_cases or review_case_service

    def list_reports(self) -> list[ReportSummary]:
        audit_events = self.audit_log.list_events()
        cases = self.review_cases.list_cases()
        withdrawal_cases = self._cases_by_type(cases, "external_withdrawal_review")
        payment_cases = self._cases_by_type(cases, "digital_asset_payment_review")

        return [
            ReportSummary(
                report_id="REPORT-DA-2026-001",
                report_type="account_documents",
                title="Account documents",
                description=(
                    "Simulated account statements and payment receipts available "
                    "for the banking prototype."
                ),
                status="Ready",
                generated_from="mock banking documents",
                item_count=4,
            ),
            ReportSummary(
                report_id="REPORT-DA-2026-002",
                report_type="digital_asset_annual_summary",
                title="Digital asset annual summary",
                description=(
                    "Prototype annual summary combining simulated wallet, payment, "
                    "and review evidence."
                ),
                status="Ready",
                generated_from="persisted audit events and review cases",
                item_count=len(audit_events) + len(cases),
            ),
            ReportSummary(
                report_id="REPORT-DA-2026-003",
                report_type="audit_evidence_package",
                title="Audit evidence package",
                description=(
                    "Evidence package concept for audit trail and manual review "
                    "records. No real file is generated."
                ),
                status="Available",
                generated_from="persisted audit events",
                item_count=len(audit_events),
            ),
            ReportSummary(
                report_id="REPORT-DA-2026-004",
                report_type="external_withdrawal_review_report",
                title="External withdrawal review report",
                description=(
                    "Simulated report of external wallet withdrawal cases and "
                    "review decisions."
                ),
                status="Ready",
                generated_from="persisted review cases",
                item_count=len(withdrawal_cases),
            ),
            ReportSummary(
                report_id="REPORT-DA-2026-005",
                report_type="digital_asset_payment_report",
                title="Digital asset payment report",
                description=(
                    "Simulated report of controlled digital asset invoice payment "
                    "review cases."
                ),
                status="Ready",
                generated_from="persisted review cases",
                item_count=len(payment_cases),
            ),
        ]

    def get_tax_summary(self, year: int) -> TaxSummary:
        cases = self.review_cases.list_cases()
        payment_cases = self._cases_by_type(cases, "digital_asset_payment_review")
        withdrawal_cases = self._cases_by_type(cases, "external_withdrawal_review")
        pending_cases = [case for case in cases if case.status == "Pending review"]

        return TaxSummary(
            year=year,
            total_purchases_eur=75.0,
            total_sales_eur=0.0,
            digital_asset_payments_eur=sum(case.amount for case in payment_cases),
            external_transfers_count=len(withdrawal_cases),
            pending_review_cases=len(pending_cases),
            estimated_realized_gain_loss_eur=0.0,
            disclaimer="Prototype values only. This is not official tax advice.",
        )

    def create_evidence_package(
        self,
        request: EvidencePackageRequest,
    ) -> EvidencePackageResponse:
        audit_events = self.audit_log.list_events()
        cases = self.review_cases.list_cases()

        if request.case_id:
            included_audit_events = [
                event for event in audit_events if event.case_id == request.case_id
            ]
            included_review_cases = [
                case for case in cases if case.case_id == request.case_id
            ]
        else:
            included_audit_events = audit_events
            included_review_cases = cases

        package_scope = (
            f"case {request.case_id}"
            if request.case_id
            else f"year {request.year}"
            if request.year
            else "current prototype evidence"
        )

        return EvidencePackageResponse(
            package_id=self._generate_package_id(),
            status="Prepared",
            included_audit_events=len(included_audit_events),
            included_review_cases=len(included_review_cases),
            message=(
                "Simulated evidence package prepared for "
                f"{package_scope}. No PDF or CSV file was generated."
            ),
        )

    def _cases_by_type(
        self,
        cases: list[ReviewCase],
        case_type: str,
    ) -> list[ReviewCase]:
        return [case for case in cases if case.case_type == case_type]

    def _generate_package_id(self) -> str:
        ReportingService._package_sequence += 1
        return f"EVIDENCE-DA-2026-{ReportingService._package_sequence:03d}"


reporting_service = ReportingService()
