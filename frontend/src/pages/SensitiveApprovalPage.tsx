import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  evaluateSensitiveApproval,
  getSensitiveApprovalOperations,
  getSensitiveApprovalScenarios,
  type MobileApprovalStatus,
  type SensitiveActorType,
  type SensitiveApprovalRequest,
  type SensitiveApprovalResponse,
  type SensitiveApprovalScenario,
  type SensitiveOperation,
} from '../services/sensitiveApprovalApi'

const defaultPayload: SensitiveApprovalRequest = {
  operation_type: 'external_wallet_withdrawal',
  actor_id: 'customer-demo',
  actor_type: 'customer',
  amount_eur: 8000,
  asset: 'BTC',
  destination_type: 'external_wallet',
  destination_id: 'new-wallet-demo',
  is_new_destination: true,
  customer_confirmed: true,
  mobile_approval_status: 'approved',
  device_trusted: true,
  session_age_minutes: 4,
}

function formatLabel(value: string) {
  return value
    .replaceAll('_', ' ')
    .replaceAll('-', ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase()
    .replace(/^\w/, (letter) => letter.toUpperCase())
}

function StringList({ items }: { items: readonly string[] }) {
  return (
    <ul className="compact-list">
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  )
}

export function SensitiveApprovalPage() {
  const { t } = useLanguage()
  const labels = t.sensitiveApproval
  const [operations, setOperations] = useState<SensitiveOperation[]>([])
  const [scenarios, setScenarios] = useState<SensitiveApprovalScenario[]>([])
  const [payload, setPayload] =
    useState<SensitiveApprovalRequest>(defaultPayload)
  const [result, setResult] = useState<SensitiveApprovalResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [evaluating, setEvaluating] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true

    async function loadData() {
      try {
        const [operationData, scenarioData] = await Promise.all([
          getSensitiveApprovalOperations(),
          getSensitiveApprovalScenarios(),
        ])
        if (!mounted) return
        setOperations(operationData)
        setScenarios(scenarioData)
      } catch (loadError) {
        if (mounted) {
          setError(loadError instanceof Error ? loadError.message : String(loadError))
        }
      } finally {
        if (mounted) setLoading(false)
      }
    }

    loadData()
    return () => {
      mounted = false
    }
  }, [])

  const metrics = useMemo(
    () => [
      { label: labels.operationCatalog, value: operations.length },
      {
        label: labels.approvalRequired,
        value: operations.filter((operation) => operation.approval_required).length,
      },
      {
        label: labels.mobileApprovalSimulated,
        value: operations.filter(
          (operation) => operation.step_up_method === 'mobile_approval_simulated',
        ).length,
      },
    ],
    [labels, operations],
  )

  function applyScenario(scenarioId: string) {
    const scenario = scenarios.find((item) => item.scenario_id === scenarioId)
    if (scenario) {
      setPayload(scenario.sample_payload)
      setResult(null)
    }
  }

  async function handleEvaluate() {
    setEvaluating(true)
    setError(null)
    try {
      setResult(await evaluateSensitiveApproval(payload))
    } catch (evaluateError) {
      setError(
        evaluateError instanceof Error
          ? evaluateError.message
          : String(evaluateError),
      )
    } finally {
      setEvaluating(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{labels.stepUpApproval}</p>
            <h1>{labels.title}</h1>
            <p>{labels.subtitle}</p>
          </div>
          <Link className="button-link secondary-button" to="/bank-staff">
            {t.common.back}
          </Link>
        </section>

        <Panel className="risk-panel">
          <p className="eyebrow">{labels.bankStyleStrongApproval}</p>
          <h2>{labels.conceptBannerTitle}</h2>
          <div className="check-list">
            {labels.conceptRules.map((rule) => (
              <div key={rule}>
                <span className="status-dot"></span>
                {rule}
              </div>
            ))}
          </div>
        </Panel>

        {error && (
          <Panel className="risk-panel">
            <p className="eyebrow">{t.common.error}</p>
            <p>{error}</p>
          </Panel>
        )}

        <section className="metric-grid">
          {metrics.map((metric) => (
            <Panel className="metric-card" key={metric.label}>
              <span>{metric.label}</span>
              <strong>{loading ? '...' : metric.value}</strong>
            </Panel>
          ))}
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.operationCatalog}</p>
                  <h2>{labels.sensitiveOperations}</h2>
                </div>
              </div>
              <div className="account-list">
                {operations.map((operation) => (
                  <article className="account-row" key={operation.operation_id}>
                    <div>
                      <h3>{operation.title}</h3>
                      <p>{operation.description}</p>
                      <span>
                        {formatLabel(operation.operation_type)} ·{' '}
                        {formatLabel(operation.step_up_method)}
                      </span>
                    </div>
                    <strong>{formatLabel(operation.sensitivity_level)}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.finnishModel}</p>
                  <h2>{labels.bankStyleStrongApproval}</h2>
                </div>
              </div>
              <p>{labels.finnishModelCopy}</p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{labels.scenarioEvaluator}</p>
              <h2>{labels.backendRiskDecision}</h2>
              <div className="form-grid">
                <label>
                  <span>{labels.scenarioEvaluator}</span>
                  <select onChange={(event) => applyScenario(event.target.value)}>
                    <option value="">Select scenario</option>
                    {scenarios.map((scenario) => (
                      <option key={scenario.scenario_id} value={scenario.scenario_id}>
                        {scenario.title}
                      </option>
                    ))}
                  </select>
                </label>
                <label>
                  <span>{labels.actorType}</span>
                  <select
                    value={payload.actor_type}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        actor_type: event.target.value as SensitiveActorType,
                      }))
                    }
                  >
                    {(['customer', 'staff', 'reviewer', 'admin'] as const).map(
                      (actorType) => (
                        <option key={actorType} value={actorType}>
                          {formatLabel(actorType)}
                        </option>
                      ),
                    )}
                  </select>
                </label>
                <label>
                  <span>{labels.operationType}</span>
                  <select
                    value={payload.operation_type}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        operation_type: event.target.value,
                      }))
                    }
                  >
                    {operations.map((operation) => (
                      <option key={operation.operation_type} value={operation.operation_type}>
                        {operation.title}
                      </option>
                    ))}
                  </select>
                </label>
                <label>
                  <span>{labels.amountEur}</span>
                  <input
                    type="number"
                    value={payload.amount_eur ?? 0}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        amount_eur: Number(event.target.value),
                      }))
                    }
                  />
                </label>
                <label>
                  <span>{labels.asset}</span>
                  <input
                    value={payload.asset ?? ''}
                    onChange={(event) =>
                      setPayload((current) => ({ ...current, asset: event.target.value }))
                    }
                  />
                </label>
                <label>
                  <span>{labels.mobileApprovalStatus}</span>
                  <select
                    value={payload.mobile_approval_status ?? 'pending'}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        mobile_approval_status: event.target.value as MobileApprovalStatus,
                      }))
                    }
                  >
                    {(['pending', 'approved', 'rejected', 'expired'] as const).map(
                      (status) => (
                        <option key={status} value={status}>
                          {labels.statuses[status]}
                        </option>
                      ),
                    )}
                  </select>
                </label>
              </div>
              <div className="check-list approval-check-list">
                <label>
                  <input
                    type="checkbox"
                    checked={payload.is_new_destination ?? false}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        is_new_destination: event.target.checked,
                      }))
                    }
                  />
                  {labels.isNewDestination}
                </label>
                <label>
                  <input
                    type="checkbox"
                    checked={payload.device_trusted ?? true}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        device_trusted: event.target.checked,
                      }))
                    }
                  />
                  {labels.deviceTrusted}
                </label>
                <label>
                  <input
                    type="checkbox"
                    checked={payload.customer_confirmed ?? false}
                    onChange={(event) =>
                      setPayload((current) => ({
                        ...current,
                        customer_confirmed: event.target.checked,
                      }))
                    }
                  />
                  {labels.customerConfirmed}
                </label>
              </div>
              <button
                className="primary-action approval-action"
                type="button"
                disabled={evaluating}
                onClick={handleEvaluate}
              >
                {evaluating ? t.common.loading : labels.evaluate}
              </button>
            </Panel>

            {result && (
              <Panel>
                <p className="eyebrow">{labels.backendRiskDecision}</p>
                <h2>{formatLabel(result.backend_risk_decision)}</h2>
                <div className="summary-list">
                  <div>
                    <span>{labels.approvalRequired}</span>
                    <strong>{result.approval_required ? t.common.yes : t.common.no}</strong>
                  </div>
                  <div>
                    <span>{labels.stepUpApproval}</span>
                    <strong>{formatLabel(result.step_up_method)}</strong>
                  </div>
                  <div>
                    <span>{labels.mobileApprovalStatus}</span>
                    <strong>{labels.statuses[result.mobile_approval_status]}</strong>
                  </div>
                  <div>
                    <span>{labels.riskLevel}</span>
                    <strong>{formatLabel(result.risk_level)}</strong>
                  </div>
                  <div>
                    <span>{labels.riskScore}</span>
                    <strong>{result.risk_score}/100</strong>
                  </div>
                  <div>
                    <span>{t.common.auditEventId}</span>
                    <strong>{result.audit_event_id}</strong>
                  </div>
                  <div>
                    <span>{t.common.correlationId}</span>
                    <strong>{result.correlation_id}</strong>
                  </div>
                  <div>
                    <span>{labels.evidencePackageReady}</span>
                    <strong>{result.evidence_package_ready ? t.common.yes : t.common.no}</strong>
                  </div>
                  <div>
                    <span>{labels.reviewCaseRequired}</span>
                    <strong>{result.review_case_required ? t.common.yes : t.common.no}</strong>
                  </div>
                  <div>
                    <span>{t.riskOperations.reviewCaseId}</span>
                    <strong>{result.review_case_id ?? 'Not required'}</strong>
                  </div>
                </div>
                <h4>{labels.reasons}</h4>
                <StringList items={result.reasons} />
                <h4>{labels.recommendedNextAction}</h4>
                <p>{formatLabel(result.recommended_next_action)}</p>
                <p>{result.user_message}</p>
              </Panel>
            )}
          </aside>
        </section>

        <p className="disclaimer">{labels.prototypeDisclaimer}</p>
      </main>
    </div>
  )
}
