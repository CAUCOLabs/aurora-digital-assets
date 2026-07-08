export type Language = 'en' | 'es'

export const defaultLanguage: Language = 'en'

const enPhrases = {
  'Local deterministic prototype only. No real assets, no real custody, no real bank integration, no real custodian integration, no real blockchain execution, no real cloud deployment, and no private keys or secrets.':
    'Local deterministic prototype only. No real assets, no real custody, no real bank integration, no real custodian integration, no real blockchain execution, no real cloud deployment, and no private keys or secrets.',
  'Human review is not a trust anchor. It is a controlled risk event.':
    'Human review is not a trust anchor. It is a controlled risk event.',
  'Every agent must be identifiable, permission-bound, revocable, and auditable.':
    'Every agent must be identifiable, permission-bound, revocable, and auditable.',
  'Go to online banking dashboard': 'Go to online banking dashboard',
  'Digital Assets navigation': 'Digital Assets navigation',
  'Hidden amount': 'Hidden amount',
  amount: 'amount',
  Home: 'Home',
  Payments: 'Payments',
  Accounts: 'Accounts',
  'Cards and Currency': 'Cards and Currency',
  Loans: 'Loans',
  'Loan overview': 'Loan overview',
  'Apply for a loan': 'Apply for a loan',
  Mortgage: 'Mortgage',
  'Consumer loan': 'Consumer loan',
  'Student loan': 'Student loan',
  'Manage loans': 'Manage loans',
  'Loan calculator': 'Loan calculator',
  'Repayment plan': 'Repayment plan',
  'Loan documents': 'Loan documents',
  'Loan FAQ': 'Loan FAQ',
  Investments: 'Investments',
  Insurance: 'Insurance',
  'Insurance overview': 'Insurance overview',
  'Home insurance': 'Home insurance',
  'Travel insurance': 'Travel insurance',
  'Life insurance': 'Life insurance',
  'Health insurance': 'Health insurance',
  Claims: 'Claims',
  'Claims overview': 'Claims overview',
  'Report a claim': 'Report a claim',
  'Claim documents': 'Claim documents',
  'Documents and support': 'Documents and support',
  'Insurance documents': 'Insurance documents',
  'Insurance FAQ': 'Insurance FAQ',
  'Coverage information': 'Coverage information',
  'Digital Assets': 'Digital Assets',
  Documents: 'Documents',
  'Online Services': 'Online Services',
  'New payment': 'New payment',
  'Approve payments': 'Approve payments',
  'International payment': 'International payment',
  Recipients: 'Recipients',
  'Payment limits': 'Payment limits',
  'Digital asset payments': 'Digital asset payments',
  'Digital asset payment': 'Digital asset payment',
  'Supported business recipients': 'Supported business recipients',
  'Payment asset settings': 'Payment asset settings',
  'Payment reporting': 'Payment reporting',
  'E-invoices and agreements': 'E-invoices and agreements',
  'Create e-invoice agreement': 'Create e-invoice agreement',
  'Recurring payment': 'Recurring payment',
  'View and edit payment agreements': 'View and edit payment agreements',
  'See also': 'See also',
  'E-invoice archive': 'E-invoice archive',
  'Message and notification settings': 'Message and notification settings',
  'Balances and transactions': 'Balances and transactions',
  Balances: 'Balances',
  Transactions: 'Transactions',
  'Open account': 'Open account',
  'Current account': 'Current account',
  'Savings and deposit accounts': 'Savings and deposit accounts',
  'Account for a child': 'Account for a child',
  'Frequently asked': 'Frequently asked',
  'Account FAQ': 'Account FAQ',
  'Account statements and bank mail': 'Account statements and bank mail',
  Cards: 'Cards',
  'Card overview': 'Card overview',
  'Apply for a card': 'Apply for a card',
  'Card settings': 'Card settings',
  'Card limits': 'Card limits',
  Currency: 'Currency',
  'Currency accounts': 'Currency accounts',
  'Exchange rates': 'Exchange rates',
  'Travel money': 'Travel money',
  'Card FAQ': 'Card FAQ',
  'Card statements': 'Card statements',
  'Security settings': 'Security settings',
  'Investment overview': 'Investment overview',
  Funds: 'Funds',
  Stocks: 'Stocks',
  'Investment accounts': 'Investment accounts',
  'Trading and custody': 'Trading and custody',
  Trading: 'Trading',
  'Custody accounts': 'Custody accounts',
  Prices: 'Prices',
  'News and analysis': 'News and analysis',
  'Market news': 'Market news',
  Research: 'Research',
  'Help with investing': 'Help with investing',
  'Investment FAQ': 'Investment FAQ',
  'Risk information': 'Risk information',
  'Balances and activity': 'Balances and activity',
  Overview: 'Overview',
  'Wallet balances': 'Wallet balances',
  'Transaction history': 'Transaction history',
  'Manage digital assets': 'Manage digital assets',
  'Buy / Sell': 'Buy / Sell',
  'External withdrawals': 'External withdrawals',
  'Custody model': 'Custody model',
  Reporting: 'Reporting',
  'Tax reports': 'Tax reports',
  'Export documents': 'Export documents',
  'Audit trail': 'Audit trail',
  'What is custody?': 'What is custody?',
  'Are digital assets deposits?': 'Are digital assets deposits?',
  'What happens during withdrawal?': 'What happens during withdrawal?',
  'Online banking': 'Online banking',
  'Online services overview': 'Online services overview',
  'Online banking settings': 'Online banking settings',
  'Mobile banking': 'Mobile banking',
  'Strong authentication': 'Strong authentication',
  Messages: 'Messages',
  'Messages and notifications': 'Messages and notifications',
  'Message settings': 'Message settings',
  'Email notifications': 'Email notifications',
  'SMS notifications': 'SMS notifications',
  'Push notifications': 'Push notifications',
  Security: 'Security',
  'Login security': 'Login security',
  'Device management': 'Device management',
  'Security alerts': 'Security alerts',
  Help: 'Help',
  Support: 'Support',
  'Online services FAQ': 'Online services FAQ',
  'Contact support': 'Contact support',
  Wallet: 'Wallet',
  Custody: 'Custody',
  Withdrawals: 'Withdrawals',
  Reports: 'Reports',
  'Simulated loans section for the Aurora Bank online banking prototype.':
    'Simulated loans section for the Aurora Bank online banking prototype.',
  'Simulated investments section. The prototype separates traditional investments from Digital Assets.':
    'Simulated investments section. The prototype separates traditional investments from Digital Assets.',
  'Simulated insurance section for the Aurora Bank online banking prototype.':
    'Simulated insurance section for the Aurora Bank online banking prototype.',
  'Simulated online and mobile services section for the Aurora Bank online banking prototype.':
    'Simulated online and mobile services section for the Aurora Bank online banking prototype.',
  'Demo section': 'Demo section',
  'Module placeholder': 'Module placeholder',
  'Coming later': 'Coming later',
  'Prototype note': 'Prototype note',
  Scope: 'Scope',
  'This section is included to make the online banking prototype feel complete. The main focus of this project remains the bank-integrated Digital Assets module.':
    'This section is included to make the online banking prototype feel complete. The main focus of this project remains the bank-integrated Digital Assets module.',
  'This page uses simulated content only. No real bank APIs, payments, cards, loans, or investment services are connected.':
    'This page uses simulated content only. No real bank APIs, payments, cards, loans, or investment services are connected.',
  Ready: 'Ready',
  'Not ready': 'Not ready',
  Draft: 'Draft',
  Submitted: 'Submitted',
  Recorded: 'Recorded',
  Completed: 'Completed',
  Active: 'Active',
  Monitoring: 'Monitoring',
  Controlled: 'Controlled',
  Denied: 'Denied',
  Created: 'Created',
  Paused: 'Paused',
  Blocked: 'Blocked',
  Required: 'Required',
  Escalated: 'Escalated',
  Confirmed: 'Confirmed',
  Visible: 'Visible',
  Enabled: 'Enabled',
  Disabled: 'Disabled',
  Conditional: 'Conditional',
  'Under review': 'Under review',
  'Pending review': 'Pending review',
  'Pending local review': 'Pending local review',
  'Pending local prototype review': 'Pending local prototype review',
  'Local fallback': 'Local fallback',
  'Backend model': 'Backend model',
  'Backend evaluation': 'Backend evaluation',
  'Prototype estimate': 'Prototype estimate',
  'Backend audit concept': 'Backend audit concept',
  'Local draft': 'Local draft',
  Evaluated: 'Evaluated',
  Evaluating: 'Evaluating',
  'Evaluating...': 'Evaluating...',
  'Ready for review': 'Ready for review',
  'Ready for evaluation': 'Ready for evaluation',
  'Needs correction': 'Needs correction',
  'Address mismatch': 'Address mismatch',
  'Unavailable externally': 'Unavailable externally',
  'Case created': 'Case created',
  'Review case created': 'Review case created',
  'Audit event recorded': 'Audit event recorded',
  'Backend decision returned': 'Backend decision returned',
  'Evaluation submitted': 'Evaluation submitted',
  'Buy/sell evaluation submitted': 'Buy/sell evaluation submitted',
  'Trade form opened': 'Trade form opened',
  'Local estimate prepared': 'Local estimate prepared',
  'Withdrawal form opened': 'Withdrawal form opened',
  'Asset and network selected': 'Asset and network selected',
  'Destination address entered': 'Destination address entered',
  'Protection review prepared': 'Protection review prepared',
  'Submitting...': 'Submitting...',
  'Submit payment': 'Submit payment',
  'Not selected': 'Not selected',
  'Not provided': 'Not provided',
  Yes: 'Yes',
  No: 'No',
  'Control status': 'Control status',
  'Static demo evidence': 'Static demo evidence',
  'Local deterministic prototype': 'Local deterministic prototype',
  'Local deterministic prototype only': 'Local deterministic prototype only',
  'Local prototype only': 'Local prototype only',
  'No live execution': 'No live execution',
  'No real assets': 'No real assets',
  'No real agent execution': 'No real agent execution',
  'No real custodian access': 'No real custodian access',
  'No real bank integration': 'No real bank integration',
  'No real custodian integration': 'No real custodian integration',
  'No real custody': 'No real custody',
  'No real blockchain execution': 'No real blockchain execution',
  'No real cloud deployment': 'No real cloud deployment',
  'No real employee monitoring': 'No real employee monitoring',
  'No legal accusation or criminal finding':
    'No legal accusation or criminal finding',
  'No private keys or secrets': 'No private keys or secrets',
  'No secrets': 'No secrets',
  'No real onboarding': 'No real onboarding',
  'No credential creation': 'No credential creation',
  'No identity verification': 'No identity verification',
  'No production strong authentication': 'No production strong authentication',
  'No real customer data': 'No real customer data',
  'No real legal report is generated': 'No real legal report is generated',
  'Governance modules': 'Governance modules',
  'Controlled agent operating model': 'Controlled agent operating model',
  'Agent governance': 'Agent governance',
  'Agent governance console': 'Agent governance console',
  'Bank staff control': 'Bank staff control',
  'Institutional control view for simulated agent identity, policy, permissions, revocation, abuse detection, and audit evidence.':
    'Institutional control view for simulated agent identity, policy, permissions, revocation, abuse detection, and audit evidence.',
  'Operating principle': 'Operating principle',
  'No blind trust': 'No blind trust',
  'Aurora does not blindly trust AI, agents, partners, custodians, or human reviewers. Sensitive decisions are controlled, scored, evidenced, reviewable, and auditable before operation state can change.':
    'Aurora does not blindly trust AI, agents, partners, custodians, or human reviewers. Sensitive decisions are controlled, scored, evidenced, reviewable, and auditable before operation state can change.',
  'Decision control chain': 'Decision control chain',
  'Before sensitive action': 'Before sensitive action',
  'Control step': 'Control step',
  'Risk signal captured': 'Risk signal captured',
  'Guardrail evaluated': 'Guardrail evaluated',
  'Evidence package prepared': 'Evidence package prepared',
  'Review case routed': 'Review case routed',
  'Agent and human integrity checked': 'Agent and human integrity checked',
  'Decision recorded': 'Decision recorded',
  'Safety boundary': 'Safety boundary',
  'Prototype constraints': 'Prototype constraints',
  'Related staff modules': 'Related staff modules',
  'Review paths': 'Review paths',
  'Open risk operations': 'Open risk operations',
  'Open human approval integrity': 'Open human approval integrity',
  'Aurora Digital Assets is a local deterministic prototype. No real agents, custodians, bank systems, secrets, or customer records are connected.':
    'Aurora Digital Assets is a local deterministic prototype. No real agents, custodians, bank systems, secrets, or customer records are connected.',
  'Agent Registry': 'Agent Registry',
  'Agent Passport': 'Agent Passport',
  'Agent Permissions': 'Agent Permissions',
  'Agent Action Audit': 'Agent Action Audit',
  'Agent Revocation': 'Agent Revocation',
  'Agent Policy Engine': 'Agent Policy Engine',
  'Agent Abuse Detection': 'Agent Abuse Detection',
  'Agent Identity Governance': 'Agent Identity Governance',
  'Inventory of simulated agent identities, ownership, permitted operating zones, and current lifecycle status.':
    'Inventory of simulated agent identities, ownership, permitted operating zones, and current lifecycle status.',
  'Structured profile for declared purpose, control evidence, model boundaries, and institutional review readiness.':
    'Structured profile for declared purpose, control evidence, model boundaries, and institutional review readiness.',
  'Deterministic permission model for what an agent may request, recommend, prepare, or never execute.':
    'Deterministic permission model for what an agent may request, recommend, prepare, or never execute.',
  'Audit trail view for simulated agent recommendations, evidence creation, routing decisions, and blocked actions.':
    'Audit trail view for simulated agent recommendations, evidence creation, routing decisions, and blocked actions.',
  'Control path for suspending or revoking an agent identity when evidence, policy, or operating context changes.':
    'Control path for suspending or revoking an agent identity when evidence, policy, or operating context changes.',
  'Policy checks for permitted actions, sensitive operation boundaries, escalation routing, and required evidence.':
    'Policy checks for permitted actions, sensitive operation boundaries, escalation routing, and required evidence.',
  'Static risk indicators for prompt abuse, policy bypass attempts, excessive access requests, and suspicious routing.':
    'Static risk indicators for prompt abuse, policy bypass attempts, excessive access requests, and suspicious routing.',
  'Governance record for identity ownership, scope, segregation, approval chain, and revocation readiness.':
    'Governance record for identity ownership, scope, segregation, approval chain, and revocation readiness.',
  'Bank operations integrity': 'Bank operations integrity',
  'Human approval integrity console': 'Human approval integrity console',
  'Critical override protected': 'Critical override protected',
  'Approval controls': 'Approval controls',
  'Reviewer integrity safeguards': 'Reviewer integrity safeguards',
  'Static deterministic control used to prevent human approval from becoming an uncontrolled bypass path.':
    'Static deterministic control used to prevent human approval from becoming an uncontrolled bypass path.',
  'Static demo case': 'Static demo case',
  'External wallet withdrawal blocked': 'External wallet withdrawal blocked',
  'Core principle': 'Core principle',
  'Controlled risk event': 'Controlled risk event',
  'A human reviewer can add context, request evidence, or approve low-risk steps within policy. A human reviewer cannot override a critical system block alone.':
    'A human reviewer can add context, request evidence, or approve low-risk steps within policy. A human reviewer cannot override a critical system block alone.',
  'Required evidence': 'Required evidence',
  'Before approval can proceed': 'Before approval can proceed',
  'Evidence item': 'Evidence item',
  'Open agent governance': 'Open agent governance',
  'Open evidence packages': 'Open evidence packages',
  'Aurora Digital Assets is a local deterministic prototype. No real employee monitoring, legal accusation, criminal finding, custody, blockchain execution, cloud deployment, or secrets are present.':
    'Aurora Digital Assets is a local deterministic prototype. No real employee monitoring, legal accusation, criminal finding, custody, blockchain execution, cloud deployment, or secrets are present.',
  'No single human can override a critical system block':
    'No single human can override a critical system block',
  'Dual control / four-eyes approval': 'Dual control / four-eyes approval',
  'Segregation of duties': 'Segregation of duties',
  'Reviewer conflict detection': 'Reviewer conflict detection',
  'Emergency override control': 'Emergency override control',
  'Post-approval audit': 'Post-approval audit',
  'Critical system block active': 'Critical system block active',
  'Emergency override requested': 'Emergency override requested',
  'Human approval blocked': 'Human approval blocked',
  'Second reviewer required': 'Second reviewer required',
  'Compliance escalation required': 'Compliance escalation required',
  'Evidence package created': 'Evidence package created',
  'Operation paused': 'Operation paused',
  'System block reason': 'System block reason',
  'Requester identity and role': 'Requester identity and role',
  'Second reviewer requirement': 'Second reviewer requirement',
  'Conflict check result': 'Conflict check result',
  'Compliance escalation record': 'Compliance escalation record',
  'Post-approval audit event': 'Post-approval audit event',
  'Bank staff customer onboarding model':
    'Bank staff customer onboarding model',
  'Identity and document review': 'Identity and document review',
  'Private PIN / secret credential setup':
    'Private PIN / secret credential setup',
  'Digital Assets eligibility check': 'Digital Assets eligibility check',
  'Bank staff': 'Bank staff',
  Customer: 'Customer',
  'Bank system / Compliance': 'Bank system / Compliance',
  'Private customer action': 'Private customer action',
  'Passport or national identity document':
    'Passport or national identity document',
  'Personal identity information': 'Personal identity information',
  'Contact information': 'Contact information',
  'Customer enters PIN privately': 'Customer enters PIN privately',
  'Staff must not see the secret credential':
    'Staff must not see the secret credential',
  'Credential is not displayed back to staff':
    'Credential is not displayed back to staff',
  'Active banking relationship': 'Active banking relationship',
  'Identity verification completed': 'Identity verification completed',
  'Source-of-funds reviewed': 'Source-of-funds reviewed',
  'Strong authentication enabled': 'Strong authentication enabled',
  'Completed by bank': 'Completed by bank',
  'Finland resident': 'Finland resident',
  'Reviewed by bank': 'Reviewed by bank',
  'Customer relationship created through bank-managed onboarding.':
    'Customer relationship created through bank-managed onboarding.',
  'Online banking credentials issued by the bank.':
    'Online banking credentials issued by the bank.',
  'PIN setup is treated as a private customer action.':
    'PIN setup is treated as a private customer action.',
  'Digital Assets access remains subject to eligibility and review controls.':
    'Digital Assets access remains subject to eligibility and review controls.',
  'Backend bank staff model unavailable. Showing local prototype fallback.':
    'Backend bank staff model unavailable. Showing local prototype fallback.',
  'Simulated bank login service is unavailable. No session was created.':
    'Simulated bank login service is unavailable. No session was created.',
  'Login approval request is unavailable. Please start again.':
    'Login approval request is unavailable. Please start again.',
  'Simulated mobile key approval is unavailable. No session was created.':
    'Simulated mobile key approval is unavailable. No session was created.',
  'Go to Aurora Bank home': 'Go to Aurora Bank home',
  Statements: 'Statements',
  'Reports overview': 'Reports overview',
  'Account statements': 'Account statements',
  'Bank mail': 'Bank mail',
  'Tax and exports': 'Tax and exports',
  'Payment receipts': 'Payment receipts',
  'Audit and evidence': 'Audit and evidence',
  'Evidence records': 'Evidence records',
  'Compliance records': 'Compliance records',
  'Aurora Trust Engine': 'Aurora Trust Engine',
  'Asset rail governance': 'Asset rail governance',
  'Evidence packages': 'Evidence packages',
  'Compliance review': 'Compliance review',
  'Related records': 'Related records',
  'Simulated action': 'Simulated action',
  Available: 'Available',
  Concept: 'Concept',
  'Not generated': 'Not generated',
  'Not sent': 'Not sent',
  Simulated: 'Simulated',
  None: 'None',
  Source: 'Source',
  Delivery: 'Delivery',
  Certification: 'Certification',
  'Tax advice': 'Tax advice',
  'Tax filing': 'Tax filing',
  'Customer data': 'Customer data',
  'No real bank statements': 'No real bank statements',
  'No real card statements': 'No real card statements',
  'No tax advice': 'No tax advice',
  'No export generated': 'No export generated',
  'Deterministic audit rows': 'Deterministic audit rows',
  'No real messages': 'No real messages',
  'No evidence exported': 'No evidence exported',
  'No regulatory certification': 'No regulatory certification',
  'Account documents': 'Account documents',
  'Available statement concepts': 'Available statement concepts',
  'Statement controls': 'Statement controls',
  'Document status': 'Document status',
  'View statement': 'View statement',
  'View document': 'View document',
  'Card documents': 'Card documents',
  'Card statement concepts': 'Card statement concepts',
  'No card transactions': 'No card transactions',
  'Card status': 'Card status',
  'Statement safeguards': 'Statement safeguards',
  'No real card data': 'No real card data',
  'Open card statement': 'Open card statement',
  'Open statement': 'Open statement',
  'Tax documents': 'Tax documents',
  'Report placeholders': 'Report placeholders',
  'No real tax document': 'No real tax document',
  'Tax boundary': 'Tax boundary',
  'Tax safeguards': 'Tax safeguards',
  'Not submitted': 'Not submitted',
  'Download tax report': 'Download tax report',
  'Download report': 'Download report',
  'Export options': 'Export options',
  'Document export concepts': 'Document export concepts',
  'PDF CSV JSON placeholders': 'PDF CSV JSON placeholders',
  'Export status': 'Export status',
  'Format placeholders': 'Format placeholders',
  'Placeholder only': 'Placeholder only',
  'Export selected records': 'Export selected records',
  Export: 'Export',
  'Audit events': 'Audit events',
  'Simulated audit trail': 'Simulated audit trail',
  Traceability: 'Traceability',
  'Audit safeguards': 'Audit safeguards',
  Execution: 'Execution',
  'Audit data': 'Audit data',
  'Open audit entry': 'Open audit entry',
  'Open entry': 'Open entry',
  'Secure messages': 'Secure messages',
  'Bank mail inbox': 'Bank mail inbox',
  'No customer communication': 'No customer communication',
  'Message status': 'Message status',
  'Communication safeguards': 'Communication safeguards',
  'Open secure message': 'Open secure message',
  'Open message': 'Open message',
  'Evidence record concepts': 'Evidence record concepts',
  'Evidence status': 'Evidence status',
  'Record states': 'Record states',
  'Open evidence record': 'Open evidence record',
  'Open record': 'Open record',
  'Compliance cases': 'Compliance cases',
  'Compliance record concepts': 'Compliance record concepts',
  'No legal certification': 'No legal certification',
  'Compliance boundary': 'Compliance boundary',
  'Record safeguards': 'Record safeguards',
  'Legal report': 'Legal report',
  'Open compliance case': 'Open compliance case',
  'Open case': 'Open case',
  'Current account statement': 'Current account statement',
  'Monthly statement concept for the everyday current account.':
    'Monthly statement concept for the everyday current account.',
  'Statement period: April 2026': 'Statement period: April 2026',
  'Savings account statement': 'Savings account statement',
  'Savings and deposit account statement placeholder.':
    'Savings and deposit account statement placeholder.',
  'Monthly statement': 'Monthly statement',
  'Consolidated monthly account document concept.':
    'Consolidated monthly account document concept.',
  'Document status: simulated': 'Document status: simulated',
  'Annual summary': 'Annual summary',
  'Year-end banking summary placeholder for customer review.':
    'Year-end banking summary placeholder for customer review.',
  'Document status: not generated': 'Document status: not generated',
  'Mock banking records': 'Mock banking records',
  'The button is disabled because no real bank statement is opened or generated in this prototype.':
    'The button is disabled because no real bank statement is opened or generated in this prototype.',
  'Card monthly statement': 'Card monthly statement',
  'Monthly card statement placeholder for a simulated Aurora Bank card.':
    'Monthly card statement placeholder for a simulated Aurora Bank card.',
  'Card transaction summary': 'Card transaction summary',
  'Summary row for card activity in the local demo only.':
    'Summary row for card activity in the local demo only.',
  'Currency conversion notice': 'Currency conversion notice',
  'Notice concept for card purchases in another currency.':
    'Notice concept for card purchases in another currency.',
  'No conversion is calculated': 'No conversion is calculated',
  'Card security notice': 'Card security notice',
  'Security information placeholder for safe card usage.':
    'Security information placeholder for safe card usage.',
  'No PDF, card account record, card statement, or card transaction file is opened in this prototype.':
    'No PDF, card account record, card statement, or card transaction file is opened in this prototype.',
  'Annual tax summary': 'Annual tax summary',
  'Yearly tax summary placeholder for the local prototype.':
    'Yearly tax summary placeholder for the local prototype.',
  'Tax year: 2026': 'Tax year: 2026',
  'Digital asset tax report concept': 'Digital asset tax report concept',
  'Concept report for digital asset activity and reporting traceability.':
    'Concept report for digital asset activity and reporting traceability.',
  'No official filing data': 'No official filing data',
  'Investment tax report concept': 'Investment tax report concept',
  'Traditional investment reporting placeholder kept separate from digital assets.':
    'Traditional investment reporting placeholder kept separate from digital assets.',
  'No investment advice': 'No investment advice',
  'Downloadable report placeholders': 'Downloadable report placeholders',
  'Static labels for PDF, CSV, and JSON report formats.':
    'Static labels for PDF, CSV, and JSON report formats.',
  'No file is created': 'No file is created',
  'The action is disabled because no real tax report, tax filing, or tax advice is generated.':
    'The action is disabled because no real tax report, tax filing, or tax advice is generated.',
  'Export account documents': 'Export account documents',
  'Account document export placeholder for PDF format.':
    'Account document export placeholder for PDF format.',
  'Format: PDF': 'Format: PDF',
  'Export payment receipts': 'Export payment receipts',
  'Payment receipt bundle placeholder for banking records.':
    'Payment receipt bundle placeholder for banking records.',
  'Export digital asset audit trail': 'Export digital asset audit trail',
  'Digital asset audit trail placeholder for CSV and JSON records.':
    'Digital asset audit trail placeholder for CSV and JSON records.',
  'Formats: CSV, JSON': 'Formats: CSV, JSON',
  'Export compliance evidence package': 'Export compliance evidence package',
  'Evidence package export concept for controlled review workflows.':
    'Evidence package export concept for controlled review workflows.',
  'Formats: PDF, JSON': 'Formats: PDF, JSON',
  'No real document, archive, bank statement, evidence package, CSV, JSON, or PDF is generated.':
    'No real document, archive, bank statement, evidence package, CSV, JSON, or PDF is generated.',
  'Risk decision recorded': 'Risk decision recorded',
  'Risk operation decision row for a simulated digital asset workflow.':
    'Risk operation decision row for a simulated digital asset workflow.',
  'Correlation ID: CORR-AUDIT-001': 'Correlation ID: CORR-AUDIT-001',
  'Evidence package creation event for an internal review concept.':
    'Evidence package creation event for an internal review concept.',
  'Package ID: EPK-DEMO-001': 'Package ID: EPK-DEMO-001',
  'Review case opened': 'Review case opened',
  'Compliance review case placeholder opened from a simulated alert.':
    'Compliance review case placeholder opened from a simulated alert.',
  'Case ID: CASE-DEMO-001': 'Case ID: CASE-DEMO-001',
  'Sensitive approval blocked': 'Sensitive approval blocked',
  'Sensitive approval control blocked a simulated high-risk action.':
    'Sensitive approval control blocked a simulated high-risk action.',
  'Guardrail: sensitive approval': 'Guardrail: sensitive approval',
  'Human approval integrity guard event':
    'Human approval integrity guard event',
  'Integrity guard event showing reviewer control checks.':
    'Integrity guard event showing reviewer control checks.',
  'Control: human approval integrity': 'Control: human approval integrity',
  'Agent governance event': 'Agent governance event',
  'Agent identity and permission event for governance traceability.':
    'Agent identity and permission event for governance traceability.',
  'Control: agent governance': 'Control: agent governance',
  'Audit rows are deterministic demo records. No real operation, approval, or system event is executed.':
    'Audit rows are deterministic demo records. No real operation, approval, or system event is executed.',
  'Secure message inbox': 'Secure message inbox',
  'Inbox container for local demo notices only.':
    'Inbox container for local demo notices only.',
  'No messages are delivered': 'No messages are delivered',
  'Bank notice': 'Bank notice',
  'General banking notice placeholder for online banking documents.':
    'General banking notice placeholder for online banking documents.',
  'Compliance notification': 'Compliance notification',
  'Compliance notification concept for review and evidence workflows.':
    'Compliance notification concept for review and evidence workflows.',
  'Statement delivery notice': 'Statement delivery notice',
  'Statement delivery notification placeholder.':
    'Statement delivery notification placeholder.',
  'No document delivery': 'No document delivery',
  'No real secure message, notification, email, SMS, or customer communication is opened or sent.':
    'No real secure message, notification, email, SMS, or customer communication is opened or sent.',
  'Evidence package list': 'Evidence package list',
  'Evidence package placeholder for internal review and audit readiness.':
    'Evidence package placeholder for internal review and audit readiness.',
  'Source audit event': 'Source audit event',
  'Audit source reference attached to a simulated evidence package.':
    'Audit source reference attached to a simulated evidence package.',
  'Audit event ID: AUD-DEMO-001': 'Audit event ID: AUD-DEMO-001',
  'Correlation ID placeholder': 'Correlation ID placeholder',
  'Correlation identifier used to connect deterministic demo records.':
    'Correlation identifier used to connect deterministic demo records.',
  'Correlation ID: CORR-DEMO-001': 'Correlation ID: CORR-DEMO-001',
  'Review case link placeholder': 'Review case link placeholder',
  'Review case reference for compliance review navigation.':
    'Review case reference for compliance review navigation.',
  'Closed evidence record': 'Closed evidence record',
  'Closed evidence record concept for completed internal review.':
    'Closed evidence record concept for completed internal review.',
  'Status: closed': 'Status: closed',
  'No evidence package, archive, document, or export is generated from this page.':
    'No evidence package, archive, document, or export is generated from this page.',
  'Compliance case': 'Compliance case',
  'Compliance review case placeholder for document traceability.':
    'Compliance review case placeholder for document traceability.',
  'Case ID: COMP-DEMO-001': 'Case ID: COMP-DEMO-001',
  'Risk operations case': 'Risk operations case',
  'Risk operations record linked to simulated monitoring signals.':
    'Risk operations record linked to simulated monitoring signals.',
  'Case ID: RISK-DEMO-001': 'Case ID: RISK-DEMO-001',
  'Financial crime monitoring case': 'Financial crime monitoring case',
  'Financial crime monitoring concept for alert review workflows.':
    'Financial crime monitoring concept for alert review workflows.',
  'Case ID: FC-DEMO-001': 'Case ID: FC-DEMO-001',
  'Sensitive approval case': 'Sensitive approval case',
  'Sensitive approval record for controlled operation review.':
    'Sensitive approval record for controlled operation review.',
  'Case ID: SAP-DEMO-001': 'Case ID: SAP-DEMO-001',
  'Custodian readiness case': 'Custodian readiness case',
  'Custodian readiness and operational review placeholder.':
    'Custodian readiness and operational review placeholder.',
  'Case ID: CUST-DEMO-001': 'Case ID: CUST-DEMO-001',
  'No legal report, regulatory filing, certification, or customer record is opened or generated.':
    'No legal report, regulatory filing, certification, or customer record is opened or generated.',
  'Local deterministic prototype only. No real document, bank statement, card statement, tax report, secure message, audit trail, evidence package, compliance record, customer data, banking operation, export, or legal certification is created or executed.':
    'Local deterministic prototype only. No real document, bank statement, card statement, tax report, secure message, audit trail, evidence package, compliance record, customer data, banking operation, export, or legal certification is created or executed.',
  'Local deterministic prototype only. No real bank statements, account records, customer data, banking operation, export, or customer communication is created or executed.':
    'Local deterministic prototype only. No real bank statements, account records, customer data, banking operation, export, or customer communication is created or executed.',
  'Local deterministic prototype only. No real card statements, card transactions, cardholder data, banking operation, export, or customer communication is created or executed.':
    'Local deterministic prototype only. No real card statements, card transactions, cardholder data, banking operation, export, or customer communication is created or executed.',
  'Local deterministic prototype only. No real tax document, tax filing, tax advice, customer data, banking operation, export, or legal certification is created or executed.':
    'Local deterministic prototype only. No real tax document, tax filing, tax advice, customer data, banking operation, export, or legal certification is created or executed.',
  'Local deterministic prototype only. No real export, bank statement, tax report, evidence package, customer data, banking operation, or secure message is created or executed.':
    'Local deterministic prototype only. No real export, bank statement, tax report, evidence package, customer data, banking operation, or secure message is created or executed.',
  'Local deterministic prototype only. No real audit trail, customer record, approval, agent execution, banking operation, evidence package, export, or legal certification is created or executed.':
    'Local deterministic prototype only. No real audit trail, customer record, approval, agent execution, banking operation, evidence package, export, or legal certification is created or executed.',
  'Local deterministic prototype only. No real secure message, bank mail, customer communication, customer data, document delivery, export, or banking operation is created or executed.':
    'Local deterministic prototype only. No real secure message, bank mail, customer communication, customer data, document delivery, export, or banking operation is created or executed.',
  'Local deterministic prototype only. No real evidence package, export, audit file, customer data, banking operation, or legal certification is created or executed.':
    'Local deterministic prototype only. No real evidence package, export, audit file, customer data, banking operation, or legal certification is created or executed.',
  'Local deterministic prototype only. No real compliance record, legal report, regulatory certification, customer data, banking operation, evidence export, or secure message is created or executed.':
    'Local deterministic prototype only. No real compliance record, legal report, regulatory certification, customer data, banking operation, evidence export, or secure message is created or executed.',
  'Checking banking session...': 'Checking banking session...',
} satisfies Record<string, string>

const esPhrases: Record<keyof typeof enPhrases, string> = {
  'Local deterministic prototype only. No real assets, no real custody, no real bank integration, no real custodian integration, no real blockchain execution, no real cloud deployment, and no private keys or secrets.':
    'Prototipo local y determinístico. Sin activos reales, sin custodia real, sin integración bancaria real, sin integración real con custodios, sin ejecución blockchain real, sin despliegue cloud real y sin llaves privadas ni secretos.',
  'Human review is not a trust anchor. It is a controlled risk event.':
    'La revisión humana no es un ancla de confianza. Es un evento de riesgo controlado.',
  'Every agent must be identifiable, permission-bound, revocable, and auditable.':
    'Todo agente debe ser identificable, limitado por permisos, revocable y auditable.',
  'Go to online banking dashboard': 'Ir al panel de banca en línea',
  'Digital Assets navigation': 'Navegación de activos digitales',
  'Hidden amount': 'Importe oculto',
  amount: 'importe',
  Home: 'Inicio',
  Payments: 'Pagos',
  Accounts: 'Cuentas',
  'Cards and Currency': 'Tarjetas y moneda',
  Loans: 'Créditos',
  'Loan overview': 'Resumen de préstamos',
  'Apply for a loan': 'Solicitar préstamo',
  Mortgage: 'Préstamo hipotecario',
  'Consumer loan': 'Crédito de consumo',
  'Student loan': 'Préstamo estudiantil',
  'Manage loans': 'Gestionar préstamos',
  'Loan calculator': 'Calculadora de préstamo',
  'Repayment plan': 'Plan de pago',
  'Loan documents': 'Documentos del préstamo',
  'Loan FAQ': 'Preguntas frecuentes de préstamos',
  Investments: 'Inversiones',
  Insurance: 'Seguros',
  'Insurance overview': 'Resumen de seguros',
  'Home insurance': 'Seguro de hogar',
  'Travel insurance': 'Seguro de viaje',
  'Life insurance': 'Seguro de vida',
  'Health insurance': 'Seguro de salud',
  Claims: 'Siniestros',
  'Claims overview': 'Resumen de siniestros',
  'Report a claim': 'Reportar siniestro',
  'Claim documents': 'Documentos de siniestro',
  'Documents and support': 'Documentos y soporte',
  'Insurance documents': 'Documentos del seguro',
  'Insurance FAQ': 'Preguntas frecuentes de seguros',
  'Coverage information': 'Información de cobertura',
  'Digital Assets': 'Activos digitales',
  Documents: 'Documentos',
  'Online Services': 'Servicios en línea',
  'New payment': 'Nuevo pago',
  'Approve payments': 'Aprobar pagos',
  'International payment': 'Pago internacional',
  Recipients: 'Destinatarios',
  'Payment limits': 'Límites de pago',
  'Digital asset payments': 'Pagos con activos digitales',
  'Digital asset payment': 'Pago con activo digital',
  'Supported business recipients': 'Destinatarios comerciales admitidos',
  'Payment asset settings': 'Configuración de activos de pago',
  'Payment reporting': 'Informes de pagos',
  'E-invoices and agreements': 'Facturas electrónicas y acuerdos',
  'Create e-invoice agreement': 'Crear acuerdo de factura electrónica',
  'Recurring payment': 'Pago recurrente',
  'View and edit payment agreements': 'Ver y editar acuerdos de pago',
  'See also': 'Ver también',
  'E-invoice archive': 'Archivo de facturas electrónicas',
  'Message and notification settings':
    'Configuración de mensajes y notificaciones',
  'Balances and transactions': 'Saldos y movimientos',
  Balances: 'Saldos',
  Transactions: 'Movimientos',
  'Open account': 'Abrir cuenta',
  'Current account': 'Cuenta corriente',
  'Savings and deposit accounts': 'Cuentas de ahorro y depósito',
  'Account for a child': 'Cuenta para un menor',
  'Frequently asked': 'Preguntas frecuentes',
  'Account FAQ': 'Preguntas frecuentes sobre cuentas',
  'Account statements and bank mail': 'Extractos de cuenta y correo bancario',
  Cards: 'Tarjetas',
  'Card overview': 'Resumen de tarjetas',
  'Apply for a card': 'Solicitar tarjeta',
  'Card settings': 'Configuración de tarjeta',
  'Card limits': 'Límites de tarjeta',
  Currency: 'Moneda',
  'Currency accounts': 'Cuentas en divisa',
  'Exchange rates': 'Tipos de cambio',
  'Travel money': 'Dinero para viajes',
  'Card FAQ': 'Preguntas frecuentes sobre tarjetas',
  'Card statements': 'Extractos de tarjeta',
  'Security settings': 'Configuración de seguridad',
  'Investment overview': 'Resumen de inversiones',
  Funds: 'Fondos',
  Stocks: 'Acciones',
  'Investment accounts': 'Cuentas de inversión',
  'Trading and custody': 'Negociación y custodia',
  Trading: 'Negociación',
  'Custody accounts': 'Cuentas de custodia',
  Prices: 'Precios',
  'News and analysis': 'Noticias y análisis',
  'Market news': 'Noticias de mercado',
  Research: 'Análisis',
  'Help with investing': 'Ayuda con inversiones',
  'Investment FAQ': 'Preguntas frecuentes sobre inversiones',
  'Risk information': 'Información de riesgo',
  'Balances and activity': 'Saldos y actividad',
  Overview: 'Resumen',
  'Wallet balances': 'Saldos de billetera',
  'Transaction history': 'Historial de movimientos',
  'Manage digital assets': 'Gestionar activos digitales',
  'Buy / Sell': 'Comprar / vender',
  'External withdrawals': 'Retiros externos',
  'Custody model': 'Modelo de custodia',
  Reporting: 'Informes',
  'Tax reports': 'Informes fiscales',
  'Export documents': 'Exportar documentos',
  'Audit trail': 'Trazabilidad de auditoría',
  'What is custody?': '¿Qué es la custodia?',
  'Are digital assets deposits?': '¿Los activos digitales son depósitos?',
  'What happens during withdrawal?': '¿Qué ocurre durante un retiro?',
  'Online banking': 'Banca en línea',
  'Online services overview': 'Resumen de servicios en línea',
  'Online banking settings': 'Configuración de banca en línea',
  'Mobile banking': 'Banca móvil',
  'Strong authentication': 'Autenticación fuerte',
  Messages: 'Mensajes',
  'Messages and notifications': 'Mensajes y notificaciones',
  'Message settings': 'Configuración de mensajes',
  'Email notifications': 'Notificaciones por correo electrónico',
  'SMS notifications': 'Notificaciones por SMS',
  'Push notifications': 'Notificaciones push',
  Security: 'Seguridad',
  'Login security': 'Seguridad de inicio de sesión',
  'Device management': 'Gestión de dispositivos',
  'Security alerts': 'Alertas de seguridad',
  Help: 'Ayuda',
  Support: 'Soporte',
  'Online services FAQ': 'Preguntas frecuentes de servicios en línea',
  'Contact support': 'Contactar soporte',
  Wallet: 'Billetera',
  Custody: 'Custodia',
  Withdrawals: 'Retiros',
  Reports: 'Informes',
  'Simulated loans section for the Aurora Bank online banking prototype.':
    'Sección simulada de créditos para el prototipo de banca en línea de Aurora Bank.',
  'Simulated investments section. The prototype separates traditional investments from Digital Assets.':
    'Sección simulada de inversiones. El prototipo separa las inversiones tradicionales de los activos digitales.',
  'Simulated insurance section for the Aurora Bank online banking prototype.':
    'Sección simulada de seguros para el prototipo de banca en línea de Aurora Bank.',
  'Simulated online and mobile services section for the Aurora Bank online banking prototype.':
    'Sección simulada de servicios en línea y móviles para el prototipo de banca en línea de Aurora Bank.',
  'Demo section': 'Sección demo',
  'Module placeholder': 'Marcador de módulo',
  'Coming later': 'Próximamente',
  'Prototype note': 'Nota del prototipo',
  Scope: 'Alcance',
  'This section is included to make the online banking prototype feel complete. The main focus of this project remains the bank-integrated Digital Assets module.':
    'Esta sección se incluye para que el prototipo de banca en línea resulte completo. El foco principal del proyecto sigue siendo el módulo de Digital Assets integrado en banca.',
  'This page uses simulated content only. No real bank APIs, payments, cards, loans, or investment services are connected.':
    'Esta página usa solo contenido simulado. No hay APIs bancarias, pagos, tarjetas, créditos ni servicios de inversión reales conectados.',
  Ready: 'Listo',
  'Not ready': 'No listo',
  Draft: 'Borrador',
  Submitted: 'Enviado',
  Recorded: 'Registrado',
  Completed: 'Completado',
  Active: 'Activo',
  Monitoring: 'Monitoreo',
  Controlled: 'Controlado',
  Denied: 'Denegado',
  Created: 'Creado',
  Paused: 'Pausado',
  Blocked: 'Bloqueado',
  Required: 'Requerido',
  Escalated: 'Escalado',
  Confirmed: 'Confirmado',
  Visible: 'Visible',
  Enabled: 'Habilitado',
  Disabled: 'Deshabilitado',
  Conditional: 'Condicional',
  'Under review': 'En revisión',
  'Pending review': 'Pendiente de revisión',
  'Pending local review': 'Pendiente de revisión local',
  'Pending local prototype review':
    'Pendiente de revisión en prototipo local',
  'Local fallback': 'Alternativa local',
  'Backend model': 'Modelo backend',
  'Backend evaluation': 'Evaluación backend',
  'Prototype estimate': 'Estimación del prototipo',
  'Backend audit concept': 'Concepto de auditoría backend',
  'Local draft': 'Borrador local',
  Evaluated: 'Evaluado',
  Evaluating: 'Evaluando',
  'Evaluating...': 'Evaluando...',
  'Ready for review': 'Listo para revisión',
  'Ready for evaluation': 'Listo para evaluación',
  'Needs correction': 'Requiere corrección',
  'Address mismatch': 'Dirección no coincide',
  'Unavailable externally': 'No disponible externamente',
  'Case created': 'Caso creado',
  'Review case created': 'Caso de revisión creado',
  'Audit event recorded': 'Evento de auditoría registrado',
  'Backend decision returned': 'Decisión backend recibida',
  'Evaluation submitted': 'Evaluación enviada',
  'Buy/sell evaluation submitted': 'Evaluación de compra/venta enviada',
  'Trade form opened': 'Formulario de operación abierto',
  'Local estimate prepared': 'Estimación local preparada',
  'Withdrawal form opened': 'Formulario de retiro abierto',
  'Asset and network selected': 'Activo y red seleccionados',
  'Destination address entered': 'Dirección de destino introducida',
  'Protection review prepared': 'Revisión de protección preparada',
  'Submitting...': 'Enviando...',
  'Submit payment': 'Enviar pago',
  'Not selected': 'No seleccionado',
  'Not provided': 'No proporcionado',
  Yes: 'Sí',
  No: 'No',
  'Control status': 'Estado del control',
  'Static demo evidence': 'Evidencia demo estática',
  'Local deterministic prototype': 'Prototipo local determinístico',
  'Local deterministic prototype only': 'Solo prototipo local determinístico',
  'Local prototype only': 'Solo prototipo local',
  'No live execution': 'Sin ejecución real',
  'No real assets': 'Sin activos reales',
  'No real agent execution': 'Sin ejecución real de agentes',
  'No real custodian access': 'Sin acceso real a custodios',
  'No real bank integration': 'Sin integración bancaria real',
  'No real custodian integration': 'Sin integración real con custodios',
  'No real custody': 'Sin custodia real',
  'No real blockchain execution': 'Sin ejecución blockchain real',
  'No real cloud deployment': 'Sin despliegue cloud real',
  'No real employee monitoring': 'Sin monitoreo real de empleados',
  'No legal accusation or criminal finding':
    'Sin acusación legal ni determinación penal',
  'No private keys or secrets': 'Sin llaves privadas ni secretos',
  'No secrets': 'Sin secretos',
  'No real onboarding': 'Sin incorporación real',
  'No credential creation': 'Sin creación de credenciales',
  'No identity verification': 'Sin verificación de identidad',
  'No production strong authentication':
    'Sin autenticación fuerte de producción',
  'No real customer data': 'Sin datos reales de clientes',
  'No real legal report is generated': 'No se genera informe legal real',
  'Governance modules': 'Módulos de gobernanza',
  'Controlled agent operating model': 'Modelo operativo controlado de agentes',
  'Agent governance': 'Gobernanza de agentes',
  'Agent governance console': 'Consola de gobernanza de agentes',
  'Bank staff control': 'Control del personal bancario',
  'Institutional control view for simulated agent identity, policy, permissions, revocation, abuse detection, and audit evidence.':
    'Vista de control institucional para identidad simulada de agentes, políticas, permisos, revocación, detección de abuso y evidencia de auditoría.',
  'Operating principle': 'Principio operativo',
  'No blind trust': 'Sin confianza ciega',
  'Aurora does not blindly trust AI, agents, partners, custodians, or human reviewers. Sensitive decisions are controlled, scored, evidenced, reviewable, and auditable before operation state can change.':
    'Aurora no confía ciegamente en IA, agentes, socios, custodios ni revisores humanos. Las decisiones sensibles se controlan, puntúan, evidencian, revisan y auditan antes de que cambie el estado operativo.',
  'Decision control chain': 'Cadena de control de decisión',
  'Before sensitive action': 'Antes de una acción sensible',
  'Control step': 'Paso de control',
  'Risk signal captured': 'Señal de riesgo capturada',
  'Guardrail evaluated': 'Control preventivo evaluado',
  'Evidence package prepared': 'Paquete de evidencia preparado',
  'Review case routed': 'Caso de revisión enrutado',
  'Agent and human integrity checked':
    'Integridad de agente y humana comprobada',
  'Decision recorded': 'Decisión registrada',
  'Safety boundary': 'Límite de seguridad',
  'Prototype constraints': 'Restricciones del prototipo',
  'Related staff modules': 'Módulos internos relacionados',
  'Review paths': 'Rutas de revisión',
  'Open risk operations': 'Abrir operaciones de riesgo',
  'Open human approval integrity':
    'Abrir integridad de aprobación humana',
  'Aurora Digital Assets is a local deterministic prototype. No real agents, custodians, bank systems, secrets, or customer records are connected.':
    'Aurora Digital Assets es un prototipo local determinístico. No hay agentes, custodios, sistemas bancarios, secretos ni registros de clientes reales conectados.',
  'Agent Registry': 'Agent Registry',
  'Agent Passport': 'Agent Passport',
  'Agent Permissions': 'Agent Permissions',
  'Agent Action Audit': 'Agent Action Audit',
  'Agent Revocation': 'Agent Revocation',
  'Agent Policy Engine': 'Agent Policy Engine',
  'Agent Abuse Detection': 'Agent Abuse Detection',
  'Agent Identity Governance': 'Agent Identity Governance',
  'Inventory of simulated agent identities, ownership, permitted operating zones, and current lifecycle status.':
    'Inventario de identidades de agentes simuladas, titularidad, zonas operativas permitidas y estado actual del ciclo de vida.',
  'Structured profile for declared purpose, control evidence, model boundaries, and institutional review readiness.':
    'Perfil estructurado para propósito declarado, evidencia de control, límites del modelo y preparación para revisión institucional.',
  'Deterministic permission model for what an agent may request, recommend, prepare, or never execute.':
    'Modelo determinístico de permisos para lo que un agente puede solicitar, recomendar, preparar o nunca ejecutar.',
  'Audit trail view for simulated agent recommendations, evidence creation, routing decisions, and blocked actions.':
    'Vista de trazabilidad de auditoría para recomendaciones simuladas de agentes, creación de evidencia, decisiones de enrutamiento y acciones bloqueadas.',
  'Control path for suspending or revoking an agent identity when evidence, policy, or operating context changes.':
    'Ruta de control para suspender o revocar una identidad de agente cuando cambia la evidencia, la política o el contexto operativo.',
  'Policy checks for permitted actions, sensitive operation boundaries, escalation routing, and required evidence.':
    'Controles de política para acciones permitidas, límites de operaciones sensibles, enrutamiento de escalamiento y evidencia requerida.',
  'Static risk indicators for prompt abuse, policy bypass attempts, excessive access requests, and suspicious routing.':
    'Indicadores estáticos de riesgo por abuso de prompts, intentos de eludir políticas, solicitudes excesivas de acceso y enrutamiento sospechoso.',
  'Governance record for identity ownership, scope, segregation, approval chain, and revocation readiness.':
    'Registro de gobernanza para titularidad de identidad, alcance, segregación, cadena de aprobación y preparación de revocación.',
  'Bank operations integrity': 'Integridad operativa bancaria',
  'Human approval integrity console':
    'Consola de integridad de aprobación humana',
  'Critical override protected': 'Anulación crítica protegida',
  'Approval controls': 'Controles de aprobación',
  'Reviewer integrity safeguards': 'Salvaguardas de integridad del revisor',
  'Static deterministic control used to prevent human approval from becoming an uncontrolled bypass path.':
    'Control determinístico estático usado para impedir que la aprobación humana se convierta en una vía de elusión no controlada.',
  'Static demo case': 'Caso demo estático',
  'External wallet withdrawal blocked': 'Retiro a billetera externa bloqueado',
  'Core principle': 'Principio central',
  'Controlled risk event': 'Evento de riesgo controlado',
  'A human reviewer can add context, request evidence, or approve low-risk steps within policy. A human reviewer cannot override a critical system block alone.':
    'Un revisor humano puede añadir contexto, solicitar evidencia o aprobar pasos de bajo riesgo dentro de la política. Un revisor humano no puede anular por sí solo un bloqueo crítico del sistema.',
  'Required evidence': 'Evidencia requerida',
  'Before approval can proceed': 'Antes de que la aprobación pueda continuar',
  'Evidence item': 'Elemento de evidencia',
  'Open agent governance': 'Abrir gobernanza de agentes',
  'Open evidence packages': 'Abrir paquetes de evidencia',
  'Aurora Digital Assets is a local deterministic prototype. No real employee monitoring, legal accusation, criminal finding, custody, blockchain execution, cloud deployment, or secrets are present.':
    'Aurora Digital Assets es un prototipo local determinístico. No hay monitoreo real de empleados, acusación legal, determinación penal, custodia, ejecución blockchain, despliegue cloud ni secretos.',
  'No single human can override a critical system block':
    'Ninguna persona puede anular por sí sola un bloqueo crítico del sistema',
  'Dual control / four-eyes approval':
    'Doble control / aprobación de cuatro ojos',
  'Segregation of duties': 'Segregación de funciones',
  'Reviewer conflict detection': 'Detección de conflicto del revisor',
  'Emergency override control': 'Control de anulación de emergencia',
  'Post-approval audit': 'Auditoría posterior a la aprobación',
  'Critical system block active': 'Bloqueo crítico del sistema activo',
  'Emergency override requested': 'Anulación de emergencia solicitada',
  'Human approval blocked': 'Aprobación humana bloqueada',
  'Second reviewer required': 'Segundo revisor requerido',
  'Compliance escalation required': 'Escalamiento de cumplimiento requerido',
  'Evidence package created': 'Paquete de evidencia creado',
  'Operation paused': 'Operación pausada',
  'System block reason': 'Motivo del bloqueo del sistema',
  'Requester identity and role': 'Identidad y rol del solicitante',
  'Second reviewer requirement': 'Requisito de segundo revisor',
  'Conflict check result': 'Resultado de comprobación de conflicto',
  'Compliance escalation record': 'Registro de escalamiento de cumplimiento',
  'Post-approval audit event': 'Evento de auditoría posterior a la aprobación',
  'Bank staff customer onboarding model':
    'Modelo de incorporación de clientes por personal bancario',
  'Identity and document review': 'Revisión de identidad y documentos',
  'Private PIN / secret credential setup':
    'Configuración privada de PIN / credencial secreta',
  'Digital Assets eligibility check':
    'Comprobación de elegibilidad para activos digitales',
  'Bank staff': 'Personal bancario',
  Customer: 'Cliente',
  'Bank system / Compliance': 'Sistema bancario / Cumplimiento',
  'Private customer action': 'Acción privada del cliente',
  'Passport or national identity document':
    'Pasaporte o documento nacional de identidad',
  'Personal identity information': 'Información de identidad personal',
  'Contact information': 'Información de contacto',
  'Customer enters PIN privately': 'El cliente introduce el PIN en privado',
  'Staff must not see the secret credential':
    'El personal no debe ver la credencial secreta',
  'Credential is not displayed back to staff':
    'La credencial no se muestra al personal',
  'Active banking relationship': 'Relación bancaria activa',
  'Identity verification completed': 'Verificación de identidad completada',
  'Source-of-funds reviewed': 'Origen de fondos revisado',
  'Strong authentication enabled': 'Autenticación fuerte habilitada',
  'Completed by bank': 'Completado por el banco',
  'Finland resident': 'Residente en Finlandia',
  'Reviewed by bank': 'Revisado por el banco',
  'Customer relationship created through bank-managed onboarding.':
    'Relación de cliente creada mediante incorporación gestionada por el banco.',
  'Online banking credentials issued by the bank.':
    'Credenciales de banca en línea emitidas por el banco.',
  'PIN setup is treated as a private customer action.':
    'La configuración del PIN se trata como acción privada del cliente.',
  'Digital Assets access remains subject to eligibility and review controls.':
    'El acceso a Digital Assets sigue sujeto a controles de elegibilidad y revisión.',
  'Backend bank staff model unavailable. Showing local prototype fallback.':
    'Modelo backend de personal bancario no disponible. Se muestra alternativa del prototipo local.',
  'Simulated bank login service is unavailable. No session was created.':
    'El servicio simulado de inicio bancario no está disponible. No se creó ninguna sesión.',
  'Login approval request is unavailable. Please start again.':
    'La solicitud de aprobación de inicio no está disponible. Empiece de nuevo.',
  'Simulated mobile key approval is unavailable. No session was created.':
    'La aprobación simulada con clave móvil no está disponible. No se creó ninguna sesión.',
  'Go to Aurora Bank home': 'Ir al inicio de Aurora Bank',
  Statements: 'Extractos',
  'Reports overview': 'Resumen de informes',
  'Account statements': 'Extractos de cuenta',
  'Bank mail': 'Correo bancario',
  'Tax and exports': 'Fiscalidad y exportaciones',
  'Payment receipts': 'Recibos de pago',
  'Audit and evidence': 'Auditoría y evidencia',
  'Evidence records': 'Registros de evidencia',
  'Compliance records': 'Registros de cumplimiento',
  'Aurora Trust Engine': 'Motor de Confianza Aurora',
  'Asset rail governance': 'Gobernanza de rails de activos',
  'Evidence packages': 'Paquetes de evidencia',
  'Compliance review': 'Revisión de cumplimiento',
  'Related records': 'Registros relacionados',
  'Simulated action': 'Acción simulada',
  Available: 'Disponible',
  Concept: 'Concepto',
  'Not generated': 'No generado',
  'Not sent': 'No enviado',
  Simulated: 'Simulado',
  None: 'Ninguna',
  Source: 'Fuente',
  Delivery: 'Entrega',
  Certification: 'Certificación',
  'Tax advice': 'Asesoría fiscal',
  'Tax filing': 'Declaración fiscal',
  'Customer data': 'Datos de cliente',
  'No real bank statements': 'Sin extractos bancarios reales',
  'No real card statements': 'Sin extractos de tarjeta reales',
  'No tax advice': 'Sin asesoría fiscal',
  'No export generated': 'Sin exportación generada',
  'Deterministic audit rows': 'Filas de auditoría determinísticas',
  'No real messages': 'Sin mensajes reales',
  'No evidence exported': 'Sin evidencia exportada',
  'No regulatory certification': 'Sin certificación regulatoria',
  'Account documents': 'Documentos de cuenta',
  'Available statement concepts': 'Conceptos de extractos disponibles',
  'Statement controls': 'Controles de extractos',
  'Document status': 'Estado del documento',
  'View statement': 'Ver extracto',
  'View document': 'Ver documento',
  'Card documents': 'Documentos de tarjeta',
  'Card statement concepts': 'Conceptos de extractos de tarjeta',
  'No card transactions': 'Sin transacciones de tarjeta',
  'Card status': 'Estado de tarjeta',
  'Statement safeguards': 'Salvaguardas de extractos',
  'No real card data': 'Sin datos reales de tarjeta',
  'Open card statement': 'Abrir extracto de tarjeta',
  'Open statement': 'Abrir extracto',
  'Tax documents': 'Documentos fiscales',
  'Report placeholders': 'Marcadores de informes',
  'No real tax document': 'Sin documento fiscal real',
  'Tax boundary': 'Límite fiscal',
  'Tax safeguards': 'Salvaguardas fiscales',
  'Not submitted': 'No presentado',
  'Download tax report': 'Descargar informe fiscal',
  'Download report': 'Descargar informe',
  'Export options': 'Opciones de exportación',
  'Document export concepts': 'Conceptos de exportación de documentos',
  'PDF CSV JSON placeholders': 'Marcadores PDF CSV JSON',
  'Export status': 'Estado de exportación',
  'Format placeholders': 'Marcadores de formato',
  'Placeholder only': 'Solo marcador',
  'Export selected records': 'Exportar registros seleccionados',
  Export: 'Exportar',
  'Audit events': 'Eventos de auditoría',
  'Simulated audit trail': 'Trazabilidad de auditoría simulada',
  Traceability: 'Trazabilidad',
  'Audit safeguards': 'Salvaguardas de auditoría',
  Execution: 'Ejecución',
  'Audit data': 'Datos de auditoría',
  'Open audit entry': 'Abrir entrada de auditoría',
  'Open entry': 'Abrir entrada',
  'Secure messages': 'Mensajes seguros',
  'Bank mail inbox': 'Bandeja de correo bancario',
  'No customer communication': 'Sin comunicación real con clientes',
  'Message status': 'Estado de mensaje',
  'Communication safeguards': 'Salvaguardas de comunicación',
  'Open secure message': 'Abrir mensaje seguro',
  'Open message': 'Abrir mensaje',
  'Evidence record concepts': 'Conceptos de registros de evidencia',
  'Evidence status': 'Estado de evidencia',
  'Record states': 'Estados de registro',
  'Open evidence record': 'Abrir registro de evidencia',
  'Open record': 'Abrir registro',
  'Compliance cases': 'Casos de cumplimiento',
  'Compliance record concepts': 'Conceptos de registros de cumplimiento',
  'No legal certification': 'Sin certificación legal',
  'Compliance boundary': 'Límite de cumplimiento',
  'Record safeguards': 'Salvaguardas de registros',
  'Legal report': 'Informe legal',
  'Open compliance case': 'Abrir caso de cumplimiento',
  'Open case': 'Abrir caso',
  'Current account statement': 'Extracto de cuenta corriente',
  'Monthly statement concept for the everyday current account.':
    'Concepto de extracto mensual para la cuenta corriente diaria.',
  'Statement period: April 2026': 'Período del extracto: abril de 2026',
  'Savings account statement': 'Extracto de cuenta de ahorro',
  'Savings and deposit account statement placeholder.':
    'Marcador de extracto de cuenta de ahorro y depósito.',
  'Monthly statement': 'Extracto mensual',
  'Consolidated monthly account document concept.':
    'Concepto de documento mensual consolidado de cuentas.',
  'Document status: simulated': 'Estado del documento: simulado',
  'Annual summary': 'Resumen anual',
  'Year-end banking summary placeholder for customer review.':
    'Marcador de resumen bancario anual para revisión del cliente.',
  'Document status: not generated': 'Estado del documento: no generado',
  'Mock banking records': 'Registros bancarios simulados',
  'The button is disabled because no real bank statement is opened or generated in this prototype.':
    'El botón está deshabilitado porque este prototipo no abre ni genera ningún extracto bancario real.',
  'Card monthly statement': 'Extracto mensual de tarjeta',
  'Monthly card statement placeholder for a simulated Aurora Bank card.':
    'Marcador de extracto mensual para una tarjeta simulada de Aurora Bank.',
  'Card transaction summary': 'Resumen de transacciones de tarjeta',
  'Summary row for card activity in the local demo only.':
    'Fila de resumen para actividad de tarjeta solo en la demo local.',
  'Currency conversion notice': 'Aviso de conversión de moneda',
  'Notice concept for card purchases in another currency.':
    'Concepto de aviso para compras con tarjeta en otra moneda.',
  'No conversion is calculated': 'No se calcula ninguna conversión',
  'Card security notice': 'Aviso de seguridad de tarjeta',
  'Security information placeholder for safe card usage.':
    'Marcador de información de seguridad para uso seguro de tarjeta.',
  'No PDF, card account record, card statement, or card transaction file is opened in this prototype.':
    'Este prototipo no abre ningún PDF, registro de cuenta de tarjeta, extracto de tarjeta ni archivo de transacciones de tarjeta.',
  'Annual tax summary': 'Resumen fiscal anual',
  'Yearly tax summary placeholder for the local prototype.':
    'Marcador de resumen fiscal anual para el prototipo local.',
  'Tax year: 2026': 'Ejercicio fiscal: 2026',
  'Digital asset tax report concept':
    'Concepto de informe fiscal de activos digitales',
  'Concept report for digital asset activity and reporting traceability.':
    'Concepto de informe para actividad de activos digitales y trazabilidad de reporting.',
  'No official filing data': 'Sin datos oficiales de presentación',
  'Investment tax report concept':
    'Concepto de informe fiscal de inversiones',
  'Traditional investment reporting placeholder kept separate from digital assets.':
    'Marcador de reporting de inversiones tradicionales separado de activos digitales.',
  'No investment advice': 'Sin asesoría de inversión',
  'Downloadable report placeholders': 'Marcadores de informes descargables',
  'Static labels for PDF, CSV, and JSON report formats.':
    'Etiquetas estáticas para formatos de informe PDF, CSV y JSON.',
  'No file is created': 'No se crea ningún archivo',
  'The action is disabled because no real tax report, tax filing, or tax advice is generated.':
    'La acción está deshabilitada porque no se genera ningún informe fiscal, declaración fiscal ni asesoría fiscal real.',
  'Export account documents': 'Exportar documentos de cuenta',
  'Account document export placeholder for PDF format.':
    'Marcador de exportación de documentos de cuenta en formato PDF.',
  'Format: PDF': 'Formato: PDF',
  'Export payment receipts': 'Exportar recibos de pago',
  'Payment receipt bundle placeholder for banking records.':
    'Marcador de paquete de recibos de pago para registros bancarios.',
  'Export digital asset audit trail':
    'Exportar trazabilidad de auditoría de activos digitales',
  'Digital asset audit trail placeholder for CSV and JSON records.':
    'Marcador de trazabilidad de auditoría de activos digitales para registros CSV y JSON.',
  'Formats: CSV, JSON': 'Formatos: CSV, JSON',
  'Export compliance evidence package':
    'Exportar paquete de evidencia de cumplimiento',
  'Evidence package export concept for controlled review workflows.':
    'Concepto de exportación de paquete de evidencia para flujos de revisión controlados.',
  'Formats: PDF, JSON': 'Formatos: PDF, JSON',
  'No real document, archive, bank statement, evidence package, CSV, JSON, or PDF is generated.':
    'No se genera ningún documento real, archivo, extracto bancario, paquete de evidencia, CSV, JSON ni PDF.',
  'Risk decision recorded': 'Decisión de riesgo registrada',
  'Risk operation decision row for a simulated digital asset workflow.':
    'Fila de decisión de operaciones de riesgo para un flujo simulado de activos digitales.',
  'Correlation ID: CORR-AUDIT-001': 'ID de correlación: CORR-AUDIT-001',
  'Evidence package creation event for an internal review concept.':
    'Evento de creación de paquete de evidencia para un concepto de revisión interna.',
  'Package ID: EPK-DEMO-001': 'ID de paquete: EPK-DEMO-001',
  'Review case opened': 'Caso de revisión abierto',
  'Compliance review case placeholder opened from a simulated alert.':
    'Marcador de caso de revisión de cumplimiento abierto desde una alerta simulada.',
  'Case ID: CASE-DEMO-001': 'ID de caso: CASE-DEMO-001',
  'Sensitive approval blocked': 'Aprobación sensible bloqueada',
  'Sensitive approval control blocked a simulated high-risk action.':
    'El control de aprobación sensible bloqueó una acción simulada de alto riesgo.',
  'Guardrail: sensitive approval': 'Guardrail: aprobación sensible',
  'Human approval integrity guard event':
    'Evento de guardia de integridad de aprobación humana',
  'Integrity guard event showing reviewer control checks.':
    'Evento de guardia de integridad que muestra controles sobre el revisor.',
  'Control: human approval integrity':
    'Control: integridad de aprobación humana',
  'Agent governance event': 'Evento de gobierno de agentes',
  'Agent identity and permission event for governance traceability.':
    'Evento de identidad y permisos de agente para trazabilidad de gobierno.',
  'Control: agent governance': 'Control: gobierno de agentes',
  'Audit rows are deterministic demo records. No real operation, approval, or system event is executed.':
    'Las filas de auditoría son registros demo determinísticos. No se ejecuta ninguna operación, aprobación ni evento de sistema real.',
  'Secure message inbox': 'Bandeja de mensajes seguros',
  'Inbox container for local demo notices only.':
    'Contenedor de bandeja solo para avisos de demo local.',
  'No messages are delivered': 'No se entregan mensajes',
  'Bank notice': 'Aviso bancario',
  'General banking notice placeholder for online banking documents.':
    'Marcador de aviso bancario general para documentos de banca en línea.',
  'Compliance notification': 'Notificación de cumplimiento',
  'Compliance notification concept for review and evidence workflows.':
    'Concepto de notificación de cumplimiento para flujos de revisión y evidencia.',
  'Statement delivery notice': 'Aviso de entrega de extracto',
  'Statement delivery notification placeholder.':
    'Marcador de notificación de entrega de extracto.',
  'No document delivery': 'Sin entrega de documento',
  'No real secure message, notification, email, SMS, or customer communication is opened or sent.':
    'No se abre ni se envía ningún mensaje seguro real, notificación, correo electrónico, SMS ni comunicación con clientes.',
  'Evidence package list': 'Lista de paquetes de evidencia',
  'Evidence package placeholder for internal review and audit readiness.':
    'Marcador de paquete de evidencia para revisión interna y preparación de auditoría.',
  'Source audit event': 'Evento de auditoría fuente',
  'Audit source reference attached to a simulated evidence package.':
    'Referencia de auditoría fuente adjunta a un paquete de evidencia simulado.',
  'Audit event ID: AUD-DEMO-001': 'ID de evento de auditoría: AUD-DEMO-001',
  'Correlation ID placeholder': 'Marcador de ID de correlación',
  'Correlation identifier used to connect deterministic demo records.':
    'Identificador de correlación usado para conectar registros demo determinísticos.',
  'Correlation ID: CORR-DEMO-001': 'ID de correlación: CORR-DEMO-001',
  'Review case link placeholder': 'Marcador de enlace a caso de revisión',
  'Review case reference for compliance review navigation.':
    'Referencia de caso de revisión para navegación de revisión de cumplimiento.',
  'Closed evidence record': 'Registro de evidencia cerrado',
  'Closed evidence record concept for completed internal review.':
    'Concepto de registro de evidencia cerrado para revisión interna completada.',
  'Status: closed': 'Estado: cerrado',
  'No evidence package, archive, document, or export is generated from this page.':
    'Esta página no genera ningún paquete de evidencia, archivo, documento ni exportación.',
  'Compliance case': 'Caso de cumplimiento',
  'Compliance review case placeholder for document traceability.':
    'Marcador de caso de revisión de cumplimiento para trazabilidad documental.',
  'Case ID: COMP-DEMO-001': 'ID de caso: COMP-DEMO-001',
  'Risk operations case': 'Caso de operaciones de riesgo',
  'Risk operations record linked to simulated monitoring signals.':
    'Registro de operaciones de riesgo vinculado a señales de monitoreo simuladas.',
  'Case ID: RISK-DEMO-001': 'ID de caso: RISK-DEMO-001',
  'Financial crime monitoring case':
    'Caso de monitoreo de delito financiero',
  'Financial crime monitoring concept for alert review workflows.':
    'Concepto de monitoreo de delito financiero para flujos de revisión de alertas.',
  'Case ID: FC-DEMO-001': 'ID de caso: FC-DEMO-001',
  'Sensitive approval case': 'Caso de aprobación sensible',
  'Sensitive approval record for controlled operation review.':
    'Registro de aprobación sensible para revisión de operación controlada.',
  'Case ID: SAP-DEMO-001': 'ID de caso: SAP-DEMO-001',
  'Custodian readiness case': 'Caso de preparación de custodio',
  'Custodian readiness and operational review placeholder.':
    'Marcador de preparación de custodio y revisión operacional.',
  'Case ID: CUST-DEMO-001': 'ID de caso: CUST-DEMO-001',
  'No legal report, regulatory filing, certification, or customer record is opened or generated.':
    'No se abre ni se genera ningún informe legal, presentación regulatoria, certificación ni registro de cliente.',
  'Local deterministic prototype only. No real document, bank statement, card statement, tax report, secure message, audit trail, evidence package, compliance record, customer data, banking operation, export, or legal certification is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún documento real, extracto bancario, extracto de tarjeta, informe fiscal, mensaje seguro, trazabilidad de auditoría, paquete de evidencia, registro de cumplimiento, dato de cliente, operación bancaria, exportación ni certificación legal.',
  'Local deterministic prototype only. No real bank statements, account records, customer data, banking operation, export, or customer communication is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún extracto bancario real, registro de cuenta, dato de cliente, operación bancaria, exportación ni comunicación con clientes.',
  'Local deterministic prototype only. No real card statements, card transactions, cardholder data, banking operation, export, or customer communication is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún extracto de tarjeta real, transacción de tarjeta, dato de titular, operación bancaria, exportación ni comunicación con clientes.',
  'Local deterministic prototype only. No real tax document, tax filing, tax advice, customer data, banking operation, export, or legal certification is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún documento fiscal real, declaración fiscal, asesoría fiscal, dato de cliente, operación bancaria, exportación ni certificación legal.',
  'Local deterministic prototype only. No real export, bank statement, tax report, evidence package, customer data, banking operation, or secure message is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ninguna exportación real, extracto bancario, informe fiscal, paquete de evidencia, dato de cliente, operación bancaria ni mensaje seguro.',
  'Local deterministic prototype only. No real audit trail, customer record, approval, agent execution, banking operation, evidence package, export, or legal certification is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ninguna trazabilidad de auditoría real, registro de cliente, aprobación, ejecución de agente, operación bancaria, paquete de evidencia, exportación ni certificación legal.',
  'Local deterministic prototype only. No real secure message, bank mail, customer communication, customer data, document delivery, export, or banking operation is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún mensaje seguro real, correo bancario, comunicación con clientes, dato de cliente, entrega de documento, exportación ni operación bancaria.',
  'Local deterministic prototype only. No real evidence package, export, audit file, customer data, banking operation, or legal certification is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún paquete de evidencia real, exportación, archivo de auditoría, dato de cliente, operación bancaria ni certificación legal.',
  'Local deterministic prototype only. No real compliance record, legal report, regulatory certification, customer data, banking operation, evidence export, or secure message is created or executed.':
    'Prototipo local determinístico. No se crea ni ejecuta ningún registro de cumplimiento real, informe legal, certificación regulatoria, dato de cliente, operación bancaria, exportación de evidencia ni mensaje seguro.',
  'Checking banking session...': 'Comprobando sesión bancaria...',
}

type PaymentDemoPageTranslation = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryPanelTitle: string
  primaryPanelEyebrow: string
  fields: { label: string; value: string; note: string }[]
  secondaryPanelTitle: string
  secondaryPanelEyebrow: string
  rows: { title: string; detail: string; status: string }[]
  summaryTitle: string
  summaryItems: { label: string; value: string }[]
  actionLabel: string
  actionNote: string
  safetyTitle: string
  safetyNotice: string
}

type PaymentDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealPaymentExecution: string
  }
  pages: Record<
    | 'newPayment'
    | 'approvePayments'
    | 'internationalPayment'
    | 'recipients'
    | 'paymentLimits'
    | 'digitalAssetPayment'
    | 'supportedBusinessRecipients'
    | 'paymentAssetSettings'
    | 'eInvoiceAgreement'
    | 'recurringPayment'
    | 'paymentAgreements',
    PaymentDemoPageTranslation
  >
}

const paymentDemoEn: PaymentDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealPaymentExecution: 'No real payment execution',
  },
  pages: {
    newPayment: {
      eyebrow: 'Payments',
      title: 'New payment',
      subtitle:
        'Simulated new payment form for reviewing recipient, amount, reference, and execution date before a local prototype submission.',
      badge: 'Draft payment',
      primaryPanelEyebrow: 'Payment details',
      primaryPanelTitle: 'Simulated payment form',
      fields: [
        {
          label: 'Recipient account',
          value: 'Aurora Telecom Oyj · FI98 0000 0000 5678 90',
          note: 'Saved recipient selected for this local prototype.',
        },
        {
          label: 'Amount',
          value: '120.45 EUR',
          note: 'Visual amount field only.',
        },
        {
          label: 'Message / reference',
          value: 'Reference 80 60206 95479',
          note: 'Reference is preserved for review.',
        },
        {
          label: 'Execution date',
          value: '19.05.2026',
          note: 'No scheduling instruction is sent.',
        },
      ],
      secondaryPanelEyebrow: 'Review',
      secondaryPanelTitle: 'Payment readiness',
      rows: [
        {
          title: 'Recipient format checked',
          detail: 'IBAN-style recipient information is present.',
          status: 'Ready',
        },
        {
          title: 'Amount reviewed',
          detail: 'Amount is positive and shown in EUR.',
          status: 'Ready',
        },
        {
          title: 'Execution blocked',
          detail: 'Submit remains a simulation and creates no payment.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Review summary',
      summaryItems: [
        { label: 'Recipient', value: 'Aurora Telecom Oyj' },
        { label: 'Payment method', value: 'EUR bank transfer concept' },
        { label: 'Execution', value: 'Simulation only' },
      ],
      actionLabel: 'Submit simulation',
      actionNote: 'Button is disabled because no real payment is created.',
      safetyTitle: 'Safety note',
      safetyNotice:
        'No real payment is created. Local deterministic prototype only.',
    },
    approvePayments: {
      eyebrow: 'Payments',
      title: 'Approve payments',
      subtitle:
        'Simulated approval queue for pending payments, review-required payments, and risk-blocked payments.',
      badge: 'Approval queue',
      primaryPanelEyebrow: 'Pending payments',
      primaryPanelTitle: 'Approval queue',
      fields: [
        {
          label: 'Queue owner',
          value: 'Customer approval simulation',
          note: 'No real customer approval is requested.',
        },
        {
          label: 'Queue date',
          value: '23.06.2026',
          note: 'Static deterministic queue snapshot.',
        },
      ],
      secondaryPanelEyebrow: 'Queue items',
      secondaryPanelTitle: 'Pending payment list',
      rows: [
        {
          title: 'Aurora Telecom Oyj · 120.45 EUR',
          detail: 'Invoice payment awaiting customer approval.',
          status: 'Pending approval',
        },
        {
          title: 'Nordic Office Supplies · 870.00 EUR',
          detail: 'New recipient requires manual review.',
          status: 'Requires review',
        },
        {
          title: 'External high-risk recipient · 2,400.00 EUR',
          detail: 'Risk controls block approval in this prototype.',
          status: 'Blocked by risk',
        },
      ],
      summaryTitle: 'Available actions',
      summaryItems: [
        { label: 'Primary action', value: 'Review' },
        { label: 'Simulation action', value: 'Approve simulation' },
        { label: 'Fallback action', value: 'Reject simulation' },
      ],
      actionLabel: 'Approve simulation',
      actionNote: 'No real approval occurs.',
      safetyTitle: 'Approval boundary',
      safetyNotice:
        'This queue is deterministic demo data. No real payment approval occurs.',
    },
    internationalPayment: {
      eyebrow: 'Payments',
      title: 'International payment',
      subtitle:
        'Simulated international payment workflow with destination, recipient bank, currency, compliance screening, and fee placeholders.',
      badge: 'International workflow',
      primaryPanelEyebrow: 'International details',
      primaryPanelTitle: 'Destination and recipient bank',
      fields: [
        {
          label: 'Destination country',
          value: 'Spain',
          note: 'Country selector visual only.',
        },
        {
          label: 'Recipient bank',
          value: 'Aurora Correspondent Bank Madrid',
          note: 'Fictional recipient bank.',
        },
        {
          label: 'Currency',
          value: 'EUR',
          note: 'No FX quote is requested.',
        },
      ],
      secondaryPanelEyebrow: 'Compliance screening',
      secondaryPanelTitle: 'Screening controls',
      rows: [
        {
          title: 'Sanctions screening',
          detail: 'Recipient and bank would be screened before execution.',
          status: 'Required',
        },
        {
          title: 'Purpose of payment',
          detail: 'Payment purpose evidence is required for review.',
          status: 'Requires review',
        },
        {
          title: 'Fees and exchange information',
          detail: 'Placeholder fee and exchange information only.',
          status: 'Draft',
        },
      ],
      summaryTitle: 'International payment summary',
      summaryItems: [
        { label: 'Destination', value: 'Spain' },
        { label: 'Currency', value: 'EUR' },
        { label: 'Execution', value: 'No real international payment' },
      ],
      actionLabel: 'Review simulation',
      actionNote: 'No international payment or FX execution is performed.',
      safetyTitle: 'Safety note',
      safetyNotice:
        'No real international payment or FX execution occurs.',
    },
    recipients: {
      eyebrow: 'Payments',
      title: 'Recipients',
      subtitle:
        'Simulated saved recipients view showing trusted recipients, business recipients, and new recipients pending verification.',
      badge: 'Recipient controls',
      primaryPanelEyebrow: 'Saved recipients',
      primaryPanelTitle: 'Trusted recipient list',
      fields: [
        {
          label: 'Trusted recipient',
          value: 'Aurora Telecom Oyj',
          note: 'Verified business invoice recipient.',
        },
        {
          label: 'Business recipient',
          value: 'Nordic Office Supplies',
          note: 'Business recipient with payment history.',
        },
        {
          label: 'Pending recipient',
          value: 'New recipient pending verification',
          note: 'Sensitive operations require review.',
        },
      ],
      secondaryPanelEyebrow: 'Recipient review',
      secondaryPanelTitle: 'Verification status',
      rows: [
        {
          title: 'Aurora Telecom Oyj',
          detail: 'Trusted recipient with existing invoice reference.',
          status: 'Verified',
        },
        {
          title: 'Nordic Office Supplies',
          detail: 'Business recipient available for standard EUR payments.',
          status: 'Verified',
        },
        {
          title: 'New external recipient',
          detail: 'New recipient requires review before sensitive operations.',
          status: 'Pending review',
        },
      ],
      summaryTitle: 'Recipient summary',
      summaryItems: [
        { label: 'Trusted recipients', value: '2' },
        { label: 'Pending verification', value: '1' },
        { label: 'Sensitive operations', value: 'Review required' },
      ],
      actionLabel: 'Add recipient simulation',
      actionNote: 'No recipient is created in a real bank system.',
      safetyTitle: 'Recipient safety',
      safetyNotice:
        'New recipients require review for sensitive operations. No real recipient is created.',
    },
    paymentLimits: {
      eyebrow: 'Payments',
      title: 'Payment limits',
      subtitle:
        'Simulated payment limits for daily transfers, single payments, digital asset payment concepts, and separate withdrawal review.',
      badge: 'Limit controls',
      primaryPanelEyebrow: 'Customer limits',
      primaryPanelTitle: 'Configured payment limits',
      fields: [
        {
          label: 'Daily transfer limit',
          value: '5,000.00 EUR',
          note: 'Visual limit only.',
        },
        {
          label: 'Single payment limit',
          value: '2,500.00 EUR',
          note: 'Static deterministic value.',
        },
        {
          label: 'Digital asset payment limit',
          value: '500.00 EUR equivalent',
          note: 'Conceptual payment limit.',
        },
        {
          label: 'External withdrawal',
          value: 'Separate review required',
          note: 'Not controlled by payment limits.',
        },
      ],
      secondaryPanelEyebrow: 'Limit changes',
      secondaryPanelTitle: 'Review requirements',
      rows: [
        {
          title: 'Strong authentication',
          detail: 'Limit changes require strong authentication.',
          status: 'Required',
        },
        {
          title: 'Manual review',
          detail: 'Higher limits require review before activation.',
          status: 'Requires review',
        },
        {
          title: 'External withdrawal boundary',
          detail: 'External wallet withdrawals follow a separate review path.',
          status: 'Separate review',
        },
      ],
      summaryTitle: 'Limit summary',
      summaryItems: [
        { label: 'Daily transfer limit', value: '5,000.00 EUR' },
        { label: 'Single payment limit', value: '2,500.00 EUR' },
        { label: 'Change execution', value: 'Simulation only' },
      ],
      actionLabel: 'Request limit change simulation',
      actionNote: 'No real limit change is submitted.',
      safetyTitle: 'Limit boundary',
      safetyNotice:
        'Limit changes require strong authentication and review. No real limit is changed.',
    },
    digitalAssetPayment: {
      eyebrow: 'Digital asset payments',
      title: 'Digital asset payment',
      subtitle:
        'Simulated control screen for asset selection, supported business recipient, compliance pre-check, sensitive approval, and evidence readiness.',
      badge: 'Sensitive payment concept',
      primaryPanelEyebrow: 'Asset payment details',
      primaryPanelTitle: 'Digital asset payment controls',
      fields: [
        {
          label: 'Asset selection',
          value: 'EURD · EUR digital asset concept',
          note: 'Allowed asset for internal settlement concept.',
        },
        {
          label: 'Supported business recipient',
          value: 'Aurora Telecom Oyj',
          note: 'Recipient must be supported before payment review.',
        },
        {
          label: 'Compliance pre-check',
          value: 'Required before approval',
          note: 'Static deterministic compliance control.',
        },
      ],
      secondaryPanelEyebrow: 'Sensitive approval',
      secondaryPanelTitle: 'Control requirements',
      rows: [
        {
          title: 'Compliance pre-check',
          detail: 'Payment context is screened before approval.',
          status: 'Required',
        },
        {
          title: 'Sensitive approval requirement',
          detail: 'Human approval integrity controls apply.',
          status: 'Required',
        },
        {
          title: 'Evidence package notice',
          detail: 'Evidence can be prepared for compliance review.',
          status: 'Ready',
        },
      ],
      summaryTitle: 'Digital asset payment summary',
      summaryItems: [
        { label: 'Asset', value: 'EURD' },
        { label: 'Recipient', value: 'Aurora Telecom Oyj' },
        { label: 'Execution', value: 'No blockchain transaction' },
      ],
      actionLabel: 'Run pre-check simulation',
      actionNote: 'No custody execution or wallet transfer occurs.',
      safetyTitle: 'Execution boundary',
      safetyNotice:
        'No blockchain transaction. No custody execution. No wallet transfer.',
    },
    supportedBusinessRecipients: {
      eyebrow: 'Digital asset payments',
      title: 'Supported business recipients',
      subtitle:
        'Simulated list of merchant and business recipients with support status, asset support, and compliance status.',
      badge: 'Recipient directory',
      primaryPanelEyebrow: 'Business recipients',
      primaryPanelTitle: 'Supported recipient list',
      fields: [
        {
          label: 'Merchant',
          value: 'Aurora Telecom Oyj',
          note: 'Verified for EUR settlement concept.',
        },
        {
          label: 'Business',
          value: 'Nordic Office Supplies',
          note: 'Pending digital asset payment review.',
        },
        {
          label: 'Restricted recipient',
          value: 'External High-Risk Services Ltd',
          note: 'Restricted in this prototype.',
        },
      ],
      secondaryPanelEyebrow: 'Compliance status',
      secondaryPanelTitle: 'Recipient eligibility',
      rows: [
        {
          title: 'Aurora Telecom Oyj',
          detail: 'EUR settlement and digital asset payment concept supported.',
          status: 'Verified',
        },
        {
          title: 'Nordic Office Supplies',
          detail: 'EUR settlement supported; digital asset concept pending.',
          status: 'Pending review',
        },
        {
          title: 'External High-Risk Services Ltd',
          detail: 'Restricted by deterministic compliance status.',
          status: 'Restricted',
        },
      ],
      summaryTitle: 'Support summary',
      summaryItems: [
        { label: 'Verified', value: '1' },
        { label: 'Pending review', value: '1' },
        { label: 'Restricted', value: '1' },
      ],
      actionLabel: 'Review recipient simulation',
      actionNote: 'No merchant or business recipient is changed.',
      safetyTitle: 'Recipient boundary',
      safetyNotice:
        'Recipient support is simulated. No real merchant enablement occurs.',
    },
    paymentAssetSettings: {
      eyebrow: 'Digital asset payments',
      title: 'Payment asset settings',
      subtitle:
        'Simulated asset settings for allowed assets, eligibility, risk level, custody boundary, and private key protection.',
      badge: 'Asset settings',
      primaryPanelEyebrow: 'Allowed assets',
      primaryPanelTitle: 'Payment asset eligibility',
      fields: [
        {
          label: 'EURD',
          value: 'Allowed for internal settlement concept',
          note: 'No real token or settlement asset exists.',
        },
        {
          label: 'USDC',
          value: 'Review required',
          note: 'External digital asset concept.',
        },
        {
          label: 'BTC',
          value: 'Restricted for payments',
          note: 'Volatility and payment suitability controls apply.',
        },
      ],
      secondaryPanelEyebrow: 'Custody boundary',
      secondaryPanelTitle: 'Asset control model',
      rows: [
        {
          title: 'Payment eligibility',
          detail: 'Eligibility is determined by simulated policy controls.',
          status: 'Required',
        },
        {
          title: 'Risk level',
          detail: 'Risk varies by asset and recipient support.',
          status: 'Medium',
        },
        {
          title: 'Private key boundary',
          detail: 'No private keys are present in the frontend.',
          status: 'No secrets',
        },
      ],
      summaryTitle: 'Settings summary',
      summaryItems: [
        { label: 'Allowed assets', value: 'EURD concept' },
        { label: 'Risk review', value: 'Required for external assets' },
        { label: 'Custody', value: 'No real custody' },
      ],
      actionLabel: 'Save settings simulation',
      actionNote: 'No real asset setting is changed.',
      safetyTitle: 'Asset boundary',
      safetyNotice:
        'No private keys. No custody execution. No real asset payment settings are changed.',
    },
    eInvoiceAgreement: {
      eyebrow: 'E-invoices and agreements',
      title: 'Create e-invoice agreement',
      subtitle:
        'Simulated e-invoice agreement creation flow with biller search, agreement reference, recurring payment option, and approval notice.',
      badge: 'Agreement draft',
      primaryPanelEyebrow: 'Agreement details',
      primaryPanelTitle: 'E-invoice agreement form',
      fields: [
        {
          label: 'Biller search',
          value: 'Aurora Energy Services',
          note: 'Fictional biller search result.',
        },
        {
          label: 'Agreement reference',
          value: 'EINV-2026-0042',
          note: 'Static agreement reference.',
        },
        {
          label: 'Recurring payment option',
          value: 'Ask before every payment',
          note: 'No automatic payment is created.',
        },
      ],
      secondaryPanelEyebrow: 'Approval notice',
      secondaryPanelTitle: 'Agreement review',
      rows: [
        {
          title: 'Biller verified',
          detail: 'Biller status is simulated as verified.',
          status: 'Verified',
        },
        {
          title: 'Customer approval',
          detail: 'Agreement would require customer approval.',
          status: 'Required',
        },
        {
          title: 'Recurring option',
          detail: 'Recurring payment option remains disabled by default.',
          status: 'Draft',
        },
      ],
      summaryTitle: 'Agreement summary',
      summaryItems: [
        { label: 'Biller', value: 'Aurora Energy Services' },
        { label: 'Reference', value: 'EINV-2026-0042' },
        { label: 'Execution', value: 'Simulation only' },
      ],
      actionLabel: 'Create agreement simulation',
      actionNote: 'No real e-invoice agreement is created.',
      safetyTitle: 'Agreement boundary',
      safetyNotice:
        'No real e-invoice agreement or payment instruction is created.',
    },
    recurringPayment: {
      eyebrow: 'E-invoices and agreements',
      title: 'Recurring payment',
      subtitle:
        'Simulated recurring payment setup with recipient, amount, frequency, start date, next execution, and review panel.',
      badge: 'Recurring draft',
      primaryPanelEyebrow: 'Recurring payment details',
      primaryPanelTitle: 'Recurring setup',
      fields: [
        {
          label: 'Recipient',
          value: 'Aurora Housing Association',
          note: 'Saved recipient for this deterministic demo.',
        },
        {
          label: 'Amount',
          value: '850.00 EUR',
          note: 'Visual amount field only.',
        },
        {
          label: 'Frequency',
          value: 'Monthly',
          note: 'No schedule is sent.',
        },
        {
          label: 'Start date',
          value: '01.07.2026',
          note: 'Static start date.',
        },
        {
          label: 'Next execution',
          value: '01.08.2026',
          note: 'Preview only.',
        },
      ],
      secondaryPanelEyebrow: 'Review panel',
      secondaryPanelTitle: 'Recurring payment controls',
      rows: [
        {
          title: 'Recipient reviewed',
          detail: 'Saved recipient is present.',
          status: 'Ready',
        },
        {
          title: 'Schedule reviewed',
          detail: 'Frequency and dates are visible for review.',
          status: 'Ready',
        },
        {
          title: 'Execution disabled',
          detail: 'No recurring payment is activated.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Recurring summary',
      summaryItems: [
        { label: 'Recipient', value: 'Aurora Housing Association' },
        { label: 'Frequency', value: 'Monthly' },
        { label: 'Execution', value: 'No real schedule' },
      ],
      actionLabel: 'Save recurring simulation',
      actionNote: 'No recurring payment is created.',
      safetyTitle: 'Recurring boundary',
      safetyNotice:
        'No real recurring payment or future execution instruction is created.',
    },
    paymentAgreements: {
      eyebrow: 'E-invoices and agreements',
      title: 'View and edit payment agreements',
      subtitle:
        'Simulated list of active agreements, e-invoice agreements, recurring payments, status, and last review.',
      badge: 'Agreement list',
      primaryPanelEyebrow: 'Payment agreements',
      primaryPanelTitle: 'Active agreements',
      fields: [
        {
          label: 'E-invoice agreement',
          value: 'Aurora Energy Services',
          note: 'Active agreement with ask-before-payment setting.',
        },
        {
          label: 'Recurring payment',
          value: 'Aurora Housing Association',
          note: 'Monthly recurring payment concept.',
        },
        {
          label: 'Agreement pending review',
          value: 'Nordic Insurance Concept',
          note: 'Pending review before activation.',
        },
      ],
      secondaryPanelEyebrow: 'Agreement status',
      secondaryPanelTitle: 'Last review',
      rows: [
        {
          title: 'Aurora Energy Services',
          detail: 'Last reviewed 12.06.2026.',
          status: 'Active',
        },
        {
          title: 'Aurora Housing Association',
          detail: 'Last reviewed 01.06.2026.',
          status: 'Active',
        },
        {
          title: 'Nordic Insurance Concept',
          detail: 'Requires customer approval before activation.',
          status: 'Pending review',
        },
      ],
      summaryTitle: 'Agreement summary',
      summaryItems: [
        { label: 'Active agreements', value: '2' },
        { label: 'Pending review', value: '1' },
        { label: 'Real execution', value: 'None' },
      ],
      actionLabel: 'Edit agreement simulation',
      actionNote: 'No agreement is changed in a real bank system.',
      safetyTitle: 'Agreement boundary',
      safetyNotice:
        'Agreement data is simulated. No real agreement is created, edited, or executed.',
    },
  },
}

const paymentDemoEs: PaymentDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealPaymentExecution: 'Sin ejecución real de pagos',
  },
  pages: {
    newPayment: {
      eyebrow: 'Pagos',
      title: 'Nuevo pago',
      subtitle:
        'Formulario simulado de nuevo pago para revisar destinatario, importe, referencia y fecha de ejecución antes de una presentación local del prototipo.',
      badge: 'Pago en borrador',
      primaryPanelEyebrow: 'Detalles del pago',
      primaryPanelTitle: 'Formulario de pago simulado',
      fields: [
        {
          label: 'Cuenta destinataria',
          value: 'Aurora Telecom Oyj · FI98 0000 0000 5678 90',
          note: 'Destinatario guardado seleccionado para este prototipo local.',
        },
        {
          label: 'Importe',
          value: '120,45 EUR',
          note: 'Campo de importe solo visual.',
        },
        {
          label: 'Mensaje / referencia',
          value: 'Referencia 80 60206 95479',
          note: 'La referencia se conserva para revisión.',
        },
        {
          label: 'Fecha de ejecución',
          value: '19.05.2026',
          note: 'No se envía ninguna instrucción de programación.',
        },
      ],
      secondaryPanelEyebrow: 'Revisión',
      secondaryPanelTitle: 'Preparación del pago',
      rows: [
        {
          title: 'Formato de destinatario comprobado',
          detail: 'La información del destinatario con formato IBAN está presente.',
          status: 'Listo',
        },
        {
          title: 'Importe revisado',
          detail: 'El importe es positivo y se muestra en EUR.',
          status: 'Listo',
        },
        {
          title: 'Ejecución bloqueada',
          detail: 'El envío sigue siendo una simulación y no crea ningún pago.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de revisión',
      summaryItems: [
        { label: 'Destinatario', value: 'Aurora Telecom Oyj' },
        { label: 'Método de pago', value: 'Concepto de transferencia bancaria EUR' },
        { label: 'Ejecución', value: 'Solo simulación' },
      ],
      actionLabel: 'Enviar simulación',
      actionNote: 'El botón está deshabilitado porque no se crea ningún pago real.',
      safetyTitle: 'Nota de seguridad',
      safetyNotice:
        'No se crea ningún pago real. Solo prototipo local determinístico.',
    },
    approvePayments: {
      eyebrow: 'Pagos',
      title: 'Aprobar pagos',
      subtitle:
        'Cola de aprobación simulada para pagos pendientes, pagos que requieren revisión y pagos bloqueados por riesgo.',
      badge: 'Cola de aprobación',
      primaryPanelEyebrow: 'Pagos pendientes',
      primaryPanelTitle: 'Cola de aprobación',
      fields: [
        {
          label: 'Responsable de cola',
          value: 'Simulación de aprobación del cliente',
          note: 'No se solicita aprobación real del cliente.',
        },
        {
          label: 'Fecha de cola',
          value: '23.06.2026',
          note: 'Instantánea estática determinística de la cola.',
        },
      ],
      secondaryPanelEyebrow: 'Elementos de la cola',
      secondaryPanelTitle: 'Lista de pagos pendientes',
      rows: [
        {
          title: 'Aurora Telecom Oyj · 120,45 EUR',
          detail: 'Pago de factura pendiente de aprobación del cliente.',
          status: 'Pendiente de aprobación',
        },
        {
          title: 'Nordic Office Supplies · 870,00 EUR',
          detail: 'El nuevo destinatario requiere revisión manual.',
          status: 'Requiere revisión',
        },
        {
          title: 'Destinatario externo de alto riesgo · 2.400,00 EUR',
          detail: 'Los controles de riesgo bloquean la aprobación en este prototipo.',
          status: 'Bloqueado por riesgo',
        },
      ],
      summaryTitle: 'Acciones disponibles',
      summaryItems: [
        { label: 'Acción principal', value: 'Revisar' },
        { label: 'Acción simulada', value: 'Aprobar simulación' },
        { label: 'Acción alternativa', value: 'Rechazar simulación' },
      ],
      actionLabel: 'Aprobar simulación',
      actionNote: 'No se produce ninguna aprobación real.',
      safetyTitle: 'Límite de aprobación',
      safetyNotice:
        'Esta cola contiene datos demo determinísticos. No se produce ninguna aprobación real de pagos.',
    },
    internationalPayment: {
      eyebrow: 'Pagos',
      title: 'Pago internacional',
      subtitle:
        'Flujo simulado de pago internacional con destino, banco destinatario, moneda, revisión de cumplimiento y marcadores de comisiones.',
      badge: 'Flujo internacional',
      primaryPanelEyebrow: 'Detalles internacionales',
      primaryPanelTitle: 'Destino y banco destinatario',
      fields: [
        {
          label: 'País de destino',
          value: 'España',
          note: 'Selector de país solo visual.',
        },
        {
          label: 'Banco destinatario',
          value: 'Aurora Correspondent Bank Madrid',
          note: 'Banco destinatario ficticio.',
        },
        {
          label: 'Moneda',
          value: 'EUR',
          note: 'No se solicita cotización de divisa.',
        },
      ],
      secondaryPanelEyebrow: 'Revisión de cumplimiento',
      secondaryPanelTitle: 'Controles de revisión',
      rows: [
        {
          title: 'Revisión de sanciones',
          detail: 'El destinatario y el banco se revisarían antes de la ejecución.',
          status: 'Requerido',
        },
        {
          title: 'Finalidad del pago',
          detail: 'Se requiere evidencia de finalidad del pago para revisión.',
          status: 'Requiere revisión',
        },
        {
          title: 'Información de comisiones y cambio',
          detail: 'Información de comisiones y cambio solo como marcador.',
          status: 'Borrador',
        },
      ],
      summaryTitle: 'Resumen del pago internacional',
      summaryItems: [
        { label: 'Destino', value: 'España' },
        { label: 'Moneda', value: 'EUR' },
        { label: 'Ejecución', value: 'Sin pago internacional real' },
      ],
      actionLabel: 'Revisar simulación',
      actionNote: 'No se realiza ningún pago internacional ni ejecución FX.',
      safetyTitle: 'Nota de seguridad',
      safetyNotice:
        'No se produce ningún pago internacional real ni ejecución FX.',
    },
    recipients: {
      eyebrow: 'Pagos',
      title: 'Destinatarios',
      subtitle:
        'Vista simulada de destinatarios guardados con destinatarios de confianza, destinatarios comerciales y nuevos destinatarios pendientes de verificación.',
      badge: 'Controles de destinatarios',
      primaryPanelEyebrow: 'Destinatarios guardados',
      primaryPanelTitle: 'Lista de destinatarios de confianza',
      fields: [
        {
          label: 'Destinatario de confianza',
          value: 'Aurora Telecom Oyj',
          note: 'Destinatario comercial verificado para facturas.',
        },
        {
          label: 'Destinatario comercial',
          value: 'Nordic Office Supplies',
          note: 'Destinatario comercial con historial de pagos.',
        },
        {
          label: 'Destinatario pendiente',
          value: 'Nuevo destinatario pendiente de verificación',
          note: 'Las operaciones sensibles requieren revisión.',
        },
      ],
      secondaryPanelEyebrow: 'Revisión de destinatario',
      secondaryPanelTitle: 'Estado de verificación',
      rows: [
        {
          title: 'Aurora Telecom Oyj',
          detail: 'Destinatario de confianza con referencia de factura existente.',
          status: 'Verificado',
        },
        {
          title: 'Nordic Office Supplies',
          detail: 'Destinatario comercial disponible para pagos EUR estándar.',
          status: 'Verificado',
        },
        {
          title: 'Nuevo destinatario externo',
          detail: 'El nuevo destinatario requiere revisión antes de operaciones sensibles.',
          status: 'Pendiente de revisión',
        },
      ],
      summaryTitle: 'Resumen de destinatarios',
      summaryItems: [
        { label: 'Destinatarios de confianza', value: '2' },
        { label: 'Pendientes de verificación', value: '1' },
        { label: 'Operaciones sensibles', value: 'Revisión requerida' },
      ],
      actionLabel: 'Añadir destinatario simulado',
      actionNote: 'No se crea ningún destinatario en un sistema bancario real.',
      safetyTitle: 'Seguridad de destinatario',
      safetyNotice:
        'Los nuevos destinatarios requieren revisión para operaciones sensibles. No se crea ningún destinatario real.',
    },
    paymentLimits: {
      eyebrow: 'Pagos',
      title: 'Límites de pago',
      subtitle:
        'Límites de pago simulados para transferencias diarias, pagos individuales, conceptos de pago con activos digitales y revisión separada de retiros.',
      badge: 'Controles de límites',
      primaryPanelEyebrow: 'Límites del cliente',
      primaryPanelTitle: 'Límites de pago configurados',
      fields: [
        {
          label: 'Límite diario de transferencias',
          value: '5.000,00 EUR',
          note: 'Límite solo visual.',
        },
        {
          label: 'Límite por pago individual',
          value: '2.500,00 EUR',
          note: 'Valor estático determinístico.',
        },
        {
          label: 'Límite de pago con activos digitales',
          value: '500,00 EUR equivalente',
          note: 'Límite conceptual de pago.',
        },
        {
          label: 'Retiro externo',
          value: 'Requiere revisión separada',
          note: 'No se controla mediante límites de pago.',
        },
      ],
      secondaryPanelEyebrow: 'Cambios de límite',
      secondaryPanelTitle: 'Requisitos de revisión',
      rows: [
        {
          title: 'Autenticación fuerte',
          detail: 'Los cambios de límite requieren autenticación fuerte.',
          status: 'Requerido',
        },
        {
          title: 'Revisión manual',
          detail: 'Los límites superiores requieren revisión antes de activarse.',
          status: 'Requiere revisión',
        },
        {
          title: 'Límite de retiro externo',
          detail: 'Los retiros a billetera externa siguen una ruta de revisión separada.',
          status: 'Revisión separada',
        },
      ],
      summaryTitle: 'Resumen de límites',
      summaryItems: [
        { label: 'Límite diario', value: '5.000,00 EUR' },
        { label: 'Límite individual', value: '2.500,00 EUR' },
        { label: 'Ejecución del cambio', value: 'Solo simulación' },
      ],
      actionLabel: 'Solicitar cambio de límite simulado',
      actionNote: 'No se envía ningún cambio real de límite.',
      safetyTitle: 'Límite operativo',
      safetyNotice:
        'Los cambios de límite requieren autenticación fuerte y revisión. No se cambia ningún límite real.',
    },
    digitalAssetPayment: {
      eyebrow: 'Pagos con activos digitales',
      title: 'Pago con activos digitales',
      subtitle:
        'Pantalla de control simulada para selección de activo, destinatario comercial admitido, comprobación previa de cumplimiento, aprobación sensible y preparación de evidencia.',
      badge: 'Concepto de pago sensible',
      primaryPanelEyebrow: 'Detalles de pago con activos',
      primaryPanelTitle: 'Controles de pago con activos digitales',
      fields: [
        {
          label: 'Selección de activo',
          value: 'EURD · concepto de activo digital EUR',
          note: 'Activo permitido para concepto de liquidación interna.',
        },
        {
          label: 'Destinatario comercial admitido',
          value: 'Aurora Telecom Oyj',
          note: 'El destinatario debe estar admitido antes de revisar el pago.',
        },
        {
          label: 'Comprobación previa de cumplimiento',
          value: 'Requerida antes de la aprobación',
          note: 'Control estático determinístico de cumplimiento.',
        },
      ],
      secondaryPanelEyebrow: 'Aprobación sensible',
      secondaryPanelTitle: 'Requisitos de control',
      rows: [
        {
          title: 'Comprobación previa de cumplimiento',
          detail: 'El contexto del pago se revisa antes de la aprobación.',
          status: 'Requerido',
        },
        {
          title: 'Requisito de aprobación sensible',
          detail: 'Aplican controles de integridad de aprobación humana.',
          status: 'Requerido',
        },
        {
          title: 'Aviso de paquete de evidencia',
          detail: 'La evidencia puede prepararse para revisión de cumplimiento.',
          status: 'Listo',
        },
      ],
      summaryTitle: 'Resumen del pago con activos digitales',
      summaryItems: [
        { label: 'Activo', value: 'EURD' },
        { label: 'Destinatario', value: 'Aurora Telecom Oyj' },
        { label: 'Ejecución', value: 'Sin transacción blockchain' },
      ],
      actionLabel: 'Ejecutar comprobación simulada',
      actionNote: 'No ocurre custodia ni transferencia de billetera.',
      safetyTitle: 'Límite de ejecución',
      safetyNotice:
        'Sin transacción blockchain. Sin ejecución de custodia. Sin transferencia de billetera.',
    },
    supportedBusinessRecipients: {
      eyebrow: 'Pagos con activos digitales',
      title: 'Destinatarios comerciales admitidos',
      subtitle:
        'Lista simulada de comercios y destinatarios comerciales con estado de soporte, activos admitidos y estado de cumplimiento.',
      badge: 'Directorio de destinatarios',
      primaryPanelEyebrow: 'Destinatarios comerciales',
      primaryPanelTitle: 'Lista de destinatarios admitidos',
      fields: [
        {
          label: 'Comercio',
          value: 'Aurora Telecom Oyj',
          note: 'Verificado para concepto de liquidación EUR.',
        },
        {
          label: 'Empresa',
          value: 'Nordic Office Supplies',
          note: 'Pago con activos digitales pendiente de revisión.',
        },
        {
          label: 'Destinatario restringido',
          value: 'External High-Risk Services Ltd',
          note: 'Restringido en este prototipo.',
        },
      ],
      secondaryPanelEyebrow: 'Estado de cumplimiento',
      secondaryPanelTitle: 'Elegibilidad del destinatario',
      rows: [
        {
          title: 'Aurora Telecom Oyj',
          detail: 'Liquidación EUR y concepto de pago con activos digitales admitidos.',
          status: 'Verificado',
        },
        {
          title: 'Nordic Office Supplies',
          detail: 'Liquidación EUR admitida; concepto de activos digitales pendiente.',
          status: 'Pendiente de revisión',
        },
        {
          title: 'External High-Risk Services Ltd',
          detail: 'Restringido por estado determinístico de cumplimiento.',
          status: 'Restringido',
        },
      ],
      summaryTitle: 'Resumen de soporte',
      summaryItems: [
        { label: 'Verificado', value: '1' },
        { label: 'Pendiente de revisión', value: '1' },
        { label: 'Restringido', value: '1' },
      ],
      actionLabel: 'Revisar destinatario simulado',
      actionNote: 'No se modifica ningún comercio ni destinatario comercial.',
      safetyTitle: 'Límite de destinatario',
      safetyNotice:
        'El soporte de destinatarios es simulado. No se habilita ningún comercio real.',
    },
    paymentAssetSettings: {
      eyebrow: 'Pagos con activos digitales',
      title: 'Configuración de activos de pago',
      subtitle:
        'Configuración simulada de activos permitidos, elegibilidad de pago, nivel de riesgo, límite de custodia y protección de llaves privadas.',
      badge: 'Configuración de activos',
      primaryPanelEyebrow: 'Activos permitidos',
      primaryPanelTitle: 'Elegibilidad de activos de pago',
      fields: [
        {
          label: 'EURD',
          value: 'Permitido para concepto de liquidación interna',
          note: 'No existe token ni activo de liquidación real.',
        },
        {
          label: 'USDC',
          value: 'Revisión requerida',
          note: 'Concepto de activo digital externo.',
        },
        {
          label: 'BTC',
          value: 'Restringido para pagos',
          note: 'Aplican controles de volatilidad e idoneidad de pago.',
        },
      ],
      secondaryPanelEyebrow: 'Límite de custodia',
      secondaryPanelTitle: 'Modelo de control de activos',
      rows: [
        {
          title: 'Elegibilidad de pago',
          detail: 'La elegibilidad se determina mediante controles de política simulados.',
          status: 'Requerido',
        },
        {
          title: 'Nivel de riesgo',
          detail: 'El riesgo varía por activo y soporte del destinatario.',
          status: 'Medio',
        },
        {
          title: 'Límite de llave privada',
          detail: 'No hay llaves privadas en el frontend.',
          status: 'Sin secretos',
        },
      ],
      summaryTitle: 'Resumen de configuración',
      summaryItems: [
        { label: 'Activos permitidos', value: 'Concepto EURD' },
        { label: 'Revisión de riesgo', value: 'Requerida para activos externos' },
        { label: 'Custodia', value: 'Sin custodia real' },
      ],
      actionLabel: 'Guardar configuración simulada',
      actionNote: 'No se cambia ninguna configuración real de activos.',
      safetyTitle: 'Límite de activos',
      safetyNotice:
        'Sin llaves privadas. Sin ejecución de custodia. No se cambia ninguna configuración real de pago con activos.',
    },
    eInvoiceAgreement: {
      eyebrow: 'Facturas electrónicas y acuerdos',
      title: 'Crear acuerdo de factura electrónica',
      subtitle:
        'Flujo simulado de creación de acuerdo de factura electrónica con búsqueda de facturador, referencia de acuerdo, opción de pago recurrente y aviso de aprobación.',
      badge: 'Borrador de acuerdo',
      primaryPanelEyebrow: 'Detalles del acuerdo',
      primaryPanelTitle: 'Formulario de acuerdo de factura electrónica',
      fields: [
        {
          label: 'Búsqueda de facturador',
          value: 'Aurora Energy Services',
          note: 'Resultado ficticio de búsqueda de facturador.',
        },
        {
          label: 'Referencia del acuerdo',
          value: 'EINV-2026-0042',
          note: 'Referencia estática del acuerdo.',
        },
        {
          label: 'Opción de pago recurrente',
          value: 'Preguntar antes de cada pago',
          note: 'No se crea ningún pago automático.',
        },
      ],
      secondaryPanelEyebrow: 'Aviso de aprobación',
      secondaryPanelTitle: 'Revisión del acuerdo',
      rows: [
        {
          title: 'Facturador verificado',
          detail: 'El estado del facturador se simula como verificado.',
          status: 'Verificado',
        },
        {
          title: 'Aprobación del cliente',
          detail: 'El acuerdo requeriría aprobación del cliente.',
          status: 'Requerido',
        },
        {
          title: 'Opción recurrente',
          detail: 'La opción de pago recurrente permanece deshabilitada por defecto.',
          status: 'Borrador',
        },
      ],
      summaryTitle: 'Resumen del acuerdo',
      summaryItems: [
        { label: 'Facturador', value: 'Aurora Energy Services' },
        { label: 'Referencia', value: 'EINV-2026-0042' },
        { label: 'Ejecución', value: 'Solo simulación' },
      ],
      actionLabel: 'Crear acuerdo simulado',
      actionNote: 'No se crea ningún acuerdo real de factura electrónica.',
      safetyTitle: 'Límite del acuerdo',
      safetyNotice:
        'No se crea ningún acuerdo real de factura electrónica ni instrucción de pago.',
    },
    recurringPayment: {
      eyebrow: 'Facturas electrónicas y acuerdos',
      title: 'Pago recurrente',
      subtitle:
        'Configuración simulada de pago recurrente con destinatario, importe, frecuencia, fecha de inicio, próxima ejecución y panel de revisión.',
      badge: 'Borrador recurrente',
      primaryPanelEyebrow: 'Detalles de pago recurrente',
      primaryPanelTitle: 'Configuración recurrente',
      fields: [
        {
          label: 'Destinatario',
          value: 'Aurora Housing Association',
          note: 'Destinatario guardado para esta demo determinística.',
        },
        {
          label: 'Importe',
          value: '850,00 EUR',
          note: 'Campo de importe solo visual.',
        },
        {
          label: 'Frecuencia',
          value: 'Mensual',
          note: 'No se envía ninguna programación.',
        },
        {
          label: 'Fecha de inicio',
          value: '01.07.2026',
          note: 'Fecha de inicio estática.',
        },
        {
          label: 'Próxima ejecución',
          value: '01.08.2026',
          note: 'Solo vista previa.',
        },
      ],
      secondaryPanelEyebrow: 'Panel de revisión',
      secondaryPanelTitle: 'Controles de pago recurrente',
      rows: [
        {
          title: 'Destinatario revisado',
          detail: 'El destinatario guardado está presente.',
          status: 'Listo',
        },
        {
          title: 'Programación revisada',
          detail: 'La frecuencia y las fechas están visibles para revisión.',
          status: 'Listo',
        },
        {
          title: 'Ejecución deshabilitada',
          detail: 'No se activa ningún pago recurrente.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen recurrente',
      summaryItems: [
        { label: 'Destinatario', value: 'Aurora Housing Association' },
        { label: 'Frecuencia', value: 'Mensual' },
        { label: 'Ejecución', value: 'Sin programación real' },
      ],
      actionLabel: 'Guardar pago recurrente simulado',
      actionNote: 'No se crea ningún pago recurrente.',
      safetyTitle: 'Límite recurrente',
      safetyNotice:
        'No se crea ningún pago recurrente real ni instrucción de ejecución futura.',
    },
    paymentAgreements: {
      eyebrow: 'Facturas electrónicas y acuerdos',
      title: 'Ver y editar acuerdos de pago',
      subtitle:
        'Lista simulada de acuerdos activos, acuerdos de factura electrónica, pagos recurrentes, estado y última revisión.',
      badge: 'Lista de acuerdos',
      primaryPanelEyebrow: 'Acuerdos de pago',
      primaryPanelTitle: 'Acuerdos activos',
      fields: [
        {
          label: 'Acuerdo de factura electrónica',
          value: 'Aurora Energy Services',
          note: 'Acuerdo activo con ajuste de preguntar antes de pagar.',
        },
        {
          label: 'Pago recurrente',
          value: 'Aurora Housing Association',
          note: 'Concepto de pago recurrente mensual.',
        },
        {
          label: 'Acuerdo pendiente de revisión',
          value: 'Nordic Insurance Concept',
          note: 'Pendiente de revisión antes de activación.',
        },
      ],
      secondaryPanelEyebrow: 'Estado de acuerdos',
      secondaryPanelTitle: 'Última revisión',
      rows: [
        {
          title: 'Aurora Energy Services',
          detail: 'Última revisión 12.06.2026.',
          status: 'Activo',
        },
        {
          title: 'Aurora Housing Association',
          detail: 'Última revisión 01.06.2026.',
          status: 'Activo',
        },
        {
          title: 'Nordic Insurance Concept',
          detail: 'Requiere aprobación del cliente antes de activación.',
          status: 'Pendiente de revisión',
        },
      ],
      summaryTitle: 'Resumen de acuerdos',
      summaryItems: [
        { label: 'Acuerdos activos', value: '2' },
        { label: 'Pendiente de revisión', value: '1' },
        { label: 'Ejecución real', value: 'Ninguna' },
      ],
      actionLabel: 'Editar acuerdo simulado',
      actionNote: 'No se cambia ningún acuerdo en un sistema bancario real.',
      safetyTitle: 'Límite del acuerdo',
      safetyNotice:
        'Los datos de acuerdos son simulados. No se crea, edita ni ejecuta ningún acuerdo real.',
    },
  },
}

type AccountDemoPageTranslation = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryPanelTitle: string
  primaryPanelEyebrow: string
  items: { label: string; value: string; note: string }[]
  secondaryPanelTitle: string
  secondaryPanelEyebrow: string
  rows: { title: string; detail: string; status: string }[]
  summaryTitle: string
  summaryItems: { label: string; value: string }[]
  actionLabel: string
  actionNote: string
  safetyTitle: string
  safetyNotice: string
}

type AccountDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealAccountOperation: string
  }
  pages: Record<
    | 'balances'
    | 'transactions'
    | 'currentAccount'
    | 'savingsDeposits'
    | 'childAccount'
    | 'accountFaq',
    AccountDemoPageTranslation
  >
}

const accountDemoEn: AccountDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealAccountOperation: 'No real account operation',
  },
  pages: {
    balances: {
      eyebrow: 'Accounts',
      title: 'Balances',
      subtitle:
        'Simulated balances overview for current account, savings account, reserved funds, available balance, and account status.',
      badge: 'Simulated balances',
      primaryPanelEyebrow: 'Balance overview',
      primaryPanelTitle: 'Account balances',
      items: [
        {
          label: 'Current account balance',
          value: '4,250.80 EUR',
          note: 'Static current account balance.',
        },
        {
          label: 'Savings account balance',
          value: '12,400.00 EUR',
          note: 'Static savings balance.',
        },
        {
          label: 'Reserved funds',
          value: '325.40 EUR',
          note: 'Reserved card payments and pending items.',
        },
        {
          label: 'Available balance',
          value: '3,925.40 EUR',
          note: 'Available balance after simulated reservations.',
        },
      ],
      secondaryPanelEyebrow: 'Account status',
      secondaryPanelTitle: 'Status controls',
      rows: [
        {
          title: 'Current account',
          detail: 'Primary account is active in this deterministic demo.',
          status: 'Active',
        },
        {
          title: 'Savings account',
          detail: 'Savings account is visible but not connected to a real core banking system.',
          status: 'Active',
        },
        {
          title: 'Reserved funds',
          detail: 'Reserved funds are shown for UI review only.',
          status: 'Simulated',
        },
      ],
      summaryTitle: 'Balance summary',
      summaryItems: [
        { label: 'Available balance', value: '3,925.40 EUR' },
        { label: 'Reserved funds', value: '325.40 EUR' },
        { label: 'Real account data', value: 'None' },
      ],
      actionLabel: 'Refresh simulation',
      actionNote: 'No real balance refresh or account query is performed.',
      safetyTitle: 'Balance boundary',
      safetyNotice:
        'Local deterministic prototype only. Simulated balances only, no real account data, no personal data, no payment, deposit, or banking operation.',
    },
    transactions: {
      eyebrow: 'Accounts',
      title: 'Transactions',
      subtitle:
        'Simulated transaction history with visual filters for date range, account, and transaction type.',
      badge: 'Transaction history',
      primaryPanelEyebrow: 'Filters',
      primaryPanelTitle: 'Transaction filters',
      items: [
        {
          label: 'Date range',
          value: '01.06.2026 - 23.06.2026',
          note: 'Visual date range only.',
        },
        {
          label: 'Account',
          value: 'Aurora Current Account',
          note: 'Static account selector.',
        },
        {
          label: 'Type',
          value: 'All transaction types',
          note: 'No query is submitted.',
        },
      ],
      secondaryPanelEyebrow: 'Transaction list',
      secondaryPanelTitle: 'Recent transactions',
      rows: [
        {
          title: '12.06.2026 · Salary payment',
          detail: '+3,240.00 EUR · Completed',
          status: 'Completed',
        },
        {
          title: '14.06.2026 · Card reservation',
          detail: '-86.40 EUR · Reserved funds',
          status: 'Reserved',
        },
        {
          title: '18.06.2026 · New recipient transfer',
          detail: '-940.00 EUR · Blocked for review',
          status: 'Blocked by review',
        },
      ],
      summaryTitle: 'Transaction summary',
      summaryItems: [
        { label: 'Completed', value: '1' },
        { label: 'Reserved', value: '1' },
        { label: 'Blocked/review', value: '1' },
      ],
      actionLabel: 'Export simulation',
      actionNote: 'No real transaction export is generated.',
      safetyTitle: 'Transaction boundary',
      safetyNotice:
        'Local deterministic prototype only. No real transactions, account data, personal data, payment, deposit, or banking operation.',
    },
    currentAccount: {
      eyebrow: 'Accounts',
      title: 'Current account',
      subtitle:
        'Simulated current account information with account features, monthly fee placeholder, eligibility checklist, and onboarding review.',
      badge: 'Opening simulation',
      primaryPanelEyebrow: 'Account features',
      primaryPanelTitle: 'Current account information',
      items: [
        {
          label: 'Everyday banking',
          value: 'Payments, cards, and account statements',
          note: 'Feature overview only.',
        },
        {
          label: 'Monthly fee',
          value: 'Placeholder fee information',
          note: 'No price or fee quote is issued.',
        },
        {
          label: 'Online banking access',
          value: 'Strong authentication required',
          note: 'Prototype access model only.',
        },
      ],
      secondaryPanelEyebrow: 'Eligibility checklist',
      secondaryPanelTitle: 'Onboarding review',
      rows: [
        {
          title: 'Identity verification',
          detail: 'Identity would be verified by the bank before account opening.',
          status: 'Required',
        },
        {
          title: 'Customer relationship review',
          detail: 'Formal onboarding review is required.',
          status: 'Required',
        },
        {
          title: 'Account opening execution',
          detail: 'Account opening is disabled in this prototype.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Opening summary',
      summaryItems: [
        { label: 'Account type', value: 'Current account' },
        { label: 'Onboarding', value: 'Review required' },
        { label: 'Real opening', value: 'None' },
      ],
      actionLabel: 'Open account simulation',
      actionNote: 'Button is disabled because no real account is opened.',
      safetyTitle: 'Opening boundary',
      safetyNotice:
        'Local deterministic prototype only. No real account is opened and no real account, transaction, personal data, payment, deposit, or banking operation is created or executed.',
    },
    savingsDeposits: {
      eyebrow: 'Accounts',
      title: 'Savings and deposit accounts',
      subtitle:
        'Simulated savings and deposit account information with interest placeholders, risk notes, and availability notes.',
      badge: 'Deposit concept',
      primaryPanelEyebrow: 'Savings products',
      primaryPanelTitle: 'Savings and deposit options',
      items: [
        {
          label: 'Savings account',
          value: 'Flexible savings concept',
          note: 'No product is created.',
        },
        {
          label: 'Fixed-term deposit',
          value: 'Fixed availability concept',
          note: 'No deposit contract is created.',
        },
        {
          label: 'Interest information',
          value: 'Placeholder interest information',
          note: 'No real rate quote is provided.',
        },
      ],
      secondaryPanelEyebrow: 'Risk and availability',
      secondaryPanelTitle: 'Deposit review',
      rows: [
        {
          title: 'Availability note',
          detail: 'Fixed-term deposits may have availability restrictions in a real product.',
          status: 'Notice',
        },
        {
          title: 'Risk note',
          detail: 'This prototype does not provide deposit advice or product terms.',
          status: 'Required',
        },
        {
          title: 'Product creation',
          detail: 'No savings or deposit product is created.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Deposit summary',
      summaryItems: [
        { label: 'Savings account', value: 'Simulated' },
        { label: 'Fixed-term deposit', value: 'Simulated' },
        { label: 'Real product', value: 'None' },
      ],
      actionLabel: 'Continue simulation',
      actionNote: 'No real deposit product is created.',
      safetyTitle: 'Deposit boundary',
      safetyNotice:
        'Local deterministic prototype only. No real deposit product, account, transaction, personal data, payment, deposit, or banking operation is created or executed.',
    },
    childAccount: {
      eyebrow: 'Accounts',
      title: 'Account for a child',
      subtitle:
        'Simulated child account information with guardian approval, identity verification placeholder, spending limits, and card/payment restrictions.',
      badge: 'Guardian review',
      primaryPanelEyebrow: 'Child account controls',
      primaryPanelTitle: 'Guardian and restriction model',
      items: [
        {
          label: 'Guardian approval',
          value: 'Required before account setup',
          note: 'No approval is requested.',
        },
        {
          label: 'Identity verification',
          value: 'Placeholder verification',
          note: 'No identity data is collected.',
        },
        {
          label: 'Spending limits',
          value: 'Low daily spending concept',
          note: 'No limit is configured.',
        },
        {
          label: 'Card/payment restrictions',
          value: 'Restricted by default',
          note: 'Restriction model is simulated.',
        },
      ],
      secondaryPanelEyebrow: 'Protection controls',
      secondaryPanelTitle: 'Review requirements',
      rows: [
        {
          title: 'Guardian approval',
          detail: 'A real product would require guardian consent.',
          status: 'Required',
        },
        {
          title: 'Personal data boundary',
          detail: 'No child personal data is stored in this prototype.',
          status: 'No real data',
        },
        {
          title: 'Account creation',
          detail: 'No child account is opened.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Child account summary',
      summaryItems: [
        { label: 'Guardian approval', value: 'Required' },
        { label: 'Restrictions', value: 'Enabled concept' },
        { label: 'Real account', value: 'None' },
      ],
      actionLabel: 'Start simulation',
      actionNote: 'No real child account or personal data is created.',
      safetyTitle: 'Child account boundary',
      safetyNotice:
        'Local deterministic prototype only. No real child account, personal data, account, transaction, payment, deposit, or banking operation is created or executed.',
    },
    accountFaq: {
      eyebrow: 'Accounts',
      title: 'Account FAQ',
      subtitle:
        'Account FAQ covering account access, account statements, payment limits, and digital asset separation from deposits.',
      badge: 'FAQ',
      primaryPanelEyebrow: 'Common account questions',
      primaryPanelTitle: 'Account information',
      items: [
        {
          label: 'Account access',
          value: 'Access requires authenticated online banking.',
          note: 'Prototype session only.',
        },
        {
          label: 'Account statements',
          value: 'Statements are available in reports concept pages.',
          note: 'No real statement is generated.',
        },
        {
          label: 'Payment limits',
          value: 'Payment limits are simulated controls.',
          note: 'No real limit is changed.',
        },
        {
          label: 'Digital assets and deposits',
          value: 'Digital assets are separate from deposits.',
          note: 'Custody and risk boundaries are explicit.',
        },
      ],
      secondaryPanelEyebrow: 'FAQ topics',
      secondaryPanelTitle: 'Account guidance',
      rows: [
        {
          title: 'How do I access accounts?',
          detail: 'Use the simulated authenticated online banking session.',
          status: 'Information',
        },
        {
          title: 'Where are account statements?',
          detail: 'Open Reports for simulated statements and bank mail.',
          status: 'Information',
        },
        {
          title: 'Are digital assets deposits?',
          detail: 'No. Digital assets are separate from bank deposits.',
          status: 'Risk notice',
        },
      ],
      summaryTitle: 'FAQ summary',
      summaryItems: [
        { label: 'Account access', value: 'Authenticated prototype' },
        { label: 'Statements', value: 'Reports concept' },
        { label: 'Digital assets', value: 'Separate from deposits' },
      ],
      actionLabel: 'Open reports',
      actionNote: 'This is an informational prototype page.',
      safetyTitle: 'Prototype boundary',
      safetyNotice:
        'Local deterministic prototype only. No real account, transaction, personal data, payment, deposit, or banking operation is created or executed.',
    },
  },
}

const accountDemoEs: AccountDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealAccountOperation: 'Sin operación bancaria real',
  },
  pages: {
    balances: {
      eyebrow: 'Cuentas',
      title: 'Saldos',
      subtitle:
        'Resumen simulado de saldos de cuenta corriente, cuenta de ahorro, fondos reservados, saldo disponible y estado de cuenta.',
      badge: 'Saldos simulados',
      primaryPanelEyebrow: 'Resumen de saldos',
      primaryPanelTitle: 'Saldos de cuenta',
      items: [
        {
          label: 'Saldo de cuenta corriente',
          value: '4.250,80 EUR',
          note: 'Saldo estático de cuenta corriente.',
        },
        {
          label: 'Saldo de cuenta de ahorro',
          value: '12.400,00 EUR',
          note: 'Saldo estático de ahorro.',
        },
        {
          label: 'Fondos reservados',
          value: '325,40 EUR',
          note: 'Pagos con tarjeta reservados y partidas pendientes.',
        },
        {
          label: 'Saldo disponible',
          value: '3.925,40 EUR',
          note: 'Saldo disponible tras reservas simuladas.',
        },
      ],
      secondaryPanelEyebrow: 'Estado de cuenta',
      secondaryPanelTitle: 'Controles de estado',
      rows: [
        {
          title: 'Cuenta corriente',
          detail: 'La cuenta principal está activa en esta demo determinística.',
          status: 'Activo',
        },
        {
          title: 'Cuenta de ahorro',
          detail: 'La cuenta de ahorro es visible, pero no está conectada a un sistema bancario real.',
          status: 'Activo',
        },
        {
          title: 'Fondos reservados',
          detail: 'Los fondos reservados se muestran solo para revisión de interfaz.',
          status: 'Simulado',
        },
      ],
      summaryTitle: 'Resumen de saldos',
      summaryItems: [
        { label: 'Saldo disponible', value: '3.925,40 EUR' },
        { label: 'Fondos reservados', value: '325,40 EUR' },
        { label: 'Datos bancarios reales', value: 'Ninguno' },
      ],
      actionLabel: 'Actualizar simulación',
      actionNote: 'No se realiza ninguna consulta ni actualización real de saldos.',
      safetyTitle: 'Límite de saldos',
      safetyNotice:
        'Solo prototipo local determinístico. Saldos simulados, sin datos bancarios reales, sin datos personales y sin creación ni ejecución de cuenta, transacción, pago, depósito u operación bancaria.',
    },
    transactions: {
      eyebrow: 'Cuentas',
      title: 'Transacciones',
      subtitle:
        'Historial simulado de transacciones con filtros visuales de rango de fechas, cuenta y tipo de transacción.',
      badge: 'Historial de transacciones',
      primaryPanelEyebrow: 'Filtros',
      primaryPanelTitle: 'Filtros de transacciones',
      items: [
        {
          label: 'Rango de fechas',
          value: '01.06.2026 - 23.06.2026',
          note: 'Rango de fechas solo visual.',
        },
        {
          label: 'Cuenta',
          value: 'Aurora Current Account',
          note: 'Selector de cuenta estático.',
        },
        {
          label: 'Tipo',
          value: 'Todos los tipos de transacción',
          note: 'No se envía ninguna consulta.',
        },
      ],
      secondaryPanelEyebrow: 'Lista de transacciones',
      secondaryPanelTitle: 'Transacciones recientes',
      rows: [
        {
          title: '12.06.2026 · Abono de nómina',
          detail: '+3.240,00 EUR · Completada',
          status: 'Completada',
        },
        {
          title: '14.06.2026 · Reserva de tarjeta',
          detail: '-86,40 EUR · Fondos reservados',
          status: 'Reservado',
        },
        {
          title: '18.06.2026 · Transferencia a nuevo destinatario',
          detail: '-940,00 EUR · Bloqueada para revisión',
          status: 'Bloqueada por revisión',
        },
      ],
      summaryTitle: 'Resumen de transacciones',
      summaryItems: [
        { label: 'Completadas', value: '1' },
        { label: 'Reservadas', value: '1' },
        { label: 'Bloqueadas/revisión', value: '1' },
      ],
      actionLabel: 'Exportar simulación',
      actionNote: 'No se genera ninguna exportación real de transacciones.',
      safetyTitle: 'Límite de transacciones',
      safetyNotice:
        'Solo prototipo local determinístico. Sin transacciones reales, datos bancarios reales, datos personales ni creación o ejecución de cuenta, pago, depósito u operación bancaria.',
    },
    currentAccount: {
      eyebrow: 'Cuentas',
      title: 'Cuenta corriente',
      subtitle:
        'Información simulada de apertura de cuenta corriente con características, marcador de comisiones mensuales, checklist de elegibilidad y revisión de incorporación.',
      badge: 'Simulación de apertura',
      primaryPanelEyebrow: 'Características de cuenta',
      primaryPanelTitle: 'Información de cuenta corriente',
      items: [
        {
          label: 'Banca diaria',
          value: 'Pagos, tarjetas y extractos de cuenta',
          note: 'Resumen de características solamente.',
        },
        {
          label: 'Comisión mensual',
          value: 'Información de comisión como marcador',
          note: 'No se emite precio ni cotización de comisiones.',
        },
        {
          label: 'Acceso a banca en línea',
          value: 'Requiere autenticación fuerte',
          note: 'Modelo de acceso del prototipo.',
        },
      ],
      secondaryPanelEyebrow: 'Checklist de elegibilidad',
      secondaryPanelTitle: 'Revisión de incorporación',
      rows: [
        {
          title: 'Verificación de identidad',
          detail: 'El banco verificaría la identidad antes de abrir la cuenta.',
          status: 'Requerido',
        },
        {
          title: 'Revisión de relación con el cliente',
          detail: 'Se requiere revisión formal de incorporación.',
          status: 'Requerido',
        },
        {
          title: 'Ejecución de apertura de cuenta',
          detail: 'La apertura de cuenta está deshabilitada en este prototipo.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de apertura',
      summaryItems: [
        { label: 'Tipo de cuenta', value: 'Cuenta corriente' },
        { label: 'Incorporación', value: 'Revisión requerida' },
        { label: 'Apertura real', value: 'Ninguna' },
      ],
      actionLabel: 'Simular apertura de cuenta',
      actionNote: 'El botón está deshabilitado porque no se abre ninguna cuenta real.',
      safetyTitle: 'Límite de apertura',
      safetyNotice:
        'Solo prototipo local determinístico. Sin apertura real de cuentas y sin creación ni ejecución de cuenta, transacción, datos personales, pago, depósito u operación bancaria.',
    },
    savingsDeposits: {
      eyebrow: 'Cuentas',
      title: 'Cuentas de ahorro y depósito',
      subtitle:
        'Información simulada de cuentas de ahorro y depósito con marcadores de intereses, notas de riesgo y disponibilidad.',
      badge: 'Concepto de depósito',
      primaryPanelEyebrow: 'Productos de ahorro',
      primaryPanelTitle: 'Opciones de ahorro y depósito',
      items: [
        {
          label: 'Cuenta de ahorro',
          value: 'Concepto de ahorro flexible',
          note: 'No se crea ningún producto.',
        },
        {
          label: 'Depósito a plazo fijo',
          value: 'Concepto de disponibilidad fija',
          note: 'No se crea ningún contrato de depósito.',
        },
        {
          label: 'Información de intereses',
          value: 'Información de intereses como marcador',
          note: 'No se proporciona tipo de interés real.',
        },
      ],
      secondaryPanelEyebrow: 'Riesgo y disponibilidad',
      secondaryPanelTitle: 'Revisión de depósito',
      rows: [
        {
          title: 'Nota de disponibilidad',
          detail: 'Los depósitos a plazo fijo pueden tener restricciones de disponibilidad en un producto real.',
          status: 'Aviso',
        },
        {
          title: 'Nota de riesgo',
          detail: 'Este prototipo no proporciona asesoramiento ni condiciones de producto.',
          status: 'Requerido',
        },
        {
          title: 'Creación de producto',
          detail: 'No se crea ningún producto de ahorro o depósito.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de depósito',
      summaryItems: [
        { label: 'Cuenta de ahorro', value: 'Simulada' },
        { label: 'Depósito a plazo fijo', value: 'Simulado' },
        { label: 'Producto real', value: 'Ninguno' },
      ],
      actionLabel: 'Continuar simulación',
      actionNote: 'No se crea ningún producto real de depósito.',
      safetyTitle: 'Límite de depósito',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ningún producto real de depósito, cuenta, transacción, dato personal, pago ni operación bancaria.',
    },
    childAccount: {
      eyebrow: 'Cuentas',
      title: 'Cuenta para menor de edad',
      subtitle:
        'Información simulada de cuenta para menor con aprobación de tutor, marcador de verificación de identidad, límites de gasto y restricciones de tarjeta/pagos.',
      badge: 'Revisión de tutor',
      primaryPanelEyebrow: 'Controles de cuenta para menor',
      primaryPanelTitle: 'Modelo de tutor y restricciones',
      items: [
        {
          label: 'Aprobación de tutor',
          value: 'Requerida antes de configurar la cuenta',
          note: 'No se solicita ninguna aprobación.',
        },
        {
          label: 'Verificación de identidad',
          value: 'Verificación como marcador',
          note: 'No se recopilan datos de identidad.',
        },
        {
          label: 'Límites de gasto',
          value: 'Concepto de gasto diario bajo',
          note: 'No se configura ningún límite.',
        },
        {
          label: 'Restricciones de tarjeta/pagos',
          value: 'Restringido por defecto',
          note: 'El modelo de restricciones es simulado.',
        },
      ],
      secondaryPanelEyebrow: 'Controles de protección',
      secondaryPanelTitle: 'Requisitos de revisión',
      rows: [
        {
          title: 'Aprobación de tutor',
          detail: 'Un producto real requeriría consentimiento del tutor.',
          status: 'Requerido',
        },
        {
          title: 'Límite de datos personales',
          detail: 'No se almacena ningún dato personal de menores en este prototipo.',
          status: 'Sin datos reales',
        },
        {
          title: 'Creación de cuenta',
          detail: 'No se abre ninguna cuenta para menor.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de cuenta para menor',
      summaryItems: [
        { label: 'Aprobación de tutor', value: 'Requerida' },
        { label: 'Restricciones', value: 'Concepto habilitado' },
        { label: 'Cuenta real', value: 'Ninguna' },
      ],
      actionLabel: 'Iniciar simulación',
      actionNote: 'No se crea ninguna cuenta real para menor ni datos personales.',
      safetyTitle: 'Límite de cuenta para menor',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ninguna cuenta real para menor, dato personal, cuenta, transacción, pago, depósito u operación bancaria.',
    },
    accountFaq: {
      eyebrow: 'Cuentas',
      title: 'Preguntas frecuentes de cuentas',
      subtitle:
        'Preguntas frecuentes sobre acceso a cuentas, extractos, límites de pago y separación de activos digitales frente a depósitos.',
      badge: 'Preguntas frecuentes',
      primaryPanelEyebrow: 'Preguntas comunes de cuentas',
      primaryPanelTitle: 'Información de cuentas',
      items: [
        {
          label: 'Acceso a cuentas',
          value: 'El acceso requiere banca en línea autenticada.',
          note: 'Solo sesión de prototipo.',
        },
        {
          label: 'Extractos de cuenta',
          value: 'Los extractos están disponibles en páginas conceptuales de informes.',
          note: 'No se genera ningún extracto real.',
        },
        {
          label: 'Límites de pago',
          value: 'Los límites de pago son controles simulados.',
          note: 'No se cambia ningún límite real.',
        },
        {
          label: 'Activos digitales y depósitos',
          value: 'Los activos digitales están separados de los depósitos.',
          note: 'Los límites de custodia y riesgo son explícitos.',
        },
      ],
      secondaryPanelEyebrow: 'Temas de FAQ',
      secondaryPanelTitle: 'Orientación de cuentas',
      rows: [
        {
          title: '¿Cómo accedo a mis cuentas?',
          detail: 'Use la sesión simulada autenticada de banca en línea.',
          status: 'Información',
        },
        {
          title: '¿Dónde están los extractos de cuenta?',
          detail: 'Abra Informes para extractos y correo bancario simulados.',
          status: 'Información',
        },
        {
          title: '¿Los activos digitales son depósitos?',
          detail: 'No. Los activos digitales están separados de los depósitos bancarios.',
          status: 'Aviso de riesgo',
        },
      ],
      summaryTitle: 'Resumen de FAQ',
      summaryItems: [
        { label: 'Acceso a cuentas', value: 'Prototipo autenticado' },
        { label: 'Extractos', value: 'Concepto de informes' },
        { label: 'Activos digitales', value: 'Separados de depósitos' },
      ],
      actionLabel: 'Abrir informes',
      actionNote: 'Esta es una página informativa del prototipo.',
      safetyTitle: 'Límite del prototipo',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ninguna cuenta real, transacción, dato personal, pago, depósito u operación bancaria.',
    },
  },
}

type CardDemoPageTranslation = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryPanelTitle: string
  primaryPanelEyebrow: string
  items: { label: string; value: string; note: string }[]
  secondaryPanelTitle: string
  secondaryPanelEyebrow: string
  rows: { title: string; detail: string; status: string }[]
  summaryTitle: string
  summaryItems: { label: string; value: string }[]
  actionLabel: string
  actionNote: string
  safetyTitle: string
  safetyNotice: string
}

type CardDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealCardOrFxOperation: string
  }
  pages: Record<
    | 'overview'
    | 'apply'
    | 'settings'
    | 'limits'
    | 'currencyAccounts'
    | 'exchangeRates'
    | 'travelMoney'
    | 'cardFaq',
    CardDemoPageTranslation
  >
}

const cardDemoEn: CardDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealCardOrFxOperation: 'No real card or FX operation',
  },
  pages: {
    overview: {
      eyebrow: 'Cards and Currency',
      title: 'Card overview',
      subtitle:
        'Simulated card overview for debit card, credit card, card status, recent activity, and card security status.',
      badge: 'Card security active',
      primaryPanelEyebrow: 'Cards',
      primaryPanelTitle: 'Card overview',
      items: [
        {
          label: 'Debit card overview',
          value: 'Aurora Debit Online · Active',
          note: 'Fictional debit card for the local prototype.',
        },
        {
          label: 'Credit card overview',
          value: 'Aurora Gold · Review required',
          note: 'Credit card concept with no real credit facility.',
        },
        {
          label: 'Card security status',
          value: 'Online purchases monitored',
          note: 'Static security state only.',
        },
      ],
      secondaryPanelEyebrow: 'Recent simulated card activity',
      secondaryPanelTitle: 'Card activity',
      rows: [
        {
          title: '12.06.2026 · Grocery purchase',
          detail: '-42.80 EUR · Aurora Debit Online',
          status: 'Completed',
        },
        {
          title: '15.06.2026 · Online purchase attempt',
          detail: '-129.00 EUR · Step-up review required',
          status: 'Requires review',
        },
        {
          title: '18.06.2026 · Foreign card authorization',
          detail: '-76.10 EUR · Blocked by travel controls',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Card summary',
      summaryItems: [
        { label: 'Debit card', value: 'Active' },
        { label: 'Credit card', value: 'Review concept' },
        { label: 'Real transactions', value: 'None' },
      ],
      actionLabel: 'Refresh simulation',
      actionNote: 'No real card data or transaction query is performed.',
      safetyTitle: 'Card boundary',
      safetyNotice:
        'Local deterministic prototype only. No real card, card application, card transaction, currency account, FX operation, travel money order, or banking operation is created or executed.',
    },
    apply: {
      eyebrow: 'Cards and Currency',
      title: 'Apply for a card',
      subtitle:
        'Simulated card application flow with card type selection, eligibility checklist, verification placeholders, and application review status.',
      badge: 'Application draft',
      primaryPanelEyebrow: 'Application details',
      primaryPanelTitle: 'Card type selection',
      items: [
        {
          label: 'Selected card type',
          value: 'Aurora Debit Online',
          note: 'Static card type selection.',
        },
        {
          label: 'Identity verification',
          value: 'Placeholder review',
          note: 'No identity data is collected.',
        },
        {
          label: 'Income verification',
          value: 'Placeholder review',
          note: 'No income data is requested.',
        },
      ],
      secondaryPanelEyebrow: 'Eligibility checklist',
      secondaryPanelTitle: 'Application review status',
      rows: [
        {
          title: 'Customer relationship',
          detail: 'A real application would require an active bank relationship.',
          status: 'Required',
        },
        {
          title: 'Identity and income verification',
          detail: 'Verification is represented as a placeholder only.',
          status: 'Required',
        },
        {
          title: 'Application submission',
          detail: 'Submission is disabled in this prototype.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Application summary',
      summaryItems: [
        { label: 'Card type', value: 'Aurora Debit Online' },
        { label: 'Review', value: 'Required' },
        { label: 'Real application', value: 'None' },
      ],
      actionLabel: 'Submit application simulation',
      actionNote: 'Button is disabled because no real card application is submitted.',
      safetyTitle: 'Application boundary',
      safetyNotice:
        'Local deterministic prototype only. No real card application, card issuing, card transaction, currency account, FX operation, travel money order, or banking operation is created or executed.',
    },
    settings: {
      eyebrow: 'Cards and Currency',
      title: 'Card settings',
      subtitle:
        'Simulated card settings for online payments, contactless payments, ATM withdrawals, geographic usage, and spending notifications.',
      badge: 'Settings simulation',
      primaryPanelEyebrow: 'Card settings',
      primaryPanelTitle: 'Usage controls',
      items: [
        {
          label: 'Online payments',
          value: 'Enabled concept',
          note: 'No real setting is changed.',
        },
        {
          label: 'Contactless payments',
          value: 'Enabled concept',
          note: 'No real card configuration exists.',
        },
        {
          label: 'ATM withdrawals',
          value: 'Restricted concept',
          note: 'Withdrawal controls are simulated.',
        },
        {
          label: 'Geographic usage',
          value: 'Nordic region concept',
          note: 'Travel controls are static.',
        },
        {
          label: 'Spending notifications',
          value: 'Enabled concept',
          note: 'No notification service is connected.',
        },
      ],
      secondaryPanelEyebrow: 'Setting changes',
      secondaryPanelTitle: 'Simulated controls',
      rows: [
        {
          title: 'Online purchases',
          detail: 'Would require strong authentication for high-risk changes.',
          status: 'Requires review',
        },
        {
          title: 'Contactless usage',
          detail: 'Setting button is simulated only.',
          status: 'Simulated',
        },
        {
          title: 'Geographic usage',
          detail: 'No real card network controls are changed.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Settings summary',
      summaryItems: [
        { label: 'Online payments', value: 'Enabled concept' },
        { label: 'Contactless', value: 'Enabled concept' },
        { label: 'Real setting changes', value: 'None' },
      ],
      actionLabel: 'Save settings simulation',
      actionNote: 'Buttons are simulated only and do not update real card settings.',
      safetyTitle: 'Settings boundary',
      safetyNotice:
        'Local deterministic prototype only. No real card, card setting, card transaction, currency account, FX operation, travel money order, or banking operation is created or executed.',
    },
    limits: {
      eyebrow: 'Cards and Currency',
      title: 'Card limits',
      subtitle:
        'Simulated card limits for daily purchases, ATM withdrawals, online purchases, and temporary limit changes.',
      badge: 'Limit controls',
      primaryPanelEyebrow: 'Limit overview',
      primaryPanelTitle: 'Configured card limits',
      items: [
        {
          label: 'Daily purchase limit',
          value: '1,500.00 EUR',
          note: 'Static purchase limit.',
        },
        {
          label: 'ATM withdrawal limit',
          value: '300.00 EUR',
          note: 'Static ATM limit.',
        },
        {
          label: 'Online purchase limit',
          value: '750.00 EUR',
          note: 'Static online limit.',
        },
        {
          label: 'Temporary limit change',
          value: 'Review required',
          note: 'No real limit change is sent.',
        },
      ],
      secondaryPanelEyebrow: 'Limit changes',
      secondaryPanelTitle: 'Authentication and review',
      rows: [
        {
          title: 'Strong authentication',
          detail: 'Limit changes require strong authentication.',
          status: 'Required',
        },
        {
          title: 'Manual review',
          detail: 'Temporary increases require review before activation.',
          status: 'Requires review',
        },
        {
          title: 'Execution disabled',
          detail: 'No real card limit is changed.',
          status: 'Blocked',
        },
      ],
      summaryTitle: 'Limit summary',
      summaryItems: [
        { label: 'Daily purchase', value: '1,500.00 EUR' },
        { label: 'ATM withdrawal', value: '300.00 EUR' },
        { label: 'Real limit change', value: 'None' },
      ],
      actionLabel: 'Request limit simulation',
      actionNote: 'No real card limit change is submitted.',
      safetyTitle: 'Limit boundary',
      safetyNotice:
        'Local deterministic prototype only. No real card limit, card transaction, card application, currency account, FX operation, travel money order, or banking operation is created or executed.',
    },
    currencyAccounts: {
      eyebrow: 'Currency',
      title: 'Currency accounts',
      subtitle:
        'Simulated currency accounts overview with EUR, USD, SEK, and GBP available balances and currency risk notice.',
      badge: 'Currency overview',
      primaryPanelEyebrow: 'Currency accounts',
      primaryPanelTitle: 'Available balances',
      items: [
        {
          label: 'EUR account',
          value: '3,925.40 EUR',
          note: 'Primary simulated account.',
        },
        {
          label: 'USD account',
          value: '1,250.00 USD',
          note: 'Static currency balance.',
        },
        {
          label: 'SEK account',
          value: '8,400.00 SEK',
          note: 'Static currency balance.',
        },
        {
          label: 'GBP account',
          value: '620.00 GBP',
          note: 'Static currency balance.',
        },
      ],
      secondaryPanelEyebrow: 'Currency risk',
      secondaryPanelTitle: 'Currency account controls',
      rows: [
        {
          title: 'FX risk notice',
          detail: 'Currency values may fluctuate in real services.',
          status: 'Notice',
        },
        {
          title: 'Currency account opening',
          detail: 'No real currency account is opened.',
          status: 'Blocked',
        },
        {
          title: 'Balance source',
          detail: 'Balances are deterministic demo values.',
          status: 'Simulated',
        },
      ],
      summaryTitle: 'Currency summary',
      summaryItems: [
        { label: 'Currency accounts', value: '4 simulated' },
        { label: 'FX execution', value: 'None' },
        { label: 'Real account opening', value: 'None' },
      ],
      actionLabel: 'Open currency account simulation',
      actionNote: 'No real currency account is opened.',
      safetyTitle: 'Currency account boundary',
      safetyNotice:
        'Local deterministic prototype only. No real currency account, card, card transaction, FX operation, travel money order, or banking operation is created or executed.',
    },
    exchangeRates: {
      eyebrow: 'Currency',
      title: 'Exchange rates',
      subtitle:
        'Simulated exchange rates page with static EUR exchange rates and a simulated timestamp.',
      badge: 'Static rates',
      primaryPanelEyebrow: 'Exchange rate table',
      primaryPanelTitle: 'Indicative rates',
      items: [
        {
          label: 'EUR/USD',
          value: '1.0875',
          note: 'Static demo rate.',
        },
        {
          label: 'EUR/SEK',
          value: '11.2140',
          note: 'Static demo rate.',
        },
        {
          label: 'EUR/GBP',
          value: '0.8425',
          note: 'Static demo rate.',
        },
        {
          label: 'EUR/CHF',
          value: '0.9630',
          note: 'Static demo rate.',
        },
      ],
      secondaryPanelEyebrow: 'Rate timestamp',
      secondaryPanelTitle: 'Rate controls',
      rows: [
        {
          title: 'Simulated timestamp',
          detail: 'Rates shown as of 23.06.2026 12:00 EET.',
          status: 'Simulated',
        },
        {
          title: 'FX execution',
          detail: 'No real FX quote or execution is available.',
          status: 'Blocked',
        },
        {
          title: 'Currency risk',
          detail: 'Rates are illustrative and not customer pricing.',
          status: 'Notice',
        },
      ],
      summaryTitle: 'Exchange rate summary',
      summaryItems: [
        { label: 'Rate source', value: 'Static demo table' },
        { label: 'Timestamp', value: '23.06.2026 12:00 EET' },
        { label: 'Real FX execution', value: 'None' },
      ],
      actionLabel: 'Refresh rates simulation',
      actionNote: 'No real market data or FX execution is requested.',
      safetyTitle: 'FX boundary',
      safetyNotice:
        'Local deterministic prototype only. No real FX execution, currency account, card transaction, travel money order, or banking operation is created or executed.',
    },
    travelMoney: {
      eyebrow: 'Currency',
      title: 'Travel money',
      subtitle:
        'Simulated travel money page with destination currency selector, travel card usage notice, cash withdrawal limits, and travel notification panel.',
      badge: 'Travel settings',
      primaryPanelEyebrow: 'Travel money details',
      primaryPanelTitle: 'Destination and travel usage',
      items: [
        {
          label: 'Destination currency',
          value: 'USD',
          note: 'Visual selector only.',
        },
        {
          label: 'Travel card usage',
          value: 'International card usage notice',
          note: 'No card setting is changed.',
        },
        {
          label: 'Cash withdrawal limits',
          value: '300.00 EUR equivalent',
          note: 'Static travel limit.',
        },
        {
          label: 'Travel notification',
          value: 'Destination notice prepared',
          note: 'No real notification is sent.',
        },
      ],
      secondaryPanelEyebrow: 'Travel controls',
      secondaryPanelTitle: 'Travel notification panel',
      rows: [
        {
          title: 'Destination review',
          detail: 'Destination currency is selected for visual review.',
          status: 'Ready',
        },
        {
          title: 'Cash order',
          detail: 'No cash or travel money order is placed.',
          status: 'Blocked',
        },
        {
          title: 'Card usage notice',
          detail: 'Travel card usage notice is informational only.',
          status: 'Notice',
        },
      ],
      summaryTitle: 'Travel summary',
      summaryItems: [
        { label: 'Destination currency', value: 'USD' },
        { label: 'Cash withdrawal limit', value: '300.00 EUR equivalent' },
        { label: 'Real travel money order', value: 'None' },
      ],
      actionLabel: 'Create travel notice simulation',
      actionNote: 'No real travel money order or card change is submitted.',
      safetyTitle: 'Travel money boundary',
      safetyNotice:
        'Local deterministic prototype only. No real travel money order, card transaction, currency account, FX operation, or banking operation is created or executed.',
    },
    cardFaq: {
      eyebrow: 'Cards and Currency',
      title: 'Card FAQ',
      subtitle:
        'Card FAQ covering lost or stolen cards, online payments, contactless payments, card limits, currency conversion, and digital asset separation.',
      badge: 'FAQ',
      primaryPanelEyebrow: 'Common card questions',
      primaryPanelTitle: 'Card guidance',
      items: [
        {
          label: 'Lost or stolen card',
          value: 'Contact official bank channels immediately.',
          note: 'Prototype guidance only.',
        },
        {
          label: 'Online payments',
          value: 'May require strong authentication.',
          note: 'No payment is executed here.',
        },
        {
          label: 'Contactless payments',
          value: 'Controlled by card settings concept.',
          note: 'No real setting is changed.',
        },
        {
          label: 'Currency conversion',
          value: 'FX rates may vary in real services.',
          note: 'No real FX operation is performed.',
        },
        {
          label: 'Digital assets',
          value: 'Separate from card and deposit products.',
          note: 'Digital assets are not card balances.',
        },
      ],
      secondaryPanelEyebrow: 'FAQ topics',
      secondaryPanelTitle: 'Support topics',
      rows: [
        {
          title: 'Card limits',
          detail: 'Limit changes require review and strong authentication in a real service.',
          status: 'Information',
        },
        {
          title: 'Currency conversion',
          detail: 'Exchange rates are illustrative in this prototype.',
          status: 'Notice',
        },
        {
          title: 'Digital asset separation',
          detail: 'Digital assets are separate from card and deposit products.',
          status: 'Risk notice',
        },
      ],
      summaryTitle: 'FAQ summary',
      summaryItems: [
        { label: 'Card support', value: 'Informational' },
        { label: 'Currency conversion', value: 'No real FX' },
        { label: 'Digital assets', value: 'Separate products' },
      ],
      actionLabel: 'Open security settings',
      actionNote: 'This is an informational prototype page.',
      safetyTitle: 'Prototype boundary',
      safetyNotice:
        'Local deterministic prototype only. No real card, card application, card transaction, currency account, FX operation, travel money order, or banking operation is created or executed.',
    },
  },
}

const cardDemoEs: CardDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealCardOrFxOperation: 'Sin operación real de tarjeta o divisas',
  },
  pages: {
    overview: {
      eyebrow: 'Tarjetas y moneda',
      title: 'Resumen de tarjetas',
      subtitle:
        'Resumen simulado de tarjeta de débito, tarjeta de crédito, estado de tarjeta, actividad reciente y seguridad de tarjeta.',
      badge: 'Seguridad de tarjeta activa',
      primaryPanelEyebrow: 'Tarjetas',
      primaryPanelTitle: 'Resumen de tarjetas',
      items: [
        {
          label: 'Resumen de tarjeta de débito',
          value: 'Aurora Debit Online · Activa',
          note: 'Tarjeta de débito ficticia para el prototipo local.',
        },
        {
          label: 'Resumen de tarjeta de crédito',
          value: 'Aurora Gold · Revisión requerida',
          note: 'Concepto de tarjeta de crédito sin línea de crédito real.',
        },
        {
          label: 'Estado de seguridad de tarjeta',
          value: 'Compras en línea monitorizadas',
          note: 'Estado de seguridad estático solamente.',
        },
      ],
      secondaryPanelEyebrow: 'Actividad simulada reciente',
      secondaryPanelTitle: 'Actividad de tarjeta',
      rows: [
        {
          title: '12.06.2026 · Compra de alimentación',
          detail: '-42,80 EUR · Aurora Debit Online',
          status: 'Completada',
        },
        {
          title: '15.06.2026 · Intento de compra en línea',
          detail: '-129,00 EUR · Requiere revisión reforzada',
          status: 'Requiere revisión',
        },
        {
          title: '18.06.2026 · Autorización de tarjeta en extranjero',
          detail: '-76,10 EUR · Bloqueada por controles de viaje',
          status: 'Bloqueada',
        },
      ],
      summaryTitle: 'Resumen de tarjeta',
      summaryItems: [
        { label: 'Tarjeta de débito', value: 'Activa' },
        { label: 'Tarjeta de crédito', value: 'Concepto en revisión' },
        { label: 'Transacciones reales', value: 'Ninguna' },
      ],
      actionLabel: 'Actualizar simulación',
      actionNote: 'No se realiza ninguna consulta real de datos de tarjeta o transacciones.',
      safetyTitle: 'Límite de tarjeta',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ninguna tarjeta real, solicitud de tarjeta, transacción de tarjeta, cuenta en divisa, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
    apply: {
      eyebrow: 'Tarjetas y moneda',
      title: 'Solicitar tarjeta',
      subtitle:
        'Flujo simulado de solicitud de tarjeta con selección de tipo, checklist de elegibilidad, marcadores de verificación y estado de revisión.',
      badge: 'Borrador de solicitud',
      primaryPanelEyebrow: 'Detalles de solicitud',
      primaryPanelTitle: 'Selección de tipo de tarjeta',
      items: [
        {
          label: 'Tipo de tarjeta seleccionado',
          value: 'Aurora Debit Online',
          note: 'Selección estática de tipo de tarjeta.',
        },
        {
          label: 'Verificación de identidad',
          value: 'Revisión como marcador',
          note: 'No se recopilan datos de identidad.',
        },
        {
          label: 'Verificación de ingresos',
          value: 'Revisión como marcador',
          note: 'No se solicitan datos de ingresos.',
        },
      ],
      secondaryPanelEyebrow: 'Checklist de elegibilidad',
      secondaryPanelTitle: 'Estado de revisión de solicitud',
      rows: [
        {
          title: 'Relación con el cliente',
          detail: 'Una solicitud real requeriría relación bancaria activa.',
          status: 'Requerido',
        },
        {
          title: 'Verificación de identidad e ingresos',
          detail: 'La verificación se representa solo como marcador.',
          status: 'Requerido',
        },
        {
          title: 'Envío de solicitud',
          detail: 'El envío está deshabilitado en este prototipo.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de solicitud',
      summaryItems: [
        { label: 'Tipo de tarjeta', value: 'Aurora Debit Online' },
        { label: 'Revisión', value: 'Requerida' },
        { label: 'Solicitud real', value: 'Ninguna' },
      ],
      actionLabel: 'Enviar solicitud simulada',
      actionNote: 'El botón está deshabilitado porque no se envía ninguna solicitud real de tarjeta.',
      safetyTitle: 'Límite de solicitud',
      safetyNotice:
        'Solo prototipo local determinístico. Sin emisión real de tarjetas y sin creación ni ejecución de solicitud de tarjeta, transacción de tarjeta, cuenta en divisa, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
    settings: {
      eyebrow: 'Tarjetas y moneda',
      title: 'Configuración de tarjeta',
      subtitle:
        'Configuración simulada de tarjeta para pagos en línea, pagos contactless, retiradas en cajero, uso geográfico y notificaciones de gasto.',
      badge: 'Simulación de configuración',
      primaryPanelEyebrow: 'Configuración de tarjeta',
      primaryPanelTitle: 'Controles de uso',
      items: [
        {
          label: 'Pagos en línea',
          value: 'Concepto habilitado',
          note: 'No se cambia ninguna configuración real.',
        },
        {
          label: 'Pagos contactless',
          value: 'Concepto habilitado',
          note: 'No existe configuración real de tarjeta.',
        },
        {
          label: 'Retiradas en cajero',
          value: 'Concepto restringido',
          note: 'Los controles de retirada son simulados.',
        },
        {
          label: 'Uso geográfico',
          value: 'Concepto de región nórdica',
          note: 'Los controles de viaje son estáticos.',
        },
        {
          label: 'Notificaciones de gasto',
          value: 'Concepto habilitado',
          note: 'No hay servicio de notificaciones conectado.',
        },
      ],
      secondaryPanelEyebrow: 'Cambios de configuración',
      secondaryPanelTitle: 'Controles simulados',
      rows: [
        {
          title: 'Compras en línea',
          detail: 'Los cambios de alto riesgo requerirían autenticación fuerte.',
          status: 'Requiere revisión',
        },
        {
          title: 'Uso contactless',
          detail: 'El botón de configuración es solo simulado.',
          status: 'Simulado',
        },
        {
          title: 'Uso geográfico',
          detail: 'No se cambia ningún control real de red de tarjetas.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de configuración',
      summaryItems: [
        { label: 'Pagos en línea', value: 'Concepto habilitado' },
        { label: 'Contactless', value: 'Concepto habilitado' },
        { label: 'Cambios reales', value: 'Ninguno' },
      ],
      actionLabel: 'Guardar configuración simulada',
      actionNote: 'Los botones son solo simulados y no actualizan configuraciones reales de tarjeta.',
      safetyTitle: 'Límite de configuración',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ninguna tarjeta real, configuración de tarjeta, transacción de tarjeta, cuenta en divisa, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
    limits: {
      eyebrow: 'Tarjetas y moneda',
      title: 'Límites de tarjeta',
      subtitle:
        'Límites simulados de tarjeta para compras diarias, retiradas en cajero, compras en línea y cambios temporales de límite.',
      badge: 'Controles de límite',
      primaryPanelEyebrow: 'Resumen de límites',
      primaryPanelTitle: 'Límites de tarjeta configurados',
      items: [
        {
          label: 'Límite diario de compras',
          value: '1.500,00 EUR',
          note: 'Límite de compra estático.',
        },
        {
          label: 'Límite de retirada en cajero',
          value: '300,00 EUR',
          note: 'Límite de cajero estático.',
        },
        {
          label: 'Límite de compra en línea',
          value: '750,00 EUR',
          note: 'Límite en línea estático.',
        },
        {
          label: 'Cambio temporal de límite',
          value: 'Revisión requerida',
          note: 'No se envía ningún cambio real de límite.',
        },
      ],
      secondaryPanelEyebrow: 'Cambios de límite',
      secondaryPanelTitle: 'Autenticación y revisión',
      rows: [
        {
          title: 'Autenticación fuerte',
          detail: 'Los cambios de límite requieren autenticación fuerte.',
          status: 'Requerido',
        },
        {
          title: 'Revisión manual',
          detail: 'Los incrementos temporales requieren revisión antes de activarse.',
          status: 'Requiere revisión',
        },
        {
          title: 'Ejecución deshabilitada',
          detail: 'No se cambia ningún límite real de tarjeta.',
          status: 'Bloqueado',
        },
      ],
      summaryTitle: 'Resumen de límites',
      summaryItems: [
        { label: 'Compra diaria', value: '1.500,00 EUR' },
        { label: 'Retirada en cajero', value: '300,00 EUR' },
        { label: 'Cambio real de límite', value: 'Ninguno' },
      ],
      actionLabel: 'Solicitar simulación de límite',
      actionNote: 'No se envía ningún cambio real de límite de tarjeta.',
      safetyTitle: 'Límite operativo',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ningún límite real de tarjeta, transacción de tarjeta, solicitud de tarjeta, cuenta en divisa, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
    currencyAccounts: {
      eyebrow: 'Moneda',
      title: 'Cuentas en divisas',
      subtitle:
        'Resumen simulado de cuentas en divisas con saldos disponibles en EUR, USD, SEK y GBP, y nota de riesgo de divisa.',
      badge: 'Resumen de divisas',
      primaryPanelEyebrow: 'Cuentas en divisas',
      primaryPanelTitle: 'Saldos disponibles',
      items: [
        {
          label: 'Cuenta EUR',
          value: '3.925,40 EUR',
          note: 'Cuenta principal simulada.',
        },
        {
          label: 'Cuenta USD',
          value: '1.250,00 USD',
          note: 'Saldo estático en divisa.',
        },
        {
          label: 'Cuenta SEK',
          value: '8.400,00 SEK',
          note: 'Saldo estático en divisa.',
        },
        {
          label: 'Cuenta GBP',
          value: '620,00 GBP',
          note: 'Saldo estático en divisa.',
        },
      ],
      secondaryPanelEyebrow: 'Riesgo de divisa',
      secondaryPanelTitle: 'Controles de cuenta en divisa',
      rows: [
        {
          title: 'Aviso de riesgo FX',
          detail: 'Los valores de divisa pueden fluctuar en servicios reales.',
          status: 'Aviso',
        },
        {
          title: 'Apertura de cuenta en divisa',
          detail: 'No se abre ninguna cuenta real en divisa.',
          status: 'Bloqueado',
        },
        {
          title: 'Origen del saldo',
          detail: 'Los saldos son valores demo determinísticos.',
          status: 'Simulado',
        },
      ],
      summaryTitle: 'Resumen de divisas',
      summaryItems: [
        { label: 'Cuentas en divisas', value: '4 simuladas' },
        { label: 'Ejecución FX', value: 'Ninguna' },
        { label: 'Apertura real', value: 'Ninguna' },
      ],
      actionLabel: 'Simular apertura de cuenta en divisa',
      actionNote: 'No se abre ninguna cuenta real en divisa.',
      safetyTitle: 'Límite de cuenta en divisa',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ninguna cuenta real en divisa, tarjeta, transacción de tarjeta, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
    exchangeRates: {
      eyebrow: 'Moneda',
      title: 'Tipos de cambio',
      subtitle:
        'Página simulada de tipos de cambio con tipos EUR estáticos y marca temporal simulada.',
      badge: 'Tipos estáticos',
      primaryPanelEyebrow: 'Tabla de tipos de cambio',
      primaryPanelTitle: 'Tipos indicativos',
      items: [
        {
          label: 'EUR/USD',
          value: '1,0875',
          note: 'Tipo demo estático.',
        },
        {
          label: 'EUR/SEK',
          value: '11,2140',
          note: 'Tipo demo estático.',
        },
        {
          label: 'EUR/GBP',
          value: '0,8425',
          note: 'Tipo demo estático.',
        },
        {
          label: 'EUR/CHF',
          value: '0,9630',
          note: 'Tipo demo estático.',
        },
      ],
      secondaryPanelEyebrow: 'Marca temporal de tipos',
      secondaryPanelTitle: 'Controles de tipos',
      rows: [
        {
          title: 'Marca temporal simulada',
          detail: 'Tipos mostrados a fecha 23.06.2026 12:00 EET.',
          status: 'Simulado',
        },
        {
          title: 'Ejecución FX',
          detail: 'No hay cotización ni ejecución FX real disponible.',
          status: 'Bloqueado',
        },
        {
          title: 'Riesgo de divisa',
          detail: 'Los tipos son ilustrativos y no son precios para clientes.',
          status: 'Aviso',
        },
      ],
      summaryTitle: 'Resumen de tipos de cambio',
      summaryItems: [
        { label: 'Origen de tipos', value: 'Tabla demo estática' },
        { label: 'Marca temporal', value: '23.06.2026 12:00 EET' },
        { label: 'Ejecución real FX', value: 'Ninguna' },
      ],
      actionLabel: 'Actualizar tipos simulados',
      actionNote: 'No se solicita ningún dato real de mercado ni ejecución FX.',
      safetyTitle: 'Límite FX',
      safetyNotice:
        'Solo prototipo local determinístico. Sin ejecución real de divisas y sin creación ni ejecución de cuenta en divisa, transacción de tarjeta, pedido de dinero para viaje u operación bancaria.',
    },
    travelMoney: {
      eyebrow: 'Moneda',
      title: 'Dinero para viaje',
      subtitle:
        'Página simulada de dinero para viaje con selector visual de divisa de destino, aviso de uso de tarjeta, límites de retirada y panel de notificación de viaje.',
      badge: 'Configuración de viaje',
      primaryPanelEyebrow: 'Detalles de viaje',
      primaryPanelTitle: 'Destino y uso en viaje',
      items: [
        {
          label: 'Divisa de destino',
          value: 'USD',
          note: 'Selector solo visual.',
        },
        {
          label: 'Uso de tarjeta en viaje',
          value: 'Aviso de uso internacional de tarjeta',
          note: 'No se cambia ninguna configuración de tarjeta.',
        },
        {
          label: 'Límites de retirada de efectivo',
          value: '300,00 EUR equivalente',
          note: 'Límite de viaje estático.',
        },
        {
          label: 'Notificación de viaje',
          value: 'Aviso de destino preparado',
          note: 'No se envía ninguna notificación real.',
        },
      ],
      secondaryPanelEyebrow: 'Controles de viaje',
      secondaryPanelTitle: 'Panel de notificación de viaje',
      rows: [
        {
          title: 'Revisión de destino',
          detail: 'La divisa de destino se selecciona para revisión visual.',
          status: 'Listo',
        },
        {
          title: 'Pedido de efectivo',
          detail: 'No se realiza ningún pedido de efectivo o dinero para viaje.',
          status: 'Bloqueado',
        },
        {
          title: 'Aviso de uso de tarjeta',
          detail: 'El aviso de uso de tarjeta en viaje es solo informativo.',
          status: 'Aviso',
        },
      ],
      summaryTitle: 'Resumen de viaje',
      summaryItems: [
        { label: 'Divisa de destino', value: 'USD' },
        { label: 'Límite de retirada', value: '300,00 EUR equivalente' },
        { label: 'Pedido real de dinero para viaje', value: 'Ninguno' },
      ],
      actionLabel: 'Crear aviso de viaje simulado',
      actionNote: 'No se envía ningún pedido real de dinero para viaje ni cambio de tarjeta.',
      safetyTitle: 'Límite de dinero para viaje',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ningún pedido real de dinero para viaje, transacción de tarjeta, cuenta en divisa, operación FX u operación bancaria.',
    },
    cardFaq: {
      eyebrow: 'Tarjetas y moneda',
      title: 'Preguntas frecuentes de tarjetas',
      subtitle:
        'Preguntas frecuentes sobre tarjeta perdida o robada, pagos en línea, pagos contactless, límites de tarjeta, conversión de moneda y separación de activos digitales.',
      badge: 'Preguntas frecuentes',
      primaryPanelEyebrow: 'Preguntas comunes de tarjetas',
      primaryPanelTitle: 'Orientación sobre tarjetas',
      items: [
        {
          label: 'Tarjeta perdida o robada',
          value: 'Contacte inmediatamente con canales bancarios oficiales.',
          note: 'Orientación de prototipo solamente.',
        },
        {
          label: 'Pagos en línea',
          value: 'Pueden requerir autenticación fuerte.',
          note: 'Aquí no se ejecuta ningún pago.',
        },
        {
          label: 'Pagos contactless',
          value: 'Controlados por el concepto de configuración de tarjeta.',
          note: 'No se cambia ninguna configuración real.',
        },
        {
          label: 'Conversión de moneda',
          value: 'Los tipos FX pueden variar en servicios reales.',
          note: 'No se realiza ninguna operación FX real.',
        },
        {
          label: 'Activos digitales',
          value: 'Separados de productos de tarjeta y depósito.',
          note: 'Los activos digitales no son saldos de tarjeta.',
        },
      ],
      secondaryPanelEyebrow: 'Temas de FAQ',
      secondaryPanelTitle: 'Temas de soporte',
      rows: [
        {
          title: 'Límites de tarjeta',
          detail: 'Los cambios de límite requerirían revisión y autenticación fuerte en un servicio real.',
          status: 'Información',
        },
        {
          title: 'Conversión de moneda',
          detail: 'Los tipos de cambio son ilustrativos en este prototipo.',
          status: 'Aviso',
        },
        {
          title: 'Separación de activos digitales',
          detail: 'Los activos digitales están separados de productos de tarjeta y depósito.',
          status: 'Aviso de riesgo',
        },
      ],
      summaryTitle: 'Resumen de FAQ',
      summaryItems: [
        { label: 'Soporte de tarjeta', value: 'Informativo' },
        { label: 'Conversión de moneda', value: 'Sin FX real' },
        { label: 'Activos digitales', value: 'Productos separados' },
      ],
      actionLabel: 'Abrir configuración de seguridad',
      actionNote: 'Esta es una página informativa del prototipo.',
      safetyTitle: 'Límite del prototipo',
      safetyNotice:
        'Solo prototipo local determinístico. No se crea ni ejecuta ninguna tarjeta real, solicitud de tarjeta, transacción de tarjeta, cuenta en divisa, operación FX, pedido de dinero para viaje u operación bancaria.',
    },
  },
}

type InvestmentDemoPageTranslation = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryPanelTitle: string
  primaryPanelEyebrow: string
  items: { label: string; value: string; note: string }[]
  secondaryPanelTitle: string
  secondaryPanelEyebrow: string
  rows: { title: string; detail: string; status: string }[]
  summaryTitle: string
  summaryItems: { label: string; value: string }[]
  actionLabel: string
  actionNote: string
  riskTitle: string
  riskNotice: string
  safetyTitle: string
  safetyNotice: string
}

type LoanDemoPageTranslation = {
  eyebrow: string
  title: string
  subtitle: string
  badge: string
  primaryPanelTitle: string
  primaryPanelEyebrow: string
  items: { label: string; value: string; note: string }[]
  secondaryPanelTitle: string
  secondaryPanelEyebrow: string
  rows: { title: string; detail: string; status: string }[]
  summaryTitle: string
  summaryItems: { label: string; value: string }[]
  actionLabel: string
  actionNote: string
  riskTitle: string
  riskNotice: string
  safetyTitle: string
  safetyNotice: string
}

type LoanDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealLoanOperation: string
    noRealCreditDecision: string
  }
  pages: Record<
    | 'loans'
    | 'overview'
    | 'application'
    | 'mortgage'
    | 'consumerLoan'
    | 'studentLoan'
    | 'loanCalculator'
    | 'repaymentPlan'
    | 'documents'
    | 'loanFaq',
    LoanDemoPageTranslation
  >
}

const loanBoundaryEn =
  'Local deterministic prototype only. No real loan, credit decision, application, repayment change, personal data, collateral evaluation, or banking operation is created or executed. Digital assets are not accepted as collateral in this prototype.'

const loanBoundaryEs =
  'Solo prototipo local determinístico. No se crea ni ejecuta ningún préstamo real, decisión crediticia, solicitud, cambio de pago, dato personal, evaluación de garantía u operación bancaria. Los activos digitales no se aceptan como garantía en este prototipo.'

const loanDemoEn: LoanDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealLoanOperation: 'No real loan operation',
    noRealCreditDecision: 'No real credit decision',
  },
  pages: {
    loans: {
      eyebrow: 'Loans',
      title: 'Loans',
      subtitle:
        'Banking-style overview of simulated loan services, active loan status, application status, repayment information, and safety boundaries.',
      badge: 'Loans concept',
      primaryPanelEyebrow: 'Loan summary',
      primaryPanelTitle: 'Simulated loan position',
      items: [
        { label: 'Total outstanding simulated amount', value: '185,240.00 EUR', note: 'Static demo amount only.' },
        { label: 'Active simulated loan', value: 'Home loan concept', note: 'No real credit account exists.' },
        { label: 'Next payment placeholder', value: '15.07.2026', note: 'Repayment date is illustrative.' },
      ],
      secondaryPanelEyebrow: 'Available loan services',
      secondaryPanelTitle: 'Services and status',
      rows: [
        { title: 'Loan overview', detail: 'Review simulated home, consumer, and student loan balances.', status: 'Simulated' },
        { title: 'Application status placeholder', detail: 'No application is active or submitted.', status: 'No real application' },
        { title: 'Repayment overview', detail: 'Upcoming installment information is static.', status: 'Prototype estimate' },
      ],
      summaryTitle: 'Loan summary',
      summaryItems: [
        { label: 'Active loans', value: '1 simulated' },
        { label: 'Application status', value: 'Placeholder' },
        { label: 'Credit decision', value: 'None' },
      ],
      actionLabel: 'Open loan services',
      actionNote: 'This disabled control represents navigation only. No loan service is executed.',
      riskTitle: 'Safety note',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Prototype boundary',
      safetyNotice: loanBoundaryEn,
    },
    overview: {
      eyebrow: 'Loans',
      title: 'Loan overview',
      subtitle:
        'Simulated overview of home loan, consumer loan, student loan, repayment status, next payment, and total outstanding amount.',
      badge: 'Overview concept',
      primaryPanelEyebrow: 'Outstanding balance',
      primaryPanelTitle: 'Loan portfolio view',
      items: [
        { label: 'Home loan / mortgage', value: '178,500.00 EUR', note: 'Static mortgage balance.' },
        { label: 'Consumer loan', value: '0.00 EUR', note: 'No active consumer credit in the demo.' },
        { label: 'Student loan', value: '6,740.00 EUR', note: 'Static student loan balance.' },
      ],
      secondaryPanelEyebrow: 'Repayment status',
      secondaryPanelTitle: 'Status overview',
      rows: [
        { title: 'Mortgage installment', detail: 'Next payment placeholder 15.07.2026.', status: 'Scheduled' },
        { title: 'Student loan installment', detail: 'Repayment plan shown for demonstration.', status: 'Simulated' },
        { title: 'Total outstanding simulated amount', detail: '185,240.00 EUR across demo loan rows.', status: 'Prototype estimate' },
      ],
      summaryTitle: 'Overview summary',
      summaryItems: [
        { label: 'Total outstanding', value: '185,240.00 EUR' },
        { label: 'Next payment', value: '15.07.2026' },
        { label: 'Repayment status', value: 'Simulated' },
      ],
      actionLabel: 'Review overview simulation',
      actionNote: 'No real balance inquiry or loan account operation is made.',
      riskTitle: 'No real loan data',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Data boundary',
      safetyNotice: loanBoundaryEn,
    },
    application: {
      eyebrow: 'Loans',
      title: 'Apply for a loan',
      subtitle:
        'Simulated loan application flow for loan type, amount, repayment period, income and expense review, and application status.',
      badge: 'Application draft',
      primaryPanelEyebrow: 'Application details',
      primaryPanelTitle: 'Loan application form',
      items: [
        { label: 'Loan type', value: 'Consumer loan concept', note: 'Visual selection only.' },
        { label: 'Amount', value: '10,000.00 EUR', note: 'Static requested amount.' },
        { label: 'Repayment period', value: '48 months', note: 'No repayment term is saved.' },
      ],
      secondaryPanelEyebrow: 'Income and expense review',
      secondaryPanelTitle: 'Application review status',
      rows: [
        { title: 'Income review placeholder', detail: 'No income data is collected or assessed.', status: 'Not submitted' },
        { title: 'Expense review placeholder', detail: 'Affordability is not calculated by a real model.', status: 'No credit scoring' },
        { title: 'Application review status', detail: 'Application remains local and disabled.', status: 'Draft' },
      ],
      summaryTitle: 'Application summary',
      summaryItems: [
        { label: 'Loan type', value: 'Consumer loan' },
        { label: 'Submission', value: 'Disabled' },
        { label: 'Credit decision', value: 'None' },
      ],
      actionLabel: 'Submit simulated application',
      actionNote: 'The submit control is disabled. No real loan application is submitted.',
      riskTitle: 'No real loan application',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Application boundary',
      safetyNotice: loanBoundaryEn,
    },
    mortgage: {
      eyebrow: 'Loans',
      title: 'Mortgage',
      subtitle:
        'Simulated home loan page with loan overview, collateral placeholder, interest type placeholder, repayment period, and affordability review.',
      badge: 'Mortgage concept',
      primaryPanelEyebrow: 'Home loan overview',
      primaryPanelTitle: 'Mortgage details',
      items: [
        { label: 'Home loan overview', value: '178,500.00 EUR', note: 'Static outstanding balance.' },
        { label: 'Interest type placeholder', value: 'Variable concept', note: 'No real pricing or reference rate.' },
        { label: 'Repayment period', value: '22 years remaining', note: 'Illustrative term only.' },
      ],
      secondaryPanelEyebrow: 'Collateral and affordability',
      secondaryPanelTitle: 'Review placeholders',
      rows: [
        { title: 'Collateral placeholder', detail: 'No property or collateral valuation is performed.', status: 'Placeholder' },
        { title: 'Affordability review', detail: 'Payment capacity is not assessed by a real model.', status: 'Simulated' },
        { title: 'Mortgage decision', detail: 'No real mortgage decision is issued.', status: 'No real decision' },
      ],
      summaryTitle: 'Mortgage summary',
      summaryItems: [
        { label: 'Outstanding balance', value: '178,500.00 EUR' },
        { label: 'Interest type', value: 'Placeholder' },
        { label: 'Collateral evaluation', value: 'None' },
      ],
      actionLabel: 'Review mortgage simulation',
      actionNote: 'No mortgage terms, collateral values, or repayment plans are changed.',
      riskTitle: 'No real mortgage decision',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Mortgage boundary',
      safetyNotice: loanBoundaryEn,
    },
    consumerLoan: {
      eyebrow: 'Loans',
      title: 'Consumer loan',
      subtitle:
        'Simulated consumer loan page with amount, repayment period, monthly installment placeholder, and risk and affordability notice.',
      badge: 'Credit concept',
      primaryPanelEyebrow: 'Consumer loan details',
      primaryPanelTitle: 'Loan amount and term',
      items: [
        { label: 'Loan amount', value: '10,000.00 EUR', note: 'Static example amount.' },
        { label: 'Repayment period', value: '48 months', note: 'Visual repayment period.' },
        { label: 'Monthly installment placeholder', value: '230.00 EUR', note: 'Estimate only, not an offer.' },
      ],
      secondaryPanelEyebrow: 'Risk and affordability notice',
      secondaryPanelTitle: 'Review controls',
      rows: [
        { title: 'Affordability notice', detail: 'No income, expenses, or credit data are processed.', status: 'Required' },
        { title: 'Risk notice', detail: 'Borrowing may increase financial risk.', status: 'Notice' },
        { title: 'Credit execution', detail: 'No real consumer credit is granted.', status: 'No real credit' },
      ],
      summaryTitle: 'Consumer loan summary',
      summaryItems: [
        { label: 'Monthly installment', value: '230.00 EUR' },
        { label: 'Affordability review', value: 'Placeholder' },
        { label: 'Credit status', value: 'No real credit' },
      ],
      actionLabel: 'Calculate consumer loan simulation',
      actionNote: 'No real consumer credit application or credit scoring is executed.',
      riskTitle: 'No real consumer credit',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Consumer credit boundary',
      safetyNotice: loanBoundaryEn,
    },
    studentLoan: {
      eyebrow: 'Loans',
      title: 'Student loan',
      subtitle:
        'Simulated student loan page with balance, guarantee and eligibility placeholder, next installment, and repayment plan.',
      badge: 'Student loan concept',
      primaryPanelEyebrow: 'Student loan balance',
      primaryPanelTitle: 'Balance and installment',
      items: [
        { label: 'Student loan balance', value: '6,740.00 EUR', note: 'Static demo balance.' },
        { label: 'Guarantee / eligibility placeholder', value: 'Not evaluated', note: 'No real guarantee data is used.' },
        { label: 'Next installment', value: '125.00 EUR', note: 'Illustrative payment only.' },
      ],
      secondaryPanelEyebrow: 'Repayment plan',
      secondaryPanelTitle: 'Plan status',
      rows: [
        { title: 'Repayment plan', detail: 'Repayment schedule shown as simulated rows.', status: 'Simulated' },
        { title: 'Eligibility placeholder', detail: 'No eligibility check is performed.', status: 'Placeholder' },
        { title: 'Student loan data', detail: 'No real student loan registry data is connected.', status: 'No real data' },
      ],
      summaryTitle: 'Student loan summary',
      summaryItems: [
        { label: 'Balance', value: '6,740.00 EUR' },
        { label: 'Next installment', value: '125.00 EUR' },
        { label: 'Eligibility', value: 'Placeholder' },
      ],
      actionLabel: 'Review student loan simulation',
      actionNote: 'No real student loan data, guarantee, or repayment change is created.',
      riskTitle: 'No real student loan data',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Student loan boundary',
      safetyNotice: loanBoundaryEn,
    },
    loanCalculator: {
      eyebrow: 'Loans',
      title: 'Loan calculator',
      subtitle:
        'Simulated loan calculator with amount input visual, repayment period visual, interest placeholder, and estimated monthly payment.',
      badge: 'Calculator concept',
      primaryPanelEyebrow: 'Calculator inputs',
      primaryPanelTitle: 'Loan estimate',
      items: [
        { label: 'Amount input visual', value: '25,000.00 EUR', note: 'Static input display.' },
        { label: 'Repayment period visual', value: '60 months', note: 'Static term display.' },
        { label: 'Interest placeholder', value: '4.50%', note: 'Not a real rate or offer.' },
      ],
      secondaryPanelEyebrow: 'Estimated monthly payment',
      secondaryPanelTitle: 'Simulated result',
      rows: [
        { title: 'Estimated monthly payment', detail: '466.00 EUR, simulated and rounded.', status: 'Prototype estimate' },
        { title: 'Financial advice', detail: 'This calculator does not provide financial advice.', status: 'No advice' },
        { title: 'Credit offer', detail: 'No binding rate, offer, or decision is produced.', status: 'No offer' },
      ],
      summaryTitle: 'Calculator summary',
      summaryItems: [
        { label: 'Amount', value: '25,000.00 EUR' },
        { label: 'Period', value: '60 months' },
        { label: 'Monthly estimate', value: '466.00 EUR' },
      ],
      actionLabel: 'Run simulated calculation',
      actionNote: 'No real loan calculation, affordability assessment, or advice is executed.',
      riskTitle: 'No financial advice',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Calculator boundary',
      safetyNotice: loanBoundaryEn,
    },
    repaymentPlan: {
      eyebrow: 'Loans',
      title: 'Repayment plan',
      subtitle:
        'Simulated repayment plan showing upcoming installments, payment date, principal, interest, and remaining balance.',
      badge: 'Repayment concept',
      primaryPanelEyebrow: 'Upcoming installments',
      primaryPanelTitle: 'Repayment schedule',
      items: [
        { label: 'Payment date', value: '15.07.2026', note: 'Static upcoming installment.' },
        { label: 'Principal', value: '520.00 EUR', note: 'Illustrative amount.' },
        { label: 'Interest', value: '185.00 EUR', note: 'Illustrative interest amount.' },
      ],
      secondaryPanelEyebrow: 'Remaining balance',
      secondaryPanelTitle: 'Installment rows',
      rows: [
        { title: '15.07.2026 installment', detail: 'Principal 520.00 EUR, interest 185.00 EUR, balance 184,720.00 EUR.', status: 'Scheduled' },
        { title: '15.08.2026 installment', detail: 'Principal 522.00 EUR, interest 183.00 EUR, balance 184,198.00 EUR.', status: 'Simulated' },
        { title: 'Repayment changes', detail: 'No real repayment changes are created.', status: 'No real change' },
      ],
      summaryTitle: 'Plan summary',
      summaryItems: [
        { label: 'Upcoming installments', value: '2 shown' },
        { label: 'Remaining balance', value: '184,720.00 EUR' },
        { label: 'Changes', value: 'None' },
      ],
      actionLabel: 'Request repayment change simulation',
      actionNote: 'No repayment change request is sent or recorded.',
      riskTitle: 'No real repayment changes',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Repayment boundary',
      safetyNotice: loanBoundaryEn,
    },
    documents: {
      eyebrow: 'Loans',
      title: 'Loan documents',
      subtitle:
        'Simulated loan documents area for loan agreement, repayment schedule, interest certificate, and annual statement.',
      badge: 'Documents concept',
      primaryPanelEyebrow: 'Document list',
      primaryPanelTitle: 'Available simulated documents',
      items: [
        { label: 'Loan agreement', value: 'PDF concept', note: 'Simulated document entry.' },
        { label: 'Repayment schedule', value: 'PDF concept', note: 'Simulated repayment schedule.' },
        { label: 'Interest certificate', value: 'PDF concept', note: 'Simulated certificate.' },
      ],
      secondaryPanelEyebrow: 'Document status',
      secondaryPanelTitle: 'Document archive',
      rows: [
        { title: 'Annual statement', detail: 'Fictional statement for prototype display.', status: 'Simulated' },
        { title: 'Loan agreement', detail: 'Document metadata only, no real contract.', status: 'No real document' },
        { title: 'Repayment schedule', detail: 'Schedule is illustrative and not bank-generated.', status: 'Prototype estimate' },
      ],
      summaryTitle: 'Document summary',
      summaryItems: [
        { label: 'Documents', value: '4 simulated' },
        { label: 'Real contracts', value: 'None' },
        { label: 'Download execution', value: 'Disabled' },
      ],
      actionLabel: 'Open simulated document',
      actionNote: 'No real document is opened, generated, or downloaded.',
      riskTitle: 'Documents marked as simulated',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'Document boundary',
      safetyNotice: loanBoundaryEn,
    },
    loanFaq: {
      eyebrow: 'Loans',
      title: 'Loan FAQ',
      subtitle:
        'Loan frequently asked questions for applying, decision factors, repayment changes, interest rate, and collateral boundaries.',
      badge: 'FAQ concept',
      primaryPanelEyebrow: 'Frequently asked questions',
      primaryPanelTitle: 'Loan guidance',
      items: [
        { label: 'How to apply for a loan', value: 'Use a bank-approved channel', note: 'This prototype does not submit applications.' },
        { label: 'What affects loan decision', value: 'Income, expenses, credit history', note: 'No real decision model is used.' },
        { label: 'Interest rate', value: 'Bank-specific and customer-specific', note: 'No real rate is quoted.' },
      ],
      secondaryPanelEyebrow: 'Responsible lending boundary',
      secondaryPanelTitle: 'Key notices',
      rows: [
        { title: 'Repayment changes', detail: 'Real changes require bank review and approval.', status: 'Information' },
        { title: 'Digital assets as collateral', detail: 'Digital assets are not collateral in this prototype.', status: 'Not accepted' },
        { title: 'No real lending', detail: 'No loan, offer, or decision is created.', status: 'No real lending' },
      ],
      summaryTitle: 'FAQ summary',
      summaryItems: [
        { label: 'Collateral', value: 'Digital assets not accepted' },
        { label: 'Credit decision', value: 'None' },
        { label: 'Lending', value: 'No real lending' },
      ],
      actionLabel: 'Contact support simulation',
      actionNote: 'No support request or banking message is sent.',
      riskTitle: 'No real lending',
      riskNotice: loanBoundaryEn,
      safetyTitle: 'FAQ boundary',
      safetyNotice: loanBoundaryEn,
    },
  },
}

const loanDemoEs: LoanDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealLoanOperation: 'Sin operación real de préstamo',
    noRealCreditDecision: 'Sin decisión crediticia real',
  },
  pages: {
    loans: {
      eyebrow: 'Préstamos',
      title: 'Préstamos',
      subtitle:
        'Resumen bancario de servicios de préstamo simulados, estado de préstamo activo, estado de solicitud, información de pago y límites de seguridad.',
      badge: 'Concepto de préstamos',
      primaryPanelEyebrow: 'Resumen de préstamos',
      primaryPanelTitle: 'Posición de préstamo simulada',
      items: [
        { label: 'Saldo pendiente total simulado', value: '185.240,00 EUR', note: 'Importe demo estático.' },
        { label: 'Préstamo simulado activo', value: 'Concepto de préstamo hipotecario', note: 'No existe una cuenta de crédito real.' },
        { label: 'Próximo pago placeholder', value: '15.07.2026', note: 'Fecha de pago ilustrativa.' },
      ],
      secondaryPanelEyebrow: 'Servicios de préstamo disponibles',
      secondaryPanelTitle: 'Servicios y estado',
      rows: [
        { title: 'Resumen de préstamos', detail: 'Revisar saldos simulados de préstamo hipotecario, consumo y estudiantil.', status: 'Simulado' },
        { title: 'Estado de solicitud placeholder', detail: 'No hay una solicitud activa ni enviada.', status: 'Sin solicitud real' },
        { title: 'Resumen de pago', detail: 'La información de cuotas próximas es estática.', status: 'Estimación de prototipo' },
      ],
      summaryTitle: 'Resumen de préstamos',
      summaryItems: [
        { label: 'Préstamos activos', value: '1 simulado' },
        { label: 'Estado de solicitud', value: 'Placeholder' },
        { label: 'Decisión crediticia', value: 'Ninguna' },
      ],
      actionLabel: 'Abrir servicios de préstamo',
      actionNote: 'Este control deshabilitado representa navegación. No se ejecuta ningún servicio de préstamo.',
      riskTitle: 'Nota de seguridad',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite del prototipo',
      safetyNotice: loanBoundaryEs,
    },
    overview: {
      eyebrow: 'Préstamos',
      title: 'Resumen de préstamos',
      subtitle:
        'Resumen simulado de préstamo hipotecario, crédito de consumo, préstamo estudiantil, estado de pago, próximo pago e importe pendiente total.',
      badge: 'Concepto de resumen',
      primaryPanelEyebrow: 'Saldo pendiente',
      primaryPanelTitle: 'Vista de cartera de préstamos',
      items: [
        { label: 'Préstamo hipotecario', value: '178.500,00 EUR', note: 'Saldo hipotecario estático.' },
        { label: 'Crédito de consumo', value: '0,00 EUR', note: 'Sin crédito de consumo activo en la demo.' },
        { label: 'Préstamo estudiantil', value: '6.740,00 EUR', note: 'Saldo estudiantil estático.' },
      ],
      secondaryPanelEyebrow: 'Estado de pago',
      secondaryPanelTitle: 'Resumen de estado',
      rows: [
        { title: 'Cuota hipotecaria', detail: 'Próximo pago placeholder 15.07.2026.', status: 'Programado' },
        { title: 'Cuota de préstamo estudiantil', detail: 'Plan de pago mostrado solo para demostración.', status: 'Simulado' },
        { title: 'Saldo pendiente total simulado', detail: '185.240,00 EUR en filas demo de préstamos.', status: 'Estimación de prototipo' },
      ],
      summaryTitle: 'Resumen general',
      summaryItems: [
        { label: 'Saldo pendiente total', value: '185.240,00 EUR' },
        { label: 'Próximo pago', value: '15.07.2026' },
        { label: 'Estado de pago', value: 'Simulado' },
      ],
      actionLabel: 'Revisar resumen simulado',
      actionNote: 'No se realiza ninguna consulta real de saldo u operación de cuenta de préstamo.',
      riskTitle: 'Sin datos reales de préstamo',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de datos',
      safetyNotice: loanBoundaryEs,
    },
    application: {
      eyebrow: 'Préstamos',
      title: 'Solicitar préstamo',
      subtitle:
        'Flujo simulado de solicitud con tipo de préstamo, importe, plazo de pago, revisión de ingresos y gastos, y estado de revisión.',
      badge: 'Borrador de solicitud',
      primaryPanelEyebrow: 'Detalles de solicitud',
      primaryPanelTitle: 'Formulario de solicitud',
      items: [
        { label: 'Tipo de préstamo', value: 'Concepto de crédito de consumo', note: 'Selección visual únicamente.' },
        { label: 'Importe', value: '10.000,00 EUR', note: 'Importe solicitado estático.' },
        { label: 'Plazo de pago', value: '48 meses', note: 'No se guarda ningún plazo.' },
      ],
      secondaryPanelEyebrow: 'Revisión de ingresos y gastos',
      secondaryPanelTitle: 'Estado de revisión de solicitud',
      rows: [
        { title: 'Placeholder de ingresos', detail: 'No se recopilan ni evalúan datos de ingresos.', status: 'No enviado' },
        { title: 'Placeholder de gastos', detail: 'La capacidad de pago no se calcula con un modelo real.', status: 'Sin scoring real' },
        { title: 'Estado de revisión', detail: 'La solicitud permanece local y deshabilitada.', status: 'Borrador' },
      ],
      summaryTitle: 'Resumen de solicitud',
      summaryItems: [
        { label: 'Tipo de préstamo', value: 'Crédito de consumo' },
        { label: 'Envío', value: 'Deshabilitado' },
        { label: 'Decisión crediticia', value: 'Ninguna' },
      ],
      actionLabel: 'Enviar solicitud simulada',
      actionNote: 'El control de envío está deshabilitado. No se envía ninguna solicitud real de préstamo.',
      riskTitle: 'Sin solicitud real de préstamo',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de solicitud',
      safetyNotice: loanBoundaryEs,
    },
    mortgage: {
      eyebrow: 'Préstamos',
      title: 'Préstamo hipotecario',
      subtitle:
        'Página hipotecaria simulada con resumen de préstamo, garantía placeholder, tipo de interés placeholder, plazo y revisión de capacidad de pago.',
      badge: 'Concepto hipotecario',
      primaryPanelEyebrow: 'Resumen de préstamo hipotecario',
      primaryPanelTitle: 'Detalles hipotecarios',
      items: [
        { label: 'Resumen de préstamo hipotecario', value: '178.500,00 EUR', note: 'Saldo pendiente estático.' },
        { label: 'Tipo de interés placeholder', value: 'Concepto variable', note: 'Sin precio ni tasa de referencia real.' },
        { label: 'Plazo de pago', value: '22 años restantes', note: 'Plazo ilustrativo.' },
      ],
      secondaryPanelEyebrow: 'Garantía y capacidad de pago',
      secondaryPanelTitle: 'Placeholders de revisión',
      rows: [
        { title: 'Garantía placeholder', detail: 'No se realiza valoración de inmueble o garantía.', status: 'Placeholder' },
        { title: 'Revisión de capacidad de pago', detail: 'La capacidad de pago no se evalúa con un modelo real.', status: 'Simulado' },
        { title: 'Decisión hipotecaria', detail: 'No se emite ninguna decisión hipotecaria real.', status: 'Sin decisión real' },
      ],
      summaryTitle: 'Resumen hipotecario',
      summaryItems: [
        { label: 'Saldo pendiente', value: '178.500,00 EUR' },
        { label: 'Tipo de interés', value: 'Placeholder' },
        { label: 'Evaluación de garantía', value: 'Ninguna' },
      ],
      actionLabel: 'Revisar simulación hipotecaria',
      actionNote: 'No se cambian condiciones hipotecarias, garantías ni planes de pago.',
      riskTitle: 'Sin decisión hipotecaria real',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite hipotecario',
      safetyNotice: loanBoundaryEs,
    },
    consumerLoan: {
      eyebrow: 'Préstamos',
      title: 'Crédito de consumo',
      subtitle:
        'Página simulada de crédito de consumo con importe, plazo de pago, cuota mensual placeholder y aviso de riesgo y capacidad de pago.',
      badge: 'Concepto de crédito',
      primaryPanelEyebrow: 'Detalles de crédito de consumo',
      primaryPanelTitle: 'Importe y plazo',
      items: [
        { label: 'Importe del préstamo', value: '10.000,00 EUR', note: 'Importe ejemplo estático.' },
        { label: 'Plazo de pago', value: '48 meses', note: 'Plazo visual.' },
        { label: 'Cuota mensual', value: '230,00 EUR', note: 'Estimación, no oferta.' },
      ],
      secondaryPanelEyebrow: 'Aviso de riesgo y capacidad de pago',
      secondaryPanelTitle: 'Controles de revisión',
      rows: [
        { title: 'Aviso de capacidad de pago', detail: 'No se procesan ingresos, gastos ni datos crediticios.', status: 'Requerido' },
        { title: 'Aviso de riesgo', detail: 'El endeudamiento puede aumentar el riesgo financiero.', status: 'Aviso' },
        { title: 'Ejecución crediticia', detail: 'No se concede crédito de consumo real.', status: 'Sin crédito real' },
      ],
      summaryTitle: 'Resumen de crédito de consumo',
      summaryItems: [
        { label: 'Cuota mensual', value: '230,00 EUR' },
        { label: 'Revisión de capacidad de pago', value: 'Placeholder' },
        { label: 'Estado crediticio', value: 'Sin crédito real' },
      ],
      actionLabel: 'Calcular simulación de consumo',
      actionNote: 'No se ejecuta ninguna solicitud real de crédito de consumo ni scoring crediticio.',
      riskTitle: 'Sin crédito de consumo real',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de crédito de consumo',
      safetyNotice: loanBoundaryEs,
    },
    studentLoan: {
      eyebrow: 'Préstamos',
      title: 'Préstamo estudiantil',
      subtitle:
        'Página simulada de préstamo estudiantil con saldo, placeholder de garantía/elegibilidad, próxima cuota y plan de pago.',
      badge: 'Concepto de préstamo estudiantil',
      primaryPanelEyebrow: 'Saldo de préstamo estudiantil',
      primaryPanelTitle: 'Saldo y cuota',
      items: [
        { label: 'Saldo de préstamo estudiantil', value: '6.740,00 EUR', note: 'Saldo demo estático.' },
        { label: 'Garantía/elegibilidad placeholder', value: 'No evaluada', note: 'No se usan datos reales de garantía.' },
        { label: 'Próxima cuota', value: '125,00 EUR', note: 'Pago ilustrativo.' },
      ],
      secondaryPanelEyebrow: 'Plan de pago',
      secondaryPanelTitle: 'Estado del plan',
      rows: [
        { title: 'Plan de pago', detail: 'Calendario mostrado como filas simuladas.', status: 'Simulado' },
        { title: 'Elegibilidad placeholder', detail: 'No se realiza comprobación de elegibilidad.', status: 'Placeholder' },
        { title: 'Datos de préstamo estudiantil', detail: 'No se conecta ningún registro real.', status: 'Sin datos reales' },
      ],
      summaryTitle: 'Resumen de préstamo estudiantil',
      summaryItems: [
        { label: 'Saldo', value: '6.740,00 EUR' },
        { label: 'Próxima cuota', value: '125,00 EUR' },
        { label: 'Elegibilidad', value: 'Placeholder' },
      ],
      actionLabel: 'Revisar simulación estudiantil',
      actionNote: 'No se crea ningún dato real, garantía o cambio de pago de préstamo estudiantil.',
      riskTitle: 'Sin datos reales de préstamo estudiantil',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de préstamo estudiantil',
      safetyNotice: loanBoundaryEs,
    },
    loanCalculator: {
      eyebrow: 'Préstamos',
      title: 'Calculadora de préstamo',
      subtitle:
        'Calculadora simulada con visual de importe, visual de plazo de pago, interés placeholder y cuota mensual estimada.',
      badge: 'Concepto de calculadora',
      primaryPanelEyebrow: 'Entradas de calculadora',
      primaryPanelTitle: 'Estimación de préstamo',
      items: [
        { label: 'Importe visual', value: '25.000,00 EUR', note: 'Entrada estática.' },
        { label: 'Plazo de pago visual', value: '60 meses', note: 'Plazo estático.' },
        { label: 'Interés placeholder', value: '4,50%', note: 'No es una tasa u oferta real.' },
      ],
      secondaryPanelEyebrow: 'Cuota mensual estimada',
      secondaryPanelTitle: 'Resultado simulado',
      rows: [
        { title: 'Cuota mensual estimada', detail: '466,00 EUR, simulada y redondeada.', status: 'Estimación de prototipo' },
        { title: 'Asesoría financiera', detail: 'Esta calculadora no proporciona asesoría financiera.', status: 'Sin asesoría' },
        { title: 'Oferta crediticia', detail: 'No se produce tasa, oferta o decisión vinculante.', status: 'Sin oferta' },
      ],
      summaryTitle: 'Resumen de calculadora',
      summaryItems: [
        { label: 'Importe', value: '25.000,00 EUR' },
        { label: 'Plazo', value: '60 meses' },
        { label: 'Cuota mensual', value: '466,00 EUR' },
      ],
      actionLabel: 'Ejecutar cálculo simulado',
      actionNote: 'No se ejecuta ningún cálculo real, evaluación de capacidad de pago o asesoría.',
      riskTitle: 'Sin asesoría financiera',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de calculadora',
      safetyNotice: loanBoundaryEs,
    },
    repaymentPlan: {
      eyebrow: 'Préstamos',
      title: 'Plan de pago',
      subtitle:
        'Plan de pago simulado con próximas cuotas, fecha de pago, principal, interés y saldo pendiente.',
      badge: 'Concepto de pago',
      primaryPanelEyebrow: 'Próximas cuotas',
      primaryPanelTitle: 'Calendario de pagos',
      items: [
        { label: 'Fecha de pago', value: '15.07.2026', note: 'Cuota próxima estática.' },
        { label: 'Principal', value: '520,00 EUR', note: 'Importe ilustrativo.' },
        { label: 'Interés', value: '185,00 EUR', note: 'Importe de interés ilustrativo.' },
      ],
      secondaryPanelEyebrow: 'Saldo pendiente',
      secondaryPanelTitle: 'Filas de cuotas',
      rows: [
        { title: 'Cuota 15.07.2026', detail: 'Principal 520,00 EUR, interés 185,00 EUR, saldo 184.720,00 EUR.', status: 'Programado' },
        { title: 'Cuota 15.08.2026', detail: 'Principal 522,00 EUR, interés 183,00 EUR, saldo 184.198,00 EUR.', status: 'Simulado' },
        { title: 'Cambios de pago', detail: 'No se crean cambios reales de pago.', status: 'Sin cambio real' },
      ],
      summaryTitle: 'Resumen del plan',
      summaryItems: [
        { label: 'Próximas cuotas', value: '2 mostradas' },
        { label: 'Saldo pendiente', value: '184.720,00 EUR' },
        { label: 'Cambios', value: 'Ninguno' },
      ],
      actionLabel: 'Solicitar cambio de pago simulado',
      actionNote: 'No se envía ni registra ninguna solicitud de cambio de pago.',
      riskTitle: 'Sin cambios reales de pago',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite de pago',
      safetyNotice: loanBoundaryEs,
    },
    documents: {
      eyebrow: 'Préstamos',
      title: 'Documentos del préstamo',
      subtitle:
        'Área simulada para acuerdo de préstamo, calendario de pagos, certificado de intereses y extracto anual.',
      badge: 'Concepto de documentos',
      primaryPanelEyebrow: 'Lista de documentos',
      primaryPanelTitle: 'Documentos simulados disponibles',
      items: [
        { label: 'Acuerdo de préstamo', value: 'Concepto PDF', note: 'Entrada de documento simulada.' },
        { label: 'Calendario de pagos', value: 'Concepto PDF', note: 'Calendario de pago simulado.' },
        { label: 'Certificado de intereses', value: 'Concepto PDF', note: 'Certificado simulado.' },
      ],
      secondaryPanelEyebrow: 'Estado de documentos',
      secondaryPanelTitle: 'Archivo documental',
      rows: [
        { title: 'Extracto anual', detail: 'Extracto ficticio para visualización de prototipo.', status: 'Simulado' },
        { title: 'Acuerdo de préstamo', detail: 'Solo metadatos, sin contrato real.', status: 'Sin documento real' },
        { title: 'Calendario de pagos', detail: 'Calendario ilustrativo, no generado por un banco.', status: 'Estimación de prototipo' },
      ],
      summaryTitle: 'Resumen documental',
      summaryItems: [
        { label: 'Documentos', value: '4 simulados' },
        { label: 'Contratos reales', value: 'Ninguno' },
        { label: 'Descarga', value: 'Deshabilitada' },
      ],
      actionLabel: 'Abrir documento simulado',
      actionNote: 'No se abre, genera ni descarga ningún documento real.',
      riskTitle: 'Documentos marcados como simulados',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite documental',
      safetyNotice: loanBoundaryEs,
    },
    loanFaq: {
      eyebrow: 'Préstamos',
      title: 'Preguntas frecuentes de préstamos',
      subtitle:
        'Preguntas frecuentes sobre cómo solicitar, factores de decisión, cambios de pago, tasa de interés y límites de garantía.',
      badge: 'Concepto FAQ',
      primaryPanelEyebrow: 'Preguntas frecuentes',
      primaryPanelTitle: 'Guía de préstamos',
      items: [
        { label: 'Cómo solicitar un préstamo', value: 'Usar un canal aprobado por el banco', note: 'Este prototipo no envía solicitudes.' },
        { label: 'Qué afecta una decisión de préstamo', value: 'Ingresos, gastos e historial crediticio', note: 'No se usa un modelo real de decisión.' },
        { label: 'Tasa de interés', value: 'Específica del banco y del cliente', note: 'No se cotiza ninguna tasa real.' },
      ],
      secondaryPanelEyebrow: 'Límite de préstamo responsable',
      secondaryPanelTitle: 'Avisos clave',
      rows: [
        { title: 'Cambios de pago', detail: 'Los cambios reales requieren revisión y aprobación bancaria.', status: 'Información' },
        { title: 'Activos digitales como garantía', detail: 'Los activos digitales no son garantía en este prototipo.', status: 'No aceptados' },
        { title: 'Sin préstamo real', detail: 'No se crea préstamo, oferta o decisión.', status: 'Sin préstamo real' },
      ],
      summaryTitle: 'Resumen FAQ',
      summaryItems: [
        { label: 'Garantía', value: 'Activos digitales no aceptados' },
        { label: 'Decisión crediticia', value: 'Ninguna' },
        { label: 'Préstamo', value: 'Sin préstamo real' },
      ],
      actionLabel: 'Simular contacto con soporte',
      actionNote: 'No se envía una solicitud de soporte ni mensaje bancario.',
      riskTitle: 'Sin préstamo real',
      riskNotice: loanBoundaryEs,
      safetyTitle: 'Límite FAQ',
      safetyNotice: loanBoundaryEs,
    },
  },
}

type InsuranceDemoPageTranslation = LoanDemoPageTranslation

type InsuranceDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealInsuranceOperation: string
    noRealInsuranceContract: string
  }
  pages: Record<
    | 'insurance'
    | 'overview'
    | 'home'
    | 'travel'
    | 'life'
    | 'health'
    | 'claims'
    | 'documents'
    | 'insuranceFaq',
    InsuranceDemoPageTranslation
  >
}

const insuranceBoundaryEn =
  'Local deterministic prototype only. No real insurance policy, claim, underwriting decision, health data, contract, coverage, or banking or insurance operation is created or executed. Digital assets are not insured by this prototype.'

const insuranceBoundaryEs =
  'Solo prototipo local determinístico. No se crea ni ejecuta ninguna póliza real, siniestro, decisión de suscripción, dato de salud, contrato, cobertura u operación bancaria o aseguradora. Los activos digitales no están asegurados por este prototipo.'

const insuranceDemoEn: InsuranceDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealInsuranceOperation: 'No real insurance operation',
    noRealInsuranceContract: 'No real insurance contract',
  },
  pages: {
    insurance: {
      eyebrow: 'Insurance',
      title: 'Insurance',
      subtitle:
        'Banking-style overview of simulated insurance products, claims status, documents, and safety boundaries.',
      badge: 'Insurance concept',
      primaryPanelEyebrow: 'Insurance summary',
      primaryPanelTitle: 'Simulated insurance position',
      items: [
        { label: 'Active simulated insurance products', value: '4 products', note: 'Home, travel, life, and health concepts.' },
        { label: 'Claims overview', value: '2 simulated claims', note: 'No real claim is submitted.' },
        { label: 'Document status', value: 'Simulated archive', note: 'No real policy documents exist.' },
      ],
      secondaryPanelEyebrow: 'Product status',
      secondaryPanelTitle: 'Insurance services',
      rows: [
        { title: 'Home insurance concept', detail: 'Coverage overview and renewal placeholder.', status: 'Simulated' },
        { title: 'Travel insurance concept', detail: 'Trip coverage and assistance notice.', status: 'Simulated' },
        { title: 'Claims and documents', detail: 'Claim rows and document entries are local prototype data.', status: 'No real claim' },
      ],
      summaryTitle: 'Insurance summary',
      summaryItems: [
        { label: 'Products', value: '4 simulated' },
        { label: 'Open claims', value: '2 simulated' },
        { label: 'Contracts', value: 'None' },
      ],
      actionLabel: 'Open insurance services',
      actionNote: 'This disabled control represents navigation only. No insurance operation is executed.',
      riskTitle: 'Safety note',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Prototype boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    overview: {
      eyebrow: 'Insurance',
      title: 'Insurance overview',
      subtitle:
        'Simulated overview of home, travel, life, and health insurance with policy status and upcoming renewal placeholder.',
      badge: 'Overview concept',
      primaryPanelEyebrow: 'Product overview',
      primaryPanelTitle: 'Insurance products',
      items: [
        { label: 'Home insurance', value: 'Active concept', note: 'No real home policy.' },
        { label: 'Travel insurance', value: 'Annual concept', note: 'No real travel coverage.' },
        { label: 'Life and health insurance', value: 'Eligibility placeholders', note: 'No underwriting or medical assessment.' },
      ],
      secondaryPanelEyebrow: 'Policy status',
      secondaryPanelTitle: 'Renewals and notices',
      rows: [
        { title: 'Home insurance renewal', detail: 'Upcoming renewal placeholder 01.09.2026.', status: 'Renewal' },
        { title: 'Travel insurance status', detail: 'Destination region is not evaluated.', status: 'Simulated' },
        { title: 'Health insurance status', detail: 'No real health data or medical decision is processed.', status: 'No medical decision' },
      ],
      summaryTitle: 'Overview summary',
      summaryItems: [
        { label: 'Policy status', value: 'Simulated' },
        { label: 'Upcoming renewal', value: '01.09.2026' },
        { label: 'Coverage', value: 'No real coverage' },
      ],
      actionLabel: 'Review insurance overview',
      actionNote: 'No real policy inquiry or insurance provider operation is made.',
      riskTitle: 'No real coverage',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Data boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    home: {
      eyebrow: 'Insurance',
      title: 'Home insurance',
      subtitle:
        'Simulated home insurance page with coverage overview, property placeholder, deductible, renewal date, and claim reporting notice.',
      badge: 'Home concept',
      primaryPanelEyebrow: 'Coverage overview',
      primaryPanelTitle: 'Home insurance details',
      items: [
        { label: 'Coverage', value: 'Home and household concept', note: 'No real policy coverage.' },
        { label: 'Property information placeholder', value: 'Apartment concept', note: 'No real property data.' },
        { label: 'Deductible', value: '250.00 EUR', note: 'Illustrative deductible.' },
      ],
      secondaryPanelEyebrow: 'Renewal and claims',
      secondaryPanelTitle: 'Policy notices',
      rows: [
        { title: 'Renewal date', detail: 'Renewal placeholder 01.09.2026.', status: 'Renewal' },
        { title: 'Claim reporting notice', detail: 'Claim reporting is visual only.', status: 'No real claim' },
        { title: 'Policy execution', detail: 'No real home insurance policy is issued.', status: 'No real policy' },
      ],
      summaryTitle: 'Home insurance summary',
      summaryItems: [
        { label: 'Deductible', value: '250.00 EUR' },
        { label: 'Renewal', value: '01.09.2026' },
        { label: 'Policy', value: 'No real policy' },
      ],
      actionLabel: 'Report home claim simulation',
      actionNote: 'No real claim, coverage check, or policy change is submitted.',
      riskTitle: 'Sin póliza real',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Home insurance boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    travel: {
      eyebrow: 'Insurance',
      title: 'Travel insurance',
      subtitle:
        'Simulated travel insurance page with trip coverage, destination region placeholder, travel dates visual, and emergency assistance notice.',
      badge: 'Travel concept',
      primaryPanelEyebrow: 'Trip coverage',
      primaryPanelTitle: 'Travel insurance details',
      items: [
        { label: 'Trip coverage', value: 'Annual travel concept', note: 'No real coverage is issued.' },
        { label: 'Destination region placeholder', value: 'Nordic and EU concept', note: 'No destination risk evaluation.' },
        { label: 'Travel dates visual', value: '10.08.2026 - 24.08.2026', note: 'Illustrative dates.' },
      ],
      secondaryPanelEyebrow: 'Emergency assistance notice',
      secondaryPanelTitle: 'Travel support status',
      rows: [
        { title: 'Emergency assistance', detail: 'Assistance notice is simulated.', status: 'Information' },
        { title: 'Coverage issuance', detail: 'No real insurance coverage is issued.', status: 'No real coverage' },
        { title: 'Trip data', detail: 'No customer itinerary or travel data is stored.', status: 'No real data' },
      ],
      summaryTitle: 'Travel insurance summary',
      summaryItems: [
        { label: 'Region', value: 'Placeholder' },
        { label: 'Dates', value: 'Visual only' },
        { label: 'Coverage', value: 'No real coverage' },
      ],
      actionLabel: 'Open travel certificate simulation',
      actionNote: 'No certificate, coverage, or assistance case is created.',
      riskTitle: 'No real travel coverage',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Travel insurance boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    life: {
      eyebrow: 'Insurance',
      title: 'Life insurance',
      subtitle:
        'Simulated life insurance page with coverage amount placeholder, beneficiary review placeholder, eligibility status, and underwriting notice.',
      badge: 'Life concept',
      primaryPanelEyebrow: 'Coverage and eligibility',
      primaryPanelTitle: 'Life insurance details',
      items: [
        { label: 'Coverage amount placeholder', value: '100,000.00 EUR', note: 'No real insured amount.' },
        { label: 'Beneficiary review placeholder', value: 'Not reviewed', note: 'No beneficiary data is stored.' },
        { label: 'Eligibility status', value: 'Review placeholder', note: 'No real eligibility decision.' },
      ],
      secondaryPanelEyebrow: 'Underwriting review notice',
      secondaryPanelTitle: 'Contract status',
      rows: [
        { title: 'Underwriting review', detail: 'No real underwriting is performed.', status: 'No underwriting' },
        { title: 'Contract status', detail: 'No life insurance contract is created.', status: 'No real contract' },
        { title: 'Eligibility status', detail: 'Eligibility is visual placeholder data.', status: 'Placeholder' },
      ],
      summaryTitle: 'Life insurance summary',
      summaryItems: [
        { label: 'Coverage amount', value: 'Placeholder' },
        { label: 'Eligibility review', value: 'Placeholder' },
        { label: 'Contract', value: 'None' },
      ],
      actionLabel: 'Review eligibility simulation',
      actionNote: 'No real underwriting, beneficiary review, or contract action is executed.',
      riskTitle: 'No real underwriting or contract',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Life insurance boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    health: {
      eyebrow: 'Insurance',
      title: 'Health insurance',
      subtitle:
        'Simulated health insurance page with coverage overview, reimbursement categories, claim placeholder, and medical decision boundary.',
      badge: 'Health concept',
      primaryPanelEyebrow: 'Coverage overview',
      primaryPanelTitle: 'Health insurance details',
      items: [
        { label: 'Coverage overview', value: 'Supplemental concept', note: 'No real health coverage.' },
        { label: 'Reimbursement categories', value: 'Visit, medicine, therapy', note: 'Static category labels.' },
        { label: 'Claim submission placeholder', value: 'Disabled', note: 'No claim is submitted.' },
      ],
      secondaryPanelEyebrow: 'Health data boundary',
      secondaryPanelTitle: 'Medical review status',
      rows: [
        { title: 'Health data', detail: 'No real health or medical data is processed.', status: 'No health data' },
        { title: 'Medical decision', detail: 'No medical decision or assessment is performed.', status: 'No medical decision' },
        { title: 'Claim submission', detail: 'Claim submission is a placeholder only.', status: 'No real claim' },
      ],
      summaryTitle: 'Health insurance summary',
      summaryItems: [
        { label: 'Coverage', value: 'Simulated' },
        { label: 'Claims', value: 'Disabled' },
        { label: 'Medical decision', value: 'None' },
      ],
      actionLabel: 'Start claim simulation',
      actionNote: 'No real health claim, health data, or medical decision is created.',
      riskTitle: 'No real health data',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Health insurance boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    claims: {
      eyebrow: 'Insurance',
      title: 'Claims overview',
      subtitle:
        'Simulated claims page with received, under review, additional information required, and closed statuses.',
      badge: 'Claims concept',
      primaryPanelEyebrow: 'Claim list',
      primaryPanelTitle: 'Simulated claims',
      items: [
        { label: 'Received', value: 'CLM-2026-001', note: 'Fictional claim row.' },
        { label: 'Under review', value: 'CLM-2026-002', note: 'No real claim handling.' },
        { label: 'Additional information required', value: 'CLM-2026-003', note: 'No customer request is sent.' },
      ],
      secondaryPanelEyebrow: 'Claim status',
      secondaryPanelTitle: 'Claim lifecycle',
      rows: [
        { title: 'Home water damage concept', detail: 'Claim status received.', status: 'Received' },
        { title: 'Travel delay concept', detail: 'Claim status under review.', status: 'Under review' },
        { title: 'Closed claim concept', detail: 'Closed status is simulated.', status: 'Closed' },
      ],
      summaryTitle: 'Claims summary',
      summaryItems: [
        { label: 'Open claims', value: '2 simulated' },
        { label: 'Additional information', value: '1 placeholder' },
        { label: 'Real submissions', value: 'None' },
      ],
      actionLabel: 'Report a claim simulation',
      actionNote: 'The new claim control is disabled. No real claim is submitted.',
      riskTitle: 'No real claim submitted',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Claims boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    documents: {
      eyebrow: 'Insurance',
      title: 'Insurance documents',
      subtitle:
        'Simulated insurance documents area for policy document, claim decision, annual statement, and coverage certificate.',
      badge: 'Documents concept',
      primaryPanelEyebrow: 'Document list',
      primaryPanelTitle: 'Available simulated documents',
      items: [
        { label: 'Policy document', value: 'PDF concept', note: 'Simulated document entry.' },
        { label: 'Claim decision', value: 'PDF concept', note: 'No real claim decision.' },
        { label: 'Annual statement', value: 'PDF concept', note: 'Fictional annual statement.' },
      ],
      secondaryPanelEyebrow: 'Document status',
      secondaryPanelTitle: 'Document archive',
      rows: [
        { title: 'Coverage certificate', detail: 'Certificate entry is simulated.', status: 'Simulated' },
        { title: 'Policy document', detail: 'Document metadata only, no real contract.', status: 'No real document' },
        { title: 'Claim decision', detail: 'No claim decision is generated.', status: 'No real claim' },
      ],
      summaryTitle: 'Document summary',
      summaryItems: [
        { label: 'Documents', value: '4 simulated' },
        { label: 'Real contracts', value: 'None' },
        { label: 'Downloads', value: 'Disabled' },
      ],
      actionLabel: 'Open simulated document',
      actionNote: 'No real insurance document is opened, generated, or downloaded.',
      riskTitle: 'Documents marked as simulated',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'Document boundary',
      safetyNotice: insuranceBoundaryEn,
    },
    insuranceFaq: {
      eyebrow: 'Insurance',
      title: 'Insurance FAQ',
      subtitle:
        'Frequently asked questions about shown products, claims, coverage limits, deductibles, and digital asset insurance boundaries.',
      badge: 'FAQ concept',
      primaryPanelEyebrow: 'Frequently asked questions',
      primaryPanelTitle: 'Insurance guidance',
      items: [
        { label: 'What insurance products are shown', value: 'Home, travel, life, and health concepts', note: 'All products are simulated.' },
        { label: 'How claims work', value: 'Bank-style claim lifecycle display', note: 'No real claim handling.' },
        { label: 'Coverage limits and deductibles', value: 'Visual placeholders', note: 'No binding terms.' },
      ],
      secondaryPanelEyebrow: 'Coverage boundary',
      secondaryPanelTitle: 'Key notices',
      rows: [
        { title: 'Digital assets', detail: 'Digital assets are not insured by this prototype.', status: 'Not insured' },
        { title: 'No real insurance', detail: 'No policy, claim, coverage, or contract is created.', status: 'No real insurance' },
        { title: 'Coverage limits', detail: 'Coverage limit information is not a real insurance term.', status: 'Information' },
      ],
      summaryTitle: 'FAQ summary',
      summaryItems: [
        { label: 'Digital assets', value: 'Not insured' },
        { label: 'Claims', value: 'No real claims' },
        { label: 'Contracts', value: 'None' },
      ],
      actionLabel: 'Contact support simulation',
      actionNote: 'No support request or insurance message is sent.',
      riskTitle: 'No real insurance',
      riskNotice: insuranceBoundaryEn,
      safetyTitle: 'FAQ boundary',
      safetyNotice: insuranceBoundaryEn,
    },
  },
}

const insuranceDemoEs: InsuranceDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealInsuranceOperation: 'Sin operación real de seguro',
    noRealInsuranceContract: 'Sin contrato real de seguro',
  },
  pages: {
    insurance: {
      eyebrow: 'Seguros',
      title: 'Seguros',
      subtitle:
        'Resumen bancario de productos de seguro simulados, estado de siniestros, documentos y límites de seguridad.',
      badge: 'Concepto de seguros',
      primaryPanelEyebrow: 'Resumen de seguros',
      primaryPanelTitle: 'Posición de seguros simulada',
      items: [
        { label: 'Productos activos simulados', value: '4 productos', note: 'Conceptos de hogar, viaje, vida y salud.' },
        { label: 'Resumen de siniestros', value: '2 siniestros simulados', note: 'No se envía ningún siniestro real.' },
        { label: 'Estado documental', value: 'Archivo simulado', note: 'No existen documentos reales de póliza.' },
      ],
      secondaryPanelEyebrow: 'Estado de producto',
      secondaryPanelTitle: 'Servicios de seguros',
      rows: [
        { title: 'Concepto de seguro de hogar', detail: 'Resumen de cobertura y renovación placeholder.', status: 'Simulado' },
        { title: 'Concepto de seguro de viaje', detail: 'Cobertura de viaje y aviso de asistencia.', status: 'Simulado' },
        { title: 'Siniestros y documentos', detail: 'Filas de siniestros y documentos son datos locales.', status: 'Sin siniestro real' },
      ],
      summaryTitle: 'Resumen de seguros',
      summaryItems: [
        { label: 'Productos', value: '4 simulados' },
        { label: 'Siniestros abiertos', value: '2 simulados' },
        { label: 'Contratos', value: 'Ninguno' },
      ],
      actionLabel: 'Abrir servicios de seguros',
      actionNote: 'Este control deshabilitado representa navegación. No se ejecuta ninguna operación de seguro.',
      riskTitle: 'Nota de seguridad',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite del prototipo',
      safetyNotice: insuranceBoundaryEs,
    },
    overview: {
      eyebrow: 'Seguros',
      title: 'Resumen de seguros',
      subtitle:
        'Resumen simulado de seguro de hogar, viaje, vida y salud con estado de póliza y renovación placeholder.',
      badge: 'Concepto de resumen',
      primaryPanelEyebrow: 'Resumen de productos',
      primaryPanelTitle: 'Productos de seguro',
      items: [
        { label: 'Seguro de hogar', value: 'Concepto activo', note: 'Sin póliza real de hogar.' },
        { label: 'Seguro de viaje', value: 'Concepto anual', note: 'Sin cobertura real de viaje.' },
        { label: 'Seguro de vida y salud', value: 'Placeholders de elegibilidad', note: 'Sin suscripción ni evaluación médica real.' },
      ],
      secondaryPanelEyebrow: 'Estado de póliza',
      secondaryPanelTitle: 'Renovaciones y avisos',
      rows: [
        { title: 'Renovación de seguro de hogar', detail: 'Renovación placeholder 01.09.2026.', status: 'Renovación' },
        { title: 'Estado de seguro de viaje', detail: 'No se evalúa la región de destino.', status: 'Simulado' },
        { title: 'Estado de seguro de salud', detail: 'No se procesan datos de salud ni decisión médica.', status: 'Sin evaluación médica real' },
      ],
      summaryTitle: 'Resumen general',
      summaryItems: [
        { label: 'Estado de póliza', value: 'Simulado' },
        { label: 'Próxima renovación', value: '01.09.2026' },
        { label: 'Cobertura', value: 'Sin cobertura real' },
      ],
      actionLabel: 'Revisar resumen de seguros',
      actionNote: 'No se realiza ninguna consulta real de póliza u operación con aseguradora.',
      riskTitle: 'Sin cobertura real',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de datos',
      safetyNotice: insuranceBoundaryEs,
    },
    home: {
      eyebrow: 'Seguros',
      title: 'Seguro de hogar',
      subtitle:
        'Página simulada de seguro de hogar con cobertura, información de propiedad placeholder, deducible, renovación y aviso de siniestro.',
      badge: 'Concepto de hogar',
      primaryPanelEyebrow: 'Cobertura',
      primaryPanelTitle: 'Detalles del seguro de hogar',
      items: [
        { label: 'Cobertura', value: 'Concepto de hogar y contenido', note: 'Sin cobertura real de póliza.' },
        { label: 'Información de propiedad placeholder', value: 'Concepto de apartamento', note: 'Sin datos reales de propiedad.' },
        { label: 'Deducible', value: '250,00 EUR', note: 'Deducible ilustrativo.' },
      ],
      secondaryPanelEyebrow: 'Renovación y siniestros',
      secondaryPanelTitle: 'Avisos de póliza',
      rows: [
        { title: 'Fecha de renovación', detail: 'Renovación placeholder 01.09.2026.', status: 'Renovación' },
        { title: 'Aviso de reporte de siniestro', detail: 'El reporte de siniestro es solo visual.', status: 'Sin siniestro real' },
        { title: 'Ejecución de póliza', detail: 'No se emite ninguna póliza real de hogar.', status: 'Sin póliza real' },
      ],
      summaryTitle: 'Resumen de seguro de hogar',
      summaryItems: [
        { label: 'Deducible', value: '250,00 EUR' },
        { label: 'Renovación', value: '01.09.2026' },
        { label: 'Póliza', value: 'Sin póliza real' },
      ],
      actionLabel: 'Simular reporte de siniestro de hogar',
      actionNote: 'No se envía ningún siniestro, revisión de cobertura o cambio de póliza real.',
      riskTitle: 'Sin póliza real',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de seguro de hogar',
      safetyNotice: insuranceBoundaryEs,
    },
    travel: {
      eyebrow: 'Seguros',
      title: 'Seguro de viaje',
      subtitle:
        'Página simulada de seguro de viaje con cobertura de viaje, región de destino placeholder, fechas visuales y aviso de asistencia.',
      badge: 'Concepto de viaje',
      primaryPanelEyebrow: 'Cobertura de viaje',
      primaryPanelTitle: 'Detalles del seguro de viaje',
      items: [
        { label: 'Cobertura de viaje', value: 'Concepto anual de viaje', note: 'No se emite cobertura real.' },
        { label: 'Región de destino placeholder', value: 'Concepto Nórdico y UE', note: 'Sin evaluación de riesgo de destino.' },
        { label: 'Fechas de viaje visuales', value: '10.08.2026 - 24.08.2026', note: 'Fechas ilustrativas.' },
      ],
      secondaryPanelEyebrow: 'Aviso de asistencia de emergencia',
      secondaryPanelTitle: 'Estado de soporte de viaje',
      rows: [
        { title: 'Asistencia de emergencia', detail: 'El aviso de asistencia es simulado.', status: 'Información' },
        { title: 'Emisión de cobertura', detail: 'No se emite cobertura real de seguro.', status: 'Sin cobertura real' },
        { title: 'Datos de viaje', detail: 'No se guarda itinerario ni dato real de cliente.', status: 'Sin datos reales' },
      ],
      summaryTitle: 'Resumen de seguro de viaje',
      summaryItems: [
        { label: 'Región', value: 'Placeholder' },
        { label: 'Fechas', value: 'Solo visuales' },
        { label: 'Cobertura', value: 'Sin cobertura real' },
      ],
      actionLabel: 'Abrir certificado de viaje simulado',
      actionNote: 'No se crea certificado, cobertura o caso de asistencia.',
      riskTitle: 'Sin cobertura real de viaje',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de seguro de viaje',
      safetyNotice: insuranceBoundaryEs,
    },
    life: {
      eyebrow: 'Seguros',
      title: 'Seguro de vida',
      subtitle:
        'Página simulada de seguro de vida con importe de cobertura placeholder, revisión de beneficiario, elegibilidad y aviso de suscripción.',
      badge: 'Concepto de vida',
      primaryPanelEyebrow: 'Cobertura y elegibilidad',
      primaryPanelTitle: 'Detalles del seguro de vida',
      items: [
        { label: 'Importe de cobertura placeholder', value: '100.000,00 EUR', note: 'Sin importe real asegurado.' },
        { label: 'Revisión de beneficiario placeholder', value: 'No revisado', note: 'No se guarda dato de beneficiario.' },
        { label: 'Revisión de elegibilidad', value: 'Placeholder de revisión', note: 'Sin decisión real de elegibilidad.' },
      ],
      secondaryPanelEyebrow: 'Aviso de suscripción',
      secondaryPanelTitle: 'Estado contractual',
      rows: [
        { title: 'Revisión de suscripción', detail: 'No se realiza suscripción real.', status: 'Sin suscripción' },
        { title: 'Estado contractual', detail: 'No se crea contrato de seguro de vida.', status: 'Sin contrato real' },
        { title: 'Estado de elegibilidad', detail: 'La elegibilidad es dato visual placeholder.', status: 'Placeholder' },
      ],
      summaryTitle: 'Resumen de seguro de vida',
      summaryItems: [
        { label: 'Cobertura', value: 'Placeholder' },
        { label: 'Revisión de elegibilidad', value: 'Placeholder' },
        { label: 'Contrato', value: 'Ninguno' },
      ],
      actionLabel: 'Revisar elegibilidad simulada',
      actionNote: 'No se ejecuta suscripción real, revisión de beneficiario o acción contractual.',
      riskTitle: 'Sin suscripción ni contrato real',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de seguro de vida',
      safetyNotice: insuranceBoundaryEs,
    },
    health: {
      eyebrow: 'Seguros',
      title: 'Seguro de salud',
      subtitle:
        'Página simulada de seguro de salud con cobertura, categorías de reembolso, placeholder de siniestro y límite de decisión médica.',
      badge: 'Concepto de salud',
      primaryPanelEyebrow: 'Cobertura',
      primaryPanelTitle: 'Detalles del seguro de salud',
      items: [
        { label: 'Cobertura', value: 'Concepto complementario', note: 'Sin cobertura real de salud.' },
        { label: 'Categorías de reembolso', value: 'Consulta, medicamento, terapia', note: 'Etiquetas estáticas.' },
        { label: 'Placeholder de envío de siniestro', value: 'Deshabilitado', note: 'No se envía siniestro.' },
      ],
      secondaryPanelEyebrow: 'Límite de datos de salud',
      secondaryPanelTitle: 'Estado de revisión médica',
      rows: [
        { title: 'Datos de salud', detail: 'No se procesan datos reales de salud o médicos.', status: 'Sin datos de salud' },
        { title: 'Decisión médica', detail: 'No se realiza evaluación ni decisión médica.', status: 'Sin evaluación médica real' },
        { title: 'Envío de siniestro', detail: 'El envío de siniestro es solo placeholder.', status: 'Sin siniestro real' },
      ],
      summaryTitle: 'Resumen de seguro de salud',
      summaryItems: [
        { label: 'Cobertura', value: 'Simulada' },
        { label: 'Siniestros', value: 'Deshabilitados' },
        { label: 'Decisión médica', value: 'Ninguna' },
      ],
      actionLabel: 'Iniciar siniestro simulado',
      actionNote: 'No se crea siniestro real de salud, dato de salud ni decisión médica.',
      riskTitle: 'Sin datos reales de salud',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de seguro de salud',
      safetyNotice: insuranceBoundaryEs,
    },
    claims: {
      eyebrow: 'Seguros',
      title: 'Resumen de siniestros',
      subtitle:
        'Página simulada de siniestros con estados recibido, en revisión, información adicional requerida y cerrado.',
      badge: 'Concepto de siniestros',
      primaryPanelEyebrow: 'Lista de siniestros',
      primaryPanelTitle: 'Siniestros simulados',
      items: [
        { label: 'Recibido', value: 'CLM-2026-001', note: 'Fila ficticia de siniestro.' },
        { label: 'En revisión', value: 'CLM-2026-002', note: 'Sin gestión real de siniestro.' },
        { label: 'Información adicional requerida', value: 'CLM-2026-003', note: 'No se envía solicitud al cliente.' },
      ],
      secondaryPanelEyebrow: 'Estado de siniestro',
      secondaryPanelTitle: 'Ciclo de vida de siniestro',
      rows: [
        { title: 'Concepto de daño de agua en hogar', detail: 'Estado de siniestro recibido.', status: 'Recibido' },
        { title: 'Concepto de retraso de viaje', detail: 'Estado de siniestro en revisión.', status: 'En revisión' },
        { title: 'Concepto de siniestro cerrado', detail: 'Estado cerrado simulado.', status: 'Cerrado' },
      ],
      summaryTitle: 'Resumen de siniestros',
      summaryItems: [
        { label: 'Siniestros abiertos', value: '2 simulados' },
        { label: 'Información adicional', value: '1 placeholder' },
        { label: 'Envíos reales', value: 'Ninguno' },
      ],
      actionLabel: 'Reportar siniestro simulado',
      actionNote: 'El control de nuevo siniestro está deshabilitado. No se envía ningún siniestro real.',
      riskTitle: 'Sin siniestro real enviado',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite de siniestros',
      safetyNotice: insuranceBoundaryEs,
    },
    documents: {
      eyebrow: 'Seguros',
      title: 'Documentos del seguro',
      subtitle:
        'Área simulada de documentos para póliza, decisión de siniestro, extracto anual y certificado de cobertura.',
      badge: 'Concepto de documentos',
      primaryPanelEyebrow: 'Lista de documentos',
      primaryPanelTitle: 'Documentos simulados disponibles',
      items: [
        { label: 'Documento de póliza', value: 'Concepto PDF', note: 'Entrada de documento simulada.' },
        { label: 'Decisión de siniestro', value: 'Concepto PDF', note: 'Sin decisión real de siniestro.' },
        { label: 'Extracto anual', value: 'Concepto PDF', note: 'Extracto anual ficticio.' },
      ],
      secondaryPanelEyebrow: 'Estado documental',
      secondaryPanelTitle: 'Archivo documental',
      rows: [
        { title: 'Certificado de cobertura', detail: 'Entrada de certificado simulada.', status: 'Simulado' },
        { title: 'Documento de póliza', detail: 'Solo metadatos, sin contrato real.', status: 'Sin documento real' },
        { title: 'Decisión de siniestro', detail: 'No se genera decisión de siniestro.', status: 'Sin siniestro real' },
      ],
      summaryTitle: 'Resumen documental',
      summaryItems: [
        { label: 'Documentos', value: '4 simulados' },
        { label: 'Contratos reales', value: 'Ninguno' },
        { label: 'Descargas', value: 'Deshabilitadas' },
      ],
      actionLabel: 'Abrir documento simulado',
      actionNote: 'No se abre, genera ni descarga ningún documento real de seguro.',
      riskTitle: 'Documentos marcados como simulados',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite documental',
      safetyNotice: insuranceBoundaryEs,
    },
    insuranceFaq: {
      eyebrow: 'Seguros',
      title: 'Preguntas frecuentes de seguros',
      subtitle:
        'Preguntas frecuentes sobre productos mostrados, siniestros, límites de cobertura, deducibles y seguros de activos digitales.',
      badge: 'Concepto FAQ',
      primaryPanelEyebrow: 'Preguntas frecuentes',
      primaryPanelTitle: 'Guía de seguros',
      items: [
        { label: 'Qué productos de seguro se muestran', value: 'Conceptos de hogar, viaje, vida y salud', note: 'Todos los productos son simulados.' },
        { label: 'Cómo funcionan los siniestros', value: 'Vista bancaria del ciclo de vida', note: 'Sin gestión real de siniestros.' },
        { label: 'Límites de cobertura y deducibles', value: 'Placeholders visuales', note: 'Sin términos vinculantes.' },
      ],
      secondaryPanelEyebrow: 'Límite de cobertura',
      secondaryPanelTitle: 'Avisos clave',
      rows: [
        { title: 'Activos digitales', detail: 'Los activos digitales no están asegurados por este prototipo.', status: 'No asegurados' },
        { title: 'Sin seguro real', detail: 'No se crea póliza, siniestro, cobertura o contrato.', status: 'Sin seguro real' },
        { title: 'Límites de cobertura', detail: 'La información de cobertura no es un término real de seguro.', status: 'Información' },
      ],
      summaryTitle: 'Resumen FAQ',
      summaryItems: [
        { label: 'Activos digitales', value: 'No asegurados' },
        { label: 'Siniestros', value: 'Sin siniestros reales' },
        { label: 'Contratos', value: 'Ninguno' },
      ],
      actionLabel: 'Simular contacto con soporte',
      actionNote: 'No se envía una solicitud de soporte ni mensaje de seguro.',
      riskTitle: 'Sin seguro real',
      riskNotice: insuranceBoundaryEs,
      safetyTitle: 'Límite FAQ',
      safetyNotice: insuranceBoundaryEs,
    },
  },
}

type InvestmentDemoTranslations = {
  common: {
    reviewSummary: string
    simulatedAction: string
    localPrototype: string
    noRealInvestmentExecution: string
  }
  pages: Record<
    | 'overview'
    | 'funds'
    | 'stocks'
    | 'accounts'
    | 'trading'
    | 'custodyAccounts'
    | 'prices'
    | 'marketNews'
    | 'research'
    | 'investmentFaq'
    | 'riskInformation',
    InvestmentDemoPageTranslation
  >
}

const investmentBoundaryEn =
  'Local deterministic prototype only. No real investment account, trading order, custody service, market data feed, investment advice, or banking operation is created or executed.'

const investmentBoundaryEs =
  'Solo prototipo local determinístico. No se crea ni ejecuta ninguna cuenta de inversión real, orden de trading, servicio de custodia, feed de datos de mercado, asesoría de inversión u operación bancaria.'

const investmentDemoEn: InvestmentDemoTranslations = {
  common: {
    reviewSummary: 'Review summary',
    simulatedAction: 'Simulated action',
    localPrototype: 'Local deterministic prototype',
    noRealInvestmentExecution: 'No real investment execution',
  },
  pages: {
    overview: {
      eyebrow: 'Investments',
      title: 'Investment overview',
      subtitle:
        'Simulated investment overview with portfolio summary, allocation placeholder, account status, recent activity, and risk notice.',
      badge: 'Portfolio concept',
      primaryPanelEyebrow: 'Portfolio summary',
      primaryPanelTitle: 'Investment portfolio',
      items: [
        { label: 'Portfolio value', value: '24,680.00 EUR', note: 'Static demo value, not portfolio data.' },
        { label: 'Asset allocation', value: 'Funds 60% · Stocks 30% · Cash 10%', note: 'Allocation placeholder only.' },
        { label: 'Investment account status', value: 'Active concept', note: 'No real account connection.' },
      ],
      secondaryPanelEyebrow: 'Recent simulated activity',
      secondaryPanelTitle: 'Activity and controls',
      rows: [
        { title: 'Monthly fund saving prepared', detail: 'Visual activity row, no subscription placed.', status: 'Simulated' },
        { title: 'Portfolio review reminder', detail: 'Risk review reminder for demonstration only.', status: 'Notice' },
        { title: 'Digital asset boundary confirmed', detail: 'Digital assets remain separate from deposits and investment products.', status: 'Risk notice' },
      ],
      summaryTitle: 'Overview summary',
      summaryItems: [
        { label: 'Portfolio data', value: 'Simulated' },
        { label: 'Investment advice', value: 'None' },
        { label: 'Execution', value: 'None' },
      ],
      actionLabel: 'Refresh overview simulation',
      actionNote: 'No real portfolio data or market data is requested.',
      riskTitle: 'Risk notice',
      riskNotice:
        'Investments can lose value. This page does not provide investment advice, recommendations, or real portfolio information.',
      safetyTitle: 'Investment boundary',
      safetyNotice: investmentBoundaryEn,
    },
    funds: {
      eyebrow: 'Investments',
      title: 'Funds',
      subtitle:
        'Simulated funds page with fund list, risk level, monthly saving option visual, and sustainability/profile placeholders.',
      badge: 'Fund concept',
      primaryPanelEyebrow: 'Fund list',
      primaryPanelTitle: 'Available fund concepts',
      items: [
        { label: 'Aurora Nordic Balanced Fund', value: 'Risk level 3/7', note: 'Fund concept, not a recommendation.' },
        { label: 'Aurora Global Index Fund', value: 'Risk level 4/7', note: 'Static fund row.' },
        { label: 'Monthly saving option', value: '100.00 EUR visual amount', note: 'No monthly saving order is created.' },
        { label: 'Sustainability/profile', value: 'Placeholder profile', note: 'No suitability assessment is performed.' },
      ],
      secondaryPanelEyebrow: 'Fund controls',
      secondaryPanelTitle: 'Subscription boundary',
      rows: [
        { title: 'Risk level visible', detail: 'Risk labels are static educational placeholders.', status: 'Notice' },
        { title: 'Monthly saving visual', detail: 'Monthly saving is shown but not activated.', status: 'Simulated' },
        { title: 'Fund subscription', detail: 'No real fund subscription is submitted.', status: 'Blocked' },
      ],
      summaryTitle: 'Fund summary',
      summaryItems: [
        { label: 'Fund rows', value: '2 simulated' },
        { label: 'Advice', value: 'None' },
        { label: 'Subscription', value: 'None' },
      ],
      actionLabel: 'Subscribe simulation',
      actionNote: 'Button is disabled because no real fund subscription is submitted.',
      riskTitle: 'Fund risk notice',
      riskNotice:
        'Fund values can rise or fall. This prototype does not assess suitability or recommend any fund.',
      safetyTitle: 'Fund boundary',
      safetyNotice: investmentBoundaryEn,
    },
    stocks: {
      eyebrow: 'Investments',
      title: 'Stocks',
      subtitle:
        'Simulated stocks page with watchlist, market status, static price rows, and disabled buy/sell simulation buttons.',
      badge: 'Watchlist concept',
      primaryPanelEyebrow: 'Stock watchlist',
      primaryPanelTitle: 'Simulated price rows',
      items: [
        { label: 'Aurora Industrial Oyj', value: '42.10 EUR', note: 'Static simulated price.' },
        { label: 'Nordic Utilities Plc', value: '18.45 EUR', note: 'Static simulated price.' },
        { label: 'Market status', value: 'Open concept', note: 'No real market status feed.' },
      ],
      secondaryPanelEyebrow: 'Trading controls',
      secondaryPanelTitle: 'Disabled trade actions',
      rows: [
        { title: 'Buy button', detail: 'Shown as simulation only.', status: 'Disabled' },
        { title: 'Sell button', detail: 'Shown as simulation only.', status: 'Disabled' },
        { title: 'Market prices', detail: 'No real market data is loaded.', status: 'Simulated' },
      ],
      summaryTitle: 'Stock summary',
      summaryItems: [
        { label: 'Watchlist', value: '2 instruments' },
        { label: 'Market data', value: 'Static' },
        { label: 'Trading', value: 'None' },
      ],
      actionLabel: 'Open trade simulation',
      actionNote: 'No real buy or sell order can be placed.',
      riskTitle: 'Market risk notice',
      riskNotice:
        'Stock prices can fluctuate and losses are possible. Static rows are not real market prices.',
      safetyTitle: 'Trading boundary',
      safetyNotice: investmentBoundaryEn,
    },
    accounts: {
      eyebrow: 'Investments',
      title: 'Investment accounts',
      subtitle:
        'Simulated investment accounts with investment account, custody account, tax wrapper placeholder, and account status.',
      badge: 'Account concept',
      primaryPanelEyebrow: 'Investment account',
      primaryPanelTitle: 'Account structure',
      items: [
        { label: 'Investment account', value: 'Aurora Investment Account', note: 'Static account concept.' },
        { label: 'Custody account', value: 'Securities custody concept', note: 'No custody execution.' },
        { label: 'Tax wrapper/account type', value: 'Placeholder account type', note: 'No tax advice.' },
      ],
      secondaryPanelEyebrow: 'Account status',
      secondaryPanelTitle: 'Opening boundary',
      rows: [
        { title: 'Account status', detail: 'Account shown as active concept only.', status: 'Simulated' },
        { title: 'Opening workflow', detail: 'No real investment account opening exists.', status: 'Blocked' },
        { title: 'Customer data', detail: 'No real customer data is used.', status: 'No real data' },
      ],
      summaryTitle: 'Account summary',
      summaryItems: [
        { label: 'Investment account', value: 'Simulated' },
        { label: 'Custody account', value: 'Simulated' },
        { label: 'Real opening', value: 'None' },
      ],
      actionLabel: 'Open account simulation',
      actionNote: 'No real investment account is opened.',
      riskTitle: 'Account risk notice',
      riskNotice:
        'Investment accounts can involve market and custody risks. This page is informational only.',
      safetyTitle: 'Account boundary',
      safetyNotice: investmentBoundaryEn,
    },
    trading: {
      eyebrow: 'Trading and custody',
      title: 'Trading',
      subtitle:
        'Simulated trading page with order ticket visual, instrument search placeholder, order type, estimated cost, and compliance/risk pre-check.',
      badge: 'Order ticket concept',
      primaryPanelEyebrow: 'Order ticket',
      primaryPanelTitle: 'Trade simulation',
      items: [
        { label: 'Instrument search', value: 'Aurora Industrial Oyj', note: 'Search placeholder only.' },
        { label: 'Order type', value: 'Limit order concept', note: 'No order is submitted.' },
        { label: 'Estimated cost', value: '421.00 EUR', note: 'Static estimate, not a quote.' },
      ],
      secondaryPanelEyebrow: 'Pre-check',
      secondaryPanelTitle: 'Compliance and risk controls',
      rows: [
        { title: 'Compliance pre-check', detail: 'Pre-check is represented as deterministic UI state.', status: 'Required' },
        { title: 'Risk acknowledgement', detail: 'Risk notice would be required before a real order.', status: 'Required' },
        { title: 'Order execution', detail: 'Order submission is disabled.', status: 'Blocked' },
      ],
      summaryTitle: 'Order summary',
      summaryItems: [
        { label: 'Instrument', value: 'Aurora Industrial Oyj' },
        { label: 'Order type', value: 'Limit concept' },
        { label: 'Real order', value: 'None' },
      ],
      actionLabel: 'Submit order simulation',
      actionNote: 'Button is disabled because no real order execution occurs.',
      riskTitle: 'Trading risk notice',
      riskNotice:
        'Trading can result in loss. This order ticket is not a recommendation, quote, or execution path.',
      safetyTitle: 'Order boundary',
      safetyNotice: investmentBoundaryEn,
    },
    custodyAccounts: {
      eyebrow: 'Trading and custody',
      title: 'Custody accounts',
      subtitle:
        'Simulated custody accounts page with securities custody account, digital asset custody boundary, status, and reconciliation placeholder.',
      badge: 'Custody concept',
      primaryPanelEyebrow: 'Custody accounts',
      primaryPanelTitle: 'Custody structure',
      items: [
        { label: 'Securities custody account', value: 'Aurora Securities Custody', note: 'Static custody concept.' },
        { label: 'Digital asset custody boundary', value: 'Separate from securities custody', note: 'No custodian integration.' },
        { label: 'Account status', value: 'Active concept', note: 'No real custody service.' },
      ],
      secondaryPanelEyebrow: 'Audit and reconciliation',
      secondaryPanelTitle: 'Control placeholders',
      rows: [
        { title: 'Reconciliation placeholder', detail: 'Reconciliation evidence is visual only.', status: 'Simulated' },
        { title: 'Audit placeholder', detail: 'Audit trail rows are deterministic copy.', status: 'Ready' },
        { title: 'Custody execution', detail: 'No real custody operation is executed.', status: 'Blocked' },
      ],
      summaryTitle: 'Custody summary',
      summaryItems: [
        { label: 'Securities custody', value: 'Simulated' },
        { label: 'Digital asset custody', value: 'Separate boundary' },
        { label: 'Real execution', value: 'None' },
      ],
      actionLabel: 'Review custody simulation',
      actionNote: 'No custody service or reconciliation job is executed.',
      riskTitle: 'Custody risk notice',
      riskNotice:
        'Custody services involve operational and legal risks. This page does not represent a real custodian integration.',
      safetyTitle: 'Custody boundary',
      safetyNotice: investmentBoundaryEn,
    },
    prices: {
      eyebrow: 'Trading and custody',
      title: 'Prices',
      subtitle:
        'Simulated prices page with fee placeholders for funds, stocks, custody, and trading, without real pricing contract or market data.',
      badge: 'Price concept',
      primaryPanelEyebrow: 'Price table',
      primaryPanelTitle: 'Indicative placeholders',
      items: [
        { label: 'Funds', value: 'Subscription fee placeholder', note: 'No contract price.' },
        { label: 'Stocks', value: 'Trading fee placeholder', note: 'No execution fee.' },
        { label: 'Custody', value: 'Custody fee placeholder', note: 'No custody contract.' },
        { label: 'Trading', value: 'Order fee placeholder', note: 'No real order route.' },
      ],
      secondaryPanelEyebrow: 'Pricing controls',
      secondaryPanelTitle: 'No real pricing',
      rows: [
        { title: 'Pricing contract', detail: 'No real customer pricing contract exists.', status: 'Blocked' },
        { title: 'Market data', detail: 'No real market data feed is loaded.', status: 'Blocked' },
        { title: 'Fee rows', detail: 'Fees are placeholders for UI structure.', status: 'Simulated' },
      ],
      summaryTitle: 'Price summary',
      summaryItems: [
        { label: 'Fee table', value: 'Placeholder' },
        { label: 'Market data', value: 'None' },
        { label: 'Real contract', value: 'None' },
      ],
      actionLabel: 'Download price list simulation',
      actionNote: 'No real pricing document is generated.',
      riskTitle: 'Pricing notice',
      riskNotice:
        'Prices, fees, and market data shown here are placeholders and not customer terms.',
      safetyTitle: 'Pricing boundary',
      safetyNotice: investmentBoundaryEn,
    },
    marketNews: {
      eyebrow: 'News and analysis',
      title: 'Market news',
      subtitle:
        'Simulated market news page with market update cards, macro note, digital asset market risk note, and no-advice disclaimer.',
      badge: 'News concept',
      primaryPanelEyebrow: 'Market update cards',
      primaryPanelTitle: 'Simulated updates',
      items: [
        { label: 'Market update', value: 'European markets mixed', note: 'Fictional headline.' },
        { label: 'Macro note', value: 'Inflation data watched by investors', note: 'General placeholder.' },
        { label: 'Digital asset market risk', value: 'Volatility remains high', note: 'Risk note, not advice.' },
      ],
      secondaryPanelEyebrow: 'News controls',
      secondaryPanelTitle: 'Information boundary',
      rows: [
        { title: 'No investment advice', detail: 'Updates are fictional and informational.', status: 'Notice' },
        { title: 'No recommendation', detail: 'No instrument is recommended.', status: 'Notice' },
        { title: 'No market feed', detail: 'No real news or market data API is connected.', status: 'Blocked' },
      ],
      summaryTitle: 'News summary',
      summaryItems: [
        { label: 'News cards', value: 'Simulated' },
        { label: 'Advice', value: 'None' },
        { label: 'Market feed', value: 'None' },
      ],
      actionLabel: 'Refresh news simulation',
      actionNote: 'No real news feed or market data source is requested.',
      riskTitle: 'No advice disclaimer',
      riskNotice:
        'Market news can influence decisions, but this page provides no investment advice or recommendation.',
      safetyTitle: 'News boundary',
      safetyNotice: investmentBoundaryEn,
    },
    research: {
      eyebrow: 'News and analysis',
      title: 'Research',
      subtitle:
        'Simulated research page with categories, analyst note placeholder, risk analysis placeholder, and digital asset research boundary.',
      badge: 'Research concept',
      primaryPanelEyebrow: 'Research categories',
      primaryPanelTitle: 'Research library',
      items: [
        { label: 'Funds research', value: 'Profile placeholder', note: 'No recommendation.' },
        { label: 'Equity research', value: 'Analyst note placeholder', note: 'No analyst opinion.' },
        { label: 'Risk analysis', value: 'Scenario placeholder', note: 'No suitability assessment.' },
        { label: 'Digital asset research boundary', value: 'Separate risk category', note: 'No crypto recommendation.' },
      ],
      secondaryPanelEyebrow: 'Research controls',
      secondaryPanelTitle: 'Advice boundary',
      rows: [
        { title: 'Analyst note placeholder', detail: 'Text is static and not analyst research.', status: 'Simulated' },
        { title: 'Risk analysis placeholder', detail: 'Risk analysis is educational only.', status: 'Notice' },
        { title: 'Investment advice', detail: 'No advice is provided.', status: 'Blocked' },
      ],
      summaryTitle: 'Research summary',
      summaryItems: [
        { label: 'Categories', value: '4 simulated' },
        { label: 'Advice', value: 'None' },
        { label: 'Recommendations', value: 'None' },
      ],
      actionLabel: 'Open research simulation',
      actionNote: 'No research subscription or advice workflow is opened.',
      riskTitle: 'Research boundary',
      riskNotice:
        'Research placeholders are not investment recommendations, advice, or real analyst publications.',
      safetyTitle: 'Research boundary',
      safetyNotice: investmentBoundaryEn,
    },
    investmentFaq: {
      eyebrow: 'Help with investing',
      title: 'Investment FAQ',
      subtitle:
        'Investment FAQ covering how investing works, risk of loss, custody accounts, trading hours, and digital asset separation from deposits.',
      badge: 'FAQ',
      primaryPanelEyebrow: 'Common investment questions',
      primaryPanelTitle: 'Investment guidance',
      items: [
        { label: 'How investing works', value: 'Investing involves risk and possible loss.', note: 'General information only.' },
        { label: 'Custody accounts', value: 'Custody account concept', note: 'No custody execution.' },
        { label: 'Trading hours', value: 'Market hours placeholder', note: 'No real market status.' },
        { label: 'Digital assets', value: 'Separate from deposits', note: 'No deposit protection for digital assets.' },
      ],
      secondaryPanelEyebrow: 'FAQ topics',
      secondaryPanelTitle: 'Information topics',
      rows: [
        { title: 'Risk of loss', detail: 'Investments can lose value.', status: 'Risk notice' },
        { title: 'Trading hours', detail: 'Trading hours shown here are not live.', status: 'Information' },
        { title: 'Digital asset separation', detail: 'Digital assets are separate from deposits.', status: 'Risk notice' },
      ],
      summaryTitle: 'FAQ summary',
      summaryItems: [
        { label: 'Advice', value: 'None' },
        { label: 'Trading', value: 'None' },
        { label: 'Digital assets', value: 'Separate from deposits' },
      ],
      actionLabel: 'Review risk information',
      actionNote: 'This is an informational prototype page.',
      riskTitle: 'No investment advice',
      riskNotice:
        'This FAQ is informational and does not provide investment advice, tax advice, or recommendations.',
      safetyTitle: 'FAQ boundary',
      safetyNotice: investmentBoundaryEn,
    },
    riskInformation: {
      eyebrow: 'Help with investing',
      title: 'Risk information',
      subtitle:
        'Investment risk information covering market risk, liquidity risk, custody risk, digital asset risk, volatility, and deposit protection boundaries.',
      badge: 'Risk information',
      primaryPanelEyebrow: 'Risk categories',
      primaryPanelTitle: 'Investment risks',
      items: [
        { label: 'Market risk', value: 'Prices can rise or fall', note: 'Loss is possible.' },
        { label: 'Liquidity risk', value: 'Selling may be delayed or costly', note: 'General risk statement.' },
        { label: 'Custody risk', value: 'Custody depends on operational controls', note: 'No real custody service.' },
        { label: 'Digital asset risk', value: 'High volatility and no deposit protection', note: 'Separate from deposits.' },
      ],
      secondaryPanelEyebrow: 'Risk notices',
      secondaryPanelTitle: 'No advice controls',
      rows: [
        { title: 'Volatility', detail: 'Investment and digital asset values can move sharply.', status: 'High risk' },
        { title: 'No deposit protection for digital assets', detail: 'Digital assets are not bank deposits.', status: 'Risk notice' },
        { title: 'No investment advice', detail: 'This page does not recommend any product or action.', status: 'Notice' },
      ],
      summaryTitle: 'Risk summary',
      summaryItems: [
        { label: 'Market risk', value: 'Present' },
        { label: 'Liquidity risk', value: 'Present' },
        { label: 'Advice', value: 'None' },
      ],
      actionLabel: 'Acknowledge simulation',
      actionNote: 'No acknowledgement is recorded in a real system.',
      riskTitle: 'Risk information',
      riskNotice:
        'Investing involves risk of loss. Digital assets are volatile and are not protected as bank deposits.',
      safetyTitle: 'Risk boundary',
      safetyNotice: investmentBoundaryEn,
    },
  },
}

const investmentDemoEs: InvestmentDemoTranslations = {
  common: {
    reviewSummary: 'Resumen de revisión',
    simulatedAction: 'Acción simulada',
    localPrototype: 'Prototipo local determinístico',
    noRealInvestmentExecution: 'Sin ejecución real de operaciones',
  },
  pages: {
    overview: {
      eyebrow: 'Inversiones',
      title: 'Resumen de inversiones',
      subtitle:
        'Resumen simulado de inversiones con cartera, asignación de activos, estado de cuenta, actividad reciente y aviso de riesgo.',
      badge: 'Concepto de cartera',
      primaryPanelEyebrow: 'Resumen de cartera',
      primaryPanelTitle: 'Cartera de inversión',
      items: [
        { label: 'Valor de cartera', value: '24.680,00 EUR', note: 'Valor demo estático, no datos de cartera.' },
        { label: 'Asignación de activos', value: 'Fondos 60% · Acciones 30% · Efectivo 10%', note: 'Marcador de asignación solamente.' },
        { label: 'Estado de cuenta de inversión', value: 'Concepto activo', note: 'Sin conexión a cuenta real.' },
      ],
      secondaryPanelEyebrow: 'Actividad simulada reciente',
      secondaryPanelTitle: 'Actividad y controles',
      rows: [
        { title: 'Ahorro mensual en fondo preparado', detail: 'Fila visual de actividad, sin suscripción.', status: 'Simulado' },
        { title: 'Recordatorio de revisión de cartera', detail: 'Recordatorio de riesgo solo para demostración.', status: 'Aviso' },
        { title: 'Límite de activos digitales confirmado', detail: 'Activos digitales separados de depósitos y productos de inversión.', status: 'Aviso de riesgo' },
      ],
      summaryTitle: 'Resumen general',
      summaryItems: [
        { label: 'Datos de cartera', value: 'Simulados' },
        { label: 'Asesoría de inversión', value: 'Ninguna' },
        { label: 'Ejecución', value: 'Ninguna' },
      ],
      actionLabel: 'Actualizar simulación',
      actionNote: 'No se solicita ningún dato real de cartera o mercado.',
      riskTitle: 'Aviso de riesgo',
      riskNotice:
        'Las inversiones pueden perder valor. Esta página no proporciona asesoría, recomendaciones ni información real de cartera.',
      safetyTitle: 'Límite de inversión',
      safetyNotice: investmentBoundaryEs,
    },
    funds: {
      eyebrow: 'Inversiones',
      title: 'Fondos',
      subtitle:
        'Página simulada de fondos con lista de fondos, nivel de riesgo, opción visual de ahorro mensual y marcadores de sostenibilidad/perfil.',
      badge: 'Concepto de fondos',
      primaryPanelEyebrow: 'Lista de fondos',
      primaryPanelTitle: 'Conceptos de fondos disponibles',
      items: [
        { label: 'Aurora Nordic Balanced Fund', value: 'Nivel de riesgo 3/7', note: 'Concepto de fondo, no recomendación.' },
        { label: 'Aurora Global Index Fund', value: 'Nivel de riesgo 4/7', note: 'Fila estática de fondo.' },
        { label: 'Opción de ahorro mensual', value: 'Importe visual 100,00 EUR', note: 'No se crea ninguna orden de ahorro mensual.' },
        { label: 'Sostenibilidad/perfil', value: 'Perfil como marcador', note: 'No se realiza evaluación de idoneidad.' },
      ],
      secondaryPanelEyebrow: 'Controles de fondos',
      secondaryPanelTitle: 'Límite de suscripción',
      rows: [
        { title: 'Nivel de riesgo visible', detail: 'Las etiquetas de riesgo son marcadores educativos estáticos.', status: 'Aviso' },
        { title: 'Ahorro mensual visual', detail: 'El ahorro mensual se muestra pero no se activa.', status: 'Simulado' },
        { title: 'Suscripción de fondo', detail: 'No se envía ninguna suscripción real de fondo.', status: 'Bloqueado' },
      ],
      summaryTitle: 'Resumen de fondos',
      summaryItems: [
        { label: 'Fondos', value: '2 simulados' },
        { label: 'Asesoría', value: 'Ninguna' },
        { label: 'Suscripción', value: 'Ninguna' },
      ],
      actionLabel: 'Simular suscripción',
      actionNote: 'El botón está deshabilitado porque no se envía ninguna suscripción real.',
      riskTitle: 'Aviso de riesgo de fondos',
      riskNotice:
        'El valor de los fondos puede subir o bajar. Este prototipo no evalúa idoneidad ni recomienda fondos.',
      safetyTitle: 'Límite de fondos',
      safetyNotice: investmentBoundaryEs,
    },
    stocks: {
      eyebrow: 'Inversiones',
      title: 'Acciones',
      subtitle:
        'Página simulada de acciones con lista de seguimiento, estado de mercado, precios estáticos y botones de compra/venta deshabilitados.',
      badge: 'Concepto de seguimiento',
      primaryPanelEyebrow: 'Lista de seguimiento',
      primaryPanelTitle: 'Filas de precio simuladas',
      items: [
        { label: 'Aurora Industrial Oyj', value: '42,10 EUR', note: 'Precio simulado estático.' },
        { label: 'Nordic Utilities Plc', value: '18,45 EUR', note: 'Precio simulado estático.' },
        { label: 'Estado de mercado', value: 'Concepto abierto', note: 'Sin feed real de estado de mercado.' },
      ],
      secondaryPanelEyebrow: 'Controles de trading',
      secondaryPanelTitle: 'Acciones de operación deshabilitadas',
      rows: [
        { title: 'Botón comprar', detail: 'Se muestra solo como simulación.', status: 'Deshabilitado' },
        { title: 'Botón vender', detail: 'Se muestra solo como simulación.', status: 'Deshabilitado' },
        { title: 'Precios de mercado', detail: 'No se cargan datos reales de mercado.', status: 'Simulado' },
      ],
      summaryTitle: 'Resumen de acciones',
      summaryItems: [
        { label: 'Lista de seguimiento', value: '2 instrumentos' },
        { label: 'Datos de mercado', value: 'Estáticos' },
        { label: 'Trading', value: 'Ninguno' },
      ],
      actionLabel: 'Abrir simulación de operación',
      actionNote: 'No se puede colocar ninguna orden real de compra o venta.',
      riskTitle: 'Aviso de riesgo de mercado',
      riskNotice:
        'Los precios de acciones pueden fluctuar y causar pérdidas. Las filas estáticas no son precios reales de mercado.',
      safetyTitle: 'Límite de trading',
      safetyNotice: investmentBoundaryEs,
    },
    accounts: {
      eyebrow: 'Inversiones',
      title: 'Cuentas de inversión',
      subtitle:
        'Cuentas de inversión simuladas con cuenta de inversión, cuenta de custodia, marcador de tipo fiscal/cuenta y estado.',
      badge: 'Concepto de cuenta',
      primaryPanelEyebrow: 'Cuenta de inversión',
      primaryPanelTitle: 'Estructura de cuenta',
      items: [
        { label: 'Cuenta de inversión', value: 'Aurora Investment Account', note: 'Concepto estático de cuenta.' },
        { label: 'Cuenta de custodia', value: 'Concepto de custodia de valores', note: 'Sin ejecución de custodia.' },
        { label: 'Tipo fiscal/cuenta', value: 'Tipo de cuenta como marcador', note: 'Sin asesoría fiscal.' },
      ],
      secondaryPanelEyebrow: 'Estado de cuenta',
      secondaryPanelTitle: 'Límite de apertura',
      rows: [
        { title: 'Estado de cuenta', detail: 'Cuenta mostrada solo como concepto activo.', status: 'Simulado' },
        { title: 'Flujo de apertura', detail: 'No existe apertura real de cuenta de inversión.', status: 'Bloqueado' },
        { title: 'Datos de cliente', detail: 'No se usan datos reales de clientes.', status: 'Sin datos reales' },
      ],
      summaryTitle: 'Resumen de cuenta',
      summaryItems: [
        { label: 'Cuenta de inversión', value: 'Simulada' },
        { label: 'Cuenta de custodia', value: 'Simulada' },
        { label: 'Apertura real', value: 'Ninguna' },
      ],
      actionLabel: 'Simular apertura de cuenta',
      actionNote: 'No se abre ninguna cuenta real de inversión.',
      riskTitle: 'Aviso de riesgo de cuenta',
      riskNotice:
        'Las cuentas de inversión pueden implicar riesgos de mercado y custodia. Esta página es solo informativa.',
      safetyTitle: 'Límite de cuenta',
      safetyNotice: investmentBoundaryEs,
    },
    trading: {
      eyebrow: 'Trading y custodia',
      title: 'Trading',
      subtitle:
        'Página simulada de trading con ticket de orden visual, búsqueda de instrumento, tipo de orden, coste estimado y comprobación previa de cumplimiento/riesgo.',
      badge: 'Concepto de orden',
      primaryPanelEyebrow: 'Ticket de orden',
      primaryPanelTitle: 'Simulación de operación',
      items: [
        { label: 'Búsqueda de instrumento', value: 'Aurora Industrial Oyj', note: 'Búsqueda como marcador.' },
        { label: 'Tipo de orden', value: 'Concepto de orden limitada', note: 'No se envía ninguna orden.' },
        { label: 'Coste estimado', value: '421,00 EUR', note: 'Estimación estática, no cotización.' },
      ],
      secondaryPanelEyebrow: 'Comprobación previa',
      secondaryPanelTitle: 'Controles de cumplimiento y riesgo',
      rows: [
        { title: 'Comprobación de cumplimiento', detail: 'La comprobación se representa como estado UI determinístico.', status: 'Requerido' },
        { title: 'Reconocimiento de riesgo', detail: 'Un aviso de riesgo sería requerido antes de una orden real.', status: 'Requerido' },
        { title: 'Ejecución de orden', detail: 'El envío de órdenes está deshabilitado.', status: 'Bloqueado' },
      ],
      summaryTitle: 'Resumen de orden',
      summaryItems: [
        { label: 'Instrumento', value: 'Aurora Industrial Oyj' },
        { label: 'Tipo de orden', value: 'Concepto limitada' },
        { label: 'Orden real', value: 'Ninguna' },
      ],
      actionLabel: 'Enviar orden simulada',
      actionNote: 'El botón está deshabilitado porque no se produce ejecución real de órdenes.',
      riskTitle: 'Aviso de riesgo de trading',
      riskNotice:
        'El trading puede causar pérdidas. Este ticket no es recomendación, cotización ni ruta de ejecución.',
      safetyTitle: 'Límite de orden',
      safetyNotice: investmentBoundaryEs,
    },
    custodyAccounts: {
      eyebrow: 'Trading y custodia',
      title: 'Cuentas de custodia',
      subtitle:
        'Página simulada de cuentas de custodia con cuenta de custodia de valores, límite de custodia de activos digitales, estado y marcador de reconciliación.',
      badge: 'Concepto de custodia',
      primaryPanelEyebrow: 'Cuentas de custodia',
      primaryPanelTitle: 'Estructura de custodia',
      items: [
        { label: 'Cuenta de custodia de valores', value: 'Aurora Securities Custody', note: 'Concepto estático de custodia.' },
        { label: 'Límite de custodia de activos digitales', value: 'Separada de custodia de valores', note: 'Sin integración real con custodios.' },
        { label: 'Estado de cuenta', value: 'Concepto activo', note: 'Sin servicio real de custodia.' },
      ],
      secondaryPanelEyebrow: 'Auditoría y reconciliación',
      secondaryPanelTitle: 'Marcadores de control',
      rows: [
        { title: 'Marcador de reconciliación', detail: 'La evidencia de reconciliación es solo visual.', status: 'Simulado' },
        { title: 'Marcador de auditoría', detail: 'Las filas de auditoría son texto determinístico.', status: 'Listo' },
        { title: 'Ejecución de custodia', detail: 'No se ejecuta ninguna operación real de custodia.', status: 'Bloqueado' },
      ],
      summaryTitle: 'Resumen de custodia',
      summaryItems: [
        { label: 'Custodia de valores', value: 'Simulada' },
        { label: 'Custodia de activos digitales', value: 'Límite separado' },
        { label: 'Ejecución real', value: 'Ninguna' },
      ],
      actionLabel: 'Revisar simulación de custodia',
      actionNote: 'No se ejecuta ningún servicio de custodia ni proceso de reconciliación.',
      riskTitle: 'Aviso de riesgo de custodia',
      riskNotice:
        'Los servicios de custodia implican riesgos operativos y legales. Esta página no representa una integración real con custodios.',
      safetyTitle: 'Límite de custodia',
      safetyNotice: investmentBoundaryEs,
    },
    prices: {
      eyebrow: 'Trading y custodia',
      title: 'Precios',
      subtitle:
        'Página simulada de precios con marcadores de comisiones de fondos, acciones, custodia y trading, sin contrato real de precios ni datos de mercado.',
      badge: 'Concepto de precios',
      primaryPanelEyebrow: 'Tabla de precios',
      primaryPanelTitle: 'Marcadores indicativos',
      items: [
        { label: 'Fondos', value: 'Marcador de comisión de suscripción', note: 'Sin precio contractual.' },
        { label: 'Acciones', value: 'Marcador de comisión de trading', note: 'Sin comisión de ejecución.' },
        { label: 'Custodia', value: 'Marcador de comisión de custodia', note: 'Sin contrato de custodia.' },
        { label: 'Trading', value: 'Marcador de comisión de orden', note: 'Sin ruta real de orden.' },
      ],
      secondaryPanelEyebrow: 'Controles de precios',
      secondaryPanelTitle: 'Sin precios reales',
      rows: [
        { title: 'Contrato de precios', detail: 'No existe contrato real de precios para cliente.', status: 'Bloqueado' },
        { title: 'Datos de mercado', detail: 'No se carga ningún feed real de datos de mercado.', status: 'Bloqueado' },
        { title: 'Filas de comisiones', detail: 'Las comisiones son marcadores de estructura UI.', status: 'Simulado' },
      ],
      summaryTitle: 'Resumen de precios',
      summaryItems: [
        { label: 'Tabla de comisiones', value: 'Marcador' },
        { label: 'Datos de mercado', value: 'Ninguno' },
        { label: 'Contrato real', value: 'Ninguno' },
      ],
      actionLabel: 'Descargar lista simulada',
      actionNote: 'No se genera ningún documento real de precios.',
      riskTitle: 'Aviso de precios',
      riskNotice:
        'Los precios, comisiones y datos de mercado mostrados son marcadores y no condiciones para clientes.',
      safetyTitle: 'Límite de precios',
      safetyNotice: investmentBoundaryEs,
    },
    marketNews: {
      eyebrow: 'Noticias y análisis',
      title: 'Noticias de mercado',
      subtitle:
        'Página simulada de noticias de mercado con tarjetas de actualización, nota macro, aviso de riesgo de activos digitales y descargo de no asesoría.',
      badge: 'Concepto de noticias',
      primaryPanelEyebrow: 'Tarjetas de mercado',
      primaryPanelTitle: 'Actualizaciones simuladas',
      items: [
        { label: 'Actualización de mercado', value: 'Mercados europeos mixtos', note: 'Titular ficticio.' },
        { label: 'Nota macro', value: 'Datos de inflación observados por inversores', note: 'Marcador general.' },
        { label: 'Riesgo de mercado de activos digitales', value: 'La volatilidad sigue elevada', note: 'Aviso de riesgo, no asesoría.' },
      ],
      secondaryPanelEyebrow: 'Controles de noticias',
      secondaryPanelTitle: 'Límite informativo',
      rows: [
        { title: 'Sin asesoría de inversión', detail: 'Las actualizaciones son ficticias e informativas.', status: 'Aviso' },
        { title: 'Sin recomendación', detail: 'No se recomienda ningún instrumento.', status: 'Aviso' },
        { title: 'Sin feed de mercado', detail: 'No hay API real de noticias o mercado conectada.', status: 'Bloqueado' },
      ],
      summaryTitle: 'Resumen de noticias',
      summaryItems: [
        { label: 'Noticias', value: 'Simuladas' },
        { label: 'Asesoría', value: 'Ninguna' },
        { label: 'Feed de mercado', value: 'Ninguno' },
      ],
      actionLabel: 'Actualizar noticias simuladas',
      actionNote: 'No se solicita ningún feed real de noticias o mercado.',
      riskTitle: 'Descargo de no asesoría',
      riskNotice:
        'Las noticias de mercado pueden influir en decisiones, pero esta página no ofrece asesoría ni recomendación de inversión.',
      safetyTitle: 'Límite de noticias',
      safetyNotice: investmentBoundaryEs,
    },
    research: {
      eyebrow: 'Noticias y análisis',
      title: 'Investigación',
      subtitle:
        'Página simulada de investigación con categorías, marcador de nota de analista, análisis de riesgo y límite de investigación de activos digitales.',
      badge: 'Concepto de investigación',
      primaryPanelEyebrow: 'Categorías de investigación',
      primaryPanelTitle: 'Biblioteca de investigación',
      items: [
        { label: 'Investigación de fondos', value: 'Perfil como marcador', note: 'Sin recomendación.' },
        { label: 'Investigación de acciones', value: 'Nota de analista como marcador', note: 'Sin opinión de analista.' },
        { label: 'Análisis de riesgo', value: 'Escenario como marcador', note: 'Sin evaluación de idoneidad.' },
        { label: 'Límite de investigación de activos digitales', value: 'Categoría de riesgo separada', note: 'Sin recomendación cripto.' },
      ],
      secondaryPanelEyebrow: 'Controles de investigación',
      secondaryPanelTitle: 'Límite de asesoría',
      rows: [
        { title: 'Nota de analista como marcador', detail: 'El texto es estático y no investigación de analista.', status: 'Simulado' },
        { title: 'Análisis de riesgo como marcador', detail: 'El análisis de riesgo es solo educativo.', status: 'Aviso' },
        { title: 'Asesoría de inversión', detail: 'No se proporciona asesoría.', status: 'Bloqueado' },
      ],
      summaryTitle: 'Resumen de investigación',
      summaryItems: [
        { label: 'Categorías', value: '4 simuladas' },
        { label: 'Asesoría', value: 'Ninguna' },
        { label: 'Recomendaciones', value: 'Ninguna' },
      ],
      actionLabel: 'Abrir investigación simulada',
      actionNote: 'No se abre ninguna suscripción de investigación ni flujo de asesoría.',
      riskTitle: 'Límite de investigación',
      riskNotice:
        'Los marcadores de investigación no son recomendaciones, asesoría ni publicaciones reales de analistas.',
      safetyTitle: 'Límite de investigación',
      safetyNotice: investmentBoundaryEs,
    },
    investmentFaq: {
      eyebrow: 'Ayuda con inversiones',
      title: 'Preguntas frecuentes de inversión',
      subtitle:
        'FAQ de inversión sobre funcionamiento, riesgo de pérdida, cuentas de custodia, horarios de trading y separación de activos digitales frente a depósitos.',
      badge: 'FAQ',
      primaryPanelEyebrow: 'Preguntas comunes de inversión',
      primaryPanelTitle: 'Orientación de inversión',
      items: [
        { label: 'Cómo funciona invertir', value: 'Invertir implica riesgo y posible pérdida.', note: 'Información general solamente.' },
        { label: 'Cuentas de custodia', value: 'Concepto de cuenta de custodia', note: 'Sin ejecución de custodia.' },
        { label: 'Horarios de trading', value: 'Horario de mercado como marcador', note: 'Sin estado real de mercado.' },
        { label: 'Activos digitales', value: 'Separados de depósitos', note: 'Sin protección de depósito para activos digitales.' },
      ],
      secondaryPanelEyebrow: 'Temas de FAQ',
      secondaryPanelTitle: 'Temas informativos',
      rows: [
        { title: 'Riesgo de pérdida', detail: 'Las inversiones pueden perder valor.', status: 'Aviso de riesgo' },
        { title: 'Horarios de trading', detail: 'Los horarios mostrados no son en vivo.', status: 'Información' },
        { title: 'Separación de activos digitales', detail: 'Los activos digitales están separados de depósitos.', status: 'Aviso de riesgo' },
      ],
      summaryTitle: 'Resumen de FAQ',
      summaryItems: [
        { label: 'Asesoría', value: 'Ninguna' },
        { label: 'Trading', value: 'Ninguno' },
        { label: 'Activos digitales', value: 'Separados de depósitos' },
      ],
      actionLabel: 'Revisar información de riesgo',
      actionNote: 'Esta es una página informativa del prototipo.',
      riskTitle: 'Sin asesoría de inversión',
      riskNotice:
        'Esta FAQ es informativa y no ofrece asesoría de inversión, asesoría fiscal ni recomendaciones.',
      safetyTitle: 'Límite de FAQ',
      safetyNotice: investmentBoundaryEs,
    },
    riskInformation: {
      eyebrow: 'Ayuda con inversiones',
      title: 'Información de riesgo',
      subtitle:
        'Información de riesgo de inversión sobre riesgo de mercado, riesgo de liquidez, riesgo de custodia, riesgo de activos digitales, volatilidad y protección de depósitos.',
      badge: 'Información de riesgo',
      primaryPanelEyebrow: 'Categorías de riesgo',
      primaryPanelTitle: 'Riesgos de inversión',
      items: [
        { label: 'Riesgo de mercado', value: 'Los precios pueden subir o bajar', note: 'La pérdida es posible.' },
        { label: 'Riesgo de liquidez', value: 'Vender puede demorarse o tener coste', note: 'Declaración general de riesgo.' },
        { label: 'Riesgo de custodia', value: 'La custodia depende de controles operativos', note: 'Sin servicio real de custodia.' },
        { label: 'Riesgo de activos digitales', value: 'Alta volatilidad y sin protección de depósitos', note: 'Separados de depósitos.' },
      ],
      secondaryPanelEyebrow: 'Avisos de riesgo',
      secondaryPanelTitle: 'Controles de no asesoría',
      rows: [
        { title: 'Volatilidad', detail: 'Los valores de inversiones y activos digitales pueden moverse bruscamente.', status: 'Riesgo alto' },
        { title: 'Sin protección de depósitos para activos digitales', detail: 'Los activos digitales no son depósitos bancarios.', status: 'Aviso de riesgo' },
        { title: 'Sin asesoría de inversión', detail: 'Esta página no recomienda productos ni acciones.', status: 'Aviso' },
      ],
      summaryTitle: 'Resumen de riesgo',
      summaryItems: [
        { label: 'Riesgo de mercado', value: 'Presente' },
        { label: 'Riesgo de liquidez', value: 'Presente' },
        { label: 'Asesoría', value: 'Ninguna' },
      ],
      actionLabel: 'Reconocer simulación',
      actionNote: 'No se registra ningún reconocimiento en un sistema real.',
      riskTitle: 'Información de riesgo',
      riskNotice:
        'Invertir implica riesgo de pérdida. Los activos digitales son volátiles y no están protegidos como depósitos bancarios.',
      safetyTitle: 'Límite de riesgo',
      safetyNotice: investmentBoundaryEs,
    },
  },
}

const onlineServicesSafetyNoticeEn =
  'Local deterministic prototype only. No real online banking setting, mobile banking access, authentication factor, device, secure message, notification, SMS, email, push notification, customer account, credential, token, biometric data, or security operation is created, modified, sent, used, or executed.'

const onlineServicesSafetyNoticeEs =
  'Prototipo local determinístico solamente. No se crea, modifica, envía, usa ni ejecuta ninguna configuración real de banca en línea, acceso de banca móvil, factor de autenticación, dispositivo, mensaje seguro, notificación, SMS, correo electrónico, notificación push, cuenta de cliente, credencial, token, dato biométrico u operación de seguridad.'

const onlineServicesEn = {
  common: {
    localDeterministicPrototype: 'Local deterministic prototype',
    noRealServiceChange: 'No real service change',
    reviewSummary: 'Service review',
    simulatedAction: 'Simulated action',
    safetyBoundary: 'Safety boundary',
  },
  pages: {
    overview: {
      eyebrow: 'Online Services',
      title: 'Online services overview',
      subtitle:
        'Institutional overview of simulated online banking settings, mobile banking, authentication, communication preferences, devices, and alerts.',
      badge: 'Prototype only',
      primaryPanelEyebrow: 'Service status',
      primaryPanelTitle: 'Online service areas',
      secondaryPanelEyebrow: 'Controls',
      secondaryPanelTitle: 'Current simulated configuration',
      summaryTitle: 'Overview status',
      actionLabel: 'Review online services',
      actionNote:
        'This disabled action represents an internal review of simulated online services. No online banking service is changed.',
      safetyTitle: 'Local deterministic prototype',
      safetyNotice: onlineServicesSafetyNoticeEn,
      items: [
        {
          label: 'Online banking settings summary',
          value: 'Configured',
          note: 'Language, document delivery, and session preferences are simulated.',
        },
        {
          label: 'Mobile banking status',
          value: 'Not enabled',
          note: 'No real mobile app access or device approval is active.',
        },
        {
          label: 'Strong authentication status',
          value: 'Simulated',
          note: 'No real credential, token, biometric data, or factor is used.',
        },
        {
          label: 'Security alerts',
          value: 'Demo queue',
          note: 'Alert rows are deterministic examples, not real monitoring.',
        },
      ],
      rows: [
        {
          title: 'Message and notification settings',
          detail: 'Secure bank mail, email, SMS, and push preferences are shown as local demo settings.',
          status: 'Local draft',
        },
        {
          title: 'Device management',
          detail: 'Trusted device and revoke-device concepts are presented without registering a real device.',
          status: 'No real device',
        },
        {
          title: 'Security alerts',
          detail: 'Login, payment approval, digital asset governance, and human approval alerts are prototype rows.',
          status: 'Recorded',
        },
      ],
      summaryItems: [
        { label: 'Authentication', value: 'No real authentication' },
        { label: 'Devices', value: 'No real devices' },
        { label: 'Communication', value: 'No real customer communication' },
      ],
    },
    settings: {
      eyebrow: 'Online banking settings',
      title: 'Online banking settings',
      subtitle:
        'Simulated profile and online banking preferences for a regulated banking-style prototype.',
      badge: 'Settings demo',
      primaryPanelEyebrow: 'Preferences',
      primaryPanelTitle: 'Banking preferences',
      secondaryPanelEyebrow: 'Setting rows',
      secondaryPanelTitle: 'Configured local values',
      summaryTitle: 'Settings boundary',
      actionLabel: 'Save settings',
      actionNote:
        'The save control is disabled because no real profile, account, or online banking setting is changed.',
      safetyTitle: 'No profile update',
      safetyNotice:
        'Local deterministic prototype only. No real profile, online banking setting, customer account, credential, message delivery, notification, or banking preference is created, modified, used, or executed.',
      items: [
        { label: 'Language preference', value: 'English / Spanish', note: 'Displayed through local i18n only.' },
        { label: 'Communication preference', value: 'Bank mail', note: 'No message is sent or received.' },
        { label: 'Document delivery preference', value: 'Electronic', note: 'No real document delivery is changed.' },
        { label: 'Session preference', value: 'Standard', note: 'No real authentication session policy is changed.' },
      ],
      rows: [
        { title: 'Security preference', detail: 'Sensitive actions remain controlled by prototype-only review concepts.', status: 'Controlled' },
        { title: 'Document delivery preference', detail: 'Electronic delivery is a local display value only.', status: 'Local draft' },
        { title: 'Session preference', detail: 'Session behavior is shown as a deterministic banking setting.', status: 'Simulated' },
      ],
      summaryItems: [
        { label: 'Profile changes', value: 'None' },
        { label: 'Customer data', value: 'Not used' },
        { label: 'Setting state', value: 'Local only' },
      ],
    },
    mobileBanking: {
      eyebrow: 'Mobile banking',
      title: 'Mobile banking',
      subtitle:
        'Simulated mobile banking access view for app status, approval concepts, login controls, and transaction confirmation.',
      badge: 'No device enrollment',
      primaryPanelEyebrow: 'Access status',
      primaryPanelTitle: 'Mobile banking controls',
      secondaryPanelEyebrow: 'Mobile controls',
      secondaryPanelTitle: 'Prototype approval concepts',
      summaryTitle: 'Mobile access boundary',
      actionLabel: 'Manage mobile access',
      actionNote:
        'The control is disabled because no real device or mobile banking access is enabled.',
      safetyTitle: 'No real mobile access',
      safetyNotice:
        'Local deterministic prototype only. No real mobile banking access, device approval, mobile login, transaction confirmation, customer account, credential, token, biometric data, SMS, push notification, or security operation is created, modified, sent, used, or executed.',
      items: [
        { label: 'Mobile app access status', value: 'Not enabled', note: 'No real mobile banking session exists.' },
        { label: 'Mobile device approval placeholder', value: 'Simulated', note: 'No device is registered or approved.' },
        { label: 'Mobile login control', value: 'Concept only', note: 'No credential or biometric data is used.' },
        { label: 'Transaction confirmation concept', value: 'Review only', note: 'No payment or transfer is confirmed.' },
      ],
      rows: [
        { title: 'Device approval placeholder', detail: 'Represents a future bank-controlled device approval step.', status: 'No real device' },
        { title: 'Mobile login control', detail: 'Shows how mobile login could be governed without enabling access.', status: 'Disabled' },
        { title: 'Transaction confirmation concept', detail: 'Represents confirmation wording only; no operation can execute.', status: 'No live execution' },
      ],
      summaryItems: [
        { label: 'App access', value: 'Not enabled' },
        { label: 'Device trust', value: 'Simulated' },
        { label: 'Confirmation', value: 'No execution' },
      ],
    },
    strongAuthentication: {
      eyebrow: 'Strong authentication',
      title: 'Strong authentication',
      subtitle:
        'Simulated strong customer authentication for login, payment confirmation, sensitive approval, and recovery concepts.',
      badge: 'Sin autenticación real',
      primaryPanelEyebrow: 'Authentication status',
      primaryPanelTitle: 'Strong authentication model',
      secondaryPanelEyebrow: 'Confirmation controls',
      secondaryPanelTitle: 'Simulated confirmation points',
      summaryTitle: 'Authentication boundary',
      actionLabel: 'Review authentication',
      actionNote:
        'No authentication factor, credential, token, biometric data, or device is used.',
      safetyTitle: 'No real authentication factor',
      safetyNotice:
        'Local deterministic prototype only. No real authentication factor, credential, token, password, biometric data, mobile device, customer account, secure message, SMS, email, push notification, or security operation is created, modified, sent, used, or executed.',
      items: [
        { label: 'Strong authentication status', value: 'Simulated', note: 'No real factor or token is active.' },
        { label: 'Login confirmation', value: 'Required concept', note: 'Displayed as bank-grade control language only.' },
        { label: 'Payment confirmation', value: 'Required concept', note: 'No payment is approved or executed.' },
        { label: 'Recovery method placeholder', value: 'Under review', note: 'No recovery credential is created.' },
      ],
      rows: [
        { title: 'Login confirmation', detail: 'Prototype row for strong login confirmation.', status: 'Strong authentication required' },
        { title: 'Payment confirmation', detail: 'Prototype row for payment confirmation governance.', status: 'Required' },
        { title: 'Sensitive approval confirmation', detail: 'Prototype row aligned with sensitive approval controls.', status: 'Controlled' },
        { title: 'Recovery method placeholder', detail: 'Recovery is only described; no reset or credential flow exists.', status: 'No credential creation' },
      ],
      summaryItems: [
        { label: 'Authentication', value: 'No real authentication' },
        { label: 'Credentials', value: 'Not used' },
        { label: 'Biometrics', value: 'Not used' },
      ],
    },
    messages: {
      eyebrow: 'Message settings',
      title: 'Message settings',
      subtitle:
        'Simulated secure bank communication preferences for mail, statements, compliance notices, and service messages.',
      badge: 'No communication sent',
      primaryPanelEyebrow: 'Communication preferences',
      primaryPanelTitle: 'Bank message preferences',
      secondaryPanelEyebrow: 'Preference rows',
      secondaryPanelTitle: 'Secure communication concepts',
      summaryTitle: 'Communication boundary',
      actionLabel: 'Update message settings',
      actionNote:
        'No secure message, statement, notice, service message, email, or SMS is sent or received.',
      safetyTitle: 'No real customer communication',
      safetyNotice:
        'Local deterministic prototype only. No real secure bank mail, customer communication, statement delivery, compliance notice, service message, email, SMS, push notification, customer contact data, or banking operation is created, modified, sent, received, used, or executed.',
      items: [
        { label: 'Secure bank mail preference', value: 'Bank mail', note: 'No real secure message is sent.' },
        { label: 'Statement delivery preference', value: 'Electronic', note: 'No statement delivery is changed.' },
        { label: 'Compliance notice preference', value: 'Bank mail', note: 'No legal or compliance notice is sent.' },
        { label: 'Service message preference', value: 'Enabled concept', note: 'Shown as deterministic display state.' },
      ],
      rows: [
        { title: 'Secure bank mail preference', detail: 'Bank mail is shown as the preferred simulated channel.', status: 'Local draft' },
        { title: 'Statement delivery preference', detail: 'Electronic statement delivery remains prototype-only.', status: 'No real communication' },
        { title: 'Compliance notice preference', detail: 'Compliance notices are display rows only.', status: 'Recorded' },
      ],
      summaryItems: [
        { label: 'Messages', value: 'Not sent' },
        { label: 'Customer contact data', value: 'Not used' },
        { label: 'Delivery', value: 'No real delivery' },
      ],
    },
    notifications: {
      eyebrow: 'Notifications',
      title: 'Notifications',
      subtitle:
        'Simulated email, SMS, push, security, and transaction notification preferences.',
      badge: 'No message delivery',
      primaryPanelEyebrow: 'Notification settings',
      primaryPanelTitle: 'Notification channels',
      secondaryPanelEyebrow: 'Notification rows',
      secondaryPanelTitle: 'Delivery preferences',
      summaryTitle: 'Notification boundary',
      actionLabel: 'Update notifications',
      actionNote:
        'No email, SMS, push notification, or customer contact data is used.',
      safetyTitle: 'No real notification delivery',
      safetyNotice:
        'Local deterministic prototype only. No real email, SMS, push notification, secure message, customer contact data, customer account, credential, token, mobile device, or security operation is created, modified, sent, received, used, or executed.',
      items: [
        { label: 'Email notifications', value: 'Simulated', note: 'No email address or email delivery is used.' },
        { label: 'SMS notifications', value: 'Simulated', note: 'No phone number or SMS delivery is used.' },
        { label: 'Push notifications', value: 'Simulated', note: 'No mobile device or push service is used.' },
        { label: 'Security notifications', value: 'Enabled concept', note: 'No real monitoring or alert delivery occurs.' },
      ],
      rows: [
        { title: 'Transaction notifications', detail: 'Displayed as a preference row without sending messages.', status: 'Local draft' },
        { title: 'Security notifications', detail: 'Displayed as a prototype-only preference.', status: 'Monitoring' },
        { title: 'Push notifications', detail: 'No device token or push service is used.', status: 'No real devices' },
      ],
      summaryItems: [
        { label: 'Email', value: 'Not sent' },
        { label: 'SMS', value: 'Not sent' },
        { label: 'Push', value: 'Not sent' },
      ],
    },
    deviceManagement: {
      eyebrow: 'Device management',
      title: 'Device management',
      subtitle:
        'Simulated device management for registered devices, trusted status, risk score, and revoke-device concepts.',
      badge: 'Sin dispositivos reales',
      primaryPanelEyebrow: 'Device inventory',
      primaryPanelTitle: 'Registered device concepts',
      secondaryPanelEyebrow: 'Device controls',
      secondaryPanelTitle: 'Trusted device governance',
      summaryTitle: 'Device boundary',
      actionLabel: 'Revoke device',
      actionNote:
        'The revoke-device control is disabled because no real device is registered, trusted, tracked, or revoked.',
      safetyTitle: 'No real device management',
      safetyNotice:
        'Local deterministic prototype only. No real device, trusted device status, device risk score, mobile banking access, credential, token, biometric data, customer account, notification, or security operation is registered, tracked, trusted, revoked, used, or executed.',
      items: [
        { label: 'Registered devices', value: '2 demo rows', note: 'Device rows are fictional and deterministic.' },
        { label: 'Trusted device status', value: 'Simulated', note: 'No real trust relationship exists.' },
        { label: 'Device risk score', value: 'Low demo risk', note: 'No real device telemetry is processed.' },
        { label: 'Revoke device placeholder', value: 'Disabled', note: 'No device can be revoked.' },
      ],
      rows: [
        { title: 'Claudio demo laptop', detail: 'Fictional browser session row for layout only.', status: 'Simulated' },
        { title: 'Aurora demo mobile', detail: 'Fictional mobile device row with no enrollment.', status: 'No real device' },
        { title: 'Revoke device placeholder', detail: 'Control is shown but disabled to preserve the prototype boundary.', status: 'Disabled' },
      ],
      summaryItems: [
        { label: 'Device registry', value: 'Fictional' },
        { label: 'Tracking', value: 'Not performed' },
        { label: 'Revocation', value: 'Not executed' },
      ],
    },
    securityAlerts: {
      eyebrow: 'Security alerts',
      title: 'Security alerts',
      subtitle:
        'Simulated alert queue for login, device change, payment approval, digital asset rail governance, and human approval integrity events.',
      badge: 'No real monitoring',
      primaryPanelEyebrow: 'Alert queue',
      primaryPanelTitle: 'Security alert concepts',
      secondaryPanelEyebrow: 'Alert details',
      secondaryPanelTitle: 'Prototype alert records',
      summaryTitle: 'Alert boundary',
      actionLabel: 'Review alerts',
      actionNote:
        'No real security event, customer account, threat detection, or alert delivery is performed.',
      safetyTitle: 'No real security monitoring',
      safetyNotice:
        'Local deterministic prototype only. No real security event, customer account, threat detection, login monitoring, device tracking, payment approval, notification, credential, token, biometric data, or security operation is created, modified, sent, used, or executed.',
      items: [
        { label: 'Suspicious login alert', value: 'Demo alert', note: 'No login monitoring is performed.' },
        { label: 'Device change alert', value: 'Demo alert', note: 'No device change is detected.' },
        { label: 'Payment approval alert', value: 'Demo alert', note: 'No payment approval is executed.' },
        { label: 'Digital asset rail governance alert', value: 'Demo alert', note: 'Local governance wording only.' },
      ],
      rows: [
        { title: 'Suspicious login alert', detail: 'Fictional alert for review layout.', status: 'Under review' },
        { title: 'Device change alert', detail: 'Fictional device-change alert with no real device telemetry.', status: 'Recorded' },
        { title: 'Payment approval alert', detail: 'Fictional payment approval alert with no payment execution.', status: 'Controlled' },
        { title: 'Human approval integrity alert', detail: 'Prototype control row aligned with staff governance modules.', status: 'Escalated' },
      ],
      summaryItems: [
        { label: 'Monitoring', value: 'Not real' },
        { label: 'Threat detection', value: 'Not performed' },
        { label: 'Alerts', value: 'Demo only' },
      ],
    },
    faq: {
      eyebrow: 'Online services FAQ',
      title: 'Online services FAQ',
      subtitle:
        'Answers for how online services, mobile banking, strong authentication, devices, and notifications are represented in this local prototype.',
      badge: 'Support information',
      primaryPanelEyebrow: 'FAQ',
      primaryPanelTitle: 'Frequently asked questions',
      secondaryPanelEyebrow: 'Support topics',
      secondaryPanelTitle: 'Prototype explanations',
      summaryTitle: 'Support boundary',
      actionLabel: 'Contact support',
      actionNote:
        'Contact support is routed to this FAQ in the prototype. No real support message is created or sent.',
      safetyTitle: 'No real support message',
      safetyNotice: onlineServicesSafetyNoticeEn,
      items: [
        { label: 'How strong authentication works in this prototype', value: 'Concept only', note: 'No real authentication factor is active.' },
        { label: 'What mobile banking means in the demo', value: 'No access enabled', note: 'No mobile device is enrolled.' },
        { label: 'Why device management is simulated', value: 'Safety boundary', note: 'No real device is registered, tracked, or revoked.' },
        { label: 'What notifications are shown', value: 'Preference rows', note: 'No email, SMS, or push is sent.' },
      ],
      rows: [
        { title: 'Why no real banking setting is changed', detail: 'Aurora Digital Assets remains a local deterministic prototype with no real customer data.', status: 'Prototype only' },
        { title: 'What notifications are shown', detail: 'Notification rows show bank-grade preference wording without delivery.', status: 'No real communication' },
        { title: 'Why device management is simulated', detail: 'Device rows are fictional and do not use telemetry, credentials, or device tokens.', status: 'No real devices' },
      ],
      summaryItems: [
        { label: 'Support messages', value: 'Not sent' },
        { label: 'FAQ scope', value: 'Prototype' },
        { label: 'Customer data', value: 'Not used' },
      ],
    },
  },
} as const

const onlineServicesEs = {
  common: {
    localDeterministicPrototype: 'Prototipo local determinístico',
    noRealServiceChange: 'Sin cambio real de servicio',
    reviewSummary: 'Revisión del servicio',
    simulatedAction: 'Acción simulada',
    safetyBoundary: 'Límite de seguridad',
  },
  pages: {
    overview: {
      ...onlineServicesEn.pages.overview,
      eyebrow: 'Servicios en línea',
      title: 'Resumen de servicios en línea',
      subtitle:
        'Resumen institucional de configuraciones simuladas de banca en línea, banca móvil, autenticación, preferencias de comunicación, dispositivos y alertas.',
      badge: 'Solo prototipo',
      primaryPanelEyebrow: 'Estado del servicio',
      primaryPanelTitle: 'Áreas de servicios en línea',
      secondaryPanelEyebrow: 'Controles',
      secondaryPanelTitle: 'Configuración simulada actual',
      summaryTitle: 'Estado del resumen',
      actionLabel: 'Revisar servicios en línea',
      actionNote:
        'Esta acción deshabilitada representa una revisión interna de servicios en línea simulados. No se cambia ningún servicio real de banca en línea.',
      safetyTitle: 'Prototipo local determinístico',
      safetyNotice: onlineServicesSafetyNoticeEs,
      items: [
        { label: 'Resumen de configuración de banca en línea', value: 'Configurado', note: 'Las preferencias de idioma, entrega documental y sesión son simuladas.' },
        { label: 'Estado de banca móvil', value: 'No habilitado', note: 'No hay acceso real de app móvil ni aprobación de dispositivo activa.' },
        { label: 'Estado de autenticación fuerte', value: 'Simulado', note: 'No se usa credencial, token, dato biométrico ni factor real.' },
        { label: 'Alertas de seguridad', value: 'Cola demo', note: 'Las filas de alerta son ejemplos determinísticos, no monitoreo real.' },
      ],
      rows: [
        { title: 'Configuración de mensajes y notificaciones', detail: 'Correo bancario seguro, correo electrónico, SMS y push se muestran como preferencias demo locales.', status: 'Borrador local' },
        { title: 'Gestión de dispositivos', detail: 'Los conceptos de dispositivo confiable y revocación se presentan sin registrar un dispositivo real.', status: 'Sin dispositivos reales' },
        { title: 'Alertas de seguridad', detail: 'Las alertas de inicio de sesión, aprobación de pagos, gobernanza de rieles de activos digitales e integridad de aprobación humana son filas de prototipo.', status: 'Registrado' },
      ],
      summaryItems: [
        { label: 'Autenticación', value: 'Sin autenticación real' },
        { label: 'Dispositivos', value: 'Sin dispositivos reales' },
        { label: 'Comunicación', value: 'Sin comunicación real con clientes' },
      ],
    },
    settings: {
      ...onlineServicesEn.pages.settings,
      eyebrow: 'Configuración de banca en línea',
      title: 'Configuración de banca en línea',
      subtitle: 'Preferencias simuladas de perfil y banca en línea para un prototipo bancario regulado.',
      badge: 'Demo de configuración',
      primaryPanelEyebrow: 'Preferencias',
      primaryPanelTitle: 'Preferencias bancarias',
      secondaryPanelEyebrow: 'Filas de configuración',
      secondaryPanelTitle: 'Valores locales configurados',
      summaryTitle: 'Límite de configuración',
      actionLabel: 'Guardar configuración',
      actionNote: 'El control de guardar está deshabilitado porque no se cambia ningún perfil, cuenta o configuración real de banca en línea.',
      safetyTitle: 'Sin actualización de perfil',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, usa ni ejecuta ningún perfil real, configuración de banca en línea, cuenta de cliente, credencial, entrega de mensajes, notificación o preferencia bancaria.',
      items: [
        { label: 'Preferencia de idioma', value: 'Inglés / Español', note: 'Mostrada solo mediante i18n local.' },
        { label: 'Preferencia de comunicación', value: 'Correo bancario', note: 'No se envía ni recibe ningún mensaje.' },
        { label: 'Preferencia de entrega documental', value: 'Electrónica', note: 'No se cambia ninguna entrega documental real.' },
        { label: 'Preferencia de sesión', value: 'Estándar', note: 'No se cambia ninguna política real de sesión de autenticación.' },
      ],
      rows: [
        { title: 'Preferencia de seguridad', detail: 'Las acciones sensibles permanecen controladas por conceptos de revisión solo de prototipo.', status: 'Controlado' },
        { title: 'Preferencia de entrega documental', detail: 'La entrega electrónica es solo un valor de visualización local.', status: 'Borrador local' },
        { title: 'Preferencia de sesión', detail: 'El comportamiento de sesión se muestra como configuración bancaria determinística.', status: 'Simulado' },
      ],
      summaryItems: [
        { label: 'Cambios de perfil', value: 'Ninguno' },
        { label: 'Datos de cliente', value: 'No usados' },
        { label: 'Estado de configuración', value: 'Solo local' },
      ],
    },
    mobileBanking: {
      ...onlineServicesEn.pages.mobileBanking,
      eyebrow: 'Banca móvil',
      title: 'Banca móvil',
      subtitle: 'Vista simulada de acceso de banca móvil para estado de app, conceptos de aprobación, controles de inicio de sesión y confirmación de transacciones.',
      badge: 'Sin enrolamiento de dispositivo',
      primaryPanelEyebrow: 'Estado de acceso',
      primaryPanelTitle: 'Controles de banca móvil',
      secondaryPanelEyebrow: 'Controles móviles',
      secondaryPanelTitle: 'Conceptos de aprobación del prototipo',
      summaryTitle: 'Límite de acceso móvil',
      actionLabel: 'Gestionar acceso móvil',
      actionNote: 'El control está deshabilitado porque no se habilita ningún dispositivo real ni acceso real de banca móvil.',
      safetyTitle: 'Sin acceso móvil real',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, envía, usa ni ejecuta ningún acceso real de banca móvil, aprobación de dispositivo, inicio de sesión móvil, confirmación de transacción, cuenta de cliente, credencial, token, dato biométrico, SMS, notificación push u operación de seguridad.',
      items: [
        { label: 'Estado de acceso a app móvil', value: 'No habilitado', note: 'No existe sesión real de banca móvil.' },
        { label: 'Placeholder de aprobación de dispositivo móvil', value: 'Simulado', note: 'No se registra ni aprueba ningún dispositivo.' },
        { label: 'Control de inicio de sesión móvil', value: 'Solo concepto', note: 'No se usa credencial ni dato biométrico.' },
        { label: 'Concepto de confirmación de transacción', value: 'Solo revisión', note: 'No se confirma ningún pago o transferencia.' },
      ],
      rows: [
        { title: 'Placeholder de aprobación de dispositivo', detail: 'Representa un paso futuro de aprobación de dispositivo controlado por el banco.', status: 'Sin dispositivos reales' },
        { title: 'Control de inicio de sesión móvil', detail: 'Muestra cómo se podría gobernar el inicio móvil sin habilitar acceso.', status: 'Deshabilitado' },
        { title: 'Concepto de confirmación de transacción', detail: 'Representa solo texto de confirmación; ninguna operación puede ejecutarse.', status: 'Sin ejecución real' },
      ],
      summaryItems: [
        { label: 'Acceso app', value: 'No habilitado' },
        { label: 'Confianza de dispositivo', value: 'Simulada' },
        { label: 'Confirmación', value: 'Sin ejecución' },
      ],
    },
    strongAuthentication: {
      ...onlineServicesEn.pages.strongAuthentication,
      eyebrow: 'Autenticación fuerte',
      title: 'Autenticación fuerte',
      subtitle: 'Autenticación fuerte de cliente simulada para inicio de sesión, confirmación de pago, aprobación sensible y conceptos de recuperación.',
      badge: 'Sin autenticación real',
      primaryPanelEyebrow: 'Estado de autenticación',
      primaryPanelTitle: 'Modelo de autenticación fuerte',
      secondaryPanelEyebrow: 'Controles de confirmación',
      secondaryPanelTitle: 'Puntos de confirmación simulados',
      summaryTitle: 'Límite de autenticación',
      actionLabel: 'Revisar autenticación',
      actionNote: 'No se usa ningún factor de autenticación, credencial, token, dato biométrico ni dispositivo.',
      safetyTitle: 'Sin factor real de autenticación',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, envía, usa ni ejecuta ningún factor real de autenticación, credencial, token, contraseña, dato biométrico, dispositivo móvil, cuenta de cliente, mensaje seguro, SMS, correo electrónico, notificación push u operación de seguridad.',
      items: [
        { label: 'Estado de autenticación fuerte', value: 'Simulado', note: 'No hay factor o token real activo.' },
        { label: 'Confirmación de inicio de sesión', value: 'Concepto requerido', note: 'Mostrado solo como lenguaje de control bancario.' },
        { label: 'Confirmación de pago', value: 'Concepto requerido', note: 'No se aprueba ni ejecuta ningún pago.' },
        { label: 'Placeholder de método de recuperación', value: 'En revisión', note: 'No se crea ninguna credencial de recuperación.' },
      ],
      rows: [
        { title: 'Confirmación de inicio de sesión', detail: 'Fila de prototipo para confirmación fuerte de inicio de sesión.', status: 'Autenticación fuerte requerida' },
        { title: 'Confirmación de pago', detail: 'Fila de prototipo para gobernanza de confirmación de pagos.', status: 'Requerido' },
        { title: 'Confirmación de aprobación sensible', detail: 'Fila de prototipo alineada con controles de aprobación sensible.', status: 'Controlado' },
        { title: 'Placeholder de método de recuperación', detail: 'La recuperación solo se describe; no existe flujo de restablecimiento o credenciales.', status: 'Sin creación de credenciales' },
      ],
      summaryItems: [
        { label: 'Autenticación', value: 'Sin autenticación real' },
        { label: 'Credenciales', value: 'No usadas' },
        { label: 'Biometría', value: 'No usada' },
      ],
    },
    messages: {
      ...onlineServicesEn.pages.messages,
      eyebrow: 'Configuración de mensajes',
      title: 'Configuración de mensajes',
      subtitle: 'Preferencias simuladas de comunicación bancaria segura para correo, extractos, avisos de cumplimiento y mensajes de servicio.',
      badge: 'Sin comunicación enviada',
      primaryPanelEyebrow: 'Preferencias de comunicación',
      primaryPanelTitle: 'Preferencias de mensajes bancarios',
      secondaryPanelEyebrow: 'Filas de preferencia',
      secondaryPanelTitle: 'Conceptos de comunicación segura',
      summaryTitle: 'Límite de comunicación',
      actionLabel: 'Actualizar configuración de mensajes',
      actionNote: 'No se envía ni recibe ningún mensaje seguro, extracto, aviso, mensaje de servicio, correo electrónico o SMS.',
      safetyTitle: 'Sin comunicación real con clientes',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, envía, recibe, usa ni ejecuta ningún correo bancario seguro real, comunicación con clientes, entrega de extractos, aviso de cumplimiento, mensaje de servicio, correo electrónico, SMS, notificación push, dato de contacto de cliente u operación bancaria.',
      items: [
        { label: 'Preferencia de correo bancario seguro', value: 'Correo bancario', note: 'No se envía ningún mensaje seguro real.' },
        { label: 'Preferencia de entrega de extractos', value: 'Electrónica', note: 'No se cambia la entrega de extractos.' },
        { label: 'Preferencia de avisos de cumplimiento', value: 'Correo bancario', note: 'No se envía ningún aviso legal o de cumplimiento.' },
        { label: 'Preferencia de mensajes de servicio', value: 'Concepto habilitado', note: 'Mostrado como estado determinístico.' },
      ],
      rows: [
        { title: 'Preferencia de correo bancario seguro', detail: 'Correo bancario se muestra como canal simulado preferido.', status: 'Borrador local' },
        { title: 'Preferencia de entrega de extractos', detail: 'La entrega electrónica de extractos permanece solo en el prototipo.', status: 'Sin comunicación real' },
        { title: 'Preferencia de avisos de cumplimiento', detail: 'Los avisos de cumplimiento son solo filas de visualización.', status: 'Registrado' },
      ],
      summaryItems: [
        { label: 'Mensajes', value: 'No enviados' },
        { label: 'Datos de contacto', value: 'No usados' },
        { label: 'Entrega', value: 'Sin entrega real' },
      ],
    },
    notifications: {
      ...onlineServicesEn.pages.notifications,
      eyebrow: 'Notificaciones',
      title: 'Notificaciones',
      subtitle: 'Preferencias simuladas de notificaciones por correo electrónico, SMS, push, seguridad y transacciones.',
      badge: 'Sin entrega de mensajes',
      primaryPanelEyebrow: 'Configuración de notificaciones',
      primaryPanelTitle: 'Canales de notificación',
      secondaryPanelEyebrow: 'Filas de notificación',
      secondaryPanelTitle: 'Preferencias de entrega',
      summaryTitle: 'Límite de notificaciones',
      actionLabel: 'Actualizar notificaciones',
      actionNote: 'No se usa ningún correo electrónico, SMS, notificación push o dato de contacto de cliente.',
      safetyTitle: 'Sin entrega real de notificaciones',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, envía, recibe, usa ni ejecuta ningún correo electrónico real, SMS, notificación push, mensaje seguro, dato de contacto de cliente, cuenta de cliente, credencial, token, dispositivo móvil u operación de seguridad.',
      items: [
        { label: 'Notificaciones por correo electrónico', value: 'Simuladas', note: 'No se usa dirección de correo ni entrega de email.' },
        { label: 'Notificaciones por SMS', value: 'Simuladas', note: 'No se usa número de teléfono ni entrega SMS.' },
        { label: 'Notificaciones push', value: 'Simuladas', note: 'No se usa dispositivo móvil ni servicio push.' },
        { label: 'Notificaciones de seguridad', value: 'Concepto habilitado', note: 'No hay monitoreo ni entrega real de alertas.' },
      ],
      rows: [
        { title: 'Notificaciones de transacciones', detail: 'Mostradas como fila de preferencia sin enviar mensajes.', status: 'Borrador local' },
        { title: 'Notificaciones de seguridad', detail: 'Mostradas como preferencia solo de prototipo.', status: 'Monitoreo' },
        { title: 'Notificaciones push', detail: 'No se usa token de dispositivo ni servicio push.', status: 'Sin dispositivos reales' },
      ],
      summaryItems: [
        { label: 'Correo electrónico', value: 'No enviado' },
        { label: 'SMS', value: 'No enviado' },
        { label: 'Push', value: 'No enviado' },
      ],
    },
    deviceManagement: {
      ...onlineServicesEn.pages.deviceManagement,
      eyebrow: 'Gestión de dispositivos',
      title: 'Gestión de dispositivos',
      subtitle: 'Gestión simulada de dispositivos registrados, estado confiable, puntaje de riesgo y conceptos de revocación.',
      badge: 'Sin dispositivos reales',
      primaryPanelEyebrow: 'Inventario de dispositivos',
      primaryPanelTitle: 'Conceptos de dispositivos registrados',
      secondaryPanelEyebrow: 'Controles de dispositivo',
      secondaryPanelTitle: 'Gobernanza de dispositivo confiable',
      summaryTitle: 'Límite de dispositivos',
      actionLabel: 'Revocar dispositivo',
      actionNote: 'El control de revocación está deshabilitado porque no se registra, confía, rastrea ni revoca ningún dispositivo real.',
      safetyTitle: 'Sin gestión real de dispositivos',
      safetyNotice: 'Prototipo local determinístico solamente. No se registra, rastrea, confía, revoca, usa ni ejecuta ningún dispositivo real, estado de dispositivo confiable, puntaje de riesgo de dispositivo, acceso de banca móvil, credencial, token, dato biométrico, cuenta de cliente, notificación u operación de seguridad.',
      items: [
        { label: 'Dispositivos registrados', value: '2 filas demo', note: 'Las filas de dispositivo son ficticias y determinísticas.' },
        { label: 'Estado de dispositivo confiable', value: 'Simulado', note: 'No existe relación real de confianza.' },
        { label: 'Puntaje de riesgo de dispositivo', value: 'Riesgo demo bajo', note: 'No se procesa telemetría real de dispositivo.' },
        { label: 'Placeholder para revocar dispositivo', value: 'Deshabilitado', note: 'No se puede revocar ningún dispositivo.' },
      ],
      rows: [
        { title: 'Laptop demo de Claudio', detail: 'Fila ficticia de sesión de navegador solo para layout.', status: 'Simulado' },
        { title: 'Móvil demo Aurora', detail: 'Fila ficticia de dispositivo móvil sin enrolamiento.', status: 'Sin dispositivos reales' },
        { title: 'Placeholder para revocar dispositivo', detail: 'El control se muestra deshabilitado para preservar el límite del prototipo.', status: 'Deshabilitado' },
      ],
      summaryItems: [
        { label: 'Registro de dispositivos', value: 'Ficticio' },
        { label: 'Rastreo', value: 'No realizado' },
        { label: 'Revocación', value: 'No ejecutada' },
      ],
    },
    securityAlerts: {
      ...onlineServicesEn.pages.securityAlerts,
      eyebrow: 'Alertas de seguridad',
      title: 'Alertas de seguridad',
      subtitle: 'Cola simulada de alertas para inicio de sesión, cambio de dispositivo, aprobación de pago, gobernanza de rieles de activos digitales e integridad de aprobación humana.',
      badge: 'Sin monitoreo real',
      primaryPanelEyebrow: 'Cola de alertas',
      primaryPanelTitle: 'Conceptos de alertas de seguridad',
      secondaryPanelEyebrow: 'Detalles de alerta',
      secondaryPanelTitle: 'Registros de alerta del prototipo',
      summaryTitle: 'Límite de alertas',
      actionLabel: 'Revisar alertas',
      actionNote: 'No se realiza ningún evento real de seguridad, cuenta de cliente, detección de amenazas o entrega de alertas.',
      safetyTitle: 'Sin monitoreo real de seguridad',
      safetyNotice: 'Prototipo local determinístico solamente. No se crea, modifica, envía, usa ni ejecuta ningún evento real de seguridad, cuenta de cliente, detección de amenazas, monitoreo de inicio de sesión, rastreo de dispositivo, aprobación de pago, notificación, credencial, token, dato biométrico u operación de seguridad.',
      items: [
        { label: 'Alerta de inicio de sesión sospechoso', value: 'Alerta demo', note: 'No se realiza monitoreo de inicio de sesión.' },
        { label: 'Alerta de cambio de dispositivo', value: 'Alerta demo', note: 'No se detecta ningún cambio de dispositivo.' },
        { label: 'Alerta de aprobación de pago', value: 'Alerta demo', note: 'No se ejecuta ninguna aprobación de pago.' },
        { label: 'Alerta de gobernanza de rieles de activos digitales', value: 'Alerta demo', note: 'Solo lenguaje de gobernanza local.' },
      ],
      rows: [
        { title: 'Alerta de inicio de sesión sospechoso', detail: 'Alerta ficticia para layout de revisión.', status: 'En revisión' },
        { title: 'Alerta de cambio de dispositivo', detail: 'Alerta ficticia de cambio de dispositivo sin telemetría real.', status: 'Registrado' },
        { title: 'Alerta de aprobación de pago', detail: 'Alerta ficticia de aprobación de pago sin ejecución de pago.', status: 'Controlado' },
        { title: 'Alerta de integridad de aprobación humana', detail: 'Fila de control de prototipo alineada con módulos de gobernanza interna.', status: 'Escalado' },
      ],
      summaryItems: [
        { label: 'Monitoreo', value: 'No real' },
        { label: 'Detección de amenazas', value: 'No realizada' },
        { label: 'Alertas', value: 'Solo demo' },
      ],
    },
    faq: {
      ...onlineServicesEn.pages.faq,
      eyebrow: 'Preguntas frecuentes de servicios en línea',
      title: 'Preguntas frecuentes de servicios en línea',
      subtitle: 'Respuestas sobre cómo se representan servicios en línea, banca móvil, autenticación fuerte, dispositivos y notificaciones en este prototipo local.',
      badge: 'Información de soporte',
      primaryPanelEyebrow: 'FAQ',
      primaryPanelTitle: 'Preguntas frecuentes',
      secondaryPanelEyebrow: 'Temas de soporte',
      secondaryPanelTitle: 'Explicaciones del prototipo',
      summaryTitle: 'Límite de soporte',
      actionLabel: 'Contactar soporte',
      actionNote: 'Contactar soporte se dirige a esta FAQ en el prototipo. No se crea ni envía ningún mensaje real de soporte.',
      safetyTitle: 'Sin mensaje real de soporte',
      safetyNotice: onlineServicesSafetyNoticeEs,
      items: [
        { label: 'Cómo funciona la autenticación fuerte en este prototipo', value: 'Solo concepto', note: 'No hay factor real de autenticación activo.' },
        { label: 'Qué significa banca móvil en la demo', value: 'Sin acceso habilitado', note: 'No se enrola ningún dispositivo móvil.' },
        { label: 'Por qué la gestión de dispositivos es simulada', value: 'Límite de seguridad', note: 'No se registra, rastrea ni revoca ningún dispositivo real.' },
        { label: 'Qué notificaciones se muestran', value: 'Filas de preferencia', note: 'No se envía correo electrónico, SMS ni push.' },
      ],
      rows: [
        { title: 'Por qué no se cambia ninguna configuración bancaria real', detail: 'Aurora Digital Assets permanece como prototipo local determinístico sin datos reales de clientes.', status: 'Solo prototipo' },
        { title: 'Qué notificaciones se muestran', detail: 'Las filas de notificación muestran lenguaje bancario de preferencias sin entrega.', status: 'Sin comunicación real' },
        { title: 'Por qué la gestión de dispositivos es simulada', detail: 'Las filas de dispositivos son ficticias y no usan telemetría, credenciales ni tokens de dispositivo.', status: 'Sin dispositivos reales' },
      ],
      summaryItems: [
        { label: 'Mensajes de soporte', value: 'No enviados' },
        { label: 'Alcance FAQ', value: 'Prototipo' },
        { label: 'Datos de cliente', value: 'No usados' },
      ],
    },
  },
} as const

export const translations = {
  en: {
    common: {
      continue: 'Continue',
      back: 'Back',
      loading: 'Loading',
      error: 'Error',
      review: 'Review',
      reports: 'Reports',
      status: 'Status',
      ready: 'Ready',
      notReady: 'Not ready',
      critical: 'Critical',
      high: 'High',
      medium: 'Medium',
      low: 'Low',
      new: 'New',
      underReview: 'Under review',
      escalated: 'Escalated',
      closed: 'Closed',
      required: 'Required',
      optional: 'Optional',
      missing: 'Missing',
      included: 'Included',
      reviewerRequired: 'Reviewer required',
      yes: 'Yes',
      no: 'No',
      cancel: 'Cancel',
      language: 'Language',
      english: 'English',
      spanish: 'Spanish',
      auditEventCreated: 'Audit event created',
      auditEventId: 'Audit event ID',
      correlationId: 'Correlation ID',
      traceabilityRecord: 'Traceability record',
      sensitiveActionRecorded: 'Sensitive action recorded',
      safetyBoundaryText:
        'Local deterministic prototype only. No real assets, no real custody, no real bank integration, no real custodian integration, no real blockchain execution, no real cloud deployment, and no private keys or secrets.',
      humanApprovalIntegrityPrinciple:
        'Human review is not a trust anchor. It is a controlled risk event.',
      agentGovernancePrinciple:
        'Every agent must be identifiable, permission-bound, revocable, and auditable.',
    },
    phrases: enPhrases,
    navigation: {
      home: 'Home',
      payments: 'Payments',
      accounts: 'Accounts',
      cardsAndCurrency: 'Cards and Currency',
      loans: 'Loans',
      investments: 'Investments',
      insurance: 'Insurance',
      digitalAssets: 'Digital Assets',
      documents: 'Documents',
      onlineServices: 'Online Services',
      logOut: 'Log out',
      hideBalances: 'Hide balances',
      showBalances: 'Show balances',
      onlineBankingDemo: 'Online Banking Demo',
      mainNavigation: 'Main navigation',
    },
    paymentDemo: paymentDemoEn,
    accountDemo: accountDemoEn,
    cardDemo: cardDemoEn,
    loanDemo: loanDemoEn,
    insuranceDemo: insuranceDemoEn,
    investmentDemo: investmentDemoEn,
    onlineServices: onlineServicesEn,
    bankHome: {
      publicConcept: 'Public banking website concept',
      logIn: 'Log in',
      logInEbanking: 'Log in to eBanking',
      heroTitle: 'Banking services for everyday life',
      heroSubtitle:
        'Access accounts, payments, documents, and eligible digital asset services through a formal banking relationship.',
      learnDigitalAssets: 'Learn about Aurora Digital Assets',
      formalAccess: 'Formal banking access',
      servicesEyebrow: 'Services and life situations',
      servicesTitle: 'How can Aurora Bank help?',
      publicInformation: 'Public information',
      explore: 'Explore',
      integratedTitle: 'Integrated within online banking',
      eligibilityApplies: 'Eligibility applies',
      securityInformation: 'Security information',
      officialChannels: 'Use official banking channels',
      logInSecurely: 'Log in securely',
      becomeCustomer: 'Become a customer',
      contactOnboarding: 'Contact and onboarding',
      contactBank: 'Contact Aurora Bank',
      readServiceInfo: 'Read service information',
      services: [
        {
          title: 'Accounts and payments',
          description:
            'Everyday account and payment service concepts for customers with an Aurora Bank relationship.',
        },
        {
          title: 'Housing loan concept',
          description:
            'Structured guidance for major life decisions within a formal banking relationship.',
        },
        {
          title: 'Savings and investments',
          description:
            'Clear information and responsible planning concepts for long-term finances.',
        },
        {
          title: 'Digital Assets module',
          description:
            'Eligible customers may access simulated digital asset services through authenticated eBanking.',
        },
        {
          title: 'Customer service',
          description:
            'Support pathways for banking questions, documents, and service information.',
        },
        {
          title: 'Security and strong authentication',
          description:
            'Bank-issued credentials and strong authentication protect access to personal services.',
        },
      ],
      publicNavigation: [
        'For you',
        'For businesses',
        'Private Banking',
        'Daily banking',
        'Customer service',
        'Digital Assets',
        'Documents',
      ],
    },
    bankLogin: {
      securePrototype: 'Secure eBanking prototype',
      simulatedAccess: 'Simulated banking access',
      bankManagedAccess: 'Bank-managed access',
      title: 'Log on to Aurora eBanking',
      subtitle:
        'Access to Aurora Digital Assets is modelled as available only after the bank has established an authenticated customer session and confirmed eligibility.',
      simulatedSignIn: 'Simulated sign-in',
      stepOne: 'Step 1 of 2',
      stepTwo: 'Step 2 of 2',
      credentials: 'Credentials',
      bankIssuedAccess: 'Bank-issued access',
      credentialsHelp:
        "Use the bank-issued customer identifier and secret credential provided through the bank's formal onboarding process.",
      customerId: 'Customer ID',
      secretCredential: 'Secret credential',
      checking: 'Checking...',
      confirmMobileKey: 'Confirm with mobile key',
      strongAuthentication: 'Strong authentication',
      mobileApprovalSent:
        "A simulated approval request has been sent to the customer's banking authentication application.",
      action: 'Action',
      loginRequest: 'Login request',
      service: 'Service',
      customer: 'Customer',
      approvalMethod: 'Approval method',
      deviceApprovalRequired: 'Device approval required',
      timeLimit: 'Time limit',
      sessionExpires: 'Session expires in 02:00',
      processingApproval: 'Processing approval...',
      approveLogin: 'Approve simulated login',
      securityNote: 'Security note',
      protectIdentifiers: 'Protect your identifiers',
      protectIdentifiersCopy:
        'The bank never asks for your identifiers by email or text message. Always access eBanking through the official banking channel.',
      onboardingBoundary: 'Onboarding boundary',
      bankManagedOnboarding: 'Bank-managed onboarding',
      productBoundary: 'Product boundary',
      prototypeOnly: 'Prototype only',
      onboardingItems: [
        'Customer onboarded by bank',
        'Documents reviewed by bank',
        'Source of funds reviewed by bank',
        'Credentials issued by bank',
        'Strong authentication required',
      ],
    },
    dashboard: {
      welcomeBack: 'Welcome back',
      financialOverview: 'Financial overview',
      subtitle:
        'Review your accounts, payments, and digital assets from one banking environment.',
      strongAuthActive: 'Strong authentication active',
      accounts: 'Accounts',
      yourAccounts: 'Your accounts',
      newPayment: 'New payment',
      loadingDashboard: 'Loading dashboard data...',
      dashboardLoaded: 'Dashboard data loaded from local FastAPI prototype.',
      digitalAssets: 'Digital Assets',
      wallet: 'Aurora Digital Assets Wallet',
      conceptModule: 'Concept module',
      backendModule: 'Backend module',
      totalDigitalAssetsValue: 'Total digital assets value',
      volatilityNotice:
        'Digital assets are volatile and are separate from bank deposits.',
      custodyStatus: 'Custody status',
      buy: 'Buy',
      sell: 'Sell',
      withdraw: 'Withdraw',
      notifications: 'Notifications',
      importantMessages: 'Important messages',
      userProtection: 'User protection',
      riskNotice: 'Digital assets risk notice',
      riskNoticeCopy:
        'Crypto assets can lose value quickly. External wallet transfers are irreversible and may require additional security review.',
      readRiskInformation: 'Read risk information',
      protectionStatus: 'Protection status',
      protection: 'Digital assets protection',
    },
    digitalAssetsPage: {
      eyebrow: 'Digital Assets',
      heroSubtitle:
        'View digital asset balances, custody status, recent activity, and asset rail governance controls from inside a simulated online banking environment.',
      assetRailPhase: 'Phase 27',
      assetRailGovernance: 'Asset Rail Governance',
      assetRailBody:
        'Aurora classifies the asset rail before applying custody, settlement, compliance, evidence, and approval controls.',
      controlModelFirst: 'Control model first',
      rail: 'Rail:',
      controlModel: 'Control model',
      governanceExample: 'Governance example',
      openStaffGovernanceView: 'Open staff governance view',
      viewAuditTrail: 'View audit trail',
      digitalEuroNotBtc: 'Digital euro is not modeled as BTC',
      digitalEuroNotBtcBody:
        'Digital euro / CBDC is modeled as central bank money distributed or intermediated by banks or supervised payment service providers. Aurora does not apply external crypto custodian controls by default to digital euro rails.',
      cryptoassetControlPath: 'Cryptoasset control path',
      cryptoassetsDifferentPath:
        'Cryptoassets use a different control path',
      cryptoassetsDifferentPathBody:
        'BTC / ETH style assets may require custodian readiness, wallet boundary, private key boundary, blockchain execution boundary, human approval integrity, and agent governance controls before sensitive operations are considered.',
      safetyNotice:
        'Local deterministic prototype only. No real digital euro, CBDC, stablecoin, cryptoasset, custody, PSP, banking, blockchain, payment, settlement, redemption, transfer, customer data, private key, credential, or secret is used or executed. This is not legal advice or regulatory certification.',
      assetRailRows: [
        {
          name: 'Digital Euro / CBDC',
          rail: 'PSP-intermediated central bank money rail',
          controlModel: 'No external crypto custodian by default',
        },
        {
          name: 'Tokenized Deposit',
          rail: 'Internal bank ledger rail',
          controlModel: 'Bank liability and internal banking controls',
        },
        {
          name: 'Regulated Stablecoin / EMT',
          rail: 'Regulated issuer rail',
          controlModel: 'Issuer, reserve and redemption governance',
        },
        {
          name: 'Cryptoasset',
          rail: 'External crypto custody or blockchain execution rail',
          controlModel:
            'Custodian readiness, wallet boundary, private key boundary and blockchain execution controls',
        },
        {
          name: 'Security Token',
          rail: 'Securities settlement rail',
          controlModel: 'Securities controls and settlement governance',
        },
      ],
    },
    bankStaffWorkspace: {
      protectedArea: 'Protected bank staff area',
      title: 'Bank Staff Workspace',
      subtitle:
        'Internal concept workspace for onboarding, customer-authorized access, compliance review, reports, and demo administration.',
      authenticatedSession: 'Authenticated session',
      workspaceModules: 'Workspace modules',
      staffTools: 'Staff tools',
      conceptPrototype: 'Concept prototype',
      prototypeControls: 'Prototype controls',
      staffBoundary: 'Staff boundary',
      accessModel: 'Access model',
      commonActions: 'Common actions',
      operatingGuardrails: 'Operating guardrails',
      modules: {
        onboarding: 'Customer onboarding',
        customerAccess: 'Customer access authorization',
        riskOperations: 'Risk operations console',
        trustEngine: 'Aurora Trust Engine',
        apiSecurity: 'API security control center',
        infrastructureSecurity: 'Infrastructure security control center',
        cryptoAgility: 'Cryptographic agility control center',
        assetRailGovernance: 'Asset Rail Governance',
        sensitiveApproval: 'Sensitive operations approval engine',
        complianceReview: 'Compliance review',
        financialCrime: 'Financial crime monitoring',
        complianceIntelligence: 'Compliance intelligence',
        evidencePackages: 'Evidence packages',
        operationalResilience: 'Operational resilience',
        reportsAuditTrail: 'Reports and audit trail',
        demoAdministration: 'Demo administration',
      },
      moduleDescriptions: {
        onboarding:
          'Review the bank-managed customer onboarding model before digital asset services become available.',
        customerAccess:
          'Look up a demo customer and request temporary customer-authorized staff access.',
        riskOperations:
          'Unified command view for alerts, incidents, evidence readiness, escalations, paused operations, and staff priorities.',
        trustEngine:
          'Shared orchestration layer for risk, policy, evidence, assessment, control, regulation and knowledge modules.',
        apiSecurity:
          'Monitor sensitive backend actions, resolver authorization, business rate limits, schema exposure, step-up authentication, and audit logging.',
        infrastructureSecurity:
          'Monitor application-to-cloud chain reaction risks across backend authorization, Kubernetes RBAC, IAM, secrets, audit evidence, and risk operations.',
        cryptoAgility:
          'Track cryptographic inventory, algorithm versioning, key rotation, long-term confidentiality risk, and post-quantum migration readiness.',
        assetRailGovernance:
          'Classify digital euro, tokenized deposits, stablecoins, cryptoassets, and security tokens before applying the correct control path.',
        sensitiveApproval:
          'Model bank-style step-up approval, simulated mobile approval status, backend risk decisioning, audit evidence, and review routing.',
        complianceReview:
          'Review simulated transaction monitoring outcomes, wallet risk checks, and escalation evidence.',
        financialCrime:
          'Review insider risk, shell company indicators, structured deposits, crypto off-ramp risk, foreign transfer risk, and network-linked suspicious activity.',
        complianceIntelligence:
          'Explain financial crime alerts, review triggered controls, identify missing evidence, and prepare reviewer guidance before escalation.',
        evidencePackages:
          'Prepare structured evidence packages for compliance review, audit, investigation, and regulator-facing documentation.',
        operationalResilience:
          'Monitor service degradation, dependency failures, fallback modes, customer impact, and continuity controls.',
        reportsAuditTrail:
          'Open customer-facing reports, tax report concepts, and prototype audit evidence.',
        demoAdministration:
          'Inspect and reset local prototype data used by the Aurora Digital Assets demo environment.',
      },
      statuses: {
        bankStaffControl: 'Bank staff control',
        customerAuthorization: 'Customer authorization',
        orchestrationLayer: 'Orchestration layer',
        sharedOrchestration: 'Shared orchestration',
        backendSecurityLayer: 'Backend security layer',
        crossLayerSecurity: 'Cross-layer security',
        cryptoAgility: 'Crypto-agility',
        railClassification: 'Rail classification',
        stepUpApproval: 'Step-up approval',
        complianceReview: 'Compliance review',
        monitoringAlerts: 'Monitoring alerts',
        reasoningLayer: 'Reasoning layer',
        packageReadiness: 'Package readiness',
        resilienceCommand: 'Resilience command',
        auditEvidence: 'Audit evidence',
        prototypeOnly: 'Prototype only',
      },
    },
    assetRailGovernance: {
      eyebrow: 'Asset Rail Governance',
      title: 'Asset Rail Governance Engine',
      subtitle:
        'Classify digital asset rails before applying custody, settlement, compliance, evidence, and approval controls.',
      phase: 'Phase',
      mode: 'Mode',
      backendTests: 'Backend tests',
      backendTestsPassing: '204 passing',
      realIntegrations: 'Real integrations',
      realAssets: 'Real assets',
      externalExecution: 'External execution',
      localDeterministicPrototype: 'Local deterministic prototype',
      disabled: 'Disabled',
      classificationEyebrow: 'Governance path',
      classificationTitle: 'Asset rail classification',
      classificationText:
        'Aurora separates digital euro / CBDC, tokenized deposits, regulated stablecoins, cryptoassets, and security tokens into different governance paths.',
      controlModelFirst: 'Control model first',
      rail: 'Rail:',
      custody: 'Custody',
      controls: 'Controls',
      classified: 'Classified',
      decisionMatrixEyebrow: 'Deterministic controls',
      decisionMatrixTitle: 'Decision matrix',
      deterministic: 'Deterministic',
      required: 'Required',
      coreMessage: 'Core message',
      firstClassify: 'Classify first, then control',
      coreMessageText:
        'Aurora must not assume that every digital asset requires the same custody or settlement architecture. Aurora first classifies the asset rail, then applies the correct control model.',
      digitalEuroEyebrow: 'Central bank money rail',
      digitalEuroTitle: 'Digital euro is not modeled as a cryptoasset',
      cryptoassetEyebrow: 'External execution rail',
      cryptoassetTitle: 'Cryptoassets require a different control path',
      evidenceEyebrow: 'Evidence and review',
      evidenceTitle: 'Review paths',
      safetyNotice: 'Safety notice',
      prototypeBoundary: 'Prototype boundary',
      safetyNoticeText:
        'Local deterministic asset rail governance interface only. No real digital euro, CBDC, stablecoin, cryptoasset, custody, PSP, banking, blockchain, cloud, payment, redemption, settlement, transfer, customer data, private key, credential, or secret is used or executed. This is not legal advice or regulatory certification.',
      rails: [
        {
          name: 'Digital Euro / CBDC',
          rail: 'PSP-intermediated central bank money rail',
          custody: 'No external crypto custodian by default',
          controls:
            'PSP intermediation, privacy controls, holding limits, offline/online mode, AML, evidence review',
        },
        {
          name: 'Tokenized Deposit',
          rail: 'Internal bank ledger rail',
          custody: 'Bank liability / internal banking infrastructure',
          controls:
            'Bank ledger controls, settlement controls, human approval integrity, operational resilience',
        },
        {
          name: 'Regulated Stablecoin / EMT',
          rail: 'Regulated issuer rail',
          custody: 'Depends on service model',
          controls:
            'Issuer governance, reserve governance, redemption governance, AML, evidence review',
        },
        {
          name: 'Asset-Referenced Token',
          rail: 'Asset-referenced token issuer rail',
          custody: 'Depends on issuer, reserve and service model',
          controls:
            'Issuer governance, reserve governance, redemption governance, compliance review',
        },
        {
          name: 'Cryptoasset',
          rail: 'External crypto custody or blockchain execution rail',
          custody: 'External regulated custodian may be required',
          controls:
            'Custodian readiness, wallet boundary, private key boundary, blockchain execution boundary, agent governance',
        },
        {
          name: 'Security Token',
          rail: 'Securities settlement rail',
          custody: 'Securities custody and settlement governance',
          controls:
            'Securities controls, settlement controls, compliance review, evidence review',
        },
      ],
      digitalEuroPoints: [
        'Digital euro / CBDC is modeled as central bank money distributed or intermediated by banks or supervised payment service providers.',
        'It is not treated as BTC, ETH, or a generic externally custodied cryptoasset.',
        'External crypto custodian controls are not applied by default.',
        'Blockchain execution and private key controls are not assumed by default.',
      ],
      cryptoassetPoints: [
        'BTC / ETH style assets may require custodian readiness controls.',
        'Wallet boundary, private key boundary, and blockchain execution boundaries become relevant.',
        'Human approval integrity and agent governance controls must be applied before any sensitive operation is considered.',
        'No real custody or blockchain execution is performed in this prototype.',
      ],
      reviewLinks: {
        evidencePackages: 'Evidence packages',
        riskOperations: 'Risk operations',
        humanApprovalIntegrity: 'Human approval integrity',
        agentGovernance: 'Agent governance',
        cryptoAgility: 'Crypto agility',
        auditTrail: 'Audit trail',
      },
    },
    trustEngine: {
      eyebrow: 'Aurora Trust Engine',
      title: 'Shared Intelligence & Orchestration Layer',
      subtitle:
        'Coordinates risk, policy, evidence, assessment, regulation, control and knowledge layers across regulated digital asset operations.',
      mode: 'Mode',
      localDeterministicPrototype: 'Local deterministic prototype',
      realIntegrations: 'Real integrations',
      realAssets: 'Real assets',
      externalExecution: 'External execution',
      disabled: 'Disabled',
      evidence: 'Evidence',
      reviewable: 'Reviewable',
      controlModel: 'Control model',
      layered: 'Layered',
      orchestrationMap: 'Orchestration map',
      trustEngineMap: 'Trust Engine map',
      sharedLayer: 'Shared layer',
      coreMessage:
        'Aurora Trust Engine coordinates risk, policy, evidence, assessment, control, regulation and knowledge layers before sensitive banking or digital asset decisions can proceed.',
      coordinated: 'Coordinated',
      connectedAurora: 'Connected Aurora',
      connectedModules: 'Connected Aurora modules',
      reviewLinks: 'Review links',
      open: 'Open',
      corePrinciple: 'Core principle',
      beforeSensitiveDecision: 'Before sensitive decisions',
      deterministicFlow: 'Deterministic flow',
      trustFlow: 'Trust flow',
      step: 'Step',
      safetyBoundary: 'Safety boundary',
      prototypeBoundary: 'Prototype boundary',
      safetyBoundaryText:
        'Local deterministic trust engine interface only. No real banking, custody, PSP, digital euro, CBDC, stablecoin, cryptoasset, blockchain, cloud, payment, settlement, transfer, customer data, private key, credential or secret is used or executed. This is not legal advice or regulatory certification.',
      engineRows: [
        {
          name: 'Risk Engine',
          description:
            'Evaluates operational, custody, payment, asset rail and approval risk',
        },
        {
          name: 'Policy Engine',
          description:
            'Applies deterministic control policies before state changes',
        },
        {
          name: 'Evidence Engine',
          description:
            'Creates audit-ready evidence packages and review links',
        },
        {
          name: 'Assessment Engine',
          description:
            'Classifies scenarios, gaps, controls and readiness',
        },
        {
          name: 'Control Engine',
          description: 'Blocks or routes sensitive operations',
        },
        {
          name: 'Regulation Engine',
          description:
            'Maps regulatory concepts into control requirements',
        },
        {
          name: 'Knowledge Engine',
          description:
            'Preserves institutional control logic and explainability',
        },
      ],
      connectedLinks: {
        assetRailGovernance: 'Asset Rail Governance',
        riskOperations: 'Risk Operations',
        evidencePackages: 'Evidence Packages',
        complianceIntelligence: 'Compliance Intelligence',
        humanApprovalIntegrity: 'Human Approval Integrity',
        agentGovernance: 'Agent Governance',
        cryptoAgility: 'Crypto Agility',
        auditTrail: 'Audit Trail',
      },
      trustFlowSteps: [
        'Signal',
        'Classification',
        'Policy',
        'Risk score',
        'Evidence',
        'Review',
        'Approval integrity',
        'Controlled decision',
      ],
    },
    financialCrimeMonitoring: {
      title: 'Financial Crime Monitoring',
      subtitle:
        'Internal monitoring view for insider risk, suspicious transaction patterns, shell company indicators, crypto off-ramp risk, and evidence-driven escalation.',
      activeAlerts: 'Active alerts',
      criticalAlerts: 'Critical alerts',
      monitoringControls: 'Monitoring controls',
      reviewReadyCases: 'Review-ready cases',
      alertQueue: 'Alert queue',
      demoAlerts: 'Demo monitoring alerts',
      evaluateActivity: 'Evaluate activity',
      complianceIntelligence: 'Compliance intelligence',
    },
    complianceIntelligence: {
      title: 'Compliance Intelligence',
      subtitle:
        'Internal reasoning layer for explaining financial crime alerts, required evidence, reviewer guidance, and escalation decisions.',
      riskExplanations: 'Risk explanations',
      alertReasoning: 'Alert reasoning',
      reviewerGuidance: 'Reviewer guidance',
      explainAlert: 'Explain alert',
      prepareReviewCase: 'Prepare review case',
      decisionPath: 'Decision path',
      evidenceRequirements: 'Evidence requirements',
      reviewerNextSteps: 'Reviewer next steps',
      prepareEvidencePackage: 'Prepare evidence package',
    },
    evidencePackages: {
      title: 'Evidence Packages',
      subtitle:
        'Internal evidence preparation layer for compliance review, audit, investigation, and regulator-facing documentation.',
      packageReadiness: 'Package readiness',
      packageQueue: 'Package queue',
      evidencePackageList: 'Evidence package list',
      packageTemplates: 'Package templates',
      evidenceStructures: 'Evidence structures',
      packageGenerator: 'Package generator',
      generateDemo: 'Generate evidence package demo',
      readinessExplanation: 'Readiness explanation',
      totalPackages: 'Total packages',
      readyPackages: 'Ready packages',
      incompletePackages: 'Incomplete packages',
      averageReadiness: 'Average readiness',
      includedEvidence: 'Included evidence',
      missingEvidence: 'Missing evidence',
      triggeredControls: 'Triggered controls',
      reviewerNotes: 'Reviewer notes',
      decisionRationale: 'Decision rationale',
      timeline: 'Timeline',
      recommendedNextAction: 'Recommended next action',
      readinessScore: 'Readiness score',
      riskType: 'Risk type',
      created: 'Created',
      summary: 'Summary',
      sourceType: 'Source type',
      sourceId: 'Source ID',
      packageType: 'Package type',
      reviewerId: 'Reviewer ID',
      generatePackage: 'Generate package',
      packageTitle: 'Package title',
      exportAvailable: 'Export available',
      userMessage: 'User message',
      generateEvidenceFromAuditEvent: 'Generate evidence from audit event',
      generateFromAuditEvent: 'Generate from audit event',
      infrastructureChainReactionAuditEvent:
        'Infrastructure Security Chain Reaction',
      useInfrastructureChainReactionAuditEvent:
        'Use infrastructure chain reaction audit event',
      infrastructureEvidencePackage: 'Infrastructure evidence package',
      crossLayerAuditEvidence: 'Cross-layer audit evidence',
      applicationToCloudChainReaction: 'Application to cloud chain reaction',
      azureStorageToIdentityRisk: 'Azure Storage to Identity Risk',
      cryptoAgilityPqReadiness: 'Crypto-agility PQ readiness',
      azureStorageToIdentityRiskEvidencePackage:
        'Azure Storage to Identity Risk Evidence Package',
      azureStorageToIdentityRiskReviewCase:
        'Azure Storage to Identity Risk Review Case',
      openReviewCase: 'Open review case',
      reviewCaseCreated: 'Review case created',
      sourceEvidencePackage: 'Source evidence package',
      linkedEvidencePackage: 'Linked evidence package',
      infrastructureSecurityChainReactionReviewCase:
        'Infrastructure Security Chain Reaction Review Case',
      createFormalReviewCaseFromEvidencePackage:
        'Create a formal review case from this evidence package.',
      evidenceToReviewTraceability: 'Evidence-to-review traceability',
      complianceReviewLinkage: 'Compliance review linkage',
      auditLinkedEvidence: 'Audit-linked evidence',
      sourceAuditEventId: 'Source audit event ID',
      traceabilitySummary: 'Traceability summary',
      linkedAuditEvents: 'Linked audit events',
      backendDecision: 'Backend decision',
      auditLinkedEvidenceCopy:
        'Evidence packages can now be prepared from structured audit events, preserving the backend decision, correlation ID, source module, and review context.',
      recommendedActions: 'Recommended actions',
      blockers: 'Blockers',
      warnings: 'Warnings',
      noBlockers: 'No blockers recorded.',
      noWarnings: 'No warnings recorded.',
      noIncludedEvidence: 'No included evidence has been attached.',
      noMissingEvidence: 'No missing evidence is recorded.',
    },
    operationalResilience: {
      title: 'Operational Resilience',
      subtitle:
        'Internal command view for service degradation, dependency failures, fallback modes, customer impact, and continuity controls.',
      servicesMonitored: 'Services monitored',
      activeIncidents: 'Active incidents',
      fallbackModes: 'Fallback modes',
      highImpactServices: 'High impact services',
      serviceHealth: 'Service health',
      incidentQueue: 'Incident queue',
      dependencies: 'Dependencies',
      criticalDependencies: 'Critical dependencies',
      controls: 'Controls',
      resilienceControls: 'Resilience controls',
      scenarioDemo: 'Scenario demo',
      evaluateScenario: 'Evaluate scenario',
      scenario: 'Scenario',
      affectedService: 'Affected service',
      dependencyStatus: 'Dependency status',
      customerImpact: 'Customer impact',
      evaluateResilienceScenario: 'Evaluate resilience scenario',
      resilienceScore: 'Resilience score',
      severity: 'Severity',
      decision: 'Decision',
      controlsActivated: 'Controls activated',
      availableOperations: 'Available operations',
      pausedOperations: 'Paused operations',
      recommendedAction: 'Recommended action',
      explanation: 'Explanation',
      availability: 'Availability',
      fallbackAvailable: 'Fallback available',
      currentMode: 'Current mode',
      summary: 'Summary',
      failureType: 'Failure type',
      fallbackMode: 'Fallback mode',
      auditEvidence: 'Audit evidence',
      timeline: 'Timeline',
      allowedOperations: 'Allowed operations',
      activated: 'Activated',
      ready: 'Ready',
    },
    apiSecurity: {
      title: 'API Security Control Center',
      subtitle:
        'Internal API security layer for sensitive financial actions, resolver authorization, business rate limits, schema exposure, step-up authentication, and audit logging.',
      commandBannerTitle: 'The API is the real security boundary',
      commandBannerText:
        'Frontend controls are not enough. Sensitive operations must be validated, authorized, rate-limited, audited, and risk-scored in the backend.',
      securityBoundary: 'Security boundary',
      securityControls: 'Security controls',
      securityEvents: 'Security events',
      sensitiveOperations: 'Sensitive operations',
      blockedOrStepUpDecisions: 'Blocked or step-up decisions',
      backendControlLayer: 'Backend control layer',
      auditReadySignals: 'Audit-ready signals',
      businessActionBoundary: 'Business action boundary',
      customerProtectionDecisions: 'Customer protection decisions',
      eventQueue: 'Event queue',
      apiSecurityEvents: 'API security events',
      apiSurface: 'API surface',
      operationName: 'Operation name',
      businessAction: 'Business action',
      affectedObject: 'Affected object',
      auditEvent: 'Audit event',
      controlCatalog: 'Control catalog',
      category: 'Category',
      enabled: 'Enabled',
      disabled: 'Disabled',
      protectedOperations: 'Protected operations',
      decisionModel: 'Decision model',
      evidenceOutputs: 'Evidence outputs',
      requiredControls: 'Required controls',
      auditRequired: 'Audit required',
      stepUpRequired: 'Step-up required',
      batchingAllowed: 'Batching allowed',
      apiSurfaces: 'API surfaces',
      controlsApplied: 'Controls applied',
      securityScenarios: 'Security scenarios',
      expectedDecision: 'Expected decision',
      riskIndicators: 'Risk indicators',
      recommendedControls: 'Recommended controls',
      scenarioDemo: 'Scenario demo',
      evaluateApiScenario: 'Evaluate API scenario',
      attempts: 'Attempts',
      objectAuthorized: 'Object authorized',
      batchingDetected: 'Batching detected',
      sensitiveFieldsRequested: 'Sensitive fields requested',
      riskScore: 'Risk score',
      auditEventRequired: 'Audit event required',
      goldenRules: 'Golden rules',
      goldenRuleItems: [
        'The interface never decides security.',
        'Authenticated does not mean authorized.',
        'One sensitive operation equals one authorization decision and one audit event.',
        'Rate-limit the business action, not only the HTTP request.',
        'Sensitive fields do not belong casually in public API contracts.',
        'High-risk operations require stronger verification.',
      ],
      prototypeDisclaimer:
        'Aurora Digital Assets is a concept prototype. API security controls, events, scenarios, risk scores, and audit records are fictional deterministic demo data only.',
    },
    cryptoAgility: {
      title: 'Cryptographic Agility Control Center',
      subtitle:
        'Inventory, algorithm versioning, key lifecycle, long-term confidentiality risk, and post-quantum migration readiness.',
      bannerTitle: 'Designed for migration, not false promises',
      designedForMigration: 'Designed for migration, not false promises',
      bannerText:
        'Aurora does not claim to be quantum-proof. This module models cryptographic agility: knowing where cryptography is used, versioning algorithms, rotating keys, separating platform crypto from blockchain protocol crypto, and preparing for future standards-based migration.',
      cryptoAssets: 'Crypto assets',
      algorithmPolicies: 'Algorithm policies',
      rotationGaps: 'Rotation gaps',
      longTermRiskAssets: 'Long-term risk assets',
      pqReadinessGaps: 'PQ readiness gaps',
      assetInventory: 'Cryptographic asset inventory',
      algorithmVersioning: 'Algorithm versioning',
      keyLifecycle: 'Key lifecycle',
      longTermConfidentialityRisk: 'Long-term confidentiality risk',
      harvestRisk: 'Harvest now, decrypt later risk',
      postQuantumReadiness: 'Post-quantum readiness',
      platformVsBlockchain: 'Platform crypto vs blockchain protocol crypto',
      noCustomCryptography: 'No custom cryptography',
      noQuantumProofClaims: 'No quantum-proof claims',
      evaluateCryptoScenario: 'Evaluate crypto-agility scenario',
      scenarioEvaluation: 'Scenario evaluation',
      scenario: 'Scenario',
      scenarioResult: 'Scenario result',
      algorithmFamily: 'Algorithm family',
      version: 'Version',
      keyLocation: 'Key location',
      rotationPeriod: 'Rotation period',
      longTermConfidentiality: 'Long-term confidentiality',
      blockchainDependency: 'Blockchain protocol dependency',
      approvedCurrent: 'Approved current',
      deprecated: 'Deprecated',
      migrationCandidates: 'Migration candidates',
      cryptoOwner: 'Crypto owner',
      storageBoundary: 'Storage boundary',
      rotationRequired: 'Rotation required',
      emergencyRolloverReady: 'Emergency rollover ready',
      auditRequired: 'Audit required',
      riskScore: 'Risk score',
      severity: 'Severity',
      decision: 'Decision',
      auditEventId: 'Audit event ID',
      correlationId: 'Correlation ID',
      evidencePackageReady: 'Evidence package ready',
      affectedDomains: 'Affected domains',
      cryptoAgilityRisk: 'Crypto-agility risk',
      triggeredControls: 'Triggered controls',
      recommendedAction: 'Recommended action',
      explanation: 'Explanation',
      boundaryTitle: 'Cryptographic boundary',
      boundaryCopy:
        'Aurora platform cryptography is governed separately from external blockchain protocol cryptography.',
      auroraControls: [
        'TLS',
        'tokens',
        'API keys',
        'internal signatures',
        'database encryption',
        'backups',
        'audit log integrity',
        'microservice communication',
        'cloud certificates',
        'custody architecture boundaries',
      ],
      auroraDoesNotControl: [
        'Bitcoin consensus cryptography',
        'Ethereum protocol cryptography',
        'external blockchain migration',
        'third-party custody internals',
      ],
      goldenRules: 'Golden rules',
      goldenRuleItems: [
        'No custom cryptography.',
        'No quantum-proof claims.',
        'Inventory every cryptographic dependency.',
        'Version algorithms and key policies.',
        'Rotate keys with audit evidence.',
        'Classify long-term confidentiality risks.',
        'Separate platform crypto from blockchain protocol crypto.',
        'Use KMS/HSM/Key Vault for production-grade key governance.',
        'Prepare standards-based migration plans.',
        'Preserve evidence for every key lifecycle decision.',
      ],
      flags: {
        deprecated_algorithm_detected: 'Deprecated algorithm detected',
        long_lived_key_detected: 'Long-lived key detected',
        missing_algorithm_versioning: 'Missing algorithm versioning',
        missing_key_rotation_policy: 'Missing key rotation policy',
        backup_long_term_risk: 'Backup long-term risk',
        audit_integrity_gap: 'Audit integrity gap',
        custody_key_rotation_gap: 'Custody key rotation gap',
        blockchain_protocol_confusion: 'Blockchain protocol confusion',
        post_quantum_readiness_gap: 'Post-quantum readiness gap',
        kms_hsm_integration_missing: 'KMS/HSM/Key Vault integration missing',
      },
      prototypeDisclaimer:
        'Aurora Digital Assets is a concept prototype. No real cryptographic operation, key material, wallet key, custody key, KMS, HSM, Key Vault, or post-quantum algorithm is accessed or executed.',
    },
    sensitiveApproval: {
      title: 'Sensitive Operations Approval Engine',
      subtitle:
        'Bank-style strong approval for digital assets and internal sensitive actions.',
      bankStyleStrongApproval: 'Bank-style strong approval',
      stepUpApproval: 'Step-up approval',
      mobileApprovalSimulated: 'Mobile approval simulated',
      backendRiskDecision: 'Backend risk decision',
      approvalRequired: 'Approval required',
      operationCatalog: 'Operation catalog',
      sensitiveOperations: 'Sensitive operations',
      scenarioEvaluator: 'Scenario evaluator',
      customerConfirmed: 'Customer confirmed',
      deviceTrusted: 'Device trusted',
      mobileApprovalStatus: 'Mobile approval status',
      highValueNewWalletWithdrawal: 'High-value new wallet withdrawal',
      securityDeviceChange: 'Security device change',
      reviewerCaseClosure: 'Reviewer case closure',
      recommendedNextAction: 'Recommended next action',
      temporaryWithdrawalFreeze: 'Temporary withdrawal freeze',
      pendingReview: 'Pending review',
      blocked: 'Blocked',
      approved: 'Approved',
      evidencePackageReady: 'Evidence package ready',
      reviewCaseRequired: 'Review case required',
      operationType: 'Operation type',
      actorType: 'Actor type',
      amountEur: 'Amount EUR',
      asset: 'Asset',
      isNewDestination: 'New destination',
      riskLevel: 'Risk level',
      riskScore: 'Risk score',
      reasons: 'Reasons',
      evaluate: 'Evaluate sensitive approval',
      finnishModel: 'Finnish banking model',
      conceptBannerTitle: 'Access is not execution',
      conceptRules: [
        'Login allows access.',
        'Step-up approval allows an attempt.',
        'Backend risk evaluation decides the outcome.',
      ],
      finnishModelCopy:
        'Aurora adapts a familiar Finnish bank approval pattern to digital asset operations. The mobile approval is simulated in this prototype, and approval itself does not automatically mean execution. The backend still evaluates risk.',
      statuses: {
        pending: 'Pending',
        approved: 'Approved',
        rejected: 'Rejected',
        expired: 'Expired',
      },
      prototypeDisclaimer:
        'Aurora Digital Assets is a concept prototype. No real mobile approval, MFA, notifications, cryptographic signing, payment execution, or blockchain execution is performed.',
    },
    infrastructureSecurity: {
      title: 'Infrastructure Security Control Center',
      subtitle:
        'Cross-layer security posture for application authorization, Kubernetes RBAC, cloud IAM, secrets, audit evidence, and risk operations.',
      commandBannerTitle: 'Prevent one vulnerability from becoming a chain reaction',
      commandBannerText:
        'Aurora models how a backend issue can be contained before it reaches containers, Kubernetes permissions, cloud roles, secrets, or sensitive financial data.',
      cloudNativeBoundary: 'Cloud-native containment',
      securityLayers: 'Security layers',
      infrastructureControls: 'Infrastructure controls',
      activeEvents: 'Active events',
      criticalChainRisks: 'Critical chain risks',
      crossLayerSecurityEvents: 'Cross-layer security events',
      eventQueue: 'Event queue',
      affectedLayer: 'Affected layer',
      affectedLayers: 'Affected layers',
      chainStage: 'Chain stage',
      chainReactionRisk: 'Chain reaction risk',
      affectedAsset: 'Affected asset',
      evidencePackageReady: 'Evidence package ready',
      protectedAssets: 'Protected assets',
      monitoredSignals: 'Monitored signals',
      possibleChain: 'Possible chain',
      evaluateInfrastructureScenario: 'Evaluate infrastructure scenario',
      objectAuthorizationFailed: 'Object authorization failed',
      unsafeTemplateInputDetected: 'Unsafe template input detected',
      podPrivileged: 'Pod privileged',
      serviceAccountCanReadSecrets: 'Service account can read secrets',
      cloudIamWildcardPermissions: 'Cloud IAM wildcard permissions',
      weakTrustPolicy: 'Weak trust policy',
      secretExposureDetected: 'Secret exposure detected',
      azureStorageToIdentityChainReaction:
        'Azure storage-to-identity chain reaction',
      publicStorageExposureDetected: 'Public storage exposure detected',
      certificateExposureDetected: 'Certificate exposure detected',
      servicePrincipalOverprivileged: 'Service principal overprivileged',
      deploymentCredentialsEnabled: 'Deployment credentials enabled',
      managedIdentityExcessiveScope: 'Managed identity excessive scope',
      passwordResetPrivilegeDetected: 'Password reset privilege detected',
      identityMonitoringGap: 'Identity monitoring gap',
      containerKubernetesHardeningFailure:
        'Container and Kubernetes hardening failure',
      dockerfileSecretsDetected: 'Dockerfile secrets detected',
      imageUsesLatestTag: 'Image uses latest tag',
      containerRunsAsRoot: 'Container runs as root',
      plaintextSecretsInManifest: 'Plaintext secrets in manifest',
      missingSecurityContext: 'Missing Kubernetes securityContext',
      serviceAccountTokenMounted: 'ServiceAccount token mounted',
      rbacWildcardPermissions: 'RBAC wildcard permissions',
      canReadKubernetesSecrets: 'Can read Kubernetes secrets',
      networkPolicyMissing: 'NetworkPolicy missing',
      resourceLimitsMissing: 'Resource limits missing',
      cisAuditMissing: 'CIS audit missing',
      hardeningVerificationMissing: 'Hardening verification missing',
      containerKubernetesHardening: 'Container and Kubernetes Hardening',
      containerKubernetesHardeningEvidencePackage:
        'Container and Kubernetes Hardening Evidence Package',
      containerKubernetesHardeningReviewCase:
        'Container and Kubernetes Hardening Review Case',
      runtimeHardeningFailure: 'Runtime hardening failure',
      devSecOpsVerificationEvidence: 'DevSecOps verification evidence',
      azureStorageToIdentityRisk: 'Azure Storage to Identity Risk',
      azureStorageToIdentityRiskEvidencePackage:
        'Azure Storage to Identity Risk Evidence Package',
      azureStorageToIdentityRiskReviewCase:
        'Azure Storage to Identity Risk Review Case',
      cloudIdentitySecurity: 'Cloud Identity Security',
      storageToIdentityChainContainment:
        'Storage-to-identity chain containment',
      applicationSecurity: 'Application Security',
      kubernetesSecurity: 'Kubernetes Security',
      cloudIamSecurity: 'Cloud IAM Security',
      secretsSecurity: 'Secrets Security',
      auditEvidence: 'Audit Evidence',
      riskOperations: 'Risk Operations',
      goldenRuleItems: [
        'Do not trust client-controlled IDs.',
        'Enforce object-level authorization.',
        'Users may provide data, not executable templates.',
        'Web workloads should not read secrets by default.',
        'Kubernetes RBAC must be least privilege.',
        'Cloud IAM trust must be bound to specific workloads.',
        'IAM permissions must avoid wildcards.',
        'Secrets must be scoped, rotated, and never logged.',
        'Logs must connect application, Kubernetes, IAM, secrets, and data access.',
        'One weak layer must not become full compromise.',
      ],
      prototypeDisclaimer:
        'Aurora Digital Assets is a concept prototype. Infrastructure security controls, events, scenarios, risk scores, and audit records are fictional deterministic demo data only.',
    },
    riskOperations: {
      title: 'Risk Operations Console',
      subtitle:
        'Unified internal view for financial crime alerts, compliance reasoning, evidence readiness, operational incidents, and staff action priorities.',
      operatingMode: 'Operating mode',
      highestPriority: 'Highest priority',
      commandSummary: 'Command summary',
      noOverview: 'No overview loaded',
      staffPriorities: 'Staff priorities',
      actionQueue: 'Action queue',
      crossModuleEvents: 'Cross-module events',
      unifiedTimeline: 'Unified timeline',
      escalations: 'Escalations',
      escalationSummary: 'Escalation summary',
      recommendedFocus: 'Recommended focus',
      operationalBoundary: 'Operational boundary',
      operationalBoundaryCopy:
        'This console does not process real bank data. It orchestrates fictional prototype outputs from monitoring, compliance intelligence, evidence readiness, and resilience modules.',
      sourceModule: 'Source module',
      sourceId: 'Source ID',
      requiredAction: 'Required action',
      relatedLinks: 'Related links',
      relatedEntity: 'Related entity',
      openItems: 'Open items',
      blockedItems: 'Blocked items',
      readyItems: 'Ready items',
      noMissingEvidence: 'No missing evidence recorded.',
      prepareReviewCase: 'Prepare review case',
      reviewCasePrepared: 'Review case prepared',
      reviewCaseId: 'Review case ID',
      auditEventCreated: 'Audit event created',
      recommendedNextAction: 'Recommended next action',
    },
    reviewCaseLifecycle: {
      title: 'Review Case Lifecycle & Decision Engine',
      caseLifecycle: 'Case lifecycle',
      currentStatus: 'Current status',
      previousStatus: 'Previous status',
      allowedNextStatuses: 'Allowed next statuses',
      startReview: 'Start review',
      markActionRequired: 'Mark action required',
      startMitigation: 'Start mitigation',
      markMitigated: 'Mark mitigated',
      closeCase: 'Close case',
      decisionNote: 'Decision note',
      mitigationAction: 'Mitigation action',
      lifecycleProgress: 'Lifecycle progress',
      reviewerAction: 'Reviewer action',
      evidenceReviewed: 'Evidence reviewed',
      mitigationRequested: 'Mitigation requested',
      mitigationStarted: 'Mitigation started',
      mitigationVerified: 'Mitigation verified',
      caseClosed: 'Case closed',
      finalDecision: 'Final decision',
      closureReady: 'Closure ready',
      recommendedNextStatus: 'Recommended next status',
      continueLifecycleInComplianceReview:
        'Continue lifecycle in Compliance Review',
    },
    prototypeBoundary: {
      independentConceptPrototype: 'Independent concept prototype',
      noRealCustomerData: 'No real customer data',
      noRealBankingSystemsConnected: 'No real banking systems connected',
      noRealLegalReport: 'No real legal report is generated',
      fictionalDemoData: 'Fictional deterministic demo data only',
      prototypeBoundary: 'Prototype boundary',
    },
  },
  es: {
    common: {
      continue: 'Continuar',
      back: 'Volver',
      loading: 'Cargando',
      error: 'Error',
      review: 'Revisar',
      reports: 'Reportes',
      status: 'Estado',
      ready: 'Listo',
      notReady: 'No listo',
      critical: 'Crítico',
      high: 'Alto',
      medium: 'Medio',
      low: 'Bajo',
      new: 'Nuevo',
      underReview: 'En revisión',
      escalated: 'Escalado',
      closed: 'Cerrado',
      required: 'Requerido',
      optional: 'Opcional',
      missing: 'Faltante',
      included: 'Incluido',
      reviewerRequired: 'Requiere revisor',
      yes: 'Sí',
      no: 'No',
      cancel: 'Cancelar',
      language: 'Idioma',
      english: 'Inglés',
      spanish: 'Español',
      auditEventCreated: 'Evento de auditoría creado',
      auditEventId: 'ID de evento de auditoría',
      correlationId: 'ID de correlación',
      traceabilityRecord: 'Registro de trazabilidad',
      sensitiveActionRecorded: 'Acción sensible registrada',
      safetyBoundaryText:
        'Prototipo local y determinístico. Sin activos reales, sin custodia real, sin integración bancaria real, sin integración real con custodios, sin ejecución blockchain real, sin despliegue cloud real y sin llaves privadas ni secretos.',
      humanApprovalIntegrityPrinciple:
        'La revisión humana no es un ancla de confianza. Es un evento de riesgo controlado.',
      agentGovernancePrinciple:
        'Todo agente debe ser identificable, limitado por permisos, revocable y auditable.',
    },
    phrases: esPhrases,
    navigation: {
      home: 'Inicio',
      payments: 'Pagos',
      accounts: 'Cuentas',
      cardsAndCurrency: 'Tarjetas y moneda',
      loans: 'Créditos',
      investments: 'Inversiones',
      insurance: 'Seguros',
      digitalAssets: 'Activos digitales',
      documents: 'Documentos',
      onlineServices: 'Servicios en línea',
      logOut: 'Cerrar sesión',
      hideBalances: 'Ocultar saldos',
      showBalances: 'Mostrar saldos',
      onlineBankingDemo: 'Demo de banca en línea',
      mainNavigation: 'Navegación principal',
    },
    paymentDemo: paymentDemoEs,
    accountDemo: accountDemoEs,
    cardDemo: cardDemoEs,
    loanDemo: loanDemoEs,
    insuranceDemo: insuranceDemoEs,
    investmentDemo: investmentDemoEs,
    onlineServices: onlineServicesEs,
    bankHome: {
      publicConcept: 'Concepto de sitio bancario público',
      logIn: 'Iniciar sesión',
      logInEbanking: 'Iniciar sesión en eBanking',
      heroTitle: 'Servicios bancarios para la vida diaria',
      heroSubtitle:
        'Acceda a cuentas, pagos, documentos y servicios elegibles de activos digitales mediante una relación bancaria formal.',
      learnDigitalAssets: 'Conocer Aurora Digital Assets',
      formalAccess: 'Acceso bancario formal',
      servicesEyebrow: 'Servicios y situaciones de vida',
      servicesTitle: '¿Cómo puede ayudar Aurora Bank?',
      publicInformation: 'Información pública',
      explore: 'Explorar',
      integratedTitle: 'Integrado en la banca en línea',
      eligibilityApplies: 'Sujeto a elegibilidad',
      securityInformation: 'Información de seguridad',
      officialChannels: 'Use canales bancarios oficiales',
      logInSecurely: 'Iniciar sesión de forma segura',
      becomeCustomer: 'Hacerse cliente',
      contactOnboarding: 'Contacto e incorporación',
      contactBank: 'Contactar Aurora Bank',
      readServiceInfo: 'Leer información del servicio',
      services: [
        {
          title: 'Cuentas y pagos',
          description:
            'Conceptos de cuentas y pagos cotidianos para clientes con relación con Aurora Bank.',
        },
        {
          title: 'Concepto de crédito hipotecario',
          description:
            'Orientación estructurada para decisiones importantes dentro de una relación bancaria formal.',
        },
        {
          title: 'Ahorro e inversiones',
          description:
            'Información clara y conceptos de planificación responsable para finanzas a largo plazo.',
        },
        {
          title: 'Módulo de activos digitales',
          description:
            'Los clientes elegibles pueden acceder a servicios simulados de activos digitales mediante eBanking autenticado.',
        },
        {
          title: 'Servicio al cliente',
          description:
            'Canales de soporte para consultas bancarias, documentos e información de servicio.',
        },
        {
          title: 'Seguridad y autenticación fuerte',
          description:
            'Las credenciales emitidas por el banco y la autenticación fuerte protegen el acceso a servicios personales.',
        },
      ],
      publicNavigation: [
        'Para usted',
        'Para empresas',
        'Banca privada',
        'Banca diaria',
        'Servicio al cliente',
        'Activos digitales',
        'Documentos',
      ],
    },
    bankLogin: {
      securePrototype: 'Prototipo seguro de eBanking',
      simulatedAccess: 'Acceso bancario simulado',
      bankManagedAccess: 'Acceso gestionado por el banco',
      title: 'Iniciar sesión en Aurora eBanking',
      subtitle:
        'El acceso a Aurora Digital Assets se modela como disponible solo después de que el banco establezca una sesión autenticada y confirme la elegibilidad.',
      simulatedSignIn: 'Inicio simulado',
      stepOne: 'Paso 1 de 2',
      stepTwo: 'Paso 2 de 2',
      credentials: 'Credenciales',
      bankIssuedAccess: 'Acceso emitido por el banco',
      credentialsHelp:
        'Use el identificador de cliente emitido por el banco y la credencial secreta proporcionada mediante el proceso formal de incorporación.',
      customerId: 'ID de cliente',
      secretCredential: 'Credencial secreta',
      checking: 'Comprobando...',
      confirmMobileKey: 'Confirmar con clave móvil',
      strongAuthentication: 'Autenticación fuerte',
      mobileApprovalSent:
        'Se ha enviado una solicitud de aprobación simulada a la aplicación bancaria de autenticación del cliente.',
      action: 'Acción',
      loginRequest: 'Solicitud de inicio de sesión',
      service: 'Servicio',
      customer: 'Cliente',
      approvalMethod: 'Método de aprobación',
      deviceApprovalRequired: 'Se requiere aprobación del dispositivo',
      timeLimit: 'Límite de tiempo',
      sessionExpires: 'La sesión expira en 02:00',
      processingApproval: 'Procesando aprobación...',
      approveLogin: 'Aprobar inicio simulado',
      securityNote: 'Nota de seguridad',
      protectIdentifiers: 'Proteja sus identificadores',
      protectIdentifiersCopy:
        'El banco nunca solicita sus identificadores por correo electrónico o mensaje de texto. Acceda siempre a eBanking mediante el canal bancario oficial.',
      onboardingBoundary: 'Límite de incorporación',
      bankManagedOnboarding: 'Incorporación gestionada por el banco',
      productBoundary: 'Límite del producto',
      prototypeOnly: 'Solo prototipo',
      onboardingItems: [
        'Cliente incorporado por el banco',
        'Documentos revisados por el banco',
        'Origen de fondos revisado por el banco',
        'Credenciales emitidas por el banco',
        'Autenticación fuerte requerida',
      ],
    },
    dashboard: {
      welcomeBack: 'Bienvenido de nuevo',
      financialOverview: 'Resumen financiero',
      subtitle:
        'Revise sus cuentas, pagos y activos digitales desde un único entorno bancario.',
      strongAuthActive: 'Autenticación fuerte activa',
      accounts: 'Cuentas',
      yourAccounts: 'Sus cuentas',
      newPayment: 'Nuevo pago',
      loadingDashboard: 'Cargando datos del panel...',
      dashboardLoaded: 'Datos del panel cargados desde el prototipo local FastAPI.',
      digitalAssets: 'Activos digitales',
      wallet: 'Billetera Aurora Digital Assets',
      conceptModule: 'Módulo conceptual',
      backendModule: 'Módulo backend',
      totalDigitalAssetsValue: 'Valor total de activos digitales',
      volatilityNotice:
        'Los activos digitales son volátiles y están separados de los depósitos bancarios.',
      custodyStatus: 'Estado de custodia',
      buy: 'Comprar',
      sell: 'Vender',
      withdraw: 'Retirar',
      notifications: 'Notificaciones',
      importantMessages: 'Mensajes importantes',
      userProtection: 'Protección del usuario',
      riskNotice: 'Aviso de riesgo de activos digitales',
      riskNoticeCopy:
        'Los criptoactivos pueden perder valor rápidamente. Las transferencias a billeteras externas son irreversibles y pueden requerir revisión adicional de seguridad.',
      readRiskInformation: 'Leer información de riesgo',
      protectionStatus: 'Estado de protección',
      protection: 'Protección de activos digitales',
    },
    digitalAssetsPage: {
      eyebrow: 'Activos digitales',
      heroSubtitle:
        'Ver saldos de activos digitales, estado de custodia, actividad reciente y controles de gobernanza de rails de activos desde un entorno simulado de banca en línea.',
      assetRailPhase: 'Fase 27',
      assetRailGovernance: 'Gobernanza de rails de activos',
      assetRailBody:
        'Aurora clasifica el rail del activo antes de aplicar controles de custodia, liquidación, cumplimiento, evidencia y aprobación.',
      controlModelFirst: 'Modelo de control primero',
      rail: 'Rail:',
      controlModel: 'Modelo de control',
      governanceExample: 'Ejemplo de gobernanza',
      openStaffGovernanceView: 'Abrir vista de gobernanza staff',
      viewAuditTrail: 'Ver trazabilidad de auditoría',
      digitalEuroNotBtc: 'El euro digital no se modela como BTC',
      digitalEuroNotBtcBody:
        'El euro digital / CBDC se modela como dinero de banco central distribuido o intermediado por bancos o proveedores de servicios de pago supervisados. Aurora no aplica controles de custodio cripto externo por defecto a rails de euro digital.',
      cryptoassetControlPath: 'Ruta de control de criptoactivos',
      cryptoassetsDifferentPath:
        'Los criptoactivos usan una ruta de control distinta',
      cryptoassetsDifferentPathBody:
        'Los activos tipo BTC / ETH pueden requerir preparación de custodio, límites de billetera, límites de llaves privadas, límites de ejecución blockchain, integridad de aprobación humana y controles de gobernanza de agentes antes de considerar operaciones sensibles.',
      safetyNotice:
        'Prototipo local determinístico solamente. No se usa ni ejecuta euro digital, CBDC, stablecoin, criptoactivo, custodia, PSP, banca, blockchain, pago, liquidación, redención, transferencia, datos de cliente, llave privada, credencial o secreto real. No es asesoría legal ni certificación regulatoria.',
      assetRailRows: [
        {
          name: 'Euro digital / CBDC',
          rail: 'Rail de dinero de banco central intermediado por PSP',
          controlModel: 'Sin custodio cripto externo por defecto',
        },
        {
          name: 'Depósito tokenizado',
          rail: 'Rail de libro interno bancario',
          controlModel: 'Pasivo bancario y controles internos bancarios',
        },
        {
          name: 'Stablecoin regulada / EMT',
          rail: 'Rail de emisor regulado',
          controlModel: 'Controles de emisor, reservas y redención',
        },
        {
          name: 'Criptoactivo',
          rail: 'Rail de custodia cripto externa o ejecución blockchain',
          controlModel:
            'Controles de custodia, billetera, llaves privadas y ejecución blockchain',
        },
        {
          name: 'Token valor',
          rail: 'Rail de liquidación de valores',
          controlModel: 'Controles de valores y gobernanza de liquidación',
        },
      ],
    },
    bankStaffWorkspace: {
      protectedArea: 'Área interna protegida del banco',
      title: 'Espacio interno del banco',
      subtitle:
        'Espacio conceptual interno para incorporación, acceso autorizado por el cliente, revisión de cumplimiento, reportes y administración demo.',
      authenticatedSession: 'Sesión autenticada',
      workspaceModules: 'Módulos del espacio',
      staffTools: 'Herramientas internas',
      conceptPrototype: 'Prototipo conceptual',
      prototypeControls: 'Controles del prototipo',
      staffBoundary: 'Límite interno',
      accessModel: 'Modelo de acceso',
      commonActions: 'Acciones comunes',
      operatingGuardrails: 'Controles operativos',
      modules: {
        onboarding: 'Incorporación de clientes',
        customerAccess: 'Autorización de acceso a clientes',
        riskOperations: 'Consola de operaciones de riesgo',
        trustEngine: 'Motor de Confianza Aurora',
        apiSecurity: 'Centro de control de seguridad API',
        infrastructureSecurity:
          'Centro de control de seguridad de infraestructura',
        cryptoAgility: 'Centro de control de agilidad criptográfica',
        assetRailGovernance: 'Gobernanza de rails de activos',
        sensitiveApproval:
          'Motor de Aprobación de Operaciones Sensibles',
        complianceReview: 'Revisión de cumplimiento',
        financialCrime: 'Monitoreo de delitos financieros',
        complianceIntelligence: 'Inteligencia de cumplimiento',
        evidencePackages: 'Paquetes de evidencia',
        operationalResilience: 'Resiliencia operacional',
        reportsAuditTrail: 'Reportes y trazabilidad de auditoría',
        demoAdministration: 'Administración demo',
      },
      moduleDescriptions: {
        onboarding:
          'Revisar el modelo de incorporación gestionado por el banco antes de habilitar servicios de activos digitales.',
        customerAccess:
          'Buscar un cliente demo y solicitar acceso temporal autorizado por el cliente.',
        riskOperations:
          'Vista de comando unificada para alertas, incidentes, preparación de evidencia, escalaciones, operaciones pausadas y prioridades del equipo.',
        trustEngine:
          'Capa compartida de orquestación para módulos de riesgo, políticas, evidencia, evaluación, control, regulación y conocimiento.',
        apiSecurity:
          'Monitorear acciones sensibles del backend, autorización por resolver, límites por acción de negocio, exposición de esquema, autenticación reforzada y auditoría.',
        infrastructureSecurity:
          'Monitorear riesgos de reacción en cadena desde aplicación hacia cloud, incluyendo autorización backend, RBAC de Kubernetes, IAM, secretos, evidencia de auditoría y operaciones de riesgo.',
        cryptoAgility:
          'Controlar inventario criptográfico, versionado de algoritmos, rotación de claves, riesgo de confidencialidad a largo plazo y preparación para migración post-cuántica.',
        assetRailGovernance:
          'Clasificar euro digital, depósitos tokenizados, stablecoins, criptoactivos y tokens valor antes de aplicar la ruta de control correcta.',
        sensitiveApproval:
          'Modelar aprobación reforzada de estilo bancario, aprobación móvil simulada, decisión de riesgo backend, evidencia de auditoría y enrutamiento a revisión.',
        complianceReview:
          'Revisar resultados simulados de monitoreo transaccional, controles de riesgo de billetera y evidencia de escalamiento.',
        financialCrime:
          'Revisar riesgo interno, indicadores de empresas de fachada, depósitos estructurados, riesgo de salida hacia criptoactivos, riesgo de transferencias extranjeras y actividad sospechosa vinculada a redes.',
        complianceIntelligence:
          'Explicar alertas de delitos financieros, revisar controles activados, identificar evidencia faltante y preparar orientación para revisores antes del escalamiento.',
        evidencePackages:
          'Preparar paquetes estructurados de evidencia para revisión de cumplimiento, auditoría, investigación y documentación orientada a reguladores.',
        operationalResilience:
          'Monitorear degradación de servicios, fallas de dependencias, modos de respaldo, impacto en clientes y controles de continuidad.',
        reportsAuditTrail:
          'Abrir reportes para clientes, conceptos de reporte fiscal y evidencia de auditoría del prototipo.',
        demoAdministration:
          'Inspeccionar y restablecer datos locales del prototipo usados por el entorno demo de Aurora Digital Assets.',
      },
      statuses: {
        bankStaffControl: 'Control interno del banco',
        customerAuthorization: 'Autorización del cliente',
        orchestrationLayer: 'Capa de orquestación',
        sharedOrchestration: 'Orquestación compartida',
        backendSecurityLayer: 'Capa de seguridad backend',
        crossLayerSecurity: 'Seguridad transversal',
        cryptoAgility: 'Agilidad criptográfica',
        railClassification: 'Clasificación de rail',
        stepUpApproval: 'Aprobación reforzada',
        complianceReview: 'Revisión de cumplimiento',
        monitoringAlerts: 'Alertas de monitoreo',
        reasoningLayer: 'Capa de razonamiento',
        packageReadiness: 'Preparación de paquetes',
        resilienceCommand: 'Comando de resiliencia',
        auditEvidence: 'Evidencia de auditoría',
        prototypeOnly: 'Solo prototipo',
      },
    },
    assetRailGovernance: {
      eyebrow: 'Gobernanza de rails de activos',
      title: 'Motor de gobernanza de rails de activos',
      subtitle:
        'Clasificar rails de activos digitales antes de aplicar controles de custodia, liquidación, cumplimiento, evidencia y aprobación.',
      phase: 'Fase',
      mode: 'Modo',
      backendTests: 'Pruebas backend',
      backendTestsPassing: '204 aprobadas',
      realIntegrations: 'Integraciones reales',
      realAssets: 'Activos reales',
      externalExecution: 'Ejecución externa',
      localDeterministicPrototype: 'Prototipo local determinístico',
      disabled: 'Deshabilitada',
      classificationEyebrow: 'Ruta de gobernanza',
      classificationTitle: 'Clasificación de rails de activos',
      classificationText:
        'Aurora separa euro digital / CBDC, depósitos tokenizados, stablecoins reguladas, criptoactivos y tokens valor en diferentes rutas de gobernanza.',
      controlModelFirst: 'Modelo de control primero',
      rail: 'Rail:',
      custody: 'Custodia',
      controls: 'Controles',
      classified: 'Clasificado',
      decisionMatrixEyebrow: 'Controles determinísticos',
      decisionMatrixTitle: 'Matriz de decisión',
      deterministic: 'Determinístico',
      required: 'Requerido',
      coreMessage: 'Mensaje central',
      firstClassify: 'Primero clasificar, luego controlar',
      coreMessageText:
        'Aurora no debe asumir que todos los activos digitales requieren la misma arquitectura de custodia o liquidación. Aurora primero clasifica el rail del activo y luego aplica el modelo de control correcto.',
      digitalEuroEyebrow: 'Rail de dinero de banco central',
      digitalEuroTitle: 'El euro digital no se modela como criptoactivo',
      cryptoassetEyebrow: 'Rail de ejecución externa',
      cryptoassetTitle: 'Los criptoactivos requieren una ruta de control distinta',
      evidenceEyebrow: 'Evidencia y revisión',
      evidenceTitle: 'Rutas de revisión',
      safetyNotice: 'Aviso de seguridad',
      prototypeBoundary: 'Límite del prototipo',
      safetyNoticeText:
        'Interfaz local determinística de gobernanza de rails de activos solamente. No se usa ni ejecuta euro digital, CBDC, stablecoin, criptoactivo, custodia, PSP, banca, blockchain, cloud, pago, redención, liquidación, transferencia, datos de cliente, llave privada, credencial o secreto real. No es asesoría legal ni certificación regulatoria.',
      rails: [
        {
          name: 'Euro digital / CBDC',
          rail: 'Rail de dinero de banco central intermediado por PSP',
          custody: 'Sin custodio cripto externo por defecto',
          controls:
            'Intermediación PSP, controles de privacidad, límites de tenencia, modo offline/online, AML, revisión de evidencia',
        },
        {
          name: 'Depósito tokenizado',
          rail: 'Rail de libro interno bancario',
          custody: 'Pasivo bancario / infraestructura bancaria interna',
          controls:
            'Controles de libro bancario, controles de liquidación, integridad de aprobación humana, resiliencia operacional',
        },
        {
          name: 'Stablecoin regulada / EMT',
          rail: 'Rail de emisor regulado',
          custody: 'Depende del modelo de servicio',
          controls:
            'Gobernanza de emisor, gobernanza de reservas, gobernanza de redención, AML, revisión de evidencia',
        },
        {
          name: 'Token referenciado a activos',
          rail: 'Rail de emisor de token referenciado a activos',
          custody: 'Depende del emisor, reservas y modelo de servicio',
          controls:
            'Gobernanza de emisor, gobernanza de reservas, gobernanza de redención, revisión de cumplimiento',
        },
        {
          name: 'Criptoactivo',
          rail: 'Rail de custodia cripto externa o ejecución blockchain',
          custody: 'Puede requerir custodio externo regulado',
          controls:
            'Preparación del custodio, límite de billetera, límite de llave privada, límite de ejecución blockchain, gobernanza de agentes',
        },
        {
          name: 'Token valor',
          rail: 'Rail de liquidación de valores',
          custody: 'Gobernanza de custodia y liquidación de valores',
          controls:
            'Controles de valores, controles de liquidación, revisión de cumplimiento, revisión de evidencia',
        },
      ],
      digitalEuroPoints: [
        'El euro digital / CBDC se modela como dinero de banco central distribuido o intermediado por bancos o proveedores de servicios de pago supervisados.',
        'No se trata como BTC, ETH o un criptoactivo genérico con custodia externa.',
        'Los controles de custodio cripto externo no se aplican por defecto.',
        'La ejecución blockchain y los controles de llave privada no se asumen por defecto.',
      ],
      cryptoassetPoints: [
        'Los activos tipo BTC / ETH pueden requerir controles de preparación del custodio.',
        'Los límites de billetera, llave privada y ejecución blockchain se vuelven relevantes.',
        'Los controles de integridad de aprobación humana y gobernanza de agentes deben aplicarse antes de considerar cualquier operación sensible.',
        'No se realiza custodia real ni ejecución blockchain en este prototipo.',
      ],
      reviewLinks: {
        evidencePackages: 'Paquetes de evidencia',
        riskOperations: 'Operaciones de riesgo',
        humanApprovalIntegrity: 'Integridad de aprobación humana',
        agentGovernance: 'Gobernanza de agentes',
        cryptoAgility: 'Agilidad criptográfica',
        auditTrail: 'Trazabilidad de auditoría',
      },
    },
    trustEngine: {
      eyebrow: 'Motor de Confianza Aurora',
      title: 'Capa compartida de inteligencia y orquestación',
      subtitle:
        'Coordina capas de riesgo, políticas, evidencia, evaluación, regulación, control y conocimiento en operaciones reguladas de activos digitales.',
      mode: 'Modo',
      localDeterministicPrototype: 'Prototipo local determinístico',
      realIntegrations: 'Integraciones reales',
      realAssets: 'Activos reales',
      externalExecution: 'Ejecución externa',
      disabled: 'deshabilitada',
      evidence: 'Evidencia',
      reviewable: 'Revisable',
      controlModel: 'Modelo de control',
      layered: 'En capas',
      orchestrationMap: 'Mapa de orquestación',
      trustEngineMap: 'Mapa del Motor de Confianza',
      sharedLayer: 'Capa compartida',
      coreMessage:
        'El Motor de Confianza Aurora coordina capas de riesgo, políticas, evidencia, evaluación, control, regulación y conocimiento antes de que puedan proceder decisiones sensibles bancarias o de activos digitales.',
      coordinated: 'Coordinado',
      connectedAurora: 'Aurora conectado',
      connectedModules: 'Módulos Aurora conectados',
      reviewLinks: 'Enlaces de revisión',
      open: 'Abrir',
      corePrinciple: 'Principio central',
      beforeSensitiveDecision: 'Antes de decisiones sensibles',
      deterministicFlow: 'Flujo determinístico',
      trustFlow: 'Flujo de confianza',
      step: 'Paso',
      safetyBoundary: 'Límite de seguridad',
      prototypeBoundary: 'Límite del prototipo',
      safetyBoundaryText:
        'Interfaz local determinística del motor de confianza solamente. No se usa ni ejecuta banca, custodia, PSP, euro digital, CBDC, stablecoin, criptoactivo, blockchain, cloud, pago, liquidación, transferencia, datos de cliente, llave privada, credencial o secreto real. No es asesoría legal ni certificación regulatoria.',
      engineRows: [
        {
          name: 'Motor de riesgo',
          description:
            'Evalúa riesgo operacional, de custodia, pago, rail de activo y aprobación',
        },
        {
          name: 'Motor de políticas',
          description:
            'Aplica políticas de control determinísticas antes de cambios de estado',
        },
        {
          name: 'Motor de evidencia',
          description:
            'Crea paquetes de evidencia listos para auditoría y enlaces de revisión',
        },
        {
          name: 'Motor de evaluación',
          description:
            'Clasifica escenarios, brechas, controles y preparación',
        },
        {
          name: 'Motor de control',
          description: 'Bloquea o enruta operaciones sensibles',
        },
        {
          name: 'Motor regulatorio',
          description:
            'Mapea conceptos regulatorios a requisitos de control',
        },
        {
          name: 'Motor de conocimiento',
          description:
            'Preserva lógica institucional de control y explicabilidad',
        },
      ],
      connectedLinks: {
        assetRailGovernance: 'Gobernanza de rails de activos',
        riskOperations: 'Operaciones de riesgo',
        evidencePackages: 'Paquetes de evidencia',
        complianceIntelligence: 'Inteligencia de cumplimiento',
        humanApprovalIntegrity: 'Integridad de aprobación humana',
        agentGovernance: 'Gobernanza de agentes',
        cryptoAgility: 'Agilidad criptográfica',
        auditTrail: 'Trazabilidad de auditoría',
      },
      trustFlowSteps: [
        'Señal',
        'Clasificación',
        'Política',
        'Puntaje de riesgo',
        'Evidencia',
        'Revisión',
        'Integridad de aprobación',
        'Decisión controlada',
      ],
    },
    financialCrimeMonitoring: {
      title: 'Monitoreo de Delitos Financieros',
      subtitle:
        'Vista interna de monitoreo para riesgo interno, patrones transaccionales sospechosos, indicadores de empresas de fachada, riesgo de salida hacia criptoactivos y escalamiento basado en evidencia.',
      activeAlerts: 'Alertas activas',
      criticalAlerts: 'Alertas críticas',
      monitoringControls: 'Controles de monitoreo',
      reviewReadyCases: 'Casos listos para revisión',
      alertQueue: 'Cola de alertas',
      demoAlerts: 'Alertas demo',
      evaluateActivity: 'Evaluar actividad',
      complianceIntelligence: 'Inteligencia de cumplimiento',
    },
    complianceIntelligence: {
      title: 'Inteligencia de Cumplimiento',
      subtitle:
        'Capa interna de razonamiento para explicar alertas de delitos financieros, evidencia requerida, orientación para revisores y decisiones de escalamiento.',
      riskExplanations: 'Explicaciones de riesgo',
      alertReasoning: 'Razonamiento de alertas',
      reviewerGuidance: 'Guía para revisores',
      explainAlert: 'Explicar alerta',
      prepareReviewCase: 'Preparar caso de revisión',
      decisionPath: 'Ruta de decisión',
      evidenceRequirements: 'Requisitos de evidencia',
      reviewerNextSteps: 'Próximos pasos del revisor',
      prepareEvidencePackage: 'Preparar evidencia',
    },
    evidencePackages: {
      title: 'Paquetes de Evidencia',
      subtitle:
        'Capa interna de preparación de evidencia para revisión de cumplimiento, auditoría, investigación y documentación orientada a reguladores.',
      packageReadiness: 'Preparación de paquetes',
      packageQueue: 'Cola de paquetes',
      evidencePackageList: 'Lista de paquetes de evidencia',
      packageTemplates: 'Plantillas de paquetes',
      evidenceStructures: 'Estructuras de evidencia',
      packageGenerator: 'Generador de paquetes',
      generateDemo: 'Generar paquete de evidencia demo',
      readinessExplanation: 'Explicación de preparación',
      totalPackages: 'Total de paquetes',
      readyPackages: 'Paquetes listos',
      incompletePackages: 'Paquetes incompletos',
      averageReadiness: 'Preparación promedio',
      includedEvidence: 'Evidencia incluida',
      missingEvidence: 'Evidencia faltante',
      triggeredControls: 'Controles activados',
      reviewerNotes: 'Notas del revisor',
      decisionRationale: 'Fundamento de decisión',
      timeline: 'Línea de tiempo',
      recommendedNextAction: 'Próxima acción recomendada',
      readinessScore: 'Puntaje de preparación',
      riskType: 'Tipo de riesgo',
      created: 'Creado',
      summary: 'Resumen',
      sourceType: 'Tipo de fuente',
      sourceId: 'ID de fuente',
      packageType: 'Tipo de paquete',
      reviewerId: 'ID del revisor',
      generatePackage: 'Generar paquete',
      packageTitle: 'Título del paquete',
      exportAvailable: 'Exportación disponible',
      userMessage: 'Mensaje al usuario',
      generateEvidenceFromAuditEvent:
        'Generar evidencia desde evento de auditoría',
      generateFromAuditEvent: 'Generar desde evento de auditoría',
      infrastructureChainReactionAuditEvent:
        'Reacción en cadena de seguridad de infraestructura',
      useInfrastructureChainReactionAuditEvent:
        'Usar evento de auditoría de reacción en cadena de infraestructura',
      infrastructureEvidencePackage:
        'Paquete de evidencia de seguridad de infraestructura',
      crossLayerAuditEvidence: 'Evidencia de auditoría entre capas',
      applicationToCloudChainReaction:
        'Reacción en cadena de aplicación a nube',
      azureStorageToIdentityRisk: 'Riesgo de Azure Storage a identidad',
      cryptoAgilityPqReadiness:
        'Preparación post-cuántica de agilidad criptográfica',
      azureStorageToIdentityRiskEvidencePackage:
        'Paquete de evidencia de riesgo de Azure Storage a identidad',
      azureStorageToIdentityRiskReviewCase:
        'Caso de revisión de riesgo de Azure Storage a identidad',
      openReviewCase: 'Abrir caso de revisión',
      reviewCaseCreated: 'Caso de revisión creado',
      sourceEvidencePackage: 'Paquete de evidencia fuente',
      linkedEvidencePackage: 'Paquete de evidencia vinculado',
      infrastructureSecurityChainReactionReviewCase:
        'Caso de revisión de reacción en cadena de seguridad de infraestructura',
      createFormalReviewCaseFromEvidencePackage:
        'Crear un caso formal de revisión desde este paquete de evidencia.',
      evidenceToReviewTraceability: 'Trazabilidad de evidencia a revisión',
      complianceReviewLinkage: 'Vinculación con revisión de cumplimiento',
      auditLinkedEvidence: 'Evidencia vinculada a auditoría',
      sourceAuditEventId: 'ID de evento de auditoría origen',
      traceabilitySummary: 'Resumen de trazabilidad',
      linkedAuditEvents: 'Eventos de auditoría vinculados',
      backendDecision: 'Decisión del backend',
      auditLinkedEvidenceCopy:
        'Los paquetes de evidencia ahora pueden prepararse desde eventos de auditoría estructurados, preservando la decisión del backend, el ID de correlación, el módulo de origen y el contexto de revisión.',
      recommendedActions: 'Acciones recomendadas',
      blockers: 'Bloqueos',
      warnings: 'Advertencias',
      noBlockers: 'No hay bloqueos registrados.',
      noWarnings: 'No hay advertencias registradas.',
      noIncludedEvidence: 'No se ha adjuntado evidencia incluida.',
      noMissingEvidence: 'No hay evidencia faltante registrada.',
    },
    operationalResilience: {
      title: 'Resiliencia Operacional',
      subtitle:
        'Vista interna de comando para degradación de servicios, fallas de dependencias, modos de respaldo, impacto en clientes y controles de continuidad.',
      servicesMonitored: 'Servicios monitoreados',
      activeIncidents: 'Incidentes activos',
      fallbackModes: 'Modos de respaldo',
      highImpactServices: 'Servicios de alto impacto',
      serviceHealth: 'Salud del servicio',
      incidentQueue: 'Cola de incidentes',
      dependencies: 'Dependencias',
      criticalDependencies: 'Dependencias críticas',
      controls: 'Controles',
      resilienceControls: 'Controles de resiliencia',
      scenarioDemo: 'Demo de escenario',
      evaluateScenario: 'Evaluar escenario',
      scenario: 'Escenario',
      affectedService: 'Servicio afectado',
      dependencyStatus: 'Estado de dependencia',
      customerImpact: 'Impacto en clientes',
      evaluateResilienceScenario: 'Evaluar escenario de resiliencia',
      resilienceScore: 'Puntaje de resiliencia',
      severity: 'Severidad',
      decision: 'Decisión',
      controlsActivated: 'Controles activados',
      availableOperations: 'Operaciones disponibles',
      pausedOperations: 'Operaciones pausadas',
      recommendedAction: 'Acción recomendada',
      explanation: 'Explicación',
      availability: 'Disponibilidad',
      fallbackAvailable: 'Respaldo disponible',
      currentMode: 'Modo actual',
      summary: 'Resumen',
      failureType: 'Tipo de falla',
      fallbackMode: 'Modo de respaldo',
      auditEvidence: 'Evidencia de auditoría',
      timeline: 'Línea de tiempo',
      allowedOperations: 'Operaciones permitidas',
      activated: 'Activado',
      ready: 'Listo',
    },
    apiSecurity: {
      title: 'Centro de Control de Seguridad API',
      subtitle:
        'Capa interna de seguridad API para acciones financieras sensibles, autorización por resolver, límites por acción de negocio, exposición de esquema, autenticación reforzada y auditoría.',
      commandBannerTitle: 'La API es la verdadera frontera de seguridad',
      commandBannerText:
        'Los controles de interfaz no son suficientes. Las operaciones sensibles deben validarse, autorizarse, limitarse, auditarse y puntuarse por riesgo en el backend.',
      securityBoundary: 'Frontera de seguridad',
      securityControls: 'Controles de seguridad',
      securityEvents: 'Eventos de seguridad',
      sensitiveOperations: 'Operaciones sensibles',
      blockedOrStepUpDecisions: 'Decisiones bloqueadas o con refuerzo',
      backendControlLayer: 'Capa de control backend',
      auditReadySignals: 'Señales listas para auditoría',
      businessActionBoundary: 'Límite de acción de negocio',
      customerProtectionDecisions: 'Decisiones de protección del cliente',
      eventQueue: 'Cola de eventos',
      apiSecurityEvents: 'Eventos de seguridad API',
      apiSurface: 'Superficie API',
      operationName: 'Nombre de operación',
      businessAction: 'Acción de negocio',
      affectedObject: 'Objeto afectado',
      auditEvent: 'Evento de auditoría',
      controlCatalog: 'Catálogo de controles',
      category: 'Categoría',
      enabled: 'Habilitado',
      disabled: 'Deshabilitado',
      protectedOperations: 'Operaciones protegidas',
      decisionModel: 'Modelo de decisión',
      evidenceOutputs: 'Salidas de evidencia',
      requiredControls: 'Controles requeridos',
      auditRequired: 'Auditoría requerida',
      stepUpRequired: 'Refuerzo requerido',
      batchingAllowed: 'Lotes permitidos',
      apiSurfaces: 'Superficies API',
      controlsApplied: 'Controles aplicados',
      securityScenarios: 'Escenarios de seguridad',
      expectedDecision: 'Decisión esperada',
      riskIndicators: 'Indicadores de riesgo',
      recommendedControls: 'Controles recomendados',
      scenarioDemo: 'Demo de escenario',
      evaluateApiScenario: 'Evaluar escenario API',
      attempts: 'Intentos',
      objectAuthorized: 'Objeto autorizado',
      batchingDetected: 'Lotes detectados',
      sensitiveFieldsRequested: 'Campos sensibles solicitados',
      riskScore: 'Puntaje de riesgo',
      auditEventRequired: 'Evento de auditoría requerido',
      goldenRules: 'Reglas clave',
      goldenRuleItems: [
        'La interfaz nunca decide la seguridad.',
        'Autenticado no significa autorizado.',
        'Una operación sensible equivale a una decisión de autorización y un evento de auditoría.',
        'Limitar la acción de negocio, no solo la solicitud HTTP.',
        'Los campos sensibles no pertenecen casualmente a contratos API públicos.',
        'Las operaciones de alto riesgo requieren verificación reforzada.',
      ],
      prototypeDisclaimer:
        'Aurora Digital Assets es un prototipo conceptual. Los controles API, eventos, escenarios, puntajes de riesgo y registros de auditoría son datos demo ficticios y determinísticos.',
    },
    cryptoAgility: {
      title: 'Centro de Control de Agilidad Criptográfica',
      subtitle:
        'Inventario, versionado de algoritmos, ciclo de vida de claves, riesgo de confidencialidad a largo plazo y preparación para migración post-cuántica.',
      bannerTitle: 'Diseñado para migración, no para promesas falsas',
      designedForMigration: 'Diseñado para migración, no para promesas falsas',
      bannerText:
        'Aurora no afirma ser quantum-proof. Este módulo modela agilidad criptográfica: saber dónde se usa criptografía, versionar algoritmos, rotar claves, separar la criptografía de la plataforma de la criptografía de los protocolos blockchain y prepararse para una futura migración basada en estándares.',
      cryptoAssets: 'Activos criptográficos',
      algorithmPolicies: 'Políticas de algoritmos',
      rotationGaps: 'Brechas de rotación',
      longTermRiskAssets: 'Activos con riesgo a largo plazo',
      pqReadinessGaps: 'Brechas de preparación post-cuántica',
      assetInventory: 'Inventario de activos criptográficos',
      algorithmVersioning: 'Versionado de algoritmos',
      keyLifecycle: 'Ciclo de vida de claves',
      longTermConfidentialityRisk:
        'Riesgo de confidencialidad a largo plazo',
      harvestRisk: 'Riesgo harvest now, decrypt later',
      postQuantumReadiness: 'Preparación post-cuántica',
      platformVsBlockchain:
        'Criptografía de plataforma vs protocolo blockchain',
      noCustomCryptography: 'Sin criptografía personalizada',
      noQuantumProofClaims: 'Sin afirmaciones quantum-proof',
      evaluateCryptoScenario: 'Evaluar escenario de agilidad criptográfica',
      scenarioEvaluation: 'Evaluación de escenario',
      scenario: 'Escenario',
      scenarioResult: 'Resultado de escenario',
      algorithmFamily: 'Familia de algoritmo',
      version: 'Versión',
      keyLocation: 'Ubicación de clave',
      rotationPeriod: 'Periodo de rotación',
      longTermConfidentiality: 'Confidencialidad a largo plazo',
      blockchainDependency: 'Dependencia de protocolo blockchain',
      approvedCurrent: 'Actual aprobado',
      deprecated: 'Deprecado',
      migrationCandidates: 'Candidatos de migración',
      cryptoOwner: 'Responsable criptográfico',
      storageBoundary: 'Límite de almacenamiento',
      rotationRequired: 'Rotación requerida',
      emergencyRolloverReady: 'Rollover de emergencia listo',
      auditRequired: 'Auditoría requerida',
      riskScore: 'Puntaje de riesgo',
      severity: 'Severidad',
      decision: 'Decisión',
      auditEventId: 'ID de evento de auditoría',
      correlationId: 'ID de correlación',
      evidencePackageReady: 'Paquete de evidencia listo',
      affectedDomains: 'Dominios afectados',
      cryptoAgilityRisk: 'Riesgo de agilidad criptográfica',
      triggeredControls: 'Controles activados',
      recommendedAction: 'Acción recomendada',
      explanation: 'Explicación',
      boundaryTitle: 'Límite criptográfico',
      boundaryCopy:
        'La criptografía de la plataforma Aurora se gobierna por separado de la criptografía de protocolos blockchain externos.',
      auroraControls: [
        'TLS',
        'tokens',
        'claves API',
        'firmas internas',
        'cifrado de base de datos',
        'respaldos',
        'integridad de auditoría',
        'comunicación entre microservicios',
        'certificados cloud',
        'límites de arquitectura de custodia',
      ],
      auroraDoesNotControl: [
        'criptografía de consenso de Bitcoin',
        'criptografía del protocolo Ethereum',
        'migración blockchain externa',
        'internos de custodia de terceros',
      ],
      goldenRules: 'Reglas clave',
      goldenRuleItems: [
        'Sin criptografía personalizada.',
        'Sin afirmaciones quantum-proof.',
        'Inventariar cada dependencia criptográfica.',
        'Versionar algoritmos y políticas de claves.',
        'Rotar claves con evidencia de auditoría.',
        'Clasificar riesgos de confidencialidad a largo plazo.',
        'Separar criptografía de plataforma de protocolos blockchain.',
        'Usar KMS/HSM/Key Vault para gobierno de claves en producción.',
        'Preparar planes de migración basados en estándares.',
        'Preservar evidencia para cada decisión del ciclo de vida de claves.',
      ],
      flags: {
        deprecated_algorithm_detected: 'Algoritmo deprecado detectado',
        long_lived_key_detected: 'Clave de larga duración detectada',
        missing_algorithm_versioning: 'Falta versionado de algoritmos',
        missing_key_rotation_policy: 'Falta política de rotación de claves',
        backup_long_term_risk: 'Riesgo de respaldo a largo plazo',
        audit_integrity_gap: 'Brecha de integridad de auditoría',
        custody_key_rotation_gap: 'Brecha de rotación de claves de custodia',
        blockchain_protocol_confusion: 'Confusión con protocolo blockchain',
        post_quantum_readiness_gap: 'Brecha de preparación post-cuántica',
        kms_hsm_integration_missing:
          'Falta integración KMS/HSM/Key Vault',
      },
      prototypeDisclaimer:
        'Aurora Digital Assets es un prototipo conceptual. No se accede ni se ejecuta ninguna operación criptográfica real, material de claves, clave de billetera, clave de custodia, KMS, HSM, Key Vault ni algoritmo post-cuántico.',
    },
    sensitiveApproval: {
      title: 'Motor de Aprobación de Operaciones Sensibles',
      subtitle:
        'Aprobación reforzada de estilo bancario para activos digitales y acciones internas sensibles.',
      bankStyleStrongApproval: 'Aprobación reforzada de estilo bancario',
      stepUpApproval: 'Aprobación reforzada',
      mobileApprovalSimulated: 'Aprobación móvil simulada',
      backendRiskDecision: 'Decisión de riesgo backend',
      approvalRequired: 'Aprobación requerida',
      operationCatalog: 'Catálogo de operaciones',
      sensitiveOperations: 'Operaciones sensibles',
      scenarioEvaluator: 'Evaluador de escenarios',
      customerConfirmed: 'Cliente confirmó',
      deviceTrusted: 'Dispositivo confiable',
      mobileApprovalStatus: 'Estado de aprobación móvil',
      highValueNewWalletWithdrawal:
        'Retiro de alto valor a billetera nueva',
      securityDeviceChange: 'Cambio de dispositivo de seguridad',
      reviewerCaseClosure: 'Cierre de caso por revisor',
      recommendedNextAction: 'Siguiente acción recomendada',
      temporaryWithdrawalFreeze: 'Congelamiento temporal de retiros',
      pendingReview: 'Revisión pendiente',
      blocked: 'Bloqueado',
      approved: 'Aprobado',
      evidencePackageReady: 'Paquete de evidencia listo',
      reviewCaseRequired: 'Caso de revisión requerido',
      operationType: 'Tipo de operación',
      actorType: 'Tipo de actor',
      amountEur: 'Importe EUR',
      asset: 'Activo',
      isNewDestination: 'Destino nuevo',
      riskLevel: 'Nivel de riesgo',
      riskScore: 'Puntaje de riesgo',
      reasons: 'Razones',
      evaluate: 'Evaluar aprobación sensible',
      finnishModel: 'Modelo bancario finlandés',
      conceptBannerTitle: 'Acceso no es ejecución',
      conceptRules: [
        'El inicio de sesión permite acceso.',
        'La aprobación reforzada permite intentar una operación.',
        'La evaluación de riesgo backend decide el resultado.',
      ],
      finnishModelCopy:
        'Aurora adapta un patrón familiar de aprobación bancaria finlandesa a operaciones de activos digitales. La aprobación móvil se simula en este prototipo y la aprobación por sí sola no significa ejecución automática. El backend todavía evalúa el riesgo.',
      statuses: {
        pending: 'Pendiente',
        approved: 'Aprobado',
        rejected: 'Rechazado',
        expired: 'Expirado',
      },
      prototypeDisclaimer:
        'Aurora Digital Assets es un prototipo conceptual. No se realiza aprobación móvil real, MFA, notificaciones, firma criptográfica, ejecución de pagos ni ejecución blockchain.',
    },
    infrastructureSecurity: {
      title: 'Centro de Control de Seguridad de Infraestructura',
      subtitle:
        'Postura de seguridad transversal para autorización de aplicación, RBAC de Kubernetes, IAM cloud, secretos, evidencia de auditoría y operaciones de riesgo.',
      commandBannerTitle:
        'Evitar que una vulnerabilidad se convierta en una reacción en cadena',
      commandBannerText:
        'Aurora modela cómo un problema de backend puede contenerse antes de alcanzar contenedores, permisos de Kubernetes, roles cloud, secretos o datos financieros sensibles.',
      cloudNativeBoundary: 'Contención cloud-native',
      securityLayers: 'Capas de seguridad',
      infrastructureControls: 'Controles de infraestructura',
      activeEvents: 'Eventos activos',
      criticalChainRisks: 'Riesgos críticos de cadena',
      crossLayerSecurityEvents: 'Eventos de seguridad transversal',
      eventQueue: 'Cola de eventos',
      affectedLayer: 'Capa afectada',
      affectedLayers: 'Capas afectadas',
      chainStage: 'Etapa de cadena',
      chainReactionRisk: 'Riesgo de reacción en cadena',
      affectedAsset: 'Activo afectado',
      evidencePackageReady: 'Paquete de evidencia listo',
      protectedAssets: 'Activos protegidos',
      monitoredSignals: 'Señales monitoreadas',
      possibleChain: 'Cadena posible',
      evaluateInfrastructureScenario:
        'Evaluar escenario de infraestructura',
      objectAuthorizationFailed: 'Autorización de objeto fallida',
      unsafeTemplateInputDetected: 'Entrada de plantilla insegura detectada',
      podPrivileged: 'Pod privilegiado',
      serviceAccountCanReadSecrets:
        'Cuenta de servicio puede leer secretos',
      cloudIamWildcardPermissions: 'Permisos wildcard en IAM cloud',
      weakTrustPolicy: 'Política de confianza débil',
      secretExposureDetected: 'Exposición de secreto detectada',
      azureStorageToIdentityChainReaction:
        'Reacción en cadena de almacenamiento Azure a identidad',
      publicStorageExposureDetected:
        'Exposición de almacenamiento público detectada',
      certificateExposureDetected: 'Exposición de certificado detectada',
      servicePrincipalOverprivileged:
        'Service principal con privilegios excesivos',
      deploymentCredentialsEnabled:
        'Credenciales de despliegue habilitadas',
      managedIdentityExcessiveScope:
        'Managed identity con alcance excesivo',
      passwordResetPrivilegeDetected:
        'Privilegio de reset de contraseña detectado',
      identityMonitoringGap: 'Brecha de monitoreo de identidad',
      containerKubernetesHardeningFailure:
        'Fallo de hardening de contenedores y Kubernetes',
      dockerfileSecretsDetected: 'Secretos detectados en Dockerfile',
      imageUsesLatestTag: 'Imagen usa etiqueta latest',
      containerRunsAsRoot: 'Contenedor ejecuta como root',
      plaintextSecretsInManifest: 'Secretos en texto plano en manifest',
      missingSecurityContext: 'Falta securityContext de Kubernetes',
      serviceAccountTokenMounted: 'Token de ServiceAccount montado',
      rbacWildcardPermissions: 'Permisos RBAC wildcard',
      canReadKubernetesSecrets: 'Puede leer secretos de Kubernetes',
      networkPolicyMissing: 'Falta NetworkPolicy',
      resourceLimitsMissing: 'Faltan límites de recursos',
      cisAuditMissing: 'Falta auditoría CIS',
      hardeningVerificationMissing: 'Falta verificación de hardening',
      containerKubernetesHardening: 'Hardening de contenedores y Kubernetes',
      containerKubernetesHardeningEvidencePackage:
        'Paquete de evidencia de hardening de contenedores y Kubernetes',
      containerKubernetesHardeningReviewCase:
        'Caso de revisión de hardening de contenedores y Kubernetes',
      runtimeHardeningFailure: 'Fallo de hardening de runtime',
      devSecOpsVerificationEvidence: 'Evidencia de verificación DevSecOps',
      azureStorageToIdentityRisk: 'Riesgo de Azure Storage a identidad',
      azureStorageToIdentityRiskEvidencePackage:
        'Paquete de evidencia de riesgo de Azure Storage a identidad',
      azureStorageToIdentityRiskReviewCase:
        'Caso de revisión de riesgo de Azure Storage a identidad',
      cloudIdentitySecurity: 'Seguridad de identidad cloud',
      storageToIdentityChainContainment:
        'Contención de cadena de almacenamiento a identidad',
      applicationSecurity: 'Seguridad de Aplicación',
      kubernetesSecurity: 'Seguridad de Kubernetes',
      cloudIamSecurity: 'Seguridad IAM Cloud',
      secretsSecurity: 'Seguridad de Secretos',
      auditEvidence: 'Evidencia de Auditoría',
      riskOperations: 'Operaciones de Riesgo',
      goldenRuleItems: [
        'No confiar en IDs controlados por el cliente.',
        'Aplicar autorización a nivel de objeto.',
        'Los usuarios pueden aportar datos, no plantillas ejecutables.',
        'Las cargas web no deben leer secretos por defecto.',
        'El RBAC de Kubernetes debe seguir privilegio mínimo.',
        'La confianza IAM cloud debe vincularse a cargas específicas.',
        'Los permisos IAM deben evitar wildcards.',
        'Los secretos deben estar acotados, rotados y nunca registrarse en logs.',
        'Los logs deben conectar aplicación, Kubernetes, IAM, secretos y acceso a datos.',
        'Una capa débil no debe convertirse en compromiso total.',
      ],
      prototypeDisclaimer:
        'Aurora Digital Assets es un prototipo conceptual. Los controles, eventos, escenarios, puntajes de riesgo y registros de auditoría de infraestructura son datos demo ficticios y determinísticos.',
    },
    riskOperations: {
      title: 'Consola de Operaciones de Riesgo',
      subtitle:
        'Vista interna unificada para alertas de delitos financieros, razonamiento de cumplimiento, preparación de evidencia, incidentes operacionales y prioridades de acción del equipo.',
      operatingMode: 'Modo operativo',
      highestPriority: 'Prioridad máxima',
      commandSummary: 'Resumen de comando',
      noOverview: 'Resumen no cargado',
      staffPriorities: 'Prioridades del equipo',
      actionQueue: 'Cola de acciones',
      crossModuleEvents: 'Eventos entre módulos',
      unifiedTimeline: 'Línea de tiempo unificada',
      escalations: 'Escalaciones',
      escalationSummary: 'Resumen de escalaciones',
      recommendedFocus: 'Foco recomendado',
      operationalBoundary: 'Límite operacional',
      operationalBoundaryCopy:
        'Esta consola no procesa datos bancarios reales. Orquesta salidas ficticias del prototipo desde monitoreo, inteligencia de cumplimiento, preparación de evidencia y módulos de resiliencia.',
      sourceModule: 'Módulo fuente',
      sourceId: 'ID de fuente',
      requiredAction: 'Acción requerida',
      relatedLinks: 'Enlaces relacionados',
      relatedEntity: 'Entidad relacionada',
      openItems: 'Ítems abiertos',
      blockedItems: 'Ítems bloqueados',
      readyItems: 'Ítems listos',
      noMissingEvidence: 'No hay evidencia faltante registrada.',
      prepareReviewCase: 'Preparar caso de revisión',
      reviewCasePrepared: 'Caso de revisión preparado',
      reviewCaseId: 'ID de caso de revisión',
      auditEventCreated: 'Evento de auditoría creado',
      recommendedNextAction: 'Siguiente acción recomendada',
    },
    reviewCaseLifecycle: {
      title: 'Ciclo de Vida de Casos y Motor de Decisión',
      caseLifecycle: 'Ciclo de vida del caso',
      currentStatus: 'Estado actual',
      previousStatus: 'Estado anterior',
      allowedNextStatuses: 'Próximos estados permitidos',
      startReview: 'Iniciar revisión',
      markActionRequired: 'Marcar acción requerida',
      startMitigation: 'Iniciar mitigación',
      markMitigated: 'Marcar mitigado',
      closeCase: 'Cerrar caso',
      decisionNote: 'Nota de decisión',
      mitigationAction: 'Acción de mitigación',
      lifecycleProgress: 'Progreso del ciclo de vida',
      reviewerAction: 'Acción del revisor',
      evidenceReviewed: 'Evidencia revisada',
      mitigationRequested: 'Mitigación solicitada',
      mitigationStarted: 'Mitigación iniciada',
      mitigationVerified: 'Mitigación verificada',
      caseClosed: 'Caso cerrado',
      finalDecision: 'Decisión final',
      closureReady: 'Listo para cierre',
      recommendedNextStatus: 'Próximo estado recomendado',
      continueLifecycleInComplianceReview:
        'Continuar ciclo de vida en Revisión de Cumplimiento',
    },
    prototypeBoundary: {
      independentConceptPrototype: 'Prototipo conceptual independiente',
      noRealCustomerData: 'Sin datos reales de clientes',
      noRealBankingSystemsConnected: 'Sin conexión a sistemas bancarios reales',
      noRealLegalReport: 'No se genera un reporte legal real',
      fictionalDemoData: 'Solo datos demo ficticios y determinísticos',
      prototypeBoundary: 'Límite del prototipo',
    },
  },
} as const
