from datetime import datetime, timezone

from app.schemas.ai_threat_defense import (
    AIThreatDefenseEvaluationRequest,
    AIThreatDefenseEvaluationResponse,
    AIThreatScenario,
    ThreatSurface,
)


class AIThreatDefenseService:
    """Deterministic AI-assisted threat defense catalog and evaluator."""

    def list_threat_surfaces(self) -> list[ThreatSurface]:
        return [
            ThreatSurface(
                surface_id="FRONTEND-ROUTES",
                name="Frontend routes",
                category="frontend",
                description=(
                    "React route and screen structure that guides customer and "
                    "staff workflows but is not a security boundary."
                ),
                exposure_level="public",
                sensitivity_level="medium",
                related_modules=[
                    "dashboard",
                    "payments",
                    "buy-sell",
                    "wallet",
                    "custody",
                    "withdrawals",
                ],
                defensive_controls=[
                    "server-side validation",
                    "response minimization",
                    "secure error handling",
                ],
                audit_event_required=False,
                review_case_required=False,
                evidence_package_required=False,
            ),
            ThreatSurface(
                surface_id="FASTAPI-ENDPOINTS",
                name="FastAPI endpoints",
                category="backend_api",
                description=(
                    "Backend API boundary for deterministic banking prototype "
                    "workflows and internal control centers."
                ),
                exposure_level="internal",
                sensitivity_level="high",
                related_modules=["all backend APIs"],
                defensive_controls=[
                    "server-side validation",
                    "object-level authorization",
                    "audit event correlation",
                ],
                audit_event_required=True,
                review_case_required=False,
                evidence_package_required=False,
            ),
            ThreatSurface(
                surface_id="SENSITIVE-OPERATIONS",
                name="Sensitive operations",
                category="sensitive_operations",
                description=(
                    "High-risk digital asset and banking actions requiring "
                    "deterministic backend approval controls."
                ),
                exposure_level="restricted",
                sensitivity_level="critical",
                related_modules=[
                    "withdrawals",
                    "buy-sell",
                    "payments",
                    "sensitive-approval",
                ],
                defensive_controls=[
                    "step-up approval",
                    "least privilege",
                    "require human approval",
                ],
                audit_event_required=True,
                review_case_required=True,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="REVIEW-CASES",
                name="Review cases",
                category="review_workflow",
                description=(
                    "Human review workflow for escalated risk, compliance, and "
                    "security decisions."
                ),
                exposure_level="restricted",
                sensitivity_level="high",
                related_modules=[
                    "compliance-review",
                    "review-case-lifecycle",
                ],
                defensive_controls=[
                    "reviewer action monitoring",
                    "least privilege",
                    "evidence chain review",
                ],
                audit_event_required=True,
                review_case_required=False,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="EVIDENCE-PACKAGES",
                name="Evidence packages",
                category="evidence",
                description=(
                    "Decision evidence assembled for compliance review, security "
                    "review, and audit traceability."
                ),
                exposure_level="restricted",
                sensitivity_level="high",
                related_modules=["evidence-packages", "reporting"],
                defensive_controls=[
                    "evidence chain review",
                    "response minimization",
                    "no secrets in prompts/logs/docs",
                ],
                audit_event_required=True,
                review_case_required=False,
                evidence_package_required=False,
            ),
            ThreatSurface(
                surface_id="AUDIT-EVENTS",
                name="Audit events",
                category="audit",
                description=(
                    "Traceable audit records for sensitive actions, risk "
                    "decisions, and review outcomes."
                ),
                exposure_level="restricted",
                sensitivity_level="critical",
                related_modules=["audit-events", "reporting", "review-cases"],
                defensive_controls=[
                    "audit event correlation",
                    "evidence chain review",
                    "secure error handling",
                ],
                audit_event_required=True,
                review_case_required=False,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="DEMO-ADMIN",
                name="Demo admin",
                category="admin_tools",
                description=(
                    "Local prototype administration tooling with no production "
                    "authority or real customer data."
                ),
                exposure_level="internal",
                sensitivity_level="high",
                related_modules=["admin-demo"],
                defensive_controls=[
                    "least privilege",
                    "audit event correlation",
                    "secure error handling",
                ],
                audit_event_required=True,
                review_case_required=True,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="LOGS-ERRORS",
                name="Logs and errors",
                category="observability",
                description=(
                    "Internal logs and error records that support investigation "
                    "without exposing secrets or implementation internals."
                ),
                exposure_level="internal",
                sensitivity_level="high",
                related_modules=["backend", "frontend"],
                defensive_controls=[
                    "secure error handling",
                    "response minimization",
                    "secret exposure signal review",
                ],
                audit_event_required=True,
                review_case_required=False,
                evidence_package_required=False,
            ),
            ThreatSurface(
                surface_id="CONFIG-SECRETS",
                name="Configuration and secrets",
                category="secrets_configuration",
                description=(
                    "Environment configuration and future secret references that "
                    "must not appear in code, docs, logs, or evidence packages."
                ),
                exposure_level="restricted",
                sensitivity_level="critical",
                related_modules=["backend", "cloud-future", "ci-cd-future"],
                defensive_controls=[
                    "no secrets in prompts/logs/docs",
                    "least privilege",
                    "secure error handling",
                ],
                audit_event_required=True,
                review_case_required=True,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="FUTURE-CLOUD-KUBERNETES",
                name="Future cloud and Kubernetes",
                category="infrastructure_future",
                description=(
                    "Future cloud identity, storage, networking, and Kubernetes "
                    "posture that is documented as a non-runtime prototype concern."
                ),
                exposure_level="future",
                sensitivity_level="critical",
                related_modules=[
                    "infrastructure-security",
                    "kubernetes",
                    "cloud-iam",
                ],
                defensive_controls=[
                    "least privilege",
                    "permission-aware retrieval",
                    "audit event correlation",
                ],
                audit_event_required=True,
                review_case_required=True,
                evidence_package_required=True,
            ),
            ThreatSurface(
                surface_id="FUTURE-CUSTODIAN-INTEGRATION",
                name="Future custodian integration",
                category="custodian_future",
                description=(
                    "Future regulated custodian boundary for custody operations, "
                    "settlement, withdrawals, and incident coordination."
                ),
                exposure_level="future",
                sensitivity_level="critical",
                related_modules=[
                    "custody",
                    "regulated-custodian",
                    "withdrawals",
                ],
                defensive_controls=[
                    "least privilege",
                    "step-up approval",
                    "require human approval",
                ],
                audit_event_required=True,
                review_case_required=True,
                evidence_package_required=True,
            ),
        ]

    def list_ai_threat_scenarios(self) -> list[AIThreatScenario]:
        return [
            AIThreatScenario(
                scenario_id="ai_assisted_api_mapping",
                title="AI-assisted API mapping",
                description=(
                    "Defensive evaluation of signals that suggest rapid mapping "
                    "of backend endpoints, responses, and error behavior."
                ),
                affected_surface_categories=["backend_api", "observability"],
                weak_signals=[
                    "endpoint enumeration",
                    "response pattern comparison",
                    "verbose error interpretation",
                ],
                expected_decision="harden or escalate depending on signals",
            ),
            AIThreatScenario(
                scenario_id="ai_assisted_documentation_exposure",
                title="AI-assisted documentation exposure",
                description=(
                    "Defensive evaluation of documentation details that could "
                    "accelerate mapping of internal controls or sensitive flows."
                ),
                affected_surface_categories=[
                    "frontend",
                    "backend_api",
                    "secrets_configuration",
                ],
                weak_signals=[
                    "overly detailed public documentation",
                    "internal control naming exposure",
                    "configuration detail exposure",
                ],
                expected_decision="harden or escalate depending on signals",
            ),
            AIThreatScenario(
                scenario_id="ai_assisted_sensitive_operation_chain",
                title="AI-assisted sensitive operation chain",
                description=(
                    "Defensive evaluation of chained signals across sensitive "
                    "financial operations, audit, evidence, and review workflows."
                ),
                affected_surface_categories=[
                    "sensitive_operations",
                    "audit",
                    "review_workflow",
                    "evidence",
                ],
                weak_signals=[
                    "sensitive operation chain",
                    "automation signal",
                    "permission anomaly",
                    "endpoint enumeration",
                ],
                expected_decision="review_required when chain risk is critical",
            ),
            AIThreatScenario(
                scenario_id="ai_assisted_permission_abuse",
                title="AI-assisted permission abuse",
                description=(
                    "Defensive evaluation of anomalous reviewer, staff, admin, "
                    "or evidence access patterns."
                ),
                affected_surface_categories=[
                    "review_workflow",
                    "evidence",
                    "audit",
                    "admin_tools",
                ],
                weak_signals=[
                    "permission anomaly",
                    "reviewer action anomaly",
                    "admin tool access anomaly",
                ],
                expected_decision="escalate or review_required",
            ),
            AIThreatScenario(
                scenario_id="ai_assisted_secret_exposure_signal",
                title="AI-assisted secret exposure signal",
                description=(
                    "Defensive evaluation of indications that sensitive "
                    "configuration or secret-like material may have been exposed."
                ),
                affected_surface_categories=[
                    "secrets_configuration",
                    "observability",
                    "evidence",
                ],
                weak_signals=[
                    "secret exposure signal",
                    "documentation exposure",
                    "log or evidence exposure",
                ],
                expected_decision="review_required when exposure risk is critical",
            ),
        ]

    def evaluate_ai_threat_scenario(
        self,
        request: AIThreatDefenseEvaluationRequest,
    ) -> AIThreatDefenseEvaluationResponse:
        scenario_config = self._scenario_config(request.scenario_id)
        base_score = scenario_config["base_score"]
        risk_score = min(base_score + self._signal_score(request), 100)
        severity = self._severity(risk_score)
        decision = self._decision(severity)

        if request.secret_exposure_signal and risk_score >= 90:
            decision = "review_required"

        evidence_package_ready = risk_score >= 85
        review_case_required = risk_score >= 85
        review_case_id = (
            scenario_config["review_case_id"]
            if review_case_required and scenario_config["review_case_id"]
            else None
        )

        return AIThreatDefenseEvaluationResponse(
            scenario_id=request.scenario_id,
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            affected_surfaces=scenario_config["affected_surfaces"],
            weak_signals=self._weak_signals(request, scenario_config["weak_signals"]),
            defensive_controls=self._defensive_controls(
                scenario_config["affected_surfaces"]
            ),
            preventive_controls=self._preventive_controls(request),
            detective_controls=self._detective_controls(request),
            corrective_controls=self._corrective_controls(
                request=request,
                evidence_package_ready=evidence_package_ready,
                review_case_required=review_case_required,
            ),
            audit_event_created=True,
            audit_event_id=scenario_config["audit_event_id"],
            correlation_id=scenario_config["correlation_id"],
            evidence_package_ready=evidence_package_ready,
            review_case_required=review_case_required,
            review_case_id=review_case_id,
            recommended_next_actions=self._recommended_next_actions(
                decision=decision,
                request=request,
                review_case_required=review_case_required,
            ),
            created_at=datetime.now(timezone.utc),
        )

    def _scenario_config(self, scenario_id: str) -> dict:
        scenarios = {
            "ai_assisted_api_mapping": {
                "base_score": 55,
                "affected_surfaces": ["FASTAPI-ENDPOINTS", "LOGS-ERRORS"],
                "audit_event_id": "AUD-AI-THREAT-API-MAPPING",
                "correlation_id": "CORR-AI-THREAT-API-MAPPING",
                "review_case_id": None,
                "weak_signals": [
                    "endpoint enumeration",
                    "response pattern comparison",
                    "verbose error interpretation",
                ],
            },
            "ai_assisted_documentation_exposure": {
                "base_score": 60,
                "affected_surfaces": [
                    "FRONTEND-ROUTES",
                    "FASTAPI-ENDPOINTS",
                    "CONFIG-SECRETS",
                ],
                "audit_event_id": "AUD-AI-THREAT-DOCUMENTATION-EXPOSURE",
                "correlation_id": "CORR-AI-THREAT-DOCUMENTATION-EXPOSURE",
                "review_case_id": None,
                "weak_signals": [
                    "documentation exposure",
                    "configuration detail exposure",
                    "internal workflow exposure",
                ],
            },
            "ai_assisted_sensitive_operation_chain": {
                "base_score": 75,
                "affected_surfaces": [
                    "SENSITIVE-OPERATIONS",
                    "AUDIT-EVENTS",
                    "REVIEW-CASES",
                    "EVIDENCE-PACKAGES",
                ],
                "audit_event_id": "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "correlation_id": "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "review_case_id": "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "weak_signals": [
                    "sensitive operation chain",
                    "automation signal",
                    "permission anomaly",
                    "endpoint enumeration",
                ],
            },
            "ai_assisted_permission_abuse": {
                "base_score": 70,
                "affected_surfaces": [
                    "REVIEW-CASES",
                    "EVIDENCE-PACKAGES",
                    "AUDIT-EVENTS",
                    "DEMO-ADMIN",
                ],
                "audit_event_id": "AUD-AI-THREAT-PERMISSION-ABUSE",
                "correlation_id": "CORR-AI-THREAT-PERMISSION-ABUSE",
                "review_case_id": None,
                "weak_signals": [
                    "permission anomaly",
                    "reviewer action anomaly",
                    "admin tool access anomaly",
                ],
            },
            "ai_assisted_secret_exposure_signal": {
                "base_score": 80,
                "affected_surfaces": [
                    "CONFIG-SECRETS",
                    "LOGS-ERRORS",
                    "EVIDENCE-PACKAGES",
                ],
                "audit_event_id": "AUD-AI-THREAT-SECRET-EXPOSURE",
                "correlation_id": "CORR-AI-THREAT-SECRET-EXPOSURE",
                "review_case_id": "CASE-AI-THREAT-SECRET-EXPOSURE",
                "weak_signals": [
                    "secret exposure signal",
                    "documentation exposure",
                    "log or evidence exposure",
                ],
            },
        }
        if scenario_id not in scenarios:
            raise ValueError(f"Unknown AI threat defense scenario: {scenario_id}")
        return scenarios[scenario_id]

    def _signal_score(self, request: AIThreatDefenseEvaluationRequest) -> int:
        score = 0
        if request.suspected_automation:
            score += 10
        if request.documentation_exposure:
            score += 10
        if request.endpoint_enumeration:
            score += 10
        if request.permission_anomaly:
            score += 15
        if request.sensitive_operation_chain:
            score += 20
        if request.secret_exposure_signal:
            score += 25
        if request.evidence_tampering_signal:
            score += 20
        if request.cloud_or_kubernetes_signal:
            score += 15
        if request.custodian_integration_signal:
            score += 20
        return score

    def _severity(self, risk_score: int) -> str:
        if risk_score >= 85:
            return "critical"
        if risk_score >= 65:
            return "high"
        if risk_score >= 40:
            return "medium"
        return "low"

    def _decision(self, severity: str) -> str:
        if severity == "critical":
            return "review_required"
        if severity == "high":
            return "escalate"
        if severity == "medium":
            return "harden"
        return "monitor"

    def _weak_signals(
        self,
        request: AIThreatDefenseEvaluationRequest,
        scenario_signals: list[str],
    ) -> list[str]:
        signals = list(scenario_signals)
        if request.suspected_automation:
            signals.append("suspected automation")
        if request.documentation_exposure:
            signals.append("documentation exposure")
        if request.endpoint_enumeration:
            signals.append("endpoint enumeration")
        if request.permission_anomaly:
            signals.append("permission anomaly")
        if request.sensitive_operation_chain:
            signals.append("sensitive operation chain")
        if request.secret_exposure_signal:
            signals.append("secret exposure signal")
        if request.evidence_tampering_signal:
            signals.append("evidence tampering signal")
        if request.cloud_or_kubernetes_signal:
            signals.append("cloud or Kubernetes signal")
        if request.custodian_integration_signal:
            signals.append("custodian integration signal")
        return list(dict.fromkeys(signals))

    def _defensive_controls(self, affected_surfaces: list[str]) -> list[str]:
        surfaces = {
            surface.surface_id: surface
            for surface in self.list_threat_surfaces()
        }
        controls: list[str] = []
        for surface_id in affected_surfaces:
            controls.extend(surfaces[surface_id].defensive_controls)
        return list(dict.fromkeys(controls))

    def _preventive_controls(
        self,
        request: AIThreatDefenseEvaluationRequest,
    ) -> list[str]:
        controls = [
            "response minimization",
            "server-side validation",
            "object-level authorization",
            "secure error handling",
        ]
        if request.sensitive_operation_chain:
            controls.extend(["step-up approval", "least privilege"])
        if request.documentation_exposure:
            controls.append("documentation classification")
        if request.secret_exposure_signal:
            controls.append("no secrets in prompts/logs/docs")
        if request.permission_anomaly:
            controls.extend(["least privilege", "permission-aware retrieval"])
        return list(dict.fromkeys(controls))

    def _detective_controls(
        self,
        request: AIThreatDefenseEvaluationRequest,
    ) -> list[str]:
        controls = ["audit event correlation"]
        if request.endpoint_enumeration:
            controls.extend([
                "API anomaly detection",
                "enumeration pattern detection",
            ])
        if request.permission_anomaly:
            controls.append("reviewer action monitoring")
        if request.secret_exposure_signal:
            controls.append("secret exposure signal review")
        if request.evidence_tampering_signal or request.sensitive_operation_chain:
            controls.append("evidence chain review")
        return list(dict.fromkeys(controls))

    def _corrective_controls(
        self,
        request: AIThreatDefenseEvaluationRequest,
        evidence_package_ready: bool,
        review_case_required: bool,
    ) -> list[str]:
        controls: list[str] = []
        if review_case_required:
            controls.append("create review case")
        if evidence_package_ready:
            controls.append("generate evidence package")
        if request.secret_exposure_signal:
            controls.append("rotate exposed credentials when applicable")
        if request.documentation_exposure:
            controls.append("restrict exposed documentation")
        if request.permission_anomaly:
            controls.append("tighten permissions")
        if request.sensitive_operation_chain:
            controls.extend([
                "require human approval",
                "pause sensitive operation if needed",
            ])
        return list(dict.fromkeys(controls))

    def _recommended_next_actions(
        self,
        decision: str,
        request: AIThreatDefenseEvaluationRequest,
        review_case_required: bool,
    ) -> list[str]:
        actions = [
            "Record the deterministic AI threat defense evaluation.",
            "Correlate the decision with related audit and evidence records.",
        ]
        if decision in {"harden", "escalate", "review_required"}:
            actions.append("Review exposed surfaces and tighten relevant controls.")
        if review_case_required:
            actions.append("Open a human review case before continuing the workflow.")
        if request.secret_exposure_signal:
            actions.append("Check logs, evidence, and documentation for secret exposure.")
        if request.sensitive_operation_chain:
            actions.append("Keep the sensitive operation paused until review completes.")
        return actions


ai_threat_defense_service = AIThreatDefenseService()
