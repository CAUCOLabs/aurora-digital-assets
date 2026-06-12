import { getJson, postJson } from './apiClient'

export type FinancialCrimeSeverity = 'low' | 'medium' | 'high' | 'critical'
export type FinancialCrimeAlertStatus =
  | 'new'
  | 'under_review'
  | 'escalated'
  | 'closed'
export type FinancialCrimeEntityType =
  | 'employee'
  | 'customer'
  | 'company'
  | 'account'
  | 'transaction'
  | 'wallet'
export type EvaluationDecision = 'allow' | 'review_required' | 'escalate'

export type RiskScenario = {
  scenario_id: string
  title: string
  description: string
  risk_indicators: string[]
}

export type MonitoringControl = {
  control_id: string
  title: string
  category: string
  description: string
  evidence_outputs: string[]
}

export type FinancialCrimeAlert = {
  alert_id: string
  title: string
  risk_type: string
  severity: FinancialCrimeSeverity
  entity_type: FinancialCrimeEntityType
  entity_name: string
  amount_eur: number
  status: FinancialCrimeAlertStatus
  triggered_rules: string[]
  recommended_action: string
  linked_review_case_id?: string | null
  evidence_summary: string
  created_at: string
}

export type EvaluateDemoActivityRequest = {
  scenario_id: string
  amount_eur: number
  entity_type: string
}

export type EvaluateDemoActivityResponse = {
  risk_score: number
  severity: FinancialCrimeSeverity
  decision: EvaluationDecision
  triggered_rules: string[]
  recommended_action: string
  explanation: string
}

export function getRiskScenarios(): Promise<RiskScenario[]> {
  return getJson<RiskScenario[]>('/financial-crime/risk-scenarios')
}

export function getMonitoringControls(): Promise<MonitoringControl[]> {
  return getJson<MonitoringControl[]>('/financial-crime/monitoring-controls')
}

export function getDemoAlerts(): Promise<FinancialCrimeAlert[]> {
  return getJson<FinancialCrimeAlert[]>('/financial-crime/demo-alerts')
}

export function evaluateDemoActivity(
  payload: EvaluateDemoActivityRequest,
): Promise<EvaluateDemoActivityResponse> {
  return postJson<EvaluateDemoActivityResponse, EvaluateDemoActivityRequest>(
    '/financial-crime/evaluate-demo-activity',
    payload,
  )
}
