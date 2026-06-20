from fastapi import APIRouter, HTTPException

from app.schemas.agent_passport import (
    AgentPassportGenerateRequest,
    AgentPassportResponse,
    AgentPassportTemplate,
)
from app.services.agent_passport_service import agent_passport_service


router = APIRouter(
    prefix="/agent-passports",
    tags=["agent passports"],
)


@router.get("/templates", response_model=list[AgentPassportTemplate])
def list_agent_passport_templates() -> list[AgentPassportTemplate]:
    return agent_passport_service.list_templates()


@router.post("/generate", response_model=AgentPassportResponse)
def generate_agent_passport(
    request: AgentPassportGenerateRequest,
) -> AgentPassportResponse:
    try:
        return agent_passport_service.generate_passport(
            agent_id=request.agent_id,
            reviewer_id=request.reviewer_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{agent_id}", response_model=AgentPassportResponse)
def get_agent_passport(agent_id: str) -> AgentPassportResponse:
    try:
        return agent_passport_service.get_passport(agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/{agent_id}/validate", response_model=AgentPassportResponse)
def validate_agent_passport(agent_id: str) -> AgentPassportResponse:
    try:
        return agent_passport_service.validate_passport(agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
