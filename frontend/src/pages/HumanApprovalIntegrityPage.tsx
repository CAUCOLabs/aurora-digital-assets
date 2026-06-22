import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'

const integrityControls = [
  {
    title: 'No single human can override a critical system block',
    status: 'Blocked',
    risk: 'critical',
  },
  {
    title: 'Dual control / four-eyes approval',
    status: 'Required',
    risk: 'medium',
  },
  {
    title: 'Segregation of duties',
    status: 'Active',
    risk: 'low',
  },
  {
    title: 'Reviewer conflict detection',
    status: 'Monitoring',
    risk: 'medium',
  },
  {
    title: 'Emergency override control',
    status: 'Escalated',
    risk: 'high',
  },
  {
    title: 'Post-approval audit',
    status: 'Ready',
    risk: 'low',
  },
]

const demoCaseEvents = [
  { label: 'Critical system block active', status: 'Blocked' },
  { label: 'Emergency override requested', status: 'Controlled' },
  { label: 'Human approval blocked', status: 'Denied' },
  { label: 'Second reviewer required', status: 'Required' },
  { label: 'Compliance escalation required', status: 'Escalated' },
  { label: 'Evidence package created', status: 'Created' },
  { label: 'Operation paused', status: 'Paused' },
]

const safetyBoundaries = [
  'Local deterministic prototype only',
  'No real bank integration',
  'No real custodian integration',
  'No real custody',
  'No real blockchain execution',
  'No real cloud deployment',
  'No real employee monitoring',
  'No legal accusation or criminal finding',
  'No private keys or secrets',
]

function formatStatusClass(status: string) {
  return status.toLowerCase().replaceAll(' ', '_')
}

export function HumanApprovalIntegrityPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Bank operations integrity</p>
            <h1>Human approval integrity console</h1>
            <p>
              Human review is not a trust anchor. It is a controlled risk event.
            </p>
          </div>
          <div className="security-badge">
            <span className="warning-dot"></span>
            Critical override protected
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Approval controls</p>
                  <h2>Reviewer integrity safeguards</h2>
                </div>
                <span className="module-tag">No live execution</span>
              </div>

              <div className="financial-crime-alert-list">
                {integrityControls.map((control) => (
                  <article className="financial-crime-alert" key={control.title}>
                    <div className="panel-header compact-panel-header">
                      <div>
                        <h3>{control.title}</h3>
                        <p>
                          Static deterministic control used to prevent human
                          approval from becoming an uncontrolled bypass path.
                        </p>
                      </div>
                      <div className="status-label-group">
                        <span className={`risk-label risk-label-${control.risk}`}>
                          {control.risk}
                        </span>
                        <span
                          className={`status-label status-${formatStatusClass(
                            control.status,
                          )}`}
                        >
                          {control.status}
                        </span>
                      </div>
                    </div>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Static demo case</p>
                  <h2>External wallet withdrawal blocked</h2>
                </div>
                <span className="risk-label risk-label-critical">critical</span>
              </div>

              <div className="summary-list financial-crime-alert-meta">
                {demoCaseEvents.map((event) => (
                  <div key={event.label}>
                    <span>{event.status}</span>
                    <strong>{event.label}</strong>
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Core principle</p>
              <h2>Controlled risk event</h2>
              <p>
                A human reviewer can add context, request evidence, or approve
                low-risk steps within policy. A human reviewer cannot override a
                critical system block alone.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Required evidence</p>
              <h2>Before approval can proceed</h2>
              <div className="summary-list">
                {[
                  'System block reason',
                  'Requester identity and role',
                  'Second reviewer requirement',
                  'Conflict check result',
                  'Compliance escalation record',
                  'Post-approval audit event',
                ].map((item) => (
                  <div key={item}>
                    <span>Evidence item</span>
                    <strong>{item}</strong>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Safety boundary</p>
              <h2>Prototype constraints</h2>
              <div className="check-list">
                {safetyBoundaries.map((boundary) => (
                  <div key={boundary}>
                    <span className="status-dot"></span>
                    {boundary}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Related staff modules</p>
              <h2>Review paths</h2>
              <div className="action-row vertical-actions">
                <Link className="button-link" to="/bank-staff/agent-governance">
                  Open agent governance
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/bank-staff/evidence-packages"
                >
                  Open evidence packages
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a local deterministic prototype. No real
          employee monitoring, legal accusation, criminal finding, custody,
          blockchain execution, cloud deployment, or secrets are present.
        </p>
      </main>
    </div>
  )
}
