from fastapi import APIRouter, HTTPException

from app.schemas.agent_sensitive_action_guard import (
    AgentSensitiveActionDefinition,
    AgentSensitiveActionGuardRequest,
    AgentSensitiveActionGuardResponse,
    AgentSensitiveActionGuardRule,
    AgentSensitiveApprovalContextRequest,
    AgentSensitiveApprovalContextResponse,
)
from app.services.agent_sensitive_action_guard_service import (
    agent_sensitive_action_guard_service,
)


router = APIRouter(
    prefix="/agent-sensitive-action-guard",
    tags=["agent sensitive action guard"],
)


@router.get("/rules", response_model=list[AgentSensitiveActionGuardRule])
def list_guard_rules() -> list[AgentSensitiveActionGuardRule]:
    return agent_sensitive_action_guard_service.list_rules()


@router.get("/sensitive-actions", response_model=list[AgentSensitiveActionDefinition])
def list_sensitive_actions() -> list[AgentSensitiveActionDefinition]:
    return agent_sensitive_action_guard_service.list_sensitive_actions()


@router.post("/evaluate", response_model=AgentSensitiveActionGuardResponse)
def evaluate_agent_sensitive_action(
    request: AgentSensitiveActionGuardRequest,
) -> AgentSensitiveActionGuardResponse:
    try:
        return agent_sensitive_action_guard_service.evaluate(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post(
    "/evaluate-sensitive-approval-context",
    response_model=AgentSensitiveApprovalContextResponse,
)
def evaluate_sensitive_approval_context(
    request: AgentSensitiveApprovalContextRequest,
) -> AgentSensitiveApprovalContextResponse:
    try:
        return agent_sensitive_action_guard_service.evaluate_sensitive_approval_context(
            request
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
