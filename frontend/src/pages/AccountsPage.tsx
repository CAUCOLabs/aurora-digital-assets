import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import {
  connectedDigitalAssetBalances as fallbackConnectedDigitalAssetBalances,
  primaryBankAccount,
  recentBankTransactions as fallbackRecentBankTransactions,
} from '../data/bankAccounts'
import {
  listAccountTransactions,
  listAccounts,
  listConnectedDigitalAssetBalances,
  type BankAccount,
  type BankTransaction,
  type ConnectedDigitalAssetBalance,
} from '../services/accountsApi'

const openAccountOptions = [
  'Current account',
  'Savings and deposit account',
  'Account for a child',
  'Add new account',
]

const documentOptions = [
  'Account statements',
  'Bank mail',
  'Payment receipts',
  'Digital asset reports',
]

export function AccountsPage() {
  const [bankAccounts, setBankAccounts] = useState<BankAccount[]>([
    primaryBankAccount,
  ])
  const [transactions, setTransactions] = useState<BankTransaction[]>(
    fallbackRecentBankTransactions,
  )
  const [connectedAssets, setConnectedAssets] = useState<
    ConnectedDigitalAssetBalance[]
  >(fallbackConnectedDigitalAssetBalances)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  const bankAccount = bankAccounts[0] ?? primaryBankAccount

  useEffect(() => {
    async function fetchAccountsData() {
      setIsLoading(true)

      try {
        const accounts = await listAccounts()
        const selectedAccount = accounts[0] ?? primaryBankAccount

        const [accountTransactions, digitalAssetBalances] = await Promise.all([
          listAccountTransactions(selectedAccount.id),
          listConnectedDigitalAssetBalances(),
        ])

        setBankAccounts(accounts.length > 0 ? accounts : [primaryBankAccount])
        setTransactions(
          accountTransactions.length > 0
            ? accountTransactions
            : fallbackRecentBankTransactions,
        )
        setConnectedAssets(
          digitalAssetBalances.length > 0
            ? digitalAssetBalances
            : fallbackConnectedDigitalAssetBalances,
        )
        setBackendError(null)
      } catch {
        setBankAccounts([primaryBankAccount])
        setTransactions(fallbackRecentBankTransactions)
        setConnectedAssets(fallbackConnectedDigitalAssetBalances)
        setBackendError(
          'Backend account data unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchAccountsData()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Accounts</p>
            <h1>Accounts and balances</h1>
            <p>
              View your bank accounts, available balances, account activity, and
              connected digital asset balances.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Strong authentication active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Bank accounts</p>
                  <h2>{bankAccount.name}</h2>
                </div>
                <span className="module-tag">{bankAccount.status}</span>
              </div>

              {isLoading && <p className="panel-note">Loading account data...</p>}
              {backendError && <p className="panel-note">{backendError}</p>}
              {!backendError && !isLoading && (
                <p className="panel-note">
                  Account data loaded from local FastAPI prototype.
                </p>
              )}

              <div className="assets-summary">
                <div>
                  <p>Book balance</p>
                  <strong>{bankAccount.bookBalance}</strong>
                  <span>
                    {bankAccount.type} · Owner: {bankAccount.owner}
                  </span>
                </div>

                <div className="custody-card">
                  <p>Available balance</p>
                  <strong>{bankAccount.availableBalance}</strong>
                  <span>
                    Reserved card payments: {bankAccount.reservedCardPayments}
                  </span>
                </div>
              </div>

              <div className="assets-summary trade-summary">
                <div>
                  <p>IBAN</p>
                  <strong>{bankAccount.iban}</strong>
                  <span>BIC {bankAccount.bic}</span>
                </div>

                <div className="custody-card">
                  <p>Status</p>
                  <strong>{bankAccount.status}</strong>
                  <span>Account information is simulated.</span>
                </div>
              </div>

              <div className="action-row">
                <Link className="button-link" to="/payments">
                  New payment
                </Link>
                <Link className="button-link secondary-button" to="/accounts">
                  View transactions
                </Link>
                <Link className="button-link secondary-button" to="/accounts">
                  Account details
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Statements
                </Link>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Recent account transactions</p>
                  <h2>Account activity</h2>
                </div>
                <span className="module-tag">
                  {backendError ? 'Fallback data' : 'Backend data'}
                </span>
              </div>

              <div className="account-list">
                {transactions.map((transaction) => (
                  <article className="account-row" key={transaction.id}>
                    <div>
                      <h3>{transaction.title}</h3>
                      <p>
                        {transaction.accountName} · {transaction.detail}
                      </p>
                      <span>{transaction.status}</span>
                    </div>
                    <strong>{transaction.amount}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Connected digital asset balances</p>
                  <h2>Connected digital asset balances</h2>
                </div>
                <span className="module-tag">Separate from deposits</span>
              </div>

              <p>
                These balances are linked to the online banking experience for
                this prototype, but they are not bank deposits.
              </p>

              <div className="account-list">
                {connectedAssets.map((asset) => (
                  <article className="account-row" key={asset.id}>
                    <div>
                      <h3>{asset.name}</h3>
                      <p>{asset.balance}</p>
                      <span>{asset.detail}</span>
                    </div>
                    <strong>{asset.value}</strong>
                  </article>
                ))}
              </div>

              <div className="action-row">
                <Link className="button-link" to="/digital-assets">
                  View Digital Assets
                </Link>
                <Link className="button-link secondary-button" to="/wallet">
                  View Wallet
                </Link>
                <Link className="button-link secondary-button" to="/custody">
                  Custody Model
                </Link>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Open account</p>
              <h2>Account options</h2>

              <div className="check-list">
                {openAccountOptions.map((option) => (
                  <div key={option}>
                    <span className="status-dot"></span>
                    {option}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Statements and documents</p>
              <h2>Documents</h2>

              <div className="check-list">
                {documentOptions.map((option) => (
                  <div key={option}>
                    <span className="status-dot"></span>
                    {option}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Protection status</p>
              <h2>Controls active</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Strong authentication active
                </div>
                <div>
                  <span className="status-dot"></span>
                  Transaction monitoring enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  Account alerts active
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Digital assets are separate from deposits
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Account note</p>
              <h2>Digital asset boundary</h2>
              <p>
                Connected digital asset balances are shown for prototype
                purposes only. They are separate from bank deposits and do not
                have the same protections as traditional bank accounts.
              </p>
              <p>
                Account information and balances are simulated. No real
                financial data is used.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real bank accounts, no real crypto
          assets, no real customer data, and no real financial transactions are
          used.
        </section>
      </main>
    </div>
  )
}