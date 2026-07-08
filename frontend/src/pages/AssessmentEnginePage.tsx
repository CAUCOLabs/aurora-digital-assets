import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const statusCards = [
  ['Mode', 'Local deterministic prototype'],
  ['Assessment scope', 'Readiness and gap analysis'],
  ['Real integrations', '0'],
  ['Real assets', '0'],
  ['External execution', 'Disabled'],
  ['Output', 'Review-ready assessment'],
]

const assessmentRows = [
  {
    name: 'Asset rail readiness',
    detail:
      'Assesses whether the asset type, settlement rail and custody model are clearly classified before controls apply.',
    score: '92',
    status: 'High',
  },
  {
    name: 'Regulatory mapping readiness',
    detail:
      'Checks whether regulatory concepts have been mapped into deterministic control requirements and evidence needs.',
    score: '88',
    status: 'High',
  },
  {
    name: 'Policy coverage',
    detail:
      'Evaluates whether internal policies cover custody, approvals, evidence, agents, risk thresholds and resilience.',
    score: '84',
    status: 'Medium',
  },
  {
    name: 'Control gate completeness',
    detail:
      'Assesses whether blocking, pause, remediation, review and controlled decision paths are defined.',
    score: '86',
    status: 'High',
  },
  {
    name: 'Evidence readiness',
    detail:
      'Checks whether audit-ready evidence packages, correlation IDs and review links are available.',
    score: '90',
    status: 'High',
  },
  {
    name: 'Human approval integrity',
    detail:
      'Assesses whether human review is controlled through dual control, conflict checks and post-review audit records.',
    score: '87',
    status: 'High',
  },
  {
    name: 'Agent governance readiness',
    detail:
      'Checks agent identity, permissions, revocation, policy controls, abuse detection and auditability.',
    score: '85',
    status: 'High',
  },
  {
    name: 'Operational resilience',
    detail:
      'Evaluates fallback modes, dependency failures, continuity controls and customer impact handling.',
    score: '82',
    status: 'Medium',
  },
]

const maturityLevels = [
  ['Initial', 'Controls exist as isolated concepts without consistent routing.'],
  ['Defined', 'Control requirements are documented and mapped to core workflows.'],
  ['Managed', 'Evidence, review paths and policy decisions are consistently generated.'],
  ['Measured', 'Scores, gaps and readiness levels are visible and comparable.'],
  ['Optimized', 'Continuous improvement loops update controls, evidence and review patterns.'],
]

const connectedModules = [
  ['Aurora Trust Engine', '/bank-staff/trust-engine'],
  ['Asset Rail Governance', '/bank-staff/asset-rail-governance'],
  ['Regulation Engine', '/bank-staff/regulation-engine'],
  ['Policy Engine', '/bank-staff/policy-engine'],
  ['Control Engine', '/bank-staff/control-engine'],
  ['Risk Operations', '/bank-staff/risk-operations'],
  ['Evidence Packages', '/bank-staff/evidence-packages'],
  ['Compliance Intelligence', '/bank-staff/compliance-intelligence'],
  ['Audit Trail', '/reports/audit-trail'],
]

const assessmentFlow = [
  'Scope',
  'Classification',
  'Control mapping',
  'Gap analysis',
  'Readiness score',
  'Evidence need',
  'Review recommendation',
  'Improvement loop',
]

const assessmentOutputs = [
  'Readiness score',
  'Maturity level',
  'Missing controls',
  'Evidence gaps',
  'Blocking risks',
  'Recommended next actions',
  'Review path',
  'Audit-ready summary',
]

export function AssessmentEnginePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Assessment Engine</p>
            <h1>Readiness, Gap & Maturity Assessment Layer</h1>
            <p>
              Evaluates control readiness, maturity, gaps, evidence needs and
              review paths before sensitive banking or digital asset operations
              move into controlled decisioning.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Assessment model active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Assessment status</p>
                  <h2>Readiness boundary</h2>
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
                  <p className="eyebrow">Assessment matrix</p>
                  <h2>Readiness scores</h2>
                </div>
                <span className="module-tag">Deterministic scoring</span>
              </div>

              <div className="account-list">
                {assessmentRows.map((row) => (
                  <div className="account-row" key={row.name}>
                    <div>
                      <strong>{row.name}: {row.score}/100</strong>
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
                  <p className="eyebrow">Maturity model</p>
                  <h2>Control maturity levels</h2>
                </div>
                <span className="module-tag">Improvement loop</span>
              </div>

              <div className="account-list">
                {maturityLevels.map(([level, detail], index) => (
                  <div className="account-row" key={level}>
                    <div>
                      <strong>{index + 1}. {level}: </strong>
                      <span>{detail}</span>
                    </div>
                    <span className="status-pill">Level</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Assessment flow</p>
                  <h2>From scope to improvement loop</h2>
                </div>
                <span className="module-tag">Review-ready</span>
              </div>

              <div className="account-list">
                {assessmentFlow.map((step, index) => (
                  <div className="account-row" key={step}>
                    <div>
                      <strong>
                        {String(index + 1).padStart(2, '0')} — {step}:{' '}
                      </strong>
                      <span>
                        {index === assessmentFlow.length - 1
                          ? 'Assessment results feed continuous improvement and control refinement.'
                          : 'The assessment continues only after this readiness gate is checked.'}
                      </span>
                    </div>
                    <span className="status-pill">Assessment gate</span>
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
                  <h2>Assessment routing</h2>
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
                  <p className="eyebrow">Assessment outputs</p>
                  <h2>Review-ready results</h2>
                </div>
                <span className="module-tag">Evidence-aware</span>
              </div>

              <div className="account-list">
                {assessmentOutputs.map((item) => (
                  <div className="account-row" key={item}>
                    <div>
                      <strong>{item}: </strong>
                      <span>Deterministic prototype assessment output.</span>
                    </div>
                    <span className="status-pill">Generated</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Safety boundary</p>
                  <h2>Prototype-only assessment layer</h2>
                </div>
              </div>

              <p className="panel-note">
                Local deterministic assessment engine interface only. No real
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
