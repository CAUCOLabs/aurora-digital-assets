import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const statusCards = [
  ['Mode', 'Local deterministic prototype'],
  ['Policy source', 'Internal control model'],
  ['Real integrations', '0'],
  ['Real assets', '0'],
  ['External execution', 'Disabled'],
  ['Decision impact', 'Pre-control only'],
]

const policyRows = [
  {
    name: 'Asset rail policy',
    detail:
      'Applies different rule sets for digital euro, tokenized deposits, stablecoins, cryptoassets and security tokens.',
    status: 'Rail-aware',
  },
  {
    name: 'Custody policy',
    detail:
      'Defines when external custodian readiness, wallet boundaries and private key boundaries are required.',
    status: 'Boundary-based',
  },
  {
    name: 'Approval policy',
    detail:
      'Requires step-up review, dual control or escalation for sensitive banking and digital asset operations.',
    status: 'Review-first',
  },
  {
    name: 'Evidence policy',
    detail:
      'Requires audit-ready evidence before a controlled decision can be routed or accepted internally.',
    status: 'Evidence-first',
  },
  {
    name: 'Agent policy',
    detail:
      'Restricts agent actions through identity, permissions, revocation, abuse detection and audit controls.',
    status: 'Permission-bound',
  },
  {
    name: 'Human review policy',
    detail:
      'Treats human approval as a controlled risk event, not as a blind trust anchor.',
    status: 'Integrity-checked',
  },
  {
    name: 'Risk threshold policy',
    detail:
      'Maps policy breaches, missing controls and risk scores into block, pause, remediate or review decisions.',
    status: 'Thresholded',
  },
  {
    name: 'Operational resilience policy',
    detail:
      'Routes dependency failures, fallback modes and continuity issues into controlled operational responses.',
    status: 'Resilient',
  },
]

const policyFlow = [
  'Asset rail classification',
  'Regulatory mapping',
  'Applicable policy selection',
  'Required controls',
  'Evidence requirement',
  'Risk threshold',
  'Control decision',
]

const connectedModules = [
  ['Aurora Trust Engine', '/bank-staff/trust-engine'],
  ['Asset Rail Governance', '/bank-staff/asset-rail-governance'],
  ['Regulation Engine', '/bank-staff/regulation-engine'],
  ['Control Engine', '/bank-staff/control-engine'],
  ['Risk Operations', '/bank-staff/risk-operations'],
  ['Evidence Packages', '/bank-staff/evidence-packages'],
  ['Human Approval Integrity', '/bank-staff/human-approval-integrity'],
  ['Agent Governance', '/bank-staff/agent-governance'],
  ['Audit Trail', '/reports/audit-trail'],
]

const policyOutcomes = [
  'Require evidence package',
  'Require human integrity check',
  'Require agent permission check',
  'Require custodian readiness',
  'Require asset rail classification',
  'Require regulation mapping',
  'Pause operation',
  'Block operation',
  'Route for review',
]

export function PolicyEnginePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Policy Engine</p>
            <h1>Deterministic Policy Layer</h1>
            <p>
              Converts internal governance policies into deterministic control
              requirements before sensitive banking or digital asset operations
              can move forward.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Policy model active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Policy status</p>
                  <h2>Internal policy boundary</h2>
                </div>
                <span className="module-tag">Bank staff console</span>
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
                  <p className="eyebrow">Policy matrix</p>
                  <h2>Deterministic policy rules</h2>
                </div>
                <span className="module-tag">Rule-based governance</span>
              </div>

              <div className="account-list">
                {policyRows.map((row) => (
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
                  <p className="eyebrow">Policy flow</p>
                  <h2>From classification to policy decision</h2>
                </div>
                <span className="module-tag">Before control execution</span>
              </div>

              <div className="account-list">
                {policyFlow.map((step, index) => (
                  <div className="account-row" key={step}>
                    <div>
                      <strong>
                        {String(index + 1).padStart(2, '0')} — {step}:{' '}
                      </strong>
                      <span>
                        {index === policyFlow.length - 1
                          ? 'Policy output is handed to the Control Engine for a controlled decision.'
                          : 'The next policy gate depends on this deterministic result.'}
                      </span>
                    </div>
                    <span className="status-pill">Policy gate</span>
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
                  <h2>Policy routing</h2>
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
                  <p className="eyebrow">Policy outputs</p>
                  <h2>Required actions</h2>
                </div>
                <span className="module-tag">No blind approval</span>
              </div>

              <div className="account-list">
                {policyOutcomes.map((item) => (
                  <div className="account-row" key={item}>
                    <div>
                      <strong>{item}: </strong>
                      <span>Deterministic prototype policy output.</span>
                    </div>
                    <span className="status-pill">Required</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Safety boundary</p>
                  <h2>Prototype-only policy layer</h2>
                </div>
              </div>

              <p className="panel-note">
                Local deterministic policy engine interface only. No real
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
