from fastapi import APIRouter

from app.schemas.auth import (
    BankLoginRequest,
    BankLoginResponse,
    BankSessionResponse,
    LogoutRequest,
    LogoutResponse,
    MobileApprovalRequest,
    MobileApprovalResponse,
)
from app.services.auth_service import auth_service


router = APIRouter(prefix="/auth", tags=["authentication prototype"])


@router.post("/login", response_model=BankLoginResponse)
def login_to_bank(request: BankLoginRequest) -> BankLoginResponse:
    return auth_service.login(request)


@router.post("/mobile-approval", response_model=MobileApprovalResponse)
def approve_mobile_login(request: MobileApprovalRequest) -> MobileApprovalResponse:
    return auth_service.process_mobile_approval(
        challenge_id=request.challenge_id,
        approved=request.approved,
    )


@router.get("/session", response_model=BankSessionResponse)
def get_bank_session(session_id: str) -> BankSessionResponse:
    return auth_service.get_session(session_id)


@router.post("/logout", response_model=LogoutResponse)
def logout_from_bank(request: LogoutRequest) -> LogoutResponse:
    return auth_service.logout(request.session_id)
