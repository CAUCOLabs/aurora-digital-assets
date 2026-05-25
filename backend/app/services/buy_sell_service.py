from app.schemas.buy_sell import (
    BuySellEstimate,
    BuySellEvaluateRequest,
    BuySellEvaluateResponse,
)
from app.services.audit_service import AuditService, audit_service
from app.services.review_case_service import (
    ReviewCaseService,
    review_case_service,
)


SUPPORTED_ASSET_PRICES_EUR = {
    "BTC": 69500.0,
    "ETH": 2066.88,
}
SUPPORTED_SIDES = {"buy", "sell"}
FEE_RATE = 0.01
SPREAD_RATE = 0.005
REVIEW_LIMIT_EUR = 500.0


class BuySellService:
    """Evaluates simulated digital asset buy and sell requests."""

    def __init__(
        self,
        audit_log: AuditService | None = None,
        review_cases: ReviewCaseService | None = None,
    ) -> None:
        self.audit_log = audit_log or audit_service
        self.review_cases = review_cases or review_case_service

    def evaluate_buy_sell(
        self,
        request: BuySellEvaluateRequest,
    ) -> BuySellEvaluateResponse:
        response = self._evaluate_request(request)
        case_id = None

        if response.case_required:
            review_case = self.review_cases.create_buy_sell_case(request, response)
            case_id = review_case.case_id
            response = response.model_copy(update={"case_id": case_id})

        self.audit_log.record_event(
            module="buy_sell",
            action_type=response.audit_event_type,
            status=response.decision,
            risk_level=response.risk_level,
            decision=response.decision,
            reasons=response.reasons,
            case_id=case_id,
            user_message=response.user_message,
        )

        return response

    def _evaluate_request(
        self,
        request: BuySellEvaluateRequest,
    ) -> BuySellEvaluateResponse:
        side = request.side.strip().lower()
        asset = request.asset.strip().upper()

        if request.amount <= 0:
            return self._validation_failed(
                reason="invalid_amount",
                user_message="Amount must be greater than zero.",
            )

        if side not in SUPPORTED_SIDES:
            return self._validation_failed(
                reason="unsupported_trade_side",
                user_message="Only simulated buy and sell requests are supported.",
            )

        if asset not in SUPPORTED_ASSET_PRICES_EUR:
            return self._validation_failed(
                reason="unsupported_asset",
                user_message=(
                    "This digital asset is not supported for simulated "
                    "buy/sell requests."
                ),
            )

        estimate = self._build_estimate(side, asset, request.amount)
        if estimate.gross_eur > REVIEW_LIMIT_EUR:
            return BuySellEvaluateResponse(
                decision="pending_review",
                risk_level="medium",
                reasons=["supported_asset", f"high_value_{side}_request"],
                case_required=True,
                case_type="buy_sell_review",
                user_message=(
                    f"Your simulated {side} request is pending security review."
                ),
                audit_event_type="buy_sell_pending_review",
                estimate=estimate,
            )

        return BuySellEvaluateResponse(
            decision="auto_approved",
            risk_level="low",
            reasons=["supported_asset", "amount_within_prototype_limit"],
            case_required=False,
            case_type=None,
            user_message=(
                "Your simulated buy/sell request passed the automated "
                "prototype review."
            ),
            audit_event_type="buy_sell_auto_approved",
            estimate=estimate,
        )

    def _build_estimate(
        self,
        side: str,
        asset: str,
        amount: float,
    ) -> BuySellEstimate:
        market_price_eur = SUPPORTED_ASSET_PRICES_EUR[asset]
        if side == "buy":
            gross_eur = amount
            estimated_asset_amount = 0.0
        else:
            estimated_asset_amount = amount
            gross_eur = amount * market_price_eur

        fee_eur = gross_eur * FEE_RATE
        spread_eur = gross_eur * SPREAD_RATE
        net_eur = gross_eur - fee_eur - spread_eur
        if side == "buy":
            estimated_asset_amount = net_eur / market_price_eur

        return BuySellEstimate(
            side=side,
            asset=asset,
            market_price_eur=market_price_eur,
            gross_eur=gross_eur,
            fee_eur=fee_eur,
            spread_eur=spread_eur,
            net_eur=net_eur,
            estimated_asset_amount=estimated_asset_amount,
        )

    def _validation_failed(
        self,
        reason: str,
        user_message: str,
    ) -> BuySellEvaluateResponse:
        return BuySellEvaluateResponse(
            decision="auto_rejected",
            risk_level="invalid",
            reasons=[reason],
            case_required=False,
            case_type=None,
            user_message=user_message,
            audit_event_type="buy_sell_validation_failed",
            estimate=None,
        )
