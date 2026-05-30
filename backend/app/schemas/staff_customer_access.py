from typing import Literal

from pydantic import BaseModel


AccessState = Literal["locked", "unlocked", "unavailable"]
AuthorizationMethod = Literal["mobile_approval", "private_branch_entry"]


class StaffCustomerLookupRequest(BaseModel):
    lookup_value: str
    lookup_type: str


class StaffCustomerLookupResponse(BaseModel):
    status: str
    customer_id: str | None = None
    customer_name: str | None = None
    relationship_status: str | None = None
    access_state: AccessState
    user_message: str


class StaffCustomerAuthorizationRequest(BaseModel):
    customer_id: str
    method: AuthorizationMethod


class StaffCustomerAuthorizationResponse(BaseModel):
    status: str
    request_id: str | None = None
    method: AuthorizationMethod | None = None
    customer_id: str | None = None
    access_state: AccessState
    user_message: str


class StaffCustomerAccessApprovalRequest(BaseModel):
    request_id: str
    approved: bool


class StaffCustomerRecordDetails(BaseModel):
    customer_id: str
    bank_user_id: str
    name: str
    account_id: str
    relationship_status: str
    identity_verification_status: str
    source_of_funds_status: str
    online_banking_enabled: bool
    strong_authentication_enabled: bool
    digital_assets_eligible: bool


class StaffCustomerAccessApprovalResponse(BaseModel):
    status: str
    access_state: AccessState
    customer_record: StaffCustomerRecordDetails | None = None
    access_expires_in_minutes: int | None = None
    user_message: str


class StaffCustomerAccessStatusResponse(BaseModel):
    status: str
    access_state: AccessState
    method: AuthorizationMethod | None = None
    customer_id: str | None = None
    request_id: str | None = None
    user_message: str
