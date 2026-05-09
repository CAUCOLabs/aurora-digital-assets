from fastapi import APIRouter

from app.schemas.audit_event import AuditEvent
from app.services.audit_service import audit_service


router = APIRouter(prefix="/audit-events", tags=["audit events"])


@router.get("", response_model=list[AuditEvent])
def list_audit_events() -> list[AuditEvent]:
    return audit_service.list_events()
