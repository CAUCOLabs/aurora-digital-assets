export type BankAccount = {
  id: string
  name: string
  owner: string
  type: string
  iban: string
  bic: string
  bookBalance: string
  availableBalance: string
  reservedCardPayments: string
  status: string
}

export type BankTransaction = {
  id: string
  title: string
  detail: string
  accountName: string
  amount: string
  status: string
}

export type ConnectedDigitalAssetBalance = {
  id: string
  name: string
  balance: string
  detail: string
  value: string
}
