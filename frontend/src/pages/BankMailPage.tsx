import { ReportDemoPanel } from '../components/ReportDemoPanel'

export function BankMailPage() {
  return (
    <ReportDemoPanel
      eyebrow="Statements"
      title="Bank mail"
      subtitle="Simulated secure message inbox and banking notices for the Aurora Bank prototype."
      badge="No real messages"
      primaryEyebrow="Secure messages"
      primaryTitle="Bank mail inbox"
      primaryTag="No customer communication"
      rows={[
        {
          title: 'Secure message inbox',
          detail: 'Inbox container for local demo notices only.',
          status: 'Visible',
          meta: 'No messages are delivered',
        },
        {
          title: 'Bank notice',
          detail: 'General banking notice placeholder for online banking documents.',
          status: 'Created',
          meta: 'Not sent',
        },
        {
          title: 'Compliance notification',
          detail: 'Compliance notification concept for review and evidence workflows.',
          status: 'Draft',
          meta: 'No customer communication',
        },
        {
          title: 'Statement delivery notice',
          detail: 'Statement delivery notification placeholder.',
          status: 'Concept',
          meta: 'No document delivery',
        },
      ]}
      secondaryEyebrow="Message status"
      secondaryTitle="Communication safeguards"
      summaryItems={[
        { label: 'Messages', value: 'No real messages' },
        { label: 'Delivery', value: 'Not sent' },
        { label: 'Customer data', value: 'No real customer data' },
      ]}
      actionTitle="Open secure message"
      actionNote="No real secure message, notification, email, SMS, or customer communication is opened or sent."
      actionLabel="Open message"
      safetyTitle="Safety note"
      safetyNotice="Local deterministic prototype only. No real secure message, bank mail, customer communication, customer data, document delivery, export, or banking operation is created or executed."
      relatedLinks={[
        { label: 'Account statements', to: '/reports/account-statements' },
        { label: 'Card statements', to: '/reports/card-statements' },
      ]}
    />
  )
}
