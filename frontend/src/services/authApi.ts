import { getJson, postJson } from './apiClient'

export type AuthCustomerInfo = {
  customer_id: string
  customer_name: string
  account_id: string
  relationship_status: string
}

export type BankLoginRequest = {
  bank_user_id: string
  pin: string
}

export type BankLoginResponse = {
  status: string
  challenge_id: string | null
  customer: AuthCustomerInfo | null
  message: string
}

export type MobileApprovalRequest = {
  challenge_id: string
  approved: boolean
}

export type MobileApprovalResponse = {
  status: string
  session_id: string | null
  customer: AuthCustomerInfo | null
  redirect_to: string
  message: string
}

export type BankSessionResponse = {
  authenticated: boolean
  customer_id: string | null
  customer_name: string | null
  account_id: string | null
  relationship_status: string | null
}

export type LogoutResponse = {
  status: string
  message: string
}

export function loginToBank(
  payload: BankLoginRequest,
): Promise<BankLoginResponse> {
  return postJson<BankLoginResponse, BankLoginRequest>('/auth/login', payload)
}

export function approveMobileLogin(
  payload: MobileApprovalRequest,
): Promise<MobileApprovalResponse> {
  return postJson<MobileApprovalResponse, MobileApprovalRequest>(
    '/auth/mobile-approval',
    payload,
  )
}

export function getSession(sessionId: string): Promise<BankSessionResponse> {
  return getJson<BankSessionResponse>(
    `/auth/session?session_id=${encodeURIComponent(sessionId)}`,
  )
}

export function logoutFromBank(sessionId: string): Promise<LogoutResponse> {
  return postJson<LogoutResponse, { session_id: string }>('/auth/logout', {
    session_id: sessionId,
  })
}
