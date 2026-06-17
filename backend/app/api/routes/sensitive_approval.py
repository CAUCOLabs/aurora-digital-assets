from fastapi import APIRouter

from app.schemas.sensitive_approval import (
    SensitiveApprovalRequest,
    SensitiveApprovalResponse,
    SensitiveApprovalScenario,
    SensitiveOperation,
)
from app.services.sensitive_approval_service import sensitive_approval_service


router = APIRouter(prefix="/sensitive-approval", tags=["sensitive approval"])


@router.get("/operations", response_model=list[SensitiveOperation])
def list_operations() -> list[SensitiveOperation]:
    return sensitive_approval_service.list_operations()


@router.get("/scenarios", response_model=list[SensitiveApprovalScenario])
def list_scenarios() -> list[SensitiveApprovalScenario]:
    return sensitive_approval_service.list_scenarios()


@router.post("/evaluate", response_model=SensitiveApprovalResponse)
def evaluate_sensitive_approval(
    request: SensitiveApprovalRequest,
) -> SensitiveApprovalResponse:
    return sensitive_approval_service.evaluate(request)
