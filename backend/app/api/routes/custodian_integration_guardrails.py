from fastapi import APIRouter

from app.schemas.custodian_integration_guardrails import (
    CustodianIntegrationGuardrailControl,
    CustodianIntegrationGuardrailEvaluationRequest,
    CustodianIntegrationGuardrailEvaluationResponse,
    CustodianIntegrationGuardrailScenario,
)
from app.services.custodian_integration_guardrails_service import (
    custodian_integration_guardrails_service,
)


router = APIRouter(
    prefix="/custodian-integration-guardrails",
    tags=["custodian integration guardrails"],
)


@router.get("/controls", response_model=list[CustodianIntegrationGuardrailControl])
def list_controls() -> list[CustodianIntegrationGuardrailControl]:
    return custodian_integration_guardrails_service.list_controls()


@router.get("/scenarios", response_model=list[CustodianIntegrationGuardrailScenario])
def list_scenarios() -> list[CustodianIntegrationGuardrailScenario]:
    return custodian_integration_guardrails_service.list_scenarios()


@router.post(
    "/evaluate",
    response_model=CustodianIntegrationGuardrailEvaluationResponse,
)
def evaluate_guardrails(
    request: CustodianIntegrationGuardrailEvaluationRequest,
) -> CustodianIntegrationGuardrailEvaluationResponse:
    return custodian_integration_guardrails_service.evaluate(request)
