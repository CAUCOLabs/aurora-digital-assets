from fastapi import APIRouter, HTTPException

from app.schemas.agent_actions import (
    AgentActionRecordRequest,
    AgentActionRecordResponse,
    AgentActionTypeDefinition,
)
from app.services.agent_actions_service import agent_actions_service


router = APIRouter(
    prefix="/agent-actions",
    tags=["agent actions"],
)


@router.get("/action-types", response_model=list[AgentActionTypeDefinition])
def list_action_types() -> list[AgentActionTypeDefinition]:
    return agent_actions_service.list_action_types()


@router.get("/recent", response_model=list[AgentActionRecordResponse])
def list_recent_agent_actions() -> list[AgentActionRecordResponse]:
    return agent_actions_service.list_recent()


@router.post("/record", response_model=AgentActionRecordResponse)
def record_agent_action(
    request: AgentActionRecordRequest,
) -> AgentActionRecordResponse:
    try:
        return agent_actions_service.record(request)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if "not found" in detail.lower() else 400
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.post("/evaluate-and-record", response_model=AgentActionRecordResponse)
def evaluate_and_record_agent_action(
    request: AgentActionRecordRequest,
) -> AgentActionRecordResponse:
    try:
        return agent_actions_service.evaluate_and_record(request)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if "not found" in detail.lower() else 400
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.get("/{action_event_id}", response_model=AgentActionRecordResponse)
def get_agent_action_event(action_event_id: str) -> AgentActionRecordResponse:
    try:
        return agent_actions_service.get_event(action_event_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
