# Risk & Review Engine

## Aurora Digital Assets  
### Bank-Integrated Crypto Wallet Framework

**Author:** Claudio Valenzuela (CAUCO)  
**Status:** v0.2 architecture planning document  
**Version:** 0.1  
**Date:** 2026-05-08  

---

## 1. Purpose

This document defines the **Risk & Review Engine** concept for Aurora Digital Assets.

The Risk & Review Engine is the backend decision layer that evaluates sensitive digital asset actions before they are completed.

Its purpose is to decide whether an action should be:

- approved automatically;
- sent to human review;
- rejected automatically;
- blocked or escalated.

The engine is designed to be deterministic, explainable, auditable, rule-based, and suitable for banking and compliance workflows.

The goal is not to build a black-box AI decision-maker. The goal is to build a transparent security and compliance layer that supports automated checks while preserving human review for sensitive or ambiguous cases.

---

## 2. Core Idea

The core idea is:

```text
User action
    |
Automated security, compliance and risk checks
    |
Risk decision
    |
Auto approve / Pending human review / Auto reject / Block or escalate
```

This model allows normal low-risk activity to proceed efficiently while ensuring that higher-risk activity is reviewed before completion.

---

## 3. Why This Engine Is Needed

Digital asset banking introduces risks that normal banking flows do not always have.

Examples:

- blockchain transfers can be irreversible;
- wrong wallet addresses can cause permanent loss;
- assets can leave the bank protection environment;
- external wallets may have risk signals;
- stablecoin payments may require monitoring;
- custody and reporting create operational responsibility;
- suspicious activity may require human review.

This directly addresses the operational challenge of bank-integrated digital assets:

> The issue is not only feature design. The issue is managing custody, AML, withdrawals, reporting, fraud risk, audit evidence, and operational cost.

The Risk & Review Engine is the layer that makes this operationally manageable.

---

## 4. Scope

The Risk & Review Engine may evaluate these actions:

### 4.1 Digital Asset Buy / Sell

Examples:

- BTC purchase;
- ETH sale;
- large buy/sell request;
- unusual repeated purchase pattern.

### 4.2 Digital Asset Payments

Examples:

- invoice payment using EUR digital asset concept;
- USDC payment to a verified business recipient;
- payment with invalid reference number;
- payment to a recipient not eligible for digital asset payments.

### 4.3 External Withdrawals

Examples:

- BTC withdrawal to personal wallet;
- ETH withdrawal to external crypto service;
- USDC withdrawal to new external address;
- withdrawal using incompatible network;
- withdrawal to a risky destination.

### 4.4 Custody-Related Changes

Examples:

- enabling external withdrawals;
- adding a trusted address;
- changing withdrawal limits;
- switching custody preferences.

### 4.5 Security-Sensitive Events

Examples:

- login from new device;
- recent phone/email change;
- strong authentication failure;
- account takeover signal;
- repeated failed withdrawal attempts.

---

## 5. Decision Outcomes

The engine should return one of the following decisions.

### 5.1 Auto Approved

The request passes automated checks and does not require human review.

Example:

```text
Known customer
Known device
Low amount
Known recipient
Valid reference number
No unusual activity
```

Result:

```text
decision: auto_approved
risk_level: low
```

### 5.2 Pending Human Review

The request is not blocked, but it requires review by a bank analyst, risk team, or compliance team before completion.

Example:

```text
New external wallet address
First external withdrawal
Medium amount
No hard block signal
```

Result:

```text
decision: pending_review
risk_level: medium
case_created: true
```

### 5.3 Auto Rejected

The request fails a hard validation rule.

Example:

```text
Invalid address format
Network incompatible with asset
Amount is zero or negative
Missing required confirmation
```

Result:

```text
decision: auto_rejected
risk_level: invalid
```

### 5.4 Blocked

The request is blocked because it violates a strong policy rule.

Example:

```text
Account blocked
Destination is prohibited
High-risk wallet signal
Strong authentication missing
Withdrawal above absolute limit
```

Result:

```text
decision: blocked
risk_level: high
```

### 5.5 Escalated

The request or case requires deeper investigation.

Example:

```text
Potential account takeover
Suspicious pattern
High-risk wallet cluster
Repeated unusual behavior
Compliance escalation needed
```

Result:

```text
decision: escalated
risk_level: critical
case_created: true
```

---

## 6. Risk Levels

Suggested risk levels:

```text
low
medium
high
critical
invalid
```

- **Low risk:** normal activity that matches user history and product rules. Usually auto approved.
- **Medium risk:** activity that may be legitimate but requires additional review.
- **High risk:** activity with strong risk indicators. Usually blocked, reviewed, or escalated.
- **Critical risk:** activity that may indicate fraud, sanctions risk, account takeover, or serious compliance concern.
- **Invalid:** request is structurally invalid and should be auto rejected.

---

## 7. Inputs

The engine should evaluate multiple input categories.

### 7.1 Customer Inputs

```text
customer_id
customer_type
customer_risk_profile
account_status
digital_assets_enabled
external_withdrawals_enabled
```

### 7.2 Session and Security Inputs

```text
session_id
device_known
strong_authentication_completed
recent_login_change
recent_phone_or_email_change
failed_auth_attempts
```

### 7.3 Transaction Inputs

```text
action_type
asset
amount
currency
source_account
recipient
destination_address
network
reference_number
payment_due_date
```

### 7.4 Recipient Inputs

For digital asset payments:

```text
recipient_id
recipient_type
recipient_has_bank_account
recipient_accepts_digital_asset_payments
recipient_accepted_assets
recipient_settlement_preference
```

### 7.5 Wallet / Destination Inputs

For withdrawals:

```text
destination_address
address_format_valid
address_known_to_customer
address_whitelisted
wallet_type
wallet_risk_signal
network_compatible
first_time_address
```

### 7.6 Historical Behavior Inputs

```text
average_transaction_amount
recent_buy_sell_activity
recent_withdrawals
recent_payment_activity
previous_review_cases
previous_rejections
```

### 7.7 Policy Inputs

```text
daily_limit
single_transaction_limit
asset_allowed
network_allowed
withdrawal_allowed
payment_allowed
cooling_period_required
```

---

## 8. Rule Categories

The engine should use deterministic rule categories.

### 8.1 Validation Rules

These check whether the request is structurally valid.

Examples:

- amount must be greater than zero;
- asset must be supported;
- network must match asset;
- address format must be valid;
- payment reference must be present when required;
- recipient must exist.

Failure usually produces:

```text
auto_rejected
```

### 8.2 Eligibility Rules

These check whether the customer, recipient, or asset is eligible.

Examples:

- digital assets must be enabled for customer;
- external withdrawals must be enabled;
- recipient must accept digital asset payments;
- asset must be allowed for payment or withdrawal;
- EUR digital asset concept may be internal-settlement only.

Failure may produce:

```text
auto_rejected
blocked
```

### 8.3 Security Rules

These check authentication and account safety.

Examples:

- strong authentication required;
- device must be trusted or reviewed;
- recent phone/email changes increase risk;
- failed authentication attempts increase risk.

Failure may produce:

```text
pending_review
blocked
```

### 8.4 Risk Scoring Rules

These assign risk points.

Examples:

- new external address;
- first withdrawal;
- unusual amount;
- high-frequency attempts;
- new device;
- wallet risk signal;
- amount close to limit;
- unusual time of activity.

These contribute to:

```text
low
medium
high
critical
```

### 8.5 Compliance Rules

These check AML, sanctions, wallet risk, and monitoring signals.

Examples:

- wallet risk signal;
- unusual transfer pattern;
- suspicious activity indicator;
- sanctions screening concept;
- Travel Rule readiness concept.

Failure may produce:

```text
pending_review
blocked
escalated
```

### 8.6 Product Constraint Rules

These enforce product design constraints.

Examples:

- no leverage;
- no derivatives;
- no unsupported assets;
- no digital asset payments to arbitrary wallets;
- digital asset payments only to verified business recipients;
- external withdrawals require address review.

Failure may produce:

```text
auto_rejected
blocked
```

---

## 9. Suggested Initial Rules

### 9.1 Universal Rules

```text
IF strong_authentication_completed == false
THEN decision = blocked
REASON = strong_authentication_required
```

```text
IF amount <= 0
THEN decision = auto_rejected
REASON = invalid_amount
```

```text
IF asset_allowed == false
THEN decision = auto_rejected
REASON = unsupported_asset
```

### 9.2 Buy / Sell Rules

```text
IF action_type == buy_sell
AND amount <= daily_limit
AND device_known == true
AND customer_risk_profile == normal
THEN decision = auto_approved
RISK = low
```

```text
IF action_type == buy_sell
AND amount > daily_limit
THEN decision = pending_review
RISK = medium
REASON = amount_above_daily_limit
```

### 9.3 Digital Asset Payment Rules

```text
IF action_type == digital_asset_payment
AND recipient_has_bank_account == false
THEN decision = auto_rejected
REASON = recipient_not_inside_bank
```

```text
IF action_type == digital_asset_payment
AND recipient_accepts_digital_asset_payments == false
THEN decision = auto_rejected
REASON = recipient_not_enabled_for_digital_asset_payments
```

```text
IF action_type == digital_asset_payment
AND recipient_has_bank_account == true
AND recipient_accepts_digital_asset_payments == true
AND amount <= payment_limit
AND reference_number IS NOT EMPTY
THEN decision = auto_approved
RISK = low
```

```text
IF action_type == digital_asset_payment
AND amount > payment_limit
THEN decision = pending_review
RISK = medium
REASON = high_value_digital_asset_payment
```

### 9.4 External Withdrawal Rules

```text
IF action_type == external_withdrawal
AND asset == EURD
THEN decision = auto_rejected
REASON = external_withdrawal_not_available_for_internal_settlement_asset
```

```text
IF action_type == external_withdrawal
AND address_format_valid == false
THEN decision = auto_rejected
REASON = invalid_destination_address
```

```text
IF action_type == external_withdrawal
AND network_compatible == false
THEN decision = auto_rejected
REASON = incompatible_network
```

```text
IF action_type == external_withdrawal
AND first_time_address == true
THEN decision = pending_review
RISK = medium
REASON = first_time_external_address
```

```text
IF action_type == external_withdrawal
AND wallet_risk_signal == high
THEN decision = blocked
RISK = high
REASON = high_risk_wallet_signal
```

```text
IF action_type == external_withdrawal
AND address_whitelisted == true
AND amount <= withdrawal_limit
AND device_known == true
THEN decision = auto_approved
RISK = low
```

---

## 10. Decision Object

The engine should return a structured decision object.

Example:

```json
{
  "decision": "pending_review",
  "risk_level": "medium",
  "reasons": [
    "external_withdrawal",
    "first_time_external_address"
  ],
  "case_required": true,
  "case_type": "external_withdrawal_review",
  "user_message": "Your external transfer request is pending security review.",
  "audit_event_type": "withdrawal_pending_review"
}
```

Possible fields:

```text
decision
risk_level
reasons
case_required
case_type
user_message
audit_event_type
blocked
requires_step_up_auth
cooling_period_required
```

---

## 11. Human Review Workflow

Human review is required when the engine cannot safely approve or reject automatically.

### 11.1 Case Creation

When a request requires human review, the system creates a review case.

Example:

```text
CASE-DA-2026-001
Type: External withdrawal review
Status: Pending review
Risk: Medium
```

### 11.2 Case Evidence

A case should include:

- customer;
- action type;
- asset;
- amount;
- network;
- destination;
- risk reasons;
- session/device context;
- audit timeline;
- previous activity;
- system recommendation.

### 11.3 Reviewer Decisions

A reviewer may decide:

```text
Approve
Reject
Request more information
Delay / cooling period
Escalate
```

### 11.4 Reviewer Notes

Reviewer notes should be stored as part of the evidence trail.

Example:

```text
Reviewer note:
First external withdrawal to a new address. Customer authenticated successfully.
Approved after standard review.
```

### 11.5 Case Closure

After decision:

- audit event is created;
- customer-facing status is updated;
- notification may be sent;
- reports are updated;
- case status becomes closed or escalated.

---

## 12. Customer-Facing Statuses

The customer should not see internal compliance details.

Customer-facing statuses should be clear and simple:

```text
Draft
Ready
Submitted
Pending security review
Approved
Rejected
Delayed
Completed
Blocked
```

Examples:

```text
Your external transfer request is pending security review.
```

```text
This transfer cannot be submitted because the selected network is incompatible with the asset.
```

```text
This digital asset payment is available only for eligible business recipients.
```

---

## 13. Internal Statuses

Internal statuses may be more detailed:

```text
validation_failed
eligible
auto_approved
pending_review
case_open
case_assigned
approved_by_reviewer
rejected_by_reviewer
escalated
blocked_policy
closed
```

These should be visible only in internal dashboards.

---

## 14. Audit Events

Every decision should create an audit event.

Example audit events:

```text
risk_evaluation_started
validation_failed
risk_score_calculated
auto_approved
pending_review
review_case_created
reviewer_decision_recorded
blocked_by_policy
customer_notified
```

Suggested audit event fields:

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
risk_level
decision
reasons
case_id
user_message
internal_notes
```

---

## 15. Backend Service Design

Suggested service:

```text
backend/app/services/risk_review_engine.py
```

Suggested rule files:

```text
backend/app/rules/withdrawal_rules.py
backend/app/rules/payment_rules.py
backend/app/rules/buy_sell_rules.py
backend/app/rules/security_rules.py
backend/app/rules/risk_thresholds.py
```

Suggested schemas:

```text
backend/app/schemas/risk_review.py
backend/app/schemas/review_case.py
```

Suggested models:

```text
backend/app/models/risk_event.py
backend/app/models/review_case.py
backend/app/models/audit_event.py
```

---

## 16. Suggested API Endpoints

### 16.1 Evaluate Withdrawal

```text
POST /api/withdrawals/evaluate
```

Input:

```json
{
  "asset": "BTC",
  "network": "Bitcoin",
  "amount": 0.001,
  "destination_address": "bc1q...",
  "wallet_type": "external_crypto_service"
}
```

Output:

```json
{
  "decision": "pending_review",
  "risk_level": "medium",
  "reasons": ["first_time_external_address"],
  "case_required": true,
  "user_message": "Your external transfer request is pending security review."
}
```

### 16.2 Submit Withdrawal

```text
POST /api/withdrawals
```

Creates withdrawal request and audit event.

### 16.3 Evaluate Digital Asset Payment

```text
POST /api/payments/digital-assets/evaluate
```

Checks recipient eligibility, amount, reference number, and payment rules.

### 16.4 Review Cases

```text
GET /api/review-cases
GET /api/review-cases/{case_id}
POST /api/review-cases/{case_id}/decision
```

### 16.5 Audit Events

```text
GET /api/audit-events
GET /api/audit-events?customer_id=...
GET /api/audit-events?case_id=...
```

---

## 17. Prototype Implementation Plan

### Phase 1: Documentation

- define engine rules;
- define risk levels;
- define decision object;
- define case workflow;
- define audit event structure.

### Phase 2: Mock Backend

- create FastAPI backend;
- create Pydantic schemas;
- implement deterministic rule engine;
- return mock decisions;
- create in-memory or SQLite review cases;
- create audit events.

### Phase 3: Frontend Integration

- connect WithdrawalsPage to risk evaluation endpoint;
- connect PaymentsPage to payment evaluation endpoint;
- connect ComplianceReviewPage to review cases endpoint;
- show real simulated case status.

### Phase 4: Persistence

- SQLite database;
- audit events table;
- review cases table;
- withdrawal requests table;
- digital asset payments table.

### Phase 5: Reporting

- include risk decisions in ReportsPage;
- export evidence package;
- generate PDF report concept.

---

## 18. Example Rule Evaluation

Example withdrawal:

```json
{
  "action_type": "external_withdrawal",
  "asset": "BTC",
  "network": "Bitcoin",
  "amount": 0.001,
  "destination_address": "bc1qexample",
  "address_format_valid": true,
  "first_time_address": true,
  "device_known": true,
  "strong_authentication_completed": true,
  "wallet_risk_signal": "none"
}
```

Evaluation:

```text
Validation:
- amount valid
- asset supported
- network compatible
- address format valid

Security:
- strong authentication completed
- device known

Risk:
- first-time external address -> medium risk

Decision:
- pending human review
```

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

---

## 19. Design Constraints

The Risk & Review Engine should avoid:

- black-box decisions;
- unexplained risk scores;
- autonomous high-impact decisions without review;
- hidden fees or hidden risk states;
- approving external withdrawals without audit events;
- treating digital asset payments like unrestricted wallet transfers.

The engine should prioritize:

- explainability;
- reproducibility;
- auditability;
- human review for ambiguous cases;
- customer-friendly status messages;
- internal evidence for reviewers.

---

## 20. Open Questions

Important questions:

- What exact thresholds should apply for auto approval?
- Should first external withdrawal always require review?
- Should all new addresses require a cooling period?
- How should wallet risk signals be sourced in a real system?
- What events require step-up authentication?
- What is the maximum auto-approved amount?
- Which assets can be externally withdrawn?
- Should EUR digital asset concept always remain internal?
- How should business recipient eligibility be maintained?
- What review SLA should be shown to customers?
- What audit events must be immutable?
- How should reviewer decisions be reported internally?
- What data retention rules apply?

---

## 21. Conclusion

The Risk & Review Engine is the operational core of Aurora Digital Assets.

It connects the customer-facing banking experience with the bank's security, compliance, AML, custody, reporting, and human review responsibilities.

The engine allows the system to:

- approve normal low-risk actions automatically;
- reject invalid requests immediately;
- block high-risk activity;
- create human review cases for sensitive actions;
- generate audit evidence for every decision.

This is what makes Aurora Digital Assets more than a wallet UI.

It becomes a controlled banking architecture for responsible digital asset access.

---

## 22. Disclaimer

This document describes a product and architecture concept only.

Aurora Digital Assets is not a bank, not a custody provider, not a crypto exchange, not a payment institution, and not a regulated financial service.

The Risk & Review Engine described here is fictional and intended for product design, architecture planning, UX, compliance discussion, and portfolio demonstration.

No real AML checks, sanctions screening, wallet analysis, bank systems, customer data, payments, private keys, assets, or blockchain transactions are used.