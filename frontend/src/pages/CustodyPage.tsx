import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'

const custodyQuestions = [
  {
    question: 'Who holds the asset?',
    answer:
      'In this concept, assets are shown inside the banking interface through an internal custodial wallet or regulated custody partner model.',
  },
  {
    question: 'Does the user manage private keys?',
    answer:
      'No. In the internal custodial wallet concept, the user does not see seed phrases or sign blockchain transactions manually.',
  },
  {
    question: 'Can the user withdraw externally?',
    answer:
      'Yes, but external withdrawals are treated as higher-risk actions and may require security review before completion.',
  },
]

const custodyEvents = [
  {
    title: 'Asset credited to internal wallet',
    detail: 'BTC purchase reflected in the simulated custodial wallet.',
    status: 'Recorded',
  },
  {
    title: 'Custody status shown to user',
    detail: 'User can see that assets are separate from bank deposits.',
    status: 'Visible',
  },
  {
    title: 'External withdrawal request',
    detail: 'Transfer request creates a reviewable audit event.',
    status: 'Pending review',
  },
]

export function CustodyPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Custody model</p>
            <h1>Who controls what?</h1>
            <p>
              Understand how the Aurora Digital Assets concept explains custody,
              private keys, bank-side protection, and external wallet risk.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Custody transparency
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Internal custodial wallet concept</h2>
                </div>
                <span className="module-tag">v0.2 concept</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Custody model</p>
                  <strong>Internal custodial wallet</strong>
                  <span>
                    Digital assets are visible inside online banking, but the
                    user does not manage private keys directly.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Product boundary</p>
                  <strong>Separate from bank deposits</strong>
                  <span>
                    Digital assets can lose value and are not presented as
                    deposit-like products in this prototype.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Custody clarity</p>
                  <h2>Questions the interface should answer</h2>
                </div>
              </div>

              <div className="account-list">
                {custodyQuestions.map((item) => (
                  <article className="account-row" key={item.question}>
                    <div>
                      <h3>{item.question}</h3>
                      <p>{item.answer}</p>
                      <span>Customer-facing explanation</span>
                    </div>
                    <strong>Clear</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Risk boundary</p>
                  <h2>External wallet transfer changes responsibility</h2>
                </div>
                <Link className="button-link secondary-button" to="/withdrawals">
                  Go to withdrawals
                </Link>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Inside banking environment</p>
                  <strong>Controls active</strong>
                  <span>
                    Authentication, monitoring, reporting, support processes,
                    withdrawal review, and audit trail concepts may apply.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Outside banking environment</p>
                  <strong>User responsibility increases</strong>
                  <span>
                    Wrong addresses, private key loss, scams, or incompatible
                    networks may be difficult or impossible to recover.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Audit trail</p>
                  <h2>Custody-related evidence</h2>
                </div>
                <span className="module-tag">Deterministic log</span>
              </div>

              <div className="account-list">
                {custodyEvents.map((event) => (
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
              <p className="eyebrow">Custody status</p>
              <h2>What the user sees</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Digital assets visible in banking UI
                </div>
                <div>
                  <span className="status-dot"></span>
                  Private keys not exposed to user
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail enabled
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Assets are separate from deposits
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Important boundary</p>
              <h2>External transfers are different</h2>
              <p>
                When assets leave the bank-integrated environment, the user may
                lose access to bank-side controls such as withdrawal review,
                support workflows, and organized reporting.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">User responsibilities</p>
              <h2>Before self-custody</h2>

              <ul className="notification-list">
                <li>Understand who controls the external wallet.</li>
                <li>Verify the destination address and network.</li>
                <li>Store seed phrases or private keys safely.</li>
                <li>Understand that blockchain transfers are irreversible.</li>
              </ul>
            </Panel>

            <Panel>
              <p className="eyebrow">Related actions</p>
              <h2>Continue</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Reports
                </Link>
                <Link className="button-link secondary-button" to="/wallet">
                  Wallet
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page describes a fictional custody
          model and does not provide real custody services, banking services, or
          financial advice.
        </section>
      </main>
    </div>
  )
}
