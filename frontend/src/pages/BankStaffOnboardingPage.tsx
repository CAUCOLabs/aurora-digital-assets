import { useEffect, useState } from 'react'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  getBankStaffCustomerRecord,
  getBankStaffOnboardingModel,
  type BankCustomerRecordResponse,
  type BankStaffOnboardingModelResponse,
} from '../services/bankStaffApi'

const fallbackOnboardingModel: BankStaffOnboardingModelResponse = {
  title: 'Bank staff customer onboarding model',
  description:
    'Aurora Digital Assets assumes that the customer is created through a formal bank-managed onboarding process before any online banking or digital asset services are available.',
  onboarding_steps: [
    {
      step_id: 'A',
      title: 'Identity and document review',
      description:
        'Bank staff review identity documents and customer information before access is available.',
      performed_by: 'Bank staff',
      status: 'Required',
      evidence_required: [
        'Passport or national identity document',
        'Personal identity information',
        'Contact information',
      ],
    },
    {
      step_id: 'F',
      title: 'Private PIN / secret credential setup',
      description:
        'The customer defines the secret credential privately and staff do not see it.',
      performed_by: 'Customer',
      status: 'Private customer action',
      evidence_required: [
        'Customer enters PIN privately',
        'Staff must not see the secret credential',
        'Credential is not displayed back to staff',
      ],
    },
    {
      step_id: 'H',
      title: 'Digital Assets eligibility check',
      description:
        'Eligibility is evaluated after bank-managed controls are completed.',
      performed_by: 'Bank system / Compliance',
      status: 'Conditional',
      evidence_required: [
        'Active banking relationship',
        'Identity verification completed',
        'Source-of-funds reviewed',
        'Strong authentication enabled',
      ],
    },
  ],
  credential_model: [
    'The bank issues the customer identifier.',
    'The customer defines the secret PIN or credential privately.',
    "Bank staff must not see or record the customer's secret credential.",
  ],
  strong_authentication_model: [
    'Strong authentication is required before accessing protected banking services.',
    'A simulated mobile key approval represents the second factor.',
  ],
  digital_assets_eligibility_model: [
    'Digital Assets access is available only after a valid banking relationship exists.',
    'Eligibility depends on completed identity verification and source-of-funds review.',
  ],
  boundary_note:
    'This prototype does not implement real customer onboarding, real identity verification, real credential issuance, real source-of-funds checks, or real strong authentication.',
}

const fallbackCustomerRecord: BankCustomerRecordResponse = {
  customer_id: 'CUST-DA-2026-001',
  bank_user_id: '12345678',
  name: 'Claudio Demo',
  relationship_status: 'Active',
  identity_verification_status: 'Completed by bank',
  residency_status: 'Finland resident',
  source_of_funds_status: 'Reviewed by bank',
  account_id: 'aurora-current',
  online_banking_enabled: true,
  strong_authentication_enabled: true,
  digital_assets_eligible: true,
  staff_review_status: 'Completed',
  notes: [
    'Customer relationship created through bank-managed onboarding.',
    'Online banking credentials issued by the bank.',
    'PIN setup is treated as a private customer action.',
    'Digital Assets access remains subject to eligibility and review controls.',
  ],
}

const staffControlledSteps = [
  'Identity and document review',
  'Residency and customer relationship review',
  'Income and source-of-funds review',
  'Account relationship creation',
]

const privateCustomerActions = [
  'Private PIN setup',
  'Secret credential remains hidden from staff',
  'Mobile approval completed by customer',
]

const eligibilityControls = [
  'Active banking relationship',
  'Identity verification completed',
  'Source-of-funds reviewed',
  'Strong authentication enabled',
]

const prototypeLimitations = [
  'No real onboarding',
  'No credential creation',
  'No identity verification',
  'No production strong authentication',
]

function formatBoolean(value: boolean) {
  return value ? 'Enabled' : 'Not enabled'
}

export function BankStaffOnboardingPage() {
  const [onboardingModel, setOnboardingModel] = useState(
    fallbackOnboardingModel,
  )
  const [customerRecord, setCustomerRecord] = useState(fallbackCustomerRecord)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchBankStaffModel() {
      setIsLoading(true)

      try {
        const [model, record] = await Promise.all([
          getBankStaffOnboardingModel(),
          getBankStaffCustomerRecord(),
        ])
        setOnboardingModel(model)
        setCustomerRecord(record)
        setBackendError(null)
      } catch {
        setOnboardingModel(fallbackOnboardingModel)
        setCustomerRecord(fallbackCustomerRecord)
        setBackendError(
          'Backend bank staff model unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchBankStaffModel()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Bank staff model</p>
            <h1>Bank Staff Onboarding Model</h1>
            <p>
              How a formal bank customer relationship is created before online
              banking and eligible digital asset services become available.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Deterministic prototype
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Customer onboarding flow</p>
                  <h2>{onboardingModel.title}</h2>
                </div>
                <span className="module-tag">
                  {backendError ? 'Local fallback' : 'Backend model'}
                </span>
              </div>

              {isLoading && (
                <p className="panel-note">Loading bank staff model...</p>
              )}
              {backendError && <p className="panel-note">{backendError}</p>}
              {!isLoading && !backendError && (
                <p className="panel-note">
                  Onboarding model loaded from local FastAPI prototype.
                </p>
              )}

              <p>{onboardingModel.description}</p>

              <div className="account-list">
                {onboardingModel.onboarding_steps.map((step) => (
                  <article className="account-row" key={step.step_id}>
                    <div>
                      <h3>
                        {step.step_id}. {step.title}
                      </h3>
                      <p>{step.description}</p>
                      <span>
                        Performed by: {step.performed_by} / Evidence:{' '}
                        {step.evidence_required.join(' / ')}
                      </span>
                    </div>
                    <strong>{step.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Demo customer record</p>
                  <h2>{customerRecord.name}</h2>
                </div>
                <span className="module-tag">
                  {customerRecord.staff_review_status}
                </span>
              </div>

              <div className="summary-list">
                <div>
                  <span>Customer ID</span>
                  <strong>{customerRecord.customer_id}</strong>
                </div>
                <div>
                  <span>Bank user ID</span>
                  <strong>{customerRecord.bank_user_id}</strong>
                </div>
                <div>
                  <span>Relationship status</span>
                  <strong>{customerRecord.relationship_status}</strong>
                </div>
                <div>
                  <span>Identity verification</span>
                  <strong>
                    {customerRecord.identity_verification_status}
                  </strong>
                </div>
                <div>
                  <span>Source of funds</span>
                  <strong>{customerRecord.source_of_funds_status}</strong>
                </div>
                <div>
                  <span>Online banking</span>
                  <strong>
                    {formatBoolean(customerRecord.online_banking_enabled)}
                  </strong>
                </div>
                <div>
                  <span>Strong authentication</span>
                  <strong>
                    {formatBoolean(
                      customerRecord.strong_authentication_enabled,
                    )}
                  </strong>
                </div>
                <div>
                  <span>Digital Assets eligible</span>
                  <strong>
                    {customerRecord.digital_assets_eligible ? 'Yes' : 'No'}
                  </strong>
                </div>
              </div>

              <ul className="notification-list">
                {customerRecord.notes.map((note) => (
                  <li key={note}>{note}</li>
                ))}
              </ul>
            </Panel>

            <Panel>
              <p className="eyebrow">Credential setup model</p>
              <h2>Private customer credential boundary</h2>
              <div className="check-list">
                {onboardingModel.credential_model.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Strong authentication model</p>
              <h2>Second factor before protected services</h2>
              <div className="check-list">
                {onboardingModel.strong_authentication_model.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Digital Assets eligibility</p>
              <h2>Access after bank-managed controls</h2>
              <div className="check-list">
                {onboardingModel.digital_assets_eligibility_model.map(
                  (item) => (
                    <div key={item}>
                      <span className="status-dot"></span>
                      {item}
                    </div>
                  ),
                )}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Boundary note</p>
              <h2>Prototype scope</h2>
              <p>{onboardingModel.boundary_note}</p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Staff-controlled steps</p>
              <h2>Bank-managed review</h2>
              <div className="check-list">
                {staffControlledSteps.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Private customer action</p>
              <h2>Credential secrecy</h2>
              <div className="check-list">
                {privateCustomerActions.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Digital assets eligibility</p>
              <h2>Conditional module access</h2>
              <div className="check-list">
                {eligibilityControls.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Prototype limitation</p>
              <h2>No production onboarding</h2>
              <div className="check-list">
                {prototypeLimitations.map((item) => (
                  <div key={item}>
                    <span className="warning-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}
