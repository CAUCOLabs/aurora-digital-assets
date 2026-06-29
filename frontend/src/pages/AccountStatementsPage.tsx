import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function AccountStatementsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Statements"
      title="Account statements"
      subtitle="Simulated account statement records for the Aurora Bank online banking prototype."
      badge="No real bank statements"
      primaryEyebrow="Account documents"
      primaryTitle="Available statement concepts"
      primaryTag="Local deterministic prototype"
      rows={[
        {
          title: 'Current account statement',
          detail: 'Monthly statement concept for the everyday current account.',
          status: 'Available',
          meta: 'Statement period: April 2026',
        },
        {
          title: 'Savings account statement',
          detail: 'Savings and deposit account statement placeholder.',
          status: 'Available',
          meta: 'Statement period: April 2026',
        },
        {
          title: 'Monthly statement',
          detail: 'Consolidated monthly account document concept.',
          status: 'Created',
          meta: 'Document status: simulated',
        },
        {
          title: 'Annual summary',
          detail: 'Year-end banking summary placeholder for customer review.',
          status: 'Draft',
          meta: 'Document status: not generated',
        },
      ]}
      secondaryEyebrow="Document status"
      secondaryTitle="Statement controls"
      summaryItems={[
        { label: 'Source', value: 'Mock banking records' },
        { label: 'Customer data', value: 'No real customer data' },
        { label: 'Delivery', value: 'Not sent' },
      ]}
      actionTitle="View statement"
      actionNote="The button is disabled because no real bank statement is opened or generated in this prototype."
      actionLabel="View document"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real bank statements, account records, customer data, banking operation, export, or customer communication is created or executed."
      relatedLinks={[
        { label: 'Bank mail', to: '/reports/bank-mail' },
        { label: 'Export documents', to: '/reports/export-documents' },
      ]}
    />
  )
}
