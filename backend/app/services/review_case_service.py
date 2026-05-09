from datetime import datetime, timezone

from app.schemas.payment import (
    DigitalAssetPaymentEvaluateRequest,
    DigitalAssetPaymentEvaluateResponse,
)
from app.schemas.review_case import ReviewCase
from app.schemas.risk_review import RiskDecisionResponse
from app.schemas.withdrawal import WithdrawalEvaluateRequest


REVIEW_DECISION_STATUSES = {
    "approve": "Approved",
    "reject": "Rejected",
    "request_information": "More information needed",
    "delay": "Delayed",
    "escalate": "Escalated",
}


class ReviewCaseService:
    """In-memory case store for simulated compliance review workflows."""

    def __init__(self) -> None:
        self._cases: list[ReviewCase] = []

    def create_withdrawal_case(
        self,
        request: WithdrawalEvaluateRequest,
        decision: RiskDecisionResponse,
    ) -> ReviewCase:
        asset = request.asset.strip().upper()
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "external_withdrawal_review",
            title=f"External {asset} withdrawal",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=request.amount,
            network=request.network.strip(),
            destination_address=request.destination_address.strip(),
            wallet_type=request.wallet_type.strip(),
        )
        self._cases.append(case)
        return case

    def create_digital_asset_payment_case(
        self,
        request: DigitalAssetPaymentEvaluateRequest,
        decision: DigitalAssetPaymentEvaluateResponse,
    ) -> ReviewCase:
        asset = request.payment_asset.strip().upper()
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "digital_asset_payment_review",
            title="Digital asset invoice payment",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=request.amount_eur,
            network="banking settlement",
            destination_address=request.recipient_name.strip(),
            wallet_type="verified_business_recipient",
        )
        self._cases.append(case)
        return case

    def list_cases(self) -> list[ReviewCase]:
        return list(self._cases)

    def get_case(self, case_id: str) -> ReviewCase | None:
        for case in self._cases:
            if case.case_id == case_id:
                return case
        return None

    def record_decision(
        self,
        case_id: str,
        decision: str,
        notes: str | None,
    ) -> ReviewCase | None:
        case = self.get_case(case_id)
        if case is None:
            return None

        case.reviewer_decision = decision
        case.reviewer_notes = notes
        case.status = REVIEW_DECISION_STATUSES[decision]
        return case

    def _next_case_id(self) -> str:
        return f"CASE-DA-2026-{len(self._cases) + 1:03d}"


review_case_service = ReviewCaseService()
