import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'

type WorkspaceModuleId =
  | 'onboarding'
  | 'customerAccess'
  | 'riskOperations'
  | 'trustEngine'
  | 'controlEngine'
  | 'policyEngine'
  | 'assessmentEngine'
  | 'knowledgeEngine'
  | 'regulationEngine'
  | 'apiSecurity'
  | 'infrastructureSecurity'
  | 'cryptoAgility'
  | 'assetRailGovernance'
  | 'sensitiveApproval'
  | 'agentGovernance'
  | 'humanApprovalIntegrity'
  | 'complianceReview'
  | 'financialCrime'
  | 'complianceIntelligence'
  | 'evidencePackages'
  | 'operationalResilience'
  | 'reportsAuditTrail'
  | 'demoAdministration'

type WorkspaceGroupId =
  | 'trustInfrastructureCore'
  | 'riskEvidenceCompliance'
  | 'securityResilience'
  | 'humanAgentGovernance'
  | 'bankingOperations'
  | 'demoAdministration'

type WorkspaceModule = {
  id: WorkspaceModuleId
  title: string
  description: string
  status: string
  to: string
}

const workspaceModules: WorkspaceModule[] = [
  {
    id: 'onboarding',
    title: 'Customer onboarding',
    description:
      'Review the bank-managed customer onboarding model before digital asset services become available.',
    status: 'Bank staff control',
    to: '/bank-staff/onboarding',
  },
  {
    id: 'customerAccess',
    title: 'Customer access authorization',
    description:
      'Look up a demo customer and request temporary customer-authorized staff access.',
    status: 'Customer authorization',
    to: '/bank-staff/customer-access',
  },
  {
    id: 'riskOperations',
    title: 'Risk operations console',
    description:
      'Unified command view for alerts, incidents, evidence readiness, escalations, paused operations, and staff priorities.',
    status: 'Orchestration layer',
    to: '/bank-staff/risk-operations',
  },
  {
    id: 'trustEngine',
    title: 'Aurora Trust Engine',
    description:
      'Shared orchestration layer for risk, policy, evidence, assessment, control, regulation and knowledge modules.',
    status: 'Shared orchestration',
    to: '/bank-staff/trust-engine',
  },
  {
    id: 'controlEngine',
    title: 'Control Engine',
    description:
      'Blocks, pauses, routes, evidences or allows internal review for sensitive operations before state can change.',
    status: 'Controlled decision layer',
    to: '/bank-staff/control-engine',
  },
  {
    id: 'policyEngine',
    title: 'Policy Engine',
    description:
      'Converts internal governance policies into deterministic control requirements before sensitive operations can proceed.',
    status: 'Policy layer',
    to: '/bank-staff/policy-engine',
  },
  {
    id: 'assessmentEngine',
    title: 'Assessment Engine',
    description:
      'Evaluates readiness, maturity, control gaps, evidence needs and review paths before controlled decisions.',
    status: 'Readiness assessment',
    to: '/bank-staff/assessment-engine',
  },
  {
    id: 'knowledgeEngine',
    title: 'Knowledge Engine',
    description:
      'Preserves institutional control logic, regulatory concepts, policy mappings, evidence context and explainable review memory.',
    status: 'Explainability layer',
    to: '/bank-staff/knowledge-engine',
  },
  {
    id: 'regulationEngine',
    title: 'Regulation Engine',
    description:
      'Maps asset rails and regulatory concepts into deterministic control requirements, evidence needs and review paths.',
    status: 'Control mapping',
    to: '/bank-staff/regulation-engine',
  },
  {
    id: 'apiSecurity',
    title: 'API security control center',
    description:
      'Monitor sensitive backend actions, resolver authorization, business rate limits, schema exposure, step-up authentication, and audit logging.',
    status: 'Backend security layer',
    to: '/bank-staff/api-security',
  },
  {
    id: 'infrastructureSecurity',
    title: 'Infrastructure security control center',
    description:
      'Monitor application-to-cloud chain reaction risks across backend authorization, Kubernetes RBAC, IAM, secrets, audit evidence, and risk operations.',
    status: 'Cross-layer security',
    to: '/bank-staff/infrastructure-security',
  },
  {
    id: 'cryptoAgility',
    title: 'Cryptographic agility control center',
    description:
      'Track cryptographic inventory, algorithm versioning, key rotation, long-term confidentiality risk, and post-quantum migration readiness.',
    status: 'Crypto-agility',
    to: '/bank-staff/crypto-agility',
  },
  {
    id: 'assetRailGovernance',
    title: 'Asset Rail Governance',
    description:
      'Classify digital euro, tokenized deposits, stablecoins, cryptoassets, and security tokens before applying the correct control path.',
    status: 'Rail classification',
    to: '/bank-staff/asset-rail-governance',
  },
  {
    id: 'sensitiveApproval',
    title: 'Sensitive operations approval engine',
    description:
      'Model bank-style step-up approval, simulated mobile approval status, backend risk decisioning, audit evidence, and review routing.',
    status: 'Step-up approval',
    to: '/bank-staff/sensitive-approval',
  },
  {
    id: 'agentGovernance',
    title: 'Agent governance',
    description:
      'Review simulated agent registry, passport, permissions, action audit, revocation, policy controls, abuse detection, and identity governance.',
    status: 'Agent control',
    to: '/bank-staff/agent-governance',
  },
  {
    id: 'humanApprovalIntegrity',
    title: 'Human approval integrity',
    description:
      'Control human review as a risk event with dual control, segregation of duties, reviewer conflict checks, and post-approval audit evidence.',
    status: 'Approval integrity',
    to: '/bank-staff/human-approval-integrity',
  },
  {
    id: 'complianceReview',
    title: 'Compliance review',
    description:
      'Review simulated transaction monitoring outcomes, wallet risk checks, and escalation evidence.',
    status: 'Compliance review',
    to: '/compliance-review',
  },
  {
    id: 'financialCrime',
    title: 'Financial crime monitoring',
    description:
      'Review insider risk, shell company indicators, structured deposits, crypto off-ramp risk, foreign transfer risk, and network-linked suspicious activity.',
    status: 'Monitoring alerts',
    to: '/bank-staff/financial-crime-monitoring',
  },
  {
    id: 'complianceIntelligence',
    title: 'Compliance intelligence',
    description:
      'Explain financial crime alerts, review triggered controls, identify missing evidence, and prepare reviewer guidance before escalation.',
    status: 'Reasoning layer',
    to: '/bank-staff/compliance-intelligence',
  },
  {
    id: 'evidencePackages',
    title: 'Evidence packages',
    description:
      'Prepare structured evidence packages for compliance review, audit, investigation, and regulator-facing documentation.',
    status: 'Package readiness',
    to: '/bank-staff/evidence-packages',
  },
  {
    id: 'operationalResilience',
    title: 'Operational resilience',
    description:
      'Monitor service degradation, dependency failures, fallback modes, customer impact, and continuity controls.',
    status: 'Resilience command',
    to: '/bank-staff/operational-resilience',
  },
  {
    id: 'reportsAuditTrail',
    title: 'Reports and audit trail',
    description:
      'Open customer-facing reports, tax report concepts, and prototype audit evidence.',
    status: 'Audit evidence',
    to: '/reports',
  },
  {
    id: 'demoAdministration',
    title: 'Demo administration',
    description:
      'Inspect and reset local prototype data used by the Aurora Digital Assets demo environment.',
    status: 'Prototype only',
    to: '/admin-demo',
  },
]

const workspaceGroups: Array<{
  id: WorkspaceGroupId
  moduleIds: WorkspaceModuleId[]
}> = [
  {
    id: 'trustInfrastructureCore',
    moduleIds: [
      'trustEngine',
      'assetRailGovernance',
      'regulationEngine',
      'policyEngine',
      'assessmentEngine',
      'controlEngine',
      'knowledgeEngine',
    ],
  },
  {
    id: 'riskEvidenceCompliance',
    moduleIds: [
      'riskOperations',
      'evidencePackages',
      'complianceIntelligence',
      'complianceReview',
      'financialCrime',
      'reportsAuditTrail',
    ],
  },
  {
    id: 'securityResilience',
    moduleIds: [
      'apiSecurity',
      'infrastructureSecurity',
      'cryptoAgility',
      'operationalResilience',
    ],
  },
  {
    id: 'humanAgentGovernance',
    moduleIds: [
      'humanApprovalIntegrity',
      'agentGovernance',
      'sensitiveApproval',
    ],
  },
  {
    id: 'bankingOperations',
    moduleIds: ['onboarding', 'customerAccess'],
  },
  {
    id: 'demoAdministration',
    moduleIds: ['demoAdministration'],
  },
]

const workspaceControls = [
  'Staff actions are represented as simulated prototype workflows.',
  'Sensitive customer details remain locked until customer authorization is granted.',
  'Digital asset access depends on eligibility, compliance review, and audit trail controls.',
  'No real banking systems, custody providers, or customer records are connected.',
]

const moduleById = new Map(workspaceModules.map((module) => [module.id, module]))

export function BankStaffWorkspacePage() {
  const { t } = useLanguage()
  const labels = t.bankStaffWorkspace

  const translatedModules: Record<WorkspaceModuleId, string> = {
    onboarding: labels.modules.onboarding,
    customerAccess: labels.modules.customerAccess,
    riskOperations: labels.modules.riskOperations,
    trustEngine: labels.modules.trustEngine,
    controlEngine: labels.modules.controlEngine,
    policyEngine: labels.modules.policyEngine,
    assessmentEngine: labels.modules.assessmentEngine,
    knowledgeEngine: labels.modules.knowledgeEngine,
    regulationEngine: labels.modules.regulationEngine,
    apiSecurity: labels.modules.apiSecurity,
    infrastructureSecurity: labels.modules.infrastructureSecurity,
    cryptoAgility: labels.modules.cryptoAgility,
    assetRailGovernance: labels.modules.assetRailGovernance,
    sensitiveApproval: labels.modules.sensitiveApproval,
    agentGovernance: labels.modules.agentGovernance,
    humanApprovalIntegrity: labels.modules.humanApprovalIntegrity,
    complianceReview: labels.modules.complianceReview,
    financialCrime: labels.modules.financialCrime,
    complianceIntelligence: labels.modules.complianceIntelligence,
    evidencePackages: labels.modules.evidencePackages,
    operationalResilience: labels.modules.operationalResilience,
    reportsAuditTrail: labels.modules.reportsAuditTrail,
    demoAdministration: labels.modules.demoAdministration,
  }

  const translatedDescriptions: Record<WorkspaceModuleId, string> = {
    onboarding: labels.moduleDescriptions.onboarding,
    customerAccess: labels.moduleDescriptions.customerAccess,
    riskOperations: labels.moduleDescriptions.riskOperations,
    trustEngine: labels.moduleDescriptions.trustEngine,
    controlEngine: labels.moduleDescriptions.controlEngine,
    policyEngine: labels.moduleDescriptions.policyEngine,
    assessmentEngine: labels.moduleDescriptions.assessmentEngine,
    knowledgeEngine: labels.moduleDescriptions.knowledgeEngine,
    regulationEngine: labels.moduleDescriptions.regulationEngine,
    apiSecurity: labels.moduleDescriptions.apiSecurity,
    infrastructureSecurity: labels.moduleDescriptions.infrastructureSecurity,
    cryptoAgility: labels.moduleDescriptions.cryptoAgility,
    assetRailGovernance: labels.moduleDescriptions.assetRailGovernance,
    sensitiveApproval: labels.moduleDescriptions.sensitiveApproval,
    agentGovernance: labels.moduleDescriptions.agentGovernance,
    humanApprovalIntegrity: labels.moduleDescriptions.humanApprovalIntegrity,
    complianceReview: labels.moduleDescriptions.complianceReview,
    financialCrime: labels.moduleDescriptions.financialCrime,
    complianceIntelligence: labels.moduleDescriptions.complianceIntelligence,
    evidencePackages: labels.moduleDescriptions.evidencePackages,
    operationalResilience: labels.moduleDescriptions.operationalResilience,
    reportsAuditTrail: labels.moduleDescriptions.reportsAuditTrail,
    demoAdministration: labels.moduleDescriptions.demoAdministration,
  }

  const translatedStatuses: Record<WorkspaceModuleId, string> = {
    onboarding: labels.statuses.bankStaffControl,
    customerAccess: labels.statuses.customerAuthorization,
    riskOperations: labels.statuses.orchestrationLayer,
    trustEngine: labels.statuses.sharedOrchestration,
    controlEngine: labels.statuses.controlledDecisionLayer,
    policyEngine: labels.statuses.policyLayer,
    assessmentEngine: labels.statuses.readinessAssessment,
    knowledgeEngine: labels.statuses.explainabilityLayer,
    regulationEngine: labels.statuses.controlMapping,
    apiSecurity: labels.statuses.backendSecurityLayer,
    infrastructureSecurity: labels.statuses.crossLayerSecurity,
    cryptoAgility: labels.statuses.cryptoAgility,
    assetRailGovernance: labels.statuses.railClassification,
    sensitiveApproval: labels.statuses.stepUpApproval,
    agentGovernance: labels.statuses.agentControl,
    humanApprovalIntegrity: labels.statuses.approvalIntegrity,
    complianceReview: labels.statuses.complianceReview,
    financialCrime: labels.statuses.monitoringAlerts,
    complianceIntelligence: labels.statuses.reasoningLayer,
    evidencePackages: labels.statuses.packageReadiness,
    operationalResilience: labels.statuses.resilienceCommand,
    reportsAuditTrail: labels.statuses.auditEvidence,
    demoAdministration: labels.statuses.prototypeOnly,
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{labels.protectedArea}</p>
            <h1>{labels.title}</h1>
            <p>{labels.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {labels.authenticatedSession}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            {workspaceGroups.slice(0, 3).map((group) => (
              <Panel key={group.id}>
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">{labels.workspaceModules}</p>
                    <h2>{labels.groups[group.id].title}</h2>
                  </div>
                  <span className="module-tag">{labels.conceptPrototype}</span>
                </div>
                <p>{labels.groups[group.id].description}</p>

                <div className="account-list">
                  {group.moduleIds.map((moduleId) => {
                    const module = moduleById.get(moduleId)
                    if (!module) {
                      return null
                    }

                    return (
                      <Link className="account-row" key={module.to} to={module.to}>
                        <div>
                          <h3>{translatedModules[module.id]}</h3>
                          <p>{translatedDescriptions[module.id]}</p>
                          <span>{module.to}</span>
                        </div>
                        <strong>{translatedStatuses[module.id]}</strong>
                      </Link>
                    )
                  })}
                </div>
              </Panel>
            ))}
          </div>

          <aside className="right-column">
            {workspaceGroups.slice(3).map((group) => (
              <Panel key={group.id}>
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">{labels.workspaceModules}</p>
                    <h2>{labels.groups[group.id].title}</h2>
                  </div>
                  <span className="module-tag">{labels.conceptPrototype}</span>
                </div>
                <p>{labels.groups[group.id].description}</p>

                <div className="account-list">
                  {group.moduleIds.map((moduleId) => {
                    const module = moduleById.get(moduleId)
                    if (!module) {
                      return null
                    }

                    return (
                      <Link className="account-row" key={module.to} to={module.to}>
                        <div>
                          <h3>{translatedModules[module.id]}</h3>
                          <p>{translatedDescriptions[module.id]}</p>
                          <span>{module.to}</span>
                        </div>
                        <strong>{translatedStatuses[module.id]}</strong>
                      </Link>
                    )
                  })}
                </div>
              </Panel>
            ))}

            <Panel className="risk-panel">
              <p className="eyebrow">{labels.staffBoundary}</p>
              <h2>{labels.prototypeControls}</h2>
              <p>{labels.safetyNote}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.operatingGuardrails}</p>
              <h2>{labels.accessModel}</h2>
              <div className="check-list">
                {workspaceControls.map((control) => (
                  <div key={control}>
                    <span className="status-dot"></span>
                    {control}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.quickLinks}</p>
              <h2>{labels.commonActions}</h2>
              <div className="action-row vertical-actions">
                <Link className="button-link" to="/bank-staff/trust-engine">
                  {labels.openTrustEngine}
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/bank-staff/risk-operations"
                >
                  {labels.openRiskOperations}
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">{labels.safetyNote}</p>
      </main>
    </div>
  )
}
