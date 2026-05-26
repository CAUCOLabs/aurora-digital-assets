from fastapi import APIRouter

from app.schemas.demo_admin import (
    DemoResetResponse,
    DemoSeedResponse,
    DemoStatusResponse,
)
from app.services.demo_admin_service import demo_admin_service


router = APIRouter(prefix="/admin/demo", tags=["demo administration"])


@router.get("/status", response_model=DemoStatusResponse)
def get_demo_status() -> DemoStatusResponse:
    return demo_admin_service.get_status()


@router.post("/reset", response_model=DemoResetResponse)
def reset_demo_data() -> DemoResetResponse:
    return demo_admin_service.reset_demo_data()


@router.post("/seed", response_model=DemoSeedResponse)
def seed_demo_data() -> DemoSeedResponse:
    return demo_admin_service.seed_demo_data()
