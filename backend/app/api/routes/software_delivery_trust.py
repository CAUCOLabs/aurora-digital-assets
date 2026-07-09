from fastapi import APIRouter

from app.schemas.software_delivery_trust import (
    SoftwareDeliveryGovernanceSummaryRequest,
    SoftwareDeliveryGovernanceSummaryResponse,
    SoftwareDeliveryIssueEvaluationRequest,
    SoftwareDeliveryIssueEvaluationResponse,
    SoftwareDeliveryProjectEvaluationRequest,
    SoftwareDeliveryProjectEvaluationResponse,
    SoftwareDeliveryReleaseGateRequest,
    SoftwareDeliveryReleaseGateResponse,
)
from app.services.software_delivery_trust_service import (
    control_matrix,
    evaluate_issue,
    evaluate_project,
    evaluate_release_gate,
    governance_summary,
)

router = APIRouter(
    prefix="/api/software-delivery-trust",
    tags=["software-delivery-trust"],
)


@router.get("/control-matrix")
def get_control_matrix() -> dict:
    return control_matrix()


@router.post("/evaluate-issue", response_model=SoftwareDeliveryIssueEvaluationResponse)
def post_evaluate_issue(
    request: SoftwareDeliveryIssueEvaluationRequest,
) -> SoftwareDeliveryIssueEvaluationResponse:
    return evaluate_issue(request)


@router.post("/evaluate-project", response_model=SoftwareDeliveryProjectEvaluationResponse)
def post_evaluate_project(
    request: SoftwareDeliveryProjectEvaluationRequest,
) -> SoftwareDeliveryProjectEvaluationResponse:
    return evaluate_project(request)


@router.post("/release-gate", response_model=SoftwareDeliveryReleaseGateResponse)
def post_release_gate(
    request: SoftwareDeliveryReleaseGateRequest,
) -> SoftwareDeliveryReleaseGateResponse:
    return evaluate_release_gate(request)


@router.post("/governance-summary", response_model=SoftwareDeliveryGovernanceSummaryResponse)
def post_governance_summary(
    request: SoftwareDeliveryGovernanceSummaryRequest,
) -> SoftwareDeliveryGovernanceSummaryResponse:
    return governance_summary(request)
