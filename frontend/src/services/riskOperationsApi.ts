import { getJson, postJson } from './apiClient'

export type MetricStatus = 'normal' | 'attention' | 'warning' | 'critical'
export type RiskSourceModule =
  | 'financial_crime'
  | 'compliance_intelligence'
  | 'evidence_packages'
  | 'operational_resilience'
  | 'infrastructure_security'
  | 'crypto_agility'
  | 'compliance_review'
  | 'reports'
export type RiskPriority = 'low' | 'medium' | 'high' | 'urgent'
export type RiskActionStatus =
  | 'new'
  | 'in_progress'
  | 'blocked'
  | 'ready'
  | 'escalated'
  | 'closed'
export type TimelineSeverity = 'low' | 'medium' | 'high' | 'critical'
export type EscalationType =
  | 'financial_crime'
  | 'operational_resilience'
  | 'infrastructure_security'
  | 'crypto_agility'
  | 'evidence_gap'
  | 'compliance_review'
export type OperatingMode =
  | 'normal'
  | 'elevated_monitoring'
  | 'restricted_operations'
  | 'incident_command'

export type RiskOperationsLink = {
  label: string
  route: string
  entity_id?: string | null
}

export type RiskOperationsMetric = {
  metric_id: string
  label: string
  value: string
  status: MetricStatus
  description: string
  source_module: RiskSourceModule
}

export type RiskActionItem = {
  action_id: string
  title: string
  source_module: RiskSourceModule
  source_id: string
  priority: RiskPriority
  status: RiskActionStatus
  risk_type: string
  summary: string
  required_action: string
  missing_evidence: string[]
  related_links: RiskOperationsLink[]
  created_at: string
}

export type UnifiedTimelineEvent = {
  event_id: string
  timestamp: string
  source_module: RiskSourceModule
  event_type: string
  severity: TimelineSeverity
  title: string
  description: string
  related_entity_id: string
  recommended_action: string
}

export type EscalationSummary = {
  summary_id: string
  title: string
  severity: TimelineSeverity
  escalation_type: EscalationType
  open_items: number
  blocked_items: number
  ready_items: number
  summary: string
  recommended_action: string
}

export type RiskOperationsOverview = {
  generated_at: string
  metrics: RiskOperationsMetric[]
  highest_priority: RiskPriority
  operating_mode: OperatingMode
  summary: string
  recommended_focus: string[]
}

export type RiskOperationsReviewCaseRequest = {
  action_id: string
  reviewer_id: string
  priority: RiskPriority
}

export type RiskOperationsReviewCaseResponse = {
  status: string
  review_case_id: string
  source_action_id: string
  case_title: string
  case_summary: string
  recommended_next_action: string
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  user_message: string
  required_action: string
  missing_evidence: string[]
}

export function getRiskOperationsOverview(): Promise<RiskOperationsOverview> {
  return getJson<RiskOperationsOverview>('/risk-operations/overview')
}

export function getRiskOperationsActionQueue(): Promise<RiskActionItem[]> {
  return getJson<RiskActionItem[]>('/risk-operations/action-queue')
}

export function getRiskOperationsUnifiedTimeline(): Promise<
  UnifiedTimelineEvent[]
> {
  return getJson<UnifiedTimelineEvent[]>('/risk-operations/unified-timeline')
}

export function getRiskOperationsEscalationSummary(): Promise<
  EscalationSummary[]
> {
  return getJson<EscalationSummary[]>('/risk-operations/escalation-summary')
}

export function createRiskOperationsReviewCase(
  payload: RiskOperationsReviewCaseRequest,
): Promise<RiskOperationsReviewCaseResponse> {
  return postJson<
    RiskOperationsReviewCaseResponse,
    RiskOperationsReviewCaseRequest
  >('/risk-operations/create-review-case', payload)
}
