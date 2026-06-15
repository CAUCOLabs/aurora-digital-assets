from fastapi import APIRouter

from app.schemas.infrastructure_security import (
    EvaluateInfrastructureSecurityScenarioRequest,
    EvaluateInfrastructureSecurityScenarioResponse,
    InfrastructureSecurityControl,
    InfrastructureSecurityEvent,
    InfrastructureSecurityLayer,
    InfrastructureSecurityScenario,
)
from app.services.infrastructure_security_service import (
    infrastructure_security_service,
)


router = APIRouter(
    prefix="/infrastructure-security",
    tags=["infrastructure security"],
)


@router.get("/controls", response_model=list[InfrastructureSecurityControl])
def list_controls() -> list[InfrastructureSecurityControl]:
    return infrastructure_security_service.list_controls()


@router.get("/events", response_model=list[InfrastructureSecurityEvent])
def list_events() -> list[InfrastructureSecurityEvent]:
    return infrastructure_security_service.list_events()


@router.get("/layers", response_model=list[InfrastructureSecurityLayer])
def list_layers() -> list[InfrastructureSecurityLayer]:
    return infrastructure_security_service.list_layers()


@router.get("/scenarios", response_model=list[InfrastructureSecurityScenario])
def list_scenarios() -> list[InfrastructureSecurityScenario]:
    return infrastructure_security_service.list_scenarios()


@router.post(
    "/evaluate-scenario",
    response_model=EvaluateInfrastructureSecurityScenarioResponse,
)
def evaluate_scenario(
    request: EvaluateInfrastructureSecurityScenarioRequest,
) -> EvaluateInfrastructureSecurityScenarioResponse:
    return infrastructure_security_service.evaluate_scenario(
        scenario_id=request.scenario_id,
        object_authorization_failed=request.object_authorization_failed,
        unsafe_template_input_detected=request.unsafe_template_input_detected,
        pod_privileged=request.pod_privileged,
        service_account_can_read_secrets=request.service_account_can_read_secrets,
        cloud_iam_wildcard_permissions=request.cloud_iam_wildcard_permissions,
        weak_trust_policy=request.weak_trust_policy,
        secret_exposure_detected=request.secret_exposure_detected,
    )
