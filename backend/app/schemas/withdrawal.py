from pydantic import BaseModel


class WithdrawalEvaluateRequest(BaseModel):
    asset: str
    network: str
    amount: float
    destination_address: str
    confirm_destination_address: str
    wallet_type: str
