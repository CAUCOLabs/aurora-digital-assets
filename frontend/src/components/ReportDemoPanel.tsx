import { Link } from 'react-router-dom'
import { Panel } from './Panel'
import { TopBar } from './TopBar'
import { useLanguage } from '../context/LanguageContext'

type ReportDemoRow = {
  title: string
  detail: string
  status: string
  meta?: string
}

type ReportDemoSummaryItem = {
  label: string
  value: string
}

type ReportDemoLink = {
  label: string
  to: string
}

type ReportDemoPanelProps = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryEyebrow: string
  primaryTitle: string
  primaryTag: string
  rows: ReportDemoRow[]
  secondaryEyebrow: string
  secondaryTitle: string
  summaryItems: ReportDemoSummaryItem[]
  safetyTitle: string
  safetyNotice: string
  actionTitle: string
  actionNote: string
  actionLabel: string
  relatedLinks?: ReportDemoLink[]
}

function statusClassName(status: string) {
  return status.toLowerCase().replaceAll(/[^a-z0-9]+/g, '_')
}

export function ReportDemoPanel({
  eyebrow,
  title,
  subtitle,
  badge,
  primaryEyebrow,
  primaryTitle,
  primaryTag,
  rows,
  secondaryEyebrow,
  secondaryTitle,
  summaryItems,
  safetyTitle,
  safetyNotice,
  actionTitle,
  actionNote,
  actionLabel,
  relatedLinks = [],
}: ReportDemoPanelProps) {
  const { t } = useLanguage()
  const phrases = t.phrases as Record<string, string>
  const phrase = (value: string) => phrases[value] ?? value

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{phrase(eyebrow)}</p>
            <h1>{phrase(title)}</h1>
            <p>{phrase(subtitle)}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {phrase(badge)}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{phrase(primaryEyebrow)}</p>
                  <h2>{phrase(primaryTitle)}</h2>
                </div>
                <span className="module-tag">{phrase(primaryTag)}</span>
              </div>

              <div className="account-list">
                {rows.map((row) => (
                  <article className="account-row" key={row.title}>
                    <div>
                      <h3>{phrase(row.title)}</h3>
                      <p>{phrase(row.detail)}</p>
                      {row.meta ? <span>{phrase(row.meta)}</span> : null}
                    </div>
                    <span
                      className={`status-label status-${statusClassName(
                        row.status,
                      )}`}
                    >
                      {phrase(row.status)}
                    </span>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{phrase(secondaryEyebrow)}</p>
              <h2>{phrase(secondaryTitle)}</h2>
              <div className="summary-list">
                {summaryItems.map((item) => (
                  <div key={item.label}>
                    <span>{phrase(item.label)}</span>
                    <strong>{phrase(item.value)}</strong>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{phrase('Simulated action')}</p>
              <h2>{phrase(actionTitle)}</h2>
              <p>{phrase(actionNote)}</p>
              <button className="button-link" type="button" disabled>
                {phrase(actionLabel)}
              </button>
            </Panel>

            {relatedLinks.length > 0 ? (
              <Panel>
                <p className="eyebrow">{phrase('Documents')}</p>
                <h2>{phrase('Related records')}</h2>
                <div className="check-list">
                  {relatedLinks.map((link) => (
                    <Link key={link.to} to={link.to}>
                      {phrase(link.label)}
                    </Link>
                  ))}
                </div>
              </Panel>
            ) : null}

            <Panel className="risk-panel">
              <p className="eyebrow">{phrase(safetyTitle)}</p>
              <h2>{phrase('Prototype boundary')}</h2>
              <p>{phrase(safetyNotice)}</p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          {phrase(
            'Local deterministic prototype only. No real document, bank statement, card statement, tax report, secure message, audit trail, evidence package, compliance record, customer data, banking operation, export, or legal certification is created or executed.',
          )}
        </section>
      </main>
    </div>
  )
}
