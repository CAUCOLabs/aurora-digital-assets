import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  getRiskOperationsActionQueue,
  getRiskOperationsEscalationSummary,
  getRiskOperationsOverview,
  getRiskOperationsUnifiedTimeline,
  type EscalationSummary,
  type RiskActionItem,
  type RiskOperationsOverview,
  type UnifiedTimelineEvent,
} from '../services/riskOperationsApi'

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

function StringList({
  items,
  emptyText,
}: {
  items: string[]
  emptyText: string
}) {
  return items.length > 0 ? (
    <ul className="compact-list">
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  ) : (
    <p className="panel-note">{emptyText}</p>
  )
}

function CommandBanner({
  overview,
  labels,
}: {
  overview: RiskOperationsOverview | null
  labels: {
    operatingMode: string
    highestPriority: string
    summary: string
    noOverview: string
  }
}) {
  return (
    <Panel className="risk-operations-command">
      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.operatingMode}</span>
          <strong>
            {overview ? formatLabel(overview.operating_mode) : labels.noOverview}
          </strong>
        </div>
        <div>
          <span>{labels.highestPriority}</span>
          <strong>
            {overview ? formatLabel(overview.highest_priority) : labels.noOverview}
          </strong>
        </div>
      </div>
      <div className="compliance-reasoning-block">
        <h2>{labels.summary}</h2>
        <p>{overview?.summary ?? labels.noOverview}</p>
      </div>
    </Panel>
  )
}

function ActionCard({
  action,
  labels,
}: {
  action: RiskActionItem
  labels: {
    sourceModule: string
    sourceId: string
    riskType: string
    summary: string
    requiredAction: string
    missingEvidence: string
    relatedLinks: string
    noMissingEvidence: string
  }
}) {
  return (
    <article className="financial-crime-alert evidence-package-card">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{action.action_id}</p>
          <h3>{action.title}</h3>
        </div>
        <div className="status-label-group">
          <span className={`risk-label risk-label-${action.priority}`}>
            {formatLabel(action.priority)}
          </span>
          <span className={`status-label status-${action.status}`}>
            {formatLabel(action.status)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.sourceModule}</span>
          <strong>{formatLabel(action.source_module)}</strong>
        </div>
        <div>
          <span>{labels.sourceId}</span>
          <strong>{action.source_id}</strong>
        </div>
        <div>
          <span>{labels.riskType}</span>
          <strong>{action.risk_type}</strong>
        </div>
        <div>
          <span>{labels.requiredAction}</span>
          <strong>{action.required_action}</strong>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.summary}</h4>
        <p>{action.summary}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid">
        <div>
          <h4>{labels.missingEvidence}</h4>
          <StringList
            items={action.missing_evidence}
            emptyText={labels.noMissingEvidence}
          />
        </div>
        <div>
          <h4>{labels.relatedLinks}</h4>
          <div className="action-row vertical-actions">
            {action.related_links.map((link) => (
              <Link
                className="button-link secondary-button compact-link"
                to={link.route}
                key={`${link.route}-${link.entity_id ?? link.label}`}
              >
                {link.label}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </article>
  )
}

function TimelineList({
  events,
  labels,
}: {
  events: UnifiedTimelineEvent[]
  labels: {
    relatedEntity: string
    recommendedAction: string
  }
}) {
  return (
    <div className="evidence-timeline">
      {events.map((event) => (
        <div key={event.event_id}>
          <span>
            {formatDateTime(event.timestamp)} · {formatLabel(event.source_module)}
          </span>
          <strong>{event.title}</strong>
          <p>{event.description}</p>
          <p>
            {labels.relatedEntity}: {event.related_entity_id} ·{' '}
            {formatLabel(event.severity)}
          </p>
          <p>
            {labels.recommendedAction}: {event.recommended_action}
          </p>
        </div>
      ))}
    </div>
  )
}

function EscalationList({
  escalations,
  labels,
}: {
  escalations: EscalationSummary[]
  labels: {
    openItems: string
    blockedItems: string
    readyItems: string
    recommendedAction: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {escalations.map((item) => (
        <div key={item.summary_id}>
          <div className="panel-header compact-panel-header">
            <div>
              <strong>{item.title}</strong>
              <small>{formatLabel(item.escalation_type)}</small>
            </div>
            <span className={`risk-label risk-label-${item.severity}`}>
              {formatLabel(item.severity)}
            </span>
          </div>
          <div className="summary-list">
            <div>
              <span>{labels.openItems}</span>
              <strong>{item.open_items}</strong>
            </div>
            <div>
              <span>{labels.blockedItems}</span>
              <strong>{item.blocked_items}</strong>
            </div>
            <div>
              <span>{labels.readyItems}</span>
              <strong>{item.ready_items}</strong>
            </div>
          </div>
          <p>{item.summary}</p>
          <p>
            <strong>{labels.recommendedAction}: </strong>
            {item.recommended_action}
          </p>
        </div>
      ))}
    </div>
  )
}

export function RiskOperationsPage() {
  const { t } = useLanguage()
  const [overview, setOverview] = useState<RiskOperationsOverview | null>(null)
  const [actions, setActions] = useState<RiskActionItem[]>([])
  const [timeline, setTimeline] = useState<UnifiedTimelineEvent[]>([])
  const [escalations, setEscalations] = useState<EscalationSummary[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const metricCards = useMemo(
    () =>
      (overview?.metrics ?? []).filter((metric) =>
        [
          'rom-active-fc-alerts',
          'rom-critical-fc-alerts',
          'rom-incomplete-evidence',
          'rom-active-incidents',
          'rom-paused-operations',
          'rom-staff-action-items',
        ].includes(metric.metric_id),
      ),
    [overview],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([
      getRiskOperationsOverview(),
      getRiskOperationsActionQueue(),
      getRiskOperationsUnifiedTimeline(),
      getRiskOperationsEscalationSummary(),
    ])
      .then(([nextOverview, nextActions, nextTimeline, nextEscalations]) => {
        if (!isActive) {
          return
        }

        setOverview(nextOverview)
        setActions(nextActions)
        setTimeline(nextTimeline)
        setEscalations(nextEscalations)
      })
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Risk operations data is unavailable in the local prototype.',
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

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.riskOperations.title}</h1>
            <p>{t.riskOperations.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankStaffWorkspace.statuses.orchestrationLayer}
          </div>
        </section>

        {errorMessage && <p className="panel-note">{errorMessage}</p>}

        <CommandBanner
          overview={overview}
          labels={{
            operatingMode: t.riskOperations.operatingMode,
            highestPriority: t.riskOperations.highestPriority,
            summary: t.riskOperations.commandSummary,
            noOverview: t.riskOperations.noOverview,
          }}
        />

        <section className="assets-summary financial-crime-summary">
          {metricCards.map((metric) => (
            <div key={metric.metric_id}>
              <p>{metric.label}</p>
              <strong>{isLoading ? '...' : metric.value}</strong>
              <span>{metric.description}</span>
            </div>
          ))}
        </section>

        <section className="content-grid compliance-intelligence-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.riskOperations.staffPriorities}</p>
                  <h2>{t.riskOperations.actionQueue}</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/operational-resilience"
                >
                  {t.operationalResilience.title}
                </Link>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/api-security"
                >
                  {t.apiSecurity.title}
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {actions.map((action) => (
                  <ActionCard
                    action={action}
                    labels={{
                      sourceModule: t.riskOperations.sourceModule,
                      sourceId: t.riskOperations.sourceId,
                      riskType: t.evidencePackages.riskType,
                      summary: t.evidencePackages.summary,
                      requiredAction: t.riskOperations.requiredAction,
                      missingEvidence: t.evidencePackages.missingEvidence,
                      relatedLinks: t.riskOperations.relatedLinks,
                      noMissingEvidence: t.riskOperations.noMissingEvidence,
                    }}
                    key={action.action_id}
                  />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.riskOperations.crossModuleEvents}</p>
                  <h2>{t.riskOperations.unifiedTimeline}</h2>
                </div>
              </div>

              <TimelineList
                events={timeline}
                labels={{
                  relatedEntity: t.riskOperations.relatedEntity,
                  recommendedAction: t.operationalResilience.recommendedAction,
                }}
              />
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.riskOperations.escalations}</p>
              <h2>{t.riskOperations.escalationSummary}</h2>
              <EscalationList
                escalations={escalations}
                labels={{
                  openItems: t.riskOperations.openItems,
                  blockedItems: t.riskOperations.blockedItems,
                  readyItems: t.riskOperations.readyItems,
                  recommendedAction: t.operationalResilience.recommendedAction,
                }}
              />
            </Panel>

            <Panel>
              <p className="eyebrow">{t.riskOperations.recommendedFocus}</p>
              <h2>{t.riskOperations.recommendedFocus}</h2>
              <div className="check-list">
                {(overview?.recommended_focus ?? []).map((focus) => (
                  <div key={focus}>
                    <span className="status-dot"></span>
                    {focus}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.prototypeBoundary.prototypeBoundary}</p>
              <h2>{t.riskOperations.operationalBoundary}</h2>
              <p>{t.riskOperations.operationalBoundaryCopy}</p>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. Risk operations,
          alerts, incidents, evidence records, escalations, and staff priorities
          are fictional deterministic demo data only.
        </p>
      </main>
    </div>
  )
}
