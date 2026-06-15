import json
from datetime import datetime, timezone
from sqlite3 import Row
from typing import Any

from app.db.database import get_connection
from app.schemas.audit_event import AuditEvent
from app.storage.sqlite_store import (
    get_audit_event_by_id,
    list_persisted_audit_events,
    save_audit_event,
)


EXTENDED_AUDIT_COLUMNS = {
    "actor_id": "TEXT",
    "actor_type": "TEXT",
    "source_module": "TEXT",
    "action": "TEXT",
    "object_type": "TEXT",
    "object_id": "TEXT",
    "severity": "TEXT",
    "risk_score": "INTEGER",
    "summary": "TEXT",
    "evidence_reference": "TEXT",
    "review_case_id": "TEXT",
    "correlation_id": "TEXT",
    "immutable_note": "TEXT",
    "metadata": "TEXT",
}


DEMO_AUDIT_EVENTS = [
    AuditEvent(
        event_id="AUD-RISK-RO-ACTION-002",
        timestamp="2026-06-14T08:45:00+03:00",
        module="risk_operations",
        action_type="create_review_case",
        status="created",
        risk_level="urgent",
        decision="review_case_prepared",
        reasons=["Shell company evidence review prepared from Risk Operations."],
        case_id="CASE-FC-2026-002",
        user_message="Review case prepared from Risk Operations.",
        actor_id="reviewer-demo",
        actor_type="staff",
        source_module="risk_operations",
        action="prepare_review_case",
        object_type="risk_action",
        object_id="RO-ACTION-002",
        severity="urgent",
        summary="Review case prepared from Risk Operations.",
        evidence_reference="EP-2026-002",
        review_case_id="CASE-FC-2026-002",
        correlation_id="CORR-RISK-RO-ACTION-002",
        immutable_note="Prototype audit trace for sensitive Risk Operations action.",
        metadata={"prototype": True},
    ),
    AuditEvent(
        event_id="AUD-API-GRAPHQL-PIN",
        timestamp="2026-06-14T09:20:00+03:00",
        module="api_security",
        action_type="evaluate_scenario",
        status="created",
        risk_level="high",
        decision="step_up_required",
        reasons=["API security decision for GraphQL batching PIN verification."],
        user_message="API security scenario evaluation recorded.",
        actor_id="api-security-engine",
        actor_type="service",
        source_module="api_security",
        action="evaluate_scenario",
        object_type="api_scenario",
        object_id="graphql_batching_pin_verification",
        severity="high",
        risk_score=70,
        summary="API security decision for GraphQL batching PIN verification.",
        correlation_id="CORR-API-GRAPHQL-PIN",
        immutable_note="Prototype audit trace for sensitive API backend decision.",
        metadata={"operation_name": "verifyTransferPin"},
    ),
    AuditEvent(
        event_id="AUD-OPS-PAYMENTS-DEGRADED",
        timestamp="2026-06-14T10:15:00+03:00",
        module="operational_resilience",
        action_type="evaluate_scenario",
        status="created",
        risk_level="high",
        decision="pause_sensitive_operations",
        reasons=["Operational resilience decision for degraded payments dependency."],
        user_message="Operational resilience scenario evaluation recorded.",
        actor_id="resilience-engine",
        actor_type="service",
        source_module="operational_resilience",
        action="evaluate_scenario",
        object_type="resilience_scenario",
        object_id="payment_dependency_failure",
        severity="high",
        risk_score=85,
        summary="Operational resilience decision for degraded payments dependency.",
        correlation_id="CORR-OPS-PAYMENTS-DEGRADED",
        immutable_note="Prototype audit trace for operational control activation.",
        metadata={"affected_service": "payments"},
    ),
    AuditEvent(
        event_id="AUD-EVIDENCE-FCA-2026-002",
        timestamp="2026-06-14T08:50:00+03:00",
        module="evidence_packages",
        action_type="generate_package",
        status="created",
        risk_level="critical",
        decision="evidence_package_prepared",
        reasons=["Evidence package prepared from financial crime alert."],
        user_message="Evidence package generation recorded.",
        actor_id="reviewer-demo",
        actor_type="staff",
        source_module="evidence_packages",
        action="generate_package",
        object_type="financial_crime_alert",
        object_id="FCA-2026-002",
        severity="critical",
        summary="Evidence package prepared from financial crime alert.",
        evidence_reference="EP-2026-002",
        correlation_id="CORR-EVIDENCE-FCA-2026-002",
        immutable_note="Prototype audit trace for evidence preparation.",
        metadata={"package_type": "internal_review"},
    ),
]


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
        self._ensure_extended_columns()
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
        self._upsert_extended_event(event)
        save_audit_event(event)
        return event

    def create_audit_event_from_sensitive_action(
        self,
        *,
        event_id: str,
        actor_id: str,
        actor_type: str,
        source_module: str,
        action: str,
        object_type: str,
        object_id: str,
        decision: str,
        severity: str,
        summary: str,
        correlation_id: str,
        risk_score: int | None = None,
        evidence_reference: str | None = None,
        review_case_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> AuditEvent:
        self._ensure_extended_columns()
        event = AuditEvent(
            event_id=event_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            module=source_module,
            action_type=action,
            status="created",
            risk_level=severity,
            decision=decision,
            reasons=[summary],
            case_id=review_case_id,
            user_message="Sensitive action recorded in prototype audit trail.",
            actor_id=actor_id,
            actor_type=actor_type,
            source_module=source_module,
            action=action,
            object_type=object_type,
            object_id=object_id,
            severity=severity,
            risk_score=risk_score,
            summary=summary,
            evidence_reference=evidence_reference,
            review_case_id=review_case_id,
            correlation_id=correlation_id,
            immutable_note=(
                "Deterministic prototype audit record. No real bank data, "
                "customer data, or external system action was used."
            ),
            metadata=metadata or {},
        )
        self._upsert_extended_event(event)
        save_audit_event(event)
        return event

    def list_events(self) -> list[AuditEvent]:
        self._ensure_extended_columns()
        self._seed_demo_events()
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
                    user_message,
                    actor_id,
                    actor_type,
                    source_module,
                    action,
                    object_type,
                    object_id,
                    severity,
                    risk_score,
                    summary,
                    evidence_reference,
                    review_case_id,
                    correlation_id,
                    immutable_note,
                    metadata
                FROM audit_events
                ORDER BY event_id ASC
                """
            ).fetchall()

        return self._merge_events(
            [self._row_to_event(row) for row in rows],
            list_persisted_audit_events(),
        )

    def list_persisted_events(self) -> list[AuditEvent]:
        return list_persisted_audit_events()

    def get_persisted_event(self, event_id: str) -> AuditEvent | None:
        return get_audit_event_by_id(event_id)

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
            actor_id=row["actor_id"],
            actor_type=row["actor_type"],
            source_module=row["source_module"],
            action=row["action"],
            object_type=row["object_type"],
            object_id=row["object_id"],
            severity=row["severity"],
            risk_score=row["risk_score"],
            summary=row["summary"],
            evidence_reference=row["evidence_reference"],
            review_case_id=row["review_case_id"],
            correlation_id=row["correlation_id"],
            immutable_note=row["immutable_note"],
            metadata=json.loads(row["metadata"] or "{}"),
        )

    def _merge_events(
        self,
        base_events: list[AuditEvent],
        persisted_events: list[AuditEvent],
    ) -> list[AuditEvent]:
        merged = {event.event_id: event for event in base_events}
        for event in persisted_events:
            merged[event.event_id] = event
        return sorted(merged.values(), key=lambda event: event.event_id)

    def _ensure_extended_columns(self) -> None:
        with get_connection() as connection:
            existing_columns = {
                row["name"]
                for row in connection.execute("PRAGMA table_info(audit_events)")
            }
            for column_name, column_type in EXTENDED_AUDIT_COLUMNS.items():
                if column_name not in existing_columns:
                    connection.execute(
                        f"ALTER TABLE audit_events ADD COLUMN {column_name} {column_type}"
                    )

    def _seed_demo_events(self) -> None:
        for event in DEMO_AUDIT_EVENTS:
            if not self._event_exists(event.event_id):
                self._upsert_extended_event(event)

    def _event_exists(self, event_id: str) -> bool:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT 1 FROM audit_events WHERE event_id = ?",
                (event_id,),
            ).fetchone()
        return row is not None

    def _upsert_extended_event(self, event: AuditEvent) -> None:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO audit_events (
                    event_id,
                    timestamp,
                    module,
                    action_type,
                    status,
                    risk_level,
                    decision,
                    reasons,
                    case_id,
                    user_message,
                    actor_id,
                    actor_type,
                    source_module,
                    action,
                    object_type,
                    object_id,
                    severity,
                    risk_score,
                    summary,
                    evidence_reference,
                    review_case_id,
                    correlation_id,
                    immutable_note,
                    metadata
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                    event.actor_id,
                    event.actor_type,
                    event.source_module,
                    event.action,
                    event.object_type,
                    event.object_id,
                    event.severity,
                    event.risk_score,
                    event.summary,
                    event.evidence_reference,
                    event.review_case_id,
                    event.correlation_id,
                    event.immutable_note,
                    json.dumps(event.metadata),
                ),
            )


audit_service = AuditService()
