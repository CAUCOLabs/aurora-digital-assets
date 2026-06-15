import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from sqlite3 import Row
from typing import Any

from app.schemas.audit_event import AuditEvent
from app.schemas.review_case import ReviewCase


DATABASE_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_demo.db"


def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    """Create lightweight local prototype persistence tables."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT UNIQUE,
                timestamp TEXT,
                actor_id TEXT,
                actor_type TEXT,
                source_module TEXT,
                action TEXT,
                object_type TEXT,
                object_id TEXT,
                decision TEXT,
                severity TEXT,
                risk_score INTEGER NULL,
                summary TEXT,
                evidence_reference TEXT NULL,
                review_case_id TEXT NULL,
                correlation_id TEXT,
                immutable_note TEXT,
                metadata_json TEXT,
                created_at TEXT
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS review_cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                review_case_id TEXT UNIQUE,
                created_at TEXT,
                source_module TEXT,
                source_id TEXT,
                source_action_id TEXT NULL,
                title TEXT,
                summary TEXT,
                priority TEXT,
                status TEXT,
                reviewer_id TEXT,
                recommended_next_action TEXT,
                audit_event_id TEXT NULL,
                correlation_id TEXT,
                metadata_json TEXT
            )
            """
        )


def save_audit_event(event: AuditEvent) -> AuditEvent:
    init_db()
    created_at = datetime.now(timezone.utc).isoformat()
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO audit_events (
                event_id,
                timestamp,
                actor_id,
                actor_type,
                source_module,
                action,
                object_type,
                object_id,
                decision,
                severity,
                risk_score,
                summary,
                evidence_reference,
                review_case_id,
                correlation_id,
                immutable_note,
                metadata_json,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(event_id) DO UPDATE SET
                timestamp = excluded.timestamp,
                actor_id = excluded.actor_id,
                actor_type = excluded.actor_type,
                source_module = excluded.source_module,
                action = excluded.action,
                object_type = excluded.object_type,
                object_id = excluded.object_id,
                decision = excluded.decision,
                severity = excluded.severity,
                risk_score = excluded.risk_score,
                summary = excluded.summary,
                evidence_reference = excluded.evidence_reference,
                review_case_id = excluded.review_case_id,
                correlation_id = excluded.correlation_id,
                immutable_note = excluded.immutable_note,
                metadata_json = excluded.metadata_json
            """,
            (
                event.event_id,
                event.timestamp,
                event.actor_id,
                event.actor_type,
                event.source_module or event.module,
                event.action or event.action_type,
                event.object_type,
                event.object_id,
                event.decision,
                event.severity or event.risk_level,
                event.risk_score,
                event.summary or " ".join(event.reasons),
                event.evidence_reference,
                event.review_case_id or event.case_id,
                event.correlation_id,
                event.immutable_note,
                json.dumps(event.metadata),
                created_at,
            ),
        )
    event.persisted = True
    return event


def list_persisted_audit_events() -> list[AuditEvent]:
    init_db()
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT
                event_id,
                timestamp,
                actor_id,
                actor_type,
                source_module,
                action,
                object_type,
                object_id,
                decision,
                severity,
                risk_score,
                summary,
                evidence_reference,
                review_case_id,
                correlation_id,
                immutable_note,
                metadata_json
            FROM audit_events
            ORDER BY event_id ASC
            """
        ).fetchall()
    return [_row_to_audit_event(row) for row in rows]


def get_audit_event_by_id(event_id: str) -> AuditEvent | None:
    init_db()
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT
                event_id,
                timestamp,
                actor_id,
                actor_type,
                source_module,
                action,
                object_type,
                object_id,
                decision,
                severity,
                risk_score,
                summary,
                evidence_reference,
                review_case_id,
                correlation_id,
                immutable_note,
                metadata_json
            FROM audit_events
            WHERE event_id = ?
            """,
            (event_id,),
        ).fetchone()
    return _row_to_audit_event(row) if row else None


def save_review_case(
    case: ReviewCase,
    *,
    source_module: str | None = None,
    source_id: str | None = None,
    source_action_id: str | None = None,
    reviewer_id: str | None = None,
    recommended_next_action: str | None = None,
    audit_event_id: str | None = None,
    correlation_id: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> ReviewCase:
    init_db()
    merged_metadata = {
        "case_type": case.case_type,
        "risk_level": case.risk_level,
        "reasons": case.reasons,
        "customer": case.customer,
        "action_type": case.action_type,
        "asset": case.asset,
        "amount": case.amount,
        "network": case.network,
        "destination_address": case.destination_address,
        "wallet_type": case.wallet_type,
        "reviewer_decision": case.reviewer_decision,
        "reviewer_notes": case.reviewer_notes,
        **(metadata or {}),
    }
    summary = case.summary if hasattr(case, "summary") else None
    if summary is None:
        summary = " ".join(case.reasons)

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO review_cases (
                review_case_id,
                created_at,
                source_module,
                source_id,
                source_action_id,
                title,
                summary,
                priority,
                status,
                reviewer_id,
                recommended_next_action,
                audit_event_id,
                correlation_id,
                metadata_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(review_case_id) DO UPDATE SET
                created_at = excluded.created_at,
                source_module = excluded.source_module,
                source_id = excluded.source_id,
                source_action_id = excluded.source_action_id,
                title = excluded.title,
                summary = excluded.summary,
                priority = excluded.priority,
                status = excluded.status,
                reviewer_id = excluded.reviewer_id,
                recommended_next_action = excluded.recommended_next_action,
                audit_event_id = excluded.audit_event_id,
                correlation_id = excluded.correlation_id,
                metadata_json = excluded.metadata_json
            """,
            (
                case.case_id,
                case.created_at,
                source_module,
                source_id,
                source_action_id,
                case.title,
                summary,
                case.risk_level,
                case.status,
                reviewer_id,
                recommended_next_action,
                audit_event_id,
                correlation_id,
                json.dumps(merged_metadata),
            ),
        )

    case.persisted = True
    case.source_module = source_module
    case.source_id = source_id
    case.source_action_id = source_action_id
    case.reviewer_id = reviewer_id
    case.recommended_next_action = recommended_next_action
    case.audit_event_id = audit_event_id
    case.correlation_id = correlation_id
    case.metadata = merged_metadata
    return case


def list_persisted_review_cases() -> list[ReviewCase]:
    init_db()
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT
                review_case_id,
                created_at,
                source_module,
                source_id,
                source_action_id,
                title,
                summary,
                priority,
                status,
                reviewer_id,
                recommended_next_action,
                audit_event_id,
                correlation_id,
                metadata_json
            FROM review_cases
            ORDER BY review_case_id ASC
            """
        ).fetchall()
    return [_row_to_review_case(row) for row in rows]


def get_review_case_by_id(review_case_id: str) -> ReviewCase | None:
    init_db()
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT
                review_case_id,
                created_at,
                source_module,
                source_id,
                source_action_id,
                title,
                summary,
                priority,
                status,
                reviewer_id,
                recommended_next_action,
                audit_event_id,
                correlation_id,
                metadata_json
            FROM review_cases
            WHERE review_case_id = ?
            """,
            (review_case_id,),
        ).fetchone()
    return _row_to_review_case(row) if row else None


def _row_to_audit_event(row: Row) -> AuditEvent:
    metadata = json.loads(row["metadata_json"] or "{}")
    return AuditEvent(
        event_id=row["event_id"],
        timestamp=row["timestamp"],
        module=row["source_module"] or "audit_events",
        action_type=row["action"] or "stored_event",
        status="created",
        risk_level=row["severity"],
        decision=row["decision"],
        reasons=[row["summary"]] if row["summary"] else [],
        case_id=row["review_case_id"],
        user_message="Stored locally in SQLite prototype storage.",
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
        metadata=metadata,
        persisted=True,
    )


def _row_to_review_case(row: Row) -> ReviewCase:
    metadata = json.loads(row["metadata_json"] or "{}")
    return ReviewCase(
        case_id=row["review_case_id"],
        created_at=row["created_at"],
        case_type=metadata.get("case_type", "local_persisted_review"),
        title=row["title"],
        status=row["status"],
        risk_level=row["priority"] or "medium",
        reasons=metadata.get("reasons", [row["summary"]] if row["summary"] else []),
        customer=metadata.get("customer", "Aurora Bank internal prototype"),
        action_type=metadata.get("action_type", "review_case_prepared"),
        asset=metadata.get("asset", "digital_assets_controls"),
        amount=metadata.get("amount", 0.0),
        network=metadata.get("network", "internal_review_workflow"),
        destination_address=metadata.get("destination_address", row["source_id"] or ""),
        wallet_type=metadata.get("wallet_type", "internal_review"),
        reviewer_decision=metadata.get("reviewer_decision"),
        reviewer_notes=metadata.get("reviewer_notes"),
        persisted=True,
        source_module=row["source_module"],
        source_id=row["source_id"],
        source_action_id=row["source_action_id"],
        reviewer_id=row["reviewer_id"],
        recommended_next_action=row["recommended_next_action"],
        audit_event_id=row["audit_event_id"],
        correlation_id=row["correlation_id"],
        metadata=metadata,
    )
