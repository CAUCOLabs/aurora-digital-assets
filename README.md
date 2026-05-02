# Aurora Digital Assets

**Bank-Integrated Crypto Wallet Framework**

Aurora Digital Assets is a concept prototype for a bank-integrated digital assets module. It explores how Finnish and Nordic banks could provide safer, regulated, and user-protective access to crypto assets inside an existing online banking environment.

This project is not a standalone exchange, not a trading platform, and not a financial advice tool. It is a product, UX, compliance, and architecture prototype focused on responsible access to digital assets through a banking interface.

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

## What This Project Is Not

- Not a real bank integration
- Not connected to any real bank
- Not affiliated with Danske Bank, Nordea, OP, S-Pankki, or any financial institution
- Not a crypto exchange
- Not a trading bot
- Not financial advice
- Not a production custody system

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

## Repository Structure

```text
agents/                  Codex and development agent instructions
docs/                    Product, architecture, compliance and screenshots
frontend/                Banking portal UI prototype
backend/                 Simulated API and business logic
mock-data/               Local mock data for the prototype
prototypes/              Wireframes and demo scenarios
scripts/                 Development scripts
