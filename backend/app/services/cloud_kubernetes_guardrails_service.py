from datetime import datetime, timezone

from app.schemas.cloud_kubernetes_guardrails import (
    CloudKubernetesGuardrailControl,
    CloudKubernetesGuardrailDecision,
    CloudKubernetesGuardrailEvaluationRequest,
    CloudKubernetesGuardrailEvaluationResponse,
    CloudKubernetesGuardrailScenario,
    CloudKubernetesGuardrailSeverity,
)
from app.services.audit_service import audit_service


ACTIVE_REVIEW_STATUSES = {
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
}

SCENARIO_CONTEXT = {
    "cloud_kubernetes_readiness_gap": {
        "base_score": 70,
        "audit_event_id": "AUD-CLOUD-K8S-READINESS-GAP",
        "correlation_id": "CORR-CLOUD-K8S-READINESS-GAP",
        "review_case_id": "CASE-CLOUD-K8S-READINESS-GAP",
        "title": "Future cloud and Kubernetes readiness gap",
        "description": (
            "Evaluates whether future cloud or Kubernetes deployment readiness "
            "has enough protective controls to proceed."
        ),
        "required_controls": [
            "CLOUD-IDENTITY-BOUNDARY",
            "CLOUD-SECRET-MANAGEMENT",
            "CLOUD-AUDIT-LOGGING",
            "CLOUD-BACKUP-ENCRYPTION",
        ],
    },
    "cloud_secret_management_gap": {
        "base_score": 80,
        "audit_event_id": "AUD-CLOUD-K8S-SECRET-MANAGEMENT-GAP",
        "correlation_id": "CORR-CLOUD-K8S-SECRET-MANAGEMENT-GAP",
        "review_case_id": "CASE-CLOUD-K8S-SECRET-MANAGEMENT-GAP",
        "title": "Future cloud secret management gap",
        "description": (
            "Evaluates whether secret material is externalized and protected in "
            "a future cloud deployment path."
        ),
        "required_controls": [
            "CLOUD-SECRET-MANAGEMENT",
            "K8S-SECRET-HANDLING",
            "CLOUD-AUDIT-LOGGING",
        ],
    },
    "kubernetes_rbac_overexposure": {
        "base_score": 75,
        "audit_event_id": "AUD-CLOUD-K8S-RBAC-OVEREXPOSURE",
        "correlation_id": "CORR-CLOUD-K8S-RBAC-OVEREXPOSURE",
        "review_case_id": "CASE-CLOUD-K8S-RBAC-OVEREXPOSURE",
        "title": "Kubernetes RBAC overexposure",
        "description": (
            "Evaluates future Kubernetes RBAC least privilege before deployment."
        ),
        "required_controls": [
            "K8S-RBAC-LEAST-PRIVILEGE",
            "K8S-NAMESPACE-ISOLATION",
            "K8S-AUDIT-EVENTS",
        ],
    },
    "kubernetes_secret_handling_gap": {
        "base_score": 85,
        "audit_event_id": "AUD-CLOUD-K8S-SECRET-HANDLING-GAP",
        "correlation_id": "CORR-CLOUD-K8S-SECRET-HANDLING-GAP",
        "review_case_id": "CASE-CLOUD-K8S-SECRET-HANDLING-GAP",
        "title": "Kubernetes secret handling gap",
        "description": (
            "Evaluates whether future Kubernetes workloads avoid unsafe secret "
            "handling patterns in this deterministic prototype."
        ),
        "required_controls": [
            "CLOUD-SECRET-MANAGEMENT",
            "K8S-SECRET-HANDLING",
            "K8S-RBAC-LEAST-PRIVILEGE",
            "K8S-NAMESPACE-ISOLATION",
            "K8S-NETWORK-POLICY",
            "K8S-IMAGE-PROVENANCE",
            "K8S-RUNTIME-POLICY",
        ],
    },
    "cloud_audit_logging_gap": {
        "base_score": 70,
        "audit_event_id": "AUD-CLOUD-K8S-AUDIT-LOGGING-GAP",
        "correlation_id": "CORR-CLOUD-K8S-AUDIT-LOGGING-GAP",
        "review_case_id": "CASE-CLOUD-K8S-AUDIT-LOGGING-GAP",
        "title": "Future cloud audit logging gap",
        "description": (
            "Evaluates whether future cloud and Kubernetes activity would have "
            "sufficient audit event coverage."
        ),
        "required_controls": ["CLOUD-AUDIT-LOGGING", "K8S-AUDIT-EVENTS"],
    },
    "deployment_with_active_ai_threat_case": {
        "base_score": 85,
        "audit_event_id": "AUD-CLOUD-K8S-ACTIVE-AI-THREAT-CASE",
        "correlation_id": "CORR-CLOUD-K8S-ACTIVE-AI-THREAT-CASE",
        "review_case_id": "CASE-CLOUD-K8S-ACTIVE-AI-THREAT-CASE",
        "title": "Deployment with active AI Threat Defense case",
        "description": (
            "Evaluates whether future deployment should pause while an AI "
            "Threat Defense review case remains active."
        ),
        "required_controls": [
            "K8S-DEPLOYMENT-APPROVAL",
            "CLOUD-AUDIT-LOGGING",
        ],
    },
    "deployment_with_active_secret_guard_case": {
        "base_score": 90,
        "audit_event_id": "AUD-CLOUD-K8S-ACTIVE-SECRET-GUARD-CASE",
        "correlation_id": "CORR-CLOUD-K8S-ACTIVE-SECRET-GUARD-CASE",
        "review_case_id": "CASE-CLOUD-K8S-ACTIVE-SECRET-GUARD-CASE",
        "title": "Deployment with active Secret Exposure Guard case",
        "description": (
            "Evaluates whether future deployment should remain blocked while a "
            "Secret Exposure Guard review case is active."
        ),
        "required_controls": [
            "K8S-DEPLOYMENT-APPROVAL",
            "CLOUD-SECRET-MANAGEMENT",
            "K8S-SECRET-HANDLING",
        ],
    },
    "custodian_network_boundary_gap": {
        "base_score": 85,
        "audit_event_id": "AUD-CLOUD-K8S-CUSTODIAN-NETWORK-BOUNDARY-GAP",
        "correlation_id": "CORR-CLOUD-K8S-CUSTODIAN-NETWORK-BOUNDARY-GAP",
        "review_case_id": "CASE-CLOUD-K8S-CUSTODIAN-NETWORK-BOUNDARY-GAP",
        "title": "Future custodian network boundary gap",
        "description": (
            "Evaluates whether future custodian integration paths have a clear "
            "network boundary and approval model."
        ),
        "required_controls": [
            "FUTURE-CUSTODIAN-NETWORK-BOUNDARY",
            "CLOUD-NETWORK-SEGMENTATION",
            "CLOUD-AUDIT-LOGGING",
        ],
    },
}


class CloudKubernetesGuardrailsService:
    """Deterministic future deployment guardrail service."""

    def list_controls(self) -> list[CloudKubernetesGuardrailControl]:
        return [
            self._control(
                "CLOUD-IDENTITY-BOUNDARY",
                "Cloud identity boundary",
                "cloud",
                "Future cloud identities must be scoped to explicit workloads and duties.",
            ),
            self._control(
                "CLOUD-SECRET-MANAGEMENT",
                "Cloud secret management",
                "cloud",
                "Secrets must be externalized, protected, rotated, and excluded from code and logs.",
            ),
            self._control(
                "CLOUD-NETWORK-SEGMENTATION",
                "Cloud network segmentation",
                "cloud",
                "Future cloud services must use segmented network paths with explicit access.",
            ),
            self._control(
                "CLOUD-AUDIT-LOGGING",
                "Cloud audit logging",
                "cloud",
                "Future cloud activity must create reviewable audit events.",
            ),
            self._control(
                "CLOUD-BACKUP-ENCRYPTION",
                "Cloud backup encryption",
                "cloud",
                "Backups must be encrypted and traceable before production use.",
            ),
            self._control(
                "K8S-RBAC-LEAST-PRIVILEGE",
                "Kubernetes RBAC least privilege",
                "kubernetes",
                "Kubernetes service accounts must avoid broad permissions and secret reads.",
            ),
            self._control(
                "K8S-NAMESPACE-ISOLATION",
                "Kubernetes namespace isolation",
                "kubernetes",
                "Workloads must remain isolated by namespace unless explicitly approved.",
            ),
            self._control(
                "K8S-SECRET-HANDLING",
                "Kubernetes secret handling",
                "kubernetes",
                "Kubernetes workloads must not store or echo secret values in manifests or logs.",
            ),
            self._control(
                "K8S-IMAGE-PROVENANCE",
                "Kubernetes image provenance",
                "kubernetes",
                "Container image origin and immutability must be verified before deployment.",
            ),
            self._control(
                "K8S-RUNTIME-POLICY",
                "Kubernetes runtime policy",
                "kubernetes",
                "Runtime restrictions must be defined before future Kubernetes use.",
            ),
            self._control(
                "K8S-NETWORK-POLICY",
                "Kubernetes network policy",
                "kubernetes",
                "Cluster traffic must use default-deny policy with explicit allowed paths.",
            ),
            self._control(
                "K8S-AUDIT-EVENTS",
                "Kubernetes audit events",
                "kubernetes",
                "Kubernetes control-plane activity must be represented in audit evidence.",
            ),
            self._control(
                "K8S-DEPLOYMENT-APPROVAL",
                "Kubernetes deployment approval",
                "kubernetes",
                "Future deployment changes must require human approval when risk is elevated.",
            ),
            self._control(
                "FUTURE-CUSTODIAN-NETWORK-BOUNDARY",
                "Future custodian network boundary",
                "custody",
                "Future custodian integration must have a controlled network boundary.",
            ),
        ]

    def list_scenarios(self) -> list[CloudKubernetesGuardrailScenario]:
        return [
            CloudKubernetesGuardrailScenario(
                scenario_id=scenario_id,
                title=context["title"],
                description=context["description"],
                expected_decision=self._decision_for_score(context["base_score"]),
                required_controls=list(context["required_controls"]),
            )
            for scenario_id, context in SCENARIO_CONTEXT.items()
        ]

    def evaluate(
        self,
        request: CloudKubernetesGuardrailEvaluationRequest,
    ) -> CloudKubernetesGuardrailEvaluationResponse:
        context = SCENARIO_CONTEXT.get(
            request.scenario_id,
            SCENARIO_CONTEXT["cloud_kubernetes_readiness_gap"],
        )
        required_controls = list(context["required_controls"])
        missing_controls = self._missing_controls(request)
        satisfied_controls = self._satisfied_controls(request)
        risk_score = self._risk_score(request, context["base_score"])
        severity = self._severity_for_score(risk_score)
        decision = self._decision_for_score(risk_score)

        active_secret_guard = self._is_active_status(
            request.active_secret_guard_case_status
        )
        if (
            request.scenario_id == "deployment_with_active_secret_guard_case"
            and active_secret_guard
        ):
            decision = "block_deployment"

        if (
            request.kubernetes_enabled
            and not request.secrets_externalized
            and risk_score >= 85
        ):
            decision = "block_deployment"
        elif request.kubernetes_enabled and not request.secrets_externalized:
            decision = "review_required"

        deployment_blocked = decision == "block_deployment"
        evidence_package_ready = severity in {"high", "critical", "medium"}
        review_case_required = severity in {"high", "critical"}
        review_case_id = context["review_case_id"] if review_case_required else None
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=context["audit_event_id"],
            actor_id=request.reviewer_id,
            actor_type="staff" if request.reviewer_id != "system" else "service",
            source_module="cloud_kubernetes_guardrails",
            action="evaluate_future_deployment_guardrails",
            object_type="future_deployment_path",
            object_id=request.scenario_id,
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=(
                "Future cloud and Kubernetes deployment guardrails evaluated by "
                "deterministic prototype policy."
            ),
            evidence_reference=(
                f"EP-FROM-{context['audit_event_id']}"
                if evidence_package_ready
                else None
            ),
            review_case_id=review_case_id,
            correlation_id=context["correlation_id"],
            metadata={
                "deployment_target": request.deployment_target,
                "environment": request.environment,
                "cloud_provider": request.cloud_provider,
                "kubernetes_enabled": request.kubernetes_enabled,
                "missing_controls": missing_controls,
                "satisfied_controls": satisfied_controls,
                "active_ai_threat_case_id": request.active_ai_threat_case_id,
                "active_secret_guard_case_id": request.active_secret_guard_case_id,
            },
        )

        return CloudKubernetesGuardrailEvaluationResponse(
            scenario_id=request.scenario_id,
            deployment_target=request.deployment_target,
            environment=request.environment,
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            deployment_guard_applied=True,
            deployment_blocked=deployment_blocked,
            required_controls=required_controls,
            missing_controls=missing_controls,
            satisfied_controls=satisfied_controls,
            linked_ai_threat_case_id=request.active_ai_threat_case_id,
            linked_secret_guard_case_id=request.active_secret_guard_case_id,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            evidence_package_ready=evidence_package_ready,
            review_case_required=review_case_required,
            review_case_id=review_case_id,
            recommended_next_actions=self._recommended_next_actions(
                missing_controls=missing_controls,
                review_case_required=review_case_required,
                deployment_blocked=deployment_blocked,
            ),
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _control(
        self,
        control_id: str,
        title: str,
        control_layer: str,
        description: str,
    ) -> CloudKubernetesGuardrailControl:
        return CloudKubernetesGuardrailControl(
            control_id=control_id,
            title=title,
            control_layer=control_layer,
            description=description,
            enabled=True,
        )

    def _risk_score(
        self,
        request: CloudKubernetesGuardrailEvaluationRequest,
        base_score: int,
    ) -> int:
        score = base_score
        if request.kubernetes_enabled and not request.rbac_least_privilege:
            score += 15
        if request.kubernetes_enabled and not request.network_policy_enabled:
            score += 10
        if request.kubernetes_enabled and not request.namespace_isolation_enabled:
            score += 10
        if request.kubernetes_enabled and not request.image_provenance_checked:
            score += 10
        if request.kubernetes_enabled and not request.runtime_policy_enabled:
            score += 10
        if not request.secrets_externalized:
            score += 20
        if not request.audit_logging_enabled:
            score += 15
        if not request.backup_encryption_enabled:
            score += 10
        if self._is_active_status(request.active_ai_threat_case_status):
            score += 20
        if self._is_active_status(request.active_secret_guard_case_status):
            score += 25
        return min(100, score)

    def _missing_controls(
        self,
        request: CloudKubernetesGuardrailEvaluationRequest,
    ) -> list[str]:
        missing = []
        if not request.secrets_externalized:
            missing.extend(["CLOUD-SECRET-MANAGEMENT", "K8S-SECRET-HANDLING"])
        if not request.audit_logging_enabled:
            missing.extend(["CLOUD-AUDIT-LOGGING", "K8S-AUDIT-EVENTS"])
        if not request.backup_encryption_enabled:
            missing.append("CLOUD-BACKUP-ENCRYPTION")
        if request.kubernetes_enabled and not request.rbac_least_privilege:
            missing.append("K8S-RBAC-LEAST-PRIVILEGE")
        if request.kubernetes_enabled and not request.network_policy_enabled:
            missing.append("K8S-NETWORK-POLICY")
        if request.kubernetes_enabled and not request.namespace_isolation_enabled:
            missing.append("K8S-NAMESPACE-ISOLATION")
        if request.kubernetes_enabled and not request.image_provenance_checked:
            missing.append("K8S-IMAGE-PROVENANCE")
        if request.kubernetes_enabled and not request.runtime_policy_enabled:
            missing.append("K8S-RUNTIME-POLICY")
        if (
            request.active_ai_threat_case_id
            and self._is_active_status(request.active_ai_threat_case_status)
        ) or (
            request.active_secret_guard_case_id
            and self._is_active_status(request.active_secret_guard_case_status)
        ):
            missing.append("K8S-DEPLOYMENT-APPROVAL")
        if request.scenario_id == "custodian_network_boundary_gap":
            missing.append("FUTURE-CUSTODIAN-NETWORK-BOUNDARY")
        return sorted(set(missing))

    def _satisfied_controls(
        self,
        request: CloudKubernetesGuardrailEvaluationRequest,
    ) -> list[str]:
        satisfied = []
        if request.secrets_externalized:
            satisfied.extend(["CLOUD-SECRET-MANAGEMENT", "K8S-SECRET-HANDLING"])
        if request.audit_logging_enabled:
            satisfied.extend(["CLOUD-AUDIT-LOGGING", "K8S-AUDIT-EVENTS"])
        if request.backup_encryption_enabled:
            satisfied.append("CLOUD-BACKUP-ENCRYPTION")
        if request.rbac_least_privilege:
            satisfied.append("K8S-RBAC-LEAST-PRIVILEGE")
        if request.network_policy_enabled:
            satisfied.append("K8S-NETWORK-POLICY")
        if request.namespace_isolation_enabled:
            satisfied.append("K8S-NAMESPACE-ISOLATION")
        if request.image_provenance_checked:
            satisfied.append("K8S-IMAGE-PROVENANCE")
        if request.runtime_policy_enabled:
            satisfied.append("K8S-RUNTIME-POLICY")
        return sorted(set(satisfied))

    def _severity_for_score(
        self,
        risk_score: int,
    ) -> CloudKubernetesGuardrailSeverity:
        if risk_score <= 39:
            return "low"
        if risk_score <= 64:
            return "medium"
        if risk_score <= 84:
            return "high"
        return "critical"

    def _decision_for_score(
        self,
        risk_score: int,
    ) -> CloudKubernetesGuardrailDecision:
        if risk_score <= 39:
            return "allow"
        if risk_score <= 64:
            return "harden"
        if risk_score <= 84:
            return "review_required"
        return "block_deployment"

    def _is_active_status(self, status: str | None) -> bool:
        return (
            status.strip().lower().replace(" ", "_") in ACTIVE_REVIEW_STATUSES
            if status
            else False
        )

    def _recommended_next_actions(
        self,
        *,
        missing_controls: list[str],
        review_case_required: bool,
        deployment_blocked: bool,
    ) -> list[str]:
        actions = []
        if deployment_blocked:
            actions.append("block_future_deployment_until_controls_are_verified")
        if "CLOUD-SECRET-MANAGEMENT" in missing_controls:
            actions.append("externalize_and_protect_secrets")
        if "K8S-RBAC-LEAST-PRIVILEGE" in missing_controls:
            actions.append("enforce_kubernetes_rbac_least_privilege")
        if "K8S-NETWORK-POLICY" in missing_controls:
            actions.append("enable_network_policy")
        if "CLOUD-AUDIT-LOGGING" in missing_controls:
            actions.append("enable_audit_logging")
        if "K8S-IMAGE-PROVENANCE" in missing_controls:
            actions.append("verify_image_provenance")
        if "K8S-RUNTIME-POLICY" in missing_controls:
            actions.append("enable_runtime_policy")
        if "K8S-NAMESPACE-ISOLATION" in missing_controls:
            actions.append("enforce_namespace_isolation")
        if review_case_required:
            actions.extend(
                [
                    "preserve_evidence",
                    "create_human_review_case",
                    "require_security_architecture_approval",
                ]
            )
        actions.append(
            "verify_ai_threat_and_secret_guard_cases_are_mitigated_or_closed"
        )
        return actions


cloud_kubernetes_guardrails_service = CloudKubernetesGuardrailsService()
