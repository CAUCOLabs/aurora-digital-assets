# Backend Implementation Plan

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)  
**Status:** v0.2 backend implementation planning document  
**Version:** 0.1  
**Date:** 2026-05-08  

---

## 1. Purpose

This document defines the implementation plan for the Aurora Digital Assets backend.

The goal is to move from a frontend-only prototype toward a backend-ready architecture without building a throwaway mock system.

The backend should be implemented as a **production-minded prototype**:

- simulated data today;
- real service boundaries from the beginning;
- deterministic risk logic;
- audit events;
- review cases;
- provider abstraction;
- clear upgrade path to real banking, custody, compliance, and reporting integrations later.

The main principle is:

> Prototype now, real system later, minimal rewrite.

---

## 2. Implementation Philosophy

Aurora Digital Assets should not be implemented as a simple demo backend with all logic inside one file.

The backend should be structured as if it could later connect to:

- a core banking system;
- a custody provider;
- a market price provider;
- a wallet risk screening provider;
- an AML / sanctions provider;
- a reporting and tax system;
- a notification service;
- a real authentication and authorization layer.

For the prototype, all these integrations remain mocked.

However, the backend should already have the right boundaries so that real providers can replace mock providers later.

---

## 3. Backend Goals

The first backend version should support:

- account data API;
- payment evaluation API;
- digital asset payment evaluation API;
- withdrawal evaluation API;
- risk decision engine;
- audit event creation;
- review case creation;
- compliance review dashboard data;
- reports data;
- provider abstraction;
- SQLite persistence or in-memory storage for early prototype.

The first backend version should not:

- connect to real bank APIs;
- execute real payments;
- execute real blockchain transfers;
- store private keys;
- perform real AML checks;
- perform real sanctions screening;
- provide financial, legal, or tax advice;
- use real customer data.

---

## 4. Recommended Stack

Initial stack:

```text
Python
FastAPI
Pydantic
SQLite
SQLAlchemy or SQLModel
Uvicorn
pytest
```

Recommended first implementation:

```text
FastAPI + Pydantic + in-memory storage
```

Then upgrade to:

```text
FastAPI + Pydantic + SQLite
```

Later possible upgrade:

```text
FastAPI + PostgreSQL + Alembic + background jobs
```

---

## 5. Target Backend Folder Structure

Create this structure:

```text
backend/
  README.md
  requirements.txt

  app/
    __init__.py
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
      constants.py
      security.py

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
      notification.py

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

    providers/
      __init__.py
      core_banking_provider.py
      custody_provider.py
      market_price_provider.py
      wallet_risk_provider.py
      aml_provider.py
      notification_provider.py

    rules/
      __init__.py
      asset_rules.py
      payment_rules.py
      withdrawal_rules.py
      security_rules.py
      risk_thresholds.py

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

    tests/
      __init__.py
      test_risk_review_engine.py
      test_withdrawals.py
      test_digital_asset_payments.py
```

The `providers/` layer is important because it allows real integrations later.

---

## 6. Provider Abstraction Strategy

The backend should use provider interfaces or provider classes from the beginning.

### 6.1 Core Banking Provider

Current prototype:

```text
MockCoreBankingProvider
```

Future real system:

```text
RealCoreBankingProvider
```

Responsibilities:

- get customer accounts;
- get balances;
- get account transactions;
- validate source account;
- create payment records;
- retrieve bank documents.

### 6.2 Custody Provider

Current prototype:

```text
MockCustodyProvider
```

Future real system:

```text
RealCustodyProvider
```

Responsibilities:

- get wallet balances;
- get custody status;
- check withdrawal availability;
- prepare withdrawal request;
- reconcile custody records.

Important:

The backend must not store private keys or seed phrases.

### 6.3 Market Price Provider

Current prototype:

```text
MockMarketPriceProvider
```

Future real system:

```text
RealMarketPriceProvider
```

Responsibilities:

- return BTC/EUR, ETH/EUR, USDC/EUR, USDT/EUR prices;
- provide timestamp;
- support estimate audit records.

### 6.4 Wallet Risk Provider

Current prototype:

```text
MockWalletRiskProvider
```

Future real system:

```text
RealWalletRiskProvider
```

Responsibilities:

- check external wallet address risk;
- return risk signal;
- identify high-risk destination concept;
- support withdrawal review.

### 6.5 AML Provider

Current prototype:

```text
MockAmlProvider
```

Future real system:

```text
RealAmlProvider
```

Responsibilities:

- simulate AML/sanctions checks;
- return risk flags;
- support compliance case creation.

### 6.6 Notification Provider

Current prototype:

```text
MockNotificationProvider
```

Future real system:

```text
RealNotificationProvider
```

Responsibilities:

- create in-app notifications;
- simulate email/SMS notifications;
- notify review status changes;
- notify report availability.

---

## 7. Implementation Phases

## Phase 0 — Repository Preparation

Goal:

Create backend folder and basic project files.

Tasks:

- create `backend/`;
- create `requirements.txt`;
- create `README.md`;
- create `app/main.py`;
- create folders for api, schemas, services, providers, rules, models, db, tests;
- add basic FastAPI health endpoint.

Endpoint:

```text
GET /api/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "aurora-digital-assets-backend",
  "version": "0.1"
}
```

Commit:

```text
Initialize backend skeleton
```

---

## Phase 1 — Core Schemas and Mock Providers

Goal:

Define backend contracts before implementing complex logic.

Create schemas for:

- accounts;
- payments;
- digital assets;
- withdrawals;
- risk decisions;
- review cases;
- audit events;
- reports.

Create mock providers:

- `MockCoreBankingProvider`;
- `MockCustodyProvider`;
- `MockMarketPriceProvider`;
- `MockWalletRiskProvider`;
- `MockAmlProvider`;
- `MockNotificationProvider`.

First routes:

```text
GET /api/accounts
GET /api/digital-assets/wallet
GET /api/reports
```

Commit:

```text
Add backend schemas and mock providers
```

---

## Phase 2 — Risk & Review Engine

Goal:

Implement the deterministic decision engine.

Create:

```text
backend/app/services/risk_review_engine.py
backend/app/rules/withdrawal_rules.py
backend/app/rules/payment_rules.py
backend/app/rules/security_rules.py
backend/app/rules/risk_thresholds.py
backend/app/schemas/risk_review.py
```

Initial decisions:

```text
auto_approved
pending_review
auto_rejected
blocked
escalated
```

Initial risk levels:

```text
low
medium
high
critical
invalid
```

Important:

The engine must return reasons and user-facing messages.

Example response:

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

Commit:

```text
Add deterministic risk review engine
```

---

## Phase 3 — Withdrawal Evaluation API

Goal:

Implement the first critical backend flow.

Endpoint:

```text
POST /api/withdrawals/evaluate
```

Input:

```json
{
  "asset": "BTC",
  "network": "Bitcoin",
  "amount": 0.001,
  "destination_address": "bc1qexample",
  "confirm_destination_address": "bc1qexample",
  "wallet_type": "external_crypto_service"
}
```

Backend flow:

```text
API route
  |
WithdrawalService
  |
Validation rules
  |
WalletRiskProvider
  |
RiskReviewEngine
  |
AuditService
  |
Decision response
```

Rules:

- amount must be greater than zero;
- asset must be supported;
- network must be compatible;
- destination address must not be empty;
- destination and confirmation must match;
- EURD external withdrawal is unavailable;
- first-time external address requires review;
- high-risk wallet signal blocks or escalates;
- known/whitelisted low amount may auto approve.

Commit:

```text
Add withdrawal evaluation endpoint
```

---

## Phase 4 — Audit Service

Goal:

Record every sensitive backend decision.

Create:

```text
backend/app/services/audit_service.py
backend/app/schemas/audit_event.py
```

Initial storage:

```text
in-memory list
```

Later:

```text
SQLite audit_events table
```

Endpoint:

```text
GET /api/audit-events
```

Audit events should include:

```text
event_id
timestamp
customer_id
module
action_type
entity_type
entity_id
status
risk_level
decision
reasons
case_id
user_message
```

Commit:

```text
Add audit event service
```

---

## Phase 5 — Review Case Service

Goal:

Create cases when the risk engine returns `case_required = true`.

Create:

```text
backend/app/services/review_case_service.py
backend/app/schemas/review_case.py
```

Endpoints:

```text
GET /api/review-cases
GET /api/review-cases/{case_id}
POST /api/review-cases/{case_id}/decision
```

Reviewer decisions:

```text
approve
reject
request_information
delay
escalate
```

Important:

Reviewer actions must create audit events.

Commit:

```text
Add review case service
```

---

## Phase 6 — Digital Asset Payment Evaluation API

Goal:

Implement controlled digital asset invoice payment evaluation.

Endpoint:

```text
POST /api/payments/digital-assets/evaluate
```

Input:

```json
{
  "recipient_name": "Aurora Telecom Oyj",
  "invoice_number": "90495185862",
  "reference_number": "80 60206 95479",
  "amount_eur": 120.45,
  "payment_asset": "EURD",
  "source_account_id": "aurora-current"
}
```

Rules:

- amount must be greater than zero;
- reference number must exist;
- recipient must have bank business account;
- recipient must accept digital asset payments;
- EURD payment has no additional processing fee in prototype;
- USDC/USDT/BTC/ETH may have simulated service and settlement fee;
- high-value payments may require review.

Commit:

```text
Add digital asset payment evaluation endpoint
```

---

## Phase 7 — Frontend Integration

Goal:

Connect existing frontend pages to backend endpoints.

Initial integrations:

```text
WithdrawalsPage -> POST /api/withdrawals/evaluate
PaymentsPage -> POST /api/payments/digital-assets/evaluate
ComplianceReviewPage -> GET /api/review-cases
ReportsPage -> GET /api/reports
```

Important:

Frontend should still work if backend is not running by using fallback mock data or clear development instructions.

Possible approach:

```text
frontend/src/services/apiClient.ts
frontend/src/services/withdrawalsApi.ts
frontend/src/services/paymentsApi.ts
frontend/src/services/reportsApi.ts
```

Commit:

```text
Connect frontend to backend evaluation APIs
```

---

## Phase 8 — SQLite Persistence

Goal:

Move from in-memory data to local persistence.

Create:

```text
backend/app/db/database.py
backend/app/db/seed.py
```

Initial tables:

```text
customers
accounts
bank_transactions
payment_recipients
invoice_payments
digital_asset_payments
external_withdrawals
review_cases
audit_events
reports
notifications
```

Important:

Audit events should be append-only by convention.

Commit:

```text
Add SQLite persistence for backend prototype
```

---

## Phase 9 — Reporting and Evidence Package

Goal:

Connect reports to actual simulated backend records.

Endpoint:

```text
GET /api/reports
GET /api/reports/tax-summary/2026
POST /api/reports/evidence-package
```

Reports should aggregate:

- invoice payments;
- digital asset payments;
- buy/sell events;
- withdrawals;
- review cases;
- audit events.

Commit:

```text
Add backend reporting service
```

---

## 8. Initial API Contract Summary

### Health

```text
GET /api/health
```

### Accounts

```text
GET /api/accounts
GET /api/accounts/{account_id}/transactions
```

### Digital Assets

```text
GET /api/digital-assets/assets
GET /api/digital-assets/wallet
```

### Payments

```text
POST /api/payments/digital-assets/evaluate
POST /api/payments/digital-assets
```

### Withdrawals

```text
POST /api/withdrawals/evaluate
POST /api/withdrawals
GET /api/withdrawals
```

### Review Cases

```text
GET /api/review-cases
GET /api/review-cases/{case_id}
POST /api/review-cases/{case_id}/decision
```

### Audit Events

```text
GET /api/audit-events
```

### Reports

```text
GET /api/reports
GET /api/reports/tax-summary/{year}
POST /api/reports/evidence-package
```

---

## 9. Risk Engine First Implementation Rules

The first coded version should include only clear deterministic rules.

### Universal Rules

```text
IF amount <= 0
THEN auto_rejected
REASON = invalid_amount
```

```text
IF asset unsupported
THEN auto_rejected
REASON = unsupported_asset
```

### Withdrawal Rules

```text
IF asset == EURD
THEN auto_rejected
REASON = external_withdrawal_unavailable_for_internal_settlement_asset
```

```text
IF destination_address != confirm_destination_address
THEN auto_rejected
REASON = destination_address_mismatch
```

```text
IF network incompatible with asset
THEN auto_rejected
REASON = incompatible_network
```

```text
IF wallet_risk_signal == high
THEN blocked
REASON = high_risk_wallet_signal
```

```text
IF first_time_address == true
THEN pending_review
REASON = first_time_external_address
```

### Digital Asset Payment Rules

```text
IF recipient_has_bank_account == false
THEN auto_rejected
REASON = recipient_not_inside_bank
```

```text
IF recipient_accepts_digital_asset_payments == false
THEN auto_rejected
REASON = recipient_not_enabled
```

```text
IF reference_number empty
THEN auto_rejected
REASON = missing_reference_number
```

```text
IF amount <= max_auto_approve_payment
THEN auto_approved
RISK = low
```

```text
IF amount > max_auto_approve_payment
THEN pending_review
RISK = medium
REASON = high_value_payment
```

---

## 10. Configuration Values

Suggested configuration:

```text
APP_NAME=Aurora Digital Assets Backend
APP_ENV=development
API_PREFIX=/api
DATABASE_URL=sqlite:///./aurora.db
DEFAULT_CUSTOMER_ID=demo-customer
SUPPORTED_ASSETS=BTC,ETH,USDC,USDT,EURD
MAX_AUTO_APPROVE_WITHDRAWAL_EUR=250
MAX_AUTO_APPROVE_PAYMENT_EUR=500
FIRST_WITHDRAWAL_REQUIRES_REVIEW=true
NEW_ADDRESS_REQUIRES_REVIEW=true
```

File:

```text
backend/app/core/config.py
```

---

## 11. Frontend Compatibility Requirements

The frontend currently uses local mock data.

Backend integration should not break the frontend.

Recommended strategy:

1. Create API service files in frontend.
2. Keep fallback mock data.
3. Use environment variable for backend URL.

Example:

```text
VITE_API_BASE_URL=http://localhost:8000/api
```

If backend is not available:

- show existing mock data;
- log development warning;
- keep page usable.

This allows the prototype to remain demo-ready.

---

## 12. Testing Requirements

The first backend tests should focus on risk decisions.

### Withdrawal Tests

- EURD withdrawal returns auto_rejected.
- Invalid amount returns auto_rejected.
- Address mismatch returns auto_rejected.
- Incompatible network returns auto_rejected.
- First-time external address returns pending_review.
- High-risk wallet signal returns blocked.
- Known whitelisted low-risk address returns auto_approved.

### Digital Asset Payment Tests

- Missing reference number returns auto_rejected.
- Recipient outside bank returns auto_rejected.
- Recipient not enabled returns auto_rejected.
- Eligible low-value EURD payment returns auto_approved.
- High-value USDC payment returns pending_review.

### Review Case Tests

- pending_review creates case;
- reviewer decision updates case;
- reviewer decision creates audit event.

### Audit Tests

- evaluation creates audit event;
- case creation creates audit event;
- report generation creates audit event.

---

## 13. Development Commands

Suggested setup:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Expected local API:

```text
http://localhost:8000/api/health
```

Testing:

```bash
pytest
```

---

## 14. Definition of Done for Backend v0.1

Backend v0.1 is complete when:

- FastAPI backend starts locally;
- `/api/health` works;
- `/api/withdrawals/evaluate` works;
- `/api/payments/digital-assets/evaluate` works;
- risk decisions are deterministic and explainable;
- audit events are recorded;
- review cases are created for pending review decisions;
- `/api/review-cases` returns cases;
- `/api/audit-events` returns audit events;
- tests cover initial risk rules;
- no real bank, custody, AML, or blockchain integrations exist;
- documentation is updated.

---

## 15. Suggested Commit Sequence

Recommended commits:

```text
Initialize backend skeleton
Add backend schemas and mock providers
Add deterministic risk review engine
Add withdrawal evaluation endpoint
Add audit event service
Add review case service
Add digital asset payment evaluation endpoint
Add backend tests for risk review engine
Add backend README instructions
```

Avoid one massive backend commit.

Small commits will make the project history easier to understand.

---

## 16. Open Questions

Important questions before coding:

- Should the first backend use in-memory storage or SQLite immediately?
- Should SQLModel be used instead of SQLAlchemy?
- Should review cases be created during evaluation or only after submit?
- Should audit events be recorded for evaluation-only actions?
- Should API schemas mirror frontend types exactly?
- Should the frontend keep fallback mocks after backend integration?
- Should internal routes require a mocked reviewer role?
- Should risk thresholds be constants or config values?
- Should rules be Python functions or JSON-configurable policies?
- Should reports be generated from stored events immediately or remain static first?

---

## 17. Conclusion

The backend implementation should start small but with the correct architecture.

The first real backend value is not executing payments or crypto transfers.

The first real backend value is the **Risk & Review Engine**:

- evaluate sensitive actions;
- return explainable decisions;
- create audit events;
- create review cases;
- support human review;
- prepare the system for real integrations later.

This approach keeps the prototype practical while avoiding a throwaway architecture.

Aurora Digital Assets should be built as a controlled, auditable banking system from the beginning, even while all data and integrations remain simulated.

---

## 18. Disclaimer

This document describes an implementation plan for a prototype backend only.

Aurora Digital Assets is not a bank, not a custody provider, not a crypto exchange, not a payment institution, and not a regulated financial service.

The backend implementation described here is fictional and intended for product design, architecture planning, software development, compliance discussion, and portfolio demonstration.

No real bank systems, real customer data, AML checks, custody services, private keys, payments, or blockchain transactions are used.
