from fastapi import APIRouter, HTTPException

from app.schemas.ai_threat_defense import (
    AIThreatDefenseEvaluationRequest,
    AIThreatDefenseEvaluationResponse,
    AIThreatScenario,
    ThreatSurface,
)
from app.services.ai_threat_defense_service import ai_threat_defense_service


router = APIRouter(
    prefix="/ai-threat-defense",
    tags=["ai threat defense"],
)


@router.get("/surfaces", response_model=list[ThreatSurface])
def list_threat_surfaces() -> list[ThreatSurface]:
    return ai_threat_defense_service.list_threat_surfaces()


@router.get("/scenarios", response_model=list[AIThreatScenario])
def list_ai_threat_scenarios() -> list[AIThreatScenario]:
    return ai_threat_defense_service.list_ai_threat_scenarios()


@router.post(
    "/evaluate-scenario",
    response_model=AIThreatDefenseEvaluationResponse,
)
def evaluate_ai_threat_scenario(
    request: AIThreatDefenseEvaluationRequest,
) -> AIThreatDefenseEvaluationResponse:
    try:
        return ai_threat_defense_service.evaluate_ai_threat_scenario(request)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
