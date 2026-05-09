import { postJson } from './apiClient'

export type DigitalAssetPaymentEvaluateRequest = {
  recipient_name: string
  invoice_number: string
  reference_number: string
  amount_eur: number
  payment_asset: string
  source_account_id: string
}

export type DigitalAssetPaymentEstimate = {
  invoice_amount_eur: number
  payment_asset: string
  estimated_asset_amount: number
  conversion_rate_eur: number
  service_fee_eur: number
  settlement_fee_eur: number
  total_estimated_cost_eur: number
  recipient_settlement: string
}

export type DigitalAssetPaymentEvaluateResponse = {
  decision: string
  risk_level: string
  reasons: string[]
  case_required: boolean
  case_type: string | null
  case_id?: string | null
  user_message: string
  audit_event_type: string
  estimate: DigitalAssetPaymentEstimate | null
}

export function evaluateDigitalAssetPayment(
  payload: DigitalAssetPaymentEvaluateRequest,
): Promise<DigitalAssetPaymentEvaluateResponse> {
  return postJson<
    DigitalAssetPaymentEvaluateResponse,
    DigitalAssetPaymentEvaluateRequest
  >('/payments/digital-assets/evaluate', payload)
}
