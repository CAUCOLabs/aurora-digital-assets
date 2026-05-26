import json
import sqlite3
from datetime import datetime, timezone

from app.db.database import get_connection
from app.schemas.audit_event import AuditEvent
from app.schemas.demo_admin import (
    DemoResetResponse,
    DemoSeedResponse,
    DemoStatusResponse,
)
from app.schemas.review_case import ReviewCase


class DemoAdminService:
    """Local prototype controls for seeded audit and compliance review data."""

    def get_status(self) -> DemoStatusResponse:
        with get_connection() as connection:
            audit_events_count = connection.execute(
                "SELECT COUNT(*) FROM audit_events"
            ).fetchone()[0]
            case_counts = connection.execute(
                """
                SELECT
                    COUNT(*) AS total,
                    SUM(CASE WHEN status = 'Pending review' THEN 1 ELSE 0 END)
                        AS pending,
                    SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END)
                        AS approved,
                    SUM(CASE WHEN status = 'Rejected' THEN 1 ELSE 0 END)
                        AS rejected
                FROM review_cases
                """
            ).fetchone()

        return DemoStatusResponse(
            audit_events_count=audit_events_count,
            review_cases_count=case_counts["total"],
            pending_cases_count=case_counts["pending"] or 0,
            approved_cases_count=case_counts["approved"] or 0,
            rejected_cases_count=case_counts["rejected"] or 0,
            database="SQLite local prototype database",
            message="Local demo environment status loaded.",
        )

    def reset_demo_data(self) -> DemoResetResponse:
        with get_connection() as connection:
            deleted_audit_events, deleted_review_cases = self._clear_data(connection)

        return DemoResetResponse(
            status="cleared",
            deleted_audit_events=deleted_audit_events,
            deleted_review_cases=deleted_review_cases,
            message="Local demo audit events and review cases were cleared.",
        )

    def seed_demo_data(self) -> DemoSeedResponse:
        timestamp = datetime.now(timezone.utc).isoformat()
        review_cases = self._build_seed_cases(timestamp)
        audit_events = self._build_seed_audit_events(timestamp)

        with get_connection() as connection:
            self._clear_data(connection)
            self._insert_review_cases(connection, review_cases)
            self._insert_audit_events(connection, audit_events)

        return DemoSeedResponse(
            status="seeded",
            created_audit_events=len(audit_events),
            created_review_cases=len(review_cases),
            message="Local demo audit events and review cases were seeded.",
        )

    def _clear_data(self, connection: sqlite3.Connection) -> tuple[int, int]:
        audit_cursor = connection.execute("DELETE FROM audit_events")
        review_case_cursor = connection.execute("DELETE FROM review_cases")
        return audit_cursor.rowcount, review_case_cursor.rowcount

    def _build_seed_cases(self, timestamp: str) -> list[ReviewCase]:
        return [
            ReviewCase(
                case_id="CASE-DA-2026-001",
                created_at=timestamp,
                case_type="external_withdrawal_review",
                title="External BTC withdrawal",
                status="Pending review",
                risk_level="medium",
                reasons=["first_time_external_address"],
                customer="Claudio Demo",
                action_type="withdrawal_pending_review",
                asset="BTC",
                amount=0.1,
                network="Bitcoin",
                destination_address="demo-btc-external-address",
                wallet_type="external_wallet",
            ),
            ReviewCase(
                case_id="CASE-DA-2026-002",
                created_at=timestamp,
                case_type="digital_asset_payment_review",
                title="Digital asset invoice payment",
                status="Approved",
                risk_level="medium",
                reasons=[
                    "eligible_business_recipient",
                    "high_value_digital_asset_payment",
                ],
                customer="Claudio Demo",
                action_type="digital_asset_payment_pending_review",
                asset="USDC",
                amount=750.0,
                network="banking settlement",
                destination_address="Aurora Telecom Oyj",
                wallet_type="verified_business_recipient",
                reviewer_decision="approve",
                reviewer_notes=(
                    "Simulated reviewer approved the payment after reviewing "
                    "the evidence timeline."
                ),
            ),
            ReviewCase(
                case_id="CASE-DA-2026-003",
                created_at=timestamp,
                case_type="buy_sell_review",
                title="Digital asset buy/sell review",
                status="Pending review",
                risk_level="medium",
                reasons=["supported_asset", "high_value_buy_request"],
                customer="Claudio Demo",
                action_type="buy_sell_pending_review",
                asset="BTC",
                amount=750.0,
                network="banking settlement",
                destination_address="Aurora Digital Assets Wallet",
                wallet_type="internal_custodial_wallet_concept",
            ),
        ]

    def _build_seed_audit_events(self, timestamp: str) -> list[AuditEvent]:
        return [
            AuditEvent(
                event_id="AUDIT-DA-2026-001",
                timestamp=timestamp,
                module="withdrawals",
                action_type="withdrawal_pending_review",
                status="pending_review",
                risk_level="medium",
                decision="pending_review",
                reasons=["first_time_external_address"],
                case_id="CASE-DA-2026-001",
                user_message=(
                    "Your external transfer request is pending security review."
                ),
            ),
            AuditEvent(
                event_id="AUDIT-DA-2026-002",
                timestamp=timestamp,
                module="payments",
                action_type="digital_asset_payment_pending_review",
                status="pending_review",
                risk_level="medium",
                decision="pending_review",
                reasons=[
                    "eligible_business_recipient",
                    "high_value_digital_asset_payment",
                ],
                case_id="CASE-DA-2026-002",
                user_message=(
                    "Your digital asset payment request is pending security review."
                ),
            ),
            AuditEvent(
                event_id="AUDIT-DA-2026-003",
                timestamp=timestamp,
                module="review_cases",
                action_type="reviewer_decision_recorded",
                status="Approved",
                reasons=[],
                case_id="CASE-DA-2026-002",
                user_message="Reviewer decision recorded.",
            ),
            AuditEvent(
                event_id="AUDIT-DA-2026-004",
                timestamp=timestamp,
                module="buy_sell",
                action_type="buy_sell_pending_review",
                status="pending_review",
                risk_level="medium",
                decision="pending_review",
                reasons=["supported_asset", "high_value_buy_request"],
                case_id="CASE-DA-2026-003",
                user_message="Your simulated buy request is pending security review.",
            ),
        ]

    def _insert_review_cases(
        self,
        connection: sqlite3.Connection,
        review_cases: list[ReviewCase],
    ) -> None:
        connection.executemany(
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
            [
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
                )
                for case in review_cases
            ],
        )

    def _insert_audit_events(
        self,
        connection: sqlite3.Connection,
        audit_events: list[AuditEvent],
    ) -> None:
        connection.executemany(
            """
            INSERT INTO audit_events (
                event_id,
                timestamp,
                module,
                action_type,
                status,
                risk_level,
                decision,
                reasons,
                case_id,
                user_message
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    event.event_id,
                    event.timestamp,
                    event.module,
                    event.action_type,
                    event.status,
                    event.risk_level,
                    event.decision,
                    json.dumps(event.reasons),
                    event.case_id,
                    event.user_message,
                )
                for event in audit_events
            ],
        )


demo_admin_service = DemoAdminService()
