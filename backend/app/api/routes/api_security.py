from fastapi import APIRouter

from app.schemas.api_security import (
    ApiSecurityControl,
    ApiSecurityEvent,
    ApiSecurityScenario,
    ApiSecuritySurface,
    ApiSensitiveOperation,
    EvaluateApiSecurityScenarioRequest,
    EvaluateApiSecurityScenarioResponse,
)
from app.services.api_security_service import api_security_service


router = APIRouter(
    prefix="/api-security",
    tags=["api security"],
)


@router.get("/controls", response_model=list[ApiSecurityControl])
def list_controls() -> list[ApiSecurityControl]:
    return api_security_service.list_controls()


@router.get("/events", response_model=list[ApiSecurityEvent])
def list_events() -> list[ApiSecurityEvent]:
    return api_security_service.list_events()


@router.get("/surfaces", response_model=list[ApiSecuritySurface])
def list_surfaces() -> list[ApiSecuritySurface]:
    return api_security_service.list_surfaces()


@router.get("/sensitive-operations", response_model=list[ApiSensitiveOperation])
def list_sensitive_operations() -> list[ApiSensitiveOperation]:
    return api_security_service.list_sensitive_operations()


@router.get("/scenarios", response_model=list[ApiSecurityScenario])
def list_scenarios() -> list[ApiSecurityScenario]:
    return api_security_service.list_scenarios()


@router.post(
    "/evaluate-scenario",
    response_model=EvaluateApiSecurityScenarioResponse,
)
def evaluate_scenario(
    request: EvaluateApiSecurityScenarioRequest,
) -> EvaluateApiSecurityScenarioResponse:
    return api_security_service.evaluate_scenario(
        scenario_id=request.scenario_id,
        operation_name=request.operation_name,
        attempts=request.attempts,
        object_authorized=request.object_authorized,
        batching_detected=request.batching_detected,
        sensitive_fields_requested=request.sensitive_fields_requested,
    )
