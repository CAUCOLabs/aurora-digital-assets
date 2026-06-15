import { getJson, postJson } from './apiClient'

export type ComplianceSeverity = 'low' | 'medium' | 'high' | 'critical'
export type RecommendedDecision =
  | 'allow'
  | 'review_required'
  | 'escalate'
  | 'block'
export type ReviewPriority = 'low' | 'medium' | 'high' | 'urgent'
export type EvidenceRequirementStatus =
  | 'included'
  | 'missing'
  | 'reviewer_required'

export type RiskExplanation = {
  explanation_id: string
  alert_id: string
  alert_title: string
  risk_type: string
  severity: ComplianceSeverity
  risk_summary: string
  reasoning: string
  triggered_controls: string[]
  supporting_evidence: string[]
  missing_evidence: string[]
  reviewer_questions: string[]
  recommended_decision: RecommendedDecision
  evidence_package_ready: boolean
}

export type ReviewerGuidance = {
  guidance_id: string
  title: string
  category: string
  description: string
  checklist: string[]
  reviewer_action: string
}

export type EvidenceRequirement = {
  requirement_id: string
  title: string
  category: string
  description: string
  status: EvidenceRequirementStatus
  required: boolean
}

export type DecisionPathStep = {
  step_number: number
  title: string
  description: string
}

export type ExplainAlertRequest = {
  alert_id: string
  include_evidence_requirements: boolean
}

export type ExplainAlertResponse = {
  alert_id: string
  explanation: RiskExplanation
  decision_path: DecisionPathStep[]
  evidence_requirements: EvidenceRequirement[]
  reviewer_next_steps: string[]
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
}

export type PrepareReviewCaseRequest = {
  alert_id: string
  reviewer_id?: string | null
  priority: ReviewPriority
}

export type PrepareReviewCaseResponse = {
  case_preview_id: string
  alert_id: string
  priority: ReviewPriority
  case_title: string
  case_summary: string
  included_evidence: string[]
  required_evidence: string[]
  recommended_assignment: string
  ready_for_review: boolean
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
}

export function getRiskExplanations(): Promise<RiskExplanation[]> {
  return getJson<RiskExplanation[]>('/compliance-intelligence/risk-explanations')
}

export function getReviewerGuidance(): Promise<ReviewerGuidance[]> {
  return getJson<ReviewerGuidance[]>('/compliance-intelligence/reviewer-guidance')
}

export function explainAlert(
  payload: ExplainAlertRequest,
): Promise<ExplainAlertResponse> {
  return postJson<ExplainAlertResponse, ExplainAlertRequest>(
    '/compliance-intelligence/explain-alert',
    payload,
  )
}

export function prepareReviewCase(
  payload: PrepareReviewCaseRequest,
): Promise<PrepareReviewCaseResponse> {
  return postJson<PrepareReviewCaseResponse, PrepareReviewCaseRequest>(
    '/compliance-intelligence/prepare-review-case',
    payload,
  )
}
