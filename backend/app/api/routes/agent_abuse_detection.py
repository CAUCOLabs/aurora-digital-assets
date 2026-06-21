from fastapi import APIRouter

from app.schemas.agent_abuse_detection import (
    AgentAbuseDetectionRequest,
    AgentAbuseDetectionResponse,
    AgentAbusePatternDefinition,
    AgentAbuseResponseRecommendationRequest,
    AgentAbuseResponseRecommendationResponse,
    AgentAbuseSequenceRequest,
    AgentAbuseSequenceResponse,
    AgentAbuseSignalDefinition,
)
from app.services.agent_abuse_detection_service import agent_abuse_detection_service


router = APIRouter(
    prefix="/agent-abuse-detection",
    tags=["agent abuse detection"],
)


@router.get("/signals", response_model=list[AgentAbuseSignalDefinition])
def list_signals() -> list[AgentAbuseSignalDefinition]:
    return agent_abuse_detection_service.list_signals()


@router.get("/patterns", response_model=list[AgentAbusePatternDefinition])
def list_patterns() -> list[AgentAbusePatternDefinition]:
    return agent_abuse_detection_service.list_patterns()


@router.post("/evaluate", response_model=AgentAbuseDetectionResponse)
def evaluate_abuse(
    request: AgentAbuseDetectionRequest,
) -> AgentAbuseDetectionResponse:
    return agent_abuse_detection_service.evaluate(request)


@router.post("/evaluate-sequence", response_model=AgentAbuseSequenceResponse)
def evaluate_sequence(
    request: AgentAbuseSequenceRequest,
) -> AgentAbuseSequenceResponse:
    return agent_abuse_detection_service.evaluate_sequence(request)


@router.post(
    "/recommend-response",
    response_model=AgentAbuseResponseRecommendationResponse,
)
def recommend_response(
    request: AgentAbuseResponseRecommendationRequest,
) -> AgentAbuseResponseRecommendationResponse:
    return agent_abuse_detection_service.recommend_response(request)
