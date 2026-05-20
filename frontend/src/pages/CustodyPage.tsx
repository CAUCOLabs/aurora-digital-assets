import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import {
  getCustodyStatus,
  type CustodyStatus,
} from '../services/digitalAssetsApi'

const fallbackCustodyStatus: CustodyStatus = {
  custodyMode: 'Internal custodial wallet concept',
  privateKeysExposed: false,
  assetsSeparateFromDeposits: true,
  auditTrailEnabled: true,
  externalWithdrawalsRequireReview: true,
  userMessage:
    'Digital assets are visible inside online banking, but the user does not manage private keys directly in this prototype.',
  controls: [
    'Strong authentication active',
    'User does not manage private keys',
    'Audit trail enabled',
    'External withdrawals require review',
    'Digital assets are separate from deposits',
  ],
}

const custodyEvents = [
  {
    title: 'Asset credited to internal wallet',
    detail: 'BTC purchase reflected in the simulated custodial wallet.',
    status: 'Recorded',
  },
  {
    title: 'Custody status shown to user',
    detail: 'User can see that assets are separate from bank deposits.',
    status: 'Visible',
  },
  {
    title: 'External withdrawal request',
    detail: 'Transfer request creates a reviewable audit event.',
    status: 'Pending review',
  },
]

function getCustodyQuestions(custodyStatus: CustodyStatus) {
  return [
    {
      question: 'Who holds the asset?',
      answer: `In this prototype, assets are shown inside the banking interface through the ${custodyStatus.custodyMode.toLowerCase()}.`,
    },
    {
      question: 'Does the user manage private keys?',
      answer: custodyStatus.privateKeysExposed
        ? 'This prototype status indicates private key exposure, which would require additional user warnings and controls.'
        : 'No. In this prototype, the user does not see seed phrases or sign blockchain transactions manually.',
    },
    {
      question: 'Can the user withdraw externally?',
      answer: custodyStatus.externalWithdrawalsRequireReview
        ? 'Yes, but external withdrawals are treated as higher-risk actions and require review before completion in this prototype.'
        : 'External withdrawal review is not marked as active in the current prototype status.',
    },
  ]
}

function getStatusItems(custodyStatus: CustodyStatus) {
  return [
    {
      label: 'Digital assets visible in banking UI',
      active: true,
      warning: false,
    },
    {
      label: custodyStatus.privateKeysExposed
        ? 'Private keys exposed to user'
        : 'User does not manage private keys',
      active: !custodyStatus.privateKeysExposed,
      warning: custodyStatus.privateKeysExposed,
    },
    {
      label: 'Digital assets are separate from deposits',
      active: custodyStatus.assetsSeparateFromDeposits,
      warning: true,
    },
    {
      label: 'Audit trail enabled',
      active: custodyStatus.auditTrailEnabled,
      warning: false,
    },
    {
      label: 'External withdrawals require review',
      active: custodyStatus.externalWithdrawalsRequireReview,
      warning: true,
    },
  ]
}

export function CustodyPage() {
  const [custodyStatus, setCustodyStatus] = useState<CustodyStatus | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  const visibleCustodyStatus = custodyStatus ?? fallbackCustodyStatus
  const custodyQuestions = getCustodyQuestions(visibleCustodyStatus)
  const statusItems = getStatusItems(visibleCustodyStatus)

  useEffect(() => {
    async function fetchCustodyStatus() {
      setIsLoading(true)

      try {
        const status = await getCustodyStatus()
        setCustodyStatus(status)
        setBackendError(null)
      } catch {
        setCustodyStatus(null)
        setBackendError(
          'Backend custody data unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchCustodyStatus()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Custody model</p>
            <h1>Who controls what?</h1>
            <p>
              Understand how the Aurora Digital Assets concept explains custody,
              private keys, bank-side protection, and external wallet risk.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Custody transparency
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Internal custodial wallet concept</h2>
                </div>
                <span className="module-tag">v0.2 concept</span>
              </div>

              {isLoading && <p className="panel-note">Loading custody data...</p>}
              {backendError ? (
                <p className="panel-note">{backendError}</p>
              ) : (
                !isLoading && (
                  <p className="panel-note">
                    Custody status loaded from local FastAPI prototype.
                  </p>
                )
              )}

              <div className="assets-summary">
                <div>
                  <p>Custody model</p>
                  <strong>{visibleCustodyStatus.custodyMode}</strong>
                  <span>{visibleCustodyStatus.userMessage}</span>
                </div>

                <div className="custody-card">
                  <p>Product boundary</p>
                  <strong>
                    {visibleCustodyStatus.assetsSeparateFromDeposits
                      ? 'Separate from bank deposits'
                      : 'Deposit boundary not confirmed'}
                  </strong>
                  <span>
                    Digital assets can lose value and are not presented as
                    deposit-like products in this prototype.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Custody clarity</p>
                  <h2>Questions the interface should answer</h2>
                </div>
              </div>

              <div className="account-list">
                {custodyQuestions.map((item) => (
                  <article className="account-row" key={item.question}>
                    <div>
                      <h3>{item.question}</h3>
                      <p>{item.answer}</p>
                      <span>Customer-facing explanation</span>
                    </div>
                    <strong>Clear</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Risk boundary</p>
                  <h2>External wallet transfer changes responsibility</h2>
                </div>
                <Link className="button-link secondary-button" to="/withdrawals">
                  Go to withdrawals
                </Link>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Inside banking environment</p>
                  <strong>
                    {visibleCustodyStatus.auditTrailEnabled
                      ? 'Controls active'
                      : 'Controls not confirmed'}
                  </strong>
                  <span>
                    Authentication, monitoring, reporting, support processes,
                    withdrawal review, and audit trail concepts may apply in
                    this prototype.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Outside banking environment</p>
                  <strong>
                    {visibleCustodyStatus.externalWithdrawalsRequireReview
                      ? 'Review required before transfer'
                      : 'User responsibility increases'}
                  </strong>
                  <span>
                    Wrong addresses, private key loss, scams, or incompatible
                    networks may be difficult or impossible to recover.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Audit trail</p>
                  <h2>Custody-related evidence</h2>
                </div>
                <span className="module-tag">Deterministic log</span>
              </div>

              <div className="account-list">
                {custodyEvents.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Custody status</p>
              <h2>What the user sees</h2>

              <div className="check-list">
                {statusItems.map((item) => (
                  <div key={item.label}>
                    <span
                      className={
                        item.warning || !item.active
                          ? 'warning-dot'
                          : 'status-dot'
                      }
                    ></span>
                    {item.label}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Backend controls</p>
              <h2>Controls</h2>

              <div className="check-list">
                {visibleCustodyStatus.controls.map((control) => (
                  <div key={control}>
                    <span
                      className={
                        control.toLowerCase().includes('separate')
                          ? 'warning-dot'
                          : 'status-dot'
                      }
                    ></span>
                    {control}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Important boundary</p>
              <h2>External transfers are different</h2>
              <p>
                When assets leave the bank-integrated environment, the user may
                lose access to bank-side controls such as withdrawal review,
                support workflows, and organized reporting.
              </p>
              <p>{visibleCustodyStatus.userMessage}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">User responsibilities</p>
              <h2>Before self-custody</h2>

              <ul className="notification-list">
                <li>Understand who controls the external wallet.</li>
                <li>Verify the destination address and network.</li>
                <li>Store seed phrases or private keys safely.</li>
                <li>Understand that blockchain transfers are irreversible.</li>
              </ul>
            </Panel>

            <Panel>
              <p className="eyebrow">Related actions</p>
              <h2>Continue</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Reports
                </Link>
                <Link className="button-link secondary-button" to="/wallet">
                  Wallet
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page describes a fictional custody
          model and does not provide real custody services, banking services, or
          financial advice.
        </section>
      </main>
    </div>
  )
}
