from fastapi import APIRouter, HTTPException

from app.schemas.operational_resilience import (
    DependencyStatus,
    EvaluateResilienceScenarioRequest,
    EvaluateResilienceScenarioResponse,
    FallbackMode,
    ResilienceControl,
    ResilienceIncident,
    ServiceHealthStatus,
)
from app.services.operational_resilience_service import (
    operational_resilience_service,
)


router = APIRouter(
    prefix="/operational-resilience",
    tags=["operational resilience"],
)


@router.get("/service-health", response_model=list[ServiceHealthStatus])
def list_service_health() -> list[ServiceHealthStatus]:
    return operational_resilience_service.list_service_health()


@router.get("/dependencies", response_model=list[DependencyStatus])
def list_dependencies() -> list[DependencyStatus]:
    return operational_resilience_service.list_dependencies()


@router.get("/fallback-modes", response_model=list[FallbackMode])
def list_fallback_modes() -> list[FallbackMode]:
    return operational_resilience_service.list_fallback_modes()


@router.get("/controls", response_model=list[ResilienceControl])
def list_resilience_controls() -> list[ResilienceControl]:
    return operational_resilience_service.list_controls()


@router.get("/incidents", response_model=list[ResilienceIncident])
def list_incidents() -> list[ResilienceIncident]:
    return operational_resilience_service.list_incidents()


@router.get("/incidents/{incident_id}", response_model=ResilienceIncident)
def get_incident(incident_id: str) -> ResilienceIncident:
    incident = operational_resilience_service.get_incident(incident_id)
    if incident is None:
        raise HTTPException(status_code=404, detail="Resilience incident not found.")
    return incident


@router.post(
    "/evaluate-scenario",
    response_model=EvaluateResilienceScenarioResponse,
)
def evaluate_scenario(
    request: EvaluateResilienceScenarioRequest,
) -> EvaluateResilienceScenarioResponse:
    return operational_resilience_service.evaluate_scenario(
        scenario_id=request.scenario_id,
        affected_service=request.affected_service,
        dependency_status=request.dependency_status,
        customer_impact=request.customer_impact,
    )
