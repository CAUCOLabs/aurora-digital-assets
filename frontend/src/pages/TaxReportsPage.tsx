import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function TaxReportsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Tax and exports"
      title="Tax reports"
      subtitle="Simulated tax reporting concepts for banking, digital assets, and investment records."
      badge="No tax advice"
      primaryEyebrow="Tax documents"
      primaryTitle="Report placeholders"
      primaryTag="No real tax document"
      rows={[
        {
          title: 'Annual tax summary',
          detail: 'Yearly tax summary placeholder for the local prototype.',
          status: 'Draft',
          meta: 'Tax year: 2026',
        },
        {
          title: 'Digital asset tax report concept',
          detail: 'Concept report for digital asset activity and reporting traceability.',
          status: 'Concept',
          meta: 'No official filing data',
        },
        {
          title: 'Investment tax report concept',
          detail: 'Traditional investment reporting placeholder kept separate from digital assets.',
          status: 'Concept',
          meta: 'No investment advice',
        },
        {
          title: 'Downloadable report placeholders',
          detail: 'Static labels for PDF, CSV, and JSON report formats.',
          status: 'Not generated',
          meta: 'No file is created',
        },
      ]}
      secondaryEyebrow="Tax boundary"
      secondaryTitle="Tax safeguards"
      summaryItems={[
        { label: 'Tax advice', value: 'None' },
        { label: 'Tax filing', value: 'Not submitted' },
        { label: 'Customer data', value: 'No real customer data' },
      ]}
      actionTitle="Download tax report"
      actionNote="The action is disabled because no real tax report, tax filing, or tax advice is generated."
      actionLabel="Download report"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real tax document, tax filing, tax advice, customer data, banking operation, export, or legal certification is created or executed."
      relatedLinks={[
        { label: 'Reports overview', to: '/reports' },
        { label: 'Export documents', to: '/reports/export-documents' },
      ]}
    />
  )
}
