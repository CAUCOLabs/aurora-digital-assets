from typing import Literal

from pydantic import BaseModel


InfrastructureSecurityLayerType = Literal[
    "application",
    "kubernetes",
    "cloud_iam",
    "secrets",
    "audit",
    "risk_operations",
]
InfrastructureSecurityControlCategory = Literal[
    "object_authorization",
    "template_safety",
    "rbac",
    "namespace_isolation",
    "service_account",
    "iam_trust",
    "iam_permissions",
    "secret_management",
    "logging",
    "chain_containment",
    "cloud_storage_access",
    "certificate_protection",
    "service_principal_least_privilege",
    "deployment_access_control",
    "managed_identity_scope",
    "privileged_identity_management",
    "identity_monitoring",
    "key_vault_monitoring",
    "storage_identity_chain_containment",
    "dockerfile_hardening",
    "image_secret_exposure",
    "non_root_runtime",
    "dependency_surface",
    "image_version_pinning",
    "kubernetes_security_context",
    "service_account_token_control",
    "kubernetes_rbac_least_privilege",
    "network_policy_isolation",
    "resource_limit_enforcement",
    "cluster_cis_audit",
    "devsecops_verification",
    "runtime_hardening_evidence",
]
InfrastructureSecurityChainStage = Literal[
    "initial_access",
    "privilege_expansion",
    "lateral_movement",
    "secret_exposure",
    "cloud_role_misuse",
    "deployment_access_abuse",
    "evidence_required",
    "contained",
]
InfrastructureSecuritySeverity = Literal["low", "medium", "high", "critical"]
InfrastructureSecurityDecision = Literal[
    "allow",
    "block",
    "review_required",
    "harden_required",
    "escalate",
]
InfrastructureSecurityEventStatus = Literal[
    "new",
    "blocked",
    "under_review",
    "escalated",
    "contained",
    "closed",
]
InfrastructureSecurityPosture = Literal[
    "hardened",
    "monitored",
    "restricted",
    "review_required",
    "critical_gap",
]


class InfrastructureSecurityControl(BaseModel):
    control_id: str
    title: str
    layer: InfrastructureSecurityLayerType
    category: InfrastructureSecurityControlCategory
    description: str
    protected_assets: list[str]
    decision_model: str
    evidence_outputs: list[str]
    enabled: bool


class InfrastructureSecurityEvent(BaseModel):
    event_id: str
    title: str
    affected_layer: InfrastructureSecurityLayerType
    chain_stage: InfrastructureSecurityChainStage
    risk_type: str
    severity: InfrastructureSecuritySeverity
    decision: InfrastructureSecurityDecision
    status: InfrastructureSecurityEventStatus
    triggered_controls: list[str]
    affected_asset: str
    summary: str
    chain_reaction_risk: str
    recommended_action: str
    evidence_package_ready: bool
    created_at: str
    audit_event_id: str | None = None
    correlation_id: str | None = None


class InfrastructureSecurityLayer(BaseModel):
    layer_id: str
    name: str
    layer_type: InfrastructureSecurityLayerType
    posture: InfrastructureSecurityPosture
    risk_summary: str
    controls_applied: list[str]
    monitored_signals: list[str]


class InfrastructureSecurityScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    starting_layer: InfrastructureSecurityLayerType
    possible_chain: list[str]
    risk_indicators: list[str]
    expected_decision: InfrastructureSecurityDecision
    recommended_controls: list[str]


class EvaluateInfrastructureSecurityScenarioRequest(BaseModel):
    scenario_id: str
    object_authorization_failed: bool
    unsafe_template_input_detected: bool
    pod_privileged: bool
    service_account_can_read_secrets: bool
    cloud_iam_wildcard_permissions: bool
    weak_trust_policy: bool
    secret_exposure_detected: bool
    storage_public_access_detected: bool = False
    certificate_exposure_detected: bool = False
    service_principal_overprivileged: bool = False
    deployment_credentials_enabled: bool = False
    managed_identity_excessive_scope: bool = False
    password_reset_privilege_detected: bool = False
    identity_monitoring_gap: bool = False
    dockerfile_secrets_detected: bool = False
    image_uses_latest_tag: bool = False
    container_runs_as_root: bool = False
    plaintext_secrets_in_manifest: bool = False
    missing_security_context: bool = False
    service_account_token_mounted: bool = False
    rbac_wildcard_permissions: bool = False
    can_read_kubernetes_secrets: bool = False
    network_policy_missing: bool = False
    resource_limits_missing: bool = False
    cis_audit_missing: bool = False
    hardening_verification_missing: bool = False


class EvaluateInfrastructureSecurityScenarioResponse(BaseModel):
    risk_score: int
    severity: InfrastructureSecuritySeverity
    decision: InfrastructureSecurityDecision
    affected_layers: list[str]
    chain_reaction_risk: str
    triggered_controls: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    recommended_action: str
    explanation: str
