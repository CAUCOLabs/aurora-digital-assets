from pydantic import BaseModel


class AuthCustomerInfo(BaseModel):
    customer_id: str
    customer_name: str
    account_id: str
    relationship_status: str


class BankLoginRequest(BaseModel):
    bank_user_id: str
    pin: str


class BankLoginResponse(BaseModel):
    status: str
    challenge_id: str | None
    customer: AuthCustomerInfo | None = None
    message: str


class MobileApprovalRequest(BaseModel):
    challenge_id: str
    approved: bool


class MobileApprovalResponse(BaseModel):
    status: str
    session_id: str | None
    customer: AuthCustomerInfo | None = None
    redirect_to: str
    message: str


class BankSessionResponse(BaseModel):
    authenticated: bool
    customer_id: str | None = None
    customer_name: str | None = None
    account_id: str | None = None
    relationship_status: str | None = None


class LogoutRequest(BaseModel):
    session_id: str


class LogoutResponse(BaseModel):
    status: str
    message: str
