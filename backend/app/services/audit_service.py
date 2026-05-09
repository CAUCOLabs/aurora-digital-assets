from datetime import datetime, timezone

from app.schemas.audit_event import AuditEvent


class AuditService:
    """In-memory audit log for deterministic prototype events."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

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
        self._events.append(event)
        return event

    def list_events(self) -> list[AuditEvent]:
        return list(self._events)

    def _next_event_id(self) -> str:
        return f"AUDIT-DA-2026-{len(self._events) + 1:03d}"


audit_service = AuditService()
