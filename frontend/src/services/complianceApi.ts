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
