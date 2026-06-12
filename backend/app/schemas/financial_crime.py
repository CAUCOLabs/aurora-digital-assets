from typing import Literal

from pydantic import BaseModel


Severity = Literal["low", "medium", "high", "critical"]
EntityType = Literal["employee", "customer", "company", "account", "transaction", "wallet"]
AlertStatus = Literal["new", "under_review", "escalated", "closed"]
EvaluationDecision = Literal["allow", "review_required", "escalate"]


class RiskScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    risk_indicators: list[str]


class MonitoringControl(BaseModel):
    control_id: str
    title: str
    category: str
    description: str
    evidence_outputs: list[str]


class FinancialCrimeAlert(BaseModel):
    alert_id: str
    title: str
    risk_type: str
    severity: Severity
    entity_type: EntityType
    entity_name: str
    amount_eur: float
    status: AlertStatus
    triggered_rules: list[str]
    recommended_action: str
    linked_review_case_id: str | None = None
    evidence_summary: str
    created_at: str


class EvaluateDemoActivityRequest(BaseModel):
    scenario_id: str
    amount_eur: float
    entity_type: str


class EvaluateDemoActivityResponse(BaseModel):
    risk_score: int
    severity: Severity
    decision: EvaluationDecision
    triggered_rules: list[str]
    recommended_action: str
    explanation: str
