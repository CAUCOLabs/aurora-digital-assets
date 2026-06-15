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
from app.storage.sqlite_store import (
    get_review_case_by_id,
    list_persisted_review_cases,
    save_review_case,
)


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

    def create_risk_operations_case(
        self,
        *,
        title: str,
        summary: str,
        required_action: str,
        missing_evidence: list[str],
        source_action_id: str,
        source_id: str,
        reviewer_id: str,
        priority: str,
        risk_type: str,
    ) -> ReviewCase:
        reasons = [
            summary,
            f"Required action: {required_action}",
            f"Source action: {source_action_id}",
            f"Assigned reviewer: {reviewer_id}",
        ]
        if missing_evidence:
            reasons.append(
                "Missing evidence: " + ", ".join(missing_evidence)
            )

        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type="risk_operations_review",
            title=title,
            status="Pending review",
            risk_level=priority,
            reasons=reasons,
            customer="Aurora Bank internal prototype",
            action_type="risk_operations_review_case_prepared",
            asset="digital_assets_controls",
            amount=0.0,
            network="internal_review_workflow",
            destination_address=source_id,
            wallet_type=risk_type,
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

        return self._merge_cases(
            [self._row_to_case(row) for row in rows],
            list_persisted_review_cases(),
        )

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
            return get_review_case_by_id(case_id)
        return self._row_to_case(row)

    def list_persisted_cases(self) -> list[ReviewCase]:
        return list_persisted_review_cases()

    def persist_case_trace(
        self,
        case: ReviewCase,
        *,
        source_module: str | None = None,
        source_id: str | None = None,
        source_action_id: str | None = None,
        reviewer_id: str | None = None,
        recommended_next_action: str | None = None,
        audit_event_id: str | None = None,
        correlation_id: str | None = None,
        metadata: dict | None = None,
    ) -> ReviewCase:
        return save_review_case(
            case,
            source_module=source_module,
            source_id=source_id,
            source_action_id=source_action_id,
            reviewer_id=reviewer_id,
            recommended_next_action=recommended_next_action,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            metadata=metadata,
        )

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
                INSERT OR REPLACE INTO review_cases (
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
        save_review_case(case)

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

    def _merge_cases(
        self,
        base_cases: list[ReviewCase],
        persisted_cases: list[ReviewCase],
    ) -> list[ReviewCase]:
        merged = {case.case_id: case for case in base_cases}
        for case in persisted_cases:
            merged[case.case_id] = case
        return sorted(merged.values(), key=lambda case: case.case_id)


review_case_service = ReviewCaseService()
