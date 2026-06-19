from datetime import datetime, timezone

from app.schemas.custodian_integration_guardrails import (
    CustodianIntegrationGuardrailControl,
    CustodianIntegrationGuardrailDecision,
    CustodianIntegrationGuardrailEvaluationRequest,
    CustodianIntegrationGuardrailEvaluationResponse,
    CustodianIntegrationGuardrailScenario,
    CustodianIntegrationGuardrailSeverity,
)
from app.services.audit_service import audit_service


ACTIVE_REVIEW_STATUSES = {
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
}

SCENARIO_CONTEXT = {
    "custodian_readiness_gap": {
        "base_score": 70,
        "audit_event_id": "AUD-CUSTODIAN-READINESS-GAP",
        "correlation_id": "CORR-CUSTODIAN-READINESS-GAP",
        "review_case_id": "CASE-CUSTODIAN-READINESS-GAP",
        "title": "Future regulated custodian readiness gap",
        "description": (
            "Evaluates whether a future regulated custodian integration has "
            "enough contractual, operational, custody, and risk-boundary "
            "controls to proceed."
        ),
        "required_controls": [
            "CUSTODIAN-REGULATORY-STATUS",
            "CUSTODIAN-ASSET-SEGREGATION",
            "CUSTODIAN-LIABILITY-BOUNDARY",
            "BANK-CUSTODIAN-RESPONSIBILITY-MATRIX",
            "AURORA-CUSTODIAN-BOUNDARY",
        ],
    },
    "custodian_missing_asset_segregation": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
        "correlation_id": "CORR-CUSTODIAN-ASSET-SEGREGATION-GAP",
        "review_case_id": "CASE-CUSTODIAN-ASSET-SEGREGATION-GAP",
        "title": "Custodian asset segregation gap",
        "description": (
            "Evaluates whether customer digital assets would be segregated in "
            "a future custodian operating model."
        ),
        "required_controls": [
            "CUSTODIAN-ASSET-SEGREGATION",
            "CUSTODIAN-AUDIT-REPORTS",
            "CUSTODIAN-RECONCILIATION",
        ],
    },
    "custodian_missing_liability_boundary": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-LIABILITY-BOUNDARY-GAP",
        "correlation_id": "CORR-CUSTODIAN-LIABILITY-BOUNDARY-GAP",
        "review_case_id": "CASE-CUSTODIAN-LIABILITY-BOUNDARY-GAP",
        "title": "Custodian liability boundary gap",
        "description": (
            "Evaluates whether liability and responsibility boundaries are "
            "defined before any future custodian integration."
        ),
        "required_controls": [
            "CUSTODIAN-LIABILITY-BOUNDARY",
            "CUSTODIAN-INSURANCE-COVERAGE",
            "BANK-CUSTODIAN-RESPONSIBILITY-MATRIX",
        ],
    },
    "custodian_missing_sla_contract": {
        "base_score": 80,
        "audit_event_id": "AUD-CUSTODIAN-SLA-CONTRACT-GAP",
        "correlation_id": "CORR-CUSTODIAN-SLA-CONTRACT-GAP",
        "review_case_id": "CASE-CUSTODIAN-SLA-CONTRACT-GAP",
        "title": "Custodian SLA and contract gap",
        "description": (
            "Evaluates whether SLA and contract terms are finalized before a "
            "future regulated custodian integration."
        ),
        "required_controls": [
            "CUSTODIAN-SLA-AND-CONTRACT",
            "CUSTODIAN-INCIDENT-REPORTING",
            "CUSTODIAN-EVIDENCE-EXPORT",
        ],
    },
    "custodian_missing_audit_reports": {
        "base_score": 75,
        "audit_event_id": "AUD-CUSTODIAN-AUDIT-REPORTS-GAP",
        "correlation_id": "CORR-CUSTODIAN-AUDIT-REPORTS-GAP",
        "review_case_id": "CASE-CUSTODIAN-AUDIT-REPORTS-GAP",
        "title": "Custodian audit reports gap",
        "description": (
            "Evaluates whether future custodian assurance reports are available "
            "for compliance and risk review."
        ),
        "required_controls": [
            "CUSTODIAN-AUDIT-REPORTS",
            "CUSTODIAN-EVIDENCE-EXPORT",
            "CUSTODIAN-REGULATORY-REPORTING",
        ],
    },
    "custodian_transfer_limit_gap": {
        "base_score": 80,
        "audit_event_id": "AUD-CUSTODIAN-TRANSFER-LIMIT-GAP",
        "correlation_id": "CORR-CUSTODIAN-TRANSFER-LIMIT-GAP",
        "review_case_id": "CASE-CUSTODIAN-TRANSFER-LIMIT-GAP",
        "title": "Custodian transfer limit gap",
        "description": (
            "Evaluates whether future custodian transfer limits are configured "
            "before any customer-facing integration."
        ),
        "required_controls": [
            "CUSTODIAN-TRANSFER-LIMITS",
            "CUSTODIAN-WITHDRAWAL-APPROVAL",
        ],
    },
    "custodian_withdrawal_approval_gap": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-WITHDRAWAL-APPROVAL-GAP",
        "correlation_id": "CORR-CUSTODIAN-WITHDRAWAL-APPROVAL-GAP",
        "review_case_id": "CASE-CUSTODIAN-WITHDRAWAL-APPROVAL-GAP",
        "title": "Custodian withdrawal approval gap",
        "description": (
            "Evaluates whether future external wallet movements require bank "
            "style approval before custodian execution."
        ),
        "required_controls": [
            "CUSTODIAN-WITHDRAWAL-APPROVAL",
            "CUSTODIAN-TRANSFER-LIMITS",
            "CUSTODIAN-API-ACCESS-CONTROLS",
        ],
    },
    "custodian_api_access_control_gap": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-API-ACCESS-CONTROL-GAP",
        "correlation_id": "CORR-CUSTODIAN-API-ACCESS-CONTROL-GAP",
        "review_case_id": "CASE-CUSTODIAN-API-ACCESS-CONTROL-GAP",
        "title": "Custodian API access control gap",
        "description": (
            "Evaluates whether future custodian API access would be scoped, "
            "approved, monitored, and separated from runtime execution."
        ),
        "required_controls": [
            "CUSTODIAN-API-ACCESS-CONTROLS",
            "CUSTODIAN-EVIDENCE-EXPORT",
            "AURORA-CUSTODIAN-BOUNDARY",
        ],
    },
    "custodian_key_management_boundary_gap": {
        "base_score": 90,
        "audit_event_id": "AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        "correlation_id": "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        "review_case_id": "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        "title": "Custodian key management boundary gap",
        "description": (
            "Evaluates whether Aurora's future boundary with custodian key "
            "management is explicit and excludes private key custody."
        ),
        "required_controls": [
            "CUSTODIAN-KEY-MANAGEMENT-BOUNDARY",
            "AURORA-CUSTODIAN-BOUNDARY",
            "SECRET-GUARD-CASE-CLEARANCE",
        ],
    },
    "custodian_incident_reporting_gap": {
        "base_score": 75,
        "audit_event_id": "AUD-CUSTODIAN-INCIDENT-REPORTING-GAP",
        "correlation_id": "CORR-CUSTODIAN-INCIDENT-REPORTING-GAP",
        "review_case_id": "CASE-CUSTODIAN-INCIDENT-REPORTING-GAP",
        "title": "Custodian incident reporting gap",
        "description": (
            "Evaluates whether future custodian incident reporting obligations "
            "are defined for bank risk operations."
        ),
        "required_controls": [
            "CUSTODIAN-INCIDENT-REPORTING",
            "CUSTODIAN-EVIDENCE-EXPORT",
        ],
    },
    "custodian_reconciliation_gap": {
        "base_score": 75,
        "audit_event_id": "AUD-CUSTODIAN-RECONCILIATION-GAP",
        "correlation_id": "CORR-CUSTODIAN-RECONCILIATION-GAP",
        "review_case_id": "CASE-CUSTODIAN-RECONCILIATION-GAP",
        "title": "Custodian reconciliation gap",
        "description": (
            "Evaluates whether future custodian balances and Aurora records "
            "have a reconciliation process."
        ),
        "required_controls": [
            "CUSTODIAN-RECONCILIATION",
            "CUSTODIAN-AUDIT-REPORTS",
            "CUSTODIAN-REGULATORY-REPORTING",
        ],
    },
    "integration_with_active_ai_threat_case": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-ACTIVE-AI-THREAT-CASE",
        "correlation_id": "CORR-CUSTODIAN-ACTIVE-AI-THREAT-CASE",
        "review_case_id": "CASE-CUSTODIAN-ACTIVE-AI-THREAT-CASE",
        "title": "Custodian integration with active AI Threat Defense case",
        "description": (
            "Evaluates whether future custodian integration should pause while "
            "an AI Threat Defense case remains active."
        ),
        "required_controls": ["AI-THREAT-CASE-CLEARANCE"],
    },
    "integration_with_active_secret_guard_case": {
        "base_score": 90,
        "audit_event_id": "AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        "correlation_id": "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        "review_case_id": "CASE-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        "title": "Custodian integration with active Secret Exposure Guard case",
        "description": (
            "Evaluates whether future custodian integration should remain "
            "blocked while a Secret Exposure Guard case is active."
        ),
        "required_controls": ["SECRET-GUARD-CASE-CLEARANCE"],
    },
    "integration_with_active_cloud_k8s_guard_case": {
        "base_score": 85,
        "audit_event_id": "AUD-CUSTODIAN-ACTIVE-CLOUD-K8S-GUARD-CASE",
        "correlation_id": "CORR-CUSTODIAN-ACTIVE-CLOUD-K8S-GUARD-CASE",
        "review_case_id": "CASE-CUSTODIAN-ACTIVE-CLOUD-K8S-GUARD-CASE",
        "title": "Custodian integration with active cloud or Kubernetes guard case",
        "description": (
            "Evaluates whether future custodian integration should pause while "
            "cloud or Kubernetes guardrails remain unresolved."
        ),
        "required_controls": ["FUTURE-CLOUD-K8S-BOUNDARY"],
    },
}


class CustodianIntegrationGuardrailsService:
    """Deterministic future custodian integration guardrail service."""

    def list_controls(self) -> list[CustodianIntegrationGuardrailControl]:
        return [
            self._control("CUSTODIAN-REGULATORY-STATUS", "Custodian regulatory status", "compliance", "Future custodians must have documented regulatory status."),
            self._control("CUSTODIAN-ASSET-SEGREGATION", "Custodian asset segregation", "custody", "Customer assets must be segregated in the future custodian model."),
            self._control("CUSTODIAN-LIABILITY-BOUNDARY", "Custodian liability boundary", "contract", "Liability boundaries must be defined before integration."),
            self._control("CUSTODIAN-SLA-AND-CONTRACT", "Custodian SLA and contract", "contract", "Service levels and contract terms must be finalized."),
            self._control("CUSTODIAN-AUDIT-REPORTS", "Custodian audit reports", "audit", "Independent audit and assurance reports must be available for review."),
            self._control("CUSTODIAN-INSURANCE-COVERAGE", "Custodian insurance coverage", "risk", "Insurance coverage must be verified for the future custody model."),
            self._control("CUSTODIAN-TRANSFER-LIMITS", "Custodian transfer limits", "operations", "Transfer limits must be configured before customer-facing use."),
            self._control("CUSTODIAN-WITHDRAWAL-APPROVAL", "Custodian withdrawal approval", "operations", "Withdrawals must require controlled approval before custodian execution."),
            self._control("CUSTODIAN-API-ACCESS-CONTROLS", "Custodian API access controls", "technical", "Future API access must be scoped, approved, and monitored."),
            self._control("CUSTODIAN-KEY-MANAGEMENT-BOUNDARY", "Custodian key management boundary", "custody", "Aurora must not generate, store, or control custodian private keys."),
            self._control("CUSTODIAN-INCIDENT-REPORTING", "Custodian incident reporting", "operations", "Incident reporting obligations must be defined."),
            self._control("CUSTODIAN-RECONCILIATION", "Custodian reconciliation", "operations", "Custodian and Aurora records must have a reconciliation process."),
            self._control("CUSTODIAN-EVIDENCE-EXPORT", "Custodian evidence export", "audit", "Future custodian evidence exports must support review and compliance."),
            self._control("CUSTODIAN-REGULATORY-REPORTING", "Custodian regulatory reporting", "compliance", "Regulatory reporting duties must be defined."),
            self._control("BANK-CUSTODIAN-RESPONSIBILITY-MATRIX", "Bank custodian responsibility matrix", "governance", "Bank and custodian responsibilities must be documented."),
            self._control("AURORA-CUSTODIAN-BOUNDARY", "Aurora custodian boundary", "governance", "Aurora's boundary with any future custodian must be explicit."),
            self._control("FUTURE-CLOUD-K8S-BOUNDARY", "Future cloud and Kubernetes boundary", "technical", "Future cloud and Kubernetes boundaries must be verified before custodian integration."),
            self._control("AI-THREAT-CASE-CLEARANCE", "AI Threat Defense case clearance", "risk", "Active AI Threat Defense cases must be mitigated or closed."),
            self._control("SECRET-GUARD-CASE-CLEARANCE", "Secret Exposure Guard case clearance", "risk", "Active Secret Exposure Guard cases must be mitigated or closed."),
        ]

    def list_scenarios(self) -> list[CustodianIntegrationGuardrailScenario]:
        return [
            CustodianIntegrationGuardrailScenario(
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
        request: CustodianIntegrationGuardrailEvaluationRequest,
    ) -> CustodianIntegrationGuardrailEvaluationResponse:
        context = SCENARIO_CONTEXT.get(
            request.scenario_id,
            SCENARIO_CONTEXT["custodian_readiness_gap"],
        )
        missing_controls = self._missing_controls(request)
        satisfied_controls = self._satisfied_controls(request)
        risk_score = self._risk_score(request, context["base_score"])
        severity = self._severity_for_score(risk_score)
        decision = self._decision_for_score(risk_score)

        if (
            request.scenario_id == "integration_with_active_secret_guard_case"
            and self._is_active_status(request.active_secret_guard_case_status)
        ):
            decision = "block_integration"
        if (
            request.scenario_id == "custodian_key_management_boundary_gap"
            and not request.key_management_boundary_defined
        ):
            decision = "block_integration"
        if (
            request.scenario_id == "custodian_missing_asset_segregation"
            and not request.asset_segregation_confirmed
        ):
            decision = "block_integration"
        if (
            request.scenario_id == "custodian_withdrawal_approval_gap"
            and not request.withdrawal_approval_required
        ):
            decision = "block_integration"

        integration_blocked = decision == "block_integration"
        evidence_package_ready = severity in {"medium", "high", "critical"}
        review_case_required = severity in {"high", "critical"}
        review_case_id = context["review_case_id"] if review_case_required else None
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=context["audit_event_id"],
            actor_id=request.reviewer_id,
            actor_type="staff" if request.reviewer_id != "system" else "service",
            source_module="custodian_integration_guardrails",
            action="evaluate_future_custodian_integration_guardrails",
            object_type="future_custodian_integration",
            object_id=request.scenario_id,
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=(
                "Future regulated custodian integration guardrails evaluated by "
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
                "integration_target": request.integration_target,
                "environment": request.environment,
                "missing_controls": missing_controls,
                "satisfied_controls": satisfied_controls,
                "active_ai_threat_case_id": request.active_ai_threat_case_id,
                "active_secret_guard_case_id": request.active_secret_guard_case_id,
                "active_cloud_k8s_guard_case_id": (
                    request.active_cloud_k8s_guard_case_id
                ),
            },
        )

        return CustodianIntegrationGuardrailEvaluationResponse(
            scenario_id=request.scenario_id,
            integration_target=request.integration_target,
            environment=request.environment,
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            integration_guard_applied=True,
            integration_blocked=integration_blocked,
            required_controls=list(context["required_controls"]),
            missing_controls=missing_controls,
            satisfied_controls=satisfied_controls,
            linked_ai_threat_case_id=request.active_ai_threat_case_id,
            linked_secret_guard_case_id=request.active_secret_guard_case_id,
            linked_cloud_k8s_guard_case_id=request.active_cloud_k8s_guard_case_id,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            evidence_package_ready=evidence_package_ready,
            review_case_required=review_case_required,
            review_case_id=review_case_id,
            recommended_next_actions=self._recommended_next_actions(
                missing_controls=missing_controls,
                review_case_required=review_case_required,
                integration_blocked=integration_blocked,
            ),
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _control(
        self,
        control_id: str,
        title: str,
        control_layer: str,
        description: str,
    ) -> CustodianIntegrationGuardrailControl:
        return CustodianIntegrationGuardrailControl(
            control_id=control_id,
            title=title,
            control_layer=control_layer,
            description=description,
            enabled=True,
        )

    def _risk_score(
        self,
        request: CustodianIntegrationGuardrailEvaluationRequest,
        base_score: int,
    ) -> int:
        score = base_score
        if not request.custodian_regulated:
            score += 20
        if not request.asset_segregation_confirmed:
            score += 20
        if not request.liability_boundary_defined:
            score += 20
        if not request.sla_contract_signed:
            score += 15
        if not request.audit_reports_available:
            score += 15
        if not request.insurance_coverage_confirmed:
            score += 10
        if not request.transfer_limits_configured:
            score += 15
        if not request.withdrawal_approval_required:
            score += 20
        if not request.api_access_controls_defined:
            score += 20
        if not request.key_management_boundary_defined:
            score += 25
        if not request.incident_reporting_defined:
            score += 10
        if not request.reconciliation_defined:
            score += 10
        if not request.evidence_export_available:
            score += 10
        if not request.regulatory_reporting_defined:
            score += 15
        if not request.responsibility_matrix_defined:
            score += 15
        if not request.aurora_custodian_boundary_defined:
            score += 20
        if not request.future_cloud_k8s_boundary_defined:
            score += 15
        if self._is_active_status(request.active_ai_threat_case_status):
            score += 20
        if self._is_active_status(request.active_secret_guard_case_status):
            score += 25
        if self._is_active_status(request.active_cloud_k8s_guard_case_status):
            score += 20
        return min(100, score)

    def _missing_controls(
        self,
        request: CustodianIntegrationGuardrailEvaluationRequest,
    ) -> list[str]:
        checks = [
            ("CUSTODIAN-REGULATORY-STATUS", request.custodian_regulated),
            ("CUSTODIAN-ASSET-SEGREGATION", request.asset_segregation_confirmed),
            ("CUSTODIAN-LIABILITY-BOUNDARY", request.liability_boundary_defined),
            ("CUSTODIAN-SLA-AND-CONTRACT", request.sla_contract_signed),
            ("CUSTODIAN-AUDIT-REPORTS", request.audit_reports_available),
            ("CUSTODIAN-INSURANCE-COVERAGE", request.insurance_coverage_confirmed),
            ("CUSTODIAN-TRANSFER-LIMITS", request.transfer_limits_configured),
            ("CUSTODIAN-WITHDRAWAL-APPROVAL", request.withdrawal_approval_required),
            ("CUSTODIAN-API-ACCESS-CONTROLS", request.api_access_controls_defined),
            (
                "CUSTODIAN-KEY-MANAGEMENT-BOUNDARY",
                request.key_management_boundary_defined,
            ),
            ("CUSTODIAN-INCIDENT-REPORTING", request.incident_reporting_defined),
            ("CUSTODIAN-RECONCILIATION", request.reconciliation_defined),
            ("CUSTODIAN-EVIDENCE-EXPORT", request.evidence_export_available),
            (
                "CUSTODIAN-REGULATORY-REPORTING",
                request.regulatory_reporting_defined,
            ),
            (
                "BANK-CUSTODIAN-RESPONSIBILITY-MATRIX",
                request.responsibility_matrix_defined,
            ),
            (
                "AURORA-CUSTODIAN-BOUNDARY",
                request.aurora_custodian_boundary_defined,
            ),
            (
                "FUTURE-CLOUD-K8S-BOUNDARY",
                request.future_cloud_k8s_boundary_defined,
            ),
        ]
        missing = [control for control, satisfied in checks if not satisfied]
        if request.active_ai_threat_case_id and self._is_active_status(
            request.active_ai_threat_case_status
        ):
            missing.append("AI-THREAT-CASE-CLEARANCE")
        if request.active_secret_guard_case_id and self._is_active_status(
            request.active_secret_guard_case_status
        ):
            missing.append("SECRET-GUARD-CASE-CLEARANCE")
        if request.active_cloud_k8s_guard_case_id and self._is_active_status(
            request.active_cloud_k8s_guard_case_status
        ):
            missing.append("FUTURE-CLOUD-K8S-BOUNDARY")
        return sorted(set(missing))

    def _satisfied_controls(
        self,
        request: CustodianIntegrationGuardrailEvaluationRequest,
    ) -> list[str]:
        checks = [
            ("CUSTODIAN-REGULATORY-STATUS", request.custodian_regulated),
            ("CUSTODIAN-ASSET-SEGREGATION", request.asset_segregation_confirmed),
            ("CUSTODIAN-LIABILITY-BOUNDARY", request.liability_boundary_defined),
            ("CUSTODIAN-SLA-AND-CONTRACT", request.sla_contract_signed),
            ("CUSTODIAN-AUDIT-REPORTS", request.audit_reports_available),
            ("CUSTODIAN-INSURANCE-COVERAGE", request.insurance_coverage_confirmed),
            ("CUSTODIAN-TRANSFER-LIMITS", request.transfer_limits_configured),
            ("CUSTODIAN-WITHDRAWAL-APPROVAL", request.withdrawal_approval_required),
            ("CUSTODIAN-API-ACCESS-CONTROLS", request.api_access_controls_defined),
            (
                "CUSTODIAN-KEY-MANAGEMENT-BOUNDARY",
                request.key_management_boundary_defined,
            ),
            ("CUSTODIAN-INCIDENT-REPORTING", request.incident_reporting_defined),
            ("CUSTODIAN-RECONCILIATION", request.reconciliation_defined),
            ("CUSTODIAN-EVIDENCE-EXPORT", request.evidence_export_available),
            (
                "CUSTODIAN-REGULATORY-REPORTING",
                request.regulatory_reporting_defined,
            ),
            (
                "BANK-CUSTODIAN-RESPONSIBILITY-MATRIX",
                request.responsibility_matrix_defined,
            ),
            (
                "AURORA-CUSTODIAN-BOUNDARY",
                request.aurora_custodian_boundary_defined,
            ),
            (
                "FUTURE-CLOUD-K8S-BOUNDARY",
                request.future_cloud_k8s_boundary_defined,
            ),
        ]
        return sorted({control for control, satisfied in checks if satisfied})

    def _severity_for_score(
        self,
        risk_score: int,
    ) -> CustodianIntegrationGuardrailSeverity:
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
    ) -> CustodianIntegrationGuardrailDecision:
        if risk_score <= 39:
            return "allow"
        if risk_score <= 64:
            return "harden"
        if risk_score <= 84:
            return "review_required"
        return "block_integration"

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
        integration_blocked: bool,
    ) -> list[str]:
        actions = []
        if integration_blocked:
            actions.append(
                "block_future_custodian_integration_until_controls_are_verified"
            )
        control_actions = {
            "CUSTODIAN-REGULATORY-STATUS": "confirm_custodian_regulatory_status",
            "CUSTODIAN-ASSET-SEGREGATION": "verify_asset_segregation",
            "CUSTODIAN-LIABILITY-BOUNDARY": "define_liability_boundary",
            "CUSTODIAN-SLA-AND-CONTRACT": "finalize_sla_and_contract_terms",
            "CUSTODIAN-AUDIT-REPORTS": "obtain_audit_reports",
            "CUSTODIAN-INSURANCE-COVERAGE": "verify_insurance_coverage",
            "CUSTODIAN-TRANSFER-LIMITS": "configure_transfer_limits",
            "CUSTODIAN-WITHDRAWAL-APPROVAL": "enforce_withdrawal_approval",
            "CUSTODIAN-API-ACCESS-CONTROLS": "define_api_access_controls",
            "CUSTODIAN-KEY-MANAGEMENT-BOUNDARY": "define_key_management_boundary",
            "CUSTODIAN-INCIDENT-REPORTING": "define_incident_reporting",
            "CUSTODIAN-RECONCILIATION": "define_reconciliation_process",
            "CUSTODIAN-EVIDENCE-EXPORT": "enable_evidence_export",
            "CUSTODIAN-REGULATORY-REPORTING": "define_regulatory_reporting",
            "BANK-CUSTODIAN-RESPONSIBILITY-MATRIX": (
                "finalize_bank_custodian_responsibility_matrix"
            ),
            "AURORA-CUSTODIAN-BOUNDARY": "define_aurora_custodian_boundary",
            "FUTURE-CLOUD-K8S-BOUNDARY": "verify_cloud_k8s_boundary",
        }
        for control in missing_controls:
            action = control_actions.get(control)
            if action:
                actions.append(action)
        actions.append(
            "verify_ai_threat_secret_guard_and_cloud_cases_are_mitigated_or_closed"
        )
        if review_case_required:
            actions.extend(
                [
                    "create_human_review_case",
                    "require_security_architecture_approval",
                ]
            )
        return actions


custodian_integration_guardrails_service = CustodianIntegrationGuardrailsService()
