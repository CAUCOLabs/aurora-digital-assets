import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const costDrivers = [
  {
    title: 'Custody',
    detail:
      'Secure custody infrastructure, segregation of assets, partner integrations, operational controls, and incident response.',
    status: 'High impact',
  },
  {
    title: 'Compliance and AML',
    detail:
      'Transaction monitoring, wallet risk checks, sanctions screening, suspicious activity escalation, and audit logs.',
    status: 'Required',
  },
  {
    title: 'Tax reporting',
    detail:
      'Purchase history, sales, transfers, annual summaries, exportable reports, and clear user-facing disclaimers.',
    status: 'User value',
  },
  {
    title: 'Customer support',
    detail:
      'Support for delayed withdrawals, custody questions, address mistakes, reporting issues, and suspected scams.',
    status: 'Operational cost',
  },
]

const riskConstraints = [
  'BTC and ETH first',
  'Spot-only access',
  'No leverage or derivatives',
  'No yield promises',
  'Transparent fees and spreads',
  'Controlled external withdrawals',
  'Cooling period for new addresses',
  'Audit trail for sensitive actions',
]

const comparisonRows = [
  {
    area: 'Main value',
    exchange: 'Liquidity and execution',
    bank: 'Trust, reporting, controlled access',
  },
  {
    area: 'Asset selection',
    exchange: 'Broad',
    bank: 'Limited and curated',
  },
  {
    area: 'Trading tools',
    exchange: 'Advanced',
    bank: 'Minimal and responsible',
  },
  {
    area: 'External withdrawals',
    exchange: 'Fast and user-controlled',
    bank: 'Controlled and reviewed',
  },
  {
    area: 'Business goal',
    exchange: 'Trading activity',
    bank: 'Safer financial relationship',
  },
]

export function OperatingModelPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Operating model</p>
            <h1>How could this make sense for a bank?</h1>
            <p>
              Explore the business and operational logic behind a bank-integrated
              digital assets module, including cost drivers, margin reality, and
              risk reduction by product design.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            v0.2 planning
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Strategic question</p>
                  <h2>Not an exchange clone</h2>
                </div>
                <span className="module-tag">Banking model</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Exchange model</p>
                  <strong>Speed, liquidity, trading volume</strong>
                  <span>
                    Global exchanges compete on execution, asset selection,
                    trading tools, and low fees.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Bank model</p>
                  <strong>Trust, clarity, reporting, protection</strong>
                  <span>
                    A bank-integrated model should focus on safer access,
                    custody visibility, reporting, and controlled withdrawals.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Cost drivers</p>
                  <h2>Operational cost is real</h2>
                </div>
                <span className="module-tag">Margin reality</span>
              </div>

              <div className="account-list">
                {costDrivers.map((item) => (
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

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Bank vs exchange</p>
                  <h2>Different product positions</h2>
                </div>
                <span className="module-tag">Comparison</span>
              </div>

              <div className="comparison-table">
                <div className="comparison-row comparison-header">
                  <strong>Area</strong>
                  <strong>Global exchange</strong>
                  <strong>Bank-integrated model</strong>
                </div>

                {comparisonRows.map((row) => (
                  <div className="comparison-row" key={row.area}>
                    <strong>{row.area}</strong>
                    <span>{row.exchange}</span>
                    <span>{row.bank}</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Risk reduction</p>
                  <h2>Product constraints by design</h2>
                </div>
                <span className="module-tag">Responsible access</span>
              </div>

              <div className="check-list two-column-checks">
                {riskConstraints.map((constraint) => (
                  <div key={constraint}>
                    <span className="status-dot"></span>
                    {constraint}
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Margin reality</p>
              <h2>Not only trading fees</h2>
              <p>
                A bank may not justify this product only through small retail
                trading fees. The broader value may come from custody, reporting,
                customer trust, retention, and long-term digital asset
                infrastructure positioning.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Possible value sources</p>
              <h2>Banking value</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Transparent transaction fee
                </div>
                <div>
                  <span className="status-dot"></span>
                  Custody or service fee
                </div>
                <div>
                  <span className="status-dot"></span>
                  Premium reporting features
                </div>
                <div>
                  <span className="status-dot"></span>
                  Customer retention
                </div>
                <div>
                  <span className="status-dot"></span>
                  Wealth or business account integration
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Operating workflow</p>
              <h2>Controlled access</h2>

              <ul className="notification-list">
                <li>User enters Digital Assets module.</li>
                <li>System shows custody and risk information.</li>
                <li>Product limits and security controls apply.</li>
                <li>Transactions create audit events.</li>
                <li>External withdrawals may enter review.</li>
              </ul>
            </Panel>

            <Panel>
              <p className="eyebrow">Related concept</p>
              <h2>Custody model</h2>
              <p>
                The operating model depends on clear custody design and
                transparent user communication around who controls what.
              </p>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/custody">
                  View custody model
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Reports
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page describes a fictional
          operating model and does not provide banking, custody, investment, tax,
          or legal advice.
        </section>
      </main>
    </div>
  )
}