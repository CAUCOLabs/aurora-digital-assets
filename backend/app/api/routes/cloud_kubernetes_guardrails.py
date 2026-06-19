from fastapi import APIRouter

from app.schemas.cloud_kubernetes_guardrails import (
    CloudKubernetesGuardrailControl,
    CloudKubernetesGuardrailEvaluationRequest,
    CloudKubernetesGuardrailEvaluationResponse,
    CloudKubernetesGuardrailScenario,
)
from app.services.cloud_kubernetes_guardrails_service import (
    cloud_kubernetes_guardrails_service,
)


router = APIRouter(
    prefix="/cloud-kubernetes-guardrails",
    tags=["cloud kubernetes guardrails"],
)


@router.get("/controls", response_model=list[CloudKubernetesGuardrailControl])
def list_controls() -> list[CloudKubernetesGuardrailControl]:
    return cloud_kubernetes_guardrails_service.list_controls()


@router.get("/scenarios", response_model=list[CloudKubernetesGuardrailScenario])
def list_scenarios() -> list[CloudKubernetesGuardrailScenario]:
    return cloud_kubernetes_guardrails_service.list_scenarios()


@router.post("/evaluate", response_model=CloudKubernetesGuardrailEvaluationResponse)
def evaluate_guardrails(
    request: CloudKubernetesGuardrailEvaluationRequest,
) -> CloudKubernetesGuardrailEvaluationResponse:
    return cloud_kubernetes_guardrails_service.evaluate(request)
