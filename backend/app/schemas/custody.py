from pydantic import BaseModel


class CustodyStatus(BaseModel):
    custodyMode: str
    privateKeysExposed: bool
    assetsSeparateFromDeposits: bool
    auditTrailEnabled: bool
    externalWithdrawalsRequireReview: bool
    userMessage: str
    controls: list[str]
