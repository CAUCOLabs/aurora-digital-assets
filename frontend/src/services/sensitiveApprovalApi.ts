import { getJson, postJson } from './apiClient'

export type SensitiveActorType = 'customer' | 'staff' | 'reviewer' | 'admin'
export type SensitivityLevel = 'low' | 'medium' | 'high' | 'critical'
export type StepUpMethod =
  | 'mobile_approval_simulated'
  | 'strong_reauthentication_simulated'
  | 'dual_control_simulated'
  | 'not_required'
export type MobileApprovalStatus = 'pending' | 'approved' | 'rejected' | 'expired'
export type BackendRiskDecision =
  | 'approved'
  | 'pending_review'
  | 'blocked'
  | 'step_up_required'

export type SensitiveOperation = {
  operation_id: string
  operation_type: string
  title: string
  description: string
  actor_type: SensitiveActorType
  sensitivity_level: SensitivityLevel
  approval_required: boolean
  step_up_method: StepUpMethod
  risk_triggers: string[]
  possible_outcomes: string[]
}

export type SensitiveApprovalRequest = {
  operation_type: string
  actor_id: string
  actor_type: SensitiveActorType
  amount_eur?: number | null
  asset?: string | null
  destination_type?: string | null
  destination_id?: string | null
  is_new_destination?: boolean
  customer_confirmed?: boolean
  mobile_approval_status?: MobileApprovalStatus
  device_trusted?: boolean
  session_age_minutes?: number
  risk_context?: Record<string, unknown>
}

export type SensitiveApprovalResponse = {
  operation_id: string
  operation_type: string
  actor_id: string
  actor_type: SensitiveActorType
  approval_required: boolean
  step_up_method: StepUpMethod
  mobile_approval_status: MobileApprovalStatus
  backend_risk_decision: BackendRiskDecision
  risk_level: SensitivityLevel
  risk_score: number
  reasons: string[]
  user_message: string
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  evidence_package_ready: boolean
  review_case_required: boolean
  review_case_id?: string | null
  recommended_next_action: string
  created_at: string
}

export type SensitiveApprovalScenario = {
  scenario_id: string
  title: string
  description: string
  operation_type: string
  sample_payload: SensitiveApprovalRequest
  expected_decision: BackendRiskDecision
}

export function getSensitiveApprovalOperations(): Promise<SensitiveOperation[]> {
  return getJson<SensitiveOperation[]>('/sensitive-approval/operations')
}

export function getSensitiveApprovalScenarios(): Promise<
  SensitiveApprovalScenario[]
> {
  return getJson<SensitiveApprovalScenario[]>('/sensitive-approval/scenarios')
}

export function evaluateSensitiveApproval(
  payload: SensitiveApprovalRequest,
): Promise<SensitiveApprovalResponse> {
  return postJson<SensitiveApprovalResponse, SensitiveApprovalRequest>(
    '/sensitive-approval/evaluate',
    payload,
  )
}
