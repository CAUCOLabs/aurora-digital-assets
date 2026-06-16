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
