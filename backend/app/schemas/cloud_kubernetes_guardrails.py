from typing import Literal

from pydantic import BaseModel


CloudKubernetesGuardrailSeverity = Literal["low", "medium", "high", "critical"]
CloudKubernetesGuardrailDecision = Literal[
    "allow",
    "harden",
    "block_deployment",
    "review_required",
]


class CloudKubernetesGuardrailControl(BaseModel):
    control_id: str
    title: str
    control_layer: str
    description: str
    enabled: bool = True


class CloudKubernetesGuardrailScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    expected_decision: CloudKubernetesGuardrailDecision
    required_controls: list[str]


class CloudKubernetesGuardrailEvaluationRequest(BaseModel):
    scenario_id: str
    deployment_target: str = "future_cloud"
    environment: str = "prototype"
    cloud_provider: str = "not_connected"
    kubernetes_enabled: bool = False
    secrets_externalized: bool = False
    rbac_least_privilege: bool = False
    network_policy_enabled: bool = False
    audit_logging_enabled: bool = False
    backup_encryption_enabled: bool = False
    image_provenance_checked: bool = False
    runtime_policy_enabled: bool = False
    namespace_isolation_enabled: bool = False
    active_ai_threat_case_id: str | None = None
    active_ai_threat_case_status: str | None = None
    active_secret_guard_case_id: str | None = None
    active_secret_guard_case_status: str | None = None
    reviewer_id: str = "system"


class CloudKubernetesGuardrailEvaluationResponse(BaseModel):
    scenario_id: str
    deployment_target: str
    environment: str
    risk_score: int
    severity: CloudKubernetesGuardrailSeverity
    decision: CloudKubernetesGuardrailDecision
    deployment_guard_applied: bool
    deployment_blocked: bool
    required_controls: list[str]
    missing_controls: list[str]
    satisfied_controls: list[str]
    linked_ai_threat_case_id: str | None = None
    linked_secret_guard_case_id: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    review_case_required: bool
    review_case_id: str | None = None
    recommended_next_actions: list[str]
    created_at: str
