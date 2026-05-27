import { useEffect, useState } from 'react'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  getBankIntegrationModel,
  getBankSessionModel,
  type BankIntegrationModelResponse,
  type BankSessionModelResponse,
} from '../services/bankAccessApi'

const fallbackSessionModel: BankSessionModelResponse = {
  title: 'Bank-managed customer access',
  description:
    'Access is modelled as available only after a bank has established the customer relationship and authenticated session.',
  customer_access_steps: [
    'Customer is onboarded through the bank outside Aurora Digital Assets.',
    'The bank issues credentials and confirms sign-in using strong authentication.',
    'Eligible digital asset services become available after a valid banking session.',
  ],
  authentication_controls: [
    'Bank-issued credentials',
    'Strong authentication required',
  ],
  session_controls: [
    'No direct signup inside Aurora Digital Assets',
    'Sensitive activity can require review',
  ],
  boundary_note:
    'Aurora Digital Assets does not open accounts or authenticate customers. This page describes a simulated module boundary only.',
}

const fallbackIntegrationModel: BankIntegrationModelResponse = {
  title: 'Bank infrastructure integration model',
  description:
    'The concept places Aurora inside bank-managed channels, controls, and reporting boundaries.',
  integration_layers: [
    {
      name: 'Bank channels and session boundary',
      responsibility:
        'Provides authenticated access to eligible online banking modules.',
      examples: ['Online banking portal', 'Strong authentication'],
    },
    {
      name: 'Digital Assets module',
      responsibility:
        'Evaluates simulated digital asset actions and records prototype evidence.',
      examples: ['Audit events', 'Review cases'],
    },
  ],
  payment_rails_note:
    "Aurora Digital Assets does not connect directly to payment rails. Any real connections would be handled by the bank's existing infrastructure.",
  digital_assets_module_note:
    'This prototype evaluates digital asset flows without executing payments, transfers, or custody operations.',
  boundary_note:
    'No real authentication, payment clearing, settlement, custody, blockchain execution, or compliance screening is implemented.',
}

const relationshipModel = [
  'Customer onboarded by bank',
  'Credentials issued by bank',
  'Strong authentication required',
  'Aurora does not open accounts',
]

const integrationControls = [
  'API gateway concept',
  'Core banking boundary',
  'Audit events',
  'Review cases',
  'Reporting evidence',
]

const prototypeLimitations = [
  'No real authentication',
  'No real bank APIs',
  'No real payment rails',
  'No real custody',
  'No blockchain execution',
]

export function BankAccessPage() {
  const [sessionModel, setSessionModel] = useState(fallbackSessionModel)
  const [integrationModel, setIntegrationModel] = useState(
    fallbackIntegrationModel,
  )
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchBankAccessModel() {
      setIsLoading(true)

      try {
        const [session, integration] = await Promise.all([
          getBankSessionModel(),
          getBankIntegrationModel(),
        ])
        setSessionModel(session)
        setIntegrationModel(integration)
        setBackendError(null)
      } catch {
        setSessionModel(fallbackSessionModel)
        setIntegrationModel(fallbackIntegrationModel)
        setBackendError(
          'Backend bank access model unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchBankAccessModel()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Bank access model</p>
            <h1>Bank Access &amp; Infrastructure</h1>
            <p>
              Aurora Digital Assets is designed as a protected module inside a
              formal bank, available only after a banking relationship,
              eligibility checks, and authenticated access are established.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Bank-managed access
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Customer session</p>
                  <h2>{sessionModel.title}</h2>
                </div>
                <span className="module-tag">
                  {backendError ? 'Local fallback' : 'Backend model'}
                </span>
              </div>

              {isLoading && (
                <p className="panel-note">Loading bank access model...</p>
              )}
              {backendError && <p className="panel-note">{backendError}</p>}
              {!isLoading && !backendError && (
                <p className="panel-note">
                  Bank access model loaded from local FastAPI prototype.
                </p>
              )}

              <p>{sessionModel.description}</p>

              <ul className="notification-list">
                {sessionModel.customer_access_steps.map((step) => (
                  <li key={step}>{step}</li>
                ))}
              </ul>

              <div className="assets-summary">
                <div>
                  <p>Authentication controls</p>
                  <div className="check-list">
                    {sessionModel.authentication_controls.map((control) => (
                      <div key={control}>
                        <span className="status-dot"></span>
                        {control}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="custody-card">
                  <p>Session controls</p>
                  <div className="check-list">
                    {sessionModel.session_controls.map((control) => (
                      <div key={control}>
                        <span className="status-dot"></span>
                        {control}
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              <p className="panel-note">{sessionModel.boundary_note}</p>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Infrastructure</p>
                  <h2>{integrationModel.title}</h2>
                </div>
                <span className="module-tag">Integration boundary</span>
              </div>

              <p>{integrationModel.description}</p>

              <div className="account-list">
                {integrationModel.integration_layers.map((layer) => (
                  <article className="account-row" key={layer.name}>
                    <div>
                      <h3>{layer.name}</h3>
                      <p>{layer.responsibility}</p>
                      <span>{layer.examples.join(' / ')}</span>
                    </div>
                    <strong>Layer</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Payment rails boundary</p>
                  <h2>Handled by bank infrastructure</h2>
                </div>
              </div>
              <p>{integrationModel.payment_rails_note}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">Digital assets module boundary</p>
              <h2>Evaluation before hypothetical execution</h2>
              <p>{integrationModel.digital_assets_module_note}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">Product boundary</p>
              <h2>Prototype scope</h2>
              <p>{integrationModel.boundary_note}</p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Access prerequisite</p>
              <h2>Customer relationship model</h2>
              <div className="check-list">
                {relationshipModel.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Service boundary</p>
              <h2>Integration controls</h2>
              <div className="check-list">
                {integrationControls.map((control) => (
                  <div key={control}>
                    <span className="status-dot"></span>
                    {control}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Prototype limitation</p>
              <h2>Simulation only</h2>
              <div className="check-list">
                {prototypeLimitations.map((limitation) => (
                  <div key={limitation}>
                    <span className="warning-dot"></span>
                    {limitation}
                  </div>
                ))}
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This model does not imply production
          readiness and does not connect to real banking, payment, custody, or
          blockchain infrastructure.
        </section>
      </main>
    </div>
  )
}
