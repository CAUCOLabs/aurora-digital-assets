import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

export function ReportsPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Reports</p>
            <h1>Digital assets reporting</h1>
            <p>
              Review simulated tax summaries, transaction history, and export
              concepts for PDF and CSV reports.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Tax reporting enabled
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Tax year</p>
                  <h2>2026 digital assets summary</h2>
                </div>
                <span className="module-tag">Mock report</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Total purchases</p>
                  <strong>75,00 €</strong>
                  <span>BTC and ETH simulated purchases.</span>
                </div>

                <div className="custody-card">
                  <p>Estimated realized gain/loss</p>
                  <strong>0,00 €</strong>
                  <span>Prototype value only. Not tax advice.</span>
                </div>
              </div>

              <div className="action-row">
                <button type="button">Export PDF</button>
                <button className="secondary-button" type="button">
                  Export CSV
                </button>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Disclaimer</p>
              <h2>Not official tax advice</h2>
              <p>
                This report view is a simulated concept and does not replace
                official tax reporting or professional tax advice.
              </p>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}