import { getJson, postJson } from './apiClient'

export type InfrastructureSecurityLayerType =
  | 'application'
  | 'kubernetes'
  | 'cloud_iam'
  | 'secrets'
  | 'audit'
  | 'risk_operations'
export type InfrastructureSecurityControlCategory =
  | 'object_authorization'
  | 'template_safety'
  | 'rbac'
  | 'namespace_isolation'
  | 'service_account'
  | 'iam_trust'
  | 'iam_permissions'
  | 'secret_management'
  | 'logging'
  | 'chain_containment'
export type InfrastructureSecurityChainStage =
  | 'initial_access'
  | 'privilege_expansion'
  | 'lateral_movement'
  | 'secret_exposure'
  | 'cloud_role_misuse'
  | 'evidence_required'
  | 'contained'
export type InfrastructureSecuritySeverity = 'low' | 'medium' | 'high' | 'critical'
export type InfrastructureSecurityDecision =
  | 'allow'
  | 'block'
  | 'review_required'
  | 'harden_required'
  | 'escalate'
export type InfrastructureSecurityEventStatus =
  | 'new'
  | 'blocked'
  | 'under_review'
  | 'escalated'
  | 'contained'
  | 'closed'
export type InfrastructureSecurityPosture =
  | 'hardened'
  | 'monitored'
  | 'restricted'
  | 'review_required'
  | 'critical_gap'

export type InfrastructureSecurityControl = {
  control_id: string
  title: string
  layer: InfrastructureSecurityLayerType
  category: InfrastructureSecurityControlCategory
  description: string
  protected_assets: string[]
  decision_model: string
  evidence_outputs: string[]
  enabled: boolean
}

export type InfrastructureSecurityEvent = {
  event_id: string
  title: string
  affected_layer: InfrastructureSecurityLayerType
  chain_stage: InfrastructureSecurityChainStage
  risk_type: string
  severity: InfrastructureSecuritySeverity
  decision: InfrastructureSecurityDecision
  status: InfrastructureSecurityEventStatus
  triggered_controls: string[]
  affected_asset: string
  summary: string
  chain_reaction_risk: string
  recommended_action: string
  evidence_package_ready: boolean
  created_at: string
  audit_event_id?: string | null
  correlation_id?: string | null
}

export type InfrastructureSecurityLayer = {
  layer_id: string
  name: string
  layer_type: InfrastructureSecurityLayerType
  posture: InfrastructureSecurityPosture
  risk_summary: string
  controls_applied: string[]
  monitored_signals: string[]
}

export type InfrastructureSecurityScenario = {
  scenario_id: string
  title: string
  description: string
  starting_layer: InfrastructureSecurityLayerType
  possible_chain: string[]
  risk_indicators: string[]
  expected_decision: InfrastructureSecurityDecision
  recommended_controls: string[]
}

export type EvaluateInfrastructureSecurityScenarioRequest = {
  scenario_id: string
  object_authorization_failed: boolean
  unsafe_template_input_detected: boolean
  pod_privileged: boolean
  service_account_can_read_secrets: boolean
  cloud_iam_wildcard_permissions: boolean
  weak_trust_policy: boolean
  secret_exposure_detected: boolean
}

export type EvaluateInfrastructureSecurityScenarioResponse = {
  risk_score: number
  severity: InfrastructureSecuritySeverity
  decision: InfrastructureSecurityDecision
  affected_layers: string[]
  chain_reaction_risk: string
  triggered_controls: string[]
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  evidence_package_ready: boolean
  recommended_action: string
  explanation: string
}

export function getInfrastructureSecurityControls(): Promise<
  InfrastructureSecurityControl[]
> {
  return getJson<InfrastructureSecurityControl[]>('/infrastructure-security/controls')
}

export function getInfrastructureSecurityEvents(): Promise<
  InfrastructureSecurityEvent[]
> {
  return getJson<InfrastructureSecurityEvent[]>('/infrastructure-security/events')
}

export function getInfrastructureSecurityLayers(): Promise<
  InfrastructureSecurityLayer[]
> {
  return getJson<InfrastructureSecurityLayer[]>('/infrastructure-security/layers')
}

export function getInfrastructureSecurityScenarios(): Promise<
  InfrastructureSecurityScenario[]
> {
  return getJson<InfrastructureSecurityScenario[]>(
    '/infrastructure-security/scenarios',
  )
}

export function evaluateInfrastructureSecurityScenario(
  payload: EvaluateInfrastructureSecurityScenarioRequest,
): Promise<EvaluateInfrastructureSecurityScenarioResponse> {
  return postJson<
    EvaluateInfrastructureSecurityScenarioResponse,
    EvaluateInfrastructureSecurityScenarioRequest
  >('/infrastructure-security/evaluate-scenario', payload)
}
