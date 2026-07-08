import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'

const decisionKeys = [
  'digital_euro_psp_controls_required',
  'central_bank_money_controls_required',
  'tokenized_deposit_bank_ledger_controls_required',
  'stablecoin_issuer_controls_required',
  'stablecoin_redemption_controls_required',
  'external_custodian_controls_required',
  'blockchain_execution_controls_required',
  'securities_controls_required',
  'unknown_asset_blocked_pending_classification',
] as const

const reviewLinks = [
  { key: 'evidencePackages', to: '/bank-staff/evidence-packages' },
  { key: 'riskOperations', to: '/bank-staff/risk-operations' },
  {
    key: 'humanApprovalIntegrity',
    to: '/bank-staff/human-approval-integrity',
  },
  { key: 'agentGovernance', to: '/bank-staff/agent-governance' },
  { key: 'cryptoAgility', to: '/bank-staff/crypto-agility' },
  { key: 'auditTrail', to: '/reports/audit-trail' },
] as const

export function AssetRailGovernancePage() {
  const { t } = useLanguage()
  const labels = t.assetRailGovernance

  const statusCards = [
    { label: labels.phase, value: '27' },
    { label: labels.mode, value: labels.localDeterministicPrototype },
    { label: labels.backendTests, value: labels.backendTestsPassing },
    { label: labels.realIntegrations, value: '0' },
    { label: labels.realAssets, value: '0' },
    { label: labels.externalExecution, value: labels.disabled },
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
            <Panel key={card.label} className="metric-card">
              <span>{card.label}</span>
              <strong>{card.value}</strong>
            </Panel>
          ))}
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.classificationEyebrow}</p>
                  <h2>{labels.classificationTitle}</h2>
                </div>
                <span className="module-tag">{labels.controlModelFirst}</span>
              </div>
              <p>{labels.classificationText}</p>

              <div className="account-list">
                {labels.rails.map((rail) => (
                  <article className="account-row" key={rail.name}>
                    <div>
                      <h3>{rail.name}</h3>
                      <p>
                        <strong>{labels.rail}</strong> {rail.rail}
                      </p>
                      <span>
                        {labels.custody}: {rail.custody}
                      </span>
                    </div>
                    <strong>{labels.classified}</strong>
                    <div className="summary-list financial-crime-alert-meta">
                      <div>
                        <span>{labels.controls}</span>
                        <strong>{rail.controls}</strong>
                      </div>
                    </div>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.decisionMatrixEyebrow}</p>
                  <h2>{labels.decisionMatrixTitle}</h2>
                </div>
                <span className="module-tag">{labels.deterministic}</span>
              </div>

              <div className="summary-list">
                {decisionKeys.map((key) => (
                  <div key={key}>
                    <span>{labels.required}</span>
                    <strong>{key}</strong>
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">{labels.coreMessage}</p>
              <h2>{labels.firstClassify}</h2>
              <p>{labels.coreMessageText}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.digitalEuroEyebrow}</p>
              <h2>{labels.digitalEuroTitle}</h2>
              <div className="check-list">
                {labels.digitalEuroPoints.map((point) => (
                  <div key={point}>
                    <span className="status-dot"></span>
                    {point}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.cryptoassetEyebrow}</p>
              <h2>{labels.cryptoassetTitle}</h2>
              <div className="check-list">
                {labels.cryptoassetPoints.map((point) => (
                  <div key={point}>
                    <span className="status-dot"></span>
                    {point}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.evidenceEyebrow}</p>
              <h2>{labels.evidenceTitle}</h2>
              <div className="action-row vertical-actions">
                {reviewLinks.map((link, index) => (
                  <Link
                    className={
                      index === 0
                        ? 'button-link'
                        : 'button-link secondary-button'
                    }
                    key={link.to}
                    to={link.to}
                  >
                    {labels.reviewLinks[link.key]}
                  </Link>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{labels.safetyNotice}</p>
              <h2>{labels.prototypeBoundary}</h2>
              <p>{labels.safetyNoticeText}</p>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">{labels.safetyNoticeText}</p>
      </main>
    </div>
  )
}
