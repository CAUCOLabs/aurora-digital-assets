from typing import Literal

from pydantic import BaseModel


CryptoAssetDomain = Literal[
    "tls",
    "session_tokens",
    "api_keys",
    "internal_signatures",
    "database_encryption",
    "backup_encryption",
    "audit_integrity",
    "wallet_keys",
    "custody_keys",
    "microservice_communication",
    "cloud_certificates",
    "admin_recovery",
]
CryptoDataClassification = Literal[
    "public",
    "internal",
    "confidential",
    "regulated",
    "critical",
]
CryptoAlgorithmFamily = Literal[
    "symmetric",
    "asymmetric",
    "signature",
    "hash",
    "key_exchange",
    "certificate",
    "custody",
    "external_blockchain",
]
CryptoKeyLocation = Literal[
    "application_config",
    "database",
    "cloud_secret_manager",
    "hsm",
    "key_vault",
    "external_provider",
    "simulated",
]
CryptoRiskLevel = Literal["low", "medium", "high", "critical"]
CryptoMigrationReadiness = Literal[
    "ready",
    "partial",
    "gap_detected",
    "not_assessed",
]
CryptoPolicyStatus = Literal[
    "active",
    "deprecated",
    "migration_required",
    "retired",
    "monitored",
]
CryptoKeyLifecycleStatus = Literal[
    "active",
    "rotation_due",
    "deprecated",
    "revoked",
    "retired",
]
CryptoAgilityDecision = Literal[
    "allow",
    "review_required",
    "migration_required",
    "harden_required",
    "escalate",
]
CryptoAgilitySeverity = Literal["low", "medium", "high", "critical"]


class CryptoAsset(BaseModel):
    asset_id: str
    name: str
    domain: CryptoAssetDomain
    owner: str
    data_classification: CryptoDataClassification
    current_algorithm: str
    algorithm_family: CryptoAlgorithmFamily
    algorithm_version: str
    key_location: CryptoKeyLocation
    rotation_period_days: int
    last_rotated_at: str
    next_rotation_due: str
    long_term_confidentiality_required: bool
    harvest_now_decrypt_later_risk: CryptoRiskLevel
    migration_readiness: CryptoMigrationReadiness
    blockchain_protocol_dependency: bool
    notes: str


class CryptoAlgorithmPolicy(BaseModel):
    policy_id: str
    algorithm_family: CryptoAlgorithmFamily
    approved_current: list[str]
    deprecated: list[str]
    migration_candidates: list[str]
    status: CryptoPolicyStatus
    reason: str
    crypto_owner: str
    evidence_outputs: list[str]


class CryptoKeyLifecycleItem(BaseModel):
    key_id: str
    asset_id: str
    purpose: str
    status: CryptoKeyLifecycleStatus
    storage_boundary: str
    rotation_required: bool
    emergency_rollover_ready: bool
    audit_required: bool
    reviewer_note: str


class CryptoAgilityScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    affected_assets: list[str]
    risk_indicators: list[str]
    expected_decision: CryptoAgilityDecision
    recommended_controls: list[str]


class EvaluateCryptoAgilityScenarioRequest(BaseModel):
    scenario_id: str
    deprecated_algorithm_detected: bool = False
    long_lived_key_detected: bool = False
    missing_algorithm_versioning: bool = False
    missing_key_rotation_policy: bool = False
    backup_long_term_risk: bool = False
    audit_integrity_gap: bool = False
    custody_key_rotation_gap: bool = False
    blockchain_protocol_confusion: bool = False
    post_quantum_readiness_gap: bool = False
    kms_hsm_integration_missing: bool = False


class EvaluateCryptoAgilityScenarioResponse(BaseModel):
    risk_score: int
    severity: CryptoAgilitySeverity
    decision: CryptoAgilityDecision
    affected_domains: list[CryptoAssetDomain]
    crypto_agility_risk: str
    triggered_controls: list[str]
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    recommended_action: str
    explanation: str


class CryptoMigrationPlan(BaseModel):
    plan_id: str
    title: str
    source_domains: list[CryptoAssetDomain]
    migration_steps: list[str]
    evidence_outputs: list[str]
    owner: str
    status: CryptoMigrationReadiness
