# Custody Model

## Aurora Digital Assets
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)
**Status:** v0.2 planning document
**Version:** 0.1
**Date:** 2026-05-05

---

## 1. Purpose

This document defines the custody model concept for Aurora Digital Assets.

The goal is to explain how a bank-integrated digital assets module could make custody more understandable, visible, and safer for retail users.

Custody is one of the most important parts of any crypto product. Many retail users buy digital assets without fully understanding where the asset is held, who controls the keys, what happens during withdrawals, and what risks change when assets leave a platform.

Aurora Digital Assets treats custody transparency as a product feature.

---

## 2. Core Principle

The custody model should answer one simple user question:

> Where are my digital assets, and who controls what?

A banking interface should not simply show "you own BTC" or "you own ETH".

It should clearly explain:

- who holds the asset;
- whether the user controls private keys;
- whether the asset is held internally or through a regulated custody partner;
- whether the user can withdraw to a personal wallet;
- what happens when the user requests an external transfer;
- what protections apply inside the banking environment;
- what protections no longer apply after an external withdrawal.

---

## 3. Custody Modes

Aurora Digital Assets can be described using three possible custody modes.

### 3.1 Internal Custodial Wallet Concept

In this model, the user sees digital assets inside the banking interface, but does not manage private keys directly.

The bank or a regulated custody infrastructure manages the custody layer.

**User experience:**

- the user sees BTC/ETH balances;
- the user can buy and sell supported assets;
- the user can view transaction history;
- the user can request external withdrawals;
- the user does not see seed phrases;
- the user does not sign blockchain transactions manually.

**Benefits:**

- simpler experience for retail users;
- fewer private key mistakes;
- clearer reporting;
- easier integration with banking records;
- stronger fraud and withdrawal controls.

**Risks and limitations:**

- user depends on the custodian;
- user does not have direct self-custody;
- assets are not the same as bank deposits;
- custody rules must be clearly disclosed.

### 3.2 Regulated Custody Partner Model

A bank may choose not to custody crypto assets directly. Instead, the bank could integrate with a regulated third-party digital asset custodian.

In this model:

- the bank owns the customer interface;
- the custody partner holds or administers the digital assets;
- custody terms are disclosed to the customer;
- the bank integrates reporting, support, and user protection flows;
- withdrawals are still controlled through bank-side security and compliance checks.

**Benefits:**

- lower technical custody burden for the bank;
- access to specialized digital asset infrastructure;
- clearer separation of responsibilities;
- faster path to market.

**Risks and limitations:**

- third-party dependency;
- operational and contractual complexity;
- user needs clear disclosure about who holds the asset;
- incident response responsibilities must be defined.

### 3.3 Personal External Wallet

In this model, the user withdraws digital assets from the bank-integrated environment to a personal wallet.

The user may control the private keys directly or through another wallet provider.

Once assets leave the banking environment:

- blockchain transfers may be irreversible;
- the bank may no longer be able to recover funds;
- address mistakes may lead to permanent loss;
- the user becomes responsible for wallet security;
- tax and reporting implications may still remain.

This is why Aurora Digital Assets treats external wallet withdrawals as high-risk actions.

---

## 4. Custody Transparency in the UI

The user interface should make custody visible in normal language.

Instead of using vague phrases, the product should explain custody clearly.

**Examples of good customer-facing language:**

- "Internal custodial wallet concept"
- "Digital assets are separate from bank deposits"
- "The user does not manage private keys in this model"
- "External transfers may leave the bank protection environment"
- "Blockchain transfers are irreversible"
- "External withdrawals require security review"

**Avoid vague or misleading language:**

- "Your assets are fully safe"
- "Bank-protected crypto"
- "Risk-free custody"
- "Guaranteed recovery"
- "Instant irreversible transfer with no warning"

The goal is clarity, not marketing.

---

## 5. What the User Should See

A user should be able to answer these questions directly from the interface:

### 5.1 Before Buying

- What asset am I buying?
- What is the estimated price?
- What fee and spread apply?
- Where will the asset be held after purchase?
- Is this a bank deposit or a digital asset?
- Can the value go down?

### 5.2 While Holding

- What is my current balance?
- What is the estimated EUR value?
- What custody model applies?
- Do I control the private keys?
- Can I withdraw externally?
- Are reporting records available?

### 5.3 Before External Withdrawal

- Which network am I using?
- What address am I sending to?
- Is the transfer reversible?
- Does the bank still protect the asset after withdrawal?
- Will the transfer require review?
- What audit record is created?

---

## 6. External Withdrawal Risk Boundary

The most important custody transition happens when assets move from the internal custodial wallet to an external wallet.

This moment should be treated as a clear risk boundary.

**Inside the banking environment:**

- the user benefits from banking authentication;
- transaction records are visible;
- reporting is organized;
- suspicious activity can be reviewed;
- withdrawal attempts can be delayed or blocked;
- support processes may exist.

**Outside the banking environment:**

- the user is responsible for wallet security;
- the bank may not be able to reverse mistakes;
- private key loss may mean asset loss;
- scams and wrong-address transfers become harder to resolve;
- reporting may depend on user-provided records.

The UI should communicate this transition clearly.

---

## 7. Suggested Withdrawal Controls

Aurora Digital Assets should treat external withdrawal as a controlled process.

**Possible controls:**

- strong authentication before withdrawal;
- address confirmation;
- address format check;
- network compatibility warning;
- first-time address review;
- optional address whitelist;
- withdrawal delay for new addresses;
- risk level indicator;
- audit event generation;
- manual review for unusual transfers.

The goal is not to block users unnecessarily.

The goal is to reduce avoidable losses.

---

## 8. Audit Trail and Evidence

Every custody-related action should create a clear audit event.

**Examples:**

- digital asset purchase completed;
- asset credited to internal wallet;
- custody status shown to user;
- external withdrawal form opened;
- destination address submitted;
- security check completed;
- withdrawal submitted for review;
- withdrawal approved or rejected;
- report generated.

**Each audit event may include:**

- timestamp;
- action type;
- asset;
- amount;
- status;
- risk level;
- review result;
- user-facing explanation.

This makes the system more transparent and defensible.

---

## 9. Banking Product Positioning

Aurora Digital Assets should not compete with global exchanges on high-frequency trading, leverage, or speculative features.

The custody model should support a different product position:

- limited asset scope;
- spot-only access;
- transparent fees;
- controlled withdrawals;
- custody clarity;
- tax reporting;
- safer onboarding;
- banking-grade support;
- user protection.

The value is not only execution speed.

The value is trust, clarity, reporting, custody visibility, and risk control.

---

## 10. Open Questions

The custody model still requires further research.

**Important questions:**

- Should the bank custody assets directly or use a regulated custody partner?
- How should assets be segregated from the bank's own assets?
- What disclosures are required under applicable regulation?
- What happens if the custody partner fails?
- What insurance, if any, applies?
- What assets should be supported first?
- Should external withdrawals be enabled by default?
- Should new addresses require a cooling-off period?
- How should self-custody risks be explained to non-technical users?
- How should custody records connect to tax reporting?

---

## 11. Prototype Implications for v0.2

For v0.2, Aurora Digital Assets should add a dedicated custody page.

**Suggested route:**

```
/custody
```

**The page should include:**

- custody model summary;
- internal custodial wallet explanation;
- external wallet risk boundary;
- custody status checklist;
- "who controls what?" explanation;
- link to withdrawals;
- link to reports;
- clear disclaimer.

**Suggested UI sections:**

1. Custody Overview
2. Internal Custodial Wallet
3. External Wallet Transfer Boundary
4. User Responsibilities
5. Audit Trail and Reporting
6. Disclaimer

---

## 12. Disclaimer

This document describes a product concept only.

Aurora Digital Assets is not a bank, not a custody provider, not a crypto exchange, and not a regulated financial service.

The custody model described here is fictional and intended for product design, UX, compliance discussion, and portfolio demonstration.

No real assets, private keys, bank data, customer data, or blockchain transactions are used.
