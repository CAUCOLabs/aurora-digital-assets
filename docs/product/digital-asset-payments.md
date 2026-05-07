# Digital Asset Payments

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)  
**Status:** v0.2 planning document  
**Version:** 0.1  
**Date:** 2026-05-06  

---

## 1. Purpose

This document defines the digital asset payments concept for Aurora Digital Assets.

The goal is to explore how a bank-integrated digital assets module could allow a customer to pay an invoice using supported digital assets, while preserving the structure, safety, and auditability of a normal online banking payment.

The concept does not propose open crypto payments to arbitrary wallet addresses.

Instead, digital asset payments should be available only for verified business recipients that:

- hold a business account inside the same banking environment;
- have enabled digital asset payment acceptance;
- can be identified by the bank;
- can receive settlement through a controlled banking flow;
- can generate invoice, reference, and reporting records.

This keeps the payment experience closer to banking and reduces the risks associated with unrestricted external wallet transfers.

---

## 2. Core Principle

The core principle is:

> A digital asset payment inside online banking should behave like a normal invoice payment, with additional digital asset fields only when the recipient supports them.

The user should still enter or confirm normal invoice data:

- recipient;
- recipient account or payment identifier;
- invoice number;
- reference number;
- due date;
- amount;
- currency;
- payer account;
- payment message or invoice note.

Only after the normal payment data is valid should the digital asset payment option become available.

---

## 3. Payment Boundary

Aurora Digital Assets should clearly separate two different actions.

### 3.1 External Wallet Withdrawal

An external wallet withdrawal means sending digital assets to:

- a personal wallet;
- a hardware wallet;
- a self-custody wallet;
- another crypto service;
- an exchange deposit address.

This is a higher-risk action because funds leave the bank-integrated environment.

External wallet withdrawals should require stronger controls such as address review, risk warnings, delays, and audit trail events.

### 3.2 Digital Asset Payment

A digital asset payment means paying a verified business recipient inside the banking environment.

The recipient:

- has a bank business account;
- has enabled digital asset payment acceptance;
- can be validated by the bank;
- can receive settlement according to bank-defined rules;
- can be connected to invoice and reporting records.

This is not the same as sending crypto to any external wallet address.

---

## 4. Recipient Eligibility

Digital asset payments should be restricted to eligible recipients.

A recipient should be eligible only if:

- the recipient is a verified business customer of the bank;
- the recipient has an active business account;
- the recipient has enabled digital asset payment acceptance;
- the recipient has defined accepted assets;
- the recipient has defined settlement preferences;
- the recipient has passed required business onboarding checks;
- the payment can be linked to invoice or reference data.

The UI should make this clear:

> Digital asset payments are available only for verified business recipients that hold an Aurora Bank business account and have enabled digital asset payment acceptance.

If a recipient is not eligible, the payment page should show only standard bank transfer options.

---

## 5. Standard Invoice Payment Fields

A digital asset payment should preserve the normal structure of a Finnish/Nordic invoice payment.

Minimum standard fields:

- recipient name;
- recipient business identifier, if available;
- recipient bank account or internal recipient identifier;
- IBAN, when applicable;
- BIC, when applicable;
- invoice number;
- reference number;
- due date;
- invoice amount;
- invoice currency;
- payer account;
- optional message;
- payment confirmation.

These fields are important because they support:

- payment matching;
- invoice reconciliation;
- accounting;
- reporting;
- audit trail;
- customer support;
- tax and business records.

---

## 6. Digital Asset Payment Fields

If the recipient supports digital asset payments, the payment form may show additional fields.

Suggested digital asset fields:

- payment method;
- selected digital asset;
- network or settlement rail;
- conversion rate;
- estimated digital asset amount;
- service fee;
- network or settlement fee;
- recipient settlement preference;
- payment protection status;
- audit trail status.

Example payment method options:

```text
Payment method
○ Bank transfer in EUR
○ Digital asset payment
```

Example supported assets:

```text
EUR digital asset concept
USDC
USDT
BTC
ETH
```

For the first version, the product should separate payment-oriented assets from investment-oriented assets.

Payment-oriented assets:

- EUR digital asset concept;
- USDC;
- USDT.

Investment-oriented assets:

- BTC;
- ETH.

BTC and ETH may still be supported, but they should not be presented as the preferred payment assets due to volatility.

---

## 7. Settlement Models

A verified business recipient could define how it wants to receive value.

### 7.1 Recipient Receives EUR

The customer pays using a digital asset, but the business receives EUR.

This model may be more practical for most businesses.

Flow:

```text
Customer selects digital asset
        |
Bank estimates conversion
        |
Customer confirms payment
        |
Digital asset value is converted
        |
Business receives EUR
        |
Invoice reference is preserved
```

Benefits:

- easier accounting for the business;
- less volatility exposure for the recipient;
- closer to normal invoice payment;
- simpler tax and reconciliation process.

### 7.2 Recipient Receives Digital Asset

The business receives the selected digital asset.

Flow:

```text
Customer selects digital asset
        |
Bank checks recipient acceptance settings
        |
Customer confirms payment
        |
Digital asset settlement is recorded
        |
Business receives digital asset balance
        |
Invoice reference is preserved
```

Benefits:

- useful for businesses that intentionally hold digital assets;
- supports digital asset treasury use cases;
- may support future business-to-business digital asset flows.

Limitations:

- more volatility risk;
- more accounting complexity;
- stronger reporting requirements;
- additional custody requirements for the business.

---

## 8. Payment Flow

A customer-facing digital asset payment flow could work as follows:

```text
Customer opens Payments
        |
Selects New payment
        |
Enters recipient or selects saved recipient
        |
System checks recipient eligibility
        |
Customer enters invoice amount, due date, and reference number
        |
Payment method options are shown
        |
Customer selects Digital asset payment
        |
Customer selects asset
        |
System shows conversion, fee, and settlement estimate
        |
Risk and payment protection notice is shown
        |
Customer confirms
        |
Payment record and audit event are created
        |
Recipient receives settlement according to its settings
```

The flow should feel like a normal bank payment with additional digital asset transparency.

---

## 9. User Interface Requirements

The Payments page should include a digital asset payment section only when relevant.

Suggested UI sections:

1. Payment Overview
2. New Payment
3. Invoice Details
4. Recipient Eligibility
5. Digital Asset Payment Option
6. Payment Estimate
7. Protection and Audit Trail
8. Confirmation

### 9.1 Invoice Details Section

Fields:

- recipient;
- invoice number;
- reference number;
- due date;
- amount;
- currency;
- payer account.

### 9.2 Recipient Eligibility Section

Show whether:

- recipient is a verified business recipient;
- recipient has an Aurora Bank business account;
- recipient accepts digital asset payments;
- recipient settlement preference is available.

### 9.3 Payment Estimate Section

Show:

- invoice amount in EUR;
- selected digital asset;
- estimated digital asset amount;
- conversion rate;
- service fee;
- settlement fee;
- recipient receives EUR or selected digital asset;
- final confirmation amount.

### 9.4 Protection Section

Show:

- payment recipient is verified;
- invoice reference is preserved;
- transaction monitoring is enabled;
- audit trail is enabled;
- payment record will appear in reports.

---

## 10. Example Mock Payment

Example data for the prototype:

```text
Recipient: Aurora Telecom Oyj
Business account: Active
Digital asset payments: Enabled
Invoice number: 90495185862
Reference number: 80 60206 95479
Due date: 19.05.2026
Amount: 120,45 EUR
Payer account: Aurora Current Account
Payment method: Digital asset payment
Selected asset: EUR digital asset concept
Recipient settlement: Receives EUR
Status: Draft
```

Alternative digital asset estimate:

```text
Invoice amount: 120,45 EUR
Selected asset: USDC
Estimated asset amount: 129.80 USDC
Service fee: 1,20 EUR
Settlement fee: 0,30 EUR
Recipient receives: 120,45 EUR
```

All values should be clearly marked as simulated.

---

## 11. Payment Protection Rules

Recommended protection rules:

- only verified business recipients can receive digital asset payments;
- recipient must have a bank business account;
- recipient must explicitly enable digital asset payment acceptance;
- payment reference must be preserved;
- payment amount must be shown in EUR and selected asset;
- fees must be visible before confirmation;
- high-value payments may require additional confirmation;
- unusual payments may trigger review;
- audit trail must be created;
- report records must be updated.

These rules make the feature feel like banking rather than unrestricted crypto transfer.

---

## 12. Audit Trail and Reporting

Every digital asset payment should create audit and reporting records.

Example audit events:

- payment form opened;
- recipient selected;
- recipient eligibility checked;
- invoice details entered;
- digital asset payment method selected;
- estimate generated;
- payment confirmed;
- payment completed;
- report record created.

Each record may include:

- timestamp;
- payer account;
- recipient;
- invoice number;
- reference number;
- amount;
- selected asset;
- conversion rate;
- fees;
- settlement model;
- status;
- user-facing explanation.

Reporting should support:

- user payment history;
- business recipient reconciliation;
- tax reporting;
- exportable PDF/CSV records;
- audit evidence package.

---

## 13. Product Positioning

Digital asset payments should be positioned as a controlled banking payment method.

It should not be marketed as:

- “pay anyone with crypto”;
- “instant crypto payments everywhere”;
- “risk-free digital currency payments”;
- “anonymous crypto payments”;
- “bypass banking rails”.

Preferred positioning:

> Pay eligible business recipients with supported digital assets inside a controlled banking environment.

This keeps the product aligned with trust, compliance, and user protection.

---

## 14. Prototype Implications for v0.2

For v0.2, Aurora Digital Assets should replace the current Payments placeholder with a real Payments page.

Suggested route:

```text
/payments
```

Suggested page:

```text
frontend/src/pages/PaymentsPage.tsx
```

The page should include:

- standard payment overview;
- invoice payment form;
- mock verified business recipient;
- digital asset payment option;
- supported payment assets;
- conversion estimate;
- recipient eligibility status;
- payment protection checklist;
- audit trail preview;
- disclaimer.

Suggested UI sections:

1. New Payment
2. Invoice Details
3. Digital Asset Payment
4. Verified Business Recipient
5. Payment Estimate
6. Payment Protection
7. Payment Audit Trail
8. Disclaimer

---

## 15. Open Questions

Important questions for future research:

- Which assets should be allowed for payments?
- Should BTC and ETH be available for invoice payments or only wallet/investment use?
- Should stablecoins be allowed before a regulated EUR digital asset exists?
- Should the recipient always receive EUR by default?
- What conversion provider would be used?
- What fees would apply?
- How should refunds work?
- How should partial payments work?
- How should payment disputes be handled?
- What happens if conversion fails?
- What reporting is needed for business recipients?
- What limits should apply to digital asset payments?
- Should this feature be available to retail users, business users, or both?
- How should the bank handle scams, invoice fraud, and account takeover risk?

---

## 16. Disclaimer

This document describes a product concept only.

Aurora Digital Assets is not a bank, not a payment institution, not a custody provider, not a crypto exchange, and not a regulated financial service.

The digital asset payments model described here is fictional and intended for product design, UX, compliance discussion, and portfolio demonstration.

No real payments, assets, bank data, customer data, private keys, financial credentials, or blockchain transactions are used.