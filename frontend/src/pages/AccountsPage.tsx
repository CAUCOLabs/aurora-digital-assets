import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const bankAccount = {
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

const recentTransactions = [
  {
    title: 'Aurora Telecom Oyj invoice payment',
    amount: '-120,45 €',
    status: 'Pending',
    detail: 'Aurora Current Account · Reference preserved',
  },
  {
    title: 'Salary payment',
    amount: '+2 850,00 €',
    status: 'Completed',
    detail: 'Aurora Current Account · Salary',
  },
  {
    title: 'Grocery store card payment',
    amount: '-42,80 €',
    status: 'Completed',
    detail: 'Aurora Current Account · Card purchase',
  },
  {
    title: 'Digital asset invoice payment',
    amount: '0,00 €',
    status: 'Pending confirmation',
    detail: 'Aurora Current Account · Digital asset payment draft',
  },
]

const digitalAssetBalances = [
  {
    name: 'BTC wallet balance',
    balance: '0.012450 BTC',
    detail: '865,28 €',
  },
  {
    name: 'ETH wallet balance',
    balance: '0.184200 ETH',
    detail: '380,52 €',
  },
  {
    name: 'USDC payment asset balance',
    balance: '129.80 USDC',
    detail: 'Payment asset',
  },
  {
    name: 'USDT payment asset balance',
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
  'Payment receipts',
  'Digital asset reports',
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
              </div>

              <div className="account-list">
                {recentTransactions.map((transaction) => (
                  <article className="account-row" key={transaction.title}>
                    <div>
                      <h3>{transaction.title}</h3>
                      <p>{transaction.detail}</p>
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
