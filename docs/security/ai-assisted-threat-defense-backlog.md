# AI-Assisted Threat Defense Backlog for Aurora Digital Assets

**Internal technical backlog**  
**Related document:** `docs/security/ai-assisted-threat-defense-layer.md`  
**Status:** Planning / defensive architecture backlog  
**Scope:** Local deterministic prototype first, future production-readiness later

Aurora Digital Assets now has a technical architecture document for the AI-Assisted Threat Defense Layer. This backlog converts that document into practical development phases.

The goal is to help Aurora prepare for a threat model where attackers may use advanced AI agents to rapidly analyze APIs, documentation, permissions, logs, workflows, infrastructure posture, sensitive operations, and small configuration weaknesses.

This backlog is defensive only. It does not contain exploit instructions, payloads, scripts, or offensive guidance.

---

## 1. Guiding Thesis

Aurora should defend against complete attack paths, not only isolated vulnerabilities.

```text
AI-assisted attacker
→ maps surfaces faster
→ finds weak signals faster
→ combines small failures faster
→ targets sensitive operations
→ attempts to bypass review, approval, evidence, or audit
```

Aurora response:

```text
Threat surface inventory
→ sensitive operation guard
→ permission and ownership controls
→ deterministic risk scoring
→ audit event
→ evidence package
→ review case
→ human approval
→ lifecycle mitigation
```

---

## 2. Current Baseline

Aurora already includes:

- API Security Control Center
- Infrastructure Security Control Center
- Azure Storage to Identity Risk flow
- Container & Kubernetes Hardening flow
- Cryptographic Agility Control Center
- Sensitive Operations Approval Engine
- Evidence Packages
- Review Cases
- Review Case Lifecycle & Decision Engine
- Compliance Review
- Risk Operations Console
- Operational Resilience Command Center
- Audit Events
- SQLite persistence
- Reporting API
- Demo Admin
- Balance Privacy Mode

The AI-Assisted Threat Defense Layer should connect these existing capabilities instead of duplicating them.

---

## 3. Phase 0 — Documentation and Control Mapping

**Status:** Started  
**Goal:** Convert the conceptual security document into actionable implementation units.

### Tasks

- [x] Create `docs/security/ai-assisted-threat-defense-layer.md`
- [ ] Create `docs/security/ai-assisted-threat-defense-backlog.md`
- [ ] Add a short reference to the AI-Assisted Threat Defense Layer in `README.md`
- [ ] Define public-safe vs internal-only security documentation categories
- [ ] Map existing Aurora modules to defensive controls
- [ ] Define which details must not be exposed publicly

### Deliverables

- Internal architecture document
- Technical backlog
- Public communication boundary
- Initial implementation roadmap

### Completion Criteria

- Backlog is committed
- README references the document without exposing sensitive implementation details
- No backend/frontend changes required in this phase

---

## 4. Phase 1 — Threat Surface Inventory

**Goal:** Create a deterministic inventory of Aurora’s attack surfaces.

### Backend Concept

Potential future endpoints:

```text
GET /api/ai-threat-defense/surfaces
GET /api/ai-threat-defense/surface-categories
GET /api/ai-threat-defense/control-map
```

### Surface Categories

- Frontend routes
- Backend endpoints
- Authentication/session flows
- Sensitive operations
- Buy/sell evaluation
- Withdrawals
- Digital asset payments
- New wallet registration
- Security device change
- Evidence packages
- Review cases
- Review case lifecycle
- Compliance Review
- Reporting API
- Demo Admin
- Audit events
- Logs and errors
- Configuration and environment variables
- Dependencies
- Future CI/CD
- Future cloud
- Future Kubernetes
- Future regulated custodian integration

### Data Model Draft

```text
ThreatSurface
- surface_id
- name
- category
- description
- exposure_level: public | internal | restricted | future
- sensitivity_level: low | medium | high | critical
- related_modules
- defensive_controls
- audit_event_required
- review_case_required
- evidence_package_required
```

### Tasks

- [ ] Add backend schema for `ThreatSurface`
- [ ] Add service with deterministic surface inventory
- [ ] Add read-only endpoint for surfaces
- [ ] Add tests for surface inventory
- [ ] Keep this phase read-only; no risk evaluation yet

### Completion Criteria

- Endpoint returns deterministic surface list
- Tests pass
- No sensitive details exposed in frontend or public docs

---

## 5. Phase 2 — AI-Assisted Threat Scenarios

**Goal:** Add defensive scenario evaluation for AI-assisted threat patterns.

### Backend Concept

Potential future endpoints:

```text
GET  /api/ai-threat-defense/scenarios
POST /api/ai-threat-defense/evaluate-scenario
```

### Initial Defensive Scenarios

```text
ai_assisted_api_mapping
ai_assisted_documentation_exposure
ai_assisted_endpoint_enumeration
ai_assisted_sensitive_operation_chain
ai_assisted_permission_abuse
ai_assisted_secret_exposure_signal
ai_assisted_review_case_manipulation
ai_assisted_evidence_tampering_signal
ai_assisted_cloud_permission_chain
ai_assisted_kubernetes_weakness_chain
ai_assisted_custodian_integration_risk
```

### Evaluation Response Draft

```text
AIThreatDefenseEvaluationResponse
- scenario_id
- risk_score
- severity
- decision: monitor | harden | escalate | block | review_required
- affected_surfaces
- weak_signals
- defensive_controls
- preventive_controls
- detective_controls
- corrective_controls
- audit_event_created
- audit_event_id
- correlation_id
- evidence_package_ready
- review_case_required
- review_case_id
- recommended_next_actions
```

### Deterministic Audit IDs

```text
AUD-AI-THREAT-API-MAPPING
AUD-AI-THREAT-DOCUMENTATION-EXPOSURE
AUD-AI-THREAT-ENDPOINT-ENUMERATION
AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN
AUD-AI-THREAT-PERMISSION-ABUSE
AUD-AI-THREAT-SECRET-EXPOSURE
AUD-AI-THREAT-REVIEW-CASE-MANIPULATION
AUD-AI-THREAT-EVIDENCE-TAMPERING
AUD-AI-THREAT-CLOUD-PERMISSION-CHAIN
AUD-AI-THREAT-K8S-WEAKNESS-CHAIN
AUD-AI-THREAT-CUSTODIAN-INTEGRATION-RISK
```

### Tasks

- [ ] Add scenario schema
- [ ] Add deterministic evaluation service
- [ ] Add route registration
- [ ] Add tests for at least 3 scenarios
- [ ] Ensure no offensive detail is returned
- [ ] Generate audit event metadata
- [ ] Prepare evidence package linkage for critical scenarios

### Completion Criteria

- Scenario endpoint works
- Critical scenarios return audit event + evidence readiness
- Tests pass
- No offensive payloads or exploit chains included

---

## 6. Phase 3 — Evidence Package Integration

**Goal:** Make critical AI-assisted threat findings generate evidence packages.

### Evidence Package IDs

```text
EP-FROM-AUD-AI-THREAT-API-MAPPING
EP-FROM-AUD-AI-THREAT-DOCUMENTATION-EXPOSURE
EP-FROM-AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN
EP-FROM-AUD-AI-THREAT-PERMISSION-ABUSE
EP-FROM-AUD-AI-THREAT-SECRET-EXPOSURE
```

### Evidence Package Fields

```text
source_module: ai_threat_defense
domain: ai_assisted_threat_defense
category: attack_path_defense
severity: high | critical
correlation_id
source_audit_event_id
affected_surfaces
defensive_controls
recommended_next_actions
```

### Tasks

- [ ] Extend evidence package service for AI threat audit IDs
- [ ] Add tests for evidence package generation
- [ ] Ensure evidence packages do not expose secrets
- [ ] Add readiness score rules
- [ ] Link to review case creation

### Completion Criteria

- Evidence packages can be generated from AI threat audit events
- Tests pass
- Evidence avoids sensitive implementation details

---

## 7. Phase 4 — Review Case Integration

**Goal:** Critical AI-assisted threat scenarios should create review cases.

### Review Case IDs

```text
CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN
CASE-AI-THREAT-PERMISSION-ABUSE
CASE-AI-THREAT-SECRET-EXPOSURE
CASE-AI-THREAT-EVIDENCE-TAMPERING
CASE-AI-THREAT-CLOUD-PERMISSION-CHAIN
CASE-AI-THREAT-K8S-WEAKNESS-CHAIN
```

### Case Type

```text
ai_assisted_threat_review
```

### Assigned Teams

```text
Risk Operations / Security Architecture
Risk Operations / Customer Protection
Risk Operations / Infrastructure Security
Risk Operations / Cryptographic Governance
Risk Operations / Evidence Integrity
```

### Tasks

- [ ] Extend review case service for AI threat evidence packages
- [ ] Add tests for review case creation
- [ ] Ensure cases can enter existing lifecycle engine
- [ ] Link final closure to audit event
- [ ] Add Compliance Review display support if needed

### Completion Criteria

- AI threat evidence can create review cases
- Review cases support lifecycle transitions
- Tests pass

---

## 8. Phase 5 — Sensitive Operation Guard Integration

**Goal:** Connect AI-assisted threat defense with the Sensitive Operations Approval Engine.

### Target Operations

- External wallet withdrawal
- New wallet registration
- High-value buy/sell
- Digital asset invoice payment
- Security device change
- Close critical review case
- Generate sensitive evidence package
- Reset demo audit data
- Override risk decision
- Future custody operation

### Integration Rules

- AI-assisted suspicious pattern + sensitive operation = higher risk score
- New wallet + high value + recent device change = review required
- Mobile approval rejected = blocked
- Reviewer closure without mitigation = blocked or review required
- Admin reset = dual control simulation
- Evidence generation from sensitive audit = role checked

### Tasks

- [ ] Add AI-assisted context to sensitive approval scenarios
- [ ] Add deterministic risk triggers
- [ ] Add tests for combined sensitive-operation scenarios
- [ ] Preserve existing sensitive approval behavior
- [ ] Avoid false claims of real AI detection

### Completion Criteria

- Sensitive operations can account for AI-assisted risk signals
- Existing tests continue to pass
- New tests added

---

## 9. Phase 6 — Secret Exposure Guard

**Goal:** Add deterministic modeling for secret exposure prevention and review.

### Secret Exposure Surfaces

- Code
- Logs
- Prompts
- Documentation
- Evidence packages
- Screenshots
- Environment variables
- CI/CD output
- Cloud configuration
- Kubernetes manifests
- Future custodian credentials

### Defensive Behaviors

- Classify secret exposure risk
- Recommend rotation
- Create audit event
- Prepare evidence package
- Create review case for high/critical exposure
- Recommend access review

### Potential Endpoint

```text
POST /api/ai-threat-defense/evaluate-secret-exposure
```

### Tasks

- [ ] Define secret exposure schema
- [ ] Add deterministic evaluation
- [ ] Add audit event IDs
- [ ] Add evidence package integration
- [ ] Add review case integration
- [ ] Add tests

### Completion Criteria

- Secret exposure scenarios are modeled defensively
- No real secret scanning required in prototype
- No real secrets handled

---

## 10. Phase 7 — Permission & Ownership Engine

**Goal:** Model object-level authorization and ownership validation as a first-class defensive layer.

### Objects

- Account
- Transaction
- Wallet
- Destination wallet
- Audit event
- Evidence package
- Review case
- Report
- Admin action
- Future custodian operation

### Tasks

- [ ] Define permission matrix document
- [ ] Add deterministic permission check service
- [ ] Add tests for allowed/denied object access
- [ ] Integrate with sensitive operations where practical
- [ ] Model ID enumeration defense

### Completion Criteria

- Ownership validation is explicit
- Permission failures generate audit events when sensitive
- Tests pass

---

## 11. Phase 8 — Audit Integrity and Evidence Chain

**Goal:** Model tamper-evident audit and evidence chains.

### Concepts

- Previous event reference
- Correlation chain
- Evidence package source audit event
- Review case source package
- Lifecycle closure event
- Tamper status
- Integrity check status

### Tasks

- [ ] Add document for audit chain model
- [ ] Add deterministic integrity check endpoint
- [ ] Add evidence chain summary
- [ ] Add tests for chain summary
- [ ] Avoid implementing real cryptographic signing in prototype

### Completion Criteria

- Aurora can explain evidence chain integrity
- No “tamper-proof” claim
- No real cryptographic signing claim

---

## 12. Phase 9 — Future Cloud/Kubernetes Guardrails

**Goal:** Extend AI-assisted threat defense to future infrastructure.

### Cloud Guardrails

- IAM least privilege
- Service account governance
- Storage exposure controls
- Trust policy review
- Cloud audit logs
- Deployment approvals

### Kubernetes Guardrails

- RBAC least privilege
- NetworkPolicies
- Non-root containers
- ServiceAccount token restrictions
- Resource limits
- Runtime monitoring
- Image scanning
- Deployment gates

### Tasks

- [ ] Connect existing Infrastructure Security scenarios to AI threat defense
- [ ] Add AI-assisted cloud permission chain scenario
- [ ] Add AI-assisted Kubernetes weakness chain scenario
- [ ] Add evidence/review integration
- [ ] Add tests

### Completion Criteria

- AI-assisted infrastructure chain risks are modeled
- Existing infrastructure tests continue to pass

---

## 13. Phase 10 — Future Regulated Custodian Integration Guardrails

**Goal:** Prepare Aurora for a future model where a bank integrates with a regulated digital asset custodian.

### Custodian Boundary Principles

- Aurora is not the custodian by default
- Bank controls customer relationship and risk process
- Custodian controls technical custody infrastructure
- Custody operations require approval, reconciliation, audit, and review
- Custodian integration must not expose secrets to Aurora UI, logs, prompts, or evidence packages

### Tasks

- [ ] Define custody and ownership model document
- [ ] Define custodian integration risk surfaces
- [ ] Define future custodian operation approval controls
- [ ] Define reconciliation evidence requirements
- [ ] Define incident coordination evidence requirements

### Completion Criteria

- Custodian boundary is clearly documented
- Future integration risks are mapped
- No claim of real custodian integration

---

## 14. Frontend Roadmap

Do not build a large frontend immediately. First complete backend and documentation.

Potential future page:

```text
/bank-staff/ai-threat-defense
```

### Page Sections

- Threat surface inventory
- AI-assisted scenario evaluator
- Affected surfaces
- Defensive controls
- Risk score
- Audit event ID
- Evidence package readiness
- Review case requirement
- Recommended next actions
- Public communication boundary

### Tasks

- [ ] Create service `aiThreatDefenseApi.ts`
- [ ] Create page `AIThreatDefensePage.tsx`
- [ ] Add route
- [ ] Add Bank Staff Workspace card
- [ ] Add EN/ES translations
- [ ] Add screenshot
- [ ] Update README

### Completion Criteria

- UI remains simple and defensive
- No offensive detail shown
- Backend-first data loading

---

## 15. Testing Roadmap

### Backend Tests

- [ ] Surface inventory endpoint
- [ ] Scenario list endpoint
- [ ] AI-assisted API mapping scenario
- [ ] Documentation exposure scenario
- [ ] Sensitive operation chain scenario
- [ ] Secret exposure signal scenario
- [ ] Evidence package generation
- [ ] Review case creation
- [ ] Lifecycle integration
- [ ] Invalid/low-risk scenario behavior

### Frontend Tests / Validation

- [ ] `npm run lint`
- [ ] `npm run build`
- [ ] Manual route check
- [ ] Screenshot update

### Required Validation Commands

```bash
cd backend
source .venv/bin/activate
python3 -m compileall app
python3 -m pytest

cd ../frontend
npm run lint
npm run build
```

---

## 16. README Update Tasks

After implementation phases begin:

- [ ] Add AI-Assisted Threat Defense Layer to project status
- [ ] Add module section
- [ ] Add endpoints
- [ ] Add demo flow step
- [ ] Add screenshot filename
- [ ] Add limitations
- [ ] Add no offensive-use note
- [ ] Add no “AI-proof” claim

Suggested screenshot:

```text
docs/screenshots/ai-threat-defense.png
```

---

## 17. Security Communication Rules

### Public-Safe

Aurora can publicly discuss:

- Defense in depth
- AI-assisted threat model
- Secure by design
- Compliance by design
- Auditability
- Sensitive operation approvals
- Evidence-based review
- Review case lifecycle
- Regulated custodian integration readiness
- Crypto-agility

### Internal-Only

Aurora should not publicly expose:

- Sensitive endpoint internals
- Permission logic details
- Control bypass conditions
- Operational playbooks
- Secret naming conventions
- Cloud/Kubernetes configuration details
- Incident response procedures
- Custodian integration secrets
- AI prompts with internal strategy
- Any real credential, token, key, or customer data

---

## 18. First Recommended Implementation

The first code implementation should be small:

```text
AI Threat Defense Phase 1:
Threat Surface Inventory + Defensive Scenario Evaluation
```

### Minimal Backend Scope

Files:

```text
backend/app/schemas/ai_threat_defense.py
backend/app/services/ai_threat_defense_service.py
backend/app/api/routes/ai_threat_defense.py
backend/tests/test_ai_threat_defense.py
```

Endpoints:

```text
GET  /api/ai-threat-defense/surfaces
GET  /api/ai-threat-defense/scenarios
POST /api/ai-threat-defense/evaluate-scenario
```

Initial scenarios:

```text
ai_assisted_api_mapping
ai_assisted_documentation_exposure
ai_assisted_sensitive_operation_chain
ai_assisted_permission_abuse
ai_assisted_secret_exposure_signal
```

Expected high-risk flow:

```text
scenario
→ risk_score
→ severity
→ defensive controls
→ audit_event_id
→ correlation_id
→ evidence_package_ready
→ review_case_required
```

### Why This First

This creates the foundation for all later implementation without immediately overbuilding UI or touching production-like controls.

---

## 19. Non-Goals

This backlog does not require:

- Real AI detection
- Real production monitoring
- Real cloud integration
- Real Kubernetes access
- Real custodian integration
- Real secret scanning
- Real exploit testing
- Offensive payloads
- Attack scripts
- Vulnerability exploitation
- AI-proof claims
- Invulnerability claims

---

## 20. Final Backlog Thesis

Aurora should evolve from module-level controls into attack-path defense.

```text
Not only:
API Security
Infrastructure Security
Sensitive Approval
Evidence
Review Cases

But:
AI-assisted attack path awareness
→ cross-layer risk scoring
→ audit evidence
→ review lifecycle
→ mitigation
```

The immediate next step is to implement a small backend-first AI Threat Defense module with deterministic surfaces and defensive scenarios.
