from fastapi import APIRouter

from app.schemas.agent_policy_engine import (
    AgentPolicyContextRequest,
    AgentPolicyDecisionExplanationRequest,
    AgentPolicyDecisionExplanationResponse,
    AgentPolicyDecisionType,
    AgentPolicyDefinition,
    AgentPolicyEvaluationRequest,
    AgentPolicyEvaluationResponse,
)
from app.services.agent_policy_engine_service import agent_policy_engine_service


router = APIRouter(
    prefix="/agent-policy-engine",
    tags=["agent policy engine"],
)


@router.get("/policies", response_model=list[AgentPolicyDefinition])
def list_policies() -> list[AgentPolicyDefinition]:
    return agent_policy_engine_service.list_policies()


@router.get("/decision-types", response_model=list[AgentPolicyDecisionType])
def list_decision_types() -> list[AgentPolicyDecisionType]:
    return agent_policy_engine_service.list_decision_types()


@router.post("/evaluate", response_model=AgentPolicyEvaluationResponse)
def evaluate_policy(
    request: AgentPolicyEvaluationRequest,
) -> AgentPolicyEvaluationResponse:
    return agent_policy_engine_service.evaluate(request)


@router.post("/evaluate-context", response_model=AgentPolicyEvaluationResponse)
def evaluate_context(
    request: AgentPolicyContextRequest,
) -> AgentPolicyEvaluationResponse:
    return agent_policy_engine_service.evaluate_context(request)


@router.post(
    "/explain-decision",
    response_model=AgentPolicyDecisionExplanationResponse,
)
def explain_decision(
    request: AgentPolicyDecisionExplanationRequest,
) -> AgentPolicyDecisionExplanationResponse:
    return agent_policy_engine_service.explain_decision(request)
