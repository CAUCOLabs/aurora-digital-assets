from fastapi import APIRouter

from app.schemas.account import (
    BankAccount,
    BankTransaction,
    ConnectedDigitalAssetBalance,
)
from app.services.account_service import AccountService


router = APIRouter(prefix="/accounts", tags=["accounts"])
account_service = AccountService()


@router.get("", response_model=list[BankAccount])
def list_accounts() -> list[BankAccount]:
    return account_service.list_accounts()


@router.get(
    "/connected-digital-assets",
    response_model=list[ConnectedDigitalAssetBalance],
)
def list_connected_digital_asset_balances() -> list[ConnectedDigitalAssetBalance]:
    return account_service.list_connected_digital_asset_balances()


@router.get("/{account_id}/transactions", response_model=list[BankTransaction])
def list_account_transactions(account_id: str) -> list[BankTransaction]:
    return account_service.list_account_transactions(account_id)
