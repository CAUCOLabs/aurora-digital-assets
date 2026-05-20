import { getJson } from './apiClient'

export type SupportedDigitalAsset = {
  symbol: string
  name: string
  category: string
  supported_actions: string[]
  status: string
  risk_note: string
}

export type WalletBalance = {
  id: string
  symbol: string
  name: string
  balance: string
  estimatedValue: string
  custodyMode: string
  status: string
}

export type DigitalAssetActivity = {
  id: string
  title: string
  detail: string
  status: string
  amount: string
  module: string
}

export type CustodyStatus = {
  custodyMode: string
  privateKeysExposed: boolean
  assetsSeparateFromDeposits: boolean
  auditTrailEnabled: boolean
  externalWithdrawalsRequireReview: boolean
  userMessage: string
  controls: string[]
}

export function listSupportedDigitalAssets(): Promise<SupportedDigitalAsset[]> {
  return getJson<SupportedDigitalAsset[]>('/digital-assets/assets')
}

export function listWalletBalances(): Promise<WalletBalance[]> {
  return getJson<WalletBalance[]>('/digital-assets/wallet')
}

export function listDigitalAssetActivity(): Promise<DigitalAssetActivity[]> {
  return getJson<DigitalAssetActivity[]>('/digital-assets/activity')
}

export function getCustodyStatus(): Promise<CustodyStatus> {
  return getJson<CustodyStatus>('/custody/status')
}
