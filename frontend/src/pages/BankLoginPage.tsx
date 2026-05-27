import { type FormEvent, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Panel } from '../components/Panel'
import {
  approveMobileLogin,
  loginToBank,
  type AuthCustomerInfo,
} from '../services/authApi'

type LoginStep = 'credentials' | 'approval'

const onboardingItems = [
  'Customer onboarded by bank',
  'Documents reviewed by bank',
  'Source of funds reviewed by bank',
  'Credentials issued by bank',
  'Strong authentication required',
]

export function BankLoginPage() {
  const navigate = useNavigate()
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
            <p className="brand-subtitle">Secure eBanking prototype</p>
          </div>
        </Link>

        <div></div>

        <div className="user-area">
          <span>Simulated banking access</span>
        </div>
      </header>

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Bank-managed access</p>
            <h1>Log on to Aurora eBanking</h1>
            <p>
              Access to Aurora Digital Assets is modelled as available only
              after the bank has established an authenticated customer session
              and confirmed eligibility.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Simulated sign-in
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              {step === 'credentials' && (
                <>
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">Step 1 of 2</p>
                      <h2>Credentials</h2>
                    </div>
                    <span className="module-tag">Bank-issued access</span>
                  </div>

                  <p>
                    Use the bank-issued customer identifier and secret
                    credential provided through the bank&apos;s formal onboarding
                    process.
                  </p>

                  <form className="form-grid" onSubmit={handleCredentialsSubmit}>
                    <label>
                      Customer ID
                      <input
                        type="text"
                        name="bankUserId"
                        autoComplete="off"
                        required
                      />
                    </label>

                    <label>
                      Secret credential
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
                        {isSubmitting ? 'Checking...' : 'Continue'}
                      </button>
                    </div>
                  </form>
                </>
              )}

              {step === 'approval' && (
                <>
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">Step 2 of 2</p>
                      <h2>Confirm with mobile key</h2>
                    </div>
                    <span className="module-tag">Strong authentication</span>
                  </div>

                  <p>
                    A simulated approval request has been sent to the
                    customer&apos;s banking authentication application.
                  </p>

                  <div className="summary-list">
                    <div>
                      <span>Action</span>
                      <strong>Login request</strong>
                    </div>
                    <div>
                      <span>Service</span>
                      <strong>Aurora eBanking</strong>
                    </div>
                    {customer && (
                      <div>
                        <span>Customer</span>
                        <strong>{customer.customer_name}</strong>
                      </div>
                    )}
                    <div>
                      <span>Approval method</span>
                      <strong>Device approval required</strong>
                    </div>
                    <div>
                      <span>Time limit</span>
                      <strong>Session expires in 02:00</strong>
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
                        ? 'Processing approval...'
                        : 'Approve simulated login'}
                    </button>
                    <button
                      type="button"
                      className="secondary-button"
                      disabled={isSubmitting}
                      onClick={() => void handleMobileApproval(false)}
                    >
                      Cancel
                    </button>
                  </div>
                </>
              )}
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Security note</p>
              <h2>Protect your identifiers</h2>
              <p>
                The bank never asks for your identifiers by email or text
                message. Always access eBanking through the official banking
                channel.
              </p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Onboarding boundary</p>
              <h2>Bank-managed onboarding</h2>

              <div className="check-list">
                {onboardingItems.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Product boundary</p>
              <h2>Prototype only</h2>
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
