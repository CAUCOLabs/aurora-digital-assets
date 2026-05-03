import './App.css'

const accounts = [
  {
    name: 'Aurora Current Account',
    type: 'Current account',
    balance: '2 450,10 €',
    maskedIban: 'FI12 **** **** **** 1234',
  },
  {
    name: 'Aurora Savings Account',
    type: 'Savings account',
    balance: '8 920,00 €',
    maskedIban: 'FI45 **** **** **** 5678',
  },
  {
    name: 'Aurora Credit Card',
    type: 'Credit account',
    balance: '-203,33 €',
    maskedIban: 'Card ending 2044',
  },
]

const digitalAssets = [
  {
    asset: 'Bitcoin',
    symbol: 'BTC',
    balance: '0.012450 BTC',
    value: '865,28 €',
  },
  {
    asset: 'Ethereum',
    symbol: 'ETH',
    balance: '0.184200 ETH',
    value: '380,52 €',
  },
]

const notifications = [
  'External wallet withdrawal is pending review.',
  'Your 2026 digital assets tax summary is being prepared.',
  'Strong authentication is active for Digital Assets.',
]

function App() {
  return (
    <div className="bank-shell">
      <header className="top-bar">
        <div className="brand">
          <div className="brand-mark">A</div>
          <div>
            <p className="brand-name">Aurora Bank</p>
            <p className="brand-subtitle">Online Banking Demo</p>
          </div>
        </div>

        <nav className="main-nav" aria-label="Main navigation">
          <a className="active" href="#home">Home</a>
          <a href="#payments">Payments</a>
          <a href="#accounts">Accounts</a>
          <a href="#cards">Cards and Currency</a>
          <a href="#investments">Investments</a>
          <a href="#digital-assets">Digital Assets</a>
          <a href="#reports">Reports</a>
        </nav>

        <div className="user-area">
          <span>Claudio Demo</span>
          <button type="button">Log out</button>
        </div>
      </header>

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Welcome back</p>
            <h1>Financial overview</h1>
            <p>
              Review your accounts, payments, and digital assets from one
              banking environment.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Strong authentication active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <section className="panel">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Accounts</p>
                  <h2>Your accounts</h2>
                </div>
                <button className="secondary-button" type="button">
                  New payment
                </button>
              </div>

              <div className="account-list">
                {accounts.map((account) => (
                  <article className="account-row" key={account.name}>
                    <div>
                      <h3>{account.name}</h3>
                      <p>{account.type}</p>
                      <span>{account.maskedIban}</span>
                    </div>
                    <strong>{account.balance}</strong>
                  </article>
                ))}
              </div>
            </section>

            <section className="panel" id="digital-assets">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Digital Assets</p>
                  <h2>Aurora Digital Assets Wallet</h2>
                </div>
                <span className="module-tag">Concept module</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Total digital assets value</p>
                  <strong>1 245,80 €</strong>
                  <span>
                    Digital assets are volatile and are separate from bank
                    deposits.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Custody status</p>
                  <strong>Internal custodial wallet concept</strong>
                  <span>KYC verified · Audit trail enabled</span>
                </div>
              </div>

              <div className="asset-list">
                {digitalAssets.map((asset) => (
                  <article className="asset-row" key={asset.symbol}>
                    <div className="asset-symbol">{asset.symbol}</div>
                    <div>
                      <h3>{asset.asset}</h3>
                      <p>{asset.balance}</p>
                    </div>
                    <strong>{asset.value}</strong>
                  </article>
                ))}
              </div>

              <div className="action-row">
                <button type="button">Buy</button>
                <button type="button">Sell</button>
                <button type="button">Withdraw</button>
                <button className="secondary-button" type="button">
                  Reports
                </button>
              </div>
            </section>
          </div>

          <aside className="right-column">
            <section className="panel">
              <p className="eyebrow">Notifications</p>
              <h2>Important messages</h2>

              <ul className="notification-list">
                {notifications.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </section>

            <section className="panel risk-panel">
              <p className="eyebrow">User protection</p>
              <h2>Digital assets risk notice</h2>
              <p>
                Crypto assets can lose value quickly. External wallet transfers
                are irreversible and may require additional security review.
              </p>
              <button className="secondary-button" type="button">
                Read risk information
              </button>
            </section>

            <section className="panel">
              <p className="eyebrow">Compliance status</p>
              <h2>Security checks</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  KYC verified
                </div>
                <div>
                  <span className="status-dot"></span>
                  Transaction monitoring enabled
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Withdrawal pending review
                </div>
              </div>
            </section>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. Not affiliated with any bank. No real
          bank APIs, no real custody, no private keys, and no real customer data.
        </section>
      </main>
    </div>
  )
}

export default App