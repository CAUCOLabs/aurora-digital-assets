from typing import TypedDict

from fastapi import APIRouter

from app.core.config import settings


class HealthResponse(TypedDict):
    status: str
    service: str
    version: str


router = APIRouter(tags=["health"])


@router.get("/health", response_model=None)
def get_health() -> HealthResponse:
    return {
        "status": "ok",
        "service": settings.service_name,
        "version": settings.version,
    }
