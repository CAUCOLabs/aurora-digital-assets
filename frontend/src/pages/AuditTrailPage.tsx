import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function AuditTrailPage() {
  return (
    <ReportDemoPanel
      eyebrow="Audit and evidence"
      title="Audit trail"
      subtitle="Deterministic audit rows for risk decisions, review events, approvals, governance, and evidence traceability."
      badge="Deterministic audit rows"
      primaryEyebrow="Audit events"
      primaryTitle="Simulated audit trail"
      primaryTag="No live execution"
      rows={[
        {
          title: 'Risk decision recorded',
          detail: 'Risk operation decision row for a simulated digital asset workflow.',
          status: 'Recorded',
          meta: 'Correlation ID: CORR-AUDIT-001',
        },
        {
          title: 'Evidence package created',
          detail: 'Evidence package creation event for an internal review concept.',
          status: 'Created',
          meta: 'Package ID: EPK-DEMO-001',
        },
        {
          title: 'Review case opened',
          detail: 'Compliance review case placeholder opened from a simulated alert.',
          status: 'Under review',
          meta: 'Case ID: CASE-DEMO-001',
        },
        {
          title: 'Sensitive approval blocked',
          detail: 'Sensitive approval control blocked a simulated high-risk action.',
          status: 'Blocked',
          meta: 'Guardrail: sensitive approval',
        },
        {
          title: 'Human approval integrity guard event',
          detail: 'Integrity guard event showing reviewer control checks.',
          status: 'Recorded',
          meta: 'Control: human approval integrity',
        },
        {
          title: 'Agent governance event',
          detail: 'Agent identity and permission event for governance traceability.',
          status: 'Recorded',
          meta: 'Control: agent governance',
        },
      ]}
      secondaryEyebrow="Traceability"
      secondaryTitle="Audit safeguards"
      summaryItems={[
        { label: 'Execution', value: 'No live execution' },
        { label: 'Audit data', value: 'Static demo evidence' },
        { label: 'Customer data', value: 'No real customer data' },
      ]}
      actionTitle="Open audit entry"
      actionNote="Audit rows are deterministic demo records. No real operation, approval, or system event is executed."
      actionLabel="Open entry"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real audit trail, customer record, approval, agent execution, banking operation, evidence package, export, or legal certification is created or executed."
      relatedLinks={[
        { label: 'Evidence records', to: '/reports/evidence-records' },
        { label: 'Compliance records', to: '/reports/compliance-records' },
      ]}
    />
  )
}
