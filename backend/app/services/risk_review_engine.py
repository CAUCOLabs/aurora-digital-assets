from app.schemas.risk_review import (
    RISK_DECISION_AUTO_APPROVED,
    RISK_DECISION_AUTO_REJECTED,
    RISK_DECISION_BLOCKED,
    RISK_DECISION_PENDING_REVIEW,
    RISK_LEVEL_HIGH,
    RISK_LEVEL_INVALID,
    RISK_LEVEL_LOW,
    RISK_LEVEL_MEDIUM,
    RiskDecisionResponse,
)
from app.schemas.withdrawal import WithdrawalEvaluateRequest


SUPPORTED_NETWORKS_BY_ASSET = {
    "BTC": {"bitcoin"},
    "ETH": {"ethereum"},
    "USDC": {"ethereum", "polygon"},
    "USDT": {"ethereum", "tron"},
    "EURD": set(),
}


class RiskReviewEngine:
    """Deterministic simulated risk rules for external withdrawals."""

    def evaluate_withdrawal(
        self,
        request: WithdrawalEvaluateRequest,
    ) -> RiskDecisionResponse:
        asset = request.asset.strip().upper()
        network = request.network.strip().lower()
        destination_address = request.destination_address.strip()
        confirm_destination_address = request.confirm_destination_address.strip()
        wallet_type = request.wallet_type.strip()

        if request.amount <= 0:
            return self._validation_failed(
                reason="invalid_amount",
                user_message="The withdrawal amount must be greater than zero.",
            )

        if not destination_address:
            return self._validation_failed(
                reason="missing_destination_address",
                user_message="Destination address is required.",
            )

        if destination_address != confirm_destination_address:
            return self._validation_failed(
                reason="destination_address_mismatch",
                user_message=(
                    "Destination address and confirmation address do not match."
                ),
            )

        if asset not in SUPPORTED_NETWORKS_BY_ASSET:
            return self._validation_failed(
                reason="unsupported_asset",
                user_message="This digital asset is not supported for withdrawal.",
            )

        if asset == "EURD":
            return self._validation_failed(
                reason=(
                    "external_withdrawal_unavailable_for_internal_settlement_asset"
                ),
                user_message=(
                    "External withdrawal is unavailable for this internal "
                    "settlement asset."
                ),
            )

        if network not in SUPPORTED_NETWORKS_BY_ASSET[asset]:
            return self._validation_failed(
                reason="incompatible_network",
                user_message=(
                    "The selected network is not compatible with this digital asset."
                ),
            )

        normalized_address = destination_address.lower()

        if "risk" in normalized_address or "blocked" in normalized_address:
            return RiskDecisionResponse(
                decision=RISK_DECISION_BLOCKED,
                risk_level=RISK_LEVEL_HIGH,
                reasons=["high_risk_wallet_signal"],
                case_required=False,
                case_type=None,
                user_message=(
                    "This destination cannot be used for external withdrawal in "
                    "this prototype."
                ),
                audit_event_type="withdrawal_blocked",
            )

        if normalized_address.startswith("new") or wallet_type != "trusted_address":
            return RiskDecisionResponse(
                decision=RISK_DECISION_PENDING_REVIEW,
                risk_level=RISK_LEVEL_MEDIUM,
                reasons=["first_time_external_address"],
                case_required=True,
                case_type="external_withdrawal_review",
                user_message=(
                    "Your external transfer request is pending security review."
                ),
                audit_event_type="withdrawal_pending_review",
            )

        return RiskDecisionResponse(
            decision=RISK_DECISION_AUTO_APPROVED,
            risk_level=RISK_LEVEL_LOW,
            reasons=["low_risk_known_destination"],
            case_required=False,
            case_type=None,
            user_message=(
                "Your external transfer request passed the simulated automated "
                "review."
            ),
            audit_event_type="withdrawal_auto_approved",
        )

    def _validation_failed(
        self,
        reason: str,
        user_message: str,
    ) -> RiskDecisionResponse:
        return RiskDecisionResponse(
            decision=RISK_DECISION_AUTO_REJECTED,
            risk_level=RISK_LEVEL_INVALID,
            reasons=[reason],
            case_required=False,
            case_type=None,
            user_message=user_message,
            audit_event_type="withdrawal_validation_failed",
        )
