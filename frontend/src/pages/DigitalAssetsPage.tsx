import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { digitalAssets } from '../data/dashboardData'

const recentActivity = [
  {
    title: 'BTC purchase completed',
    detail: '50,00 € from Aurora Current Account',
    status: 'Completed',
  },
  {
    title: 'ETH purchase completed',
    detail: '25,00 € from Aurora Current Account',
    status: 'Completed',
  },
  {
    title: 'External BTC withdrawal',
    detail: '0.001 BTC transfer request',
    status: 'Pending review',
  },
]

export function DigitalAssetsPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Digital Assets</p>
            <h1>Aurora Digital Assets</h1>
            <p>
              View your digital asset balances, custody status, recent activity,
              and available actions from inside your online banking environment.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Digital assets access active
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Total digital assets value</h2>
                </div>
                <span className="module-tag">Concept module</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Current estimated value</p>
                  <strong>1 245,80 €</strong>
                  <span>
                    This value is based on mock market prices and is shown for
                    prototype purposes only.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Custody model</p>
                  <strong>Internal custodial wallet concept</strong>
                  <span>
                    Digital assets are separate from bank deposits and may lose
                    value.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Wallet</p>
                  <h2>Your digital assets</h2>
                </div>
                <Link className="button-link secondary-button" to="/wallet">
                  View wallet
                </Link>
              </div>

              <div className="asset-list">
                {digitalAssets.map((asset) => (
                  <DigitalAssetRow key={asset.symbol} asset={asset} />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Recent activity</p>
                  <h2>Digital asset transactions</h2>
                </div>
              </div>

              <div className="account-list">
                {recentActivity.map((item) => (
                  <article className="account-row" key={item.title}>
                    <div>
                      <h3>{item.title}</h3>
                      <p>{item.detail}</p>
                      <span>{item.status}</span>
                    </div>
                    <strong>{item.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Quick actions</p>
              <h2>Manage digital assets</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/buy-sell">
                  Buy digital assets
                </Link>
                <Link className="button-link" to="/buy-sell">
                  Sell digital assets
                </Link>
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Tax reports
                </Link>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Risk notice</p>
              <h2>Before you continue</h2>
              <p>
                Crypto assets are volatile. External wallet transfers are
                irreversible and may require additional review before approval.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Protection status</p>
              <h2>Protection enabled</h2>

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
                  Tax reporting enabled
                </div>
                <div>
                  <span className="warning-dot"></span>
                  External withdrawals require review
                </div>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real bank APIs, no real crypto
          custody, no private keys, and no real customer data.
        </section>
      </main>
    </div>
  )
}
