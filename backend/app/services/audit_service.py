import json
from datetime import datetime, timezone
from sqlite3 import Row

from app.db.database import get_connection
from app.schemas.audit_event import AuditEvent


class AuditService:
    """SQLite-backed audit log for deterministic prototype events."""

    def record_event(
        self,
        module: str,
        action_type: str,
        status: str,
        risk_level: str | None = None,
        decision: str | None = None,
        reasons: list[str] | None = None,
        case_id: str | None = None,
        user_message: str | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            event_id=self._next_event_id(),
            timestamp=datetime.now(timezone.utc).isoformat(),
            module=module,
            action_type=action_type,
            status=status,
            risk_level=risk_level,
            decision=decision,
            reasons=reasons or [],
            case_id=case_id,
            user_message=user_message,
        )

        with get_connection() as connection:
            connection.execute(
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
                ),
            )

        return event

    def list_events(self) -> list[AuditEvent]:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
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
                FROM audit_events
                ORDER BY event_id ASC
                """
            ).fetchall()

        return [self._row_to_event(row) for row in rows]

    def _next_event_id(self) -> str:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT event_id FROM audit_events"
            ).fetchall()

        sequence_numbers = [
            int(row["event_id"].rsplit("-", 1)[-1])
            for row in rows
            if row["event_id"].startswith("AUDIT-DA-2026-")
        ]
        next_sequence = max(sequence_numbers, default=0) + 1
        return f"AUDIT-DA-2026-{next_sequence:03d}"

    def _row_to_event(self, row: Row) -> AuditEvent:
        return AuditEvent(
            event_id=row["event_id"],
            timestamp=row["timestamp"],
            module=row["module"],
            action_type=row["action_type"],
            status=row["status"],
            risk_level=row["risk_level"],
            decision=row["decision"],
            reasons=json.loads(row["reasons"]),
            case_id=row["case_id"],
            user_message=row["user_message"],
        )


audit_service = AuditService()
