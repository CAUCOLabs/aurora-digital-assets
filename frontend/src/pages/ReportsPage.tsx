import { useEffect, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { PrivacyAmount } from '../components/PrivacyAmount'
import {
  listAuditEvents,
  listReviewCases,
  type AuditEvent,
  type ReviewCase,
} from '../services/complianceApi'
import {
  listReports,
  getTaxSummary,
  createEvidencePackage,
  type ReportSummary,
  type TaxSummary,
} from '../services/reportsApi'

type DisplayRow = {
  id: string
  title: string
  detail: string
  status: string
  message?: string | null
}

type BackendFailures = {
  reports: boolean
  taxSummary: boolean
  auditEvents: boolean
  reviewCases: boolean
}

const fallbackBankingDocuments = [
  {
    title: 'Current account statement',
    detail: 'April 2026',
    status: 'Available',
    action: 'View',
  },
  {
    title: 'Payment receipt',
    detail: 'Aurora Telecom Oyj',
    status: 'Available',
    action: 'Open',
  },
]

// Fallback data is only for offline demo mode when the backend is unavailable.
const fallbackReports: DisplayRow[] = [
  {
    id: 'fallback-annual-summary',
    title: 'Digital assets annual summary',
    detail: '2026',
    status: 'Ready',
  },
  {
    id: 'fallback-wallet-activity',
    title: 'Wallet activity report',
    detail: 'BTC / ETH',
    status: 'Ready',
  },
]

const fallbackAuditEvents: DisplayRow[] = [
  {
    id: 'fallback-estimate-generated',
    title: 'Digital asset payment estimate generated',
    detail: 'Payments',
    status: 'Recorded',
  },
  {
    id: 'fallback-buy-evaluated',
    title: 'BTC buy evaluation recorded',
    detail: 'Buy / Sell',
    status: 'Recorded',
  },
]

const exportConcepts = [
  'PDF report export',
  'CSV transaction export',
  'Audit evidence package',
  'Payment receipts bundle',
  'Tax summary export',
]

const evidenceCoverage = [
  'Payments',
  'Buy / Sell',
  'Wallet and custody',
  'External withdrawals',
  'Reports',
]

const fallbackTaxSummary: TaxSummary = {
  year: 2026,
  total_purchases_eur: 75,
  total_sales_eur: 0,
  digital_asset_payments_eur: 120.45,
  external_transfers_count: 1,
  pending_review_cases: 1,
  estimated_realized_gain_loss_eur: 0,
  disclaimer: 'Prototype values only. Not official tax advice.',
}

const fallbackReviewCases: DisplayRow[] = [
  {
    id: 'fallback-review-evidence-package',
    title: 'Review evidence package',
    detail:
      'Review cases created by withdrawal and digital asset payment flows can be included in evidence packages.',
    status: 'Concept',
  },
]

const initialBackendFailures: BackendFailures = {
  reports: false,
  taxSummary: false,
  auditEvents: false,
  reviewCases: false,
}

function formatEur(amount: number) {
  return new Intl.NumberFormat('fi-FI', {
    style: 'currency',
    currency: 'EUR',
  }).format(amount)
}

function formatLabel(value: string) {
  return value
    .replaceAll('_', ' ')
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
}

function formatStatus(value: string) {
  return value
    .replaceAll('_', ' ')
    .toLowerCase()
    .replace(/^\w/, (letter) => letter.toUpperCase())
}

function formatReviewAmount(reviewCase: ReviewCase) {
  if (reviewCase.case_type === 'external_withdrawal_review') {
    return `${reviewCase.amount} ${reviewCase.asset}`
  }

  return formatEur(reviewCase.amount)
}

export function ReportsPage() {
  const [backendAuditEvents, setBackendAuditEvents] = useState<AuditEvent[]>([])
  const [backendReviewCases, setBackendReviewCases] = useState<ReviewCase[]>([])
  const [backendReports, setBackendReports] = useState<ReportSummary[]>([])
  const [backendTaxSummary, setBackendTaxSummary] = useState<TaxSummary | null>(
    null,
  )
  const [isLoading, setIsLoading] = useState(true)
  const [backendFailures, setBackendFailures] = useState<BackendFailures>(
    initialBackendFailures,
  )

  const [evidencePackageMessage, setEvidencePackageMessage] = useState<
    string | null
  >(null)
  const [isGeneratingPackage, setIsGeneratingPackage] = useState(false)

  const reportRows: DisplayRow[] =
    backendReports.length > 0
      ? backendReports.map((report) => ({
          id: report.report_id,
          title: report.title,
          detail: `${report.description} Included records: ${report.item_count}.`,
          status: report.status,
          message: `Source: ${report.generated_from}`,
        }))
      : backendFailures.reports
        ? fallbackReports
        : []

  const taxSummary = backendTaxSummary ?? (
    backendFailures.taxSummary ? fallbackTaxSummary : null
  )

  const visibleAuditEvents: DisplayRow[] =
    backendAuditEvents.length > 0
      ? backendAuditEvents.map((event) => ({
          id: event.event_id,
          title: formatLabel(event.action_type),
          detail: [
            event.module,
            event.risk_level ? `${event.risk_level} risk` : null,
            event.case_id ? `case ${event.case_id}` : null,
          ]
            .filter(Boolean)
            .join(' · '),
          status: formatStatus(event.status),
          message: event.user_message,
        }))
      : backendFailures.auditEvents
        ? fallbackAuditEvents
        : []

  const hasBackendFailure = Object.values(backendFailures).some(Boolean)

  const backendStatusNote = hasBackendFailure
    ? 'Backend reporting data unavailable. Showing local prototype fallback.'
    : null

  useEffect(() => {
    async function fetchReportingData() {
      setIsLoading(true)

      const [eventsResult, casesResult, reportsResult, taxSummaryResult] =
        await Promise.allSettled([
          listAuditEvents(),
          listReviewCases(),
          listReports(),
          getTaxSummary(2026),
        ])

      if (eventsResult.status === 'fulfilled') {
        const events = eventsResult.value
        setBackendAuditEvents(events)
      } else {
        setBackendAuditEvents([])
      }

      if (casesResult.status === 'fulfilled') {
        const cases = casesResult.value
        setBackendReviewCases(cases)
      } else {
        setBackendReviewCases([])
      }

      if (reportsResult.status === 'fulfilled') {
        const reports = reportsResult.value
        setBackendReports(reports)
      } else {
        setBackendReports([])
      }

      if (taxSummaryResult.status === 'fulfilled') {
        const taxSummary = taxSummaryResult.value
        setBackendTaxSummary(taxSummary)
      } else {
        setBackendTaxSummary(null)
      }

      setBackendFailures({
        reports: reportsResult.status === 'rejected',
        taxSummary: taxSummaryResult.status === 'rejected',
        auditEvents: eventsResult.status === 'rejected',
        reviewCases: casesResult.status === 'rejected',
      })
      setIsLoading(false)
    }

    void fetchReportingData()
  }, [])

  async function handleGenerateAuditPackage() {
    setIsGeneratingPackage(true)
    setEvidencePackageMessage(null)

    try {
      const response = await createEvidencePackage({ year: 2026 })
      setEvidencePackageMessage(
        `${response.package_id} prepared. Included ${response.included_audit_events} audit events and ${response.included_review_cases} review cases.`,
      )
    } catch {
      setEvidencePackageMessage(
        'Backend evidence package unavailable. Export remains a local prototype concept.',
      )
    } finally {
      setIsGeneratingPackage(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Documents</p>
            <h1>Reports and audit evidence</h1>
            <p>
              Review account statements, payment receipts, digital asset
              activity, tax summaries, and audit evidence generated by the
              Aurora Bank prototype.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Reports available
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Banking documents</p>
                  <h2>Banking documents</h2>
                </div>
                <span className="module-tag">Documents area</span>
              </div>

              <div className="account-list">
                {fallbackBankingDocuments.map((document) => (
                  <article className="account-row" key={document.title}>
                    <div>
                      <h3>{document.title}</h3>
                      <p>{document.detail}</p>
                      <span>{document.status}</span>
                    </div>
                    <strong>{document.action}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Digital asset reports</p>
                  <h2>Digital asset reports</h2>
                </div>
                <span className="module-tag">
                  {backendFailures.reports ? 'Local fallback' : 'Backend reports'}
                </span>
              </div>

              {isLoading && <p className="panel-note">Loading reports...</p>}
              {backendStatusNote && <p className="panel-note">{backendStatusNote}</p>}

              <div className="account-list">
                {reportRows.map((report) => (
                  <article className="account-row" key={report.id}>
                    <div>
                      <h3>{report.title}</h3>
                      <p>{report.detail}</p>
                      {report.message && <span>{report.message}</span>}
                    </div>
                    <strong>{report.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Tax summary</p>
                  <h2>2026 tax summary</h2>
                </div>
                <span className="module-tag">
                  {backendTaxSummary
                    ? 'Backend values'
                    : backendFailures.taxSummary
                      ? 'Fallback values'
                      : 'Loading values'}
                </span>
              </div>

              {taxSummary ? (
                <>
                  <div className="withdrawal-preview">
                    <div>
                      <p>Tax year</p>
                      <strong>{taxSummary.year}</strong>
                    </div>
                    <div>
                      <p>Total purchases</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(taxSummary.total_purchases_eur)}
                          label="Total purchases"
                        />
                      </strong>
                    </div>
                    <div>
                      <p>Total sales</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(taxSummary.total_sales_eur)}
                          label="Total sales"
                        />
                      </strong>
                    </div>
                    <div>
                      <p>Digital asset payments</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(
                            taxSummary.digital_asset_payments_eur,
                          )}
                          label="Digital asset payments"
                        />
                      </strong>
                    </div>
                    <div>
                      <p>External transfers</p>
                      <strong>
                        {taxSummary.external_transfers_count}
                      </strong>
                    </div>
                    <div>
                      <p>Pending review cases</p>
                      <strong>
                        {taxSummary.pending_review_cases}
                      </strong>
                    </div>
                    <div>
                      <p>Estimated realized gain/loss</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(
                            taxSummary.estimated_realized_gain_loss_eur,
                          )}
                          label="Estimated realized gain or loss"
                        />
                      </strong>
                    </div>
                  </div>

                  <p className="panel-note">{taxSummary.disclaimer}</p>
                </>
              ) : (
                <p className="panel-note">Loading tax summary...</p>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Audit evidence timeline</p>
                  <h2>Cross-module audit evidence</h2>
                </div>
                <span className="module-tag">
                  {backendFailures.auditEvents
                    ? 'Local fallback'
                    : 'Backend audit events'}
                </span>
              </div>
              {isLoading && <p className="panel-note">Loading report evidence...</p>}

              <div className="account-list">
                {visibleAuditEvents.map((event) => (
                  <article className="account-row" key={event.id}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      {'message' in event && event.message && (
                        <p>{event.message}</p>
                      )}
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
                  <p className="eyebrow">Review case evidence</p>
                  <h2>Internal review cases</h2>
                </div>
                <span className="module-tag">
                  {backendFailures.reviewCases
                    ? 'Local fallback'
                    : 'Backend review cases'}
                </span>
              </div>

              {backendReviewCases.length > 0 && (
                <div className="account-list">
                  {backendReviewCases.map((reviewCase) => (
                    <article className="account-row" key={reviewCase.case_id}>
                      <div>
                        <h3>{reviewCase.title}</h3>
                        <div className="summary-list">
                          <div>
                            <span>Case ID</span>
                            <strong>{reviewCase.case_id}</strong>
                          </div>
                          <div>
                            <span>Status</span>
                            <strong>
                              <span
                                className={
                                  formatStatus(reviewCase.status) ===
                                  'Pending review'
                                    ? 'warning-dot'
                                    : 'status-dot'
                                }
                              ></span>
                              {formatStatus(reviewCase.status)}
                            </strong>
                          </div>
                          <div>
                            <span>Risk level</span>
                            <strong>{reviewCase.risk_level}</strong>
                          </div>
                          <div>
                            <span>Case type</span>
                            <strong>{formatLabel(reviewCase.case_type)}</strong>
                          </div>
                          <div>
                            <span>Asset</span>
                            <strong>{reviewCase.asset}</strong>
                          </div>
                          <div>
                            <span>Amount</span>
                            <strong>
                              <PrivacyAmount
                                value={formatReviewAmount(reviewCase)}
                                label={`${reviewCase.case_id} amount`}
                              />
                            </strong>
                          </div>
                          <div>
                            <span>Destination / recipient</span>
                            <strong>{reviewCase.destination_address}</strong>
                          </div>
                          <div>
                            <span>Reasons</span>
                            <strong>
                              {reviewCase.reasons.map(formatLabel).join(', ')}
                            </strong>
                          </div>
                          {reviewCase.reviewer_decision && (
                            <div>
                              <span>Reviewer decision</span>
                              <strong>
                                {formatStatus(reviewCase.reviewer_decision)}
                              </strong>
                            </div>
                          )}
                        </div>
                      </div>
                      <strong>{formatStatus(reviewCase.status)}</strong>
                    </article>
                  ))}
                </div>
              )}

              {backendFailures.reviewCases && (
                <div className="account-list">
                  {fallbackReviewCases.map((reviewCase) => (
                    <article className="account-row" key={reviewCase.id}>
                      <div>
                        <h3>{reviewCase.title}</h3>
                        <p>{reviewCase.detail}</p>
                      </div>
                      <strong>{reviewCase.status}</strong>
                    </article>
                  ))}
                </div>
              )}

              {!isLoading &&
                !backendFailures.reviewCases &&
                backendReviewCases.length === 0 && (
                  <p className="panel-note">
                    No persisted review cases are available for this report.
                  </p>
                )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Export center</p>
                  <h2>Export center</h2>
                </div>
                <span className="module-tag">Concept actions</span>
              </div>

              <div className="account-list">
                {exportConcepts.map((exportConcept) => (
                  <article className="account-row" key={exportConcept}>
                    <div>
                      <h3>{exportConcept}</h3>
                      <p>Prepared from simulated prototype records.</p>
                      <span>Not generated yet</span>
                    </div>
                    <strong>Concept</strong>
                  </article>
                ))}
              </div>

              {evidencePackageMessage && (
                <p className="panel-note">{evidencePackageMessage}</p>
              )}

              <p className="panel-note">
                Evidence package concept only. No real PDF or CSV file is
                generated by this action.
              </p>

              <div className="action-row">
                <button type="button">Export PDF</button>
                <button className="secondary-button" type="button">
                  Export CSV
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={handleGenerateAuditPackage}
                  disabled={isGeneratingPackage}
                >
                  {isGeneratingPackage ? 'Generating...' : 'Generate audit package'}
                </button>
                <button className="secondary-button" type="button">
                  Download receipts
                </button>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Report status</p>
              <h2>Available records</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Account documents available
                </div>
                <div>
                  <span className="status-dot"></span>
                  Payment receipts available
                </div>
                <div>
                  <span
                    className={
                      backendReports.length > 0 ? 'status-dot' : 'warning-dot'
                    }
                  ></span>
                  Digital asset reports {backendReports.length > 0 ? 'loaded' : 'available'}
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail available
                </div>
                <div>
                  <span
                    className={
                      backendAuditEvents.length > 0
                        ? 'status-dot'
                        : 'warning-dot'
                    }
                  ></span>
                  Audit events loaded
                </div>
                <div>
                  <span
                    className={
                      backendReviewCases.length > 0
                        ? 'status-dot'
                        : 'warning-dot'
                    }
                  ></span>
                  Review cases available
                </div>
                <div>
                  <span className="status-dot"></span>
                  Evidence package concept ready
                </div>
                <div>
                  <span
                    className={
                      backendTaxSummary ? 'status-dot' : 'warning-dot'
                    }
                  ></span>
                  Tax summary {backendTaxSummary ? 'loaded' : 'simulated'}
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Evidence coverage</p>
              <h2>Covered modules</h2>

              <div className="check-list">
                {evidenceCoverage.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Tax disclaimer</p>
              <h2>Simulated tax information</h2>
              <p>
                This page provides simulated reporting concepts only. It does
                not provide official tax advice or replace professional tax
                guidance.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Product boundary</p>
              <h2>Mock records only</h2>
              <p>
                Reports are generated from simulated values only. No real bank
                records, real crypto custody data, private keys, or customer
                data are used.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real bank APIs, no real tax filing,
          no real crypto custody, no private keys, and no real customer data.
        </section>
      </main>
    </div>
  )
}
