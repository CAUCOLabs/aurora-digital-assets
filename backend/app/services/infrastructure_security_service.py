from app.schemas.infrastructure_security import (
    EvaluateInfrastructureSecurityScenarioResponse,
    InfrastructureSecurityControl,
    InfrastructureSecurityEvent,
    InfrastructureSecurityLayer,
    InfrastructureSecurityScenario,
)
from app.services.audit_service import audit_service


AUDIT_IDS_BY_SCENARIO = {
    "object_authorization_to_data_exposure": "AUD-INFRA-OBJECT-AUTH",
    "unsafe_template_to_runtime_exposure": "AUD-INFRA-TEMPLATE",
    "pod_rbac_secret_read": "AUD-INFRA-K8S-SECRETS",
    "weak_irsa_trust_policy": "AUD-INFRA-IAM-TRUST",
    "wildcard_iam_permission": "AUD-INFRA-IAM-WILDCARD",
    "plaintext_secret_exposure": "AUD-INFRA-SECRET",
    "app_to_cloud_chain_reaction": "AUD-INFRA-CHAIN-REACTION",
}

CORRELATION_IDS_BY_SCENARIO = {
    scenario_id: audit_id.replace("AUD-", "CORR-")
    for scenario_id, audit_id in AUDIT_IDS_BY_SCENARIO.items()
}


class InfrastructureSecurityService:
    """Deterministic infrastructure security control center demo service."""

    def list_controls(self) -> list[InfrastructureSecurityControl]:
        return [
            self._control(
                "infrasec-ctrl-object-auth",
                "Object-level authorization guard",
                "application",
                "object_authorization",
                "Prevents authenticated sessions from reading or changing objects outside their ownership or staff authorization scope.",
                ["accounts", "transfers", "reports", "wallets", "KYC documents"],
                "Authenticated identity must match object ownership or staff authorization.",
                ["object_authorization_decision", "access_denial_audit_event"],
            ),
            self._control(
                "infrasec-ctrl-template-safety",
                "Safe template execution control",
                "application",
                "template_safety",
                "Allows user data in approved rendering flows while blocking user-controlled executable templates.",
                ["reports", "invoices", "emails", "PDF generation"],
                "Users may provide data, but not executable templates.",
                ["template_source_record", "escaped_input_record"],
            ),
            self._control(
                "infrasec-ctrl-k8s-rbac",
                "Kubernetes least privilege RBAC",
                "kubernetes",
                "rbac",
                "Restricts simulated web workloads from creating pods, listing secrets, or accessing unrelated namespaces.",
                ["service accounts", "config maps", "pods", "namespaces"],
                "Web workloads must not create pods, list secrets, or access unrelated namespaces.",
                ["rbac_permission_snapshot", "service_account_scope_record"],
            ),
            self._control(
                "infrasec-ctrl-namespace-isolation",
                "Namespace isolation control",
                "kubernetes",
                "namespace_isolation",
                "Keeps application, compliance, and reporting workloads isolated unless a business-approved path exists.",
                ["fintech-app namespace", "compliance namespace", "reporting namespace"],
                "Workloads must not access unrelated namespaces unless explicitly authorized.",
                ["namespace_boundary_record", "cross_namespace_denial"],
            ),
            self._control(
                "infrasec-ctrl-service-account-secrets",
                "Service account secret restriction",
                "kubernetes",
                "service_account",
                "Models a default-deny posture for Kubernetes secret reads by application service accounts.",
                ["Kubernetes secrets", "application credentials", "API tokens"],
                "Service accounts should not read secrets by default.",
                ["secret_read_entitlement_record", "secret_rotation_trigger"],
            ),
            self._control(
                "infrasec-ctrl-iam-trust",
                "Cloud IAM trust policy restriction",
                "cloud_iam",
                "iam_trust",
                "Binds simulated cloud role trust to a specific namespace and service account subject.",
                ["workload identity", "IRSA role", "cloud service role"],
                "Cloud role trust must bind to a specific namespace and service account.",
                ["trust_policy_condition_snapshot", "role_assumption_decision"],
            ),
            self._control(
                "infrasec-ctrl-iam-permissions",
                "Cloud IAM permission scope",
                "cloud_iam",
                "iam_permissions",
                "Requires business-aware cloud permissions scoped to the resources needed by the workload.",
                ["transaction table", "audit table", "reports bucket"],
                "IAM policies must avoid wildcard actions and wildcard resources.",
                ["iam_policy_scope_review", "resource_condition_record"],
            ),
            self._control(
                "infrasec-ctrl-secret-management",
                "Secret management control",
                "secrets",
                "secret_management",
                "Keeps simulated secrets centralized, scoped, rotated, and out of code, runtime logs, and shared configuration.",
                ["API keys", "signing keys", "database credentials", "third-party tokens"],
                "Secrets must be centralized, rotated, scoped, and never logged.",
                ["secret_location_record", "rotation_status_snapshot"],
            ),
            self._control(
                "infrasec-ctrl-audit-correlation",
                "Cross-layer audit correlation",
                "audit",
                "logging",
                "Connects application, Kubernetes, IAM, secrets, and database signals into a single audit trail.",
                [
                    "application logs",
                    "Kubernetes service account usage",
                    "IAM role assumption",
                    "secret access",
                    "database access",
                ],
                "Security events must correlate across application, Kubernetes, IAM, secrets, and data access.",
                ["cross_layer_correlation_id", "audit_event_record"],
            ),
            self._control(
                "infrasec-ctrl-chain-containment",
                "Chain reaction containment",
                "risk_operations",
                "chain_containment",
                "Escalates cross-layer weakness before an application issue can become infrastructure or data compromise.",
                [
                    "backend API",
                    "runtime environment",
                    "cloud identity",
                    "sensitive financial data",
                ],
                "One vulnerable layer must not allow uncontrolled movement to the next layer.",
                ["risk_operations_escalation", "evidence_readiness_flag"],
            ),
        ]

    def list_events(self) -> list[InfrastructureSecurityEvent]:
        return [
            self._event(
                "INFRASEC-2026-001",
                "Application object authorization failure",
                "application",
                "initial_access",
                "IDOR / object-level authorization failure",
                "critical",
                "block",
                "blocked",
                [
                    "Object-level authorization guard",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "transfer-demo-foreign-object",
                "Authenticated session attempted to access an object outside its authorization scope.",
                "If not blocked, this could expose sensitive financial data and trigger downstream abuse.",
                "Return not found, block disclosure, create audit event, and review object access logic.",
                "AUD-INFRA-OBJECT-AUTH",
                "CORR-INFRA-OBJECT-AUTH",
                "2026-06-14T11:05:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-002",
                "Unsafe template execution attempt",
                "application",
                "privilege_expansion",
                "Server-side template execution risk",
                "high",
                "block",
                "blocked",
                ["Safe template execution control", "Cross-layer audit correlation"],
                "report-renderer",
                "User-controlled input attempted to influence server-side template execution.",
                "Unsafe template execution could expose runtime context, secrets, or service metadata.",
                "Use predefined templates only, escape user data, and audit report generation.",
                "AUD-INFRA-TEMPLATE",
                "CORR-INFRA-TEMPLATE",
                "2026-06-14T11:14:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-003",
                "Service account can read Kubernetes secrets",
                "kubernetes",
                "secret_exposure",
                "Excessive Kubernetes RBAC permission",
                "critical",
                "harden_required",
                "under_review",
                [
                    "Kubernetes least privilege RBAC",
                    "Service account secret restriction",
                    "Chain reaction containment",
                ],
                "web-api service account",
                "The web API workload has a simulated permission allowing secret reads.",
                "A backend compromise could become secret exposure.",
                "Remove secret read permission, scope role to required config only, and rotate exposed secrets if needed.",
                "AUD-INFRA-K8S-SECRETS",
                "CORR-INFRA-K8S-SECRETS",
                "2026-06-14T11:22:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-004",
                "Weak cloud IAM trust policy",
                "cloud_iam",
                "cloud_role_misuse",
                "Weak workload identity trust condition",
                "critical",
                "harden_required",
                "under_review",
                ["Cloud IAM trust policy restriction", "Cross-layer audit correlation"],
                "aurora-web-api-role",
                "The simulated trust policy is not sufficiently bound to namespace and service account.",
                "The wrong workload could assume a cloud role.",
                "Bind trust policy to a specific namespace and service account subject.",
                "AUD-INFRA-IAM-TRUST",
                "CORR-INFRA-IAM-TRUST",
                "2026-06-14T11:31:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-005",
                "Wildcard IAM permission detected",
                "cloud_iam",
                "cloud_role_misuse",
                "Overbroad IAM policy",
                "critical",
                "harden_required",
                "under_review",
                ["Cloud IAM permission scope", "Chain reaction containment"],
                "AuroraTransactions table access",
                "Simulated workload policy contains wildcard-like access that should be narrowed.",
                "Compromised workload could access more resources than required.",
                "Restrict actions, resources, conditions, and environment-specific scope.",
                "AUD-INFRA-IAM-WILDCARD",
                "CORR-INFRA-IAM-WILDCARD",
                "2026-06-14T11:38:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-006",
                "Plaintext secret exposure in runtime configuration",
                "secrets",
                "secret_exposure",
                "Secret management failure",
                "high",
                "harden_required",
                "under_review",
                ["Secret management control", "Cross-layer audit correlation"],
                "api-token-demo",
                "Simulated runtime configuration exposes a plaintext token pattern.",
                "Secret exposure could enable unauthorized downstream service access.",
                "Move secret to managed secret storage, rotate it, and ensure logs never expose it.",
                "AUD-INFRA-SECRET",
                "CORR-INFRA-SECRET",
                "2026-06-14T11:46:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-007",
                "Application-to-cloud chain reaction risk",
                "risk_operations",
                "evidence_required",
                "Cross-layer compromise path",
                "critical",
                "escalate",
                "escalated",
                [
                    "Object-level authorization guard",
                    "Kubernetes least privilege RBAC",
                    "Cloud IAM permission scope",
                    "Secret management control",
                    "Chain reaction containment",
                ],
                "Aurora financial platform control plane",
                "Multiple simulated weak controls could allow an application bug to become an infrastructure incident.",
                "Application issue could move into Kubernetes, IAM, secrets, and sensitive data access.",
                "Escalate to Risk Operations, create audit event, prepare evidence package, and harden controls.",
                "AUD-INFRA-CHAIN-REACTION",
                "CORR-INFRA-CHAIN-REACTION",
                "2026-06-14T11:58:00+03:00",
            ),
        ]

    def list_layers(self) -> list[InfrastructureSecurityLayer]:
        return [
            self._layer(
                "layer-application",
                "Application Security",
                "application",
                "restricted",
                "Object access and template rendering are controlled at the backend boundary.",
                ["Object-level authorization guard", "Safe template execution control"],
                ["object access denials", "template source selection"],
            ),
            self._layer(
                "layer-kubernetes",
                "Kubernetes Runtime Security",
                "kubernetes",
                "review_required",
                "Workload identity, RBAC, namespace access, and secret reads require least privilege review.",
                [
                    "Kubernetes least privilege RBAC",
                    "Namespace isolation control",
                    "Service account secret restriction",
                ],
                ["service account permissions", "namespace access attempts"],
            ),
            self._layer(
                "layer-cloud-iam",
                "Cloud IAM Security",
                "cloud_iam",
                "restricted",
                "Role trust and permissions are modeled as narrow, workload-bound, and resource-scoped.",
                ["Cloud IAM trust policy restriction", "Cloud IAM permission scope"],
                ["role assumption", "wildcard permission indicators"],
            ),
            self._layer(
                "layer-secrets",
                "Secrets Security",
                "secrets",
                "monitored",
                "Secret access is simulated as centralized, scoped, rotated, and redacted from logs.",
                ["Secret management control"],
                ["secret access attempts", "rotation status", "log redaction checks"],
            ),
            self._layer(
                "layer-audit",
                "Audit Evidence",
                "audit",
                "hardened",
                "Cross-layer events use deterministic correlation IDs for later evidence package preparation.",
                ["Cross-layer audit correlation"],
                ["audit event creation", "correlation ID propagation"],
            ),
            self._layer(
                "layer-risk-operations",
                "Risk Operations",
                "risk_operations",
                "monitored",
                "Cross-layer chain reaction risk is escalated for staff review before sensitive operations continue.",
                ["Chain reaction containment"],
                ["escalated infrastructure events", "critical chain risk count"],
            ),
        ]

    def list_scenarios(self) -> list[InfrastructureSecurityScenario]:
        return [
            self._scenario(
                "object_authorization_to_data_exposure",
                "Object authorization to data exposure",
                "A user-controlled object ID attempts to access a financial object outside the authorized scope.",
                "application",
                ["application", "audit", "risk_operations"],
                ["object_authorization_failed", "sensitive_object_requested"],
                "block",
                ["Object-level authorization guard", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "unsafe_template_to_runtime_exposure",
                "Unsafe template to runtime exposure",
                "User-controlled input attempts to influence server-side template execution.",
                "application",
                ["application", "secrets", "audit"],
                ["unsafe_template_input_detected", "runtime_context_access"],
                "block",
                ["Safe template execution control", "Secret management control"],
            ),
            self._scenario(
                "pod_rbac_secret_read",
                "Pod RBAC secret read",
                "A simulated web workload has service account permissions that could read Kubernetes secrets.",
                "kubernetes",
                ["kubernetes", "secrets", "risk_operations"],
                ["service_account_can_read_secrets", "pod_privileged"],
                "harden_required",
                ["Kubernetes least privilege RBAC", "Service account secret restriction"],
            ),
            self._scenario(
                "weak_irsa_trust_policy",
                "Weak workload identity trust policy",
                "A cloud role trust policy is not bound narrowly enough to the expected namespace and service account.",
                "cloud_iam",
                ["kubernetes", "cloud_iam", "audit"],
                ["weak_trust_policy", "unexpected_workload_identity"],
                "harden_required",
                ["Cloud IAM trust policy restriction", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "wildcard_iam_permission",
                "Wildcard IAM permission",
                "A simulated cloud IAM policy allows wildcard-like actions or resources for a financial data workload.",
                "cloud_iam",
                ["cloud_iam", "audit", "risk_operations"],
                ["cloud_iam_wildcard_permissions", "sensitive_resource_scope"],
                "harden_required",
                ["Cloud IAM permission scope", "Chain reaction containment"],
            ),
            self._scenario(
                "plaintext_secret_exposure",
                "Plaintext secret exposure",
                "A simulated runtime configuration exposes a token-like value that should be managed centrally.",
                "secrets",
                ["secrets", "audit", "risk_operations"],
                ["secret_exposure_detected", "runtime_configuration"],
                "harden_required",
                ["Secret management control", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "app_to_cloud_chain_reaction",
                "Application-to-cloud chain reaction",
                "Multiple weak controls could allow an application issue to move through Kubernetes, IAM, secrets, and data access.",
                "application",
                [
                    "application",
                    "kubernetes",
                    "cloud_iam",
                    "secrets",
                    "audit",
                    "risk_operations",
                ],
                [
                    "object_authorization_failed",
                    "unsafe_template_input_detected",
                    "service_account_can_read_secrets",
                    "cloud_iam_wildcard_permissions",
                    "weak_trust_policy",
                    "secret_exposure_detected",
                ],
                "escalate",
                [
                    "Object-level authorization guard",
                    "Kubernetes least privilege RBAC",
                    "Cloud IAM permission scope",
                    "Secret management control",
                    "Chain reaction containment",
                ],
            ),
        ]

    def evaluate_scenario(
        self,
        *,
        scenario_id: str,
        object_authorization_failed: bool,
        unsafe_template_input_detected: bool,
        pod_privileged: bool,
        service_account_can_read_secrets: bool,
        cloud_iam_wildcard_permissions: bool,
        weak_trust_policy: bool,
        secret_exposure_detected: bool,
    ) -> EvaluateInfrastructureSecurityScenarioResponse:
        score = 10
        affected_layers = set[str]()
        triggered_controls = set[str]()
        risk_reasons: list[str] = []

        checks = [
            (
                object_authorization_failed,
                35,
                ["application", "audit", "risk_operations"],
                [
                    "Object-level authorization guard",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "object authorization failed",
            ),
            (
                unsafe_template_input_detected,
                25,
                ["application", "secrets", "audit"],
                [
                    "Safe template execution control",
                    "Secret management control",
                    "Cross-layer audit correlation",
                ],
                "unsafe template input detected",
            ),
            (
                pod_privileged,
                25,
                ["kubernetes", "risk_operations"],
                [
                    "Kubernetes least privilege RBAC",
                    "Namespace isolation control",
                    "Chain reaction containment",
                ],
                "privileged pod configuration",
            ),
            (
                service_account_can_read_secrets,
                35,
                ["kubernetes", "secrets", "risk_operations"],
                [
                    "Kubernetes least privilege RBAC",
                    "Service account secret restriction",
                    "Secret management control",
                    "Chain reaction containment",
                ],
                "service account can read secrets",
            ),
            (
                cloud_iam_wildcard_permissions,
                35,
                ["cloud_iam", "audit", "risk_operations"],
                [
                    "Cloud IAM permission scope",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "wildcard IAM permissions",
            ),
            (
                weak_trust_policy,
                30,
                ["kubernetes", "cloud_iam", "audit"],
                [
                    "Cloud IAM trust policy restriction",
                    "Cross-layer audit correlation",
                ],
                "weak cloud IAM trust policy",
            ),
            (
                secret_exposure_detected,
                30,
                ["secrets", "audit", "risk_operations"],
                [
                    "Secret management control",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "secret exposure detected",
            ),
        ]

        for enabled, points, layers, controls, reason in checks:
            if enabled:
                score += points
                affected_layers.update(layers)
                triggered_controls.update(controls)
                risk_reasons.append(reason)

        true_flags = len(risk_reasons)
        if true_flags >= 4:
            score += 15
        elif true_flags >= 2:
            score += 8

        if not affected_layers:
            affected_layers.add("application")
            triggered_controls.add("Cross-layer audit correlation")
            risk_reasons.append("no high-risk infrastructure indicator selected")

        risk_score = min(score, 100)
        severity = self._severity_for_score(risk_score)
        decision = self._decision_for_score(risk_score)
        audit_event_id = AUDIT_IDS_BY_SCENARIO.get(
            scenario_id,
            f"AUD-INFRA-{scenario_id.upper().replace('-', '_')}",
        )
        correlation_id = CORRELATION_IDS_BY_SCENARIO.get(
            scenario_id,
            f"CORR-INFRA-{scenario_id.upper().replace('-', '_')}",
        )
        evidence_package_ready = severity in {"high", "critical"}
        chain_reaction_risk = self._chain_reaction_risk(true_flags)
        recommended_action = self._recommended_action(decision)
        explanation = (
            "Deterministic prototype evaluation based on "
            f"{', '.join(risk_reasons)}. Evidence can be prepared later from "
            f"audit event {audit_event_id}."
        )

        audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="infrastructure-security-engine",
            actor_type="service",
            source_module="infrastructure_security",
            action="evaluate_scenario",
            object_type="infrastructure_security_scenario",
            object_id=scenario_id,
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=explanation,
            correlation_id=correlation_id,
            metadata={
                "prototype": True,
                "affected_layers": sorted(affected_layers),
                "chain_reaction_risk": chain_reaction_risk,
                "evidence_package_ready": evidence_package_ready,
            },
        )

        return EvaluateInfrastructureSecurityScenarioResponse(
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            affected_layers=sorted(affected_layers),
            chain_reaction_risk=chain_reaction_risk,
            triggered_controls=sorted(triggered_controls),
            audit_event_created=True,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=evidence_package_ready,
            recommended_action=recommended_action,
            explanation=explanation,
        )

    def _control(
        self,
        control_id: str,
        title: str,
        layer: str,
        category: str,
        description: str,
        protected_assets: list[str],
        decision_model: str,
        evidence_outputs: list[str],
    ) -> InfrastructureSecurityControl:
        return InfrastructureSecurityControl(
            control_id=control_id,
            title=title,
            layer=layer,
            category=category,
            description=description,
            protected_assets=protected_assets,
            decision_model=decision_model,
            evidence_outputs=evidence_outputs,
            enabled=True,
        )

    def _event(
        self,
        event_id: str,
        title: str,
        affected_layer: str,
        chain_stage: str,
        risk_type: str,
        severity: str,
        decision: str,
        status: str,
        triggered_controls: list[str],
        affected_asset: str,
        summary: str,
        chain_reaction_risk: str,
        recommended_action: str,
        audit_event_id: str,
        correlation_id: str,
        created_at: str,
    ) -> InfrastructureSecurityEvent:
        return InfrastructureSecurityEvent(
            event_id=event_id,
            title=title,
            affected_layer=affected_layer,
            chain_stage=chain_stage,
            risk_type=risk_type,
            severity=severity,
            decision=decision,
            status=status,
            triggered_controls=triggered_controls,
            affected_asset=affected_asset,
            summary=summary,
            chain_reaction_risk=chain_reaction_risk,
            recommended_action=recommended_action,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=severity in {"high", "critical"},
            created_at=created_at,
        )

    def _layer(
        self,
        layer_id: str,
        name: str,
        layer_type: str,
        posture: str,
        risk_summary: str,
        controls_applied: list[str],
        monitored_signals: list[str],
    ) -> InfrastructureSecurityLayer:
        return InfrastructureSecurityLayer(
            layer_id=layer_id,
            name=name,
            layer_type=layer_type,
            posture=posture,
            risk_summary=risk_summary,
            controls_applied=controls_applied,
            monitored_signals=monitored_signals,
        )

    def _scenario(
        self,
        scenario_id: str,
        title: str,
        description: str,
        starting_layer: str,
        possible_chain: list[str],
        risk_indicators: list[str],
        expected_decision: str,
        recommended_controls: list[str],
    ) -> InfrastructureSecurityScenario:
        return InfrastructureSecurityScenario(
            scenario_id=scenario_id,
            title=title,
            description=description,
            starting_layer=starting_layer,
            possible_chain=possible_chain,
            risk_indicators=risk_indicators,
            expected_decision=expected_decision,
            recommended_controls=recommended_controls,
        )

    def _severity_for_score(self, risk_score: int) -> str:
        if risk_score >= 70:
            return "critical"
        if risk_score >= 50:
            return "high"
        if risk_score >= 30:
            return "medium"
        return "low"

    def _decision_for_score(self, risk_score: int) -> str:
        if risk_score >= 85:
            return "escalate"
        if risk_score >= 70:
            return "harden_required"
        if risk_score >= 50:
            return "review_required"
        return "allow"

    def _chain_reaction_risk(self, true_flags: int) -> str:
        if true_flags >= 4:
            return (
                "Critical chain reaction path across application, Kubernetes, "
                "cloud IAM, secrets, audit evidence, and risk operations."
            )
        if true_flags >= 2:
            return (
                "Elevated chain reaction risk because multiple control layers "
                "require review before sensitive operations continue."
            )
        if true_flags == 1:
            return "Single-layer issue detected and contained with audit evidence."
        return "No chain reaction path selected in this deterministic scenario."

    def _recommended_action(self, decision: str) -> str:
        if decision == "escalate":
            return (
                "Escalate to Risk Operations, preserve cross-layer audit evidence, "
                "and harden application, Kubernetes, IAM, and secrets controls."
            )
        if decision == "harden_required":
            return (
                "Harden the affected control layer, preserve audit evidence, and "
                "prepare an evidence package if review is required."
            )
        if decision == "review_required":
            return "Open a staff review, validate control scope, and keep the audit correlation record."
        return "Allow the scenario to continue with standard monitoring."


infrastructure_security_service = InfrastructureSecurityService()
