from fastapi import APIRouter

from app.schemas.risk_operations import (
    EscalationSummary,
    RiskActionItem,
    RiskOperationsOverview,
    UnifiedTimelineEvent,
)
from app.services.risk_operations_service import risk_operations_service


router = APIRouter(prefix="/risk-operations", tags=["risk operations"])


@router.get("/overview", response_model=RiskOperationsOverview)
def get_risk_operations_overview() -> RiskOperationsOverview:
    return risk_operations_service.get_overview()


@router.get("/action-queue", response_model=list[RiskActionItem])
def get_risk_operations_action_queue() -> list[RiskActionItem]:
    return risk_operations_service.list_action_queue()


@router.get("/unified-timeline", response_model=list[UnifiedTimelineEvent])
def get_risk_operations_unified_timeline() -> list[UnifiedTimelineEvent]:
    return risk_operations_service.list_unified_timeline()


@router.get("/escalation-summary", response_model=list[EscalationSummary])
def get_risk_operations_escalation_summary() -> list[EscalationSummary]:
    return risk_operations_service.list_escalation_summary()
