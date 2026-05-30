from fastapi import APIRouter

from app.schemas.staff_customer_access import (
    StaffCustomerAccessApprovalRequest,
    StaffCustomerAccessApprovalResponse,
    StaffCustomerAccessStatusResponse,
    StaffCustomerAuthorizationRequest,
    StaffCustomerAuthorizationResponse,
    StaffCustomerLookupRequest,
    StaffCustomerLookupResponse,
)
from app.services.staff_customer_access_service import (
    staff_customer_access_service,
)


router = APIRouter(
    prefix="/bank-staff/customer-access",
    tags=["staff customer access"],
)


@router.post("/lookup", response_model=StaffCustomerLookupResponse)
def lookup_customer(
    request: StaffCustomerLookupRequest,
) -> StaffCustomerLookupResponse:
    return staff_customer_access_service.lookup_customer(
        lookup_value=request.lookup_value,
        lookup_type=request.lookup_type,
    )


@router.post(
    "/request-authorization",
    response_model=StaffCustomerAuthorizationResponse,
)
def request_authorization(
    request: StaffCustomerAuthorizationRequest,
) -> StaffCustomerAuthorizationResponse:
    return staff_customer_access_service.request_authorization(
        customer_id=request.customer_id,
        method=request.method,
    )


@router.post("/approve", response_model=StaffCustomerAccessApprovalResponse)
def approve_authorization(
    request: StaffCustomerAccessApprovalRequest,
) -> StaffCustomerAccessApprovalResponse:
    return staff_customer_access_service.approve_authorization(
        request_id=request.request_id,
        approved=request.approved,
    )


@router.get("/status/{request_id}", response_model=StaffCustomerAccessStatusResponse)
def get_authorization_status(
    request_id: str,
) -> StaffCustomerAccessStatusResponse:
    return staff_customer_access_service.get_status(request_id)
