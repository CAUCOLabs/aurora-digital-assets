from fastapi import APIRouter

from app.schemas.financial_crime import (
    EvaluateDemoActivityRequest,
    EvaluateDemoActivityResponse,
    FinancialCrimeAlert,
    MonitoringControl,
    RiskScenario,
)
from app.services.financial_crime_service import financial_crime_service


router = APIRouter(prefix="/financial-crime", tags=["financial crime"])


@router.get("/risk-scenarios", response_model=list[RiskScenario])
def get_risk_scenarios() -> list[RiskScenario]:
    return financial_crime_service.list_risk_scenarios()


@router.get("/monitoring-controls", response_model=list[MonitoringControl])
def get_monitoring_controls() -> list[MonitoringControl]:
    return financial_crime_service.list_monitoring_controls()


@router.get("/demo-alerts", response_model=list[FinancialCrimeAlert])
def get_demo_alerts() -> list[FinancialCrimeAlert]:
    return financial_crime_service.list_demo_alerts()


@router.post(
    "/evaluate-demo-activity",
    response_model=EvaluateDemoActivityResponse,
)
def evaluate_demo_activity(
    request: EvaluateDemoActivityRequest,
) -> EvaluateDemoActivityResponse:
    return financial_crime_service.evaluate_demo_activity(
        scenario_id=request.scenario_id,
        amount_eur=request.amount_eur,
        entity_type=request.entity_type,
    )
