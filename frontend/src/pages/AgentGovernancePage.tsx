import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'

const prototypeBadges = [
  'Local deterministic prototype',
  '26 backend phases completed',
  '196 backend tests passing',
  'No real agent execution',
  'No real custodian access',
  'No secrets',
]

const governanceModules = [
  {
    title: 'Agent Registry',
    status: 'Ready',
    risk: 'low',
    description:
      'Inventory of simulated agent identities, ownership, permitted operating zones, and current lifecycle status.',
  },
  {
    title: 'Agent Passport',
    status: 'Ready',
    risk: 'low',
    description:
      'Structured profile for declared purpose, control evidence, model boundaries, and institutional review readiness.',
  },
  {
    title: 'Agent Permissions',
    status: 'Under review',
    risk: 'medium',
    description:
      'Deterministic permission model for what an agent may request, recommend, prepare, or never execute.',
  },
  {
    title: 'Agent Action Audit',
    status: 'Ready',
    risk: 'low',
    description:
      'Audit trail view for simulated agent recommendations, evidence creation, routing decisions, and blocked actions.',
  },
  {
    title: 'Agent Revocation',
    status: 'Ready',
    risk: 'medium',
    description:
      'Control path for suspending or revoking an agent identity when evidence, policy, or operating context changes.',
  },
  {
    title: 'Agent Policy Engine',
    status: 'Active',
    risk: 'medium',
    description:
      'Policy checks for permitted actions, sensitive operation boundaries, escalation routing, and required evidence.',
  },
  {
    title: 'Agent Abuse Detection',
    status: 'Monitoring',
    risk: 'high',
    description:
      'Static risk indicators for prompt abuse, policy bypass attempts, excessive access requests, and suspicious routing.',
  },
  {
    title: 'Agent Identity Governance',
    status: 'Ready',
    risk: 'low',
    description:
      'Governance record for identity ownership, scope, segregation, approval chain, and revocation readiness.',
  },
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

export function AgentGovernancePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Bank staff control</p>
            <h1>Agent governance console</h1>
            <p>
              Institutional control view for simulated agent identity, policy,
              permissions, revocation, abuse detection, and audit evidence.
            </p>
          </div>
          <div className="security-badge">
            <span className="status-dot"></span>
            Local prototype only
          </div>
        </section>

        <section className="assets-summary financial-crime-summary">
          {prototypeBadges.map((badge) => (
            <div key={badge}>
              <p>Control status</p>
              <strong>{badge}</strong>
              <span>Static demo evidence</span>
            </div>
          ))}
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Governance modules</p>
                  <h2>Controlled agent operating model</h2>
                </div>
                <span className="module-tag">No live execution</span>
              </div>

              <div className="financial-crime-alert-list">
                {governanceModules.map((module) => (
                  <article className="financial-crime-alert" key={module.title}>
                    <div className="panel-header">
                      <div>
                        <p className="eyebrow">Agent governance</p>
                        <h3>{module.title}</h3>
                      </div>
                      <div className="status-label-group">
                        <span className={`risk-label risk-label-${module.risk}`}>
                          {module.risk}
                        </span>
                        <span
                          className={`status-label status-${formatStatusClass(
                            module.status,
                          )}`}
                        >
                          {module.status}
                        </span>
                      </div>
                    </div>
                    <p>{module.description}</p>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Operating principle</p>
              <h2>No blind trust</h2>
              <p>
                Aurora does not blindly trust AI, agents, partners, custodians,
                or human reviewers. Sensitive decisions are controlled, scored,
                evidenced, reviewable, and auditable before operation state can
                change.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Decision control chain</p>
              <h2>Before sensitive action</h2>
              <div className="summary-list">
                {[
                  'Risk signal captured',
                  'Guardrail evaluated',
                  'Evidence package prepared',
                  'Review case routed',
                  'Agent and human integrity checked',
                  'Decision recorded',
                ].map((step) => (
                  <div key={step}>
                    <span>Control step</span>
                    <strong>{step}</strong>
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
                <Link className="button-link" to="/bank-staff/risk-operations">
                  Open risk operations
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/bank-staff/human-approval-integrity"
                >
                  Open human approval integrity
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a local deterministic prototype. No real
          agents, custodians, bank systems, secrets, or customer records are
          connected.
        </p>
      </main>
    </div>
  )
}
