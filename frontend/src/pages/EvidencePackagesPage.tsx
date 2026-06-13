import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  generateEvidencePackage,
  getEvidencePackageReadiness,
  getEvidencePackageTemplates,
  getEvidencePackages,
  type EvidenceItem,
  type EvidencePackage,
  type EvidencePackageSourceType,
  type EvidencePackageTemplate,
  type EvidencePackageType,
  type EvidenceReadinessCheck,
  type GenerateEvidencePackageResponse,
} from '../services/evidencePackagesApi'

const sourceIdOptions = [
  'FCA-2026-001',
  'FCA-2026-002',
  'FCA-2026-004',
  'FCA-2026-005',
  'CASE-FC-2026-002',
]

const packageTypeOptions: EvidencePackageType[] = [
  'internal_review',
  'audit',
  'regulator',
  'investigation',
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

function formatDateTime(value: string) {
  return new Intl.DateTimeFormat('en-FI', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(new Date(value))
}

function EvidenceItemList({
  title,
  items,
  emptyText,
}: {
  title: string
  items: EvidenceItem[]
  emptyText: string
}) {
  return (
    <div>
      <h4>{title}</h4>
      {items.length > 0 ? (
        <ul>
          {items.map((item) => (
            <li key={item.item_id}>
              <strong>{item.title}</strong>
              <span>
                {item.category} · {formatLabel(item.status)} ·{' '}
                {item.required ? 'Required' : 'Optional'}
              </span>
              <p>{item.description}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>{emptyText}</p>
      )}
    </div>
  )
}

function StringList({
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

function PackageCard({ evidencePackage }: { evidencePackage: EvidencePackage }) {
  const sourceReference =
    evidencePackage.source_alert_id ??
    evidencePackage.source_case_id ??
    'No source reference'

  return (
    <article className="financial-crime-alert evidence-package-card">
      <div className="panel-header">
        <div>
          <p className="eyebrow">
            {evidencePackage.package_id} · {sourceReference}
          </p>
          <h3>{evidencePackage.title}</h3>
        </div>
        <div className="status-label-group">
          <span className={`risk-label risk-label-${evidencePackage.severity}`}>
            {formatLabel(evidencePackage.severity)}
          </span>
          <span className={`status-label status-${evidencePackage.status}`}>
            {formatLabel(evidencePackage.status)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>Risk type</span>
          <strong>{evidencePackage.risk_type}</strong>
        </div>
        <div>
          <span>Readiness score</span>
          <strong>{evidencePackage.readiness_score}/100</strong>
        </div>
        <div>
          <span>Created</span>
          <strong>{formatDateTime(evidencePackage.created_at)}</strong>
        </div>
        <div>
          <span>Recommended next action</span>
          <strong>{evidencePackage.recommended_next_action}</strong>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>Summary</h4>
        <p>{evidencePackage.summary}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid evidence-package-evidence-grid">
        <EvidenceItemList
          title="Included evidence"
          items={evidencePackage.included_evidence}
          emptyText="No included evidence has been attached."
        />
        <EvidenceItemList
          title="Missing evidence"
          items={evidencePackage.missing_evidence}
          emptyText="No missing evidence is recorded."
        />
        <StringList
          title="Triggered controls"
          items={evidencePackage.triggered_controls}
        />
        <StringList title="Reviewer notes" items={evidencePackage.reviewer_notes} />
      </div>

      <div className="compliance-reasoning-block">
        <h4>Decision rationale</h4>
        <p>{evidencePackage.decision_rationale}</p>
      </div>

      <div className="evidence-timeline">
        <h4>Timeline</h4>
        {evidencePackage.timeline.map((event) => (
          <div key={event.event_id}>
            <span>{formatDateTime(event.timestamp)}</span>
            <strong>{event.title}</strong>
            <p>
              {event.description} ({formatLabel(event.source_module)})
            </p>
          </div>
        ))}
      </div>
    </article>
  )
}

function TemplateList({ templates }: { templates: EvidencePackageTemplate[] }) {
  return (
    <div className="financial-crime-side-list">
      {templates.map((template) => (
        <div key={template.template_id}>
          <strong>{template.title}</strong>
          <small>{formatLabel(template.use_case)}</small>
          <p>{template.description}</p>
          <ul className="compact-list">
            {template.required_items.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}

function ReadinessSummary({ check }: { check: EvidenceReadinessCheck }) {
  return (
    <div className="summary-list">
      <div>
        <span>Ready</span>
        <strong>{check.ready ? 'Yes' : 'No'}</strong>
      </div>
      <div>
        <span>Readiness score</span>
        <strong>{check.score}/100</strong>
      </div>
      <div>
        <span>Blockers</span>
        <ul className="compact-list">
          {(check.blockers.length ? check.blockers : ['No blockers recorded.']).map(
            (item) => (
              <li key={item}>{item}</li>
            ),
          )}
        </ul>
      </div>
      <div>
        <span>Warnings</span>
        <ul className="compact-list">
          {(check.warnings.length ? check.warnings : ['No warnings recorded.']).map(
            (item) => (
              <li key={item}>{item}</li>
            ),
          )}
        </ul>
      </div>
      <div>
        <span>Recommended actions</span>
        <ul className="compact-list">
          {check.recommended_actions.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export function EvidencePackagesPage() {
  const [packages, setPackages] = useState<EvidencePackage[]>([])
  const [templates, setTemplates] = useState<EvidencePackageTemplate[]>([])
  const [sourceType, setSourceType] =
    useState<EvidencePackageSourceType>('alert')
  const [sourceId, setSourceId] = useState('FCA-2026-002')
  const [packageType, setPackageType] =
    useState<EvidencePackageType>('internal_review')
  const [reviewerId, setReviewerId] = useState('reviewer-demo')
  const [generateResult, setGenerateResult] =
    useState<GenerateEvidencePackageResponse | null>(null)
  const [selectedReadiness, setSelectedReadiness] =
    useState<EvidenceReadinessCheck | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isGenerating, setIsGenerating] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const readyPackages = packages.filter((item) => item.status === 'ready').length
  const incompletePackages = packages.filter(
    (item) => item.status === 'incomplete',
  ).length
  const averageReadiness =
    packages.length > 0
      ? Math.round(
          packages.reduce((total, item) => total + item.readiness_score, 0) /
            packages.length,
        )
      : 0

  const summaryCards = useMemo(
    () => [
      {
        label: 'Total packages',
        value: packages.length.toString(),
        detail: 'Deterministic evidence inventory',
      },
      {
        label: 'Ready packages',
        value: readyPackages.toString(),
        detail: 'No readiness blockers',
      },
      {
        label: 'Incomplete packages',
        value: incompletePackages.toString(),
        detail: 'Evidence still required',
      },
      {
        label: 'Average readiness',
        value: `${averageReadiness}/100`,
        detail: 'Across demo packages',
      },
    ],
    [averageReadiness, incompletePackages, packages.length, readyPackages],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([
      getEvidencePackages(),
      getEvidencePackageTemplates(),
      getEvidencePackageReadiness('EP-2026-002'),
    ])
      .then(([nextPackages, nextTemplates, readiness]) => {
        if (!isActive) {
          return
        }

        setPackages(nextPackages)
        setTemplates(nextTemplates)
        setSelectedReadiness(readiness)
      })
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Evidence package data is unavailable in the local prototype.',
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

  async function handleGeneratePackage() {
    setIsGenerating(true)
    setErrorMessage(null)

    try {
      const response = await generateEvidencePackage({
        source_type: sourceType,
        source_id: sourceId,
        package_type: packageType,
        reviewer_id: reviewerId || null,
      })
      setGenerateResult(response)
      setSelectedReadiness(response.readiness_check)
    } catch {
      setErrorMessage('The evidence package demo could not be generated.')
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Protected bank staff area</p>
            <h1>Evidence Packages</h1>
            <p>
              Internal evidence preparation layer for compliance review, audit,
              investigation, and regulator-facing documentation.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Package readiness
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
                  <p className="eyebrow">Evidence package list</p>
                  <h2>Package queue</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/compliance-intelligence"
                >
                  Compliance intelligence
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {packages.map((evidencePackage) => (
                  <PackageCard
                    evidencePackage={evidencePackage}
                    key={evidencePackage.package_id}
                  />
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Package templates</p>
              <h2>Evidence structures</h2>
              <TemplateList templates={templates} />
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Generate evidence package demo</p>
              <h2>Package generator</h2>

              <div className="form-grid">
                <label>
                  <span>Source type</span>
                  <select
                    value={sourceType}
                    onChange={(event) =>
                      setSourceType(
                        event.target.value as EvidencePackageSourceType,
                      )
                    }
                  >
                    <option value="alert">Alert</option>
                    <option value="review_case">Review case</option>
                  </select>
                </label>

                <label>
                  <span>Source ID</span>
                  <select
                    value={sourceId}
                    onChange={(event) => setSourceId(event.target.value)}
                  >
                    {sourceIdOptions.map((option) => (
                      <option key={option} value={option}>
                        {option}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Package type</span>
                  <select
                    value={packageType}
                    onChange={(event) =>
                      setPackageType(event.target.value as EvidencePackageType)
                    }
                  >
                    {packageTypeOptions.map((option) => (
                      <option key={option} value={option}>
                        {formatLabel(option)}
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
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleGeneratePackage()}
                  disabled={isGenerating}
                >
                  Generate package
                </button>
              </div>

              {generateResult && (
                <div className="summary-list">
                  <div>
                    <span>Package title</span>
                    <strong>{generateResult.package.title}</strong>
                  </div>
                  <div>
                    <span>Readiness score</span>
                    <strong>{generateResult.readiness_check.score}/100</strong>
                  </div>
                  <div>
                    <span>Export available</span>
                    <strong>
                      {generateResult.export_available ? 'Yes' : 'No'}
                    </strong>
                  </div>
                  <div>
                    <span>User message</span>
                    <strong>{generateResult.user_message}</strong>
                  </div>
                  <div>
                    <span>Recommended actions</span>
                    <ul className="compact-list">
                      {generateResult.readiness_check.recommended_actions.map(
                        (action) => (
                          <li key={action}>{action}</li>
                        ),
                      )}
                    </ul>
                  </div>
                </div>
              )}
            </Panel>

            <Panel>
              <p className="eyebrow">Readiness explanation</p>
              <h2>Prototype boundary</h2>
              <p>
                This prototype does not create real legal reports, regulator
                filings, or customer records. It models readiness, audit
                evidence, reviewer rationale, missing evidence, and recommended
                next actions using fictional deterministic demo data.
              </p>
              {selectedReadiness && <ReadinessSummary check={selectedReadiness} />}
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. Evidence packages,
          alerts, reviewers, companies, audit events, and documentation states
          are fictional demo data only.
        </p>
      </main>
    </div>
  )
}
