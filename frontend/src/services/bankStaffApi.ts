import { getJson } from './apiClient'

export type OnboardingStep = {
  step_id: string
  title: string
  description: string
  performed_by: string
  status: string
  evidence_required: string[]
}

export type BankStaffOnboardingModelResponse = {
  title: string
  description: string
  onboarding_steps: OnboardingStep[]
  credential_model: string[]
  strong_authentication_model: string[]
  digital_assets_eligibility_model: string[]
  boundary_note: string
}

export type BankCustomerRecordResponse = {
  customer_id: string
  bank_user_id: string
  name: string
  relationship_status: string
  identity_verification_status: string
  residency_status: string
  source_of_funds_status: string
  account_id: string
  online_banking_enabled: boolean
  strong_authentication_enabled: boolean
  digital_assets_eligible: boolean
  staff_review_status: string
  notes: string[]
}

export function getBankStaffOnboardingModel(): Promise<BankStaffOnboardingModelResponse> {
  return getJson<BankStaffOnboardingModelResponse>(
    '/bank-staff/onboarding-model',
  )
}

export function getBankStaffCustomerRecord(): Promise<BankCustomerRecordResponse> {
  return getJson<BankCustomerRecordResponse>('/bank-staff/customer-record')
}
