import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function CardStatementsPage() {
  return (
    <ReportDemoPanel
      eyebrow="Statements"
      title="Card statements"
      subtitle="Simulated card statement area for card documents, card transaction summaries, and security notices."
      badge="No real card statements"
      primaryEyebrow="Card documents"
      primaryTitle="Card statement concepts"
      primaryTag="No card transactions"
      rows={[
        {
          title: 'Card monthly statement',
          detail: 'Monthly card statement placeholder for a simulated Aurora Bank card.',
          status: 'Available',
          meta: 'Statement period: April 2026',
        },
        {
          title: 'Card transaction summary',
          detail: 'Summary row for card activity in the local demo only.',
          status: 'Created',
          meta: 'No real card transactions',
        },
        {
          title: 'Currency conversion notice',
          detail: 'Notice concept for card purchases in another currency.',
          status: 'Concept',
          meta: 'No conversion is calculated',
        },
        {
          title: 'Card security notice',
          detail: 'Security information placeholder for safe card usage.',
          status: 'Visible',
          meta: 'No customer communication is sent',
        },
      ]}
      secondaryEyebrow="Card status"
      secondaryTitle="Statement safeguards"
      summaryItems={[
        { label: 'Card data', value: 'No real card data' },
        { label: 'Transactions', value: 'No real card transactions' },
        { label: 'Delivery', value: 'Not sent' },
      ]}
      actionTitle="Open card statement"
      actionNote="No PDF, card account record, card statement, or card transaction file is opened in this prototype."
      actionLabel="Open statement"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real card statements, card transactions, cardholder data, banking operation, export, or customer communication is created or executed."
      relatedLinks={[
        { label: 'Account statements', to: '/reports/account-statements' },
        { label: 'Bank mail', to: '/reports/bank-mail' },
      ]}
    />
  )
}
