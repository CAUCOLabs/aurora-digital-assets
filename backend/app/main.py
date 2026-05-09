from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.audit_events import router as audit_events_router
from app.api.routes.health import router as health_router
from app.api.routes.review_cases import router as review_cases_router
from app.api.routes.withdrawals import router as withdrawals_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        description=(
            "Simulated backend for the Aurora Digital Assets banking prototype."
        ),
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router, prefix=settings.api_prefix)
    app.include_router(withdrawals_router, prefix=settings.api_prefix)
    app.include_router(review_cases_router, prefix=settings.api_prefix)
    app.include_router(audit_events_router, prefix=settings.api_prefix)

    return app


app = create_app()
