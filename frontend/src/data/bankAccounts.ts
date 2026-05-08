import type {
  BankAccount,
  BankTransaction,
  ConnectedDigitalAssetBalance,
} from '../types/banking'

export const primaryBankAccount: BankAccount = {
  id: 'aurora-current',
  name: 'Aurora Current Account',
  owner: 'Claudio Demo',
  type: 'Current account',
  iban: 'FI12 0000 0000 1234 56',
  bic: 'AURAFIHH',
  bookBalance: '2 450,10 €',
  availableBalance: '2 430,10 €',
  reservedCardPayments: '20,00 €',
  status: 'Active',
}

export const recentBankTransactions: BankTransaction[] = [
  {
    id: 'aurora-telecom-invoice',
    title: 'Aurora Telecom Oyj invoice payment',
    detail: 'Reference preserved',
    accountName: 'Aurora Current Account',
    amount: '-120,45 €',
    status: 'Pending',
  },
  {
    id: 'salary-payment',
    title: 'Salary payment',
    detail: 'Salary',
    accountName: 'Aurora Current Account',
    amount: '+2 850,00 €',
    status: 'Completed',
  },
  {
    id: 'grocery-card-payment',
    title: 'Grocery store card payment',
    detail: 'Card purchase',
    accountName: 'Aurora Current Account',
    amount: '-42,80 €',
    status: 'Completed',
  },
  {
    id: 'digital-asset-invoice-payment',
    title: 'Digital asset invoice payment',
    detail: 'Digital asset payment draft',
    accountName: 'Aurora Current Account',
    amount: '0,00 €',
    status: 'Pending confirmation',
  },
]

export const connectedDigitalAssetBalances: ConnectedDigitalAssetBalance[] = [
  {
    id: 'btc-wallet-balance',
    name: 'BTC wallet balance',
    balance: '0.012450 BTC',
    detail: 'Connected digital asset balance',
    value: '865,28 €',
  },
  {
    id: 'eth-wallet-balance',
    name: 'ETH wallet balance',
    balance: '0.184200 ETH',
    detail: 'Connected digital asset balance',
    value: '380,52 €',
  },
  {
    id: 'usdc-payment-asset-balance',
    name: 'USDC payment asset balance',
    balance: '129.80 USDC',
    detail: 'Connected digital asset balance',
    value: 'Payment asset',
  },
  {
    id: 'usdt-payment-asset-balance',
    name: 'USDT payment asset balance',
    balance: '129.60 USDT',
    detail: 'Connected digital asset balance',
    value: 'Payment asset',
  },
  {
    id: 'xrp-cross-border-concept',
    name: 'XRP cross-border concept',
    balance: 'Future support',
    detail: 'Connected digital asset balance',
    value: 'Concept only',
  },
]
