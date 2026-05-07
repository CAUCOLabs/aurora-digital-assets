# Bank Digital Assets Architecture

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)  
**Status:** v0.2 architecture planning document  
**Version:** 0.1  
**Date:** 2026-05-07  

---

## 1. Purpose

This document defines the high-level architecture for Aurora Digital Assets as a bank-integrated digital assets framework.

The goal is to describe how a traditional online banking platform could safely integrate a digital assets layer without becoming a speculative crypto exchange.

Aurora Digital Assets is designed around three architectural realities:

1. **Banks already have a strong trust and security base**  
   Customer authentication, identity, account protection, notifications, audit logs, and regulated financial workflows already exist inside the banking environment.

2. **Digital assets introduce new operational and compliance costs**  
   Custody, tax reporting, AML monitoring, wallet risk checks, withdrawal review, support, and audit evidence are real cost drivers.

3. **Custody transparency is essential**  
   Users need to understand where their digital assets are held, who controls the private keys, what protections apply inside the bank, and what changes when assets leave the banking environment.

This architecture document connects the normal banking layer with the proposed digital assets extension layer.

---

## 2. Architecture Principles

Aurora Digital Assets should follow these principles:

### 2.1 Banking First

Digital assets should be integrated into the banking environment, not presented as a separate speculative trading app.

The user should feel they are inside online banking.

### 2.2 Security by Design

Security should not be an extra feature.

It should be part of every flow:

- login;
- payments;
- buy/sell;
- custody;
- reporting;
- external withdrawals;
- digital asset payments.

### 2.3 Compliance by Design

AML, transaction monitoring, sanctions screening, audit logs, and case review should be designed into the architecture from the beginning.

### 2.4 Custody Transparency

The system must clearly explain:

- who holds the asset;
- who controls private keys;
- whether assets are internally custodied or held by a regulated partner;
- whether assets are separate from bank deposits;
- what protections apply before and after external withdrawal.

### 2.5 Controlled Product Scope

The product should reduce risk through constraints:

- limited asset scope;
- spot-only access;
- no leverage;
- no derivatives;
- no speculative trading features;
- no open payments to arbitrary crypto addresses;
- controlled external withdrawals;
- digital asset payments only to verified business recipients.

### 2.6 Auditability

Every sensitive action should create an audit event.

The system should support both customer-facing records and internal evidence packages.

---

## 3. High-Level Architecture

Aurora Digital Assets can be seen as two connected platforms:

1. **Core Banking Platform**
2. **Digital Assets Extension Layer**

High-level view:

```text
Customer
   |
Web / Mobile Banking UI
   |
Strong Authentication & Session Layer
   |
----------------------------------------------------
|                                                  |
Core Banking Platform                 Digital Assets Extension Layer
|                                                  |
Accounts Service                      Digital Assets Module
Payments Service                      Wallet & Custody Service
Cards Service                         Custody Transparency Service
Loans / Investments / Insurance       Buy / Sell Service
Documents & Bank Mail                 Digital Asset Payments Service
Notifications                         External Withdrawal Service
Fraud Monitoring                      Market Price Service
Audit Log                             Tax Reporting Service
|                                                  |
---------------- Shared Security & Compliance -----
                       |
              Compliance / AML Engine
                       |
              Risk Scoring & Review
                       |
              Case Management
                       |
              Reporting & Evidence
```

The digital assets layer does not replace the banking platform.

It extends it.

---

## 4. Core Banking Layer

The Core Banking Layer represents traditional online banking capabilities.

### 4.1 Customer Interface

Components:

- web banking;
- mobile banking;
- navigation;
- user dashboard;
- account overview;
- payment flows;
- documents and bank mail;
- notification views.

Responsibilities:

- provide trusted user access;
- display account and product data;
- route users into banking services;
- expose digital assets as a controlled banking module.

### 4.2 Authentication and Session Layer

Responsibilities:

- strong customer authentication;
- session management;
- device recognition;
- login security;
- step-up authentication for sensitive actions;
- logout and session expiration.

Digital assets should reuse this layer rather than creating a separate login model.

### 4.3 Customer Identity Layer

Responsibilities:

- customer identity records;
- customer profile;
- customer risk category;
- business customer profile;
- relationship data;
- onboarding records.

Digital asset eligibility should depend on this layer.

### 4.4 Accounts Service

Responsibilities:

- current account balances;
- available balance;
- account owner;
- IBAN/BIC;
- account transactions;
- account statements;
- account status.

Digital assets may connect to accounts for funding buy/sell activity and invoice payments, but digital assets must not be presented as deposits.

### 4.5 Payments Service

Responsibilities:

- domestic payments;
- invoice payments;
- reference numbers;
- due dates;
- recipients;
- payment limits;
- payment confirmations;
- payment history.

The Digital Asset Payments Service extends this layer only for verified business recipients.

### 4.6 Cards, Loans, Investments, Insurance

These services provide normal banking completeness.

They are not the main focus of Aurora Digital Assets, but they help the prototype feel like a real banking portal.

### 4.7 Documents and Bank Mail

Responsibilities:

- account statements;
- payment receipts;
- reports;
- notices;
- tax summaries;
- PDF/CSV exports;
- customer messages.

Digital asset reports should appear here as banking documents.

### 4.8 Notifications

Responsibilities:

- payment notifications;
- withdrawal status;
- review status;
- security alerts;
- report availability;
- account messages.

Digital asset events should use normal banking notification channels.

### 4.9 Core Audit Log

Responsibilities:

- login events;
- account access;
- payment actions;
- document access;
- security events;
- user actions.

Digital asset audit events may be connected to or mirrored into the core audit log.

---

## 5. Digital Assets Extension Layer

The Digital Assets Extension Layer provides the crypto/digital coin functionality inside the bank.

### 5.1 Digital Assets Module

Responsibilities:

- Digital Assets overview;
- portfolio value;
- asset balances;
- quick actions;
- risk notices;
- module navigation.

This module is the customer-facing entry point.

### 5.2 Asset Eligibility Service

Responsibilities:

- define which assets are supported;
- separate investment-oriented assets from payment-oriented assets;
- define customer eligibility;
- define business recipient eligibility;
- control availability by region, customer type, and risk profile.

Suggested asset categories:

```text
Investment / holding assets:
- BTC
- ETH

Payment-oriented assets:
- EUR digital asset concept
- USDC
- USDT

Future / concept assets:
- XRP cross-border concept
```

### 5.3 Wallet and Custody Service

Responsibilities:

- show wallet balances;
- track internal custodial wallet status;
- connect to custody provider or internal custody layer;
- manage supported assets;
- show wallet activity;
- prevent exposure of seed phrases or private keys to retail users.

The wallet service should not imply that assets are bank deposits.

### 5.4 Custody Transparency Service

Responsibilities:

- explain custody model;
- show who controls what;
- disclose whether the user manages private keys;
- explain internal custody or partner custody;
- show what changes after external withdrawal;
- keep user-facing custody explanations aligned with actual backend state.

Example customer-facing questions:

- Where is my asset held?
- Who controls the keys?
- Can I withdraw externally?
- What protections apply inside the bank?
- What risks apply outside the bank?

### 5.5 Market Price Service

Responsibilities:

- provide simulated or real market prices;
- calculate estimated buy/sell amounts;
- calculate payment conversion estimates;
- show timestamp and source concept;
- support audit records for estimates shown to users.

For the current prototype, this service is mocked.

### 5.6 Buy / Sell Service

Responsibilities:

- select asset;
- select funding account;
- enter amount;
- estimate asset received or EUR received;
- show fee/spread;
- show volatility warning;
- confirm simulated order;
- create audit event;
- update reportable activity.

Constraints:

- spot-only;
- no leverage;
- no derivatives;
- no trading chart-first interface;
- no speculative language.

### 5.7 Digital Asset Payments Service

Responsibilities:

- allow invoice payments using supported digital assets;
- preserve recipient, invoice number, reference number, due date, and amount;
- validate recipient eligibility;
- allow digital asset payment only to verified business recipients inside the bank;
- show conversion estimate;
- show settlement model;
- create payment record;
- create audit event;
- update reports.

Important boundary:

```text
Digital asset payments are not arbitrary wallet transfers.
They are controlled payments to verified business recipients inside the banking environment.
```

### 5.8 External Withdrawal Service

Responsibilities:

- select asset;
- select network;
- enter destination address;
- confirm amount;
- show irreversible transfer warning;
- perform address checks;
- require strong authentication;
- apply review rules;
- create withdrawal request;
- track state.

Possible states:

```text
Draft
Pending review
Approved
Rejected
Delayed
Completed
```

External withdrawals are a higher-risk flow because assets leave the banking environment.

### 5.9 Tax Reporting Service

Responsibilities:

- collect reportable digital asset activity;
- show annual summary;
- show purchases, sales, transfers, and payments;
- show estimated gain/loss concept;
- generate PDF/CSV export concept;
- support audit evidence package.

This service should not provide official tax advice unless integrated with regulated tax processes.

### 5.10 Digital Asset Audit Trail

Responsibilities:

- record every sensitive digital asset action;
- connect events to user, account, asset, amount, status, and timestamp;
- support customer-facing history;
- support internal review;
- support evidence export.

Example events:

- Digital Assets module opened;
- buy/sell estimate generated;
- buy request submitted;
- wallet balance updated;
- custody status shown;
- invoice payment estimate generated;
- external withdrawal address submitted;
- withdrawal review completed;
- report generated.

---

## 6. Shared Security Controls

The strongest architecture is not separate bank security and crypto security.

The strongest architecture uses shared controls.

### 6.1 Strong Customer Authentication

Used for:

- login;
- payment submission;
- buy/sell confirmation;
- external withdrawal submission;
- changing wallet or transfer settings;
- viewing sensitive documents.

### 6.2 Step-Up Authentication

Required for higher-risk actions:

- new recipient;
- large payment;
- digital asset payment;
- new external wallet address;
- first external withdrawal;
- unusual transaction pattern.

### 6.3 Device and Session Security

Controls:

- known device recognition;
- session expiration;
- suspicious session detection;
- login alerts;
- high-risk device checks.

### 6.4 Limits

Limits may apply to:

- daily buy/sell amount;
- digital asset payment amount;
- external withdrawal amount;
- first-time address withdrawal amount;
- new user activity;
- high-risk asset categories.

### 6.5 Notifications

Security notifications should be sent for:

- new digital asset activation;
- buy/sell confirmation;
- digital asset payment submission;
- external withdrawal request;
- withdrawal approval/rejection;
- report generation;
- unusual activity.

---

## 7. Compliance, AML and Risk Architecture

The compliance layer responds directly to the operational concern that banks inherit cost and responsibility when they offer digital asset access.

### 7.1 Compliance / AML Engine

Responsibilities:

- monitor digital asset activity;
- screen recipients and counterparties;
- detect unusual behavior;
- apply policy rules;
- assign risk levels;
- trigger review cases;
- support regulatory reporting concepts.

### 7.2 Transaction Monitoring

Applies to:

- buy/sell activity;
- digital asset invoice payments;
- external withdrawal requests;
- repeated failed attempts;
- unusual amounts;
- unusual timing;
- new recipient patterns.

### 7.3 Wallet Risk Checks

Applies to:

- external withdrawal addresses;
- known risky wallets;
- high-risk patterns;
- first-time addresses;
- network mismatch;
- address format validation.

### 7.4 Sanctions Screening

Applies to:

- business recipients;
- external wallet risk sources;
- counterparties;
- payment flows.

### 7.5 Travel Rule Concept

For applicable digital asset transfers, the architecture should leave space for Travel Rule data handling.

Prototype scope:

- no real Travel Rule processing;
- only conceptual readiness.

### 7.6 Risk Scoring

Risk score inputs may include:

- customer profile;
- asset type;
- amount;
- destination;
- recipient type;
- new address;
- historical behavior;
- device/session context;
- payment or withdrawal type.

### 7.7 Review Rules

Examples:

- first external withdrawal requires review;
- new address requires review or delay;
- high-value withdrawal requires review;
- risky wallet destination is blocked or escalated;
- unusual payment pattern creates case.

---

## 8. Case Management Architecture

Banks need operational workflows, not just automatic decisions.

### 8.1 Case Creation

Cases may be created from:

- external withdrawal risk;
- suspicious payment;
- large digital asset transfer;
- address risk flag;
- account takeover suspicion;
- customer support escalation.

### 8.2 Case Data

A case may include:

- customer;
- action type;
- asset;
- amount;
- destination;
- risk score;
- audit events;
- reviewer notes;
- decision;
- timestamps.

### 8.3 Case Status

Possible statuses:

```text
Open
Pending review
More information needed
Approved
Rejected
Escalated
Closed
```

### 8.4 Human-in-the-Loop Review

The system should not act as an autonomous decision-maker for sensitive cases.

Human reviewers should be able to:

- inspect evidence;
- approve;
- reject;
- delay;
- request more information;
- add notes.

---

## 9. Custody Architecture

Custody is the core trust question.

### 9.1 Custody Modes

Possible models:

1. **Internal custodial wallet**
2. **Regulated custody partner**
3. **External personal wallet after withdrawal**

### 9.2 Internal Custodial Wallet

Responsibilities:

- show balances;
- record internal asset movements;
- maintain custody status;
- connect with audit records;
- prevent seed phrase exposure;
- provide user-facing custody explanation.

### 9.3 Regulated Custody Partner

Responsibilities:

- hold or administer assets;
- provide custody records;
- support reconciliation;
- provide operational status;
- support incident response;
- integrate with bank reporting.

### 9.4 External Wallet Boundary

When assets leave the bank:

- bank-side protections may no longer apply;
- transfers may be irreversible;
- user responsibility increases;
- wrong addresses may cause permanent loss;
- reporting may become harder.

The UI and backend must treat this as a distinct risk boundary.

### 9.5 Custody Transparency Data

The system should store and display:

- custody mode;
- supported asset;
- whether withdrawal is enabled;
- whether user controls keys;
- whether assets are separate from deposits;
- custody partner, if applicable;
- user-facing custody disclosure.

---

## 10. Digital Asset Payments Architecture

Digital asset payments are not the same as withdrawals.

### 10.1 Payment Eligibility

A digital asset payment is allowed only when:

- recipient is a verified business customer;
- recipient has a bank business account;
- recipient has enabled digital asset payments;
- accepted assets are configured;
- settlement preference is configured;
- invoice/reference data exists.

### 10.2 Payment Flow

```text
Customer enters Payments
        |
Inputs invoice details
        |
System validates recipient
        |
System checks digital asset payment eligibility
        |
Customer selects payment method
        |
Estimate is generated
        |
Customer confirms
        |
Payment record is created
        |
Audit event is created
        |
Recipient settlement is processed
        |
Reports are updated
```

### 10.3 Settlement Options

Possible models:

- customer pays digital asset and recipient receives EUR;
- customer pays digital asset and recipient receives selected asset;
- internal EUR digital asset settlement concept;
- stablecoin settlement concept.

### 10.4 Fee Logic

Prototype model:

```text
EUR bank transfer:
- no digital asset processing fee

EUR digital asset concept:
- no additional processing fee in prototype
- internal settlement concept

USDC / USDT:
- simulated service fee
- simulated settlement fee

BTC / ETH:
- simulated service fee
- volatility warning
- optional / not preferred for invoice payments
```

### 10.5 Reporting

Digital asset payments should appear in:

- payment history;
- account activity;
- digital asset activity;
- tax/reporting view;
- audit trail;
- documents/receipts.

---

## 11. External Withdrawal Architecture

External withdrawals are the highest-risk customer action in the digital assets module.

### 11.1 Withdrawal Flow

```text
Customer enters Withdrawals
        |
Selects asset and network
        |
Enters destination address
        |
System validates format
        |
Risk warning is shown
        |
Strong authentication is required
        |
Risk score is calculated
        |
Request may enter review
        |
Case may be created
        |
Decision is recorded
        |
Withdrawal is completed, delayed, rejected, or blocked
```

### 11.2 Withdrawal Controls

Controls:

- address confirmation;
- address format validation;
- network compatibility warning;
- first-time address review;
- optional address whitelist;
- cooling period;
- withdrawal limits;
- risk scoring;
- manual review;
- audit event creation.

### 11.3 Withdrawal Review

Review decisions:

- approve;
- reject;
- delay;
- request more information;
- escalate to compliance.

### 11.4 User Messaging

The user should see:

- transfer is irreversible;
- asset may leave bank protection environment;
- bank may not recover funds sent to wrong address;
- review may take time;
- audit trail is created.

---

## 12. Reporting and Evidence Architecture

### 12.1 Customer Reports

Customer-facing reports:

- annual summary;
- purchase history;
- sale history;
- digital asset payments;
- external transfers;
- estimated gain/loss concept;
- PDF/CSV export.

### 12.2 Internal Evidence Package

Internal review may require:

- timeline;
- audit events;
- customer action;
- system estimate shown;
- risk score;
- review notes;
- decision;
- communication history.

### 12.3 Documents Integration

Reports should be available through:

- Digital Assets Reports;
- Documents;
- Bank mail;
- downloadable PDF/CSV.

### 12.4 Audit Event Structure

Suggested fields:

```text
event_id
timestamp
customer_id
session_id
action_type
asset
amount
currency
source_account
destination
risk_score
status
user_message
review_case_id
```

---

## 13. Operational Risk and Cost Controls

This section responds to the operational concern that digital assets can create heavy cost for banks.

### 13.1 Cost Drivers

Cost drivers:

- custody operations;
- AML monitoring;
- wallet risk checks;
- tax reporting;
- customer support;
- dispute handling;
- fraud response;
- external withdrawal review;
- compliance evidence;
- incident response.

### 13.2 Risk-Reducing Product Constraints

Constraints:

- limited assets;
- no leverage;
- no derivatives;
- no high-frequency trading design;
- no open recipient crypto payments;
- verified business recipients only for digital asset payments;
- reviewed external withdrawals;
- reporting-first architecture;
- custody transparency;
- conservative UX.

### 13.3 Business Value Sources

Potential value sources:

- custody/service fee;
- transparent transaction fee;
- reporting services;
- business payment services;
- customer retention;
- trust;
- premium banking integration;
- long-term digital asset infrastructure positioning.

### 13.4 Why Not Compete with Exchanges

A bank should not try to win by becoming a cheaper exchange.

The bank model should compete on:

- trust;
- reporting;
- safety;
- account integration;
- custody clarity;
- controlled payments;
- responsible access;
- regulated relationship.

---

## 14. Future Backend Implementation

A possible backend implementation could include:

```text
frontend/
  React + TypeScript banking UI

backend/
  FastAPI application

database/
  PostgreSQL or SQLite for prototype

services/
  account_service
  payment_service
  digital_asset_service
  custody_service
  compliance_service
  reporting_service
  audit_service
  notification_service
```

### 14.1 Suggested Backend Services

#### Account Service

- accounts;
- balances;
- account transactions;
- account metadata.

#### Payment Service

- invoice payments;
- recipients;
- references;
- due dates;
- payment records.

#### Digital Asset Service

- wallet balances;
- supported assets;
- buy/sell records;
- payment estimates.

#### Custody Service

- custody mode;
- custody partner status;
- wallet status;
- external withdrawal permissions.

#### Compliance Service

- risk rules;
- risk scoring;
- monitoring;
- review triggers.

#### Case Management Service

- cases;
- reviewer actions;
- status;
- evidence.

#### Reporting Service

- tax summaries;
- PDF/CSV exports;
- document generation.

#### Audit Service

- immutable event log;
- event search;
- evidence timeline.

### 14.2 Suggested Database Entities

```text
customers
accounts
bank_transactions
digital_assets
wallet_balances
digital_asset_transactions
payment_recipients
invoice_payments
digital_asset_payments
external_withdrawals
custody_status
risk_events
review_cases
audit_events
reports
notifications
```

### 14.3 Prototype Evolution

Current state:

- frontend mock data;
- simulated flows;
- no backend;
- no real custody;
- no real payments.

Next backend step:

- FastAPI mock backend;
- SQLite persistence;
- local audit events;
- simulated risk engine;
- generated PDF reports.

---

## 15. Architecture Diagrams to Create

Recommended diagrams:

1. **System Overview**
   - core banking + digital assets extension.

2. **Security Layers**
   - authentication, authorization, fraud, compliance, custody protection.

3. **Custody Flow**
   - internal custody, partner custody, external wallet boundary.

4. **Digital Asset Payment Flow**
   - invoice payment using digital assets to verified business recipient.

5. **External Withdrawal Review Flow**
   - address input, risk score, review, approval/rejection.

6. **Audit and Reporting Flow**
   - event capture, report generation, evidence package.

Suggested file paths:

```text
docs/architecture/bank-digital-assets-architecture.drawio
docs/architecture/security-layers.drawio
docs/architecture/custody-flow.drawio
docs/architecture/digital-asset-payment-flow.drawio
docs/architecture/withdrawal-review-flow.drawio
docs/architecture/audit-reporting-flow.drawio
```

---

## 16. Open Questions

Important questions:

- Should custody be internal or partner-based?
- What assets should be supported first?
- Should digital asset payments support stablecoins before a regulated EUR digital asset exists?
- Should BTC/ETH be available for payments or only holding?
- What withdrawal limits should apply?
- What actions require step-up authentication?
- What risk rules should trigger manual review?
- How should Travel Rule obligations be handled?
- What reporting must be customer-facing?
- What reporting must be internal?
- What operational model justifies cost?
- What support workflows are required?
- How should scams and social engineering be handled?
- What data must be stored for audit?
- What should be immutable?
- Which parts should be built by the bank and which by partners?

---

## 17. Conclusion

Aurora Digital Assets should be designed as a controlled extension of online banking, not as a separate crypto application.

The architecture must start with the bank’s existing trust layer:

- authentication;
- identity;
- account protection;
- payment records;
- documents;
- notifications;
- audit logs;
- compliance processes.

The digital assets layer then adds:

- custody;
- wallet balances;
- buy/sell;
- digital asset payments;
- external withdrawals;
- reporting;
- AML monitoring;
- review cases;
- custody transparency.

The strongest version of this product is not a bank trying to become an exchange.

It is a bank using its security, trust, reporting, and customer relationship infrastructure to make digital asset access safer, clearer, and more responsible.

---

## 18. Disclaimer

This document describes a product and architecture concept only.

Aurora Digital Assets is not a bank, not a custody provider, not a crypto exchange, not a payment institution, and not a regulated financial service.

The architecture described here is fictional and intended for product design, UX, compliance discussion, technical planning, and portfolio demonstration.

No real assets, bank systems, private keys, customer data, financial credentials, payments, or blockchain transactions are used.
