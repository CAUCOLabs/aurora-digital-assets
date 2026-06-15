import { getJson, postJson } from './apiClient'

export type ServiceCategory =
  | 'payments'
  | 'authentication'
  | 'digital_assets'
  | 'core_banking'
  | 'reporting'
  | 'staff_operations'
  | 'external_dependency'
export type ServiceStatus =
  | 'healthy'
  | 'degraded'
  | 'outage'
  | 'maintenance'
  | 'paused'
export type CustomerImpact = 'none' | 'low' | 'medium' | 'high' | 'severe'
export type CurrentMode =
  | 'normal'
  | 'degraded'
  | 'read_only'
  | 'paused'
  | 'fallback'
export type DependencyType =
  | 'internal'
  | 'external'
  | 'network'
  | 'authentication'
  | 'payment_rail'
  | 'custody'
  | 'reporting'
export type DependencyHealth = 'healthy' | 'degraded' | 'outage' | 'unknown'
export type FallbackStatus =
  | 'available'
  | 'active'
  | 'unavailable'
  | 'testing'
export type IncidentSeverity = 'low' | 'medium' | 'high' | 'critical'
export type IncidentStatus = 'open' | 'investigating' | 'mitigated' | 'resolved'
export type FailureType =
  | 'service_degradation'
  | 'outage'
  | 'dependency_failure'
  | 'traffic_spike'
  | 'maintenance_failure'
  | 'fallback_activation'
export type ResilienceDecision =
  | 'normal_operations'
  | 'degraded_mode'
  | 'activate_fallback'
  | 'pause_sensitive_operations'
  | 'escalate_incident'

export type ServiceHealthStatus = {
  service_id: string
  name: string
  category: ServiceCategory
  status: ServiceStatus
  availability_percent: number
  customer_impact: CustomerImpact
  fallback_available: boolean
  current_mode: CurrentMode
  recommended_action: string
}

export type DependencyStatus = {
  dependency_id: string
  name: string
  dependency_type: DependencyType
  status: DependencyHealth
  affected_services: string[]
  risk_summary: string
}

export type FallbackMode = {
  fallback_id: string
  title: string
  status: FallbackStatus
  description: string
  allowed_operations: string[]
  paused_operations: string[]
  activation_reason?: string | null
}

export type ResilienceControl = {
  control_id: string
  title: string
  category: string
  description: string
  activated: boolean
  evidence_outputs: string[]
}

export type IncidentTimelineEvent = {
  event_id: string
  timestamp: string
  event_type: string
  title: string
  description: string
  source_module: string
}

export type ResilienceIncident = {
  incident_id: string
  title: string
  affected_service: string
  severity: IncidentSeverity
  status: IncidentStatus
  failure_type: FailureType
  customer_impact: CustomerImpact
  summary: string
  controls_activated: string[]
  fallback_mode: string
  paused_operations: string[]
  available_operations: string[]
  recommended_action: string
  audit_evidence: string[]
  timeline: IncidentTimelineEvent[]
  created_at: string
}

export type EvaluateResilienceScenarioRequest = {
  scenario_id: string
  affected_service: string
  dependency_status: string
  customer_impact: string
}

export type EvaluateResilienceScenarioResponse = {
  resilience_score: number
  severity: IncidentSeverity
  decision: ResilienceDecision
  controls_activated: string[]
  available_operations: string[]
  paused_operations: string[]
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  recommended_action: string
  explanation: string
}

export function getServiceHealth(): Promise<ServiceHealthStatus[]> {
  return getJson<ServiceHealthStatus[]>('/operational-resilience/service-health')
}

export function getDependencies(): Promise<DependencyStatus[]> {
  return getJson<DependencyStatus[]>('/operational-resilience/dependencies')
}

export function getFallbackModes(): Promise<FallbackMode[]> {
  return getJson<FallbackMode[]>('/operational-resilience/fallback-modes')
}

export function getResilienceControls(): Promise<ResilienceControl[]> {
  return getJson<ResilienceControl[]>('/operational-resilience/controls')
}

export function getResilienceIncidents(): Promise<ResilienceIncident[]> {
  return getJson<ResilienceIncident[]>('/operational-resilience/incidents')
}

export function getResilienceIncident(
  incidentId: string,
): Promise<ResilienceIncident> {
  return getJson<ResilienceIncident>(
    `/operational-resilience/incidents/${incidentId}`,
  )
}

export function evaluateResilienceScenario(
  payload: EvaluateResilienceScenarioRequest,
): Promise<EvaluateResilienceScenarioResponse> {
  return postJson<
    EvaluateResilienceScenarioResponse,
    EvaluateResilienceScenarioRequest
  >('/operational-resilience/evaluate-scenario', payload)
}
