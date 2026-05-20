from app.schemas.custody import CustodyStatus


class CustodyService:
    """Provides simulated custody status for the banking prototype."""

    def get_custody_status(self) -> CustodyStatus:
        return CustodyStatus(
            custodyMode="Internal custodial wallet concept",
            privateKeysExposed=False,
            assetsSeparateFromDeposits=True,
            auditTrailEnabled=True,
            externalWithdrawalsRequireReview=True,
            userMessage=(
                "Digital assets are visible inside online banking, but the user "
                "does not manage private keys directly in this prototype."
            ),
            controls=[
                "Strong authentication active",
                "User does not manage private keys",
                "Audit trail enabled",
                "External withdrawals require review",
                "Digital assets are separate from deposits",
            ],
        )


custody_service = CustodyService()
