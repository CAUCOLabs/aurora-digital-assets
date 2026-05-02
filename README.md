# Aurora Digital Assets

**Bank-Integrated Crypto Wallet Framework**

Aurora Digital Assets is a concept prototype for a bank-integrated digital assets module. It explores how Finnish and Nordic banks could provide safer, regulated, and user-protective access to crypto assets inside an existing online banking environment.

This project is not a standalone exchange, not a trading platform, and not a financial advice tool. It is a product, UX, compliance, and architecture prototype focused on responsible access to digital assets through a banking interface.

---

## Project Vision

Retail users already access crypto assets through global exchanges, but many users do not fully understand custody, withdrawal risk, tax reporting, compliance, or the difference between holding assets on an exchange and using a personal wallet.

Aurora Digital Assets proposes a safer banking-first model:

- Bank account integration
- Internal custodial crypto wallet
- BTC/ETH buy and sell flow
- External wallet withdrawal controls
- Risk education and warnings
- Compliance checks
- Audit trail
- Tax reporting
- PDF/CSV report exports
- Human-reviewable surveillance and case concepts

---

## Design Philosophy

The project follows five principles:

1. **Banking-first UX**  
   Digital assets should feel like a regulated banking module, not a casino or speculative trading app.

2. **User protection**  
   The interface should clearly explain volatility, custody, withdrawal risk, and tax implications.

3. **Compliance by design**  
   KYC, AML, transaction monitoring, audit trails, and review workflows are part of the product architecture.

4. **Transparency**  
   Fees, spreads, custody status, transaction status, and risk warnings should be visible to the user.

5. **Controlled external withdrawal**  
   Moving assets to an external wallet should include address checks, risk warnings, delays, and compliance review when needed.

---

## What This Project Is Not

- Not a real bank integration
- Not connected to any real bank
- Not affiliated with Danske Bank, Nordea, OP, S-Pankki, or any financial institution
- Not a crypto exchange
- Not a trading bot
- Not financial advice
- Not a production custody system

---

## Prototype Scope

The first prototype will simulate:

- Online banking dashboard
- Current account and savings account overview
- Digital Assets module
- Internal BTC/ETH wallet
- Simulated buy/sell flow
- Simulated external wallet withdrawal
- Compliance status and audit trail
- Tax report view
- Mock market prices
- Mock transaction history

---

## Suggested Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Recharts or Chart.js

### Backend

- Python
- FastAPI
- SQLite
- Pydantic
- PDF report generation

### Data

- Local mock JSON data
- Simulated account balances
- Simulated crypto wallet balances
- Simulated compliance events
- Simulated market prices

---

## Repository Structure

```text
agents/                  Codex and development agent instructions
docs/                    Product, architecture, compliance and screenshots
frontend/                Banking portal UI prototype
backend/                 Simulated API and business logic
mock-data/               Local mock data for the prototype
prototypes/              Wireframes and demo scenarios
scripts/                 Development scripts
```

---

## Planned Modules

### Banking Portal

A simulated online banking interface with:

- Account overview
- Payments navigation
- Investments navigation
- Cards and currency navigation
- Digital Assets module entry point

### Digital Assets

A bank-integrated crypto assets module with:

- BTC and ETH balances
- EUR valuation
- Buy and sell flow
- Custody status
- Transaction history
- Risk warnings
- Educational notices

### External Wallet Transfers

A controlled withdrawal flow with:

- External wallet address input
- Network selection
- Address confirmation
- Risk warning
- Compliance status
- Security delay concept
- Audit log entry

### Compliance & Audit

A simulated compliance layer with:

- KYC status
- Transaction monitoring
- Risk flags
- Human-reviewable cases
- Audit trail
- Exportable evidence

### Reporting

A reporting layer with:

- Tax summary
- Transaction history
- PDF report concept
- CSV export concept
- Annual reporting view

---

## UI Direction

The visual direction is inspired by traditional Nordic online banking portals:

- Dark blue top navigation
- Light grey-blue background
- White content cards
- Table-based account views
- Simple typography
- Conservative buttons
- Low visual noise
- Clear risk and compliance messaging

The UI should not look like a crypto exchange. It should look like a serious banking module.

---

## Development Principles

- Use fictional branding only.
- Use mock data only.
- Do not store real financial data.
- Do not use real bank APIs.
- Do not use real crypto private keys.
- Do not connect to real custody providers.
- Keep the architecture modular and easy to understand.
- Keep compliance and audit concepts visible in the product.
- Prioritize clarity, safety, and user protection over speculative features.

---

## Status

Project status: **Initial concept and repository setup**

Current phase:

- Repository structure
- Product documentation
- Architecture planning
- UI direction
- Mock data design

---

## Author

**Claudio Valenzuela (CAUCO)**

This concept connects with previous projects by the author:

- **WhaleScope Desktop** — crypto market intelligence and on-chain analytics desktop application delivered during internship work with Aalto University.
- **Market Surveillance AI** — deterministic market surveillance, compliance alerts, case management, evidence timelines, and audit-ready reporting.

---

## Disclaimer

Aurora Digital Assets is an independent concept prototype.

It is not affiliated with Danske Bank, Nordea, OP, S-Pankki, Aktia, OmaSp, Handelsbanken, or any other financial institution.

This project does not provide financial advice, investment recommendations, custody services, banking services, crypto exchange services, or regulated financial services.

All data used in the prototype is fictional or simulated.