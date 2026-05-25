from fastapi import APIRouter

from app.schemas.buy_sell import BuySellEvaluateRequest, BuySellEvaluateResponse
from app.services.buy_sell_service import BuySellService


router = APIRouter(prefix="/digital-assets", tags=["digital-assets"])
buy_sell_service = BuySellService()


@router.post("/buy-sell/evaluate", response_model=BuySellEvaluateResponse)
def evaluate_buy_sell(
    request: BuySellEvaluateRequest,
) -> BuySellEvaluateResponse:
    return buy_sell_service.evaluate_buy_sell(request)
