from dataclasses import dataclass
from uuid import uuid4

from app.schemas.staff_customer_access import (
    AccessState,
    AuthorizationMethod,
    StaffCustomerAccessApprovalResponse,
    StaffCustomerAccessStatusResponse,
    StaffCustomerAuthorizationResponse,
    StaffCustomerLookupResponse,
    StaffCustomerRecordDetails,
)
from app.services.audit_service import AuditService, audit_service


@dataclass
class AccessRequest:
    request_id: str
    customer_id: str
    method: AuthorizationMethod
    status: str
    access_state: AccessState
    user_message: str


class StaffCustomerAccessService:
    """Models temporary staff access authorization for deterministic demo data."""

    def __init__(self, audit_log: AuditService | None = None):
        self.audit_log = audit_log or audit_service
        self.access_requests: dict[str, AccessRequest] = {}

    def lookup_customer(
        self,
        lookup_value: str,
        lookup_type: str,
    ) -> StaffCustomerLookupResponse:
        normalized_type = lookup_type.strip().lower()
        normalized_value = lookup_value.strip()

        valid_lookup = (
            (normalized_type == "customer_id" and normalized_value == "CUST-DA-2026-001")
            or (normalized_type == "bank_user_id" and normalized_value == "12345678")
            or (
                normalized_type == "passport_or_id"
                and normalized_value == "DEMO-PASSPORT-001"
            )
        )

        if not valid_lookup:
            return StaffCustomerLookupResponse(
                status="not_found",
                access_state="unavailable",
                user_message="No matching demo customer record found.",
            )

        return StaffCustomerLookupResponse(
            status="found",
            customer_id="CUST-DA-2026-001",
            customer_name="Claudio Demo",
            relationship_status="Active",
            access_state="locked",
            user_message=(
                "Customer record found. Sensitive details require customer "
                "authorization."
            ),
        )

    def request_authorization(
        self,
        customer_id: str,
        method: AuthorizationMethod,
    ) -> StaffCustomerAuthorizationResponse:
        if customer_id != "CUST-DA-2026-001":
            return StaffCustomerAuthorizationResponse(
                status="not_found",
                access_state="unavailable",
                user_message="No matching demo customer record found.",
            )

        request_id = f"ACCESS-{uuid4().hex[:12].upper()}"
        if method == "mobile_approval":
            user_message = (
                "A simulated authorization request has been sent to the "
                "customer's banking app."
            )
        else:
            user_message = (
                "A private credential entry screen is ready for the customer."
            )

        self.access_requests[request_id] = AccessRequest(
            request_id=request_id,
            customer_id=customer_id,
            method=method,
            status="pending_customer_authorization",
            access_state="locked",
            user_message=user_message,
        )

        return StaffCustomerAuthorizationResponse(
            status="pending_customer_authorization",
            request_id=request_id,
            method=method,
            customer_id=customer_id,
            access_state="locked",
            user_message=user_message,
        )

    def approve_authorization(
        self,
        request_id: str,
        approved: bool,
    ) -> StaffCustomerAccessApprovalResponse:
        access_request = self.access_requests.get(request_id)
        if access_request is None:
            return StaffCustomerAccessApprovalResponse(
                status="not_found",
                access_state="unavailable",
                user_message="No matching authorization request found.",
            )

        if not approved:
            access_request.status = "rejected"
            access_request.access_state = "locked"
            access_request.user_message = "Customer authorization was rejected."
            self._record_access_event(access_request, approved=False)
            return StaffCustomerAccessApprovalResponse(
                status="rejected",
                access_state="locked",
                user_message="Customer authorization was rejected.",
            )

        access_request.status = "authorized"
        access_request.access_state = "unlocked"
        access_request.user_message = (
            "Customer authorized temporary staff access to the record."
        )
        self._record_access_event(access_request, approved=True)

        return StaffCustomerAccessApprovalResponse(
            status="authorized",
            access_state="unlocked",
            customer_record=self._customer_record_details(),
            access_expires_in_minutes=15,
            user_message=(
                "Customer authorized temporary staff access to the record."
            ),
        )

    def get_status(self, request_id: str) -> StaffCustomerAccessStatusResponse:
        access_request = self.access_requests.get(request_id)
        if access_request is None:
            return StaffCustomerAccessStatusResponse(
                status="not_found",
                access_state="unavailable",
                request_id=request_id,
                user_message="No matching authorization request found.",
            )

        return StaffCustomerAccessStatusResponse(
            status=access_request.status,
            access_state=access_request.access_state,
            method=access_request.method,
            customer_id=access_request.customer_id,
            request_id=access_request.request_id,
            user_message=access_request.user_message,
        )

    def _customer_record_details(self) -> StaffCustomerRecordDetails:
        return StaffCustomerRecordDetails(
            customer_id="CUST-DA-2026-001",
            bank_user_id="12345678",
            name="Claudio Demo",
            account_id="aurora-current",
            relationship_status="Active",
            identity_verification_status="Completed by bank",
            source_of_funds_status="Reviewed by bank",
            online_banking_enabled=True,
            strong_authentication_enabled=True,
            digital_assets_eligible=True,
        )

    def _record_access_event(
        self,
        access_request: AccessRequest,
        approved: bool,
    ) -> None:
        self.audit_log.record_event(
            module="bank_staff",
            action_type=(
                "staff_customer_access_authorized"
                if approved
                else "staff_customer_access_rejected"
            ),
            status="completed",
            decision="approved" if approved else "rejected",
            reasons=[
                f"request_id={access_request.request_id}",
                f"customer_id={access_request.customer_id}",
                f"method={access_request.method}",
            ],
            user_message=access_request.user_message,
        )


staff_customer_access_service = StaffCustomerAccessService()
