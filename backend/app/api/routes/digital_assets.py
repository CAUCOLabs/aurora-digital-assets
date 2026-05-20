from fastapi import APIRouter

from app.schemas.digital_asset import (
    DigitalAssetActivity,
    SupportedDigitalAsset,
    WalletBalance,
)
from app.services.digital_asset_service import DigitalAssetService


router = APIRouter(prefix="/digital-assets", tags=["digital-assets"])
digital_asset_service = DigitalAssetService()


@router.get("/assets", response_model=list[SupportedDigitalAsset])
def list_supported_assets() -> list[SupportedDigitalAsset]:
    return digital_asset_service.list_supported_assets()


@router.get("/wallet", response_model=list[WalletBalance])
def get_wallet_balances() -> list[WalletBalance]:
    return digital_asset_service.get_wallet_balances()


@router.get("/activity", response_model=list[DigitalAssetActivity])
def get_digital_asset_activity() -> list[DigitalAssetActivity]:
    return digital_asset_service.get_digital_asset_activity()
