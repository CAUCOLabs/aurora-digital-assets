import { useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

type ReviewerDecision =
  | 'Approve'
  | 'Reject'
  | 'Request information'
  | 'Escalate'

const reviewQueue = [
  {
    title: 'External BTC withdrawal',
    detail: 'Pending review',
    status: 'Pending review',
    risk: 'Medium risk',
  },
  {
    title: 'New external wallet address',
    detail: 'Review required',
    status: 'Review required',
    risk: 'Medium risk',
  },
  {
    title: 'Digital asset invoice payment',
    detail: 'Recorded',
    status: 'Recorded',
    risk: 'Low risk',
  },
  {
    title: 'Large USDC payment',
    detail: 'Monitoring event',
    status: 'Monitoring event',
    risk: 'Low risk',
  },
  {
    title: 'Wallet risk check',
    detail: 'Escalated',
    status: 'Escalated',
    risk: 'High risk',
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

export function ComplianceReviewPage() {
  const [selectedDecision, setSelectedDecision] =
    useState<ReviewerDecision | null>(null)

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
                <span className="module-tag">Simulated cases</span>
              </div>

              <div className="account-list">
                {reviewQueue.map((reviewCase) => (
                  <article className="account-row" key={reviewCase.title}>
                    <div>
                      <h3>{reviewCase.title}</h3>
                      <p>{reviewCase.detail}</p>
                      <span>{reviewCase.status}</span>
                    </div>
                    <strong>{reviewCase.risk}</strong>
                  </article>
                ))}
              </div>
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
                {evidenceTimeline.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Monitoring signals</p>
                  <h2>Triggered signals</h2>
                </div>
              </div>

              <div className="check-list">
                {monitoringSignals.map((signal) => (
                  <div key={signal}>
                    <span className="status-dot"></span>
                    {signal}
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Selected case</p>
              <h2>CASE-DA-2026-001</h2>

              <div className="summary-list">
                <div>
                  <span>Case ID</span>
                  <strong>CASE-DA-2026-001</strong>
                </div>
                <div>
                  <span>Type</span>
                  <strong>External withdrawal review</strong>
                </div>
                <div>
                  <span>Customer</span>
                  <strong>Claudio Demo</strong>
                </div>
                <div>
                  <span>Asset</span>
                  <strong>BTC</strong>
                </div>
                <div>
                  <span>Amount</span>
                  <strong>0.001 BTC</strong>
                </div>
                <div>
                  <span>Network</span>
                  <strong>Bitcoin</strong>
                </div>
                <div>
                  <span>Status</span>
                  <strong>Pending review</strong>
                </div>
                <div>
                  <span>Risk score</span>
                  <strong>Medium</strong>
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Reviewer actions</p>
              <h2>Decision workflow</h2>

              <div className="action-row vertical-actions">
                <button type="button" onClick={() => setSelectedDecision('Approve')}>
                  Approve
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={() => setSelectedDecision('Reject')}
                >
                  Reject
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={() => setSelectedDecision('Request information')}
                >
                  Request information
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={() => setSelectedDecision('Escalate')}
                >
                  Escalate
                </button>
              </div>

              <p className="panel-note">
                Reviewer decision:{' '}
                {selectedDecision ?? 'No decision selected'}
              </p>
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
