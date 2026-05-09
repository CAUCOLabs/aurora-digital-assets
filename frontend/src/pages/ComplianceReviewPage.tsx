import { useEffect, useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import {
  listAuditEvents,
  listReviewCases,
  recordReviewerDecision,
  type AuditEvent,
  type ReviewCase,
} from '../services/complianceApi'

type ReviewerDecision =
  | 'Approve'
  | 'Reject'
  | 'Request information'
  | 'Escalate'

type LocalReviewCase = {
  case_id: string
  case_type: string
  title: string
  detail: string
  status: string
  risk_level: string
  customer: string
  asset: string
  amount: number
  network: string
  reasons: string[]
}

const reviewQueue = [
  {
    case_id: 'CASE-DA-2026-001',
    case_type: 'external_withdrawal_review',
    title: 'External BTC withdrawal',
    detail: 'Pending review',
    status: 'Pending review',
    risk_level: 'medium',
    customer: 'Claudio Demo',
    asset: 'BTC',
    amount: 0.001,
    network: 'Bitcoin',
    reasons: ['New wallet address', 'External transfer requested'],
  },
  {
    case_id: 'CASE-DA-2026-002',
    case_type: 'external_withdrawal_review',
    title: 'New external wallet address',
    detail: 'Review required',
    status: 'Review required',
    risk_level: 'medium',
    customer: 'Claudio Demo',
    asset: 'ETH',
    amount: 0.05,
    network: 'Ethereum',
    reasons: ['Address review required'],
  },
  {
    case_id: 'CASE-DA-2026-003',
    case_type: 'digital_asset_payment_review',
    title: 'Digital asset invoice payment',
    detail: 'Recorded',
    status: 'Recorded',
    risk_level: 'low',
    customer: 'Claudio Demo',
    asset: 'EURD',
    amount: 120.45,
    network: 'banking settlement',
    reasons: ['Eligible business recipient'],
  },
  {
    case_id: 'CASE-DA-2026-004',
    case_type: 'digital_asset_payment_review',
    title: 'Large USDC payment',
    detail: 'Monitoring event',
    status: 'Monitoring event',
    risk_level: 'low',
    customer: 'Claudio Demo',
    asset: 'USDC',
    amount: 750,
    network: 'banking settlement',
    reasons: ['High value digital asset payment'],
  },
  {
    case_id: 'CASE-DA-2026-005',
    case_type: 'wallet_risk_review',
    title: 'Wallet risk check',
    detail: 'Escalated',
    status: 'Escalated',
    risk_level: 'high',
    customer: 'Claudio Demo',
    asset: 'BTC',
    amount: 0.002,
    network: 'Bitcoin',
    reasons: ['Wallet risk check enabled'],
  },
] satisfies LocalReviewCase[]

const evidenceTimeline = [
  {
    title: 'Customer authenticated',
    detail: 'Strong authentication event',
    status: 'Recorded',
  },
  {
    title: 'Digital Assets module accessed',
    detail: 'Customer entered digital assets area',
    status: 'Recorded',
  },
  {
    title: 'External withdrawal form opened',
    detail: 'Withdrawal flow started',
    status: 'Recorded',
  },
  {
    title: 'Destination address submitted',
    detail: 'External address captured for review',
    status: 'Recorded',
  },
  {
    title: 'Address review triggered',
    detail: 'Manual address review required',
    status: 'Pending',
  },
  {
    title: 'Case created',
    detail: 'Operational review case opened',
    status: 'Open',
  },
]

const monitoringSignals = [
  'New wallet address',
  'External transfer requested',
  'Amount within prototype limit',
  'Address review required',
  'Audit trail available',
]

export function ComplianceReviewPage() {
  const [selectedDecision, setSelectedDecision] =
    useState<ReviewerDecision | null>(null)
  const [reviewCases, setReviewCases] = useState<ReviewCase[]>([])
  const [auditEvents, setAuditEvents] = useState<AuditEvent[]>([])
  const [selectedCaseId, setSelectedCaseId] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isRecordingDecision, setIsRecordingDecision] = useState(false)
  const [backendUnavailable, setBackendUnavailable] = useState(false)
  const [reviewerMessage, setReviewerMessage] = useState<string | null>(null)

  const activeReviewCases = reviewCases.length > 0 ? reviewCases : reviewQueue
  const selectedCaseIdOrDefault =
    selectedCaseId ?? activeReviewCases[0]?.case_id ?? null
  const selectedCase =
    activeReviewCases.find(
      (reviewCase) => reviewCase.case_id === selectedCaseIdOrDefault,
    ) ??
    activeReviewCases[0]
  const activeEvidenceTimeline =
    auditEvents.length > 0
      ? auditEvents.map((event) => ({
          title: event.action_type.replaceAll('_', ' '),
          detail:
            event.user_message ??
            `${event.module} event ${event.event_id} recorded.`,
          status: event.status,
        }))
      : evidenceTimeline
  const activeMonitoringSignals = useMemo(() => {
    if (!selectedCase) return monitoringSignals
    const reasonSignals = selectedCase.reasons.map((reason) =>
      reason.replaceAll('_', ' '),
    )
    return reasonSignals.length > 0 ? reasonSignals : monitoringSignals
  }, [selectedCase])

  useEffect(() => {
    void fetchBackendReviewData()
  }, [])

  async function fetchBackendReviewData() {
    setIsLoading(true)

    try {
      const [cases, events] = await Promise.all([
        listReviewCases(),
        listAuditEvents(),
      ])
      setReviewCases(cases)
      setAuditEvents(events)
      setBackendUnavailable(false)
      setSelectedCaseId((currentCaseId) => currentCaseId ?? cases[0]?.case_id ?? null)
    } catch {
      setReviewCases([])
      setAuditEvents([])
      setBackendUnavailable(true)
    } finally {
      setIsLoading(false)
    }
  }

  async function handleReviewerDecision(
    nextDecision: ReviewerDecision,
    backendDecision: string,
  ) {
    setSelectedDecision(nextDecision)

    if (backendUnavailable || !selectedCase) {
      setReviewerMessage('Reviewer decision recorded in local prototype view.')
      return
    }

    setIsRecordingDecision(true)
    setReviewerMessage(null)

    try {
      const updatedCase = await recordReviewerDecision(selectedCase.case_id, {
        decision: backendDecision,
        notes: `Reviewer selected ${nextDecision}.`,
      })
      setSelectedCaseId(updatedCase.case_id)
      setReviewerMessage('Reviewer decision recorded.')
      await fetchBackendReviewData()
    } catch {
      setBackendUnavailable(true)
      setReviewerMessage(
        'Backend review data unavailable. Showing local prototype data.',
      )
    } finally {
      setIsRecordingDecision(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Internal review</p>
            <h1>Compliance review dashboard</h1>
            <p>
              Review simulated digital asset cases, withdrawal risk events,
              audit evidence, and human decision workflows.
            </p>
          </div>

          <div className="security-badge">
            <span className="warning-dot"></span>
            Internal concept
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Review queue</p>
                  <h2>Open review queue</h2>
                </div>
                <span className="module-tag">
                  {reviewCases.length > 0 ? 'Backend cases' : 'Simulated cases'}
                </span>
              </div>
              {isLoading && <p className="panel-note">Loading review data...</p>}
              {backendUnavailable && (
                <p className="panel-note">
                  Backend review data unavailable. Showing local prototype data.
                </p>
              )}

              <div className="account-list">
                {activeReviewCases.map((reviewCase) => (
                  <article
                    className="account-row"
                    key={reviewCase.case_id}
                    onClick={() => setSelectedCaseId(reviewCase.case_id)}
                  >
                    <div>
                      <h3>{reviewCase.title}</h3>
                      <p>
                        {'detail' in reviewCase
                          ? reviewCase.detail
                          : reviewCase.case_type.replaceAll('_', ' ')}
                      </p>
                      <span>{reviewCase.status}</span>
                    </div>
                    <strong>{reviewCase.risk_level} risk</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Evidence timeline</p>
                  <h2>Case evidence timeline</h2>
                </div>
                <span className="module-tag">Audit evidence</span>
              </div>

              <div className="account-list">
                {activeEvidenceTimeline.map((event) => (
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

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Monitoring signals</p>
                  <h2>Triggered signals</h2>
                </div>
              </div>

              <div className="check-list">
                {activeMonitoringSignals.map((signal) => (
                  <div key={signal}>
                    <span className="status-dot"></span>
                    {signal}
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Selected case</p>
              <h2>{selectedCase?.case_id ?? 'No case selected'}</h2>

              <div className="summary-list">
                <div>
                  <span>Case ID</span>
                  <strong>{selectedCase?.case_id ?? 'Not available'}</strong>
                </div>
                <div>
                  <span>Type</span>
                  <strong>
                    {selectedCase?.case_type.replaceAll('_', ' ') ??
                      'Not available'}
                  </strong>
                </div>
                <div>
                  <span>Customer</span>
                  <strong>{selectedCase?.customer ?? 'Not available'}</strong>
                </div>
                <div>
                  <span>Asset</span>
                  <strong>{selectedCase?.asset ?? 'Not available'}</strong>
                </div>
                <div>
                  <span>Amount</span>
                  <strong>
                    {selectedCase
                      ? `${selectedCase.amount} ${selectedCase.asset}`
                      : 'Not available'}
                  </strong>
                </div>
                <div>
                  <span>Network</span>
                  <strong>{selectedCase?.network ?? 'Not available'}</strong>
                </div>
                <div>
                  <span>Status</span>
                  <strong>{selectedCase?.status ?? 'Not available'}</strong>
                </div>
                <div>
                  <span>Risk score</span>
                  <strong>{selectedCase?.risk_level ?? 'Not available'}</strong>
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Reviewer actions</p>
              <h2>Decision workflow</h2>

              <div className="action-row vertical-actions">
                <button
                  type="button"
                  disabled={isRecordingDecision || !selectedCase}
                  onClick={() => handleReviewerDecision('Approve', 'approve')}
                >
                  Approve
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isRecordingDecision || !selectedCase}
                  onClick={() => handleReviewerDecision('Reject', 'reject')}
                >
                  Reject
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isRecordingDecision || !selectedCase}
                  onClick={() =>
                    handleReviewerDecision(
                      'Request information',
                      'request_information',
                    )
                  }
                >
                  Request information
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isRecordingDecision || !selectedCase}
                  onClick={() => handleReviewerDecision('Escalate', 'escalate')}
                >
                  Escalate
                </button>
              </div>

              <p className="panel-note">
                Reviewer decision:{' '}
                {selectedDecision ?? 'No decision selected'}
              </p>
              {reviewerMessage && (
                <p className="panel-note">{reviewerMessage}</p>
              )}
            </Panel>

            <Panel>
              <p className="eyebrow">Compliance controls</p>
              <h2>Controls active</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Transaction monitoring enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  Wallet risk checks enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail available
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Manual review required
                </div>
                <div>
                  <span className="status-dot"></span>
                  No real transaction executed
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Operational note</p>
              <h2>Internal concept only</h2>
              <p>
                This page demonstrates the operational layer required behind
                digital asset banking. It does not perform real AML checks,
                sanctions screening, wallet analysis, or regulatory reporting.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real customer data, bank systems,
          AML checks, wallet screening, or blockchain transactions are used.
        </section>
      </main>
    </div>
  )
}
