from fastapi import APIRouter

from app.schemas.payment import (
    DigitalAssetPaymentEvaluateRequest,
    DigitalAssetPaymentEvaluateResponse,
)
from app.services.payment_service import PaymentService


router = APIRouter(prefix="/payments", tags=["payments"])
payment_service = PaymentService()


@router.post(
    "/digital-assets/evaluate",
    response_model=DigitalAssetPaymentEvaluateResponse,
)
def evaluate_digital_asset_payment(
    request: DigitalAssetPaymentEvaluateRequest,
) -> DigitalAssetPaymentEvaluateResponse:
    return payment_service.evaluate_digital_asset_payment(request)
