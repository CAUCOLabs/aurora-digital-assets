from app.schemas.payment import (
    DigitalAssetPaymentEstimate,
    DigitalAssetPaymentEvaluateRequest,
    DigitalAssetPaymentEvaluateResponse,
)
from app.services.audit_service import AuditService, audit_service
from app.services.review_case_service import (
    ReviewCaseService,
    review_case_service,
)


ELIGIBLE_BUSINESS_RECIPIENT = "Aurora Telecom Oyj"
SUPPORTED_PAYMENT_ASSETS = {"EURD", "USDC", "USDT", "BTC", "ETH"}
CONVERSION_RATES_EUR = {
    "EURD": 1.0,
    "USDC": 0.928,
    "USDT": 0.926,
    "BTC": 69500,
    "ETH": 2066.88,
}
VOLATILE_PAYMENT_ASSETS = {"BTC", "ETH"}


class PaymentService:
    """Evaluates simulated digital asset invoice payments."""

    def __init__(
        self,
        audit_log: AuditService | None = None,
        review_cases: ReviewCaseService | None = None,
    ) -> None:
        self.audit_log = audit_log or audit_service
        self.review_cases = review_cases or review_case_service

    def evaluate_digital_asset_payment(
        self,
        request: DigitalAssetPaymentEvaluateRequest,
    ) -> DigitalAssetPaymentEvaluateResponse:
        response = self._evaluate_request(request)
        case_id = None

        if response.case_required:
            review_case = self.review_cases.create_digital_asset_payment_case(
                request,
                response,
            )
            case_id = review_case.case_id
            response = response.model_copy(update={"case_id": case_id})

        self.audit_log.record_event(
            module="payments",
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
        request: DigitalAssetPaymentEvaluateRequest,
    ) -> DigitalAssetPaymentEvaluateResponse:
        payment_asset = request.payment_asset.strip().upper()
        recipient_name = request.recipient_name.strip()

        if request.amount_eur <= 0:
            return self._validation_failed(
                reason="invalid_amount",
                user_message="The payment amount must be greater than zero.",
            )

        if not request.reference_number.strip():
            return self._validation_failed(
                reason="missing_reference_number",
                user_message="Reference number is required.",
            )

        if not request.invoice_number.strip():
            return self._validation_failed(
                reason="missing_invoice_number",
                user_message="Invoice number is required.",
            )

        if payment_asset not in SUPPORTED_PAYMENT_ASSETS:
            return self._validation_failed(
                reason="unsupported_payment_asset",
                user_message=(
                    "This digital asset is not supported for invoice payments."
                ),
            )

        if recipient_name != ELIGIBLE_BUSINESS_RECIPIENT:
            return self._validation_failed(
                reason="recipient_not_enabled_for_digital_asset_payments",
                user_message=(
                    "Digital asset payments are available only for eligible "
                    "business recipients."
                ),
            )

        estimate = self._build_estimate(request.amount_eur, payment_asset)
        reasons = ["eligible_business_recipient"]
        if payment_asset in VOLATILE_PAYMENT_ASSETS:
            reasons.append("volatile_payment_asset")

        if request.amount_eur > 500:
            reasons.append("high_value_digital_asset_payment")
            return DigitalAssetPaymentEvaluateResponse(
                decision="pending_review",
                risk_level="medium",
                reasons=reasons,
                case_required=True,
                case_type="digital_asset_payment_review",
                user_message=(
                    "Your digital asset payment request is pending security review."
                ),
                audit_event_type="digital_asset_payment_pending_review",
                estimate=estimate,
            )

        return DigitalAssetPaymentEvaluateResponse(
            decision="auto_approved",
            risk_level="low",
            reasons=reasons,
            case_required=False,
            case_type=None,
            user_message=(
                "Your digital asset payment passed the simulated automated review."
            ),
            audit_event_type="digital_asset_payment_auto_approved",
            estimate=estimate,
        )

    def _build_estimate(
        self,
        invoice_amount_eur: float,
        payment_asset: str,
    ) -> DigitalAssetPaymentEstimate:
        if payment_asset == "EURD":
            service_fee_eur = 0.0
            settlement_fee_eur = 0.0
        else:
            service_fee_eur = 1.2
            settlement_fee_eur = 0.3

        total_estimated_cost_eur = (
            invoice_amount_eur + service_fee_eur + settlement_fee_eur
        )
        conversion_rate_eur = CONVERSION_RATES_EUR[payment_asset]

        return DigitalAssetPaymentEstimate(
            invoice_amount_eur=invoice_amount_eur,
            payment_asset=payment_asset,
            estimated_asset_amount=total_estimated_cost_eur / conversion_rate_eur,
            conversion_rate_eur=conversion_rate_eur,
            service_fee_eur=service_fee_eur,
            settlement_fee_eur=settlement_fee_eur,
            total_estimated_cost_eur=total_estimated_cost_eur,
            recipient_settlement="Recipient receives EUR",
        )

    def _validation_failed(
        self,
        reason: str,
        user_message: str,
    ) -> DigitalAssetPaymentEvaluateResponse:
        return DigitalAssetPaymentEvaluateResponse(
            decision="auto_rejected",
            risk_level="invalid",
            reasons=[reason],
            case_required=False,
            case_type=None,
            user_message=user_message,
            audit_event_type="digital_asset_payment_validation_failed",
            estimate=None,
        )
