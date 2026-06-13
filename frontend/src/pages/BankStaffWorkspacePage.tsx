import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'

const workspaceModules = [
  {
    title: 'Customer onboarding',
    description:
      'Review the bank-managed customer onboarding model before digital asset services become available.',
    status: 'Bank staff control',
    to: '/bank-staff/onboarding',
  },
  {
    title: 'Customer access authorization',
    description:
      'Look up a demo customer and request temporary customer-authorized staff access.',
    status: 'Customer authorization',
    to: '/bank-staff/customer-access',
  },
  {
    title: 'Compliance review',
    description:
      'Review simulated transaction monitoring outcomes, wallet risk checks, and escalation evidence.',
    status: 'Compliance review',
    to: '/compliance-review',
  },
  {
    title: 'Financial crime monitoring',
    description:
      'Review insider risk, shell company indicators, structured deposits, crypto off-ramp risk, foreign transfer risk, and network-linked suspicious activity.',
    status: 'Monitoring alerts',
    to: '/bank-staff/financial-crime-monitoring',
  },
  {
    title: 'Compliance intelligence',
    description:
      'Explain financial crime alerts, review triggered controls, identify missing evidence, and prepare reviewer guidance before escalation.',
    status: 'Reasoning layer',
    to: '/bank-staff/compliance-intelligence',
  },
  {
    title: 'Evidence packages',
    description:
      'Prepare structured evidence packages for compliance review, audit, investigation, and regulator-facing documentation.',
    status: 'Package readiness',
    to: '/bank-staff/evidence-packages',
  },
  {
    title: 'Reports and audit trail',
    description:
      'Open customer-facing reports, tax report concepts, and prototype audit evidence.',
    status: 'Audit evidence',
    to: '/reports',
  },
  {
    title: 'Demo administration',
    description:
      'Inspect and reset local prototype data used by the Aurora Digital Assets demo environment.',
    status: 'Prototype only',
    to: '/admin-demo',
  },
]

const workspaceControls = [
  'Staff actions are represented as simulated prototype workflows.',
  'Sensitive customer details remain locked until customer authorization is granted.',
  'Digital asset access depends on eligibility, compliance review, and audit trail controls.',
  'No real banking systems, custody providers, or customer records are connected.',
]

export function BankStaffWorkspacePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Protected bank staff area</p>
            <h1>Bank Staff Workspace</h1>
            <p>
              Internal concept workspace for onboarding, customer-authorized
              access, compliance review, reports, and demo administration.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Authenticated session
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Workspace modules</p>
                  <h2>Staff tools</h2>
                </div>
                <span className="module-tag">Concept prototype</span>
              </div>

              <div className="account-list">
                {workspaceModules.map((module) => (
                  <Link
                    className="account-row"
                    key={module.to}
                    to={module.to}
                  >
                    <div>
                      <h3>{module.title}</h3>
                      <p>{module.description}</p>
                      <span>{module.to}</span>
                    </div>
                    <strong>{module.status}</strong>
                  </Link>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Staff boundary</p>
              <h2>Prototype controls</h2>
              <p>
                This workspace demonstrates banking-first control points for a
                regulated digital assets concept. It is not connected to real
                staff identities, customer records, custody systems, or banking
                infrastructure.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Operating guardrails</p>
              <h2>Access model</h2>
              <div className="check-list">
                {workspaceControls.map((control) => (
                  <div key={control}>
                    <span className="status-dot"></span>
                    {control}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Quick links</p>
              <h2>Common actions</h2>
              <div className="action-row vertical-actions">
                <Link className="button-link" to="/bank-staff/onboarding">
                  Open onboarding model
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/bank-staff/customer-access"
                >
                  Request customer access
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. No real financial
          transactions, digital asset custody, staff access, or customer data are
          processed.
        </p>
      </main>
    </div>
  )
}
