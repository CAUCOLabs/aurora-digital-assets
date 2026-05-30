from fastapi import APIRouter

from app.schemas.bank_staff import (
    BankCustomerRecordResponse,
    BankStaffOnboardingModelResponse,
)
from app.services.bank_staff_service import bank_staff_service


router = APIRouter(prefix="/bank-staff", tags=["bank staff"])


@router.get("/onboarding-model", response_model=BankStaffOnboardingModelResponse)
def get_onboarding_model() -> BankStaffOnboardingModelResponse:
    return bank_staff_service.get_onboarding_model()


@router.get("/customer-record", response_model=BankCustomerRecordResponse)
def get_customer_record() -> BankCustomerRecordResponse:
    return bank_staff_service.get_customer_record()
