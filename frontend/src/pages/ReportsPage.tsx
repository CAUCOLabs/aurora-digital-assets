import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const reportableActivities = [
  {
    title: 'BTC purchase completed',
    detail: '50,00 €',
    status: 'Completed',
  },
  {
    title: 'ETH purchase completed',
    detail: '25,00 €',
    status: 'Completed',
  },
  {
    title: 'External BTC withdrawal',
    detail: '0.001 BTC',
    status: 'Pending review',
  },
]

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
              Review simulated annual summaries, transaction records, and
              export concepts for digital assets reporting inside the Aurora
              Bank prototype.
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
                  <p className="eyebrow">Annual summary</p>
                  <h2>2026 digital assets summary</h2>
                </div>
                <span className="module-tag">Mock report</span>
              </div>

              <div className="withdrawal-preview">
                <div>
                  <p>Tax year</p>
                  <strong>2026</strong>
                </div>
                <div>
                  <p>Total purchases</p>
                  <strong>75,00 €</strong>
                </div>
                <div>
                  <p>Total sales</p>
                  <strong>0,00 €</strong>
                </div>
                <div>
                  <p>Transfers</p>
                  <strong>1 pending external withdrawal</strong>
                </div>
                <div>
                  <p>Estimated realized gain/loss</p>
                  <strong>0,00 €</strong>
                </div>
              </div>

              <p>
                Prototype values only. Not official tax advice.
              </p>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Reportable activity</p>
                  <h2>Mocked transaction records</h2>
                </div>
                <span className="module-tag">Simulated</span>
              </div>

              <div className="account-list">
                {reportableActivities.map((activity) => (
                  <article className="account-row" key={activity.title}>
                    <div>
                      <h3>{activity.title}</h3>
                      <p>{activity.detail}</p>
                      <span>{activity.status}</span>
                    </div>
                    <strong>{activity.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Export center</p>
                  <h2>Reporting export concepts</h2>
                </div>
                <span className="module-tag">Static actions</span>
              </div>

              <div className="account-list">
                <article className="account-row">
                  <div>
                    <h3>PDF report export concept</h3>
                    <p>Annual digital assets summary formatted for review.</p>
                    <span>Prototype only</span>
                  </div>
                  <strong>Ready</strong>
                </article>
                <article className="account-row">
                  <div>
                    <h3>CSV transaction export concept</h3>
                    <p>Structured transaction records for user review.</p>
                    <span>Prototype only</span>
                  </div>
                  <strong>Ready</strong>
                </article>
                <article className="account-row">
                  <div>
                    <h3>Audit evidence package concept</h3>
                    <p>Mock evidence set for compliance and audit review.</p>
                    <span>Prototype only</span>
                  </div>
                  <strong>Ready</strong>
                </article>
              </div>

              <div className="action-row">
                <button type="button">Export PDF</button>
                <button className="secondary-button" type="button">
                  Export CSV
                </button>
                <button className="secondary-button" type="button">
                  Generate audit package
                </button>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Tax disclaimer</p>
              <h2>Simulated report only</h2>
              <p>
                This report view is a simulated concept and does not replace
                official tax reporting, official tax filing, or professional
                tax advice.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Report status</p>
              <h2>Export readiness</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Mock transactions loaded
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail available
                </div>
                <div>
                  <span className="status-dot"></span>
                  PDF export concept ready
                </div>
                <div>
                  <span className="status-dot"></span>
                  CSV export concept ready
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Official tax submission not connected
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">User protection</p>
              <h2>Transparent reporting</h2>
              <p>
                Clear reporting helps users understand purchases, sales,
                transfers, custody, and potential tax obligations before
                relying on official tax channels.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real bank APIs, no real tax filing,
          no real crypto custody, no private keys, and no real customer data.
        </section>
      </main>
    </div>
  )
}
