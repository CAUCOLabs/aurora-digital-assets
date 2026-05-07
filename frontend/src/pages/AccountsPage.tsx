import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const bankAccount = {
  name: 'Aurora Current Account',
  type: 'Current account',
  iban: 'FI12 0000 0000 1234 56',
  balance: '2 450,10 €',
  availableBalance: '2 430,10 €',
  status: 'Active',
}

const recentTransactions = [
  {
    title: 'Aurora Telecom Oyj invoice payment',
    amount: '-120,45 €',
    status: 'Pending',
  },
  {
    title: 'Salary payment',
    amount: '+2 850,00 €',
    status: 'Completed',
  },
  {
    title: 'Grocery store card payment',
    amount: '-42,80 €',
    status: 'Completed',
  },
  {
    title: 'Digital asset payment estimate',
    amount: '0,00 €',
    status: 'Draft',
  },
]

const digitalAssetBalances = [
  {
    name: 'BTC wallet',
    balance: '0.012450 BTC',
    detail: '865,28 €',
  },
  {
    name: 'ETH wallet',
    balance: '0.184200 ETH',
    detail: '380,52 €',
  },
  {
    name: 'USDC payment balance',
    balance: '129.80 USDC',
    detail: 'Payment asset',
  },
  {
    name: 'USDT payment balance',
    balance: '129.60 USDT',
    detail: 'Payment asset',
  },
  {
    name: 'XRP cross-border concept',
    balance: 'Future support',
    detail: 'Concept only',
  },
]

const openAccountOptions = [
  'Current account',
  'Savings and deposit account',
  'Account for a child',
  'Add new account',
]

const documentOptions = [
  'Account statements',
  'Bank mail',
  'Digital asset reports',
  'Payment receipts',
]

export function AccountsPage() {
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

              <div className="assets-summary">
                <div>
                  <p>{bankAccount.type}</p>
                  <strong>{bankAccount.balance}</strong>
                  <span>IBAN {bankAccount.iban}</span>
                </div>

                <div className="custody-card">
                  <p>Available balance</p>
                  <strong>{bankAccount.availableBalance}</strong>
                  <span>Status: {bankAccount.status}</span>
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
                  Open account
                </Link>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Recent account transactions</p>
                  <h2>Account activity</h2>
                </div>
              </div>

              <div className="account-list">
                {recentTransactions.map((transaction) => (
                  <article className="account-row" key={transaction.title}>
                    <div>
                      <h3>{transaction.title}</h3>
                      <p>{transaction.status}</p>
                      <span>{bankAccount.name}</span>
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
                  <h2>Wallet balances linked to online banking</h2>
                </div>
                <span className="module-tag">Separate from deposits</span>
              </div>

              <p>
                Digital assets are connected to the banking environment for this
                prototype, but they are separate from bank deposits.
              </p>

              <div className="account-list">
                {digitalAssetBalances.map((asset) => (
                  <article className="account-row" key={asset.name}>
                    <div>
                      <h3>{asset.name}</h3>
                      <p>{asset.balance}</p>
                      <span>Connected digital asset balance</span>
                    </div>
                    <strong>{asset.detail}</strong>
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
                Digital assets shown on this page are connected balances for
                prototype purposes only. They are not bank deposits and do not
                have the same protections as traditional accounts.
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
