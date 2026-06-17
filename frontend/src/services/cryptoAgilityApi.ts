import { getJson, postJson } from './apiClient'

export type CryptoAssetDomain =
  | 'tls'
  | 'session_tokens'
  | 'api_keys'
  | 'internal_signatures'
  | 'database_encryption'
  | 'backup_encryption'
  | 'audit_integrity'
  | 'wallet_keys'
  | 'custody_keys'
  | 'microservice_communication'
  | 'cloud_certificates'
  | 'admin_recovery'
export type CryptoRiskLevel = 'low' | 'medium' | 'high' | 'critical'
export type CryptoMigrationReadiness =
  | 'ready'
  | 'partial'
  | 'gap_detected'
  | 'not_assessed'
export type CryptoAgilityDecision =
  | 'allow'
  | 'review_required'
  | 'migration_required'
  | 'harden_required'
  | 'escalate'
export type CryptoAgilitySeverity = 'low' | 'medium' | 'high' | 'critical'

export type CryptoAsset = {
  asset_id: string
  name: string
  domain: CryptoAssetDomain
  owner: string
  data_classification: string
  current_algorithm: string
  algorithm_family: string
  algorithm_version: string
  key_location: string
  rotation_period_days: number
  last_rotated_at: string
  next_rotation_due: string
  long_term_confidentiality_required: boolean
  harvest_now_decrypt_later_risk: CryptoRiskLevel
  migration_readiness: CryptoMigrationReadiness
  blockchain_protocol_dependency: boolean
  notes: string
}

export type CryptoAlgorithmPolicy = {
  policy_id: string
  algorithm_family: string
  approved_current: string[]
  deprecated: string[]
  migration_candidates: string[]
  status: string
  reason: string
  crypto_owner: string
  evidence_outputs: string[]
}

export type CryptoKeyLifecycleItem = {
  key_id: string
  asset_id: string
  purpose: string
  status: string
  storage_boundary: string
  rotation_required: boolean
  emergency_rollover_ready: boolean
  audit_required: boolean
  reviewer_note: string
}

export type CryptoAgilityScenario = {
  scenario_id: string
  title: string
  description: string
  affected_assets: string[]
  risk_indicators: string[]
  expected_decision: CryptoAgilityDecision
  recommended_controls: string[]
}

export type EvaluateCryptoAgilityScenarioRequest = {
  scenario_id: string
  deprecated_algorithm_detected: boolean
  long_lived_key_detected: boolean
  missing_algorithm_versioning: boolean
  missing_key_rotation_policy: boolean
  backup_long_term_risk: boolean
  audit_integrity_gap: boolean
  custody_key_rotation_gap: boolean
  blockchain_protocol_confusion: boolean
  post_quantum_readiness_gap: boolean
  kms_hsm_integration_missing: boolean
}

export type EvaluateCryptoAgilityScenarioResponse = {
  risk_score: number
  severity: CryptoAgilitySeverity
  decision: CryptoAgilityDecision
  affected_domains: CryptoAssetDomain[]
  crypto_agility_risk: string
  triggered_controls: string[]
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  evidence_package_ready: boolean
  recommended_action: string
  explanation: string
}

export function getCryptoAssets(): Promise<CryptoAsset[]> {
  return getJson<CryptoAsset[]>('/crypto-agility/assets')
}

export function getCryptoPolicies(): Promise<CryptoAlgorithmPolicy[]> {
  return getJson<CryptoAlgorithmPolicy[]>('/crypto-agility/policies')
}

export function getCryptoKeyLifecycle(): Promise<CryptoKeyLifecycleItem[]> {
  return getJson<CryptoKeyLifecycleItem[]>('/crypto-agility/key-lifecycle')
}

export function getCryptoScenarios(): Promise<CryptoAgilityScenario[]> {
  return getJson<CryptoAgilityScenario[]>('/crypto-agility/scenarios')
}

export function evaluateCryptoScenario(
  payload: EvaluateCryptoAgilityScenarioRequest,
): Promise<EvaluateCryptoAgilityScenarioResponse> {
  return postJson<
    EvaluateCryptoAgilityScenarioResponse,
    EvaluateCryptoAgilityScenarioRequest
  >('/crypto-agility/evaluate-scenario', payload)
}
