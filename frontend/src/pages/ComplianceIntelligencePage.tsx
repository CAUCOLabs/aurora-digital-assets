import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  explainAlert,
  getReviewerGuidance,
  getRiskExplanations,
  prepareReviewCase,
  type ExplainAlertResponse,
  type PrepareReviewCaseResponse,
  type ReviewPriority,
  type ReviewerGuidance,
  type RiskExplanation,
} from '../services/complianceIntelligenceApi'

const demoAlertIds = [
  'FCA-2026-001',
  'FCA-2026-002',
  'FCA-2026-003',
  'FCA-2026-004',
  'FCA-2026-005',
]

const reviewPriorityOptions: ReviewPriority[] = [
  'low',
  'medium',
  'high',
  'urgent',
]

function formatLabel(value: string) {
  return value
    .replaceAll('_', ' ')
    .replaceAll('-', ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase()
    .replace(/^\w/, (letter) => letter.toUpperCase())
}

function EvidenceList({
  title,
  items,
}: {
  title: string
  items: string[]
}) {
  return (
    <div>
      <h4>{title}</h4>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  )
}

export function ComplianceIntelligencePage() {
  const [explanations, setExplanations] = useState<RiskExplanation[]>([])
  const [guidance, setGuidance] = useState<ReviewerGuidance[]>([])
  const [selectedExplainAlertId, setSelectedExplainAlertId] = useState(
    demoAlertIds[1],
  )
  const [includeEvidenceRequirements, setIncludeEvidenceRequirements] =
    useState(true)
  const [explainResult, setExplainResult] =
    useState<ExplainAlertResponse | null>(null)
  const [selectedCaseAlertId, setSelectedCaseAlertId] = useState(demoAlertIds[1])
  const [reviewerId, setReviewerId] = useState('reviewer-demo')
  const [priority, setPriority] = useState<ReviewPriority>('urgent')
  const [casePreview, setCasePreview] =
    useState<PrepareReviewCaseResponse | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isExplaining, setIsExplaining] = useState(false)
  const [isPreparingCase, setIsPreparingCase] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const criticalExplanations = explanations.filter(
    (explanation) => explanation.severity === 'critical',
  ).length
  const reviewReadyPreviews = explanations.filter(
    (explanation) => explanation.evidence_package_ready,
  ).length

  const summaryCards = useMemo(
    () => [
      {
        label: 'Risk explanations',
        value: explanations.length.toString(),
        detail: 'Mapped to demo monitoring alerts',
      },
      {
        label: 'Critical explanations',
        value: criticalExplanations.toString(),
        detail: 'Escalation-focused reasoning',
      },
      {
        label: 'Reviewer guidance items',
        value: guidance.length.toString(),
        detail: 'Human review checklists',
      },
      {
        label: 'Review-ready previews',
        value: reviewReadyPreviews.toString(),
        detail: 'Evidence package ready',
      },
    ],
    [
      criticalExplanations,
      explanations.length,
      guidance.length,
      reviewReadyPreviews,
    ],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([getRiskExplanations(), getReviewerGuidance()])
      .then(([nextExplanations, nextGuidance]) => {
        if (!isActive) {
          return
        }

        setExplanations(nextExplanations)
        setGuidance(nextGuidance)
      })
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Compliance intelligence data is unavailable in the local prototype.',
        )
      })
      .finally(() => {
        if (!isActive) {
          return
        }

        setIsLoading(false)
      })

    return () => {
      isActive = false
    }
  }, [])

  async function handleExplainAlert() {
    setIsExplaining(true)
    setErrorMessage(null)

    try {
      const response = await explainAlert({
        alert_id: selectedExplainAlertId,
        include_evidence_requirements: includeEvidenceRequirements,
      })
      setExplainResult(response)
    } catch {
      setErrorMessage('The selected demo alert could not be explained.')
    } finally {
      setIsExplaining(false)
    }
  }

  async function handlePrepareReviewCase() {
    setIsPreparingCase(true)
    setErrorMessage(null)

    try {
      const response = await prepareReviewCase({
        alert_id: selectedCaseAlertId,
        reviewer_id: reviewerId || null,
        priority,
      })
      setCasePreview(response)
    } catch {
      setErrorMessage('The review case preview could not be prepared.')
    } finally {
      setIsPreparingCase(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Protected bank staff area</p>
            <h1>Compliance Intelligence</h1>
            <p>
              Internal reasoning layer for explaining financial crime alerts,
              required evidence, reviewer guidance, and escalation decisions.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Reasoning layer
          </div>
        </section>

        {errorMessage && <p className="panel-note">{errorMessage}</p>}

        <section className="assets-summary financial-crime-summary">
          {summaryCards.map((card) => (
            <div key={card.label}>
              <p>{card.label}</p>
              <strong>{isLoading ? '...' : card.value}</strong>
              <span>{card.detail}</span>
            </div>
          ))}
        </section>

        <section className="content-grid compliance-intelligence-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Risk explanations</p>
                  <h2>Alert reasoning</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/evidence-packages"
                >
                  Prepare evidence package
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {explanations.map((explanation) => (
                  <article
                    className="financial-crime-alert"
                    key={explanation.explanation_id}
                  >
                    <div className="panel-header">
                      <div>
                        <p className="eyebrow">
                          {explanation.alert_id} · {explanation.risk_type}
                        </p>
                        <h3>{explanation.alert_title}</h3>
                      </div>
                      <div className="status-label-group">
                        <span
                          className={`risk-label risk-label-${explanation.severity}`}
                        >
                          {formatLabel(explanation.severity)}
                        </span>
                        <span
                          className={`decision-label decision-label-${explanation.recommended_decision}`}
                        >
                          {formatLabel(explanation.recommended_decision)}
                        </span>
                      </div>
                    </div>

                    <div className="summary-list financial-crime-alert-meta">
                      <div>
                        <span>Risk summary</span>
                        <strong>{explanation.risk_summary}</strong>
                      </div>
                      <div>
                        <span>Evidence package</span>
                        <strong>
                          {explanation.evidence_package_ready
                            ? 'Ready'
                            : 'Not ready'}
                        </strong>
                      </div>
                    </div>

                    <div className="compliance-reasoning-block">
                      <h4>Reasoning</h4>
                      <p>{explanation.reasoning}</p>
                    </div>

                    <div className="financial-crime-evidence compliance-evidence-grid">
                      <EvidenceList
                        title="Triggered controls"
                        items={explanation.triggered_controls}
                      />
                      <EvidenceList
                        title="Supporting evidence"
                        items={explanation.supporting_evidence}
                      />
                      <EvidenceList
                        title="Missing evidence"
                        items={explanation.missing_evidence}
                      />
                      <EvidenceList
                        title="Reviewer questions"
                        items={explanation.reviewer_questions}
                      />
                    </div>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Reviewer guidance</p>
              <h2>Review checklists</h2>
              <div className="financial-crime-side-list">
                {guidance.map((item) => (
                  <div key={item.guidance_id}>
                    <strong>{item.title}</strong>
                    <small>{item.category}</small>
                    <p>{item.description}</p>
                    <ul className="compact-list">
                      {item.checklist.map((check) => (
                        <li key={check}>{check}</li>
                      ))}
                    </ul>
                    <p>
                      <strong>Action:</strong> {item.reviewer_action}
                    </p>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Explain alert demo</p>
                  <h2>Explain alert</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  <span>Alert</span>
                  <select
                    value={selectedExplainAlertId}
                    onChange={(event) =>
                      setSelectedExplainAlertId(event.target.value)
                    }
                  >
                    {demoAlertIds.map((alertId) => (
                      <option key={alertId} value={alertId}>
                        {alertId}
                      </option>
                    ))}
                  </select>
                </label>

                <label className="checkbox-label compliance-checkbox">
                  <input
                    type="checkbox"
                    checked={includeEvidenceRequirements}
                    onChange={(event) =>
                      setIncludeEvidenceRequirements(event.target.checked)
                    }
                  />
                  Include evidence requirements
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleExplainAlert()}
                  disabled={isExplaining}
                >
                  Explain alert
                </button>
              </div>

              {explainResult && (
                <div className="summary-list">
                  <div>
                    <span>Explanation summary</span>
                    <strong>{explainResult.explanation.risk_summary}</strong>
                  </div>
                  <div>
                    <span>Decision path</span>
                    <ol className="compact-list">
                      {explainResult.decision_path.map((step) => (
                        <li key={step.step_number}>
                          <strong>{step.title}:</strong> {step.description}
                        </li>
                      ))}
                    </ol>
                  </div>
                  <div>
                    <span>Evidence requirements</span>
                    <ul className="compact-list">
                      {explainResult.evidence_requirements.map((requirement) => (
                        <li key={requirement.requirement_id}>
                          {requirement.title} ({formatLabel(requirement.status)})
                        </li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span>Reviewer next steps</span>
                    <ul className="compact-list">
                      {explainResult.reviewer_next_steps.map((step) => (
                        <li key={step}>{step}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Prepare review case demo</p>
                  <h2>Case preview</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  <span>Alert</span>
                  <select
                    value={selectedCaseAlertId}
                    onChange={(event) => setSelectedCaseAlertId(event.target.value)}
                  >
                    {demoAlertIds.map((alertId) => (
                      <option key={alertId} value={alertId}>
                        {alertId}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Reviewer ID</span>
                  <input
                    value={reviewerId}
                    onChange={(event) => setReviewerId(event.target.value)}
                  />
                </label>

                <label>
                  <span>Priority</span>
                  <select
                    value={priority}
                    onChange={(event) =>
                      setPriority(event.target.value as ReviewPriority)
                    }
                  >
                    {reviewPriorityOptions.map((option) => (
                      <option key={option} value={option}>
                        {formatLabel(option)}
                      </option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handlePrepareReviewCase()}
                  disabled={isPreparingCase}
                >
                  Prepare case preview
                </button>
              </div>

              {casePreview && (
                <div className="summary-list">
                  <div>
                    <span>Case preview ID</span>
                    <strong>{casePreview.case_preview_id}</strong>
                  </div>
                  <div>
                    <span>Case title</span>
                    <strong>{casePreview.case_title}</strong>
                  </div>
                  <div>
                    <span>Case summary</span>
                    <strong>{casePreview.case_summary}</strong>
                  </div>
                  <div>
                    <span>Included evidence</span>
                    <ul className="compact-list">
                      {casePreview.included_evidence.map((item) => (
                        <li key={item}>{item}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span>Required evidence</span>
                    <ul className="compact-list">
                      {casePreview.required_evidence.map((item) => (
                        <li key={item}>{item}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span>Recommended assignment</span>
                    <strong>{casePreview.recommended_assignment}</strong>
                  </div>
                  <div>
                    <span>Ready for review</span>
                    <strong>{casePreview.ready_for_review ? 'Yes' : 'No'}</strong>
                  </div>
                </div>
              )}
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. Compliance intelligence
          explanations, evidence requirements, reviewers, companies, accounts,
          and alerts are fictional demo data only.
        </p>
      </main>
    </div>
  )
}
