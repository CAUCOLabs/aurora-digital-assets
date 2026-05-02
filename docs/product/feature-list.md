# Feature List

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Status:** Initial feature scope  
**Version:** 0.1  

---

## 1. Banking Portal Features

### 1.1 Main Banking Dashboard

The prototype should include a fictional Aurora Bank dashboard with:

- account overview;
- current account balance;
- savings account balance;
- card or credit account example;
- notifications panel;
- Digital Assets entry point;
- conservative Nordic banking visual style.

### 1.2 Navigation

The top navigation should include:

- Home;
- Payments;
- Accounts;
- Cards and Currency;
- Loans;
- Investments;
- Digital Assets;
- Reports;
- Settings.

The **Digital Assets** navigation item should behave like a normal banking module, not a separate crypto exchange.

---

## 2. Digital Assets Features

### 2.1 Digital Assets Overview

The overview page should show:

- total digital assets value in EUR;
- BTC balance;
- ETH balance;
- latest BTC/EUR and ETH/EUR prices;
- recent digital asset transactions;
- custody status;
- risk profile;
- quick action buttons.

### 2.2 Buy Crypto Flow

The buy flow should support simulated purchases of:

- BTC;
- ETH.

The user should be able to select:

- funding account;
- crypto asset;
- EUR amount;
- estimated crypto amount.

The confirmation view should show:

- estimated price;
- estimated fee;
- estimated spread;
- volatility warning;
- custody information;
- final confirmation button.

### 2.3 Sell Crypto Flow

The sell flow should support simulated sales of:

- BTC;
- ETH.

The confirmation view should show:

- crypto amount;
- estimated EUR amount;
- estimated fee;
- tax reminder;
- final confirmation button.

---

## 3. Wallet Features

### 3.1 Internal Custodial Wallet

The internal wallet page should show:

- asset balances;
- EUR equivalent value;
- transaction history;
- custody status;
- supported assets;
- wallet activity.

### 3.2 External Wallet Withdrawal

The external wallet withdrawal flow should include:

- asset selection;
- destination address input;
- network selection;
- address confirmation;
- irreversible transfer warning;
- compliance review status;
- withdrawal delay notice;
- final confirmation.

Possible withdrawal states:

- draft;
- pending review;
- approved;
- rejected;
- completed.

---

## 4. Compliance and Risk Features

### 4.1 Compliance Status

The prototype should show:

- KYC verified status;
- risk profile;
- withdrawal limit;
- transaction monitoring status;
- audit trail enabled status.

### 4.2 Risk Warnings

Risk warnings should appear before:

- first activation of Digital Assets;
- crypto purchase confirmation;
- external wallet withdrawal;
- report generation disclaimer.

### 4.3 Audit Trail

The audit trail should record simulated events such as:

- Digital Assets module activated;
- BTC purchase requested;
- BTC purchase completed;
- external withdrawal requested;
- compliance check completed;
- report generated.

---

## 5. Reporting Features

### 5.1 Tax Report View

The reporting page should show:

- yearly summary;
- purchases;
- sales;
- transfers;
- estimated realized gain/loss concept;
- export PDF button;
- export CSV button.

### 5.2 Export Concept

The first prototype does not need to generate production-ready reports.

The UI should still include a simulated export flow for:

- PDF;
- CSV.

---

## 6. Mock Data Features

The prototype should use local mock data for:

- user profile;
- bank accounts;
- crypto wallet balances;
- market prices;
- transaction history;
- compliance events;
- audit log.

No real user data, bank API, crypto private key, or real transaction should be used.

---

## 7. Out of Scope for v0.1

The following are out of scope:

- real bank API integration;
- real crypto custody;
- real private key management;
- real blockchain transactions;
- real KYC provider integration;
- real trading execution;
- investment advice;
- mobile banking app;
- production authentication;
- regulatory approval workflow.

---

## 8. Future Features

Possible future features:

- address whitelist management;
- advanced tax report generation;
- PDF generation backend;
- admin compliance dashboard;
- manual case review;
- multi-user simulation;
- MiCA-aligned disclosure flow;
- Travel Rule concept module;
- proof-of-custody view;
- mobile responsive version;
- bank-core integration simulation.