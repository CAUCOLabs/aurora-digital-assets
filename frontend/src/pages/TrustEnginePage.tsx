import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'

const connectedModuleLinks = [
  { key: 'assetRailGovernance', to: '/bank-staff/asset-rail-governance' },
  { key: 'riskOperations', to: '/bank-staff/risk-operations' },
  { key: 'evidencePackages', to: '/bank-staff/evidence-packages' },
  {
    key: 'complianceIntelligence',
    to: '/bank-staff/compliance-intelligence',
  },
  {
    key: 'humanApprovalIntegrity',
    to: '/bank-staff/human-approval-integrity',
  },
  { key: 'agentGovernance', to: '/bank-staff/agent-governance' },
  { key: 'cryptoAgility', to: '/bank-staff/crypto-agility' },
  { key: 'auditTrail', to: '/reports/audit-trail' },
] as const

export function TrustEnginePage() {
  const { t } = useLanguage()
  const labels = t.trustEngine

  const statusCards = [
    { label: labels.mode, value: labels.localDeterministicPrototype },
    { label: labels.realIntegrations, value: '0' },
    { label: labels.realAssets, value: '0' },
    { label: labels.externalExecution, value: labels.disabled },
    { label: labels.evidence, value: labels.reviewable },
    { label: labels.controlModel, value: labels.layered },
  ]

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{labels.eyebrow}</p>
            <h1>{labels.title}</h1>
            <p>{labels.subtitle}</p>
          </div>
          <Link className="button-link secondary-button" to="/bank-staff">
            {t.common.back}
          </Link>
        </section>

        <section className="metric-grid">
          {statusCards.map((card) => (
            <Panel className="metric-card" key={card.label}>
              <span>{card.label}:</span>
              <strong>{card.value}</strong>
            </Panel>
          ))}
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.orchestrationMap}</p>
                  <h2>{labels.trustEngineMap}</h2>
                </div>
                <span className="module-tag">{labels.sharedLayer}</span>
              </div>
              <p>{labels.coreMessage}</p>

              <div className="account-list">
                {labels.engineRows.map((engine) => (
                  <article className="account-row" key={engine.name}>
                    <div>
                      <h3>{engine.name}</h3>
                      <p>{engine.description}</p>
                    </div>
                    <strong>{labels.coordinated}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.connectedAurora}</p>
                  <h2>{labels.connectedModules}</h2>
                </div>
                <span className="module-tag">{labels.reviewLinks}</span>
              </div>

              <div className="account-list">
                {connectedModuleLinks.map((module) => (
                  <Link className="account-row" key={module.to} to={module.to}>
                    <div>
                      <h3>{labels.connectedLinks[module.key]}</h3>
                      <p>{module.to}</p>
                    </div>
                    <strong>{labels.open}</strong>
                  </Link>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">{labels.corePrinciple}</p>
              <h2>{labels.beforeSensitiveDecision}</h2>
              <p>{labels.coreMessage}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.deterministicFlow}</p>
              <h2>{labels.trustFlow}</h2>
              <div className="summary-list">
                {labels.trustFlowSteps.map((step, index) => (
                  <div key={step}>
                    <span>{labels.step} {index + 1}</span>
                    <strong>{step}</strong>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{labels.safetyBoundary}</p>
              <h2>{labels.prototypeBoundary}</h2>
              <p>{labels.safetyBoundaryText}</p>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">{labels.safetyBoundaryText}</p>
      </main>
    </div>
  )
}
