from fastapi import APIRouter

from app.schemas.agent_identity_governance import (
    AgentGovernanceSummaryRequest,
    AgentGovernanceSummaryResponse,
    AgentIdentityGovernanceEvaluationRequest,
    AgentIdentityGovernanceEvaluationResponse,
    AgentProductionReadinessRequest,
    GovernanceControlDomain,
    GovernanceFrameworkResponse,
)
from app.services.agent_identity_governance_service import (
    agent_identity_governance_service,
)


router = APIRouter(
    prefix="/agent-identity-governance",
    tags=["agent identity governance"],
)


@router.get("/framework", response_model=GovernanceFrameworkResponse)
def get_framework() -> GovernanceFrameworkResponse:
    return agent_identity_governance_service.framework()


@router.get("/control-domains", response_model=list[GovernanceControlDomain])
def list_control_domains() -> list[GovernanceControlDomain]:
    return agent_identity_governance_service.control_domains()


@router.post("/evaluate", response_model=AgentIdentityGovernanceEvaluationResponse)
def evaluate_governance(
    request: AgentIdentityGovernanceEvaluationRequest,
) -> AgentIdentityGovernanceEvaluationResponse:
    return agent_identity_governance_service.evaluate(request)


@router.post(
    "/evaluate-production-readiness",
    response_model=AgentIdentityGovernanceEvaluationResponse,
)
def evaluate_production_readiness(
    request: AgentProductionReadinessRequest,
) -> AgentIdentityGovernanceEvaluationResponse:
    return agent_identity_governance_service.evaluate_production_readiness(request)


@router.post(
    "/generate-governance-summary",
    response_model=AgentGovernanceSummaryResponse,
)
def generate_governance_summary(
    request: AgentGovernanceSummaryRequest,
) -> AgentGovernanceSummaryResponse:
    return agent_identity_governance_service.generate_governance_summary(request)
