import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'

const outputKeys = [
  'required_control_domains',
  'evidence_required',
  'review_required',
  'blocking_reasons',
  'recommended_next_actions',
  'governance_decision',
  'audit_event_id',
  'correlation_id',
] as const

const connectedModuleLinks = [
  { key: 'assetRailGovernance', to: '/bank-staff/asset-rail-governance' },
  { key: 'trustEngine', to: '/bank-staff/trust-engine' },
  {
    key: 'complianceIntelligence',
    to: '/bank-staff/compliance-intelligence',
  },
  { key: 'evidencePackages', to: '/bank-staff/evidence-packages' },
  { key: 'riskOperations', to: '/bank-staff/risk-operations' },
  {
    key: 'humanApprovalIntegrity',
    to: '/bank-staff/human-approval-integrity',
  },
  { key: 'auditTrail', to: '/reports/audit-trail' },
] as const

export function RegulationEnginePage() {
  const { t } = useLanguage()
  const labels = t.regulationEngine

  const statusCards = [
    { label: labels.mode, value: labels.localDeterministicPrototype },
    { label: labels.legalAdvice, value: labels.disabled },
    { label: labels.regulatoryCertification, value: labels.notProvided },
    { label: labels.realIntegrations, value: '0' },
    { label: labels.evidence, value: labels.required },
    { label: labels.review, value: labels.humanControlled },
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
                  <p className="eyebrow">{labels.mappingEyebrow}</p>
                  <h2>{labels.mappingMatrix}</h2>
                </div>
                <span className="module-tag">{labels.controlMapping}</span>
              </div>
              <p>{labels.coreMessage}</p>

              <div className="account-list">
                {labels.mappingRows.map((row) => (
                  <article className="account-row" key={row.name}>
                    <div>
                      <h3>{row.name}</h3>
                      <p>
                        <strong>{labels.regulatoryConcept}:</strong>{' '}
                        {row.regulatoryConcept}
                      </p>
                      <span>
                        {labels.controlRequirements}: {row.controlRequirements}
                      </span>
                    </div>
                    <strong>{labels.mapped}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.outputsEyebrow}</p>
                  <h2>{labels.controlRequirementOutputs}</h2>
                </div>
                <span className="module-tag">{labels.deterministic}</span>
              </div>

              <div className="summary-list">
                {outputKeys.map((key) => (
                  <div key={key}>
                    <span>{labels.output}</span>
                    <strong>{key}</strong>
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">{labels.corePrinciple}</p>
              <h2>{labels.noLegalAdvice}</h2>
              <p>{labels.coreMessage}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.connectedModulesEyebrow}</p>
              <h2>{labels.connectedModules}</h2>
              <div className="action-row vertical-actions">
                {connectedModuleLinks.map((module, index) => (
                  <Link
                    className={
                      index === 0
                        ? 'button-link'
                        : 'button-link secondary-button'
                    }
                    key={module.to}
                    to={module.to}
                  >
                    {labels.connectedLinks[module.key]}
                  </Link>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.deterministicFlow}</p>
              <h2>{labels.regulationToControlFlow}</h2>
              <div className="summary-list">
                {labels.flowSteps.map((step, index) => (
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
