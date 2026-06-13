import { type FormEvent, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { LanguageToggle } from '../components/LanguageToggle'
import { Panel } from '../components/Panel'
import { useLanguage } from '../context/LanguageContext'
import {
  approveMobileLogin,
  loginToBank,
  type AuthCustomerInfo,
} from '../services/authApi'

type LoginStep = 'credentials' | 'approval'

export function BankLoginPage() {
  const navigate = useNavigate()
  const { t } = useLanguage()
  const [step, setStep] = useState<LoginStep>('credentials')
  const [challengeId, setChallengeId] = useState<string | null>(null)
  const [customer, setCustomer] = useState<AuthCustomerInfo | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  async function handleCredentialsSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const form = new FormData(event.currentTarget)
    const bankUserId = String(form.get('bankUserId') ?? '')
    const pin = String(form.get('pin') ?? '')
    event.currentTarget.reset()

    setIsSubmitting(true)
    setError(null)

    try {
      const response = await loginToBank({
        bank_user_id: bankUserId,
        pin,
      })

      if (
        response.status === 'pending_mobile_approval' &&
        response.challenge_id
      ) {
        setChallengeId(response.challenge_id)
        setCustomer(response.customer)
        setStep('approval')
      } else {
        setError(response.message)
      }
    } catch {
      setError(
        'Simulated bank login service is unavailable. No session was created.',
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleMobileApproval(approved: boolean) {
    if (!challengeId) {
      setStep('credentials')
      setError('Login approval request is unavailable. Please start again.')
      return
    }

    setIsSubmitting(true)
    setError(null)

    try {
      const response = await approveMobileLogin({
        challenge_id: challengeId,
        approved,
      })

      if (
        approved &&
        response.status === 'authenticated' &&
        response.session_id
      ) {
        const redirectTo =
          response.redirect_to === '/' ? '/dashboard' : response.redirect_to
        localStorage.setItem('aurora_bank_session_id', response.session_id)
        navigate(redirectTo, { replace: true })
        return
      }

      setChallengeId(null)
      setCustomer(null)
      setStep('credentials')
      setError(approved ? response.message : null)
    } catch {
      setError(
        'Simulated mobile key approval is unavailable. No session was created.',
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="bank-shell">
      <header className="top-bar">
        <Link className="brand" to="/" aria-label="Go to Aurora Bank home">
          <div className="brand-mark">A</div>
          <div>
            <p className="brand-name">Aurora Bank</p>
            <p className="brand-subtitle">{t.bankLogin.securePrototype}</p>
          </div>
        </Link>

        <div></div>

        <div className="user-area">
          <LanguageToggle />
          <span>{t.bankLogin.simulatedAccess}</span>
        </div>
      </header>

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.bankLogin.bankManagedAccess}</p>
            <h1>{t.bankLogin.title}</h1>
            <p>{t.bankLogin.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankLogin.simulatedSignIn}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              {step === 'credentials' && (
                <>
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">{t.bankLogin.stepOne}</p>
                      <h2>{t.bankLogin.credentials}</h2>
                    </div>
                    <span className="module-tag">{t.bankLogin.bankIssuedAccess}</span>
                  </div>

                  <p>{t.bankLogin.credentialsHelp}</p>

                  <form className="form-grid" onSubmit={handleCredentialsSubmit}>
                    <label>
                      {t.bankLogin.customerId}
                      <input
                        type="text"
                        name="bankUserId"
                        autoComplete="off"
                        required
                      />
                    </label>

                    <label>
                      {t.bankLogin.secretCredential}
                      <input
                        type="password"
                        name="pin"
                        autoComplete="off"
                        required
                      />
                    </label>

                    <p className="panel-note">
                      Demo credentials: customer ID 12345678 and PIN 1234.
                      Entered values are sent only to this local prototype
                      backend and are not stored by the page.
                    </p>

                    {error && <p className="field-warning">{error}</p>}

                    <div className="action-row">
                      <button type="submit" disabled={isSubmitting}>
                        {isSubmitting ? t.bankLogin.checking : t.common.continue}
                      </button>
                    </div>
                  </form>
                </>
              )}

              {step === 'approval' && (
                <>
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">{t.bankLogin.stepTwo}</p>
                      <h2>{t.bankLogin.confirmMobileKey}</h2>
                    </div>
                    <span className="module-tag">
                      {t.bankLogin.strongAuthentication}
                    </span>
                  </div>

                  <p>{t.bankLogin.mobileApprovalSent}</p>

                  <div className="summary-list">
                    <div>
                      <span>{t.bankLogin.action}</span>
                      <strong>{t.bankLogin.loginRequest}</strong>
                    </div>
                    <div>
                      <span>{t.bankLogin.service}</span>
                      <strong>Aurora eBanking</strong>
                    </div>
                    {customer && (
                      <div>
                        <span>{t.bankLogin.customer}</span>
                        <strong>{customer.customer_name}</strong>
                      </div>
                    )}
                    <div>
                      <span>{t.bankLogin.approvalMethod}</span>
                      <strong>{t.bankLogin.deviceApprovalRequired}</strong>
                    </div>
                    <div>
                      <span>{t.bankLogin.timeLimit}</span>
                      <strong>{t.bankLogin.sessionExpires}</strong>
                    </div>
                  </div>

                  {error && <p className="field-warning">{error}</p>}

                  <div className="action-row">
                    <button
                      type="button"
                      disabled={isSubmitting}
                      onClick={() => void handleMobileApproval(true)}
                    >
                      {isSubmitting
                        ? t.bankLogin.processingApproval
                        : t.bankLogin.approveLogin}
                    </button>
                    <button
                      type="button"
                      className="secondary-button"
                      disabled={isSubmitting}
                      onClick={() => void handleMobileApproval(false)}
                    >
                      {t.common.cancel}
                    </button>
                  </div>
                </>
              )}
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.bankLogin.securityNote}</p>
              <h2>{t.bankLogin.protectIdentifiers}</h2>
              <p>{t.bankLogin.protectIdentifiersCopy}</p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.bankLogin.onboardingBoundary}</p>
              <h2>{t.bankLogin.bankManagedOnboarding}</h2>

              <div className="check-list">
                {t.bankLogin.onboardingItems.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.bankLogin.productBoundary}</p>
              <h2>{t.bankLogin.prototypeOnly}</h2>
              <p>
                This prototype does not implement real authentication. It uses
                only simulated authentication records, does not verify real
                credentials, does not connect to bank identity systems or a
                real mobile key, and does not create customer accounts.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. Use fictional information only. No
          real credentials, authentication requests, accounts, or banking
          systems are used.
        </section>
      </main>
    </div>
  )
}
