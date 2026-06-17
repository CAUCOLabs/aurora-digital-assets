import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'
import {
  evaluateCryptoScenario,
  getCryptoAssets,
  getCryptoKeyLifecycle,
  getCryptoPolicies,
  getCryptoScenarios,
  type CryptoAgilityScenario,
  type CryptoAlgorithmPolicy,
  type CryptoAsset,
  type CryptoKeyLifecycleItem,
  type EvaluateCryptoAgilityScenarioRequest,
  type EvaluateCryptoAgilityScenarioResponse,
} from '../services/cryptoAgilityApi'

const defaultScenarioPayload: EvaluateCryptoAgilityScenarioRequest = {
  scenario_id: 'crypto_agility_post_quantum_readiness_gap',
  deprecated_algorithm_detected: true,
  long_lived_key_detected: true,
  missing_algorithm_versioning: true,
  missing_key_rotation_policy: true,
  backup_long_term_risk: true,
  audit_integrity_gap: true,
  custody_key_rotation_gap: true,
  blockchain_protocol_confusion: true,
  post_quantum_readiness_gap: true,
  kms_hsm_integration_missing: true,
}

const controlKeys = [
  'deprecated_algorithm_detected',
  'long_lived_key_detected',
  'missing_algorithm_versioning',
  'missing_key_rotation_policy',
  'backup_long_term_risk',
  'audit_integrity_gap',
  'custody_key_rotation_gap',
  'blockchain_protocol_confusion',
  'post_quantum_readiness_gap',
  'kms_hsm_integration_missing',
] as const

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

export function CryptoAgilityPage() {
  const { t } = useLanguage()
  const labels = t.cryptoAgility
  const [assets, setAssets] = useState<CryptoAsset[]>([])
  const [policies, setPolicies] = useState<CryptoAlgorithmPolicy[]>([])
  const [keyLifecycle, setKeyLifecycle] = useState<CryptoKeyLifecycleItem[]>([])
  const [scenarios, setScenarios] = useState<CryptoAgilityScenario[]>([])
  const [payload, setPayload] =
    useState<EvaluateCryptoAgilityScenarioRequest>(defaultScenarioPayload)
  const [result, setResult] =
    useState<EvaluateCryptoAgilityScenarioResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [evaluating, setEvaluating] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true

    async function loadData() {
      try {
        const [assetData, policyData, lifecycleData, scenarioData] =
          await Promise.all([
            getCryptoAssets(),
            getCryptoPolicies(),
            getCryptoKeyLifecycle(),
            getCryptoScenarios(),
          ])
        if (!mounted) {
          return
        }
        setAssets(assetData)
        setPolicies(policyData)
        setKeyLifecycle(lifecycleData)
        setScenarios(scenarioData)
      } catch (loadError) {
        if (mounted) {
          setError(
            loadError instanceof Error ? loadError.message : String(loadError),
          )
        }
      } finally {
        if (mounted) {
          setLoading(false)
        }
      }
    }

    loadData()

    return () => {
      mounted = false
    }
  }, [])

  const metrics = useMemo(
    () => [
      {
        label: labels.cryptoAssets,
        value: assets.length,
      },
      {
        label: labels.algorithmPolicies,
        value: policies.length,
      },
      {
        label: labels.rotationGaps,
        value: keyLifecycle.filter((item) => item.rotation_required).length,
      },
      {
        label: labels.longTermRiskAssets,
        value: assets.filter((asset) => asset.long_term_confidentiality_required)
          .length,
      },
      {
        label: labels.pqReadinessGaps,
        value: assets.filter((asset) =>
          ['gap_detected', 'not_assessed'].includes(asset.migration_readiness),
        ).length,
      },
    ],
    [assets, keyLifecycle, labels, policies],
  )

  async function handleEvaluate() {
    setEvaluating(true)
    setError(null)
    try {
      const nextResult = await evaluateCryptoScenario(payload)
      setResult(nextResult)
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

  function setFlag(
    key: (typeof controlKeys)[number],
    checked: boolean,
  ) {
    setPayload((current) => ({
      ...current,
      [key]: checked,
    }))
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{labels.postQuantumReadiness}</p>
            <h1>{labels.title}</h1>
            <p>{labels.subtitle}</p>
          </div>
          <Link className="button-link secondary-button" to="/bank-staff">
            {t.common.back}
          </Link>
        </section>

        <Panel className="risk-panel">
          <p className="eyebrow">{labels.bannerTitle}</p>
          <h2>{labels.designedForMigration}</h2>
          <p>{labels.bannerText}</p>
        </Panel>

        {error && (
          <Panel className="risk-panel">
            <p className="eyebrow">{t.common.error}</p>
            <p>{error}</p>
          </Panel>
        )}

        <section className="metric-grid">
          {metrics.map((metric) => (
            <Panel key={metric.label} className="metric-card">
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
                  <p className="eyebrow">{labels.algorithmVersioning}</p>
                  <h2>{labels.assetInventory}</h2>
                </div>
                <span className="module-tag">{labels.cryptoAssets}</span>
              </div>

              <div className="account-list">
                {assets.map((asset) => (
                  <article className="account-row" key={asset.asset_id}>
                    <div>
                      <h3>{asset.name}</h3>
                      <p>{asset.notes}</p>
                      <span>
                        {formatLabel(asset.domain)} · {asset.owner} ·{' '}
                        {asset.current_algorithm}
                      </span>
                    </div>
                    <strong>{formatLabel(asset.migration_readiness)}</strong>
                    <div className="summary-list financial-crime-alert-meta">
                      <div>
                        <span>{labels.algorithmFamily}</span>
                        <strong>{formatLabel(asset.algorithm_family)}</strong>
                      </div>
                      <div>
                        <span>{labels.version}</span>
                        <strong>{asset.algorithm_version}</strong>
                      </div>
                      <div>
                        <span>{labels.keyLocation}</span>
                        <strong>{formatLabel(asset.key_location)}</strong>
                      </div>
                      <div>
                        <span>{labels.rotationPeriod}</span>
                        <strong>{asset.rotation_period_days}</strong>
                      </div>
                      <div>
                        <span>{labels.longTermConfidentiality}</span>
                        <strong>
                          {asset.long_term_confidentiality_required
                            ? t.common.yes
                            : t.common.no}
                        </strong>
                      </div>
                      <div>
                        <span>{labels.harvestRisk}</span>
                        <strong>{formatLabel(asset.harvest_now_decrypt_later_risk)}</strong>
                      </div>
                      <div>
                        <span>{labels.blockchainDependency}</span>
                        <strong>
                          {asset.blockchain_protocol_dependency
                            ? t.common.yes
                            : t.common.no}
                        </strong>
                      </div>
                    </div>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.noCustomCryptography}</p>
                  <h2>{labels.algorithmPolicies}</h2>
                </div>
              </div>
              <div className="financial-crime-side-list">
                {policies.map((policy) => (
                  <div key={policy.policy_id}>
                    <div className="panel-header compact-panel-header">
                      <div>
                        <strong>{policy.policy_id}</strong>
                        <small>{formatLabel(policy.algorithm_family)}</small>
                      </div>
                      <span className={`status-label status-${policy.status}`}>
                        {formatLabel(policy.status)}
                      </span>
                    </div>
                    <p>{policy.reason}</p>
                    <div className="financial-crime-evidence compliance-evidence-grid">
                      <StringList
                        items={[
                          `${labels.approvedCurrent}: ${policy.approved_current.join(', ')}`,
                          `${labels.deprecated}: ${policy.deprecated.join(', ')}`,
                          `${labels.migrationCandidates}: ${policy.migration_candidates.join(', ')}`,
                        ]}
                      />
                      <StringList items={policy.evidence_outputs} />
                    </div>
                    <p>
                      <strong>{labels.cryptoOwner}: </strong>
                      {policy.crypto_owner}
                    </p>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.longTermConfidentialityRisk}</p>
                  <h2>{labels.keyLifecycle}</h2>
                </div>
              </div>
              <div className="financial-crime-side-list">
                {keyLifecycle.map((item) => (
                  <div key={item.key_id}>
                    <div className="panel-header compact-panel-header">
                      <div>
                        <strong>{item.key_id}</strong>
                        <small>{item.asset_id}</small>
                      </div>
                      <span className={`status-label status-${item.status}`}>
                        {formatLabel(item.status)}
                      </span>
                    </div>
                    <p>{item.purpose}</p>
                    <div className="summary-list">
                      <div>
                        <span>{labels.storageBoundary}</span>
                        <strong>{item.storage_boundary}</strong>
                      </div>
                      <div>
                        <span>{labels.rotationRequired}</span>
                        <strong>
                          {item.rotation_required ? t.common.yes : t.common.no}
                        </strong>
                      </div>
                      <div>
                        <span>{labels.emergencyRolloverReady}</span>
                        <strong>
                          {item.emergency_rollover_ready
                            ? t.common.yes
                            : t.common.no}
                        </strong>
                      </div>
                      <div>
                        <span>{labels.auditRequired}</span>
                        <strong>{item.audit_required ? t.common.yes : t.common.no}</strong>
                      </div>
                    </div>
                    <p>{item.reviewer_note}</p>
                  </div>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="crypto-scenario-panel">
              <p className="eyebrow">{labels.scenarioEvaluation}</p>
              <h2>{labels.evaluateCryptoScenario}</h2>
              <label className="form-field crypto-scenario-field">
                <span>{labels.scenario}</span>
                <select
                  value={payload.scenario_id}
                  onChange={(event) =>
                    setPayload((current) => ({
                      ...current,
                      scenario_id: event.target.value,
                    }))
                  }
                >
                  {scenarios.map((scenario) => (
                    <option key={scenario.scenario_id} value={scenario.scenario_id}>
                      {scenario.title}
                    </option>
                  ))}
                </select>
              </label>
              <div className="check-list crypto-scenario-check-list">
                {controlKeys.map((key) => (
                  <label key={key}>
                    <input
                      type="checkbox"
                      checked={payload[key]}
                      onChange={(event) => setFlag(key, event.target.checked)}
                    />
                    {labels.flags[key]}
                  </label>
                ))}
              </div>
              <button
                className="primary-action crypto-scenario-action"
                type="button"
                onClick={handleEvaluate}
                disabled={evaluating}
              >
                {evaluating ? t.common.loading : labels.evaluateCryptoScenario}
              </button>
            </Panel>

            {result && (
              <Panel>
                <p className="eyebrow">{labels.scenarioResult}</p>
                <h2>{labels.postQuantumReadiness}</h2>
                <div className="summary-list">
                  <div>
                    <span>{labels.riskScore}</span>
                    <strong>{result.risk_score}/100</strong>
                  </div>
                  <div>
                    <span>{labels.severity}</span>
                    <strong>{formatLabel(result.severity)}</strong>
                  </div>
                  <div>
                    <span>{labels.decision}</span>
                    <strong>{formatLabel(result.decision)}</strong>
                  </div>
                  <div>
                    <span>{labels.auditEventId}</span>
                    <strong>{result.audit_event_id}</strong>
                  </div>
                  <div>
                    <span>{labels.correlationId}</span>
                    <strong>{result.correlation_id}</strong>
                  </div>
                  <div>
                    <span>{labels.evidencePackageReady}</span>
                    <strong>
                      {result.evidence_package_ready ? t.common.yes : t.common.no}
                    </strong>
                  </div>
                </div>
                <h4>{labels.affectedDomains}</h4>
                <StringList items={result.affected_domains.map(formatLabel)} />
                <h4>{labels.cryptoAgilityRisk}</h4>
                <p>{result.crypto_agility_risk}</p>
                <h4>{labels.triggeredControls}</h4>
                <StringList items={result.triggered_controls} />
                <h4>{labels.recommendedAction}</h4>
                <p>{result.recommended_action}</p>
                <h4>{labels.explanation}</h4>
                <p>{result.explanation}</p>
              </Panel>
            )}

            <Panel>
              <p className="eyebrow">{labels.boundaryTitle}</p>
              <h2>{labels.platformVsBlockchain}</h2>
              <p>{labels.boundaryCopy}</p>
              <div className="financial-crime-evidence compliance-evidence-grid">
                <StringList items={labels.auroraControls} />
                <StringList items={labels.auroraDoesNotControl} />
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.noQuantumProofClaims}</p>
              <h2>{labels.goldenRules}</h2>
              <StringList items={labels.goldenRuleItems} />
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">{labels.prototypeDisclaimer}</p>
      </main>
    </div>
  )
}
