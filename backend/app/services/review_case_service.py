import json
from datetime import datetime, timezone
from sqlite3 import Row

from app.db.database import get_connection
from app.schemas.buy_sell import BuySellEvaluateRequest, BuySellEvaluateResponse
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
    """SQLite-backed case store for simulated compliance review workflows."""

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
        self._insert_case(case)
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
        self._insert_case(case)
        return case

    def create_buy_sell_case(
        self,
        request: BuySellEvaluateRequest,
        decision: BuySellEvaluateResponse,
    ) -> ReviewCase:
        asset = request.asset.strip().upper()
        gross_eur = decision.estimate.gross_eur if decision.estimate else 0.0
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "buy_sell_review",
            title="Digital asset buy/sell review",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=gross_eur,
            network="banking settlement",
            destination_address="Aurora Digital Assets Wallet",
            wallet_type="internal_custodial_wallet_concept",
        )
        self._insert_case(case)
        return case

    def list_cases(self) -> list[ReviewCase]:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                FROM review_cases
                ORDER BY case_id ASC
                """
            ).fetchall()

        return [self._row_to_case(row) for row in rows]

    def get_case(self, case_id: str) -> ReviewCase | None:
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                FROM review_cases
                WHERE case_id = ?
                """,
                (case_id,),
            ).fetchone()

        if row is None:
            return None
        return self._row_to_case(row)

    def record_decision(
        self,
        case_id: str,
        decision: str,
        notes: str | None,
    ) -> ReviewCase | None:
        case = self.get_case(case_id)
        if case is None:
            return None

        status = REVIEW_DECISION_STATUSES[decision]
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE review_cases
                SET reviewer_decision = ?,
                    reviewer_notes = ?,
                    status = ?
                WHERE case_id = ?
                """,
                (decision, notes, status, case_id),
            )

        return self.get_case(case_id)

    def _next_case_id(self) -> str:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT case_id FROM review_cases"
            ).fetchall()

        sequence_numbers = [
            int(row["case_id"].rsplit("-", 1)[-1])
            for row in rows
            if row["case_id"].startswith("CASE-DA-2026-")
        ]
        next_sequence = max(sequence_numbers, default=0) + 1
        return f"CASE-DA-2026-{next_sequence:03d}"

    def _insert_case(self, case: ReviewCase) -> None:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO review_cases (
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    case.case_id,
                    case.created_at,
                    case.case_type,
                    case.title,
                    case.status,
                    case.risk_level,
                    json.dumps(case.reasons),
                    case.customer,
                    case.action_type,
                    case.asset,
                    case.amount,
                    case.network,
                    case.destination_address,
                    case.wallet_type,
                    case.reviewer_decision,
                    case.reviewer_notes,
                ),
            )

    def _row_to_case(self, row: Row) -> ReviewCase:
        return ReviewCase(
            case_id=row["case_id"],
            created_at=row["created_at"],
            case_type=row["case_type"],
            title=row["title"],
            status=row["status"],
            risk_level=row["risk_level"],
            reasons=json.loads(row["reasons"]),
            customer=row["customer"],
            action_type=row["action_type"],
            asset=row["asset"],
            amount=row["amount"],
            network=row["network"],
            destination_address=row["destination_address"],
            wallet_type=row["wallet_type"],
            reviewer_decision=row["reviewer_decision"],
            reviewer_notes=row["reviewer_notes"],
        )


review_case_service = ReviewCaseService()
