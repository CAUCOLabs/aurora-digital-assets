import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

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
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{eyebrow}</p>
            <h1>{title}</h1>
            <p>{description}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Demo section
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Module placeholder</p>
                  <h2>{title}</h2>
                </div>
                <span className="module-tag">Coming later</span>
              </div>

              <p>
                This section is included to make the online banking prototype
                feel complete. The main focus of this project remains the
                bank-integrated Digital Assets module.
              </p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Prototype note</p>
              <h2>Scope</h2>
              <p>
                This page uses simulated content only. No real bank APIs,
                payments, cards, loans, or investment services are connected.
              </p>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}