import { getJson, postJson } from './apiClient'

export type ReportSummary = {
  report_id: string
  report_type: string
  title: string
  description: string
  status: string
  generated_from: string
  item_count: number
}

export type TaxSummary = {
  year: number
  total_purchases_eur: number
  total_sales_eur: number
  digital_asset_payments_eur: number
  external_transfers_count: number
  pending_review_cases: number
  estimated_realized_gain_loss_eur: number
  disclaimer: string
}

export type EvidencePackageRequest = {
  case_id?: string | null
  year?: number | null
}

export type EvidencePackageResponse = {
  package_id: string
  status: string
  included_audit_events: number
  included_review_cases: number
  message: string
}

export function listReports(): Promise<ReportSummary[]> {
  return getJson<ReportSummary[]>('/reports')
}

export function getTaxSummary(year: number): Promise<TaxSummary> {
  return getJson<TaxSummary>(`/reports/tax-summary/${year}`)
}

export function createEvidencePackage(
  payload: EvidencePackageRequest,
): Promise<EvidencePackageResponse> {
  return postJson<EvidencePackageResponse, EvidencePackageRequest>(
    '/reports/evidence-package',
    payload,
  )
}
