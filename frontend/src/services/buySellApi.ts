import { postJson } from './apiClient'

export type BuySellSide = 'buy' | 'sell'
export type BuySellAsset = 'BTC' | 'ETH'

export type BuySellEvaluateRequest = {
  side: BuySellSide
  asset: BuySellAsset
  amount: number
  source_account_id: string
}

export type BuySellEstimate = {
  side: string
  asset: string
  market_price_eur: number
  gross_eur: number
  fee_eur: number
  spread_eur: number
  net_eur: number
  estimated_asset_amount: number
}

export type BuySellEvaluateResponse = {
  decision: string
  risk_level: string
  reasons: string[]
  case_required: boolean
  case_type: string | null
  case_id?: string | null
  user_message: string
  audit_event_type: string
  estimate: BuySellEstimate | null
}

export function evaluateBuySell(
  payload: BuySellEvaluateRequest,
): Promise<BuySellEvaluateResponse> {
  return postJson<BuySellEvaluateResponse, BuySellEvaluateRequest>(
    '/digital-assets/buy-sell/evaluate',
    payload,
  )
}