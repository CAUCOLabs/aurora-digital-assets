from app.schemas.digital_asset import (
    DigitalAssetActivity,
    SupportedDigitalAsset,
    WalletBalance,
)


class DigitalAssetService:
    """Provides simulated digital asset data for the prototype."""

    def list_supported_assets(self) -> list[SupportedDigitalAsset]:
        return [
            SupportedDigitalAsset(
                symbol="BTC",
                name="Bitcoin",
                category="Investment / holding asset",
                supported_actions=[
                    "buy",
                    "sell",
                    "hold",
                    "external_withdrawal",
                ],
                status="Active",
                risk_note=(
                    "Volatile digital asset. External withdrawals require review."
                ),
            ),
            SupportedDigitalAsset(
                symbol="ETH",
                name="Ethereum",
                category="Investment / holding asset",
                supported_actions=[
                    "buy",
                    "sell",
                    "hold",
                    "external_withdrawal",
                ],
                status="Active",
                risk_note=(
                    "Volatile digital asset. External withdrawals require review."
                ),
            ),
            SupportedDigitalAsset(
                symbol="EURD",
                name="EUR digital asset concept",
                category="Payment / internal settlement asset",
                supported_actions=["payment", "internal_settlement"],
                status="Concept",
                risk_note="Internal settlement only in this prototype.",
            ),
            SupportedDigitalAsset(
                symbol="USDC",
                name="USD Coin",
                category="Payment-oriented asset",
                supported_actions=["payment", "hold", "external_withdrawal"],
                status="Simulated",
                risk_note="Stablecoin concept. Payment and withdrawal rules apply.",
            ),
            SupportedDigitalAsset(
                symbol="USDT",
                name="Tether USD",
                category="Payment-oriented asset",
                supported_actions=["payment", "hold", "external_withdrawal"],
                status="Simulated",
                risk_note="Stablecoin concept. Payment and withdrawal rules apply.",
            ),
        ]

    def get_wallet_balances(self) -> list[WalletBalance]:
        return [
            WalletBalance(
                id="btc-wallet",
                symbol="BTC",
                name="Bitcoin",
                balance="0.012450 BTC",
                estimatedValue="865,28 €",
                custodyMode="Internal custodial wallet concept",
                status="Active",
            ),
            WalletBalance(
                id="eth-wallet",
                symbol="ETH",
                name="Ethereum",
                balance="0.184200 ETH",
                estimatedValue="380,52 €",
                custodyMode="Internal custodial wallet concept",
                status="Active",
            ),
            WalletBalance(
                id="usdc-payment",
                symbol="USDC",
                name="USDC payment asset",
                balance="129.80 USDC",
                estimatedValue="Payment asset",
                custodyMode="Internal settlement / payment asset concept",
                status="Simulated",
            ),
            WalletBalance(
                id="usdt-payment",
                symbol="USDT",
                name="USDT payment asset",
                balance="129.60 USDT",
                estimatedValue="Payment asset",
                custodyMode="Internal settlement / payment asset concept",
                status="Simulated",
            ),
        ]

    def get_digital_asset_activity(self) -> list[DigitalAssetActivity]:
        return [
            DigitalAssetActivity(
                id="activity-btc-purchase",
                title="BTC purchase completed",
                detail="50,00 € from Aurora Current Account",
                status="Completed",
                amount="0.00072 BTC",
                module="Buy / Sell",
            ),
            DigitalAssetActivity(
                id="activity-eth-purchase",
                title="ETH purchase completed",
                detail="25,00 € from Aurora Current Account",
                status="Completed",
                amount="0.0121 ETH",
                module="Buy / Sell",
            ),
            DigitalAssetActivity(
                id="activity-btc-withdrawal",
                title="External BTC withdrawal",
                detail="0.001 BTC transfer request",
                status="Pending review",
                amount="0.001 BTC",
                module="Withdrawals",
            ),
            DigitalAssetActivity(
                id="activity-invoice-payment",
                title="Digital asset invoice payment",
                detail="Aurora Telecom Oyj",
                status="Evaluated",
                amount="120,45 €",
                module="Payments",
            ),
        ]


digital_asset_service = DigitalAssetService()
