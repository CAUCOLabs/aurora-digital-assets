from fastapi import APIRouter, HTTPException

from app.schemas.agent_permissions import (
    AgentPermissionDefinition,
    AgentPermissionEvaluationRequest,
    AgentPermissionEvaluationResponse,
    AgentPermissionGrantPreviewRequest,
    AgentPermissionGrantPreviewResponse,
    AgentPermissionProfile,
    AgentPermissionsForAgentResponse,
)
from app.services.agent_permissions_service import agent_permissions_service


router = APIRouter(
    prefix="/agent-permissions",
    tags=["agent permissions"],
)


@router.get("/catalog", response_model=list[AgentPermissionDefinition])
def list_permission_catalog() -> list[AgentPermissionDefinition]:
    return agent_permissions_service.list_catalog()


@router.get("/profiles", response_model=list[AgentPermissionProfile])
def list_permission_profiles() -> list[AgentPermissionProfile]:
    return agent_permissions_service.list_profiles()


@router.post("/evaluate", response_model=AgentPermissionEvaluationResponse)
def evaluate_agent_permission(
    request: AgentPermissionEvaluationRequest,
) -> AgentPermissionEvaluationResponse:
    try:
        return agent_permissions_service.evaluate(request)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if "not found" in detail.lower() else 400
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.get(
    "/agents/{agent_id}",
    response_model=AgentPermissionsForAgentResponse,
)
def get_agent_permissions(agent_id: str) -> AgentPermissionsForAgentResponse:
    try:
        return agent_permissions_service.get_agent_permissions(agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post(
    "/agents/{agent_id}/grant-preview",
    response_model=AgentPermissionGrantPreviewResponse,
)
def preview_agent_permission_grant(
    agent_id: str,
    request: AgentPermissionGrantPreviewRequest,
) -> AgentPermissionGrantPreviewResponse:
    try:
        return agent_permissions_service.grant_preview(agent_id, request)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if "not found" in detail.lower() else 400
        raise HTTPException(status_code=status_code, detail=detail) from exc
