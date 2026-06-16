import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  evaluateInfrastructureSecurityScenario,
  getInfrastructureSecurityControls,
  getInfrastructureSecurityEvents,
  getInfrastructureSecurityLayers,
  getInfrastructureSecurityScenarios,
  type EvaluateInfrastructureSecurityScenarioResponse,
  type InfrastructureSecurityControl,
  type InfrastructureSecurityDecision,
  type InfrastructureSecurityEvent,
  type InfrastructureSecurityLayer,
  type InfrastructureSecurityScenario,
} from '../services/infrastructureSecurityApi'

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
  event: InfrastructureSecurityEvent
  labels: {
    affectedLayer: string
    chainStage: string
    riskType: string
    affectedAsset: string
    summary: string
    chainReactionRisk: string
    triggeredControls: string
    recommendedAction: string
    evidencePackageReady: string
    auditEventId: string
    correlationId: string
    yes: string
    no: string
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
          <span>{labels.affectedLayer}</span>
          <strong>{formatLabel(event.affected_layer)}</strong>
        </div>
        <div>
          <span>{labels.chainStage}</span>
          <strong>{formatLabel(event.chain_stage)}</strong>
        </div>
        <div>
          <span>{labels.riskType}</span>
          <strong>{event.risk_type}</strong>
        </div>
        <div>
          <span>{labels.affectedAsset}</span>
          <strong>{event.affected_asset}</strong>
        </div>
        <div>
          <span>{labels.evidencePackageReady}</span>
          <strong>{event.evidence_package_ready ? labels.yes : labels.no}</strong>
        </div>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.summary}</h4>
        <p>{event.summary}</p>
      </div>

      <div className="compliance-reasoning-block">
        <h4>{labels.chainReactionRisk}</h4>
        <p>{event.chain_reaction_risk}</p>
      </div>

      <div className="financial-crime-evidence compliance-evidence-grid">
        <div>
          <h4>{labels.triggeredControls}</h4>
          <StringList items={event.triggered_controls} />
        </div>
        <div>
          <h4>{labels.auditEventId}</h4>
          <p>{event.audit_event_id ?? '-'}</p>
          <h4>{labels.correlationId}</h4>
          <p>{event.correlation_id ?? '-'}</p>
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
  control: InfrastructureSecurityControl
  labels: {
    layer: string
    category: string
    enabled: string
    disabled: string
    protectedAssets: string
    decisionModel: string
    evidenceOutputs: string
  }
}) {
  return (
    <article className="financial-crime-alert">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{formatLabel(control.layer)}</p>
          <h3>{control.title}</h3>
        </div>
        <span className={`status-label status-${control.enabled ? 'ready' : 'blocked'}`}>
          {control.enabled ? labels.enabled : labels.disabled}
        </span>
      </div>
      <p>{control.description}</p>
      <div className="summary-list financial-crime-alert-meta">
        <div>
          <span>{labels.layer}</span>
          <strong>{formatLabel(control.layer)}</strong>
        </div>
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
          <h4>{labels.protectedAssets}</h4>
          <StringList items={control.protected_assets} />
        </div>
        <div>
          <h4>{labels.evidenceOutputs}</h4>
          <StringList items={control.evidence_outputs} />
        </div>
      </div>
    </article>
  )
}

function LayerList({
  layers,
  labels,
}: {
  layers: InfrastructureSecurityLayer[]
  labels: {
    controlsApplied: string
    monitoredSignals: string
  }
}) {
  return (
    <div className="financial-crime-side-list">
      {layers.map((layer) => (
        <div key={layer.layer_id}>
          <div className="panel-header compact-panel-header">
            <div>
              <strong>{layer.name}</strong>
              <small>{formatLabel(layer.layer_type)}</small>
            </div>
            <span className={`status-label status-${layer.posture}`}>
              {formatLabel(layer.posture)}
            </span>
          </div>
          <p>{layer.risk_summary}</p>
          <h4>{labels.controlsApplied}</h4>
          <StringList items={layer.controls_applied} />
          <h4>{labels.monitoredSignals}</h4>
          <StringList items={layer.monitored_signals} />
        </div>
      ))}
    </div>
  )
}

function ScenarioList({
  scenarios,
  labels,
}: {
  scenarios: InfrastructureSecurityScenario[]
  labels: {
    expectedDecision: string
    riskIndicators: string
    recommendedControls: string
    possibleChain: string
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
          <h4>{labels.possibleChain}</h4>
          <StringList items={scenario.possible_chain.map(formatLabel)} />
          <h4>{labels.riskIndicators}</h4>
          <StringList items={scenario.risk_indicators} />
          <h4>{labels.recommendedControls}</h4>
          <StringList items={scenario.recommended_controls} />
        </div>
      ))}
    </div>
  )
}

export function InfrastructureSecurityPage() {
  const { t } = useLanguage()
  const [controls, setControls] = useState<InfrastructureSecurityControl[]>([])
  const [events, setEvents] = useState<InfrastructureSecurityEvent[]>([])
  const [layers, setLayers] = useState<InfrastructureSecurityLayer[]>([])
  const [scenarios, setScenarios] = useState<InfrastructureSecurityScenario[]>([])
  const [scenarioId, setScenarioId] = useState('app_to_cloud_chain_reaction')
  const [objectAuthorizationFailed, setObjectAuthorizationFailed] = useState(true)
  const [unsafeTemplateInputDetected, setUnsafeTemplateInputDetected] =
    useState(true)
  const [podPrivileged, setPodPrivileged] = useState(false)
  const [serviceAccountCanReadSecrets, setServiceAccountCanReadSecrets] =
    useState(true)
  const [cloudIamWildcardPermissions, setCloudIamWildcardPermissions] =
    useState(true)
  const [weakTrustPolicy, setWeakTrustPolicy] = useState(true)
  const [secretExposureDetected, setSecretExposureDetected] = useState(true)
  const [storagePublicAccessDetected, setStoragePublicAccessDetected] =
    useState(true)
  const [certificateExposureDetected, setCertificateExposureDetected] =
    useState(true)
  const [servicePrincipalOverprivileged, setServicePrincipalOverprivileged] =
    useState(true)
  const [deploymentCredentialsEnabled, setDeploymentCredentialsEnabled] =
    useState(true)
  const [managedIdentityExcessiveScope, setManagedIdentityExcessiveScope] =
    useState(true)
  const [passwordResetPrivilegeDetected, setPasswordResetPrivilegeDetected] =
    useState(true)
  const [identityMonitoringGap, setIdentityMonitoringGap] = useState(true)
  const [dockerfileSecretsDetected, setDockerfileSecretsDetected] =
    useState(true)
  const [imageUsesLatestTag, setImageUsesLatestTag] = useState(true)
  const [containerRunsAsRoot, setContainerRunsAsRoot] = useState(true)
  const [plaintextSecretsInManifest, setPlaintextSecretsInManifest] =
    useState(true)
  const [missingSecurityContext, setMissingSecurityContext] = useState(true)
  const [serviceAccountTokenMounted, setServiceAccountTokenMounted] =
    useState(true)
  const [rbacWildcardPermissions, setRbacWildcardPermissions] = useState(true)
  const [canReadKubernetesSecrets, setCanReadKubernetesSecrets] =
    useState(true)
  const [networkPolicyMissing, setNetworkPolicyMissing] = useState(true)
  const [resourceLimitsMissing, setResourceLimitsMissing] = useState(true)
  const [cisAuditMissing, setCisAuditMissing] = useState(true)
  const [hardeningVerificationMissing, setHardeningVerificationMissing] =
    useState(true)
  const [evaluationResult, setEvaluationResult] =
    useState<EvaluateInfrastructureSecurityScenarioResponse | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isEvaluating, setIsEvaluating] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const criticalChainRisks = events.filter(
    (event) => event.severity === 'critical' && event.decision === 'escalate',
  ).length

  const summaryCards = useMemo(
    () => [
      {
        label: t.infrastructureSecurity.securityLayers,
        value: layers.length.toString(),
        detail: t.infrastructureSecurity.applicationSecurity,
      },
      {
        label: t.infrastructureSecurity.infrastructureControls,
        value: controls.length.toString(),
        detail: t.infrastructureSecurity.kubernetesSecurity,
      },
      {
        label: t.infrastructureSecurity.activeEvents,
        value: events.length.toString(),
        detail: t.infrastructureSecurity.auditEvidence,
      },
      {
        label: t.infrastructureSecurity.criticalChainRisks,
        value: criticalChainRisks.toString(),
        detail: t.infrastructureSecurity.riskOperations,
      },
    ],
    [
      controls.length,
      criticalChainRisks,
      events.length,
      layers.length,
      t.infrastructureSecurity.activeEvents,
      t.infrastructureSecurity.applicationSecurity,
      t.infrastructureSecurity.auditEvidence,
      t.infrastructureSecurity.criticalChainRisks,
      t.infrastructureSecurity.infrastructureControls,
      t.infrastructureSecurity.kubernetesSecurity,
      t.infrastructureSecurity.riskOperations,
      t.infrastructureSecurity.securityLayers,
    ],
  )

  useEffect(() => {
    let isActive = true

    Promise.all([
      getInfrastructureSecurityControls(),
      getInfrastructureSecurityEvents(),
      getInfrastructureSecurityLayers(),
      getInfrastructureSecurityScenarios(),
    ])
      .then(([nextControls, nextEvents, nextLayers, nextScenarios]) => {
        if (!isActive) {
          return
        }

        setControls(nextControls)
        setEvents(nextEvents)
        setLayers(nextLayers)
        setScenarios(nextScenarios)
      })
      .catch(() => {
        if (!isActive) {
          return
        }

        setErrorMessage(
          'Infrastructure security data is unavailable in the local prototype.',
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
      const response = await evaluateInfrastructureSecurityScenario({
        scenario_id: scenarioId,
        object_authorization_failed: objectAuthorizationFailed,
        unsafe_template_input_detected: unsafeTemplateInputDetected,
        pod_privileged: podPrivileged,
        service_account_can_read_secrets: serviceAccountCanReadSecrets,
        cloud_iam_wildcard_permissions: cloudIamWildcardPermissions,
        weak_trust_policy: weakTrustPolicy,
        secret_exposure_detected: secretExposureDetected,
        storage_public_access_detected: storagePublicAccessDetected,
        certificate_exposure_detected: certificateExposureDetected,
        service_principal_overprivileged: servicePrincipalOverprivileged,
        deployment_credentials_enabled: deploymentCredentialsEnabled,
        managed_identity_excessive_scope: managedIdentityExcessiveScope,
        password_reset_privilege_detected: passwordResetPrivilegeDetected,
        identity_monitoring_gap: identityMonitoringGap,
        dockerfile_secrets_detected: dockerfileSecretsDetected,
        image_uses_latest_tag: imageUsesLatestTag,
        container_runs_as_root: containerRunsAsRoot,
        plaintext_secrets_in_manifest: plaintextSecretsInManifest,
        missing_security_context: missingSecurityContext,
        service_account_token_mounted: serviceAccountTokenMounted,
        rbac_wildcard_permissions: rbacWildcardPermissions,
        can_read_kubernetes_secrets: canReadKubernetesSecrets,
        network_policy_missing: networkPolicyMissing,
        resource_limits_missing: resourceLimitsMissing,
        cis_audit_missing: cisAuditMissing,
        hardening_verification_missing: hardeningVerificationMissing,
      })
      setEvaluationResult(response)
    } catch {
      setErrorMessage(
        'The infrastructure security scenario could not be evaluated.',
      )
    } finally {
      setIsEvaluating(false)
    }
  }

  const decisionClass = (decision: InfrastructureSecurityDecision) =>
    `decision-label decision-label-${decision}`

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.infrastructureSecurity.title}</h1>
            <p>{t.infrastructureSecurity.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankStaffWorkspace.statuses.crossLayerSecurity}
          </div>
        </section>

        {errorMessage && <p className="panel-note">{errorMessage}</p>}

        <Panel className="risk-operations-command">
          <div className="panel-header">
            <div>
              <p className="eyebrow">{t.infrastructureSecurity.cloudNativeBoundary}</p>
              <h2>{t.infrastructureSecurity.commandBannerTitle}</h2>
            </div>
            <Link
              className="button-link secondary-button compact-link"
              to="/bank-staff/risk-operations"
            >
              {t.riskOperations.title}
            </Link>
          </div>
          <p>{t.infrastructureSecurity.commandBannerText}</p>
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
                  <p className="eyebrow">{t.infrastructureSecurity.eventQueue}</p>
                  <h2>{t.infrastructureSecurity.crossLayerSecurityEvents}</h2>
                </div>
              </div>

              <div className="financial-crime-alert-list">
                {events.map((event) => (
                  <EventCard
                    event={event}
                    labels={{
                      affectedLayer: t.infrastructureSecurity.affectedLayer,
                      chainStage: t.infrastructureSecurity.chainStage,
                      riskType: t.evidencePackages.riskType,
                      affectedAsset: t.infrastructureSecurity.affectedAsset,
                      summary: t.evidencePackages.summary,
                      chainReactionRisk:
                        t.infrastructureSecurity.chainReactionRisk,
                      triggeredControls: t.evidencePackages.triggeredControls,
                      recommendedAction:
                        t.operationalResilience.recommendedAction,
                      evidencePackageReady:
                        t.infrastructureSecurity.evidencePackageReady,
                      auditEventId: t.common.auditEventId,
                      correlationId: t.common.correlationId,
                      yes: t.common.yes,
                      no: t.common.no,
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
                  <h2>{t.infrastructureSecurity.infrastructureControls}</h2>
                </div>
              </div>
              <div className="financial-crime-alert-list">
                {controls.map((control) => (
                  <ControlCard
                    control={control}
                    labels={{
                      layer: t.infrastructureSecurity.affectedLayer,
                      category: t.apiSecurity.category,
                      enabled: t.apiSecurity.enabled,
                      disabled: t.apiSecurity.disabled,
                      protectedAssets: t.infrastructureSecurity.protectedAssets,
                      decisionModel: t.apiSecurity.decisionModel,
                      evidenceOutputs: t.apiSecurity.evidenceOutputs,
                    }}
                    key={control.control_id}
                  />
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.infrastructureSecurity.securityLayers}</p>
              <h2>{t.infrastructureSecurity.securityLayers}</h2>
              <LayerList
                layers={layers}
                labels={{
                  controlsApplied: t.apiSecurity.controlsApplied,
                  monitoredSignals: t.infrastructureSecurity.monitoredSignals,
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
                  possibleChain: t.infrastructureSecurity.possibleChain,
                }}
              />
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.apiSecurity.scenarioDemo}</p>
              <h2>{t.infrastructureSecurity.evaluateInfrastructureScenario}</h2>

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

                <label className="compliance-checkbox">
                  <input
                    checked={objectAuthorizationFailed}
                    type="checkbox"
                    onChange={(event) =>
                      setObjectAuthorizationFailed(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.objectAuthorizationFailed}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={unsafeTemplateInputDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setUnsafeTemplateInputDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.unsafeTemplateInputDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={podPrivileged}
                    type="checkbox"
                    onChange={(event) => setPodPrivileged(event.target.checked)}
                  />
                  <span>{t.infrastructureSecurity.podPrivileged}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={serviceAccountCanReadSecrets}
                    type="checkbox"
                    onChange={(event) =>
                      setServiceAccountCanReadSecrets(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.serviceAccountCanReadSecrets}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={cloudIamWildcardPermissions}
                    type="checkbox"
                    onChange={(event) =>
                      setCloudIamWildcardPermissions(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.cloudIamWildcardPermissions}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={weakTrustPolicy}
                    type="checkbox"
                    onChange={(event) => setWeakTrustPolicy(event.target.checked)}
                  />
                  <span>{t.infrastructureSecurity.weakTrustPolicy}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={secretExposureDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setSecretExposureDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.secretExposureDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={storagePublicAccessDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setStoragePublicAccessDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.publicStorageExposureDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={certificateExposureDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setCertificateExposureDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.certificateExposureDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={servicePrincipalOverprivileged}
                    type="checkbox"
                    onChange={(event) =>
                      setServicePrincipalOverprivileged(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.servicePrincipalOverprivileged}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={deploymentCredentialsEnabled}
                    type="checkbox"
                    onChange={(event) =>
                      setDeploymentCredentialsEnabled(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.deploymentCredentialsEnabled}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={managedIdentityExcessiveScope}
                    type="checkbox"
                    onChange={(event) =>
                      setManagedIdentityExcessiveScope(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.managedIdentityExcessiveScope}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={passwordResetPrivilegeDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setPasswordResetPrivilegeDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.passwordResetPrivilegeDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={identityMonitoringGap}
                    type="checkbox"
                    onChange={(event) =>
                      setIdentityMonitoringGap(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.identityMonitoringGap}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={dockerfileSecretsDetected}
                    type="checkbox"
                    onChange={(event) =>
                      setDockerfileSecretsDetected(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.dockerfileSecretsDetected}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={imageUsesLatestTag}
                    type="checkbox"
                    onChange={(event) =>
                      setImageUsesLatestTag(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.imageUsesLatestTag}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={containerRunsAsRoot}
                    type="checkbox"
                    onChange={(event) =>
                      setContainerRunsAsRoot(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.containerRunsAsRoot}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={plaintextSecretsInManifest}
                    type="checkbox"
                    onChange={(event) =>
                      setPlaintextSecretsInManifest(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.plaintextSecretsInManifest}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={missingSecurityContext}
                    type="checkbox"
                    onChange={(event) =>
                      setMissingSecurityContext(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.missingSecurityContext}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={serviceAccountTokenMounted}
                    type="checkbox"
                    onChange={(event) =>
                      setServiceAccountTokenMounted(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.serviceAccountTokenMounted}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={rbacWildcardPermissions}
                    type="checkbox"
                    onChange={(event) =>
                      setRbacWildcardPermissions(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.rbacWildcardPermissions}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={canReadKubernetesSecrets}
                    type="checkbox"
                    onChange={(event) =>
                      setCanReadKubernetesSecrets(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.canReadKubernetesSecrets}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={networkPolicyMissing}
                    type="checkbox"
                    onChange={(event) =>
                      setNetworkPolicyMissing(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.networkPolicyMissing}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={resourceLimitsMissing}
                    type="checkbox"
                    onChange={(event) =>
                      setResourceLimitsMissing(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.resourceLimitsMissing}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={cisAuditMissing}
                    type="checkbox"
                    onChange={(event) => setCisAuditMissing(event.target.checked)}
                  />
                  <span>{t.infrastructureSecurity.cisAuditMissing}</span>
                </label>

                <label className="compliance-checkbox">
                  <input
                    checked={hardeningVerificationMissing}
                    type="checkbox"
                    onChange={(event) =>
                      setHardeningVerificationMissing(event.target.checked)
                    }
                  />
                  <span>{t.infrastructureSecurity.hardeningVerificationMissing}</span>
                </label>
              </div>

              <div className="action-row">
                <button
                  onClick={() => void handleEvaluateScenario()}
                  disabled={isEvaluating}
                >
                  {t.infrastructureSecurity.evaluateInfrastructureScenario}
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
                    <span>{t.infrastructureSecurity.affectedLayers}</span>
                    <StringList items={evaluationResult.affected_layers.map(formatLabel)} />
                  </div>
                  <div>
                    <span>{t.infrastructureSecurity.chainReactionRisk}</span>
                    <strong>{evaluationResult.chain_reaction_risk}</strong>
                  </div>
                  <div>
                    <span>{t.evidencePackages.triggeredControls}</span>
                    <StringList items={evaluationResult.triggered_controls} />
                  </div>
                  <div>
                    <span>{t.common.auditEventCreated}</span>
                    <strong>
                      {evaluationResult.audit_event_created ? t.common.yes : t.common.no}
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
                    <span>{t.infrastructureSecurity.evidencePackageReady}</span>
                    <strong>
                      {evaluationResult.evidence_package_ready
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
                {t.infrastructureSecurity.goldenRuleItems.map((rule) => (
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
          {t.infrastructureSecurity.prototypeDisclaimer}
        </p>
      </main>
    </div>
  )
}
