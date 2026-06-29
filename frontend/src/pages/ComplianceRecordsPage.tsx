import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function ComplianceRecordsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Audit and evidence"
      title="Compliance records"
      subtitle="Simulated compliance record area for review cases, financial crime monitoring, sensitive approvals, and custodian readiness."
      badge="No regulatory certification"
      primaryEyebrow="Compliance cases"
      primaryTitle="Compliance record concepts"
      primaryTag="No legal certification"
      rows={[
        {
          title: 'Compliance case',
          detail: 'Compliance review case placeholder for document traceability.',
          status: 'Under review',
          meta: 'Case ID: COMP-DEMO-001',
        },
        {
          title: 'Risk operations case',
          detail: 'Risk operations record linked to simulated monitoring signals.',
          status: 'Created',
          meta: 'Case ID: RISK-DEMO-001',
        },
        {
          title: 'Financial crime monitoring case',
          detail: 'Financial crime monitoring concept for alert review workflows.',
          status: 'Escalated',
          meta: 'Case ID: FC-DEMO-001',
        },
        {
          title: 'Sensitive approval case',
          detail: 'Sensitive approval record for controlled operation review.',
          status: 'Blocked',
          meta: 'Case ID: SAP-DEMO-001',
        },
        {
          title: 'Custodian readiness case',
          detail: 'Custodian readiness and operational review placeholder.',
          status: 'Draft',
          meta: 'Case ID: CUST-DEMO-001',
        },
      ]}
      secondaryEyebrow="Compliance boundary"
      secondaryTitle="Record safeguards"
      summaryItems={[
        { label: 'Certification', value: 'No regulatory certification' },
        { label: 'Legal report', value: 'Not generated' },
        { label: 'Customer data', value: 'No real customer data' },
      ]}
      actionTitle="Open compliance case"
      actionNote="No legal report, regulatory filing, certification, or customer record is opened or generated."
      actionLabel="Open case"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real compliance record, legal report, regulatory certification, customer data, banking operation, evidence export, or secure message is created or executed."
      relatedLinks={[
        { label: 'Compliance review', to: '/compliance-review' },
        { label: 'Audit trail', to: '/reports/audit-trail' },
      ]}
    />
  )
}
