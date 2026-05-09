import { postJson } from './apiClient'

export type WithdrawalEvaluateRequest = {
  asset: string
  network: string
  amount: number
  destination_address: string
  confirm_destination_address: string
  wallet_type: string
}

export type RiskDecisionResponse = {
  decision: string
  risk_level: string
  reasons: string[]
  case_required: boolean
  case_type: string | null
  case_id?: string | null
  user_message: string
  audit_event_type: string
}

export function evaluateWithdrawal(
  payload: WithdrawalEvaluateRequest,
): Promise<RiskDecisionResponse> {
  return postJson<RiskDecisionResponse, WithdrawalEvaluateRequest>(
    '/withdrawals/evaluate',
    payload,
  )
}
