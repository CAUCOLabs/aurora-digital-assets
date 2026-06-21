from datetime import datetime, timezone

from app.schemas.external_partner_agent_readiness import (
    CustodianAgentReadinessRequest,
    ExternalPartnerReadinessPreviewRequest,
    ExternalPartnerReadinessRequest,
    ExternalPartnerReadinessResponse,
    PartnerTypeDefinition,
    ReadinessControlDefinition,
)
from app.services.audit_service import audit_service


PARTNER_TYPES = {
    "regulated_custodian": "Regulated future custody partner metadata review.",
    "bank_partner": "Bank partner or regulated financial institution metadata review.",
    "compliance_vendor": "Compliance tooling or service vendor metadata review.",
    "security_vendor": "Security tooling or advisory vendor metadata review.",
    "reporting_vendor": "Reporting or data export vendor metadata review.",
    "cloud_infrastructure_partner": "Cloud or infrastructure partner metadata review.",
    "identity_provider": "Identity provider partner metadata review.",
    "audit_partner": "External audit partner metadata review.",
    "liquidity_provider": "Liquidity provider metadata review without execution.",
    "external_ai_agent_vendor": "External AI agent vendor metadata review.",
    "internal_partner_agent": "Internal partner agent readiness review.",
}

CONTROL_GROUPS = {
    "legal_and_contractual": [
        "legal_entity_verified",
        "regulatory_status_verified",
        "responsibility_matrix_defined",
        "data_processing_agreement_defined",
        "liability_boundary_defined",
        "audit_rights_defined",
        "incident_reporting_defined",
        "sla_defined",
    ],
    "security_and_access": [
        "security_assessment_completed",
        "penetration_test_attestation_available",
        "soc2_or_iso27001_available",
        "access_control_model_defined",
        "least_privilege_enforced",
        "mfa_required",
        "credential_boundary_defined",
        "no_raw_secret_exchange_confirmed",
        "credential_rotation_policy_defined",
        "api_scope_limited",
        "rate_limits_defined",
        "webhook_signing_defined",
        "ip_allowlisting_defined",
        "network_segmentation_defined",
        "monitoring_and_alerting_defined",
    ],
    "operational_resilience": [
        "operational_resilience_review_completed",
        "business_continuity_plan_available",
        "disaster_recovery_plan_available",
    ],
    "data_and_privacy": [
        "data_retention_policy_defined",
        "data_residency_defined",
        "privacy_impact_assessment_completed",
    ],
    "audit_and_evidence": [
        "audit_log_export_available",
        "evidence_export_available",
        "review_case_workflow_defined",
        "revocation_workflow_defined",
    ],
    "agent_governance": [
        "human_approval_required_for_sensitive_actions",
        "agent_passport_required",
        "agent_permissions_defined",
        "agent_policy_engine_required",
        "agent_abuse_detection_required",
        "agent_sensitive_action_guard_required",
        "agent_revocation_required",
    ],
    "custodian_specific": [
        "custodian_asset_segregation_confirmed",
        "custodian_key_management_boundary_defined",
        "custodian_withdrawal_policy_defined",
        "custodian_reconciliation_defined",
        "custodian_insurance_coverage_confirmed",
        "custodian_regulatory_reporting_defined",
    ],
}

CRITICAL_CONTROLS = {
    "legal_entity_verified",
    "responsibility_matrix_defined",
    "liability_boundary_defined",
    "incident_reporting_defined",
    "security_assessment_completed",
    "access_control_model_defined",
    "least_privilege_enforced",
    "credential_boundary_defined",
    "no_raw_secret_exchange_confirmed",
    "human_approval_required_for_sensitive_actions",
    "agent_passport_required",
    "agent_permissions_defined",
    "agent_policy_engine_required",
    "agent_abuse_detection_required",
    "agent_sensitive_action_guard_required",
    "agent_revocation_required",
}
REGULATORY_CRITICAL_PARTNER_TYPES = {"regulated_custodian", "bank_partner"}
CUSTODIAN_CRITICAL_CONTROLS = {
    "custodian_asset_segregation_confirmed",
    "custodian_key_management_boundary_defined",
    "custodian_withdrawal_policy_defined",
    "custodian_reconciliation_defined",
    "custodian_regulatory_reporting_defined",
}
HIGH_CONTROLS = {
    "data_processing_agreement_defined",
    "audit_rights_defined",
    "sla_defined",
    "penetration_test_attestation_available",
    "soc2_or_iso27001_available",
    "operational_resilience_review_completed",
    "business_continuity_plan_available",
    "disaster_recovery_plan_available",
    "credential_rotation_policy_defined",
    "api_scope_limited",
    "rate_limits_defined",
    "webhook_signing_defined",
    "monitoring_and_alerting_defined",
    "audit_log_export_available",
    "evidence_export_available",
    "review_case_workflow_defined",
    "revocation_workflow_defined",
    "custodian_insurance_coverage_confirmed",
}
PRODUCTION_LIKE_ENVIRONMENTS = {"production", "future_production"}

READINESS_SAFETY_NOTICE = (
    "Local deterministic readiness evaluation only. No partner onboarded, no "
    "external access granted, no real custodian API access, no credentials "
    "created or exchanged, no secrets stored or exposed, and no custody, "
    "blockchain, banking, or withdrawal execution occurred."
)


class ExternalPartnerAgentReadinessService:
    """Deterministic readiness evaluator for partner and custodian-facing agents."""

    def list_controls(self) -> list[ReadinessControlDefinition]:
        return [
            ReadinessControlDefinition(
                control_id=control,
                group=group,
                criticality=self._criticality(control),
                description=self._description(control),
            )
            for group, controls in CONTROL_GROUPS.items()
            for control in controls
        ]

    def list_partner_types(self) -> list[PartnerTypeDefinition]:
        return [
            PartnerTypeDefinition(
                partner_type=partner_type,
                description=description,
            )
            for partner_type, description in PARTNER_TYPES.items()
        ]

    def evaluate(
        self,
        request: ExternalPartnerReadinessRequest,
    ) -> ExternalPartnerReadinessResponse:
        partner_id = self._normalize_id(request.partner_id, "PARTNER")
        partner_type = request.partner_type.strip().lower()
        environment = request.environment.strip().lower() or "local"
        scope = request.intended_integration_scope.strip().lower()
        if partner_type not in PARTNER_TYPES:
            return self._build_response(
                request=request,
                partner_id=partner_id,
                partner_type=partner_type or "unknown",
                environment=environment,
                scope=scope,
                readiness_score=0,
                readiness_decision="insufficient_evidence",
                readiness_level="blocked",
                missing_controls=[],
                failed_controls=[],
                satisfied_controls=[],
                critical_blockers=["unknown_partner_type"],
                conditional_requirements=[
                    "verify_partner_type_before_readiness_review"
                ],
            )

        missing, failed, satisfied = self._control_status(request.controls, partner_type)
        critical_blockers = self._critical_blockers(
            failed=failed,
            partner_type=partner_type,
            linked_agent_abuse_audit_event_id=request.linked_agent_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            environment=environment,
        )
        score = self._score(
            failed_controls=failed,
            partner_type=partner_type,
            linked_agent_abuse_audit_event_id=request.linked_agent_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            environment=environment,
            scope=scope,
        )
        decision = self._decision(
            score=score,
            partner_type=partner_type,
            failed_controls=failed,
            critical_blockers=critical_blockers,
            linked_agent_abuse_audit_event_id=request.linked_agent_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            environment=environment,
        )
        return self._build_response(
            request=request,
            partner_id=partner_id,
            partner_type=partner_type,
            environment=environment,
            scope=scope,
            readiness_score=score,
            readiness_decision=decision,
            readiness_level=self._readiness_level(score),
            missing_controls=missing,
            failed_controls=failed,
            satisfied_controls=satisfied,
            critical_blockers=critical_blockers,
            conditional_requirements=self._conditional_requirements(decision, failed),
        )

    def evaluate_custodian_agent(
        self,
        request: CustodianAgentReadinessRequest,
    ) -> ExternalPartnerReadinessResponse:
        return self.evaluate(
            ExternalPartnerReadinessRequest(
                partner_id=request.partner_id,
                partner_name=request.partner_name,
                partner_type="regulated_custodian",
                environment=request.environment,
                intended_integration_scope="custodian_agent_metadata_review",
                agent_id=request.agent_id,
                agent_type="custodian_integration_agent",
                controls=request.controls,
                linked_agent_passport_id=request.linked_agent_passport_id,
                linked_agent_policy_audit_event_id=(
                    request.linked_agent_policy_audit_event_id
                ),
                linked_agent_abuse_audit_event_id=(
                    request.linked_agent_abuse_audit_event_id
                ),
                linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
                linked_review_case_id=request.linked_review_case_id,
                reviewer_id=request.reviewer_id,
            )
        )

    def readiness_preview(
        self,
        request: ExternalPartnerReadinessPreviewRequest,
    ) -> ExternalPartnerReadinessResponse:
        return self.evaluate(
            ExternalPartnerReadinessRequest(
                partner_id="PREVIEW-PARTNER",
                partner_name="Readiness Preview",
                partner_type=request.partner_type,
                environment=request.environment,
                intended_integration_scope=request.intended_integration_scope,
                controls=request.controls,
                reviewer_id=request.reviewer_id,
            )
        )

    def _build_response(
        self,
        *,
        request: ExternalPartnerReadinessRequest,
        partner_id: str,
        partner_type: str,
        environment: str,
        scope: str,
        readiness_score: int,
        readiness_decision: str,
        readiness_level: str,
        missing_controls: list[str],
        failed_controls: list[str],
        satisfied_controls: list[str],
        critical_blockers: list[str],
        conditional_requirements: list[str],
    ) -> ExternalPartnerReadinessResponse:
        flags = self._blocking_flags(
            partner_type=partner_type,
            decision=readiness_decision,
            failed_controls=failed_controls,
            linked_agent_abuse_audit_event_id=request.linked_agent_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
        )
        audit_event_id = self._audit_event_id(partner_id)
        correlation_id = self._correlation_id(partner_id)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="external_partner_agent_readiness",
            action="evaluate_external_partner_agent_readiness",
            object_type="external_partner_readiness",
            object_id=partner_id,
            decision=readiness_decision,
            severity=readiness_level if readiness_level != "blocked" else "critical",
            risk_score=100 - readiness_score,
            summary=(
                "External partner agent readiness evaluated in local deterministic "
                "prototype."
            ),
            correlation_id=correlation_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "partner_name": request.partner_name,
                "partner_type": partner_type,
                "environment": environment,
                "intended_integration_scope": scope,
                "agent_id": request.agent_id,
                "agent_type": request.agent_type,
                "agent_correlation_id": self._agent_correlation_id(request.agent_id),
                "missing_controls": missing_controls,
                "failed_controls": failed_controls,
                "critical_blockers": critical_blockers,
                "safety_notice": READINESS_SAFETY_NOTICE,
            },
        )
        return ExternalPartnerReadinessResponse(
            partner_id=partner_id,
            partner_name=request.partner_name,
            partner_type=partner_type,
            environment=environment,
            intended_integration_scope=scope,
            agent_id=request.agent_id,
            readiness_decision=readiness_decision,
            readiness_score=readiness_score,
            readiness_level=readiness_level,
            missing_controls=missing_controls,
            failed_controls=failed_controls,
            satisfied_controls=satisfied_controls,
            critical_blockers=critical_blockers,
            conditional_requirements=conditional_requirements,
            sensitive_operations_blocked=flags["sensitive_operations_blocked"],
            external_access_blocked=flags["external_access_blocked"],
            custodian_access_blocked=flags["custodian_access_blocked"],
            secret_exchange_blocked=flags["secret_exchange_blocked"],
            human_review_required=readiness_decision != "ready_for_internal_review",
            evidence_required=readiness_decision != "ready_for_internal_review",
            review_case_required=readiness_decision
            not in {"ready_for_internal_review", "ready_with_conditions"},
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            linked_agent_passport_id=request.linked_agent_passport_id,
            linked_agent_policy_audit_event_id=request.linked_agent_policy_audit_event_id,
            linked_agent_abuse_audit_event_id=request.linked_agent_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_review_case_id=request.linked_review_case_id,
            recommended_next_actions=self._recommended_next_actions(
                readiness_decision,
                failed_controls,
                request.linked_agent_abuse_audit_event_id,
                request.linked_revocation_audit_event_id,
            ),
            safety_notice=READINESS_SAFETY_NOTICE,
            created_at=created_at,
        )

    def _control_status(
        self,
        controls: dict[str, bool],
        partner_type: str,
    ) -> tuple[list[str], list[str], list[str]]:
        required = set(CRITICAL_CONTROLS | HIGH_CONTROLS)
        if partner_type in REGULATORY_CRITICAL_PARTNER_TYPES:
            required.add("regulatory_status_verified")
        if partner_type == "regulated_custodian":
            required.update(CUSTODIAN_CRITICAL_CONTROLS)
        missing = sorted(control for control in required if control not in controls)
        failed = sorted(control for control, passed in controls.items() if not passed)
        satisfied = sorted(control for control, passed in controls.items() if passed)
        return missing, failed, satisfied

    def _critical_blockers(
        self,
        *,
        failed: list[str],
        partner_type: str,
        linked_agent_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
        environment: str,
    ) -> list[str]:
        blockers = [
            control
            for control in failed
            if control in CRITICAL_CONTROLS
            or (
                partner_type in REGULATORY_CRITICAL_PARTNER_TYPES
                and control == "regulatory_status_verified"
            )
            or (
                partner_type == "regulated_custodian"
                and control in CUSTODIAN_CRITICAL_CONTROLS
            )
        ]
        if linked_agent_abuse_audit_event_id:
            blockers.append("linked_agent_abuse_audit_event")
        if linked_revocation_audit_event_id:
            blockers.append("linked_revocation_audit_event")
        if environment in PRODUCTION_LIKE_ENVIRONMENTS and blockers:
            blockers.append("production_environment_with_missing_critical_controls")
        return self._dedupe(blockers)

    def _score(
        self,
        *,
        failed_controls: list[str],
        partner_type: str,
        linked_agent_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
        environment: str,
        scope: str,
    ) -> int:
        score = 100
        for control in failed_controls:
            if (
                control in CRITICAL_CONTROLS
                or (
                    partner_type == "regulated_custodian"
                    and control in CUSTODIAN_CRITICAL_CONTROLS
                )
                or (
                    partner_type in REGULATORY_CRITICAL_PARTNER_TYPES
                    and control == "regulatory_status_verified"
                )
            ):
                score -= 20
            elif control in HIGH_CONTROLS:
                score -= 12
            else:
                score -= 6
        if linked_revocation_audit_event_id:
            score -= 25
        if linked_agent_abuse_audit_event_id:
            score -= 25
        if environment in PRODUCTION_LIKE_ENVIRONMENTS:
            score -= 15
        if "sensitive_operations" in scope:
            score -= 15
        if "custodian_api_access" in scope:
            score -= 20
        if "secret_exchange" in scope:
            score -= 30
        return max(score, 0)

    def _decision(
        self,
        *,
        score: int,
        partner_type: str,
        failed_controls: list[str],
        critical_blockers: list[str],
        linked_agent_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
        environment: str,
    ) -> str:
        if linked_agent_abuse_audit_event_id or linked_revocation_audit_event_id:
            return "block_external_access"
        if {
            "no_raw_secret_exchange_confirmed",
            "credential_boundary_defined",
        }.intersection(failed_controls):
            return "block_secret_exchange"
        if {
            "human_approval_required_for_sensitive_actions",
            "agent_sensitive_action_guard_required",
        }.intersection(failed_controls):
            return "block_sensitive_operations"
        if "agent_revocation_required" in failed_controls:
            return "block_external_access"
        if (
            partner_type == "regulated_custodian"
            and "custodian_key_management_boundary_defined" in failed_controls
        ):
            return "block_custodian_agent_readiness"
        if environment in PRODUCTION_LIKE_ENVIRONMENTS and critical_blockers:
            return "block_partner_onboarding"
        if score < 40:
            return "block_partner_onboarding"
        if score < 65:
            return "requires_remediation"
        if score < 85:
            return "ready_with_conditions"
        if critical_blockers:
            return "requires_remediation"
        return "ready_for_internal_review"

    def _blocking_flags(
        self,
        *,
        partner_type: str,
        decision: str,
        failed_controls: list[str],
        linked_agent_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> dict[str, bool]:
        secret = bool(
            {
                "no_raw_secret_exchange_confirmed",
                "credential_boundary_defined",
            }.intersection(failed_controls)
        ) or decision == "block_secret_exchange"
        custodian = (
            partner_type == "regulated_custodian"
            and bool(CUSTODIAN_CRITICAL_CONTROLS.intersection(failed_controls))
        ) or decision == "block_custodian_agent_readiness"
        sensitive = bool(
            {
                "human_approval_required_for_sensitive_actions",
                "agent_sensitive_action_guard_required",
            }.intersection(failed_controls)
        ) or decision == "block_sensitive_operations"
        external = (
            decision
            in {
                "block_external_access",
                "block_partner_onboarding",
                "block_secret_exchange",
            }
            or bool(linked_agent_abuse_audit_event_id)
            or bool(linked_revocation_audit_event_id)
        )
        return {
            "secret_exchange_blocked": secret,
            "custodian_access_blocked": custodian,
            "sensitive_operations_blocked": sensitive,
            "external_access_blocked": external,
        }

    def _conditional_requirements(
        self,
        decision: str,
        failed_controls: list[str],
    ) -> list[str]:
        requirements = [f"remediate_{control}" for control in failed_controls]
        if decision in {
            "ready_with_conditions",
            "requires_remediation",
            "block_partner_onboarding",
            "block_custodian_agent_readiness",
        }:
            requirements.append("complete_human_readiness_review")
        return self._dedupe(requirements)

    def _recommended_next_actions(
        self,
        decision: str,
        failed_controls: list[str],
        linked_agent_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> list[str]:
        actions = ["preserve_readiness_audit_trail"]
        if decision == "ready_for_internal_review":
            actions.append("route_to_internal_readiness_review_no_access_granted")
        if decision == "ready_with_conditions":
            actions.append("document_conditions_before_any_future_integration")
        if failed_controls:
            actions.append("remediate_missing_controls")
        if linked_agent_abuse_audit_event_id:
            actions.append("review_agent_abuse_detection")
        if linked_revocation_audit_event_id:
            actions.append("review_agent_revocation_status")
        if decision.startswith("block_") or decision == "requires_remediation":
            actions.append("create_review_case")
        return self._dedupe(actions)

    def _readiness_level(self, score: int) -> str:
        if score >= 85:
            return "high"
        if score >= 65:
            return "medium"
        if score >= 40:
            return "low"
        return "blocked"

    def _criticality(self, control: str) -> str:
        if control in CRITICAL_CONTROLS or control in CUSTODIAN_CRITICAL_CONTROLS:
            return "critical"
        if control in HIGH_CONTROLS:
            return "high"
        return "medium"

    def _description(self, control: str) -> str:
        return control.replace("_", " ").capitalize() + "."

    def _audit_event_id(self, partner_id: str) -> str:
        return f"AUD-EXTERNAL-PARTNER-READINESS-{partner_id}"

    def _correlation_id(self, partner_id: str) -> str:
        return f"CORR-EXTERNAL-PARTNER-{partner_id}"

    def _agent_correlation_id(self, agent_id: str | None) -> str | None:
        if not agent_id:
            return None
        return f"CORR-AGENT-{agent_id.strip().upper().removeprefix('AGENT-')}"

    def _normalize_id(self, value: str, fallback: str) -> str:
        normalized = value.strip().upper().replace("_", "-").replace(" ", "-")
        return normalized or fallback

    def _dedupe(self, values: list[str]) -> list[str]:
        deduped = []
        for value in values:
            if value and value not in deduped:
                deduped.append(value)
        return deduped


external_partner_agent_readiness_service = ExternalPartnerAgentReadinessService()
