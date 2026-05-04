import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { AccountRow } from '../components/AccountRow'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { accounts, digitalAssets, notifications } from '../data/dashboardData'

export function DashboardPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

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
            <Panel>
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
                  <AccountRow key={account.name} account={account} />
                ))}
              </div>
            </Panel>

            <Panel id="digital-assets">
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
                  <DigitalAssetRow key={asset.symbol} asset={asset} />
                ))}
              </div>

              <div className="action-row">
                <Link className="button-link" to="/buy-sell">
                  Buy
                </Link>
                <Link className="button-link" to="/buy-sell">
                  Sell
                </Link>
                <Link className="button-link" to="/withdrawals">
                  Withdraw
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Reports
                </Link>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Notifications</p>
              <h2>Important messages</h2>

              <ul className="notification-list">
                {notifications.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">User protection</p>
              <h2>Digital assets risk notice</h2>
              <p>
                Crypto assets can lose value quickly. External wallet transfers
                are irreversible and may require additional security review.
              </p>
              <Link className="button-link secondary-button" to="/digital-assets">
                Read risk information
              </Link>
            </Panel>

            <Panel>
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
            </Panel>
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