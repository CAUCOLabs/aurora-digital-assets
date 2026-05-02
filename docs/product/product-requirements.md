# Product Requirements Document

## Aurora Digital Assets
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)
**Status:** Draft
**Version:** 0.1
**Date:** 2026-05-02

---

## 1. Purpose

Aurora Digital Assets is a concept prototype for integrating a digital assets wallet module inside a fictional online banking environment.

The purpose of this prototype is to demonstrate how a Finnish or Nordic bank could offer safer, regulated, and user-protective access to crypto assets without creating an exchange-like or speculative trading experience.

The prototype focuses on:

- banking-first UX;
- digital asset access;
- internal custodial wallet concept;
- controlled external wallet withdrawal;
- compliance visibility;
- audit trail;
- tax reporting concept;
- user protection.

---

## 2. Product Vision

Retail crypto access should not depend only on global exchanges or speculative trading platforms.

Banks could provide a safer bridge between traditional finance and digital assets by integrating crypto access into an existing online banking environment.

Aurora Digital Assets explores this model through a fictional bank called **Aurora Bank**.

The product should feel like a banking module, not like a crypto exchange.

---

## 3. Target Users

### 3.1 Retail Banking User

A normal bank customer who wants limited, responsible access to digital assets such as BTC or ETH.

Needs:

- simple interface;
- clear risk warnings;
- custody explanation;
- tax reporting;
- safe withdrawal flow;
- familiar banking environment.

### 3.2 Compliance / Risk Reviewer

A bank-side reviewer who needs visibility into digital asset actions.

Needs:

- transaction monitoring status;
- withdrawal review state;
- audit log;
- risk events;
- case concept;
- reportable evidence.

### 3.3 Product / Innovation Stakeholder

A bank, fintech, or research stakeholder evaluating whether bank-integrated digital assets could be offered safely.

Needs:

- clear product concept;
- architecture;
- user flows;
- compliance logic;
- UI prototype;
- limitations and future roadmap.

---

## 4. Scope for Version 0.1

Version 0.1 is a simulated web prototype.

It will include:

- fictional Aurora Bank dashboard;
- account overview;
- Digital Assets navigation module;
- digital assets overview page;
- simulated BTC and ETH balances;
- simulated buy flow;
- simulated sell flow;
- simulated external wallet withdrawal flow;
- compliance and security status;
- audit trail view;
- tax report view;
- local mock data.

Version 0.1 will not include:

- real bank API integration;
- real crypto custody;
- real blockchain transactions;
- real KYC provider integration;
- real private keys;
- real trading execution;
- real user accounts;
- production authentication;
- financial advice.

---

## 5. Product Modules

### 5.1 Banking Dashboard

The main dashboard should simulate a Nordic online banking portal.

Requirements:

- show fictional user name;
- show current account balance;
- show savings account balance;
- show card or credit account example;
- show Digital Assets Wallet as a separated financial section;
- show notifications;
- show top navigation;
- use calm banking visual design.

Acceptance criteria:

- user can visually understand this is a banking environment;
- Digital Assets appears integrated but clearly separated from deposits;
- no real bank branding is used.

---

### 5.2 Digital Assets Overview

The Digital Assets overview page should summarize the user's crypto position.

Requirements:

- show total digital assets value in EUR;
- show BTC balance;
- show ETH balance;
- show latest mock BTC/EUR and ETH/EUR prices;
- show recent digital asset transactions;
- show custody status;
- show risk profile;
- show quick actions: Buy, Sell, Withdraw, Reports.

Acceptance criteria:

- user can understand total value and asset breakdown;
- user sees that digital assets are volatile and separate from deposits;
- user can navigate to buy/sell, wallet, withdrawals, and reports.

---

### 5.3 Buy Crypto Flow

The buy flow should simulate purchasing BTC or ETH with EUR from a bank account.

Requirements:

- select funding account;
- select asset: BTC or ETH;
- enter EUR amount;
- calculate estimated crypto amount using mock market price;
- show estimated fee;
- show estimated spread;
- show volatility warning;
- show custody explanation;
- require final confirmation.

Acceptance criteria:

- buy flow does not look like trading;
- all costs are visible before confirmation;
- user receives risk warning before completing the simulated purchase;
- simulated transaction is recorded in mock transaction history or displayed as completed.

---

### 5.4 Sell Crypto Flow

The sell flow should simulate selling BTC or ETH into EUR.

Requirements:

- select asset;
- enter crypto amount;
- calculate estimated EUR amount;
- show estimated fee;
- show tax reminder;
- require final confirmation.

Acceptance criteria:

- user understands sale may have tax consequences;
- simulated sale updates or displays transaction result;
- transaction appears in recent activity or audit trail.

---

### 5.5 Internal Crypto Wallet

The internal wallet page should show assets held through the simulated bank custody layer.

Requirements:

- show BTC balance;
- show ETH balance;
- show EUR equivalent values;
- show custody status;
- show transaction history;
- show wallet activity;
- show supported assets.

Acceptance criteria:

- user understands this is an internal custodial wallet concept;
- wallet does not expose private keys or seed phrases;
- UI avoids suggesting that the user directly controls private keys.

---

### 5.6 External Wallet Withdrawal

The withdrawal flow should simulate sending crypto to a personal external wallet.

Requirements:

- select asset;
- select network;
- enter destination address;
- confirm address;
- show irreversible transfer warning;
- show external wallet responsibility warning;
- run simulated compliance check;
- show withdrawal state.

Possible states:

- draft;
- pending review;
- approved;
- rejected;
- completed.

Acceptance criteria:

- withdrawal flow feels more serious than a normal transfer;
- user sees clear warning about irreversible transactions;
- system shows compliance/risk status;
- withdrawal creates an audit event.

---

### 5.7 Compliance and Security

The compliance/security page should show how the bank protects users and reviews activity.

Requirements:

- show KYC verified status;
- show risk profile;
- show transaction monitoring enabled;
- show external withdrawal protection;
- show audit trail enabled;
- show recent compliance events.

Acceptance criteria:

- user can see why some actions may require review;
- compliance is presented as user protection, not only restriction;
- language remains clear and non-technical.

---

### 5.8 Audit Trail

The audit trail should show simulated system events.

Requirements:

- timestamp;
- event type;
- user action;
- status;
- related transaction;
- compliance result when applicable.

Example events:

- Digital Assets module activated;
- BTC purchase requested;
- BTC purchase completed;
- withdrawal address submitted;
- compliance check completed;
- withdrawal approved;
- tax report generated.

Acceptance criteria:

- events are readable and ordered;
- audit trail supports the compliance narrative;
- no real personal data is shown.

---

### 5.9 Tax Reports

The tax report page should simulate annual crypto reporting.

Requirements:

- show selected tax year;
- show purchases;
- show sales;
- show transfers;
- show estimated realized gain/loss concept;
- show PDF export button;
- show CSV export button;
- show disclaimer that values are simulated.

Acceptance criteria:

- user understands the bank can help organize crypto tax records;
- UI does not claim to provide official tax advice;
- export buttons can be simulated in v0.1.

---

## 6. UX Requirements

The UI must feel like a serious online banking environment.

Design requirements:

- dark blue navigation;
- light grey-blue background;
- white content cards;
- clear tables;
- conservative spacing;
- simple icons;
- calm typography;
- no crypto hype;
- no speculative design language.

The UI must avoid:

- neon colors;
- casino-like visuals;
- "moon" language;
- leverage or futures features;
- aggressive trading charts;
- profit-promising language.

---

## 7. Content Requirements

The product language should use responsible terms.

Recommended terms:

- digital assets;
- custody;
- risk warning;
- volatility;
- tax reporting;
- external wallet;
- compliance review;
- audit trail;
- transaction monitoring;
- user protection.

Avoided terms:

- guaranteed returns;
- passive income;
- get rich;
- moon;
- pump;
- 100x;
- financial freedom;
- risk-free.

---

## 8. Data Requirements

Version 0.1 should use local mock data only.

Mock data files:

- `mock-data/user-profile.json`
- `mock-data/bank-accounts.json`
- `mock-data/crypto-wallet.json`
- `mock-data/transactions.json`
- `mock-data/compliance-events.json`
- `mock-data/market-prices.json`

No real user financial data should be used.

No screenshots containing real bank data should be committed.

No real private keys, seed phrases, API keys, or bank credentials should be added to the repository.

---

## 9. Technical Requirements

### 9.1 Frontend

Suggested stack:

- React;
- TypeScript;
- Vite;
- Tailwind CSS;
- React Router;
- Recharts or Chart.js.

Frontend should initially consume local mock JSON data.

### 9.2 Backend

Suggested future stack:

- Python;
- FastAPI;
- Pydantic;
- SQLite;
- PDF generation library.

The backend may be added after the first static UI prototype.

### 9.3 Architecture

Initial architecture:

```text
Aurora Bank Online Portal
        |
Digital Assets Module
        |
Mock Banking Data
Mock Wallet Data
Mock Market Data
Mock Compliance Data
        |
Reports and Audit Trail
```

Future architecture:

```text
Aurora Bank Online Portal
        |
Digital Assets Module
        |
Banking Account Service
Crypto Wallet Service
Market Price Service
Compliance Engine
Audit Log
Reporting Service
```

---

## 10. Compliance and Safety Boundaries

The prototype must clearly state that it is:

- not affiliated with any real bank;
- not connected to real bank accounts;
- not connected to real crypto wallets;
- not a regulated financial product;
- not financial advice;
- not a custody provider;
- not a production system.

The prototype must not:

- process real transactions;
- request real bank credentials;
- request seed phrases;
- store real API keys;
- encourage investment decisions;
- imply guaranteed returns.

---

## 11. Success Criteria

Version 0.1 is successful if it demonstrates:

- a credible online banking UI;
- Digital Assets as an integrated banking module;
- clear BTC/ETH wallet overview;
- responsible buy/sell flow;
- controlled external withdrawal concept;
- compliance and audit trail visibility;
- tax reporting concept;
- professional product documentation;
- strong portfolio value.

---

## 12. Future Roadmap

### v0.2

- fully working React prototype;
- mock transaction state updates;
- improved UI polish;
- initial report export simulation;
- responsive layout.

### v0.3

- FastAPI backend;
- SQLite persistence;
- PDF report generation;
- audit event generation;
- compliance rule simulation.

### v0.4

- admin compliance dashboard;
- withdrawal case review;
- address whitelist concept;
- risk scoring explanation;
- demo video.

### v1.0 Concept Release

- polished UI;
- full concept paper PDF;
- architecture diagrams;
- screenshots;
- LinkedIn-ready presentation;
- portfolio page;
- private repository maintained as proof of work.

---

## 13. Open Questions

- Should the first prototype be frontend-only or include FastAPI from the beginning?
- Should the interface language be English, Finnish, or bilingual?
- Should the product support only BTC/ETH or include stablecoins in future scope?
- Should the bank custody model be described as direct custody or third-party regulated custody?
- Should the external withdrawal flow include a mandatory waiting period?
- Should the compliance view be user-facing only or also include an internal reviewer dashboard?

---

## 14. References

References will be added later during the public concept paper phase.

Potential reference areas:

- MiCA crypto asset service provider framework;
- FIN-FSA crypto asset service provider guidance;
- bank custody models;
- crypto tax reporting;
- Travel Rule;
- retail investor protection;
- digital asset custody standards.
