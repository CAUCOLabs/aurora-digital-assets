import { useEffect, useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import {
  addReviewCaseAction,
  closeReviewCase,
  getReviewCaseLifecycle,
  listAuditEvents,
  listReviewCases,
  recordReviewerDecision,
  transitionReviewCase,
  type AuditEvent,
  type ReviewCase,
  type ReviewCaseActionType,
  type ReviewCaseLifecycleStatus,
  type ReviewCaseLifecycleSummary,
  type ReviewCaseLifecycleTransitionResponse,
} from '../services/complianceApi'
import { useLanguage } from '../context/LanguageContext'

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
  reviewer_decision?: string | null
  source_module?: string | null
  source_id?: string | null
  source_action_id?: string | null
  correlation_id?: string | null
  metadata?: Record<string, unknown>
}

const reviewQueue: LocalReviewCase[] = [
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
]

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

const defaultDecisionNotes =
  'Simulated reviewer decision from Compliance Review dashboard.'

const deterministicLifecycleCases = [
  {
    caseId: 'CASE-INFRA-CHAIN-REACTION',
    evidencePackageId: 'EP-FROM-AUD-INFRA-CHAIN-REACTION',
  },
  {
    caseId: 'CASE-INFRA-AZURE-STORAGE-IDENTITY',
    evidencePackageId: 'EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY',
  },
  {
    caseId: 'CASE-INFRA-K8S-HARDENING-FAILURE',
    evidencePackageId: 'EP-FROM-AUD-INFRA-K8S-HARDENING-FAILURE',
  },
  {
    caseId: 'CASE-CRYPTO-AGILITY-PQ-READINESS',
    evidencePackageId: 'EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS',
  },
]

function formatLabel(value: string) {
  const normalizedValue = value.replaceAll('_', ' ').replace(/\s+/g, ' ').trim()
  return normalizedValue
    .toLowerCase()
    .replace(/^\w/, (letter) => letter.toUpperCase())
}

function formatStatus(value: string) {
  return formatLabel(value)
}

function formatDecision(value: string) {
  return formatLabel(value)
}

function metadataString(
  metadata: Record<string, unknown> | undefined,
  key: string,
) {
  const value = metadata?.[key]
  return typeof value === 'string' ? value : null
}

function metadataList(
  metadata: Record<string, unknown> | undefined,
  key: string,
) {
  const value = metadata?.[key]
  return Array.isArray(value)
    ? value.filter((item): item is string => typeof item === 'string')
    : []
}

export function ComplianceReviewPage() {
  const { t } = useLanguage()
  const [selectedDecision, setSelectedDecision] =
    useState<ReviewerDecision | null>(null)
  const [reviewCases, setReviewCases] = useState<ReviewCase[]>([])
  const [auditEvents, setAuditEvents] = useState<AuditEvent[]>([])
  const [selectedCaseId, setSelectedCaseId] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isRecordingDecision, setIsRecordingDecision] = useState(false)
  const [backendError, setBackendError] = useState<string | null>(null)
  const [reviewerMessage, setReviewerMessage] = useState<string | null>(null)
  const [decisionNotes, setDecisionNotes] = useState(defaultDecisionNotes)
  const [lifecycleCaseId, setLifecycleCaseId] = useState(
    'CASE-CRYPTO-AGILITY-PQ-READINESS',
  )
  const [lifecycleSummary, setLifecycleSummary] =
    useState<ReviewCaseLifecycleSummary | null>(null)
  const [lifecycleResult, setLifecycleResult] =
    useState<ReviewCaseLifecycleTransitionResponse | null>(null)
  const [lifecycleDecisionNote, setLifecycleDecisionNote] = useState(
    'Initial review started.',
  )
  const [mitigationAction, setMitigationAction] = useState(
    'Prepare deterministic mitigation path and preserve evidence.',
  )
  const [lifecycleEvidencePackageId, setLifecycleEvidencePackageId] = useState(
    'EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS',
  )
  const [isTransitioningLifecycle, setIsTransitioningLifecycle] =
    useState(false)

  const activeReviewCases = backendError ? reviewQueue : reviewCases
  const selectedCaseIdOrDefault =
    selectedCaseId ?? activeReviewCases[0]?.case_id ?? null
  const selectedCase =
    activeReviewCases.find(
      (reviewCase) => reviewCase.case_id === selectedCaseIdOrDefault,
    ) ??
    activeReviewCases[0]
  const sortedAuditEvents = [...auditEvents].sort((firstEvent, secondEvent) =>
    secondEvent.timestamp.localeCompare(firstEvent.timestamp),
  )
  const selectedCaseAuditEvents = selectedCase?.case_id
    ? sortedAuditEvents.filter((event) => event.case_id === selectedCase.case_id)
    : []
  const visibleAuditEvents = (
    selectedCaseAuditEvents.length > 0
      ? selectedCaseAuditEvents
      : sortedAuditEvents
  ).slice(0, 6)
  const activeEvidenceTimeline =
    backendError
      ? evidenceTimeline.map((event) => ({
          ...event,
          id: event.title,
        }))
      : visibleAuditEvents.map((event) => ({
          id: event.event_id,
          title: formatLabel(event.action_type),
          detail:
            (event.user_message ??
              `${formatLabel(event.module)} event ${event.event_id} recorded.`) +
            (event.decision
              ? ` Decision: ${formatDecision(event.decision)}.`
              : ''),
          status: formatStatus(event.status),
        }))
  const activeMonitoringSignals = useMemo(() => {
    if (!selectedCase) return backendError ? monitoringSignals : []
    const reasonSignals = selectedCase.reasons.map(formatLabel)
    return reasonSignals.length > 0 ? reasonSignals : monitoringSignals
  }, [backendError, selectedCase])
  const isSelectedCaseFinal = selectedCase
    ? ['Approved', 'Rejected', 'Escalated'].includes(
        formatStatus(selectedCase.status),
      )
    : false
  const sourcePackageId =
    selectedCase?.source_id ??
    metadataString(selectedCase?.metadata, 'source_package_id')
  const sourceAuditEventId =
    selectedCase?.source_action_id ??
    metadataString(selectedCase?.metadata, 'source_audit_event_id')
  const linkedEvidencePackages = metadataList(
    selectedCase?.metadata,
    'linked_evidence_packages',
  )
  const linkedAuditEvents = metadataList(
    selectedCase?.metadata,
    'linked_audit_events',
  )

  useEffect(() => {
    void fetchBackendReviewData()
  }, [])

  useEffect(() => {
    void fetchLifecycle(lifecycleCaseId)
  }, [lifecycleCaseId])

  async function fetchBackendReviewData() {
    setIsLoading(true)

    try {
      const [cases, events] = await Promise.all([
        listReviewCases(),
        listAuditEvents(),
      ])
      setReviewCases(cases)
      setAuditEvents(events)
      setBackendError(null)
      setSelectedCaseId((currentCaseId) => currentCaseId ?? cases[0]?.case_id ?? null)
    } catch {
      setReviewCases([])
      setAuditEvents([])
      setBackendError(
        'Backend review data unavailable. Showing local prototype data.',
      )
    } finally {
      setIsLoading(false)
    }
  }

  async function handleReviewerDecision(
    nextDecision: ReviewerDecision,
    backendDecision: string,
  ) {
    if (isSelectedCaseFinal) return

    setSelectedDecision(nextDecision)

    if (backendError || !selectedCase || reviewCases.length === 0) {
      setReviewerMessage(
        `Reviewer decision recorded locally: ${formatDecision(backendDecision)}`,
      )
      return
    }

    setIsRecordingDecision(true)
    setReviewerMessage(null)

    try {
      const updatedCase = await recordReviewerDecision(selectedCase.case_id, {
        decision: backendDecision,
        notes: decisionNotes.trim() || defaultDecisionNotes,
      })
      setSelectedCaseId(updatedCase.case_id)
      setReviewerMessage(
        `Reviewer decision recorded: ${formatDecision(backendDecision)}`,
      )
      await fetchBackendReviewData()
    } catch {
      setBackendError(
        'Backend review data unavailable. Showing local prototype data.',
      )
      setReviewerMessage(
        'Backend review data unavailable. Showing local prototype data.',
      )
    } finally {
      setIsRecordingDecision(false)
    }
  }

  function handleSelectCase(caseId: string) {
    setSelectedCaseId(caseId)
    setSelectedDecision(null)
    setReviewerMessage(null)
  }

  async function fetchLifecycle(caseId: string) {
    try {
      const summary = await getReviewCaseLifecycle(caseId)
      setLifecycleSummary(summary)
    } catch {
      setLifecycleSummary(null)
    }
  }

  function handleSelectLifecycleCase(caseId: string) {
    const selectedLifecycleCase = deterministicLifecycleCases.find(
      (reviewCase) => reviewCase.caseId === caseId,
    )
    setLifecycleCaseId(caseId)
    setLifecycleEvidencePackageId(
      selectedLifecycleCase?.evidencePackageId ?? '',
    )
    setLifecycleResult(null)
  }

  async function handleLifecycleTransition(
    targetStatus: ReviewCaseLifecycleStatus,
  ) {
    setIsTransitioningLifecycle(true)
    try {
      const response =
        targetStatus === 'closed'
          ? await closeReviewCase(lifecycleCaseId, {
              reviewer_id: 'reviewer-demo',
              decision_note: lifecycleDecisionNote,
              final_decision: 'mitigated',
              evidence_package_id: lifecycleEvidencePackageId || null,
            })
          : await transitionReviewCase(lifecycleCaseId, {
              target_status: targetStatus,
              reviewer_id: 'reviewer-demo',
              decision_note: lifecycleDecisionNote,
              mitigation_action: mitigationAction,
              evidence_package_id: lifecycleEvidencePackageId || null,
            })
      setLifecycleResult(response)
      await fetchLifecycle(lifecycleCaseId)
      await fetchBackendReviewData()
    } finally {
      setIsTransitioningLifecycle(false)
    }
  }

  async function handleAddLifecycleAction(actionType: ReviewCaseActionType) {
    await addReviewCaseAction(lifecycleCaseId, {
      action_type: actionType,
      actor_id: 'reviewer-demo',
      note: lifecycleDecisionNote || 'Lifecycle action recorded.',
    })
    await fetchLifecycle(lifecycleCaseId)
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
              {backendError && <p className="panel-note">{backendError}</p>}

              <div className="account-list">
                {activeReviewCases.map((reviewCase) => (
                  <article
                    className="account-row"
                    key={reviewCase.case_id}
                    onClick={() => handleSelectCase(reviewCase.case_id)}
                  >
                    <div>
                      <h3>{reviewCase.title}</h3>
                      <p>{formatLabel(reviewCase.case_type)}</p>
                      <span>{formatStatus(reviewCase.status)}</span>
                    </div>
                    <strong>{formatLabel(reviewCase.risk_level)} risk</strong>
                  </article>
                ))}
              </div>
              {!isLoading && !backendError && reviewCases.length === 0 && (
                <p className="panel-note">
                  No review cases are currently recorded.
                </p>
              )}
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
                  <article className="account-row" key={event.id}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
              {!isLoading && !backendError && visibleAuditEvents.length === 0 && (
                <p className="panel-note">
                  No audit evidence is currently recorded.
                </p>
              )}
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
              {!isLoading && activeMonitoringSignals.length === 0 && (
                <p className="panel-note">
                  No monitoring signals are currently recorded.
                </p>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.reviewCaseLifecycle.caseLifecycle}</p>
                  <h2>{t.reviewCaseLifecycle.title}</h2>
                </div>
                <span className="module-tag">
                  {t.reviewCaseLifecycle.lifecycleProgress}
                </span>
              </div>

              <div className="form-grid">
                <label>
                  <span>Case ID</span>
                  <select
                    value={lifecycleCaseId}
                    onChange={(event) =>
                      handleSelectLifecycleCase(event.target.value)
                    }
                  >
                    {deterministicLifecycleCases.map((reviewCase) => (
                      <option key={reviewCase.caseId} value={reviewCase.caseId}>
                        {reviewCase.caseId}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.reviewCaseLifecycle.decisionNote}</span>
                  <textarea
                    value={lifecycleDecisionNote}
                    onChange={(event) =>
                      setLifecycleDecisionNote(event.target.value)
                    }
                  />
                </label>

                <label>
                  <span>{t.reviewCaseLifecycle.mitigationAction}</span>
                  <input
                    value={mitigationAction}
                    onChange={(event) =>
                      setMitigationAction(event.target.value)
                    }
                  />
                </label>

                <label>
                  <span>{t.evidencePackages.linkedEvidencePackage}</span>
                  <input
                    value={lifecycleEvidencePackageId}
                    onChange={(event) =>
                      setLifecycleEvidencePackageId(event.target.value)
                    }
                  />
                </label>
              </div>

              <div className="summary-list">
                <div>
                  <span>{t.reviewCaseLifecycle.currentStatus}</span>
                  <strong>
                    {lifecycleSummary
                      ? formatStatus(lifecycleSummary.current_status)
                      : 'Not loaded'}
                  </strong>
                </div>
                <div>
                  <span>{t.reviewCaseLifecycle.allowedNextStatuses}</span>
                  <ul className="compact-list">
                    {(lifecycleSummary?.allowed_next_statuses.length
                      ? lifecycleSummary.allowed_next_statuses
                      : ['None']
                    ).map((status) => (
                      <li key={status}>{formatStatus(status)}</li>
                    ))}
                  </ul>
                </div>
                <div>
                  <span>{t.reviewCaseLifecycle.closureReady}</span>
                  <strong>
                    {lifecycleSummary?.closure_ready ? 'Yes' : 'No'}
                  </strong>
                </div>
              </div>

              <div className="lifecycle-progress-track">
                <span
                  style={{
                    width: `${lifecycleSummary?.lifecycle_progress_percent ?? 0}%`,
                  }}
                />
              </div>

              <div className="action-row vertical-actions">
                <button
                  type="button"
                  disabled={isTransitioningLifecycle}
                  onClick={() => handleLifecycleTransition('under_review')}
                >
                  {t.reviewCaseLifecycle.startReview}
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isTransitioningLifecycle}
                  onClick={() => handleLifecycleTransition('action_required')}
                >
                  {t.reviewCaseLifecycle.markActionRequired}
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isTransitioningLifecycle}
                  onClick={() =>
                    handleLifecycleTransition('mitigation_in_progress')
                  }
                >
                  {t.reviewCaseLifecycle.startMitigation}
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isTransitioningLifecycle}
                  onClick={() => handleLifecycleTransition('mitigated')}
                >
                  {t.reviewCaseLifecycle.markMitigated}
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  disabled={isTransitioningLifecycle}
                  onClick={() => handleLifecycleTransition('closed')}
                >
                  {t.reviewCaseLifecycle.closeCase}
                </button>
              </div>

              {lifecycleResult && (
                <div className="summary-list">
                  <div>
                    <span>{t.reviewCaseLifecycle.previousStatus}</span>
                    <strong>{formatStatus(lifecycleResult.previous_status)}</strong>
                  </div>
                  <div>
                    <span>{t.reviewCaseLifecycle.currentStatus}</span>
                    <strong>{formatStatus(lifecycleResult.new_status)}</strong>
                  </div>
                  <div>
                    <span>{t.common.auditEventCreated}</span>
                    <strong>
                      {lifecycleResult.audit_event_created ? 'Yes' : 'No'}
                    </strong>
                  </div>
                  <div>
                    <span>{t.common.auditEventId}</span>
                    <strong>{lifecycleResult.audit_event_id || 'Not created'}</strong>
                  </div>
                  <div>
                    <span>{t.common.correlationId}</span>
                    <strong>{lifecycleResult.correlation_id}</strong>
                  </div>
                  <div>
                    <span>{t.reviewCaseLifecycle.recommendedNextStatus}</span>
                    <strong>
                      {lifecycleResult.recommended_next_status
                        ? formatStatus(lifecycleResult.recommended_next_status)
                        : 'None'}
                    </strong>
                  </div>
                </div>
              )}

              <div className="financial-crime-evidence compliance-evidence-grid">
                <div>
                  <h4>{t.reviewCaseLifecycle.reviewerAction}</h4>
                  <div className="action-row vertical-actions">
                    {(
                      [
                        'reviewer_note',
                        'evidence_reviewed',
                        'mitigation_requested',
                        'mitigation_started',
                        'mitigation_verified',
                        'case_closed',
                      ] as ReviewCaseActionType[]
                    ).map((actionType) => (
                      <button
                        className="secondary-button compact-link"
                        type="button"
                        key={actionType}
                        onClick={() => void handleAddLifecycleAction(actionType)}
                      >
                        {formatStatus(actionType)}
                      </button>
                    ))}
                  </div>
                </div>
                <div>
                  <h4>{t.reviewCaseLifecycle.caseLifecycle}</h4>
                  <div className="evidence-timeline">
                    {(lifecycleSummary?.actions ?? []).map((action) => (
                      <div key={action.action_id}>
                        <span>{formatStatus(action.action_type)}</span>
                        <strong>{action.actor_id}</strong>
                        <p>{action.note}</p>
                      </div>
                    ))}
                  </div>
                </div>
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
                    {selectedCase
                      ? formatLabel(selectedCase.case_type)
                      : 'Not available'}
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
                  <strong>
                    {selectedCase
                      ? formatStatus(selectedCase.status)
                      : 'Not available'}
                  </strong>
                </div>
                <div>
                  <span>Risk score</span>
                  <strong>
                    {selectedCase
                      ? formatLabel(selectedCase.risk_level)
                      : 'Not available'}
                  </strong>
                </div>
                <div>
                  <span>Reviewer decision</span>
                  <strong>
                    {selectedCase?.reviewer_decision
                      ? formatDecision(selectedCase.reviewer_decision)
                    : 'Not recorded'}
                  </strong>
                </div>
              </div>
            </Panel>

            {selectedCase?.source_module === 'evidence_packages' && (
              <Panel>
                <p className="eyebrow">Compliance review linkage</p>
                <h2>Evidence-to-review traceability</h2>
                <div className="summary-list">
                  <div>
                    <span>Origin</span>
                    <strong>Evidence package</strong>
                  </div>
                  <div>
                    <span>Source module</span>
                    <strong>
                      {formatLabel(
                        metadataString(selectedCase.metadata, 'source_domain') ??
                          'infrastructure_security',
                      )}
                    </strong>
                  </div>
                  <div>
                    <span>Source evidence package</span>
                    <strong>{sourcePackageId ?? 'Not recorded'}</strong>
                  </div>
                  <div>
                    <span>Audit event</span>
                    <strong>{sourceAuditEventId ?? 'Not recorded'}</strong>
                  </div>
                  <div>
                    <span>Correlation ID</span>
                    <strong>
                      {selectedCase.correlation_id ?? 'Not recorded'}
                    </strong>
                  </div>
                  <div>
                    <span>Linked evidence packages</span>
                    <ul className="compact-list">
                      {(linkedEvidencePackages.length
                        ? linkedEvidencePackages
                        : [sourcePackageId ?? 'Not recorded']
                      ).map((item) => (
                        <li key={item}>{item}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span>Linked audit events</span>
                    <ul className="compact-list">
                      {(linkedAuditEvents.length
                        ? linkedAuditEvents
                        : [sourceAuditEventId ?? 'Not recorded']
                      ).map((item) => (
                        <li key={item}>{item}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </Panel>
            )}

            <Panel>
              <p className="eyebrow">Reviewer actions</p>
              <h2>Decision workflow</h2>

              <div className="form-grid">
                <label>
                  Reviewer notes
                  <textarea
                    value={decisionNotes}
                    onChange={(event) => setDecisionNotes(event.target.value)}
                  />
                </label>
              </div>

              {isSelectedCaseFinal ? (
                <p className="panel-note">
                  This case already has a recorded reviewer outcome.
                </p>
              ) : (
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
              )}

              <p className="panel-note">
                Reviewer decision:{' '}
                {selectedDecision
                  ? formatDecision(selectedDecision)
                  : selectedCase?.reviewer_decision
                    ? formatDecision(selectedCase.reviewer_decision)
                    : 'No decision selected'}
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
