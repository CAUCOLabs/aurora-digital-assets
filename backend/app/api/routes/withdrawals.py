from fastapi import APIRouter

from app.schemas.risk_review import RiskDecisionResponse
from app.schemas.withdrawal import WithdrawalEvaluateRequest
from app.services.withdrawal_service import WithdrawalService


router = APIRouter(prefix="/withdrawals", tags=["withdrawals"])
withdrawal_service = WithdrawalService()


@router.post("/evaluate", response_model=RiskDecisionResponse)
def evaluate_withdrawal(
    request: WithdrawalEvaluateRequest,
) -> RiskDecisionResponse:
    return withdrawal_service.evaluate_withdrawal(request)
