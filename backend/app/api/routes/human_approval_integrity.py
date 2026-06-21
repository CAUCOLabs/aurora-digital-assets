from fastapi import APIRouter

from app.schemas.human_approval_integrity import (
    HumanApprovalIntegrityEvaluationRequest,
    HumanApprovalIntegrityEvaluationResponse,
    HumanApprovalIntegrityRiskSignalsResponse,
    HumanApprovalIntegrityRulesResponse,
    HumanDualControlPreviewRequest,
    HumanDualControlPreviewResponse,
    HumanSensitiveApprovalIntegrityRequest,
    HumanSensitiveApprovalIntegrityResponse,
)
from app.services.human_approval_integrity_service import (
    human_approval_integrity_service,
)


router = APIRouter(
    prefix="/human-approval-integrity",
    tags=["human approval integrity"],
)


@router.get("/rules", response_model=HumanApprovalIntegrityRulesResponse)
def get_rules() -> HumanApprovalIntegrityRulesResponse:
    return human_approval_integrity_service.rules()


@router.get("/risk-signals", response_model=HumanApprovalIntegrityRiskSignalsResponse)
def get_risk_signals() -> HumanApprovalIntegrityRiskSignalsResponse:
    return human_approval_integrity_service.risk_signals()


@router.post("/evaluate", response_model=HumanApprovalIntegrityEvaluationResponse)
def evaluate_human_approval_integrity(
    request: HumanApprovalIntegrityEvaluationRequest,
) -> HumanApprovalIntegrityEvaluationResponse:
    return human_approval_integrity_service.evaluate(request)


@router.post(
    "/evaluate-sensitive-approval",
    response_model=HumanSensitiveApprovalIntegrityResponse,
)
def evaluate_sensitive_approval(
    request: HumanSensitiveApprovalIntegrityRequest,
) -> HumanSensitiveApprovalIntegrityResponse:
    return human_approval_integrity_service.evaluate_sensitive_approval(request)


@router.post(
    "/dual-control-preview",
    response_model=HumanDualControlPreviewResponse,
)
def dual_control_preview(
    request: HumanDualControlPreviewRequest,
) -> HumanDualControlPreviewResponse:
    return human_approval_integrity_service.dual_control_preview(request)
