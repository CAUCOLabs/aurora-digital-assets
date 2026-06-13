import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
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
import { type Language, type translations } from '../i18n/translations'

type Translation = (typeof translations)[Language]

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
  t,
  formatStatus,
}: {
  title: string
  items: EvidenceItem[]
  emptyText: string
  t: Translation
  formatStatus: (value: string) => string
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
                {item.category} · {formatStatus(item.status)} ·{' '}
                {item.required ? t.common.required : t.common.optional}
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

function PackageCard({
  evidencePackage,
  t,
  formatStatus,
}: {
  evidencePackage: EvidencePackage
  t: Translation
  formatStatus: (value: string) => string
}) {
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
            {formatStatus(evidencePackage.severity)}
          </span>
          <span className={`status-label status-${evidencePackage.status}`}>
            {formatStatus(evidencePackage.status)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{t.evidencePackages.riskType}</span>
          <strong>{evidencePackage.risk_type}</strong>
        </div>
        <div>
          <span>{t.evidencePackages.readinessScore}</span>
          <strong>{evidencePackage.readiness_score}/100</strong>
        </div>
        <div>
          <span>{t.evidencePackages.created}</span>
          <strong>{formatDateTime(evidencePackage.created_at)}</strong>
        </div>
        <div>
          <span>{t.evidencePackages.recommendedNextAction}</span>
          <strong>{evidencePackage.recommended_next_action}</strong>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{t.evidencePackages.summary}</h4>
        <p>{evidencePackage.summary}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid evidence-package-evidence-grid">
        <EvidenceItemList
          title={t.evidencePackages.includedEvidence}
          items={evidencePackage.included_evidence}
          emptyText={t.evidencePackages.noIncludedEvidence}
          t={t}
          formatStatus={formatStatus}
        />
        <EvidenceItemList
          title={t.evidencePackages.missingEvidence}
          items={evidencePackage.missing_evidence}
          emptyText={t.evidencePackages.noMissingEvidence}
          t={t}
          formatStatus={formatStatus}
        />
        <StringList
          title={t.evidencePackages.triggeredControls}
          items={evidencePackage.triggered_controls}
        />
        <StringList
          title={t.evidencePackages.reviewerNotes}
          items={evidencePackage.reviewer_notes}
        />
      </div>

      <div className="compliance-reasoning-block">
        <h4>{t.evidencePackages.decisionRationale}</h4>
        <p>{evidencePackage.decision_rationale}</p>
      </div>

      <div className="evidence-timeline">
        <h4>{t.evidencePackages.timeline}</h4>
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

function TemplateList({
  templates,
  formatStatus,
}: {
  templates: EvidencePackageTemplate[]
  formatStatus: (value: string) => string
}) {
  return (
    <div className="financial-crime-side-list">
      {templates.map((template) => (
        <div key={template.template_id}>
          <strong>{template.title}</strong>
          <small>{formatStatus(template.use_case)}</small>
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

function ReadinessSummary({
  check,
  t,
}: {
  check: EvidenceReadinessCheck
  t: Translation
}) {
  return (
    <div className="summary-list">
      <div>
        <span>{t.common.ready}</span>
        <strong>{check.ready ? t.common.yes : t.common.no}</strong>
      </div>
      <div>
        <span>{t.evidencePackages.readinessScore}</span>
        <strong>{check.score}/100</strong>
      </div>
      <div>
        <span>{t.evidencePackages.blockers}</span>
        <ul className="compact-list">
          {(check.blockers.length
            ? check.blockers
            : [t.evidencePackages.noBlockers]
          ).map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <span>{t.evidencePackages.warnings}</span>
        <ul className="compact-list">
          {(check.warnings.length
            ? check.warnings
            : [t.evidencePackages.noWarnings]
          ).map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <span>{t.evidencePackages.recommendedActions}</span>
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
  const { t } = useLanguage()
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
        label: t.evidencePackages.totalPackages,
        value: packages.length.toString(),
        detail: 'Deterministic evidence inventory',
      },
      {
        label: t.evidencePackages.readyPackages,
        value: readyPackages.toString(),
        detail: 'No readiness blockers',
      },
      {
        label: t.evidencePackages.incompletePackages,
        value: incompletePackages.toString(),
        detail: 'Evidence still required',
      },
      {
        label: t.evidencePackages.averageReadiness,
        value: `${averageReadiness}/100`,
        detail: 'Across demo packages',
      },
    ],
    [
      averageReadiness,
      incompletePackages,
      packages.length,
      readyPackages,
      t.evidencePackages.averageReadiness,
      t.evidencePackages.incompletePackages,
      t.evidencePackages.readyPackages,
      t.evidencePackages.totalPackages,
    ],
  )

  function formatStatus(value: string) {
    const labels: Record<string, string> = {
      ready: t.common.ready,
      draft: formatLabel(value),
      incomplete: formatLabel(value),
      escalated: t.common.escalated,
      low: t.common.low,
      medium: t.common.medium,
      high: t.common.high,
      critical: t.common.critical,
      included: t.common.included,
      missing: t.common.missing,
      reviewer_required: t.common.reviewerRequired,
      optional: t.common.optional,
      internal_review: t.common.review,
      audit: 'Audit',
      regulator: 'Regulator',
      investigation: 'Investigation',
    }

    return labels[value] ?? formatLabel(value)
  }

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
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.evidencePackages.title}</h1>
            <p>{t.evidencePackages.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.evidencePackages.packageReadiness}
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
                  <p className="eyebrow">
                    {t.evidencePackages.evidencePackageList}
                  </p>
                  <h2>{t.evidencePackages.packageQueue}</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/compliance-intelligence"
                >
                  {t.complianceIntelligence.title}
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {packages.map((evidencePackage) => (
                  <PackageCard
                    evidencePackage={evidencePackage}
                    t={t}
                    formatStatus={formatStatus}
                    key={evidencePackage.package_id}
                  />
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.evidencePackages.packageTemplates}</p>
              <h2>{t.evidencePackages.evidenceStructures}</h2>
              <TemplateList templates={templates} formatStatus={formatStatus} />
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.evidencePackages.generateDemo}</p>
              <h2>{t.evidencePackages.packageGenerator}</h2>

              <div className="form-grid">
                <label>
                  <span>{t.evidencePackages.sourceType}</span>
                  <select
                    value={sourceType}
                    onChange={(event) =>
                      setSourceType(
                        event.target.value as EvidencePackageSourceType,
                      )
                    }
                  >
                    <option value="alert">Alert</option>
                    <option value="review_case">{t.common.review}</option>
                  </select>
                </label>

                <label>
                  <span>{t.evidencePackages.sourceId}</span>
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
                  <span>{t.evidencePackages.packageType}</span>
                  <select
                    value={packageType}
                    onChange={(event) =>
                      setPackageType(event.target.value as EvidencePackageType)
                    }
                  >
                    {packageTypeOptions.map((option) => (
                      <option key={option} value={option}>
                        {formatStatus(option)}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.evidencePackages.reviewerId}</span>
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
                  {t.evidencePackages.generatePackage}
                </button>
              </div>

              {generateResult && (
                <div className="summary-list">
                  <div>
                    <span>{t.evidencePackages.packageTitle}</span>
                    <strong>{generateResult.package.title}</strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.readinessScore}</span>
                    <strong>{generateResult.readiness_check.score}/100</strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.exportAvailable}</span>
                    <strong>
                      {generateResult.export_available ? t.common.yes : t.common.no}
                    </strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.userMessage}</span>
                    <strong>{generateResult.user_message}</strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.recommendedActions}</span>
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
              <p className="eyebrow">{t.evidencePackages.readinessExplanation}</p>
              <h2>{t.prototypeBoundary.prototypeBoundary}</h2>
              <p>
                This prototype does not create real legal reports, regulator
                filings, or customer records. It models readiness, audit
                evidence, reviewer rationale, missing evidence, and recommended
                next actions using fictional deterministic demo data.
              </p>
              {selectedReadiness && (
                <ReadinessSummary check={selectedReadiness} t={t} />
              )}
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
