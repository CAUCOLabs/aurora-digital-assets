import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function ExportDocumentsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Tax and exports"
      title="Export documents"
      subtitle="Simulated export center for account documents, payment receipts, audit records, and evidence packages."
      badge="No export generated"
      primaryEyebrow="Export options"
      primaryTitle="Document export concepts"
      primaryTag="PDF CSV JSON placeholders"
      rows={[
        {
          title: 'Export account documents',
          detail: 'Account document export placeholder for PDF format.',
          status: 'Not generated',
          meta: 'Format: PDF',
        },
        {
          title: 'Export payment receipts',
          detail: 'Payment receipt bundle placeholder for banking records.',
          status: 'Not generated',
          meta: 'Format: PDF',
        },
        {
          title: 'Export digital asset audit trail',
          detail: 'Digital asset audit trail placeholder for CSV and JSON records.',
          status: 'Concept',
          meta: 'Formats: CSV, JSON',
        },
        {
          title: 'Export compliance evidence package',
          detail: 'Evidence package export concept for controlled review workflows.',
          status: 'Concept',
          meta: 'Formats: PDF, JSON',
        },
      ]}
      secondaryEyebrow="Export status"
      secondaryTitle="Format placeholders"
      summaryItems={[
        { label: 'PDF', value: 'Placeholder only' },
        { label: 'CSV', value: 'Placeholder only' },
        { label: 'JSON', value: 'Placeholder only' },
      ]}
      actionTitle="Export selected records"
      actionNote="No real document, archive, bank statement, evidence package, CSV, JSON, or PDF is generated."
      actionLabel="Export"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real export, bank statement, tax report, evidence package, customer data, banking operation, or secure message is created or executed."
      relatedLinks={[
        { label: 'Audit trail', to: '/reports/audit-trail' },
        { label: 'Evidence records', to: '/reports/evidence-records' },
      ]}
    />
  )
}
