import { getJson, postJson } from './apiClient'

export type ReviewCase = {
  case_id: string
  created_at: string
  case_type: string
  title: string
  status: string
  risk_level: string
  reasons: string[]
  customer: string
  action_type: string
  asset: string
  amount: number
  network: string
  destination_address: string
  wallet_type: string
  reviewer_decision: string | null
  reviewer_notes: string | null
  persisted?: boolean
  source_module?: string | null
  source_id?: string | null
  source_action_id?: string | null
  reviewer_id?: string | null
  recommended_next_action?: string | null
  audit_event_id?: string | null
  correlation_id?: string | null
  metadata?: Record<string, unknown>
}

export type AuditEvent = {
  event_id: string
  timestamp: string
  module: string
  action_type: string
  status: string
  risk_level: string | null
  decision: string | null
  reasons: string[]
  case_id: string | null
  user_message: string | null
}

export type ReviewerDecisionRequest = {
  decision: string
  notes: string
}

export type ReviewCaseLifecycleStatus =
  | 'open'
  | 'under_review'
  | 'action_required'
  | 'mitigation_in_progress'
  | 'mitigated'
  | 'closed'

export type ReviewCaseActionType =
  | 'reviewer_note'
  | 'evidence_reviewed'
  | 'mitigation_requested'
  | 'mitigation_started'
  | 'mitigation_verified'
  | 'risk_accepted'
  | 'case_closed'

export type ReviewCaseLifecycleTransitionRequest = {
  case_id?: string | null
  target_status: ReviewCaseLifecycleStatus
  reviewer_id: string
  decision_note: string
  mitigation_action?: string | null
  evidence_package_id?: string | null
  risk_acceptance?: boolean
}

export type ReviewCaseLifecycleTransitionResponse = {
  case_id: string
  previous_status: string
  new_status: string
  transition_allowed: boolean
  lifecycle_stage: string
  reviewer_id: string
  decision_note: string
  mitigation_action?: string | null
  linked_evidence_package?: string | null
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  recommended_next_status?: string | null
  created_at: string
}

export type ReviewCaseActionRequest = {
  action_type: ReviewCaseActionType
  actor_id: string
  note: string
}

export type ReviewCaseAction = {
  action_id: string
  case_id: string
  action_type: ReviewCaseActionType
  actor_id: string
  note: string
  created_at: string
  audit_event_id?: string | null
}

export type ReviewCaseCloseRequest = {
  reviewer_id: string
  decision_note: string
  final_decision: string
  evidence_package_id?: string | null
  risk_acceptance?: boolean
}

export type ReviewCaseLifecycleSummary = {
  case_id: string
  current_status: string
  allowed_next_statuses: string[]
  lifecycle_progress_percent: number
  actions: ReviewCaseAction[]
  linked_evidence_packages: string[]
  linked_audit_events: string[]
  final_decision?: string | null
  closure_ready: boolean
}

export function listReviewCases(): Promise<ReviewCase[]> {
  return getJson<ReviewCase[]>('/review-cases')
}

export function listAuditEvents(): Promise<AuditEvent[]> {
  return getJson<AuditEvent[]>('/audit-events')
}

export function recordReviewerDecision(
  caseId: string,
  payload: ReviewerDecisionRequest,
): Promise<ReviewCase> {
  return postJson<ReviewCase, ReviewerDecisionRequest>(
    `/review-cases/${caseId}/decision`,
    payload,
  )
}

export function getReviewCaseLifecycle(
  caseId: string,
): Promise<ReviewCaseLifecycleSummary> {
  return getJson<ReviewCaseLifecycleSummary>(
    `/review-cases/${caseId}/lifecycle`,
  )
}

export function transitionReviewCase(
  caseId: string,
  payload: ReviewCaseLifecycleTransitionRequest,
): Promise<ReviewCaseLifecycleTransitionResponse> {
  return postJson<
    ReviewCaseLifecycleTransitionResponse,
    ReviewCaseLifecycleTransitionRequest
  >(`/review-cases/${caseId}/transition`, payload)
}

export function addReviewCaseAction(
  caseId: string,
  payload: ReviewCaseActionRequest,
): Promise<ReviewCaseAction> {
  return postJson<ReviewCaseAction, ReviewCaseActionRequest>(
    `/review-cases/${caseId}/actions`,
    payload,
  )
}

export function closeReviewCase(
  caseId: string,
  payload: ReviewCaseCloseRequest,
): Promise<ReviewCaseLifecycleTransitionResponse> {
  return postJson<
    ReviewCaseLifecycleTransitionResponse,
    ReviewCaseCloseRequest
  >(`/review-cases/${caseId}/close`, payload)
}
