from fastapi import APIRouter, HTTPException

from app.schemas.compliance_intelligence import (
    ExplainAlertRequest,
    ExplainAlertResponse,
    PrepareReviewCaseRequest,
    PrepareReviewCaseResponse,
    ReviewerGuidance,
    RiskExplanation,
)
from app.services.compliance_intelligence_service import (
    compliance_intelligence_service,
)


router = APIRouter(
    prefix="/compliance-intelligence",
    tags=["compliance intelligence"],
)


@router.get("/risk-explanations", response_model=list[RiskExplanation])
def get_risk_explanations() -> list[RiskExplanation]:
    return compliance_intelligence_service.list_risk_explanations()


@router.get("/reviewer-guidance", response_model=list[ReviewerGuidance])
def get_reviewer_guidance() -> list[ReviewerGuidance]:
    return compliance_intelligence_service.list_reviewer_guidance()


@router.post("/explain-alert", response_model=ExplainAlertResponse)
def explain_alert(request: ExplainAlertRequest) -> ExplainAlertResponse:
    try:
        return compliance_intelligence_service.explain_alert(
            alert_id=request.alert_id,
            include_evidence_requirements=request.include_evidence_requirements,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post(
    "/prepare-review-case",
    response_model=PrepareReviewCaseResponse,
)
def prepare_review_case(
    request: PrepareReviewCaseRequest,
) -> PrepareReviewCaseResponse:
    try:
        return compliance_intelligence_service.prepare_review_case(
            alert_id=request.alert_id,
            reviewer_id=request.reviewer_id,
            priority=request.priority,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
