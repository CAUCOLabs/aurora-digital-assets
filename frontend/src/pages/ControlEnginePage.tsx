import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const statusCards = [
  ['Mode', 'Local deterministic prototype'],
  ['Real integrations', '0'],
  ['Real assets', '0'],
  ['External execution', 'Disabled'],
  ['Evidence', 'Required'],
  ['Decision model', 'Controlled'],
]

const controlRows = [
  {
    name: 'Policy check',
    detail: 'Applies deterministic policy requirements before any sensitive operation can continue.',
    status: 'Required',
  },
  {
    name: 'Risk score',
    detail: 'Converts rail, custody, approval, agent and operational signals into a controlled risk level.',
    status: 'Scored',
  },
  {
    name: 'Evidence requirement',
    detail: 'Requires audit-ready evidence before routing review or changing operation state.',
    status: 'Evidence-first',
  },
  {
    name: 'Blocking reasons',
    detail: 'Keeps explicit reasons when an operation is blocked, paused or routed for remediation.',
    status: 'Traceable',
  },
  {
    name: 'Review route',
    detail: 'Routes decisions to risk, compliance, evidence, human approval integrity or agent governance paths.',
    status: 'Reviewable',
  },
  {
    name: 'Controlled decision',
    detail: 'Allows only controlled decisions such as block, pause, remediate, route for review or approve internally.',
    status: 'Governed',
  },
]

const decisionFlow = [
  'Signal',
  'Classification',
  'Policy',
  'Risk score',
  'Evidence',
  'Review route',
  'Approval integrity',
  'Controlled decision',
]

const connectedModules = [
  ['Aurora Trust Engine', '/bank-staff/trust-engine'],
  ['Asset Rail Governance', '/bank-staff/asset-rail-governance'],
  ['Regulation Engine', '/bank-staff/regulation-engine'],
  ['Risk Operations', '/bank-staff/risk-operations'],
  ['Evidence Packages', '/bank-staff/evidence-packages'],
  ['Human Approval Integrity', '/bank-staff/human-approval-integrity'],
  ['Agent Governance', '/bank-staff/agent-governance'],
  ['Audit Trail', '/reports/audit-trail'],
]

export function ControlEnginePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Control Engine</p>
            <h1>Controlled Decision Layer</h1>
            <p>
              Blocks, pauses, routes, evidences or allows internal review for
              sensitive banking and digital asset operations before state can
              change.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Control model active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Control status</p>
                  <h2>Decision boundary</h2>
                </div>
                <span className="module-tag">Internal staff console</span>
              </div>

              <div className="account-list">
                {statusCards.map(([label, value]) => (
                  <div className="account-row" key={label}>
                    <div>
                      <strong>{label}: </strong>
                      <span>{value}</span>
                    </div>
                    <span className="status-pill">Ready</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Control matrix</p>
                  <h2>Deterministic control gates</h2>
                </div>
                <span className="module-tag">Evidence-preserving</span>
              </div>

              <div className="account-list">
                {controlRows.map((row) => (
                  <div className="account-row" key={row.name}>
                    <div>
                      <strong>{row.name}: </strong>
                      <span>{row.detail}</span>
                    </div>
                    <span className="status-pill">{row.status}</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Decision flow</p>
                  <h2>From signal to controlled decision</h2>
                </div>
                <span className="module-tag">No direct execution</span>
              </div>

              <div className="account-list">
                {decisionFlow.map((step, index) => (
                  <div className="account-row" key={step}>
                    <div>
                      <strong>{String(index + 1).padStart(2, '0')} — {step}: </strong>
                      <span>
                        {index === decisionFlow.length - 1
                          ? 'Final decision remains controlled, evidenced and reviewable.'
                          : 'The operation cannot continue until this gate is evaluated.'}
                      </span>
                    </div>
                    <span className="status-pill">Gate</span>
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <div className="right-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Connected modules</p>
                  <h2>Control routing</h2>
                </div>
                <span className="module-tag">Aurora Trust Engine</span>
              </div>

              <div className="account-list">
                {connectedModules.map(([label, to]) => (
                  <Link className="account-row" to={to} key={to}>
                    <div>
                      <strong>{label}: </strong>
                      <span>Open related governance module</span>
                    </div>
                    <span className="status-pill">Open</span>
                  </Link>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Controlled outcomes</p>
                  <h2>Allowed decision types</h2>
                </div>
                <span className="module-tag">No blind approval</span>
              </div>

              <div className="account-list">
                {[
                  'Block operation',
                  'Pause operation',
                  'Require remediation',
                  'Route for review',
                  'Create evidence package',
                  'Require dual control',
                  'Allow internal review only',
                ].map((item) => (
                  <div className="account-row" key={item}>
                    <div>
                      <strong>{item}: </strong>
                      <span>Deterministic prototype decision path.</span>
                    </div>
                    <span className="status-pill">Controlled</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Safety boundary</p>
                  <h2>Prototype-only control layer</h2>
                </div>
              </div>

              <p className="panel-note">
                Local deterministic control engine interface only. No real
                banking, custody, PSP, digital euro, CBDC, stablecoin,
                cryptoasset, blockchain, cloud, payment, settlement, transfer,
                customer data, private key, credential or secret is used or
                executed. This is not legal advice or regulatory certification.
              </p>
            </Panel>
          </div>
        </section>
      </main>
    </div>
  )
}
