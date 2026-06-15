from fastapi import APIRouter, HTTPException

from app.schemas.risk_operations import (
    EscalationSummary,
    RiskActionItem,
    RiskOperationsOverview,
    RiskOperationsReviewCaseRequest,
    RiskOperationsReviewCaseResponse,
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


@router.post(
    "/create-review-case",
    response_model=RiskOperationsReviewCaseResponse,
)
def create_risk_operations_review_case(
    request: RiskOperationsReviewCaseRequest,
) -> RiskOperationsReviewCaseResponse:
    response = risk_operations_service.create_review_case(
        action_id=request.action_id,
        reviewer_id=request.reviewer_id,
        priority=request.priority,
    )
    if response is None:
        raise HTTPException(status_code=404, detail="Risk action not found")
    return response
