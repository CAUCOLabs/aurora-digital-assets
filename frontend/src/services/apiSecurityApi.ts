import { getJson, postJson } from './apiClient'

export type ApiSecurityControlCategory =
  | 'batching'
  | 'rate_limit'
  | 'authorization'
  | 'schema_exposure'
  | 'mutation_control'
  | 'token_security'
  | 'audit_logging'
  | 'step_up_authentication'
export type ApiSecuritySurfaceType =
  | 'graphql'
  | 'rest'
  | 'auth'
  | 'payments'
  | 'digital_assets'
  | 'customer_access'
export type ApiSurfaceKind = 'graphql' | 'rest' | 'auth' | 'internal_api'
export type ApiSecuritySeverity = 'low' | 'medium' | 'high' | 'critical'
export type ApiSecurityDecision =
  | 'allow'
  | 'block'
  | 'review_required'
  | 'step_up_required'
  | 'audit_only'
export type ApiSecurityEventStatus =
  | 'new'
  | 'blocked'
  | 'under_review'
  | 'escalated'
  | 'closed'
export type ApiSecuritySurfaceStatus =
  | 'monitored'
  | 'restricted'
  | 'hardened'
  | 'review_required'
export type ApiSensitiveOperationCategory =
  | 'pin'
  | 'transfer'
  | 'recovery'
  | 'token'
  | 'beneficiary'
  | 'account_lookup'
  | 'wallet_withdrawal'
  | 'staff_access'

export type ApiSecurityControl = {
  control_id: string
  title: string
  category: ApiSecurityControlCategory
  description: string
  protected_operations: string[]
  decision_model: string
  evidence_outputs: string[]
  enabled: boolean
}

export type ApiSecurityEvent = {
  event_id: string
  title: string
  api_surface: ApiSecuritySurfaceType
  operation_name: string
  risk_type: string
  severity: ApiSecuritySeverity
  decision: ApiSecurityDecision
  status: ApiSecurityEventStatus
  triggered_controls: string[]
  affected_object?: string | null
  business_action: string
  summary: string
  recommended_action: string
  audit_event: string
  created_at: string
}

export type ApiSecuritySurface = {
  surface_id: string
  name: string
  surface_type: ApiSurfaceKind
  risk_summary: string
  sensitive_operations: string[]
  controls_applied: string[]
  status: ApiSecuritySurfaceStatus
}

export type ApiSensitiveOperation = {
  operation_id: string
  name: string
  category: ApiSensitiveOperationCategory
  risk_level: ApiSecuritySeverity
  required_controls: string[]
  audit_required: boolean
  step_up_required: boolean
  batching_allowed: boolean
}

export type ApiSecurityScenario = {
  scenario_id: string
  title: string
  description: string
  risk_indicators: string[]
  expected_decision: ApiSecurityDecision
  recommended_controls: string[]
}

export type EvaluateApiSecurityScenarioRequest = {
  scenario_id: string
  operation_name: string
  attempts: number
  object_authorized: boolean
  batching_detected: boolean
  sensitive_fields_requested: boolean
}

export type EvaluateApiSecurityScenarioResponse = {
  risk_score: number
  severity: ApiSecuritySeverity
  decision: ApiSecurityDecision
  triggered_controls: string[]
  audit_event_required: boolean
  recommended_action: string
  explanation: string
}

export function getApiSecurityControls(): Promise<ApiSecurityControl[]> {
  return getJson<ApiSecurityControl[]>('/api-security/controls')
}

export function getApiSecurityEvents(): Promise<ApiSecurityEvent[]> {
  return getJson<ApiSecurityEvent[]>('/api-security/events')
}

export function getApiSecuritySurfaces(): Promise<ApiSecuritySurface[]> {
  return getJson<ApiSecuritySurface[]>('/api-security/surfaces')
}

export function getApiSensitiveOperations(): Promise<ApiSensitiveOperation[]> {
  return getJson<ApiSensitiveOperation[]>('/api-security/sensitive-operations')
}

export function getApiSecurityScenarios(): Promise<ApiSecurityScenario[]> {
  return getJson<ApiSecurityScenario[]>('/api-security/scenarios')
}

export function evaluateApiSecurityScenario(
  payload: EvaluateApiSecurityScenarioRequest,
): Promise<EvaluateApiSecurityScenarioResponse> {
  return postJson<
    EvaluateApiSecurityScenarioResponse,
    EvaluateApiSecurityScenarioRequest
  >('/api-security/evaluate-scenario', payload)
}
