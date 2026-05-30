import { getJson, postJson } from './apiClient'

export type LookupType = 'customer_id' | 'bank_user_id' | 'passport_or_id'
export type AuthorizationMethod = 'mobile_approval' | 'private_branch_entry'

export type StaffCustomerLookupRequest = {
  lookup_value: string
  lookup_type: LookupType
}

export type StaffCustomerLookupResponse = {
  status: string
  customer_id?: string | null
  customer_name?: string | null
  relationship_status?: string | null
  access_state: 'locked' | 'unlocked' | 'unavailable'
  user_message: string
}

export type StaffCustomerAuthorizationRequest = {
  customer_id: string
  method: AuthorizationMethod
}

export type StaffCustomerAuthorizationResponse = {
  status: string
  request_id?: string | null
  method?: AuthorizationMethod | null
  customer_id?: string | null
  access_state: 'locked' | 'unlocked' | 'unavailable'
  user_message: string
}

export type StaffCustomerAccessApprovalRequest = {
  request_id: string
  approved: boolean
}

export type StaffCustomerRecordDetails = {
  customer_id: string
  bank_user_id: string
  name: string
  account_id: string
  relationship_status: string
  identity_verification_status: string
  source_of_funds_status: string
  online_banking_enabled: boolean
  strong_authentication_enabled: boolean
  digital_assets_eligible: boolean
}

export type StaffCustomerAccessApprovalResponse = {
  status: string
  access_state: 'locked' | 'unlocked' | 'unavailable'
  customer_record?: StaffCustomerRecordDetails | null
  access_expires_in_minutes?: number | null
  user_message: string
}

export type StaffCustomerAccessStatusResponse = {
  status: string
  access_state: 'locked' | 'unlocked' | 'unavailable'
  method?: AuthorizationMethod | null
  customer_id?: string | null
  request_id?: string | null
  user_message: string
}

export function lookupStaffCustomer(
  request: StaffCustomerLookupRequest,
): Promise<StaffCustomerLookupResponse> {
  return postJson<StaffCustomerLookupResponse, StaffCustomerLookupRequest>(
    '/bank-staff/customer-access/lookup',
    request,
  )
}

export function requestStaffCustomerAuthorization(
  request: StaffCustomerAuthorizationRequest,
): Promise<StaffCustomerAuthorizationResponse> {
  return postJson<
    StaffCustomerAuthorizationResponse,
    StaffCustomerAuthorizationRequest
  >('/bank-staff/customer-access/request-authorization', request)
}

export function approveStaffCustomerAuthorization(
  request: StaffCustomerAccessApprovalRequest,
): Promise<StaffCustomerAccessApprovalResponse> {
  return postJson<
    StaffCustomerAccessApprovalResponse,
    StaffCustomerAccessApprovalRequest
  >('/bank-staff/customer-access/approve', request)
}

export function getStaffCustomerAccessStatus(
  requestId: string,
): Promise<StaffCustomerAccessStatusResponse> {
  return getJson<StaffCustomerAccessStatusResponse>(
    `/bank-staff/customer-access/status/${requestId}`,
  )
}
