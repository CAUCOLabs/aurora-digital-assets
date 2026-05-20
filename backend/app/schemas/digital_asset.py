from pydantic import BaseModel


class SupportedDigitalAsset(BaseModel):
    symbol: str
    name: str
    category: str
    supported_actions: list[str]
    status: str
    risk_note: str


class WalletBalance(BaseModel):
    id: str
    symbol: str
    name: str
    balance: str
    estimatedValue: str
    custodyMode: str
    status: str


class DigitalAssetActivity(BaseModel):
    id: str
    title: str
    detail: str
    status: str
    amount: str
    module: str
