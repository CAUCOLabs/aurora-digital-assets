import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { digitalAssets } from '../data/dashboardData'

const walletActivity = [
  {
    title: 'BTC purchase received',
    detail: '0.00072 BTC added to internal wallet',
    status: 'Completed',
  },
  {
    title: 'ETH purchase received',
    detail: '0.0121 ETH added to internal wallet',
    status: 'Completed',
  },
  {
    title: 'External BTC withdrawal request',
    detail: '0.001 BTC pending review',
    status: 'Pending review',
  },
]

export function WalletPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Wallet</p>
            <h1>Internal digital assets wallet</h1>
            <p>
              View simulated assets held through the Aurora Bank custodial
              wallet concept, including balances, custody status, and wallet
              activity.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Audit trail enabled
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Wallet summary</h2>
                </div>
                <span className="module-tag">Custodial concept</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Total wallet value</p>
                  <strong>1 245,80 €</strong>
                  <span>
                    Estimated value based on mock market prices. Digital assets
                    are separate from bank deposits.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Custody model</p>
                  <strong>Internal custodial wallet concept</strong>
                  <span>
                    The user does not manage private keys in this simulated
                    banking model.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Balances</p>
                  <h2>Wallet assets</h2>
                </div>
                <Link className="button-link secondary-button" to="/buy-sell">
                  Buy / Sell
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
                  <p className="eyebrow">Activity</p>
                  <h2>Wallet activity</h2>
                </div>
                <span className="module-tag">Simulated events</span>
              </div>

              <div className="account-list">
                {walletActivity.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Quick actions</p>
              <h2>Manage wallet</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/buy-sell">
                  Buy / Sell
                </Link>
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Tax reports
                </Link>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Custody</p>
              <h2>Custody status</h2>
              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Internal custodial wallet concept
                </div>
                <div>
                  <span className="status-dot"></span>
                  User does not manage private keys
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail enabled
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Digital assets are separate from deposits
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Important</p>
              <h2>No private key access</h2>
              <p>
                In this custodial concept, the banking interface shows wallet
                balances and activity, but does not expose seed phrases or
                private keys to the user.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page simulates an internal
          custodial wallet and does not store real crypto assets, private keys,
          or customer data.
        </section>
      </main>
    </div>
  )
}
