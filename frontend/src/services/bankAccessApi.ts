import { getJson } from './apiClient'

export type BankSessionModelResponse = {
  title: string
  description: string
  customer_access_steps: string[]
  authentication_controls: string[]
  session_controls: string[]
  boundary_note: string
}

export type IntegrationLayer = {
  name: string
  responsibility: string
  examples: string[]
}

export type BankIntegrationModelResponse = {
  title: string
  description: string
  integration_layers: IntegrationLayer[]
  payment_rails_note: string
  digital_assets_module_note: string
  boundary_note: string
}

export function getBankSessionModel(): Promise<BankSessionModelResponse> {
  return getJson<BankSessionModelResponse>('/bank-access/session-model')
}

export function getBankIntegrationModel(): Promise<BankIntegrationModelResponse> {
  return getJson<BankIntegrationModelResponse>('/bank-access/integration-model')
}
