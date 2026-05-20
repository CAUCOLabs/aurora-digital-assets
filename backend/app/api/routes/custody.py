from fastapi import APIRouter

from app.schemas.custody import CustodyStatus
from app.services.custody_service import CustodyService


router = APIRouter(prefix="/custody", tags=["custody"])
custody_service = CustodyService()


@router.get("/status", response_model=CustodyStatus)
def get_custody_status() -> CustodyStatus:
    return custody_service.get_custody_status()
