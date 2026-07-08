import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const statusCards = [
  ['Mode', 'Local deterministic prototype'],
  ['Knowledge scope', 'Institutional control logic'],
  ['Real integrations', '0'],
  ['Real assets', '0'],
  ['External execution', 'Disabled'],
  ['Output', 'Explainable knowledge map'],
]

const knowledgeRows = [
  {
    name: 'Regulatory knowledge',
    detail:
      'Organizes regulatory concepts such as digital euro, CBDC, stablecoins, asset-referenced tokens, cryptoassets and securities controls.',
    status: 'Mapped',
  },
  {
    name: 'Control knowledge',
    detail:
      'Preserves how Aurora maps requirements into policies, evidence, review paths and controlled decision boundaries.',
    status: 'Structured',
  },
  {
    name: 'Risk knowledge',
    detail:
      'Connects operational, custody, asset rail, approval, agent and resilience risk patterns into reusable internal logic.',
    status: 'Reusable',
  },
  {
    name: 'Evidence knowledge',
    detail:
      'Links audit events, evidence packages, correlation IDs, review cases and decision records into explainable context.',
    status: 'Traceable',
  },
  {
    name: 'Policy knowledge',
    detail:
      'Documents which internal policies apply to each asset rail, operation type, review path and control threshold.',
    status: 'Policy-aware',
  },
  {
    name: 'Assessment knowledge',
    detail:
      'Preserves readiness scores, maturity levels, evidence gaps, missing controls and improvement recommendations.',
    status: 'Assessment-ready',
  },
  {
    name: 'Agent knowledge',
    detail:
      'Connects agent identity, permissions, revocation, abuse detection, passport and audit controls.',
    status: 'Agent-aware',
  },
  {
    name: 'Human review knowledge',
    detail:
      'Keeps institutional logic for dual control, segregation of duties, reviewer conflicts and approval integrity.',
    status: 'Integrity-aware',
  },
]

const knowledgeFlow = [
  'Signal context',
  'Asset rail knowledge',
  'Regulatory concept',
  'Internal policy logic',
  'Control requirement',
  'Evidence context',
  'Review explanation',
  'Institutional memory',
]

const connectedModules = [
  ['Aurora Trust Engine', '/bank-staff/trust-engine'],
  ['Asset Rail Governance', '/bank-staff/asset-rail-governance'],
  ['Regulation Engine', '/bank-staff/regulation-engine'],
  ['Policy Engine', '/bank-staff/policy-engine'],
  ['Assessment Engine', '/bank-staff/assessment-engine'],
  ['Control Engine', '/bank-staff/control-engine'],
  ['Risk Operations', '/bank-staff/risk-operations'],
  ['Evidence Packages', '/bank-staff/evidence-packages'],
  ['Compliance Intelligence', '/bank-staff/compliance-intelligence'],
  ['Audit Trail', '/reports/audit-trail'],
]

const knowledgeOutputs = [
  'Explainable decision context',
  'Reusable control logic',
  'Regulatory concept map',
  'Policy-to-control mapping',
  'Evidence relationship map',
  'Review guidance',
  'Audit-ready explanation',
  'Improvement memory',
]

export function KnowledgeEnginePage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Knowledge Engine</p>
            <h1>Institutional Knowledge & Explainability Layer</h1>
            <p>
              Preserves Aurora's institutional control logic by connecting
              regulatory concepts, policies, evidence, assessments, risk
              patterns and review decisions into explainable knowledge.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Knowledge model active
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Knowledge status</p>
                  <h2>Institutional memory boundary</h2>
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
                  <p className="eyebrow">Knowledge map</p>
                  <h2>Reusable institutional logic</h2>
                </div>
                <span className="module-tag">Explainability layer</span>
              </div>

              <div className="account-list">
                {knowledgeRows.map((row) => (
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
                  <p className="eyebrow">Knowledge flow</p>
                  <h2>From signal context to institutional memory</h2>
                </div>
                <span className="module-tag">Decision explainability</span>
              </div>

              <div className="account-list">
                {knowledgeFlow.map((step, index) => (
                  <div className="account-row" key={step}>
                    <div>
                      <strong>
                        {String(index + 1).padStart(2, '0')} — {step}:{' '}
                      </strong>
                      <span>
                        {index === knowledgeFlow.length - 1
                          ? 'The knowledge output preserves explainable institutional context for future review.'
                          : 'Aurora links this knowledge element to the next governance layer.'}
                      </span>
                    </div>
                    <span className="status-pill">Knowledge node</span>
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
                  <h2>Knowledge routing</h2>
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
                  <p className="eyebrow">Knowledge outputs</p>
                  <h2>Explainable results</h2>
                </div>
                <span className="module-tag">Audit-ready context</span>
              </div>

              <div className="account-list">
                {knowledgeOutputs.map((item) => (
                  <div className="account-row" key={item}>
                    <div>
                      <strong>{item}: </strong>
                      <span>Deterministic prototype knowledge output.</span>
                    </div>
                    <span className="status-pill">Available</span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Safety boundary</p>
                  <h2>Prototype-only knowledge layer</h2>
                </div>
              </div>

              <p className="panel-note">
                Local deterministic knowledge engine interface only. No real
                legal advice, regulatory certification, banking, custody, PSP,
                digital euro, CBDC, stablecoin, cryptoasset, blockchain, cloud,
                payment, settlement, transfer, customer data, private key,
                credential or secret is used or executed.
              </p>
            </Panel>
          </div>
        </section>
      </main>
    </div>
  )
}
