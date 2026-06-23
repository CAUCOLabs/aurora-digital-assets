import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { useLanguage } from '../context/LanguageContext'

type PlaceholderPageProps = {
  eyebrow: string
  title: string
  description: string
}

export function PlaceholderPage({
  eyebrow,
  title,
  description,
}: PlaceholderPageProps) {
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
            <p>{phrase(description)}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {phrase('Demo section')}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{phrase('Module placeholder')}</p>
                  <h2>{phrase(title)}</h2>
                </div>
                <span className="module-tag">{phrase('Coming later')}</span>
              </div>

              <p>
                {phrase(
                  'This section is included to make the online banking prototype feel complete. The main focus of this project remains the bank-integrated Digital Assets module.',
                )}
              </p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{phrase('Prototype note')}</p>
              <h2>{phrase('Scope')}</h2>
              <p>
                {phrase(
                  'This page uses simulated content only. No real bank APIs, payments, cards, loans, or investment services are connected.',
                )}
              </p>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}
