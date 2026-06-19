from typing import Literal

from pydantic import BaseModel


CustodianIntegrationGuardrailSeverity = Literal[
    "low",
    "medium",
    "high",
    "critical",
]
CustodianIntegrationGuardrailDecision = Literal[
    "allow",
    "harden",
    "block_integration",
    "review_required",
]


class CustodianIntegrationGuardrailControl(BaseModel):
    control_id: str
    title: str
    control_layer: str
    description: str
    enabled: bool = True


class CustodianIntegrationGuardrailScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    expected_decision: CustodianIntegrationGuardrailDecision
    required_controls: list[str]


class CustodianIntegrationGuardrailEvaluationRequest(BaseModel):
    scenario_id: str
    integration_target: str = "future_regulated_custodian"
    environment: str = "prototype"
    custodian_regulated: bool = False
    asset_segregation_confirmed: bool = False
    liability_boundary_defined: bool = False
    sla_contract_signed: bool = False
    audit_reports_available: bool = False
    insurance_coverage_confirmed: bool = False
    transfer_limits_configured: bool = False
    withdrawal_approval_required: bool = False
    api_access_controls_defined: bool = False
    key_management_boundary_defined: bool = False
    incident_reporting_defined: bool = False
    reconciliation_defined: bool = False
    evidence_export_available: bool = False
    regulatory_reporting_defined: bool = False
    responsibility_matrix_defined: bool = False
    aurora_custodian_boundary_defined: bool = False
    future_cloud_k8s_boundary_defined: bool = False
    active_ai_threat_case_id: str | None = None
    active_ai_threat_case_status: str | None = None
    active_secret_guard_case_id: str | None = None
    active_secret_guard_case_status: str | None = None
    active_cloud_k8s_guard_case_id: str | None = None
    active_cloud_k8s_guard_case_status: str | None = None
    reviewer_id: str = "system"


class CustodianIntegrationGuardrailEvaluationResponse(BaseModel):
    scenario_id: str
    integration_target: str
    environment: str
    risk_score: int
    severity: CustodianIntegrationGuardrailSeverity
    decision: CustodianIntegrationGuardrailDecision
    integration_guard_applied: bool
    integration_blocked: bool
    required_controls: list[str]
    missing_controls: list[str]
    satisfied_controls: list[str]
    linked_ai_threat_case_id: str | None = None
    linked_secret_guard_case_id: str | None = None
    linked_cloud_k8s_guard_case_id: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    review_case_required: bool
    review_case_id: str | None = None
    recommended_next_actions: list[str]
    created_at: str
