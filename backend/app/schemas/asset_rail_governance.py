from pydantic import BaseModel


class AssetRailTypeItem(BaseModel):
    type_id: str
    description: str


class AssetRailControlMatrixItem(BaseModel):
    asset_type: str
    default_rail_type: str
    required_control_domains: list[str]
    not_applicable_control_domains: list[str]
    control_decisions: list[str]


class AssetRailClassificationRequest(BaseModel):
    asset_symbol: str
    asset_name: str | None = None
    declared_asset_type: str | None = None
    declared_rail_type: str | None = None
    issuer_type: str | None = None
    issuer_jurisdiction: str | None = None
    is_central_bank_money: bool = False
    is_bank_liability: bool = False
    is_stablecoin: bool = False
    is_e_money_token: bool = False
    is_asset_referenced_token: bool = False
    is_cryptoasset: bool = False
    is_security_token: bool = False
    uses_external_custodian: bool = False
    uses_blockchain_execution: bool = False
    uses_private_keys: bool = False
    distributed_by_psp: bool = False
    redemption_rights_defined: bool = False
    reserve_model_defined: bool = False
    holding_limits_required: bool = False
    offline_mode_supported: bool = False
    privacy_controls_required: bool = False
    environment: str = "local"
    reviewer_id: str | None = None


class AssetRailClassificationResponse(BaseModel):
    asset_symbol: str
    asset_name: str | None = None
    asset_type: str
    rail_type: str
    custody_model: str
    settlement_model: str
    primary_control_domains: list[str]
    required_controls: list[str]
    not_applicable_controls: list[str]
    control_decisions: list[str]
    classification_confidence: int
    classification_level: str
    external_custodian_required: bool
    blockchain_execution_required: bool
    psp_intermediation_required: bool
    bank_ledger_controls_required: bool
    issuer_controls_required: bool
    redemption_controls_required: bool
    reserve_controls_required: bool
    privacy_controls_required: bool
    holding_limits_required: bool
    evidence_required: bool
    review_required: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class AssetRailControlSet(BaseModel):
    asset_classification_confirmed: bool = False
    settlement_rail_confirmed: bool = False
    custody_model_confirmed: bool = False
    issuer_governance_defined: bool = False
    redemption_model_defined: bool = False
    reserve_model_defined: bool = False
    psp_intermediation_defined: bool = False
    bank_ledger_controls_defined: bool = False
    custodian_readiness_completed: bool = False
    private_key_boundary_defined: bool = False
    blockchain_execution_boundary_defined: bool = False
    securities_controls_defined: bool = False
    holding_limits_defined: bool = False
    offline_online_mode_defined: bool = False
    privacy_controls_defined: bool = False
    aml_controls_defined: bool = False
    evidence_review_defined: bool = False
    human_approval_integrity_required: bool = False
    agent_governance_required: bool = False
    operational_resilience_defined: bool = False
    regulatory_disclaimer_present: bool = False


class AssetRailControlEvaluationRequest(BaseModel):
    asset_symbol: str
    asset_type: str
    rail_type: str
    environment: str = "local"
    controls: AssetRailControlSet
    linked_custodian_guard_case_id: str | None = None
    linked_human_integrity_audit_event_id: str | None = None
    linked_agent_governance_audit_event_id: str | None = None
    reviewer_id: str | None = None


class AssetRailControlEvaluationResponse(BaseModel):
    asset_symbol: str
    asset_type: str
    rail_type: str
    governance_decision: str
    governance_score: int
    governance_level: str
    satisfied_controls: list[str]
    missing_controls: list[str]
    not_applicable_controls: list[str]
    required_control_domains: list[str]
    blocking_reasons: list[str]
    recommended_next_actions: list[str]
    external_custodian_required: bool
    blockchain_execution_required: bool
    psp_intermediation_required: bool
    bank_ledger_controls_required: bool
    issuer_controls_required: bool
    redemption_controls_required: bool
    reserve_controls_required: bool
    evidence_required: bool
    review_required: bool
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    safety_notice: str
    created_at: str


class AssetRailGovernanceSummaryRequest(BaseModel):
    asset_symbol: str
    asset_name: str | None = None
    asset_type: str
    rail_type: str
    governance_decision: str
    governance_score: int
    reviewer_id: str | None = None


class AssetRailGovernanceSummaryResponse(BaseModel):
    summary_id: str
    title: str
    asset_symbol: str
    asset_type: str
    rail_type: str
    summary_points: list[str]
    risk_notes: list[str]
    required_next_steps: list[str]
    safety_notice: str
    created_at: str
