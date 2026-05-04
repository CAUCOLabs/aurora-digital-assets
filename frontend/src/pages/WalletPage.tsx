import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { digitalAssets } from '../data/dashboardData'

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
              wallet concept.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Audit trail enabled
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Balances</p>
                  <h2>Wallet assets</h2>
                </div>
                <span className="module-tag">Custodial concept</span>
              </div>

              <div className="asset-list">
                {digitalAssets.map((asset) => (
                  <DigitalAssetRow key={asset.symbol} asset={asset} />
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
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
                  <span className="warning-dot"></span>
                  Digital assets are separate from deposits
                </div>
              </div>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}