import { Panel } from './Panel'
import { TopBar } from './TopBar'
import { useLanguage } from '../context/LanguageContext'

type PaymentDemoPageKey = keyof typeof import('../i18n/translations').translations.en.paymentDemo.pages

type PaymentDemoPanelProps = {
  pageKey: PaymentDemoPageKey
}

function statusClassName(status: string) {
  return status.toLowerCase().replaceAll(' ', '_')
}

export function PaymentDemoPanel({ pageKey }: PaymentDemoPanelProps) {
  const { t } = useLanguage()
  const page = t.paymentDemo.pages[pageKey]

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{page.eyebrow}</p>
            <h1>{page.title}</h1>
            <p>{page.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {page.badge}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{page.primaryPanelEyebrow}</p>
                  <h2>{page.primaryPanelTitle}</h2>
                </div>
                <span className="module-tag">
                  {t.paymentDemo.common.localPrototype}
                </span>
              </div>

              <div className="form-grid">
                {page.fields.map((field) => (
                  <label key={field.label}>
                    <span>{field.label}</span>
                    <input value={field.value} readOnly />
                    <small className="field-warning">{field.note}</small>
                  </label>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{page.secondaryPanelEyebrow}</p>
                  <h2>{page.secondaryPanelTitle}</h2>
                </div>
                <span className="module-tag">
                  {t.paymentDemo.common.noRealPaymentExecution}
                </span>
              </div>

              <div className="account-list">
                {page.rows.map((row) => (
                  <article className="account-row" key={row.title}>
                    <div>
                      <h3>{row.title}</h3>
                      <p>{row.detail}</p>
                    </div>
                    <span
                      className={`status-label status-${statusClassName(
                        row.status,
                      )}`}
                    >
                      {row.status}
                    </span>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.paymentDemo.common.reviewSummary}</p>
              <h2>{page.summaryTitle}</h2>
              <div className="summary-list">
                {page.summaryItems.map((item) => (
                  <div key={item.label}>
                    <span>{item.label}</span>
                    <strong>{item.value}</strong>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{t.paymentDemo.common.simulatedAction}</p>
              <h2>{page.actionLabel}</h2>
              <p>{page.actionNote}</p>
              <button className="button-link" type="button" disabled>
                {page.actionLabel}
              </button>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{page.safetyTitle}</p>
              <h2>{t.paymentDemo.common.noRealPaymentExecution}</h2>
              <p>{page.safetyNotice}</p>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}
