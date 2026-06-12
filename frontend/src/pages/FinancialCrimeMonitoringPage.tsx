import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  evaluateDemoActivity,
  getDemoAlerts,
  getMonitoringControls,
  getRiskScenarios,
  type EvaluateDemoActivityResponse,
  type FinancialCrimeAlert,
  type FinancialCrimeEntityType,
  type MonitoringControl,
  type RiskScenario,
} from '../services/financialCrimeApi'

const entityTypeOptions: FinancialCrimeEntityType[] = [
  'employee',
  'customer',
  'company',
  'account',
  'transaction',
  'wallet',
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

function formatCurrency(value: number) {
  return new Intl.NumberFormat('en-FI', {
    style: 'currency',
    currency: 'EUR',
    maximumFractionDigits: 0,
  }).format(value)
}

export function FinancialCrimeMonitoringPage() {
  const [alerts, setAlerts] = useState<FinancialCrimeAlert[]>([])
  const [controls, setControls] = useState<MonitoringControl[]>([])
  const [scenarios, setScenarios] = useState<RiskScenario[]>([])
  const [selectedScenarioId, setSelectedScenarioId] = useState('')
  const [amount, setAmount] = useState('56000')
  const [entityType, setEntityType] =
    useState<FinancialCrimeEntityType>('transaction')
  const [evaluationResult, setEvaluationResult] =
    useState<EvaluateDemoActivityResponse | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isEvaluating, setIsEvaluating] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const criticalAlerts = alerts.filter(
    (alert) => alert.severity === 'critical',
  ).length
  const reviewReadyCases = alerts.filter(
    (alert) => alert.linked_review_case_id,
  ).length

  const selectedScenario =
    scenarios.find((scenario) => scenario.scenario_id === selectedScenarioId) ??
    scenarios[0]

  const summaryCards = useMemo(
    () => [
      {
        label: 'Active alerts',
        value: alerts.length.toString(),
        detail: 'Deterministic monitoring queue',
      },
      {
        label: 'Critical alerts',
        value: criticalAlerts.toString(),
        detail: 'Require escalation review',
      },
      {
        label: 'Monitoring controls',
        value: controls.length.toString(),
        detail: 'Bank control categories',
      },
      {
        label: 'Review-ready cases',
        value: reviewReadyCases.toString(),
        detail: 'Linked to evidence records',
      },
    ],
    [alerts.length, controls.length, criticalAlerts, reviewReadyCases],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([getRiskScenarios(), getMonitoringControls(), getDemoAlerts()])
      .then(([nextScenarios, nextControls, nextAlerts]) => {
        if (!isActive) {
          return
        }

        setScenarios(nextScenarios)
        setControls(nextControls)
        setAlerts(nextAlerts)
        setSelectedScenarioId(
          (currentScenarioId) =>
            currentScenarioId || nextScenarios[0]?.scenario_id || '',
        )
      })
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Financial crime monitoring data is unavailable in the local prototype.',
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

  async function handleEvaluateActivity() {
    if (!selectedScenario) {
      return
    }

    setIsEvaluating(true)
    setErrorMessage(null)

    try {
      const response = await evaluateDemoActivity({
        scenario_id: selectedScenario.scenario_id,
        amount_eur: Number(amount),
        entity_type: entityType,
      })
      setEvaluationResult(response)
    } catch {
      setErrorMessage('Demo activity evaluation is unavailable.')
    } finally {
      setIsEvaluating(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Protected bank staff area</p>
            <h1>Financial Crime Monitoring</h1>
            <p>
              Internal monitoring view for insider risk, suspicious transaction
              patterns, shell company indicators, crypto off-ramp risk, and
              evidence-driven escalation.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Monitoring alerts
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

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Alert queue</p>
                  <h2>Demo monitoring alerts</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/compliance-intelligence"
                >
                  Compliance intelligence
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {alerts.map((alert) => (
                  <article className="financial-crime-alert" key={alert.alert_id}>
                    <div className="panel-header">
                      <div>
                        <p className="eyebrow">{alert.risk_type}</p>
                        <h3>{alert.title}</h3>
                      </div>
                      <div className="status-label-group">
                        <span
                          className={`risk-label risk-label-${alert.severity}`}
                        >
                          {formatLabel(alert.severity)}
                        </span>
                        <span className={`status-label status-${alert.status}`}>
                          {formatLabel(alert.status)}
                        </span>
                      </div>
                    </div>

                    <div className="summary-list financial-crime-alert-meta">
                      <div>
                        <span>Entity</span>
                        <strong>
                          {alert.entity_name} ({formatLabel(alert.entity_type)})
                        </strong>
                      </div>
                      <div>
                        <span>Amount</span>
                        <strong>{formatCurrency(alert.amount_eur)}</strong>
                      </div>
                      <div>
                        <span>Alert ID</span>
                        <strong>{alert.alert_id}</strong>
                      </div>
                      {alert.linked_review_case_id && (
                        <div>
                          <span>Linked review case</span>
                          <strong>{alert.linked_review_case_id}</strong>
                        </div>
                      )}
                    </div>

                    <div className="financial-crime-evidence">
                      <div>
                        <h4>Triggered rules</h4>
                        <ul>
                          {alert.triggered_rules.map((rule) => (
                            <li key={rule}>{rule}</li>
                          ))}
                        </ul>
                      </div>
                      <div>
                        <h4>Evidence summary</h4>
                        <p>{alert.evidence_summary}</p>
                        <h4>Recommended action</h4>
                        <p>{alert.recommended_action}</p>
                      </div>
                    </div>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Controls</p>
              <h2>Monitoring controls</h2>
              <div className="check-list financial-crime-side-list">
                {controls.map((control) => (
                  <div key={control.control_id}>
                    <span className="status-dot"></span>
                    <span>
                      <strong>{control.title}</strong>
                      <small>{control.category}</small>
                    </span>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Risk library</p>
              <h2>Risk scenarios</h2>
              <div className="financial-crime-side-list">
                {scenarios.map((scenario) => (
                  <div key={scenario.scenario_id}>
                    <strong>{scenario.title}</strong>
                    <p>{scenario.description}</p>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Evaluation demo</p>
                  <h2>Assess activity</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  <span>Scenario</span>
                  <select
                    value={selectedScenarioId}
                    onChange={(event) =>
                      setSelectedScenarioId(event.target.value)
                    }
                  >
                    {scenarios.map((scenario) => (
                      <option
                        key={scenario.scenario_id}
                        value={scenario.scenario_id}
                      >
                        {scenario.title}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Amount EUR</span>
                  <input
                    min="0"
                    type="number"
                    value={amount}
                    onChange={(event) => setAmount(event.target.value)}
                  />
                </label>

                <label>
                  <span>Entity type</span>
                  <select
                    value={entityType}
                    onChange={(event) =>
                      setEntityType(
                        event.target.value as FinancialCrimeEntityType,
                      )
                    }
                  >
                    {entityTypeOptions.map((option) => (
                      <option key={option} value={option}>
                        {formatLabel(option)}
                      </option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleEvaluateActivity()}
                  disabled={isEvaluating || !selectedScenario}
                >
                  Evaluate
                </button>
              </div>

              {evaluationResult && (
                <div className="summary-list">
                  <div>
                    <span>Risk score</span>
                    <strong>{evaluationResult.risk_score}/100</strong>
                  </div>
                  <div>
                    <span>Severity</span>
                    <strong>{formatLabel(evaluationResult.severity)}</strong>
                  </div>
                  <div>
                    <span>Decision</span>
                    <strong>{formatLabel(evaluationResult.decision)}</strong>
                  </div>
                  <div>
                    <span>Triggered rules</span>
                    <strong>
                      {evaluationResult.triggered_rules.map(formatLabel).join(', ')}
                    </strong>
                  </div>
                  <div>
                    <span>Explanation</span>
                    <strong>{evaluationResult.explanation}</strong>
                  </div>
                  <div>
                    <span>Recommended action</span>
                    <strong>{evaluationResult.recommended_action}</strong>
                  </div>
                </div>
              )}
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. Financial crime alerts,
          entities, staff references, companies, wallets, and transactions are
          fictional demo data only.
        </p>
      </main>
    </div>
  )
}
