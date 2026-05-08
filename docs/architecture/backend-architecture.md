# Backend Architecture

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)  
**Status:** v0.2 backend architecture planning document  
**Version:** 0.1  
**Date:** 2026-05-08  

---

## 1. Purpose

This document defines the proposed backend architecture for Aurora Digital Assets.

Aurora Digital Assets is a bank-integrated digital assets concept. The frontend prototype already demonstrates banking navigation, accounts, payments, cards, custody, withdrawals, reports, and compliance review views.

The next architectural step is to define how a backend could support these flows with clear service boundaries, auditability, risk evaluation, review cases, and future persistence.

The backend should be designed as a simulated banking-grade API, not as a crypto exchange backend.

Primary goals:

- support realistic banking and digital asset workflows;
- keep all prototype data simulated;
- provide a future path from frontend mock data to API-backed data;
- centralize audit events;
- support the Risk & Review Engine;
- support compliance review cases;
- support reports and evidence packages;
- remain deterministic, explainable, and backend-ready.

---

## 2. Backend Design Principles

### 2.1 Banking-First Backend

The backend should model banking concepts first:

- customers;
- accounts;
- balances;
- payments;
- recipients;
- statements;
- documents;
- notifications;
- audit events.

Digital asset functionality should extend these banking concepts rather than replace them.

### 2.2 Deterministic Business Logic

The backend should use deterministic rules for early versions.

This means:

- no black-box AI decisions;
- no hidden scoring;
- clear rule evaluation;
- explicit decision reasons;
- auditable outcomes.

### 2.3 Separation of Concerns

Each backend service should have a clear responsibility:

- accounts;
- payments;
- digital assets;
- custody;
- withdrawals;
- risk review;
- compliance cases;
- audit events;
- reports.

### 2.4 Audit Everything Sensitive

Every sensitive action should create an audit event.

Examples:

- login context received;
- payment draft created;
- digital asset payment evaluated;
- withdrawal evaluated;
- risk decision generated;
- review case created;
- reviewer decision recorded;
- report generated.

### 2.5 Human Review Support

The backend should support human review workflows for sensitive or ambiguous actions.

The system should be able to:

- create review cases;
- attach evidence;
- store reviewer decisions;
- update customer-facing status;
- preserve audit history.

### 2.6 Mock First, Real Later

For the prototype, the backend should use simulated data and local persistence.

Future production-level integrations may include:

- real core banking systems;
- real custody providers;
- real AML/wallet screening vendors;
- real tax reporting systems;
- real notification services.

These are outside prototype scope.

---

## 3. Suggested Technology Stack

Recommended prototype stack:

```text
Python
FastAPI
Pydantic
SQLite
SQLAlchemy or SQLModel
Uvicorn
pytest
```

Optional later additions:

```text
PostgreSQL
Alembic migrations
Redis
Celery / background jobs
OpenAPI client generation
PDF generation
Structured logging
```

The prototype should start simple:

```text
FastAPI + Pydantic + SQLite
```

---

## 4. Proposed Backend Folder Structure

Suggested structure:

```text
backend/
  README.md
  requirements.txt
  app/
    main.py

    api/
      __init__.py
      routes/
        __init__.py
        accounts.py
        payments.py
        digital_assets.py
        withdrawals.py
        custody.py
        reports.py
        compliance.py
        review_cases.py
        audit_events.py

    core/
      __init__.py
      config.py
      security.py
      constants.py

    db/
      __init__.py
      database.py
      seed.py

    models/
      __init__.py
      account.py
      payment.py
      digital_asset.py
      withdrawal.py
      custody.py
      review_case.py
      audit_event.py
      report.py
      notification.py

    schemas/
      __init__.py
      account.py
      payment.py
      digital_asset.py
      withdrawal.py
      custody.py
      risk_review.py
      review_case.py
      audit_event.py
      report.py

    services/
      __init__.py
      account_service.py
      payment_service.py
      digital_asset_service.py
      withdrawal_service.py
      custody_service.py
      risk_review_engine.py
      compliance_service.py
      review_case_service.py
      audit_service.py
      reporting_service.py
      notification_service.py

    rules/
      __init__.py
      asset_rules.py
      payment_rules.py
      withdrawal_rules.py
      security_rules.py
      risk_thresholds.py

    tests/
      __init__.py
      test_risk_review_engine.py
      test_withdrawals.py
      test_digital_asset_payments.py
```

---

## 5. Backend Layers

The backend can be organized into five logical layers.

### 5.1 API Layer

Responsible for HTTP endpoints.

Examples:

```text
GET /api/accounts
POST /api/payments
POST /api/payments/digital-assets/evaluate
GET /api/digital-assets/wallet
POST /api/withdrawals/evaluate
POST /api/withdrawals
GET /api/review-cases
POST /api/review-cases/{case_id}/decision
GET /api/reports
GET /api/audit-events
```

The API layer should be thin. It should validate request payloads and call service functions.

### 5.2 Schema Layer

Responsible for Pydantic request and response models.

Examples:

```text
PaymentCreateRequest
DigitalAssetPaymentEvaluateRequest
WithdrawalEvaluateRequest
RiskDecisionResponse
ReviewCaseResponse
AuditEventResponse
```

### 5.3 Service Layer

Responsible for business workflows.

Examples:

- create payment;
- evaluate digital asset payment;
- evaluate withdrawal;
- create review case;
- record audit event;
- generate report summary.

### 5.4 Rule Layer

Responsible for deterministic rules.

Examples:

- withdrawal rules;
- digital asset payment rules;
- asset eligibility rules;
- security rules;
- risk thresholds.

### 5.5 Persistence Layer

Responsible for storing prototype data.

For v0.2/v0.3:

```text
SQLite
```

Future:

```text
PostgreSQL
```

---

## 6. Core Services

### 6.1 Account Service

Responsibilities:

- list bank accounts;
- get account details;
- show balances;
- list transactions;
- connect bank account funding to buy/sell flows;
- connect account activity to payments and reports.

Example functions:

```text
list_accounts(customer_id)
get_account(account_id)
list_account_transactions(account_id)
```

### 6.2 Payment Service

Responsibilities:

- create standard invoice payment drafts;
- validate reference numbers;
- validate payment amount;
- check recipient data;
- submit standard EUR bank payment concept;
- connect to digital asset payment evaluation.

Example functions:

```text
create_payment_draft(payload)
validate_invoice_payment(payload)
submit_payment(payload)
```

### 6.3 Digital Asset Payment Service

Responsibilities:

- check whether recipient is eligible for digital asset payments;
- evaluate selected payment asset;
- calculate simulated conversion;
- preserve invoice reference;
- create payment record;
- trigger audit events;
- optionally call Risk & Review Engine.

Example functions:

```text
evaluate_digital_asset_payment(payload)
submit_digital_asset_payment(payload)
```

### 6.4 Digital Asset Service

Responsibilities:

- list supported assets;
- list wallet balances;
- show digital asset activity;
- calculate buy/sell estimates;
- create simulated buy/sell records;
- connect to market prices.

Example functions:

```text
list_supported_assets()
get_wallet_balances(customer_id)
estimate_buy_sell(payload)
submit_buy_sell(payload)
```

### 6.5 Custody Service

Responsibilities:

- return custody mode;
- show custody transparency data;
- define whether external withdrawal is enabled;
- define whether user controls private keys;
- define custody partner concept;
- expose custody disclosures.

Example functions:

```text
get_custody_status(customer_id)
get_asset_custody_details(asset)
```

### 6.6 Withdrawal Service

Responsibilities:

- validate asset, network, amount and destination;
- call Risk & Review Engine;
- create withdrawal request;
- create review case if required;
- update withdrawal status;
- record audit events.

Example functions:

```text
evaluate_withdrawal(payload)
submit_withdrawal(payload)
get_withdrawal_status(withdrawal_id)
```

### 6.7 Risk Review Engine

Responsibilities:

- evaluate sensitive actions;
- apply deterministic rules;
- calculate risk level;
- return decision object;
- create case recommendation;
- provide customer-facing message;
- provide internal reasons.

Example functions:

```text
evaluate_action(context)
evaluate_withdrawal(context)
evaluate_digital_asset_payment(context)
evaluate_buy_sell(context)
```

### 6.8 Compliance Service

Responsibilities:

- apply monitoring rules;
- manage risk events;
- connect to review cases;
- simulate AML and sanctions logic;
- store compliance flags.

Example functions:

```text
create_risk_event(payload)
list_risk_events()
get_compliance_summary(customer_id)
```

### 6.9 Review Case Service

Responsibilities:

- create review case;
- list review cases;
- get case details;
- record reviewer decision;
- close or escalate case;
- attach audit events.

Example functions:

```text
create_case(payload)
list_cases()
get_case(case_id)
record_decision(case_id, decision)
```

### 6.10 Audit Service

Responsibilities:

- create audit events;
- list audit events;
- filter audit events by customer, case, action type or module;
- support evidence timelines;
- support reports.

Example functions:

```text
record_event(event)
list_events(filters)
get_case_timeline(case_id)
```

### 6.11 Reporting Service

Responsibilities:

- generate account document summaries;
- generate digital asset annual summary;
- generate tax summary concept;
- generate audit evidence package concept;
- support PDF/CSV export later.

Example functions:

```text
get_reports(customer_id)
generate_tax_summary(customer_id, year)
generate_evidence_package(case_id)
```

### 6.12 Notification Service

Responsibilities:

- create customer-facing notifications;
- send simulated status updates;
- notify review decisions;
- notify report availability.

Example functions:

```text
create_notification(customer_id, message)
list_notifications(customer_id)
```

---

## 7. Core Data Models

### 7.1 Customer

```text
customer_id
display_name
customer_type
risk_profile
digital_assets_enabled
external_withdrawals_enabled
status
created_at
```

### 7.2 Account

```text
account_id
customer_id
name
type
iban
bic
book_balance
available_balance
currency
status
created_at
```

### 7.3 Bank Transaction

```text
transaction_id
account_id
title
detail
amount
currency
status
reference_number
created_at
```

### 7.4 Digital Asset

```text
asset_id
symbol
name
asset_type
payment_enabled
withdrawal_enabled
buy_sell_enabled
status
```

### 7.5 Wallet Balance

```text
wallet_balance_id
customer_id
asset_symbol
balance
estimated_value_eur
custody_mode
status
updated_at
```

### 7.6 Digital Asset Transaction

```text
digital_asset_transaction_id
customer_id
action_type
asset_symbol
amount
estimated_value_eur
fee_eur
status
created_at
```

### 7.7 Payment Recipient

```text
recipient_id
name
recipient_type
has_bank_account
iban
bic
accepts_digital_asset_payments
accepted_assets
settlement_preference
status
```

### 7.8 Invoice Payment

```text
payment_id
customer_id
recipient_id
source_account_id
invoice_number
reference_number
due_date
amount_eur
payment_method
status
created_at
```

### 7.9 Digital Asset Payment

```text
digital_asset_payment_id
payment_id
asset_symbol
estimated_asset_amount
conversion_rate
service_fee_eur
settlement_fee_eur
recipient_settlement
risk_decision
status
created_at
```

### 7.10 External Withdrawal

```text
withdrawal_id
customer_id
asset_symbol
network
amount
destination_address
destination_label
wallet_type
risk_level
decision
status
case_id
created_at
updated_at
```

### 7.11 Review Case

```text
case_id
customer_id
case_type
related_action_id
risk_level
status
reasons
assigned_to
reviewer_decision
reviewer_notes
created_at
updated_at
closed_at
```

### 7.12 Audit Event

```text
event_id
timestamp
customer_id
session_id
module
action_type
entity_type
entity_id
asset_symbol
amount
currency
status
risk_level
decision
reasons
case_id
user_message
internal_notes
```

### 7.13 Report

```text
report_id
customer_id
report_type
year
status
generated_at
file_type
description
```

### 7.14 Notification

```text
notification_id
customer_id
title
message
severity
status
created_at
read_at
```

---

## 8. Main API Endpoints

### 8.1 Accounts

```text
GET /api/accounts
GET /api/accounts/{account_id}
GET /api/accounts/{account_id}/transactions
```

### 8.2 Payments

```text
GET /api/payments
POST /api/payments
POST /api/payments/evaluate
POST /api/payments/digital-assets/evaluate
POST /api/payments/digital-assets
```

### 8.3 Digital Assets

```text
GET /api/digital-assets/assets
GET /api/digital-assets/wallet
GET /api/digital-assets/activity
POST /api/digital-assets/buy-sell/evaluate
POST /api/digital-assets/buy-sell
```

### 8.4 Custody

```text
GET /api/custody/status
GET /api/custody/assets/{asset_symbol}
```

### 8.5 Withdrawals

```text
GET /api/withdrawals
POST /api/withdrawals/evaluate
POST /api/withdrawals
GET /api/withdrawals/{withdrawal_id}
```

### 8.6 Review Cases

```text
GET /api/review-cases
GET /api/review-cases/{case_id}
POST /api/review-cases/{case_id}/decision
```

### 8.7 Audit Events

```text
GET /api/audit-events
GET /api/audit-events?customer_id=...
GET /api/audit-events?case_id=...
GET /api/audit-events?module=...
```

### 8.8 Reports

```text
GET /api/reports
GET /api/reports/tax-summary/{year}
POST /api/reports/evidence-package
```

### 8.9 Notifications

```text
GET /api/notifications
POST /api/notifications/{notification_id}/read
```

---

## 9. Example Backend Flow: Digital Asset Payment

```text
Frontend PaymentsPage
        |
POST /api/payments/digital-assets/evaluate
        |
Payment Service
        |
Recipient eligibility check
        |
Risk & Review Engine
        |
Decision object
        |
Audit Service records evaluation
        |
Frontend shows result
```

If submitted:

```text
Frontend Submit Payment
        |
POST /api/payments/digital-assets
        |
Payment Service creates payment record
        |
Digital Asset Payment Service creates digital asset payment record
        |
Audit Service records submission
        |
Reporting Service updates activity
        |
Notification Service creates customer notification
```

---

## 10. Example Backend Flow: External Withdrawal

```text
Frontend WithdrawalsPage
        |
POST /api/withdrawals/evaluate
        |
Withdrawal Service validates request
        |
Risk & Review Engine evaluates request
        |
Decision object returned
        |
Audit event created
```

Decision branches:

```text
auto_approved
        |
withdrawal request accepted
        |
audit event created

pending_review
        |
review case created
        |
customer status = Pending security review
        |
audit event created

auto_rejected
        |
customer receives validation message
        |
audit event created

blocked
        |
customer receives blocked message
        |
risk event created
        |
audit event created
```

---

## 11. Risk & Review Engine Integration

The backend should treat the Risk & Review Engine as a central internal service.

Inputs:

- action type;
- customer profile;
- asset;
- amount;
- network;
- destination;
- recipient;
- session/security context;
- historical activity;
- policy limits.

Output:

```json
{
  "decision": "pending_review",
  "risk_level": "medium",
  "reasons": ["first_time_external_address"],
  "case_required": true,
  "case_type": "external_withdrawal_review",
  "user_message": "Your external transfer request is pending security review.",
  "audit_event_type": "withdrawal_pending_review"
}
```

The result should be stored through the Audit Service.

If `case_required` is true, the Review Case Service should create a case.

---

## 12. Audit Event Strategy

The backend should record audit events for all sensitive workflows.

### 12.1 Event Categories

```text
account_event
payment_event
digital_asset_event
custody_event
withdrawal_event
risk_event
review_case_event
report_event
security_event
```

### 12.2 Event Timing

Audit events should be created when:

- form is submitted;
- evaluation starts;
- validation fails;
- risk score is calculated;
- decision is returned;
- case is created;
- reviewer acts;
- report is generated;
- notification is sent.

### 12.3 Immutability Concept

For the prototype, events may be stored normally.

For a production concept, audit events should be append-only.

The system should not overwrite historical evidence.

---

## 13. Review Case Lifecycle

Suggested lifecycle:

```text
Open
Pending review
More information needed
Approved
Rejected
Escalated
Closed
```

Flow:

```text
Risk decision requires case
        |
Review case created
        |
Case appears in Compliance Review dashboard
        |
Reviewer inspects evidence
        |
Reviewer records decision
        |
Customer-facing status is updated
        |
Audit event is created
        |
Case is closed or escalated
```

---

## 14. Reporting Backend

The Reporting Service should aggregate records from:

- bank transactions;
- invoice payments;
- digital asset payments;
- buy/sell activity;
- wallet activity;
- external withdrawals;
- review cases;
- audit events.

Report types:

```text
account_statement
payment_receipt
digital_asset_annual_summary
wallet_activity_report
digital_asset_payment_report
external_withdrawal_review_report
tax_summary_concept
audit_evidence_package
```

Prototype exports:

```text
PDF concept
CSV concept
Evidence package concept
```

---

## 15. Security Model

Prototype security is simulated.

Future security model should include:

- strong customer authentication;
- session validation;
- role-based internal access;
- admin/reviewer roles;
- customer vs internal route separation;
- audit of reviewer actions;
- secure handling of sensitive identifiers;
- no storage of private keys in application database.

Important:

The backend should never expose:

- private keys;
- seed phrases;
- real bank credentials;
- real customer secrets.

---

## 16. Roles and Access Control

Suggested roles:

### Customer

Can access:

- own accounts;
- own payments;
- own digital assets;
- own withdrawals;
- own reports.

### Business Recipient

Future role.

Can access:

- business payment receipts;
- settlement preferences;
- accepted digital asset settings;
- business reports.

### Reviewer

Internal role.

Can access:

- review cases;
- audit evidence;
- risk decisions;
- reviewer actions.

### Admin

Internal role.

Can configure:

- supported assets;
- limits;
- product rules;
- simulated settings.

For the prototype, roles may be mocked.

---

## 17. Backend Configuration

Suggested configuration values:

```text
APP_ENV=development
DATABASE_URL=sqlite:///./aurora.db
SUPPORTED_ASSETS=BTC,ETH,USDC,USDT,EURD
DEFAULT_CUSTOMER_ID=demo-customer
MAX_AUTO_APPROVE_WITHDRAWAL_EUR=250
MAX_AUTO_APPROVE_PAYMENT_EUR=500
FIRST_WITHDRAWAL_REQUIRES_REVIEW=true
NEW_ADDRESS_REQUIRES_REVIEW=true
```

These values should live in:

```text
backend/app/core/config.py
```

---

## 18. Testing Strategy

Initial tests should focus on the Risk & Review Engine.

### 18.1 Withdrawal Tests

Test cases:

- invalid amount returns auto_rejected;
- EURD external withdrawal returns auto_rejected;
- invalid address returns auto_rejected;
- new BTC address returns pending_review;
- whitelisted address with low amount returns auto_approved;
- high-risk wallet signal returns blocked.

### 18.2 Digital Asset Payment Tests

Test cases:

- recipient not inside bank returns auto_rejected;
- recipient not enabled for digital asset payments returns auto_rejected;
- eligible recipient with low amount returns auto_approved;
- high-value digital asset payment returns pending_review;
- missing reference number returns auto_rejected.

### 18.3 Audit Tests

Test cases:

- evaluation creates audit event;
- pending review creates case event;
- reviewer decision creates audit event;
- report generation creates audit event.

---

## 19. Prototype Build Plan

### Phase 1: Backend Skeleton

- create FastAPI app;
- create routes;
- create Pydantic schemas;
- return static mock data.

### Phase 2: Risk Engine

- implement deterministic Risk & Review Engine;
- implement withdrawal evaluation;
- implement digital asset payment evaluation;
- add unit tests.

### Phase 3: Persistence

- add SQLite;
- create tables;
- seed demo data;
- store audit events;
- store review cases.

### Phase 4: Frontend Integration

- connect WithdrawalsPage to backend evaluate endpoint;
- connect PaymentsPage to backend evaluate endpoint;
- connect ComplianceReviewPage to review cases endpoint;
- connect ReportsPage to report endpoint.

### Phase 5: Reporting

- generate simulated PDF/CSV;
- generate evidence package concept;
- connect reports to audit events.

---

## 20. Open Questions

Important questions:

- Should the backend use SQLAlchemy or SQLModel?
- Should the prototype use SQLite only or prepare PostgreSQL compatibility?
- Should audit events be append-only from the beginning?
- Should risk rules be Python functions or JSON-configurable policies?
- Should review cases be created immediately during evaluation or only on submit?
- Should PaymentsPage call evaluate before submit?
- How should frontend state synchronize with backend status?
- Should reports be generated dynamically or from stored events?
- How should a future custody provider integration be abstracted?
- Which endpoints should be customer-facing and which internal?
- Should internal routes require a separate reviewer role in the prototype?
- How should simulated authentication context be passed to the backend?

---

## 21. Conclusion

The backend architecture for Aurora Digital Assets should make the prototype more than a visual banking UI.

It should provide the foundation for:

- realistic banking data;
- digital asset balances;
- controlled digital asset payments;
- external withdrawal review;
- deterministic risk decisions;
- human review cases;
- audit evidence;
- reports and export concepts.

The key backend principle is:

> Low-risk activity can be automated, but sensitive digital asset actions must be evaluated, explained, audited, and in some cases reviewed by a human operator.

This architecture directly supports the product strategy of building safer digital asset access inside a trusted banking environment.

---

## 22. Disclaimer

This document describes a backend architecture concept only.

Aurora Digital Assets is not a bank, not a custody provider, not a crypto exchange, not a payment institution, and not a regulated financial service.

The backend architecture described here is fictional and intended for product design, software architecture planning, compliance discussion, and portfolio demonstration.

No real bank systems, real customer data, private keys, payments, AML checks, custody operations, or blockchain transactions are used.