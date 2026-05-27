from fastapi import APIRouter

from app.schemas.bank_access import (
    BankIntegrationModelResponse,
    BankSessionModelResponse,
)
from app.services.bank_access_service import bank_access_service


router = APIRouter(prefix="/bank-access", tags=["bank access"])


@router.get("/session-model", response_model=BankSessionModelResponse)
def get_session_model() -> BankSessionModelResponse:
    return bank_access_service.get_session_model()


@router.get("/integration-model", response_model=BankIntegrationModelResponse)
def get_integration_model() -> BankIntegrationModelResponse:
    return bank_access_service.get_integration_model()
