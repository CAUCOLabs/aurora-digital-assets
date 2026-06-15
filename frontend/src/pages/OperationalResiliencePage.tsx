import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  evaluateResilienceScenario,
  getDependencies,
  getFallbackModes,
  getResilienceControls,
  getResilienceIncidents,
  getServiceHealth,
  type CustomerImpact,
  type DependencyHealth,
  type DependencyStatus,
  type EvaluateResilienceScenarioResponse,
  type FallbackMode,
  type ResilienceControl,
  type ResilienceIncident,
  type ServiceCategory,
  type ServiceHealthStatus,
} from '../services/operationalResilienceApi'

const affectedServiceOptions: ServiceCategory[] = [
  'payments',
  'authentication',
  'digital_assets',
  'core_banking',
  'reporting',
  'staff_operations',
]

const dependencyStatusOptions: DependencyHealth[] = [
  'healthy',
  'degraded',
  'outage',
  'unknown',
]

const customerImpactOptions: CustomerImpact[] = [
  'none',
  'low',
  'medium',
  'high',
  'severe',
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

function formatDateTime(value: string) {
  return new Intl.DateTimeFormat('en-FI', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(new Date(value))
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

function ServiceCard({
  service,
  labels,
}: {
  service: ServiceHealthStatus
  labels: {
    availability: string
    fallbackAvailable: string
    currentMode: string
    recommendedAction: string
    yes: string
    no: string
  }
}) {
  return (
    <article className="financial-crime-alert">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{formatLabel(service.category)}</p>
          <h3>{service.name}</h3>
        </div>
        <div className="status-label-group">
          <span className={`status-label status-${service.status}`}>
            {formatLabel(service.status)}
          </span>
          <span className={`risk-label risk-label-${service.customer_impact}`}>
            {formatLabel(service.customer_impact)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.availability}</span>
          <strong>{service.availability_percent.toFixed(1)}%</strong>
        </div>
        <div>
          <span>{labels.fallbackAvailable}</span>
          <strong>{service.fallback_available ? labels.yes : labels.no}</strong>
        </div>
        <div>
          <span>{labels.currentMode}</span>
          <strong>{formatLabel(service.current_mode)}</strong>
        </div>
        <div>
          <span>{labels.recommendedAction}</span>
          <strong>{service.recommended_action}</strong>
        </div>
      </div>
    </article>
  )
}

function IncidentCard({
  incident,
  labels,
}: {
  incident: ResilienceIncident
  labels: {
    affectedService: string
    failureType: string
    customerImpact: string
    fallbackMode: string
    summary: string
    controlsActivated: string
    pausedOperations: string
    availableOperations: string
    auditEvidence: string
    recommendedAction: string
    timeline: string
  }
}) {
  return (
    <article className="financial-crime-alert evidence-package-card">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{incident.incident_id}</p>
          <h3>{incident.title}</h3>
        </div>
        <div className="status-label-group">
          <span className={`risk-label risk-label-${incident.severity}`}>
            {formatLabel(incident.severity)}
          </span>
          <span className={`status-label status-${incident.status}`}>
            {formatLabel(incident.status)}
          </span>
        </div>
      </div>

      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.affectedService}</span>
          <strong>{incident.affected_service}</strong>
        </div>
        <div>
          <span>{labels.failureType}</span>
          <strong>{formatLabel(incident.failure_type)}</strong>
        </div>
        <div>
          <span>{labels.customerImpact}</span>
          <strong>{formatLabel(incident.customer_impact)}</strong>
        </div>
        <div>
          <span>{labels.fallbackMode}</span>
          <strong>{incident.fallback_mode}</strong>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.summary}</h4>
        <p>{incident.summary}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid">
        <div>
          <h4>{labels.controlsActivated}</h4>
          <StringList items={incident.controls_activated} />
        </div>
        <div>
          <h4>{labels.pausedOperations}</h4>
          <StringList items={incident.paused_operations} />
        </div>
        <div>
          <h4>{labels.availableOperations}</h4>
          <StringList items={incident.available_operations} />
        </div>
        <div>
          <h4>{labels.auditEvidence}</h4>
          <StringList items={incident.audit_evidence} />
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.recommendedAction}</h4>
        <p>{incident.recommended_action}</p>
      </div>

      <div className="evidence-timeline">
        <h4>{labels.timeline}</h4>
        {incident.timeline.map((event) => (
          <div key={event.event_id}>
            <span>{formatDateTime(event.timestamp)}</span>
            <strong>{event.title}</strong>
            <p>
              {event.description} ({formatLabel(event.source_module)})
            </p>
          </div>
        ))}
      </div>
    </article>
  )
}

function DependencyList({ dependencies }: { dependencies: DependencyStatus[] }) {
  return (
    <div className="financial-crime-side-list">
      {dependencies.map((dependency) => (
        <div key={dependency.dependency_id}>
          <strong>{dependency.name}</strong>
          <small>
            {formatLabel(dependency.dependency_type)} ·{' '}
            {formatLabel(dependency.status)}
          </small>
          <p>{dependency.risk_summary}</p>
          <StringList items={dependency.affected_services} />
        </div>
      ))}
    </div>
  )
}

function FallbackList({
  fallbackModes,
  labels,
}: {
  fallbackModes: FallbackMode[]
  labels: {
    allowedOperations: string
    pausedOperations: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {fallbackModes.map((mode) => (
        <div key={mode.fallback_id}>
          <strong>{mode.title}</strong>
          <small>{formatLabel(mode.status)}</small>
          <p>{mode.description}</p>
          {mode.activation_reason && <p>{mode.activation_reason}</p>}
          <h4>{labels.allowedOperations}</h4>
          <StringList items={mode.allowed_operations} />
          <h4>{labels.pausedOperations}</h4>
          <StringList items={mode.paused_operations} />
        </div>
      ))}
    </div>
  )
}

function ControlList({
  controls,
  labels,
}: {
  controls: ResilienceControl[]
  labels: {
    activated: string
    ready: string
  }
}) {
  return (
    <div className="check-list financial-crime-side-list">
      {controls.map((control) => (
        <div key={control.control_id}>
          <span className={control.activated ? 'status-dot' : 'warning-dot'}></span>
          <span>
            <strong>{control.title}</strong>
            <small>
              {control.category} ·{' '}
              {control.activated ? labels.activated : labels.ready}
            </small>
            <p>{control.description}</p>
            <StringList items={control.evidence_outputs} />
          </span>
        </div>
      ))}
    </div>
  )
}

export function OperationalResiliencePage() {
  const { t } = useLanguage()
  const [serviceHealth, setServiceHealth] = useState<ServiceHealthStatus[]>([])
  const [dependencies, setDependencies] = useState<DependencyStatus[]>([])
  const [fallbackModes, setFallbackModes] = useState<FallbackMode[]>([])
  const [controls, setControls] = useState<ResilienceControl[]>([])
  const [incidents, setIncidents] = useState<ResilienceIncident[]>([])
  const [scenarioId, setScenarioId] = useState('payment_dependency_failure')
  const [affectedService, setAffectedService] =
    useState<ServiceCategory>('payments')
  const [dependencyStatus, setDependencyStatus] =
    useState<DependencyHealth>('degraded')
  const [customerImpact, setCustomerImpact] = useState<CustomerImpact>('high')
  const [evaluationResult, setEvaluationResult] =
    useState<EvaluateResilienceScenarioResponse | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isEvaluating, setIsEvaluating] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const activeIncidents = incidents.filter(
    (incident) => incident.status !== 'resolved',
  ).length
  const highImpactServices = serviceHealth.filter((service) =>
    ['high', 'severe'].includes(service.customer_impact),
  ).length

  const summaryCards = useMemo(
    () => [
      {
        label: t.operationalResilience.servicesMonitored,
        value: serviceHealth.length.toString(),
        detail: 'Bank service continuity view',
      },
      {
        label: t.operationalResilience.activeIncidents,
        value: activeIncidents.toString(),
        detail: 'Open, investigating, or mitigated',
      },
      {
        label: t.operationalResilience.fallbackModes,
        value: fallbackModes.length.toString(),
        detail: 'Available or active continuity modes',
      },
      {
        label: t.operationalResilience.highImpactServices,
        value: highImpactServices.toString(),
        detail: 'High or severe customer impact',
      },
    ],
    [
      activeIncidents,
      fallbackModes.length,
      highImpactServices,
      serviceHealth.length,
      t.operationalResilience.activeIncidents,
      t.operationalResilience.fallbackModes,
      t.operationalResilience.highImpactServices,
      t.operationalResilience.servicesMonitored,
    ],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([
      getServiceHealth(),
      getDependencies(),
      getFallbackModes(),
      getResilienceControls(),
      getResilienceIncidents(),
    ])
      .then(
        ([
          nextServiceHealth,
          nextDependencies,
          nextFallbackModes,
          nextControls,
          nextIncidents,
        ]) => {
          if (!isActive) {
            return
          }

          setServiceHealth(nextServiceHealth)
          setDependencies(nextDependencies)
          setFallbackModes(nextFallbackModes)
          setControls(nextControls)
          setIncidents(nextIncidents)
        },
      )
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Operational resilience data is unavailable in the local prototype.',
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
      const response = await evaluateResilienceScenario({
        scenario_id: scenarioId,
        affected_service: affectedService,
        dependency_status: dependencyStatus,
        customer_impact: customerImpact,
      })
      setEvaluationResult(response)
    } catch {
      setErrorMessage('The operational resilience scenario could not be evaluated.')
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
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.operationalResilience.title}</h1>
            <p>{t.operationalResilience.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankStaffWorkspace.statuses.resilienceCommand}
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

        <section className="content-grid compliance-intelligence-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">
                    {t.operationalResilience.serviceHealth}
                  </p>
                  <h2>{t.operationalResilience.serviceHealth}</h2>
                </div>
                <Link
                  className="button-link secondary-button compact-link"
                  to="/bank-staff/evidence-packages"
                >
                  {t.evidencePackages.title}
                </Link>
              </div>

              <div className="financial-crime-alert-list">
                {serviceHealth.map((service) => (
                  <ServiceCard
                    service={service}
                    labels={{
                      availability: t.operationalResilience.availability,
                      fallbackAvailable:
                        t.operationalResilience.fallbackAvailable,
                      currentMode: t.operationalResilience.currentMode,
                      recommendedAction:
                        t.operationalResilience.recommendedAction,
                      yes: t.common.yes,
                      no: t.common.no,
                    }}
                    key={service.service_id}
                  />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">
                    {t.operationalResilience.incidentQueue}
                  </p>
                  <h2>{t.operationalResilience.incidentQueue}</h2>
                </div>
              </div>

              <div className="financial-crime-alert-list">
                {incidents.map((incident) => (
                  <IncidentCard
                    incident={incident}
                    labels={{
                      affectedService:
                        t.operationalResilience.affectedService,
                      failureType: t.operationalResilience.failureType,
                      customerImpact: t.operationalResilience.customerImpact,
                      fallbackMode: t.operationalResilience.fallbackMode,
                      summary: t.operationalResilience.summary,
                      controlsActivated:
                        t.operationalResilience.controlsActivated,
                      pausedOperations:
                        t.operationalResilience.pausedOperations,
                      availableOperations:
                        t.operationalResilience.availableOperations,
                      auditEvidence: t.operationalResilience.auditEvidence,
                      recommendedAction:
                        t.operationalResilience.recommendedAction,
                      timeline: t.operationalResilience.timeline,
                    }}
                    key={incident.incident_id}
                  />
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.operationalResilience.dependencies}</p>
              <h2>{t.operationalResilience.criticalDependencies}</h2>
              <DependencyList dependencies={dependencies} />
            </Panel>

            <Panel>
              <p className="eyebrow">{t.operationalResilience.fallbackModes}</p>
              <h2>{t.operationalResilience.fallbackModes}</h2>
              <FallbackList
                fallbackModes={fallbackModes}
                labels={{
                  allowedOperations: t.operationalResilience.allowedOperations,
                  pausedOperations: t.operationalResilience.pausedOperations,
                }}
              />
            </Panel>

            <Panel>
              <p className="eyebrow">{t.operationalResilience.controls}</p>
              <h2>{t.operationalResilience.resilienceControls}</h2>
              <ControlList
                controls={controls}
                labels={{
                  activated: t.operationalResilience.activated,
                  ready: t.operationalResilience.ready,
                }}
              />
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.operationalResilience.scenarioDemo}</p>
              <h2>{t.operationalResilience.evaluateScenario}</h2>

              <div className="form-grid">
                <label>
                  <span>{t.operationalResilience.scenario}</span>
                  <input
                    value={scenarioId}
                    onChange={(event) => setScenarioId(event.target.value)}
                  />
                </label>

                <label>
                  <span>{t.operationalResilience.affectedService}</span>
                  <select
                    value={affectedService}
                    onChange={(event) =>
                      setAffectedService(event.target.value as ServiceCategory)
                    }
                  >
                    {affectedServiceOptions.map((option) => (
                      <option value={option} key={option}>
                        {formatLabel(option)}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.operationalResilience.dependencyStatus}</span>
                  <select
                    value={dependencyStatus}
                    onChange={(event) =>
                      setDependencyStatus(event.target.value as DependencyHealth)
                    }
                  >
                    {dependencyStatusOptions.map((option) => (
                      <option value={option} key={option}>
                        {formatLabel(option)}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{t.operationalResilience.customerImpact}</span>
                  <select
                    value={customerImpact}
                    onChange={(event) =>
                      setCustomerImpact(event.target.value as CustomerImpact)
                    }
                  >
                    {customerImpactOptions.map((option) => (
                      <option value={option} key={option}>
                        {formatLabel(option)}
                      </option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleEvaluateScenario()}
                  disabled={isEvaluating}
                >
                  {t.operationalResilience.evaluateResilienceScenario}
                </button>
              </div>

              {evaluationResult && (
                <div className="summary-list">
                  <div>
                    <span>{t.operationalResilience.resilienceScore}</span>
                    <strong>{evaluationResult.resilience_score}/100</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.severity}</span>
                    <strong>{formatLabel(evaluationResult.severity)}</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.decision}</span>
                    <strong>{formatLabel(evaluationResult.decision)}</strong>
                  </div>
                  <div>
                    <span>{t.operationalResilience.controlsActivated}</span>
                    <StringList items={evaluationResult.controls_activated} />
                  </div>
                  <div>
                    <span>{t.operationalResilience.availableOperations}</span>
                    <StringList items={evaluationResult.available_operations} />
                  </div>
                  <div>
                    <span>{t.operationalResilience.pausedOperations}</span>
                    <StringList items={evaluationResult.paused_operations} />
                  </div>
                  <div>
                    <span>{t.common.auditEventCreated}</span>
                    <strong>
                      {evaluationResult.audit_event_created
                        ? t.common.yes
                        : t.common.no}
                    </strong>
                  </div>
                  <div>
                    <span>{t.common.auditEventId}</span>
                    <strong>{evaluationResult.audit_event_id}</strong>
                  </div>
                  <div>
                    <span>{t.common.correlationId}</span>
                    <strong>{evaluationResult.correlation_id}</strong>
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
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. Operational resilience
          incidents, dependencies, controls, audit evidence, and availability
          states are fictional deterministic demo data only.
        </p>
      </main>
    </div>
  )
}
