import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function EvidenceRecordsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Audit and evidence"
      title="Evidence records"
      subtitle="Simulated Aurora evidence record list for audit events, correlation IDs, and review case references."
      badge="No evidence exported"
      primaryEyebrow="Evidence packages"
      primaryTitle="Evidence record concepts"
      primaryTag="Static demo evidence"
      rows={[
        {
          title: 'Evidence package list',
          detail: 'Evidence package placeholder for internal review and audit readiness.',
          status: 'Created',
          meta: 'Package ID: EPK-DEMO-001',
        },
        {
          title: 'Source audit event',
          detail: 'Audit source reference attached to a simulated evidence package.',
          status: 'Recorded',
          meta: 'Audit event ID: AUD-DEMO-001',
        },
        {
          title: 'Correlation ID placeholder',
          detail: 'Correlation identifier used to connect deterministic demo records.',
          status: 'Available',
          meta: 'Correlation ID: CORR-DEMO-001',
        },
        {
          title: 'Review case link placeholder',
          detail: 'Review case reference for compliance review navigation.',
          status: 'Under review',
          meta: 'Case ID: CASE-DEMO-001',
        },
        {
          title: 'Closed evidence record',
          detail: 'Closed evidence record concept for completed internal review.',
          status: 'Closed',
          meta: 'Status: closed',
        },
      ]}
      secondaryEyebrow="Evidence status"
      secondaryTitle="Record states"
      summaryItems={[
        { label: 'Created', value: 'Simulated' },
        { label: 'Under review', value: 'Simulated' },
        { label: 'Closed', value: 'Simulated' },
      ]}
      actionTitle="Open evidence record"
      actionNote="No evidence package, archive, document, or export is generated from this page."
      actionLabel="Open record"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real evidence package, export, audit file, customer data, banking operation, or legal certification is created or executed."
      relatedLinks={[
        { label: 'Evidence packages', to: '/bank-staff/evidence-packages' },
        { label: 'Compliance records', to: '/reports/compliance-records' },
      ]}
    />
  )
}
