from app.schemas.account import (
    BankAccount,
    BankTransaction,
    ConnectedDigitalAssetBalance,
)


class AccountService:
    """Provides simulated account data for the banking prototype."""

    def list_accounts(self) -> list[BankAccount]:
        return [
            BankAccount(
                id="aurora-current",
                name="Aurora Current Account",
                owner="Claudio Demo",
                type="Current account",
                iban="FI12 0000 0000 1234 56",
                bic="AURAFIHH",
                bookBalance="2 450,10 €",
                availableBalance="2 430,10 €",
                reservedCardPayments="20,00 €",
                status="Active",
            )
        ]

    def list_account_transactions(self, account_id: str) -> list[BankTransaction]:
        if account_id != "aurora-current":
            return []

        return [
            BankTransaction(
                id="tx-001",
                title="Aurora Telecom Oyj invoice payment",
                detail="Reference preserved",
                accountName="Aurora Current Account",
                amount="-120,45 €",
                status="Pending",
            ),
            BankTransaction(
                id="tx-002",
                title="Salary payment",
                detail="Salary",
                accountName="Aurora Current Account",
                amount="+2 850,00 €",
                status="Completed",
            ),
            BankTransaction(
                id="tx-003",
                title="Grocery store card payment",
                detail="Card purchase",
                accountName="Aurora Current Account",
                amount="-42,80 €",
                status="Completed",
            ),
            BankTransaction(
                id="tx-004",
                title="Digital asset invoice payment",
                detail="Digital asset payment draft",
                accountName="Aurora Current Account",
                amount="0,00 €",
                status="Pending confirmation",
            ),
        ]

    def list_connected_digital_asset_balances(
        self,
    ) -> list[ConnectedDigitalAssetBalance]:
        return [
            ConnectedDigitalAssetBalance(
                id="btc-wallet",
                name="BTC wallet balance",
                balance="0.012450 BTC",
                detail="Connected digital asset balance",
                value="865,28 €",
            ),
            ConnectedDigitalAssetBalance(
                id="eth-wallet",
                name="ETH wallet balance",
                balance="0.184200 ETH",
                detail="Connected digital asset balance",
                value="380,52 €",
            ),
            ConnectedDigitalAssetBalance(
                id="usdc-payment",
                name="USDC payment asset balance",
                balance="129.80 USDC",
                detail="Connected digital asset balance",
                value="Payment asset",
            ),
            ConnectedDigitalAssetBalance(
                id="usdt-payment",
                name="USDT payment asset balance",
                balance="129.60 USDT",
                detail="Connected digital asset balance",
                value="Payment asset",
            ),
            ConnectedDigitalAssetBalance(
                id="xrp-concept",
                name="XRP cross-border concept",
                balance="Future support",
                detail="Connected digital asset balance",
                value="Concept only",
            ),
        ]


account_service = AccountService()
