import { getJson, postJson } from './apiClient'

export type DemoStatusResponse = {
  audit_events_count: number
  review_cases_count: number
  pending_cases_count: number
  approved_cases_count: number
  rejected_cases_count: number
  database: string
  message: string
}

export type DemoResetResponse = {
  status: string
  deleted_audit_events: number
  deleted_review_cases: number
  message: string
}

export type DemoSeedResponse = {
  status: string
  created_audit_events: number
  created_review_cases: number
  message: string
}

export function getDemoStatus(): Promise<DemoStatusResponse> {
  return getJson<DemoStatusResponse>('/admin/demo/status')
}

export function resetDemoData(): Promise<DemoResetResponse> {
  return postJson<DemoResetResponse, undefined>('/admin/demo/reset', undefined)
}

export function seedDemoData(): Promise<DemoSeedResponse> {
  return postJson<DemoSeedResponse, undefined>('/admin/demo/seed', undefined)
}
