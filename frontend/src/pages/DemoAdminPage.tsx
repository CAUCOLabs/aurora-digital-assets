import { useEffect, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import {
  getDemoStatus,
  resetDemoData,
  seedDemoData,
  type DemoStatusResponse,
} from '../services/demoAdminApi'

type DemoActionResponse = {
  message: string
}

export function DemoAdminPage() {
  const [demoStatus, setDemoStatus] = useState<DemoStatusResponse | null>(null)
  const [latestActionMessage, setLatestActionMessage] = useState<string | null>(
    null,
  )
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  useEffect(() => {
    void getDemoStatus()
      .then((nextStatus) => {
        setDemoStatus(nextStatus)
        setLatestActionMessage(nextStatus.message)
      })
      .catch(() => {
        setBackendError('Backend demo administration data is unavailable.')
      })
      .finally(() => {
        setIsLoading(false)
      })
  }, [])

  async function loadStatus() {
    setIsLoading(true)
    setBackendError(null)

    try {
      const nextStatus = await getDemoStatus()
      setDemoStatus(nextStatus)
      setLatestActionMessage(nextStatus.message)
    } catch {
      setBackendError('Backend demo administration data is unavailable.')
    } finally {
      setIsLoading(false)
    }
  }

  async function refreshStatus(actionMessage?: string) {
    const nextStatus = await getDemoStatus()
    setDemoStatus(nextStatus)
    setLatestActionMessage(actionMessage ?? nextStatus.message)
  }

  async function runDemoAction(action: () => Promise<DemoActionResponse>) {
    setIsLoading(true)
    setBackendError(null)

    try {
      const result = await action()
      await refreshStatus(result.message)
    } catch {
      setBackendError('Backend demo administration action is unavailable.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Internal prototype tool</p>
            <h1>Internal demo environment</h1>
            <p>
              Control representative local audit events and compliance review
              cases used for demonstration purposes.
            </p>
          </div>

          <div className="security-badge">
            <span className={backendError ? 'warning-dot' : 'status-dot'}></span>
            {isLoading
              ? 'Loading'
              : backendError
                ? 'Unavailable'
                : 'Local prototype'}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Demo controls</p>
                  <h2>Local data controls</h2>
                </div>
                <span className="module-tag">Internal only</span>
              </div>

              <p>
                This is an internal prototype tool. It does not manage real
                users, real bank data, or real crypto records.
              </p>

              {isLoading && (
                <p className="panel-note">Loading demo environment status...</p>
              )}
              {backendError && <p className="panel-note">{backendError}</p>}

              <div className="action-row">
                <button
                  className="secondary-button"
                  type="button"
                  onClick={() => void loadStatus()}
                  disabled={isLoading}
                >
                  Load status
                </button>
                <button
                  type="button"
                  onClick={() => void runDemoAction(seedDemoData)}
                  disabled={isLoading}
                >
                  Seed demo data
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={() => void runDemoAction(resetDemoData)}
                  disabled={isLoading}
                >
                  Reset demo data
                </button>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Status</p>
                  <h2>Stored prototype records</h2>
                </div>
              </div>

              {demoStatus ? (
                <div className="summary-list">
                  <div>
                    <span>Audit events</span>
                    <strong>{demoStatus.audit_events_count}</strong>
                  </div>
                  <div>
                    <span>Review cases</span>
                    <strong>{demoStatus.review_cases_count}</strong>
                  </div>
                  <div>
                    <span>Pending review</span>
                    <strong>{demoStatus.pending_cases_count}</strong>
                  </div>
                  <div>
                    <span>Approved</span>
                    <strong>{demoStatus.approved_cases_count}</strong>
                  </div>
                  <div>
                    <span>Rejected</span>
                    <strong>{demoStatus.rejected_cases_count}</strong>
                  </div>
                </div>
              ) : (
                !isLoading && (
                  <p>Load the local demo environment status to view records.</p>
                )
              )}
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Storage</p>
              <h2>Database</h2>
              <div className="summary-list">
                <div>
                  <span>Environment</span>
                  <strong>
                    {demoStatus?.database ?? 'Status not loaded'}
                  </strong>
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Latest action</p>
              <h2>Demo control status</h2>
              <p>
                {latestActionMessage ??
                  'No local demo administration action has been recorded.'}
              </p>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">System boundary</p>
              <h2>Local records only</h2>
              <p>
                Seed and reset actions apply only to simulated audit events and
                compliance review cases in the local prototype database.
              </p>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}
