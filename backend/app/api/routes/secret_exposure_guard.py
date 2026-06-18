from fastapi import APIRouter, HTTPException

from app.schemas.secret_exposure_guard import (
    SecretExposureGuardEvaluationRequest,
    SecretExposureGuardEvaluationResponse,
    SecretExposureSurface,
)
from app.services.secret_exposure_guard_service import (
    secret_exposure_guard_service,
)


router = APIRouter(
    prefix="/secret-exposure-guard",
    tags=["secret exposure guard"],
)


@router.get("/surfaces", response_model=list[SecretExposureSurface])
def list_secret_exposure_surfaces() -> list[SecretExposureSurface]:
    return secret_exposure_guard_service.list_surfaces()


@router.get("/signals", response_model=list[str])
def list_secret_exposure_signals() -> list[str]:
    return secret_exposure_guard_service.list_signals()


@router.post(
    "/evaluate",
    response_model=SecretExposureGuardEvaluationResponse,
)
def evaluate_secret_exposure_signal(
    request: SecretExposureGuardEvaluationRequest,
) -> SecretExposureGuardEvaluationResponse:
    try:
        return secret_exposure_guard_service.evaluate(request)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
