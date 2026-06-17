import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import { useLanguage } from '../context/LanguageContext'

const workspaceModules = [
  {
    title: 'Customer onboarding',
    description:
      'Review the bank-managed customer onboarding model before digital asset services become available.',
    status: 'Bank staff control',
    to: '/bank-staff/onboarding',
  },
  {
    title: 'Customer access authorization',
    description:
      'Look up a demo customer and request temporary customer-authorized staff access.',
    status: 'Customer authorization',
    to: '/bank-staff/customer-access',
  },
  {
    title: 'Risk operations console',
    description:
      'Unified command view for alerts, incidents, evidence readiness, escalations, paused operations, and staff priorities.',
    status: 'Orchestration layer',
    to: '/bank-staff/risk-operations',
  },
  {
    title: 'API security control center',
    description:
      'Monitor sensitive backend actions, resolver authorization, business rate limits, schema exposure, step-up authentication, and audit logging.',
    status: 'Backend security layer',
    to: '/bank-staff/api-security',
  },
  {
    title: 'Infrastructure security control center',
    description:
      'Monitor application-to-cloud chain reaction risks across backend authorization, Kubernetes RBAC, IAM, secrets, audit evidence, and risk operations.',
    status: 'Cross-layer security',
    to: '/bank-staff/infrastructure-security',
  },
  {
    title: 'Cryptographic agility control center',
    description:
      'Track cryptographic inventory, algorithm versioning, key rotation, long-term confidentiality risk, and post-quantum migration readiness.',
    status: 'Crypto-agility',
    to: '/bank-staff/crypto-agility',
  },
  {
    title: 'Sensitive operations approval engine',
    description:
      'Model bank-style step-up approval, simulated mobile approval status, backend risk decisioning, audit evidence, and review routing.',
    status: 'Step-up approval',
    to: '/bank-staff/sensitive-approval',
  },
  {
    title: 'Compliance review',
    description:
      'Review simulated transaction monitoring outcomes, wallet risk checks, and escalation evidence.',
    status: 'Compliance review',
    to: '/compliance-review',
  },
  {
    title: 'Financial crime monitoring',
    description:
      'Review insider risk, shell company indicators, structured deposits, crypto off-ramp risk, foreign transfer risk, and network-linked suspicious activity.',
    status: 'Monitoring alerts',
    to: '/bank-staff/financial-crime-monitoring',
  },
  {
    title: 'Compliance intelligence',
    description:
      'Explain financial crime alerts, review triggered controls, identify missing evidence, and prepare reviewer guidance before escalation.',
    status: 'Reasoning layer',
    to: '/bank-staff/compliance-intelligence',
  },
  {
    title: 'Evidence packages',
    description:
      'Prepare structured evidence packages for compliance review, audit, investigation, and regulator-facing documentation.',
    status: 'Package readiness',
    to: '/bank-staff/evidence-packages',
  },
  {
    title: 'Operational resilience',
    description:
      'Monitor service degradation, dependency failures, fallback modes, customer impact, and continuity controls.',
    status: 'Resilience command',
    to: '/bank-staff/operational-resilience',
  },
  {
    title: 'Reports and audit trail',
    description:
      'Open customer-facing reports, tax report concepts, and prototype audit evidence.',
    status: 'Audit evidence',
    to: '/reports',
  },
  {
    title: 'Demo administration',
    description:
      'Inspect and reset local prototype data used by the Aurora Digital Assets demo environment.',
    status: 'Prototype only',
    to: '/admin-demo',
  },
]

const workspaceControls = [
  'Staff actions are represented as simulated prototype workflows.',
  'Sensitive customer details remain locked until customer authorization is granted.',
  'Digital asset access depends on eligibility, compliance review, and audit trail controls.',
  'No real banking systems, custody providers, or customer records are connected.',
]

export function BankStaffWorkspacePage() {
  const { t } = useLanguage()
  const translatedModules = [
    t.bankStaffWorkspace.modules.onboarding,
    t.bankStaffWorkspace.modules.customerAccess,
    t.bankStaffWorkspace.modules.riskOperations,
    t.bankStaffWorkspace.modules.apiSecurity,
    t.bankStaffWorkspace.modules.infrastructureSecurity,
    t.bankStaffWorkspace.modules.cryptoAgility,
    t.bankStaffWorkspace.modules.sensitiveApproval,
    t.bankStaffWorkspace.modules.complianceReview,
    t.bankStaffWorkspace.modules.financialCrime,
    t.bankStaffWorkspace.modules.complianceIntelligence,
    t.bankStaffWorkspace.modules.evidencePackages,
    t.bankStaffWorkspace.modules.operationalResilience,
    t.bankStaffWorkspace.modules.reportsAuditTrail,
    t.bankStaffWorkspace.modules.demoAdministration,
  ]
  const translatedStatuses = [
    t.bankStaffWorkspace.statuses.bankStaffControl,
    t.bankStaffWorkspace.statuses.customerAuthorization,
    t.bankStaffWorkspace.statuses.orchestrationLayer,
    t.bankStaffWorkspace.statuses.backendSecurityLayer,
    t.bankStaffWorkspace.statuses.crossLayerSecurity,
    t.bankStaffWorkspace.statuses.cryptoAgility,
    t.bankStaffWorkspace.statuses.stepUpApproval,
    t.bankStaffWorkspace.statuses.complianceReview,
    t.bankStaffWorkspace.statuses.monitoringAlerts,
    t.bankStaffWorkspace.statuses.reasoningLayer,
    t.bankStaffWorkspace.statuses.packageReadiness,
    t.bankStaffWorkspace.statuses.resilienceCommand,
    t.bankStaffWorkspace.statuses.auditEvidence,
    t.bankStaffWorkspace.statuses.prototypeOnly,
  ]
  const translatedDescriptions = [
    t.bankStaffWorkspace.moduleDescriptions.onboarding,
    t.bankStaffWorkspace.moduleDescriptions.customerAccess,
    t.bankStaffWorkspace.moduleDescriptions.riskOperations,
    t.bankStaffWorkspace.moduleDescriptions.apiSecurity,
    t.bankStaffWorkspace.moduleDescriptions.infrastructureSecurity,
    t.bankStaffWorkspace.moduleDescriptions.cryptoAgility,
    t.bankStaffWorkspace.moduleDescriptions.sensitiveApproval,
    t.bankStaffWorkspace.moduleDescriptions.complianceReview,
    t.bankStaffWorkspace.moduleDescriptions.financialCrime,
    t.bankStaffWorkspace.moduleDescriptions.complianceIntelligence,
    t.bankStaffWorkspace.moduleDescriptions.evidencePackages,
    t.bankStaffWorkspace.moduleDescriptions.operationalResilience,
    t.bankStaffWorkspace.moduleDescriptions.reportsAuditTrail,
    t.bankStaffWorkspace.moduleDescriptions.demoAdministration,
  ]

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.bankStaffWorkspace.protectedArea}</p>
            <h1>{t.bankStaffWorkspace.title}</h1>
            <p>{t.bankStaffWorkspace.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankStaffWorkspace.authenticatedSession}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.bankStaffWorkspace.workspaceModules}</p>
                  <h2>{t.bankStaffWorkspace.staffTools}</h2>
                </div>
                <span className="module-tag">
                  {t.bankStaffWorkspace.conceptPrototype}
                </span>
              </div>

              <div className="account-list">
                {workspaceModules.map((module, index) => (
                  <Link
                    className="account-row"
                    key={module.to}
                    to={module.to}
                  >
                    <div>
                      <h3>{translatedModules[index]}</h3>
                      <p>{translatedDescriptions[index] ?? module.description}</p>
                      <span>{module.to}</span>
                    </div>
                    <strong>{translatedStatuses[index]}</strong>
                  </Link>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">{t.bankStaffWorkspace.staffBoundary}</p>
              <h2>{t.bankStaffWorkspace.prototypeControls}</h2>
              <p>
                This workspace demonstrates banking-first control points for a
                regulated digital assets concept. It is not connected to real
                staff identities, customer records, custody systems, or banking
                infrastructure.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">{t.bankStaffWorkspace.operatingGuardrails}</p>
              <h2>{t.bankStaffWorkspace.accessModel}</h2>
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
              <p className="eyebrow">Quick links</p>
              <h2>{t.bankStaffWorkspace.commonActions}</h2>
              <div className="action-row vertical-actions">
                <Link className="button-link" to="/bank-staff/onboarding">
                  Open onboarding model
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/bank-staff/customer-access"
                >
                  Request customer access
                </Link>
              </div>
            </Panel>
          </aside>
        </section>

        <p className="disclaimer">
          Aurora Digital Assets is a concept prototype. No real financial
          transactions, digital asset custody, staff access, or customer data are
          processed.
        </p>
      </main>
    </div>
  )
}
