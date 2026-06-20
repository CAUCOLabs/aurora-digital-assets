from fastapi import APIRouter, HTTPException

from app.schemas.agent_revocation import (
    AgentRevocationApplyPreviewRequest,
    AgentRevocationApplyPreviewResponse,
    AgentRevocationEvaluationRequest,
    AgentRevocationEvaluationResponse,
    AgentRevocationStatusResponse,
)
from app.services.agent_revocation_service import agent_revocation_service


router = APIRouter(
    prefix="/agent-revocation",
    tags=["agent revocation"],
)


@router.get("/reasons", response_model=list[str])
def list_revocation_reasons() -> list[str]:
    return agent_revocation_service.list_reasons()


@router.get("/actions", response_model=list[str])
def list_revocation_actions() -> list[str]:
    return agent_revocation_service.list_actions()


@router.post("/evaluate", response_model=AgentRevocationEvaluationResponse)
def evaluate_agent_revocation(
    request: AgentRevocationEvaluationRequest,
) -> AgentRevocationEvaluationResponse:
    return agent_revocation_service.evaluate(request)


@router.post("/apply-preview", response_model=AgentRevocationApplyPreviewResponse)
def preview_agent_revocation_application(
    request: AgentRevocationApplyPreviewRequest,
) -> AgentRevocationApplyPreviewResponse:
    return agent_revocation_service.apply_preview(request)


@router.get(
    "/agents/{agent_id}/status",
    response_model=AgentRevocationStatusResponse,
)
def get_agent_revocation_status(agent_id: str) -> AgentRevocationStatusResponse:
    try:
        return agent_revocation_service.get_agent_status(agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
