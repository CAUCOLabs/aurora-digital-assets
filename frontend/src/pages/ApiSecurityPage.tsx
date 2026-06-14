import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  evaluateApiSecurityScenario,
  getApiSecurityControls,
  getApiSecurityEvents,
  getApiSecurityScenarios,
  getApiSecuritySurfaces,
  getApiSensitiveOperations,
  type ApiSecurityControl,
  type ApiSecurityDecision,
  type ApiSecurityEvent,
  type ApiSecurityScenario,
  type ApiSecuritySurface,
  type ApiSensitiveOperation,
  type EvaluateApiSecurityScenarioResponse,
} from '../services/apiSecurityApi'

function formatLabel(value: string) {
  return value
    .replaceAll('_', ' ')
    .replaceAll('-', ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase()
    .replace(/^\w/, (letter) => letter.toUpperCase())
}

function StringList({ items }: { items: string[] }) {
  return (
    <ul className="compact-list">
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  )
}

function EventCard({
  event,
  labels,
}: {
  event: ApiSecurityEvent
  labels: {
    apiSurface: string
    operationName: string
    riskType: string
    businessAction: string
    affectedObject: string
    summary: string
    triggeredControls: string
    recommendedAction: string
    auditEvent: string
  }
}) {
  return (
    <article className="financial-crime-alert evidence-package-card">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{event.event_id}</p>
          <h3>{event.title}</h3>
        </div>
        <div className="status-label-group">
          <span className={`risk-label risk-label-${event.severity}`}>
            {formatLabel(event.severity)}
          </span>
          <span className={`decision-label decision-label-${event.decision}`}>
            {formatLabel(event.decision)}
          </span>
          <span className={`status-label status-${event.status}`}>
            {formatLabel(event.status)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.apiSurface}</span>
          <strong>{formatLabel(event.api_surface)}</strong>
        </div>
        <div>
          <span>{labels.operationName}</span>
          <strong>{event.operation_name}</strong>
        </div>
        <div>
          <span>{labels.riskType}</span>
          <strong>{event.risk_type}</strong>
        </div>
        <div>
          <span>{labels.businessAction}</span>
          <strong>{event.business_action}</strong>
        </div>
        {event.affected_object && (
          <div>
            <span>{labels.affectedObject}</span>
            <strong>{event.affected_object}</strong>
          </div>
        )}
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.summary}</h4>
        <p>{event.summary}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid">
        <div>
          <h4>{labels.triggeredControls}</h4>
          <StringList items={event.triggered_controls} />
        </div>
        <div>
          <h4>{labels.auditEvent}</h4>
          <p>{event.audit_event}</p>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.recommendedAction}</h4>
        <p>{event.recommended_action}</p>
      </div>
    </article>
  )
}

function ControlCard({
  control,
  labels,
}: {
  control: ApiSecurityControl
  labels: {
    category: string
    enabled: string
    disabled: string
    protectedOperations: string
    decisionModel: string
    evidenceOutputs: string
  }
}) {
  return (
    <article className="financial-crime-alert">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{formatLabel(control.category)}</p>
          <h3>{control.title}</h3>
        </div>
        <span className={`status-label status-${control.enabled ? 'ready' : 'blocked'}`}>
          {control.enabled ? labels.enabled : labels.disabled}
        </span>
      </div>
      <p>{control.description}</p>
      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.category}</span>
          <strong>{formatLabel(control.category)}</strong>
        </div>
        <div>
          <span>{labels.decisionModel}</span>
          <strong>{control.decision_model}</strong>
        </div>
      </div>
      <div className="financial-crime-evidence compliance-evidence-grid">
        <div>
          <h4>{labels.protectedOperations}</h4>
          <StringList items={control.protected_operations} />
        </div>
        <div>
          <h4>{labels.evidenceOutputs}</h4>
          <StringList items={control.evidence_outputs} />
        </div>
      </div>
    </article>
  )
}

function OperationList({
  operations,
  labels,
}: {
  operations: ApiSensitiveOperation[]
  labels: {
    category: string
    requiredControls: string
    auditRequired: string
    stepUpRequired: string
    batchingAllowed: string
    yes: string
    no: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {operations.map((operation) => (
        <div key={operation.operation_id}>
          <div className="panel-header compact-panel-header">
            <div>
              <strong>{operation.name}</strong>
              <small>
                {labels.category}: {formatLabel(operation.category)}
              </small>
            </div>
            <span className={`risk-label risk-label-${operation.risk_level}`}>
              {formatLabel(operation.risk_level)}
            </span>
          </div>
          <div className="summary-list">
            <div>
              <span>{labels.auditRequired}</span>
              <strong>{operation.audit_required ? labels.yes : labels.no}</strong>
            </div>
            <div>
              <span>{labels.stepUpRequired}</span>
              <strong>{operation.step_up_required ? labels.yes : labels.no}</strong>
            </div>
            <div>
              <span>{labels.batchingAllowed}</span>
              <strong>{operation.batching_allowed ? labels.yes : labels.no}</strong>
            </div>
          </div>
          <h4>{labels.requiredControls}</h4>
          <StringList items={operation.required_controls} />
        </div>
      ))}
    </div>
  )
}

function SurfaceList({
  surfaces,
  labels,
}: {
  surfaces: ApiSecuritySurface[]
  labels: {
    sensitiveOperations: string
    controlsApplied: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {surfaces.map((surface) => (
        <div key={surface.surface_id}>
          <div className="panel-header compact-panel-header">
            <div>
              <strong>{surface.name}</strong>
              <small>{formatLabel(surface.surface_type)}</small>
            </div>
            <span className={`status-label status-${surface.status}`}>
              {formatLabel(surface.status)}
            </span>
          </div>
          <p>{surface.risk_summary}</p>
          <h4>{labels.sensitiveOperations}</h4>
          <StringList items={surface.sensitive_operations} />
          <h4>{labels.controlsApplied}</h4>
          <StringList items={surface.controls_applied} />
        </div>
      ))}
    </div>
  )
}

function ScenarioList({
  scenarios,
  labels,
}: {
  scenarios: ApiSecurityScenario[]
  labels: {
    expectedDecision: string
    riskIndicators: string
    recommendedControls: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {scenarios.map((scenario) => (
        <div key={scenario.scenario_id}>
          <strong>{scenario.title}</strong>
          <small>
            {labels.expectedDecision}: {formatLabel(scenario.expected_decision)}
          </small>
          <p>{scenario.description}</p>
          <h4>{labels.riskIndicators}</h4>
          <StringList items={scenario.risk_indicators} />
          <h4>{labels.recommendedControls}</h4>
          <StringList items={scenario.recommended_controls} />
        </div>
      ))}
    </div>
  )
}

export function ApiSecurityPage() {
  const { t } = useLanguage()
  const [controls, setControls] = useState<ApiSecurityControl[]>([])
  const [events, setEvents] = useState<ApiSecurityEvent[]>([])
  const [surfaces, setSurfaces] = useState<ApiSecuritySurface[]>([])
  const [operations, setOperations] = useState<ApiSensitiveOperation[]>([])
  const [scenarios, setScenarios] = useState<ApiSecurityScenario[]>([])
  const [scenarioId, setScenarioId] = useState('graphql_batching_pin_verification')
  const [operationName, setOperationName] = useState('verifyTransferPin')
  const [attempts, setAttempts] = useState(8)
  const [objectAuthorized, setObjectAuthorized] = useState(true)
  const [batchingDetected, setBatchingDetected] = useState(true)
  const [sensitiveFieldsRequested, setSensitiveFieldsRequested] = useState(false)
  const [evaluationResult, setEvaluationResult] =
    useState<EvaluateApiSecurityScenarioResponse | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isEvaluating, setIsEvaluating] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const blockedOrStepUp = events.filter((event) =>
    ['block', 'step_up_required'].includes(event.decision),
  ).length

  const summaryCards = useMemo(
    () => [
      {
        label: t.apiSecurity.securityControls,
        value: controls.length.toString(),
        detail: t.apiSecurity.backendControlLayer,
      },
      {
        label: t.apiSecurity.securityEvents,
        value: events.length.toString(),
        detail: t.apiSecurity.auditReadySignals,
      },
      {
        label: t.apiSecurity.sensitiveOperations,
        value: operations.length.toString(),
        detail: t.apiSecurity.businessActionBoundary,
      },
      {
        label: t.apiSecurity.blockedOrStepUpDecisions,
        value: blockedOrStepUp.toString(),
        detail: t.apiSecurity.customerProtectionDecisions,
      },
    ],
    [
      blockedOrStepUp,
      controls.length,
      events.length,
      operations.length,
      t.apiSecurity.auditReadySignals,
      t.apiSecurity.backendControlLayer,
      t.apiSecurity.blockedOrStepUpDecisions,
      t.apiSecurity.businessActionBoundary,
      t.apiSecurity.customerProtectionDecisions,
      t.apiSecurity.securityControls,
      t.apiSecurity.securityEvents,
      t.apiSecurity.sensitiveOperations,
    ],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([
      getApiSecurityControls(),
      getApiSecurityEvents(),
      getApiSecuritySurfaces(),
      getApiSensitiveOperations(),
      getApiSecurityScenarios(),
    ])
      .then(
        ([
          nextControls,
          nextEvents,
          nextSurfaces,
          nextOperations,
          nextScenarios,
        ]) => {
          if (!isActive) {
            return
          }

          setControls(nextControls)
          setEvents(nextEvents)
          setSurfaces(nextSurfaces)
          setOperations(nextOperations)
          setScenarios(nextScenarios)
        },
      )
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'API security data is unavailable in the local prototype.',
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

  async function handleEvaluateScenario() {
    setIsEvaluating(true)
    setErrorMessage(null)

    try {
      const response = await evaluateApiSecurityScenario({
        scenario_id: scenarioId,
        operation_name: operationName,
        attempts,
        object_authorized: objectAuthorized,
        batching_detected: batchingDetected,
        sensitive_fields_requested: sensitiveFieldsRequested,
      })
      setEvaluationResult(response)
    } catch {
      setErrorMessage('The API security scenario could not be evaluated.')
    } finally {
      setIsEvaluating(false)
    }
  }

  const decisionClass = (decision: ApiSecurityDecision) =>
    `decision-label decision-label-${decision}`

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.apiSecurity.title}</h1>
            <p>{t.apiSecurity.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankStaffWorkspace.statuses.backendSecurityLayer}
          </div>
        </section>

        {errorMessage && <p className="panel-note">{errorMessage}</p>}

        <Panel className="risk-operations-command">
          <div className="panel-header">
            <div>
              <p className="eyebrow">{t.apiSecurity.securityBoundary}</p>
              <h2>{t.apiSecurity.commandBannerTitle}</h2>
            </div>
            <Link
              className="button-link secondary-button compact-link"
              to="/bank-staff/risk-operations"
            >
              {t.riskOperations.title}
            </Link>
          </div>
          <p>{t.apiSecurity.commandBannerText}</p>
        </Panel>

        <section className="assets-summary financial-crime-summary">
          {summaryCards.map((card) => (
            <div key={card.label}>
              <p>{card.label}</p>
              <strong>{isLoading ? '...' : card.value}</strong>
              <span>{card.detail}</span>
            </div>
          ))}
        </section>

        <section className="content-grid compliance-intelligence-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.apiSecurity.eventQueue}</p>
                  <h2>{t.apiSecurity.apiSecurityEvents}</h2>
                </div>
              </div>

              <div className="financial-crime-alert-list">
                {events.map((event) => (
                  <EventCard
                    event={event}
                    labels={{
                      apiSurface: t.apiSecurity.apiSurface,
                      operationName: t.apiSecurity.operationName,
                      riskType: t.evidencePackages.riskType,
                      businessAction: t.apiSecurity.businessAction,
                      affectedObject: t.apiSecurity.affectedObject,
                      summary: t.evidencePackages.summary,
                      triggeredControls: t.evidencePackages.triggeredControls,
                      recommendedAction:
                        t.operationalResilience.recommendedAction,
                      auditEvent: t.apiSecurity.auditEvent,
                    }}
                    key={event.event_id}
                  />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.apiSecurity.controlCatalog}</p>
                  <h2>{t.apiSecurity.securityControls}</h2>
                </div>
              </div>
              <div className="financial-crime-alert-list">
                {controls.map((control) => (
                  <ControlCard
                    control={control}
                    labels={{
                      category: t.apiSecurity.category,
                      enabled: t.apiSecurity.enabled,
                      disabled: t.apiSecurity.disabled,
                      protectedOperations: t.apiSecurity.protectedOperations,
                      decisionModel: t.apiSecurity.decisionModel,
                      evidenceOutputs: t.apiSecurity.evidenceOutputs,
                    }}
                    key={control.control_id}
                  />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.apiSecurity.sensitiveOperations}</p>
                  <h2>{t.apiSecurity.sensitiveOperations}</h2>
                </div>
              </div>
              <OperationList
                operations={operations}
                labels={{
                  category: t.apiSecurity.category,
                  requiredControls: t.apiSecurity.requiredControls,
                  auditRequired: t.apiSecurity.auditRequired,
                  stepUpRequired: t.apiSecurity.stepUpRequired,
                  batchingAllowed: t.apiSecurity.batchingAllowed,
                  yes: t.common.yes,
                  no: t.common.no,
                }}
              />
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.apiSecurity.apiSurfaces}</p>
              <h2>{t.apiSecurity.apiSurfaces}</h2>
              <SurfaceList
                surfaces={surfaces}
                labels={{
                  sensitiveOperations: t.apiSecurity.sensitiveOperations,
                  controlsApplied: t.apiSecurity.controlsApplied,
                }}
              />
            </Panel>

            <Panel>
              <p className="eyebrow">{t.apiSecurity.securityScenarios}</p>
              <h2>{t.apiSecurity.securityScenarios}</h2>
              <ScenarioList
                scenarios={scenarios}
                labels={{
                  expectedDecision: t.apiSecurity.expectedDecision,
                  riskIndicators: t.apiSecurity.riskIndicators,
                  recommendedControls: t.apiSecurity.recommendedControls,
                }}
              />
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.apiSecurity.scenarioDemo}</p>
              <h2>{t.apiSecurity.evaluateApiScenario}</h2>

              <div className="form-grid">
                <label>
                  <span>{t.operationalResilience.scenario}</span>
                  <select
                    value={scenarioId}
                    onChange={(event) => setScenarioId(event.target.value)}
                  >
                    {scenarios.map((scenario) => (
                      <option value={scenario.scenario_id} key={scenario.scenario_id}>
                        {scenario.title}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.apiSecurity.operationName}</span>
                  <select
                    value={operationName}
                    onChange={(event) => setOperationName(event.target.value)}
                  >
                    {operations.map((operation) => (
                      <option value={operation.name} key={operation.operation_id}>
                        {operation.name}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.apiSecurity.attempts}</span>
                  <input
                    min="0"
                    type="number"
                    value={attempts}
                    onChange={(event) => setAttempts(Number(event.target.value))}
                  />
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={objectAuthorized}
                    type="checkbox"
                    onChange={(event) => setObjectAuthorized(event.target.checked)}
                  />
                  <span>{t.apiSecurity.objectAuthorized}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={batchingDetected}
                    type="checkbox"
                    onChange={(event) => setBatchingDetected(event.target.checked)}
                  />
                  <span>{t.apiSecurity.batchingDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={sensitiveFieldsRequested}
                    type="checkbox"
                    onChange={(event) =>
                      setSensitiveFieldsRequested(event.target.checked)
                    }
                  />
                  <span>{t.apiSecurity.sensitiveFieldsRequested}</span>
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleEvaluateScenario()}
                  disabled={isEvaluating}
                >
                  {t.apiSecurity.evaluateApiScenario}
                </button>
              </div>

              {evaluationResult && (
                <div className="summary-list">
                  <div>
                    <span>{t.apiSecurity.riskScore}</span>
                    <strong>{evaluationResult.risk_score}/100</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.severity}</span>
                    <strong>{formatLabel(evaluationResult.severity)}</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.decision}</span>
                    <strong className={decisionClass(evaluationResult.decision)}>
                      {formatLabel(evaluationResult.decision)}
                    </strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.triggeredControls}</span>
                    <StringList items={evaluationResult.triggered_controls} />
                  </div>
                  <div>
                    <span>{t.apiSecurity.auditEventRequired}</span>
                    <strong>
                      {evaluationResult.audit_event_required
                        ? t.common.yes
                        : t.common.no}
                    </strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.recommendedAction}</span>
                    <strong>{evaluationResult.recommended_action}</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.explanation}</span>
                    <strong>{evaluationResult.explanation}</strong>
                  </div>
                </div>
              )}
            </Panel>

            <Panel>
              <p className="eyebrow">{t.apiSecurity.goldenRules}</p>
              <h2>{t.apiSecurity.goldenRules}</h2>
              <div className="check-list">
                {t.apiSecurity.goldenRuleItems.map((rule) => (
                  <div key={rule}>
                    <span className="status-dot"></span>
                    {rule}
                  </div>
                ))}
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          {t.apiSecurity.prototypeDisclaimer}
        </p>
      </main>
    </div>
  )
}
