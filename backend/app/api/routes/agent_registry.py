from fastapi import APIRouter, HTTPException

from app.schemas.agent_registry import (
    AgentRegistrationRequest,
    AgentRegistrationResponse,
    AgentRegistryDetail,
    AgentRegistrySummary,
    AgentStatusDefinition,
    AgentStatusUpdateRequest,
    AgentStatusUpdateResponse,
    AgentTypeDefinition,
)
from app.services.agent_registry_service import agent_registry_service


router = APIRouter(
    prefix="/agent-registry",
    tags=["agent registry"],
)


@router.get("/types", response_model=list[AgentTypeDefinition])
def list_agent_types() -> list[AgentTypeDefinition]:
    return agent_registry_service.list_types()


@router.get("/statuses", response_model=list[AgentStatusDefinition])
def list_agent_statuses() -> list[AgentStatusDefinition]:
    return agent_registry_service.list_statuses()


@router.get("/agents", response_model=list[AgentRegistrySummary])
def list_agents() -> list[AgentRegistrySummary]:
    return agent_registry_service.list_agents()


@router.get("/agents/{agent_id}", response_model=AgentRegistryDetail)
def get_agent(agent_id: str) -> AgentRegistryDetail:
    try:
        return agent_registry_service.get_agent(agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/register", response_model=AgentRegistrationResponse)
def register_agent(
    request: AgentRegistrationRequest,
) -> AgentRegistrationResponse:
    try:
        return agent_registry_service.register(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post(
    "/agents/{agent_id}/status",
    response_model=AgentStatusUpdateResponse,
)
def update_agent_status(
    agent_id: str,
    request: AgentStatusUpdateRequest,
) -> AgentStatusUpdateResponse:
    try:
        return agent_registry_service.update_status(agent_id, request)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if "not found" in detail.lower() else 400
        raise HTTPException(status_code=status_code, detail=detail) from exc
