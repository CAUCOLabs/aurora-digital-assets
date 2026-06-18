from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.accounts import router as accounts_router
from app.api.routes.ai_threat_defense import router as ai_threat_defense_router
from app.api.routes.api_security import router as api_security_router
from app.api.routes.audit_events import router as audit_events_router
from app.api.routes.auth import router as auth_router
from app.api.routes.bank_access import router as bank_access_router
from app.api.routes.bank_staff import router as bank_staff_router
from app.api.routes.buy_sell import router as buy_sell_router
from app.api.routes.compliance_intelligence import (
    router as compliance_intelligence_router,
)
from app.api.routes.custody import router as custody_router
from app.api.routes.crypto_agility import router as crypto_agility_router
from app.api.routes.demo_admin import router as demo_admin_router
from app.api.routes.digital_assets import router as digital_assets_router
from app.api.routes.evidence_packages import router as evidence_packages_router
from app.api.routes.financial_crime import router as financial_crime_router
from app.api.routes.health import router as health_router
from app.api.routes.infrastructure_security import (
    router as infrastructure_security_router,
)
from app.api.routes.operational_resilience import (
    router as operational_resilience_router,
)
from app.api.routes.payments import router as payments_router
from app.api.routes.reports import router as reports_router
from app.api.routes.review_cases import router as review_cases_router
from app.api.routes.risk_operations import router as risk_operations_router
from app.api.routes.sensitive_approval import router as sensitive_approval_router
from app.api.routes.staff_customer_access import (
    router as staff_customer_access_router,
)
from app.api.routes.withdrawals import router as withdrawals_router
from app.core.config import settings
from app.db.database import initialize_database
from app.storage.sqlite_store import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        description=(
            "Simulated backend for the Aurora Digital Assets banking prototype."
        ),
        lifespan=lifespan,
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
    app.include_router(payments_router, prefix=settings.api_prefix)
    app.include_router(buy_sell_router, prefix=settings.api_prefix)
    app.include_router(review_cases_router, prefix=settings.api_prefix)
    app.include_router(audit_events_router, prefix=settings.api_prefix)
    app.include_router(demo_admin_router, prefix=settings.api_prefix)
    app.include_router(reports_router, prefix=settings.api_prefix)
    app.include_router(accounts_router, prefix=settings.api_prefix)
    app.include_router(digital_assets_router, prefix=settings.api_prefix)
    app.include_router(custody_router, prefix=settings.api_prefix)
    app.include_router(bank_access_router, prefix=settings.api_prefix)
    app.include_router(bank_staff_router, prefix=settings.api_prefix)
    app.include_router(staff_customer_access_router, prefix=settings.api_prefix)
    app.include_router(financial_crime_router, prefix=settings.api_prefix)
    app.include_router(compliance_intelligence_router, prefix=settings.api_prefix)
    app.include_router(evidence_packages_router, prefix=settings.api_prefix)
    app.include_router(operational_resilience_router, prefix=settings.api_prefix)
    app.include_router(risk_operations_router, prefix=settings.api_prefix)
    app.include_router(api_security_router, prefix=settings.api_prefix)
    app.include_router(infrastructure_security_router, prefix=settings.api_prefix)
    app.include_router(crypto_agility_router, prefix=settings.api_prefix)
    app.include_router(sensitive_approval_router, prefix=settings.api_prefix)
    app.include_router(ai_threat_defense_router, prefix=settings.api_prefix)
    app.include_router(auth_router, prefix=settings.api_prefix)

    return app


app = create_app()
