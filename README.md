# Aurora Digital Assets

**Bank-Integrated Digital Asset Banking Prototype**

Aurora Digital Assets is a backend-first local prototype for a bank-integrated digital assets module. It explores how a Finnish or Nordic banking environment could provide safer, more transparent, and more controlled access to digital assets inside an existing online banking experience.

The project combines product design, UX, compliance workflows, backend architecture, audit evidence, reporting concepts, and deterministic risk/review logic.

Aurora Digital Assets is not a real bank integration, not a crypto exchange, not a custody provider, not an investment tool, and not financial advice.

---

## Project Status

**Status:** Backend-first local prototype in active development

Current implementation includes:

- React + TypeScript + Vite frontend
- FastAPI backend
- SQLite local persistence
- Backend-first pages with local fallback
- Deterministic payment, withdrawal, and buy/sell evaluation flows
- Audit event persistence
- Review case persistence
- Compliance review dashboard
- Reporting API
- Evidence package preparation concept
- Internal demo admin seed/reset tools
- Global balance privacy mode

The project is still a prototype. It does not use real bank APIs, real customer data, real custody systems, real private keys, real payment execution, or real blockchain transactions.

---

## Project Vision

Retail users already access crypto assets through global exchanges, but many users do not fully understand custody, withdrawal risk, tax reporting, compliance obligations, or the difference between holding assets inside a custodial environment and transferring assets to an external wallet.

Aurora Digital Assets proposes a banking-first model:

- Digital assets visible inside online banking
- Clear custody boundaries
- Controlled buy/sell evaluation
- Controlled digital asset invoice payments
- Controlled external wallet withdrawals
- Human-reviewable risk cases
- Audit evidence by design
- Reporting and tax-summary concepts
- User protection through clear warnings and privacy controls

The goal is not to make digital assets feel speculative. The goal is to explore how a bank-style product could make digital asset access more controlled, explainable, and auditable.

---

## What This Project Is Not

Aurora Digital Assets is:

- Not connected to any real bank
- Not affiliated with Danske Bank, Nordea, OP, S-Pankki, Aktia, OmaSp, Handelsbanken, or any financial institution
- Not a crypto exchange
- Not a trading platform
- Not a trading bot
- Not a real custody system
- Not a payment processor
- Not an AML or sanctions screening provider
- Not financial, legal, tax, or investment advice

All data is fictional or simulated.

---

## Architecture Overview

### Frontend

The frontend is a React banking portal prototype.

Technologies and patterns:

- React
- TypeScript
- Vite
- React Router
- Reusable UI components
- Backend-first service layer
- Local fallback only when backend is unavailable
- Global balance privacy mode
- Conservative banking-style UI

Implemented frontend areas include:

- Dashboard
- Accounts
- Payments
- Buy / Sell
- Digital Assets
- Wallet
- Custody
- External Withdrawals
- Compliance Review
- Reports
- Internal Demo Admin

### Backend

The backend is a local FastAPI prototype.

Technologies and patterns:

- Python
- FastAPI
- Pydantic schemas
- Service-layer architecture
- SQLite local persistence
- Deterministic evaluation services
- Audit event service
- Review case service
- Reporting service
- Demo admin service

The backend is intentionally deterministic and auditable. Evaluation flows return explicit decisions, reasons, risk levels, user-facing messages, audit event types, and review case IDs when needed.

### Persistence

The prototype uses SQLite as a local persistence layer.

Current persisted records:

- `audit_events`
- `review_cases`

There is no production migration system yet. SQLite is used to make the local prototype realistic enough for backend-first workflows, audit evidence, reporting, and demo data control.

---

## Implemented Modules

### Dashboard

The dashboard provides a backend-first financial overview with account summary, digital asset value summary, custody status, risk/protection notices, and backend data loading with local fallback.

### Accounts

The accounts area provides simulated current account details, account balances, recent account activity, connected digital asset balances, and backend account data endpoints.

### Payments

The payments flow supports standard EUR transfer simulation and digital asset invoice payment evaluation. Digital asset payment evaluation is backend-driven and can return decision, risk level, reasons, case ID, estimate, fee data, and user-facing messages.

No real payment is executed.

### Buy / Sell

The buy/sell flow supports BTC and ETH simulated buy/sell evaluation. Backend services return market price, fee, spread, net amount, estimated asset amount, decision, risk level, and optional review case creation.

No real trade is executed. No exchange or custody provider is connected.

### Digital Assets

The Digital Assets module shows supported digital assets, wallet balances, activity records, risk notes, and backend-first data loading.

### Wallet

The wallet view shows simulated digital asset balances, estimated values, custody mode, wallet activity, and backend-first wallet data.

No private keys are created, stored, exposed, or used.

### Custody

The custody page explains internal custodial wallet concepts, private key boundaries, audit trail controls, external withdrawal review controls, and separation between digital assets and bank deposits.

No real custody service is implemented.

### External Withdrawals

The withdrawal flow supports asset/network selection, destination address confirmation, backend risk evaluation, review case creation when required, and audit event creation.

No real blockchain transaction is executed.

### Compliance Review

The compliance review dashboard supports backend review case queues, selected case details, evidence timelines filtered by case ID, human reviewer actions, reviewer decision recording, and audit evidence visibility.

This is a simulated operational layer. It does not perform real AML checks, sanctions screening, wallet screening, or regulatory reporting.

### Reports

The reports page consumes backend reporting APIs and shows report summaries, a tax summary concept, audit evidence timeline, review case evidence, and evidence package preparation concept.

No official tax filing or legal reporting is provided.

### Internal Demo Admin

The internal demo admin page supports loading demo status, seeding demo data, and resetting local demo audit/review data.

This is local development/demo tooling only. It is not a production admin system and does not include production authentication or authorization.

---
## Backend API Capabilities

The backend currently supports API areas for:

- Accounts data
- Account transactions
- Connected digital asset balances
- Supported digital assets
- Wallet balances
- Digital asset activity
- Custody status
- Digital asset payment evaluation
- External withdrawal evaluation
- Buy/sell evaluation
- Review cases
- Audit events
- Reports
- Tax summary concept
- Evidence package preparation
- Demo status/reset/seed

Representative endpoints include:

```text
GET  /api/accounts
GET  /api/accounts/{account_id}/transactions
GET  /api/accounts/connected-digital-assets

GET  /api/digital-assets/assets
GET  /api/digital-assets/wallet
GET  /api/digital-assets/activity
POST /api/digital-assets/buy-sell/evaluate

GET  /api/custody/status

POST /api/payments/digital-assets/evaluate
POST /api/withdrawals/evaluate

GET  /api/review-cases
POST /api/review-cases/{case_id}/decision

GET  /api/audit-events

GET  /api/reports
GET  /api/reports/tax-summary/2026
POST /api/reports/evidence-package

GET  /api/admin/demo/status
POST /api/admin/demo/reset
POST /api/admin/demo/seed
```

---

## Risk & Review Engine

The prototype includes deterministic evaluation flows for:

- Digital asset invoice payments
- External wallet withdrawals
- Digital asset buy/sell requests

Evaluation responses can include:

- `auto_approved`
- `pending_review`
- `auto_rejected`
- `blocked`
- `escalated`

Each evaluation can return decision, risk level, reasons, case requirement, case type, case ID, user message, audit event type, and estimate data when relevant.

Medium-risk or higher-risk actions can create review cases. These review cases appear in the Compliance Review dashboard and are included in reporting/evidence views.

---

## Audit Events and Review Cases

Aurora Digital Assets treats auditability as a core product requirement.

The backend persists:

- Evaluation audit events
- Pending review cases
- Reviewer decisions
- Evidence links between actions and cases

This allows the prototype to demonstrate how digital asset banking flows could be reviewed, explained, and reported without relying on opaque or speculative logic.

---

## Balance Privacy Mode

The frontend includes a global balance privacy mode.

Sensitive financial values are hidden by default and can be revealed using the Show / Hide balances control.

Implemented through:

- `PrivacyModeContext`
- `PrivacyAmount`
- TopBar privacy toggle

This is a user-protection feature for shared or public environments where a user may need to open online banking without exposing balances on screen.

---

## Reporting and Evidence

The reporting module demonstrates:

- Simulated annual digital asset summary
- Simulated tax summary values
- Audit evidence timeline
- Review case evidence
- Evidence package preparation concept

The evidence package action prepares a simulated backend response showing how many audit events and review cases would be included.

No real PDF, CSV, tax filing, bank statement, or regulatory report is generated unless explicitly implemented later.

This is not tax advice.

---

## Internal Demo Admin

The prototype includes an internal demo page:

```text
/admin-demo
```

It can:

- Load local demo status
- Seed representative review cases and audit events
- Reset local demo audit/review data

This helps keep demos repeatable and reduces the need to manually recreate cases through the UI.

The demo admin tool is not production administration. It has no production authentication, authorization, or operational security model.

---

## Repository Structure

```text
agents/                  Development guidance for coding assistants
backend/                 FastAPI backend, services, schemas, SQLite persistence
docs/                    Product, architecture, compliance notes, screenshots
frontend/                React/Vite banking portal frontend
mock-data/               Legacy/local mock data used as fallback or reference
prototypes/              Wireframes and demo scenarios
scripts/                 Development scripts
```

---
## Running Locally

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend runs by default at:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs by default at:

```text
http://localhost:5173
```

### Frontend Checks

```bash
cd frontend
npm run lint
npm run build
```

### Backend Compile Check

```bash
cd backend
python3 -m compileall app
```

---

## Useful Demo Flow

A useful local demo flow:

1. Start the backend.
2. Start the frontend.
3. Open `/admin-demo`.
4. Seed demo data.
5. Open `/compliance-review`.
6. Review seeded cases.
7. Open `/reports`.
8. Generate an evidence package.
9. Try `/payments` with a high-value digital asset payment.
10. Try `/withdrawals` with a first-time external address.
11. Try `/buy-sell` with a high-value BTC buy request.
12. Confirm that pending-review flows create review cases and audit events.

---

## Screenshots

Screenshots are stored in:

```text
docs/screenshots/
```

Suggested screenshot filenames:

```text
dashboard.png
accounts.png
payments.png
buy-sell.png
digital-assets.png
wallet.png
custody.png
withdrawals.png
compliance-review.png
reports.png
admin-demo.png
```

### Dashboard

![Dashboard](docs/screenshots/dashboard.png)

### Payments

![Payments](docs/screenshots/payments.png)

### Buy / Sell

![Buy Sell](docs/screenshots/buy-sell.png)

### External Withdrawals

![External Withdrawals](docs/screenshots/withdrawals.png)

### Compliance Review

![Compliance Review](docs/screenshots/compliance-review.png)

### Reports

![Reports](docs/screenshots/reports.png)

### Internal Demo Admin

![Internal Demo Admin](docs/screenshots/admin-demo.png)

---

## Current Limitations

Aurora Digital Assets currently does not include:

- Real bank integration
- Real customer accounts
- Real payment execution
- Real custody provider integration
- Real private keys
- Real blockchain transactions
- Real exchange integration
- Real market pricing
- Real AML screening
- Real sanctions screening
- Real wallet risk scoring
- Production authentication/authorization
- Production database migrations
- Official tax reporting
- Regulatory reporting
- Production admin tooling

The demo admin page is local prototype tooling only.

---

## Development Principles

The project follows these principles:

1. **Backend-first**  
   Business decisions, risk outcomes, estimates, audit events, and review cases should come from backend services where endpoints exist.

2. **Deterministic and auditable**  
   Decisions should be explainable, reproducible, and tied to persisted evidence.

3. **Compliance by design**  
   Review cases, audit trails, and reporting concepts are part of the product architecture, not an afterthought.

4. **User protection**  
   The UI should clearly communicate volatility, custody boundaries, withdrawal risk, review requirements, and reporting limitations.

5. **No fake production claims**  
   The prototype must never imply real execution, real custody, real payment processing, or real regulated financial service delivery.

6. **Minimal mock dependency**  
   Frontend mock data should only be used as local fallback or reference. Backend APIs should be the primary source of truth where implemented.

---

## Development Assistance Note

This repository may include guidance files for coding assistants used during development, such as Codex or similar tools.

These files are part of the development workflow only.

Aurora Digital Assets does not use Codex, AI agents, autonomous decision-making, or machine learning as part of the product runtime.

The product logic is designed as deterministic, auditable banking and compliance prototype logic using simulated data.

---

## Related Work

This concept connects with previous projects by the author:

- **WhaleScope Desktop** — crypto market intelligence and on-chain analytics desktop application delivered during internship work with Aalto University.
- **Market Surveillance AI** — deterministic market surveillance, compliance alerts, case management, evidence timelines, and audit-ready reporting.

---

## Author

**Claudio Valenzuela (CAUCO)**

---

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

---

## Disclaimer

Aurora Digital Assets is an independent concept prototype.

It is not affiliated with Danske Bank, Nordea, OP, S-Pankki, Aktia, OmaSp, Handelsbanken, or any other financial institution.

This project does not provide financial advice, investment recommendations, custody services, banking services, crypto exchange services, payment services, AML services, sanctions screening, tax advice, legal advice, or regulated financial services.

All data used in the prototype is fictional or simulated.

No real customer data, bank data, private keys, crypto assets, blockchain transactions, payment transactions, or regulated financial records are used.
