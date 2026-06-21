from datetime import datetime, timezone

from app.schemas.agent_identity_governance import (
    AgentGovernanceSummaryRequest,
    AgentGovernanceSummaryResponse,
    AgentIdentityGovernanceEvaluationRequest,
    AgentIdentityGovernanceEvaluationResponse,
    AgentProductionReadinessRequest,
    GovernanceControlDomain,
    GovernanceFrameworkResponse,
)
from app.services.audit_service import audit_service


CONTROL_DOMAINS = {
    "identity_registration": [
        "agents_have_unique_identity",
        "agents_have_human_accountable_owner",
    ],
    "passport_governance": [
        "agents_have_passport",
        "passports_are_status_checked",
        "passports_can_block_agents",
    ],
    "permission_governance": [
        "permissions_are_explicit",
        "permissions_are_deny_by_default",
        "sensitive_permissions_require_review",
    ],
    "action_auditability": [
        "actions_are_audited",
        "blocked_actions_are_audited",
    ],
    "evidence_traceability": [
        "evidence_packages_link_to_agent_actions",
        "evidence_required_for_high_and_critical_actions",
    ],
    "review_case_governance": [
        "review_cases_link_to_agent_evidence",
        "review_lifecycle_available",
    ],
    "lifecycle_governance": [
        "review_lifecycle_available",
        "human_review_required_for_critical_actions",
    ],
    "revocation_governance": [
        "revocation_evaluation_available",
        "revocation_preview_available",
    ],
    "sensitive_action_governance": [
        "sensitive_action_guard_available",
        "sensitive_permissions_require_review",
    ],
    "policy_engine_governance": [
        "policy_engine_available",
        "emergency_override_cannot_bypass_safety",
    ],
    "abuse_detection_governance": ["abuse_detection_available"],
    "external_partner_governance": ["external_partner_readiness_available"],
    "custodian_readiness_governance": ["custodian_guardrails_available"],
    "cloud_kubernetes_governance": [
        "cloud_kubernetes_guardrails_available",
        "no_real_cloud_deployment_policy",
    ],
    "secret_exposure_governance": [
        "secret_exposure_guard_available",
        "no_raw_secret_storage_policy",
    ],
    "ai_threat_governance": ["ai_threat_defense_available"],
    "sensitive_approval_governance": ["sensitive_approval_guard_available"],
    "human_accountability": [
        "agents_have_human_accountable_owner",
        "human_review_required_for_critical_actions",
    ],
    "operational_resilience": ["production_requires_additional_controls"],
    "audit_export_readiness": [
        "audit_export_readiness",
        "audit_event_ids_deterministic",
        "correlation_ids_deterministic",
    ],
    "production_safety_boundary": [
        "no_real_execution_policy",
        "no_real_custodian_access_policy",
        "no_real_blockchain_execution_policy",
        "no_real_cloud_deployment_policy",
        "production_requires_additional_controls",
    ],
}

CRITICAL_CONTROLS = {
    "agents_have_unique_identity",
    "agents_have_human_accountable_owner",
    "agents_have_passport",
    "passports_are_status_checked",
    "passports_can_block_agents",
    "permissions_are_explicit",
    "permissions_are_deny_by_default",
    "actions_are_audited",
    "blocked_actions_are_audited",
    "evidence_packages_link_to_agent_actions",
    "review_cases_link_to_agent_evidence",
    "review_lifecycle_available",
    "revocation_evaluation_available",
    "sensitive_action_guard_available",
    "policy_engine_available",
    "abuse_detection_available",
    "no_raw_secret_storage_policy",
    "no_real_execution_policy",
    "no_real_custodian_access_policy",
    "no_real_blockchain_execution_policy",
    "emergency_override_cannot_bypass_safety",
    "audit_event_ids_deterministic",
    "correlation_ids_deterministic",
    "human_review_required_for_critical_actions",
    "evidence_required_for_high_and_critical_actions",
}

HIGH_CONTROLS = {
    "revocation_preview_available",
    "external_partner_readiness_available",
    "custodian_guardrails_available",
    "cloud_kubernetes_guardrails_available",
    "secret_exposure_guard_available",
    "ai_threat_defense_available",
    "sensitive_approval_guard_available",
    "production_requires_additional_controls",
    "audit_export_readiness",
}

PRODUCTION_SAFETY_CONTROLS = {
    "no_real_execution_policy",
    "no_real_custodian_access_policy",
    "no_real_blockchain_execution_policy",
    "no_real_cloud_deployment_policy",
    "production_requires_additional_controls",
}
BLOCKING_SECRET_CONTROLS = {"no_raw_secret_storage_policy"}
BLOCKING_EXECUTION_CONTROLS = {"no_real_execution_policy"}
PRODUCTION_LIKE_ENVIRONMENTS = {"production", "future_production"}

GOVERNANCE_SAFETY_NOTICE = (
    "Local deterministic governance readiness evaluation only. No production "
    "deployment performed, no real access granted, no real custodian or bank "
    "integration used, no credentials created or exchanged, no secrets stored "
    "or exposed, no custody, blockchain, cloud, banking, or withdrawal "
    "execution occurred, and this is not a legal or regulatory certification."
)


class AgentIdentityGovernanceService:
    """Deterministic governance readiness layer for local agent identity controls."""

    def framework(self) -> GovernanceFrameworkResponse:
        return GovernanceFrameworkResponse(
            purpose=(
                "Evaluate production-grade agent identity governance readiness "
                "for Aurora's local deterministic prototype."
            ),
            scope=[
                "agent registry",
                "agent passport",
                "agent permission model",
                "action auditability",
                "evidence and review case linkage",
                "lifecycle and revocation controls",
                "sensitive action, policy, and abuse controls",
                "external partner, cloud, custodian, secret, and AI guardrails",
                "human accountability and audit traceability",
            ],
            non_goals=[
                "real production deployment",
                "legal or regulatory certification",
                "bank, custodian, cloud, Kubernetes, or blockchain integration",
                "credential creation or secret exchange",
                "real custody, withdrawal, banking, or agent execution",
            ],
            safety_boundaries=[
                "no real production deployment",
                "no real access granted",
                "no real custodian or bank integration",
                "no credentials created or exchanged",
                "no secrets stored or exposed",
                "no custody, blockchain, cloud, banking, or withdrawal execution",
            ],
            linked_modules=[
                "agent_registry",
                "agent_passports",
                "agent_permissions",
                "agent_actions",
                "evidence_packages",
                "review_cases",
                "agent_revocation",
                "agent_sensitive_action_guard",
                "agent_policy_engine",
                "agent_abuse_detection",
                "external_partner_agent_readiness",
                "cloud_kubernetes_guardrails",
                "custodian_integration_guardrails",
                "secret_exposure_guard",
                "ai_threat_defense",
                "sensitive_approval",
            ],
        )

    def control_domains(self) -> list[GovernanceControlDomain]:
        return [
            GovernanceControlDomain(
                domain_id=domain,
                description=domain.replace("_", " "),
                controls=controls,
            )
            for domain, controls in CONTROL_DOMAINS.items()
        ]

    def evaluate(
        self,
        request: AgentIdentityGovernanceEvaluationRequest,
    ) -> AgentIdentityGovernanceEvaluationResponse:
        assessment_id = self._normalize_id(request.assessment_id)
        environment = request.environment.strip().lower() or "local"
        target_environment = (
            request.target_environment.strip().lower() or "future_production"
        )
        missing, failed, satisfied = self._control_status(
            request.controls,
            target_environment,
        )
        blockers = self._critical_blockers(
            failed_controls=failed,
            missing_controls=missing,
            linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
        )
        score = self._score(
            failed_controls=failed,
            missing_controls=missing,
            target_environment=target_environment,
            linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_readiness_audit_event_id=request.linked_readiness_audit_event_id,
        )
        decision = self._decision(
            score=score,
            critical_blockers=blockers,
            failed_controls=failed,
            missing_controls=missing,
            linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
        )
        return self._build_response(
            request=request,
            assessment_id=assessment_id,
            environment=environment,
            target_environment=target_environment,
            governance_decision=decision,
            governance_score=score,
            governance_level=self._governance_level(score),
            satisfied_controls=satisfied,
            missing_controls=missing,
            failed_controls=failed,
            critical_blockers=blockers,
        )

    def evaluate_production_readiness(
        self,
        request: AgentProductionReadinessRequest,
    ) -> AgentIdentityGovernanceEvaluationResponse:
        return self.evaluate(
            AgentIdentityGovernanceEvaluationRequest(
                assessment_id=request.assessment_id,
                environment="local",
                target_environment=request.target_environment,
                reviewer_id=request.reviewer_id,
                controls=request.controls,
                linked_agent_id=request.linked_agent_id,
                linked_partner_id=request.linked_partner_id,
                linked_policy_audit_event_id=request.linked_policy_audit_event_id,
                linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
                linked_revocation_audit_event_id=(
                    request.linked_revocation_audit_event_id
                ),
                linked_readiness_audit_event_id=(
                    request.linked_readiness_audit_event_id
                ),
                linked_review_case_id=request.linked_review_case_id,
            )
        )

    def generate_governance_summary(
        self,
        request: AgentGovernanceSummaryRequest,
    ) -> AgentGovernanceSummaryResponse:
        critical_blockers = request.critical_blockers or []
        missing_controls = request.missing_controls or []
        return AgentGovernanceSummaryResponse(
            assessment_id=self._normalize_id(request.assessment_id),
            summary_title="Agent Identity Governance Readiness Summary",
            summary=(
                "Aurora's local agent identity governance posture was summarized "
                "from deterministic prototype controls. The summary is audit-safe "
                "and does not include secret material, credentials, or real access."
            ),
            governance_decision=request.governance_decision,
            governance_score=max(min(request.governance_score, 100), 0),
            governance_level=request.governance_level,
            critical_blockers=critical_blockers,
            missing_controls=missing_controls,
            recommended_next_actions=self._summary_next_actions(
                request.governance_decision,
                critical_blockers,
                missing_controls,
            ),
            audit_safe=True,
            no_secret_material_included=True,
            safety_notice=GOVERNANCE_SAFETY_NOTICE,
        )

    def _build_response(
        self,
        *,
        request: AgentIdentityGovernanceEvaluationRequest,
        assessment_id: str,
        environment: str,
        target_environment: str,
        governance_decision: str,
        governance_score: int,
        governance_level: str,
        satisfied_controls: list[str],
        missing_controls: list[str],
        failed_controls: list[str],
        critical_blockers: list[str],
    ) -> AgentIdentityGovernanceEvaluationResponse:
        flags = self._blocking_flags(
            governance_decision=governance_decision,
            failed_controls=failed_controls,
            missing_controls=missing_controls,
            linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
        )
        audit_event_id = self._audit_event_id(assessment_id)
        correlation_id = self._correlation_id(assessment_id)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_identity_governance",
            action="evaluate_agent_identity_governance",
            object_type="agent_identity_governance_assessment",
            object_id=assessment_id,
            decision=governance_decision,
            severity=governance_level if governance_level != "blocked" else "critical",
            risk_score=100 - governance_score,
            summary=(
                "Agent identity governance evaluated in local deterministic "
                "prototype."
            ),
            correlation_id=correlation_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "environment": environment,
                "target_environment": target_environment,
                "linked_agent_id": request.linked_agent_id,
                "linked_partner_id": request.linked_partner_id,
                "missing_controls": missing_controls,
                "failed_controls": failed_controls,
                "critical_blockers": critical_blockers,
                "notes": request.notes,
                "safety_notice": GOVERNANCE_SAFETY_NOTICE,
            },
        )
        return AgentIdentityGovernanceEvaluationResponse(
            assessment_id=assessment_id,
            environment=environment,
            target_environment=target_environment,
            governance_decision=governance_decision,
            governance_score=governance_score,
            governance_level=governance_level,
            satisfied_controls=satisfied_controls,
            missing_controls=missing_controls,
            failed_controls=failed_controls,
            critical_blockers=critical_blockers,
            conditional_requirements=self._conditional_requirements(
                governance_decision,
                missing_controls,
                failed_controls,
            ),
            human_review_required=governance_decision
            != "production_governance_ready_for_internal_review",
            evidence_required=bool(
                critical_blockers
                or failed_controls
                or governance_level in {"low", "blocked"}
            ),
            review_case_required=governance_decision
            in {
                "production_governance_requires_remediation",
                "production_governance_blocked",
                "production_governance_insufficient_evidence",
            },
            production_access_blocked=flags["production_access_blocked"],
            external_access_blocked=flags["external_access_blocked"],
            custodian_access_blocked=flags["custodian_access_blocked"],
            secret_access_blocked=flags["secret_access_blocked"],
            sensitive_operations_blocked=flags["sensitive_operations_blocked"],
            cloud_deployment_blocked=flags["cloud_deployment_blocked"],
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            linked_agent_id=request.linked_agent_id,
            linked_partner_id=request.linked_partner_id,
            linked_policy_audit_event_id=request.linked_policy_audit_event_id,
            linked_abuse_audit_event_id=request.linked_abuse_audit_event_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            linked_readiness_audit_event_id=request.linked_readiness_audit_event_id,
            linked_review_case_id=request.linked_review_case_id,
            recommended_next_actions=self._recommended_next_actions(
                governance_decision,
                missing_controls,
                failed_controls,
                request.linked_abuse_audit_event_id,
                request.linked_revocation_audit_event_id,
            ),
            safety_notice=GOVERNANCE_SAFETY_NOTICE,
            created_at=created_at,
        )

    def _control_status(
        self,
        controls: dict[str, bool],
        target_environment: str,
    ) -> tuple[list[str], list[str], list[str]]:
        expected_controls = set(CRITICAL_CONTROLS)
        if target_environment in PRODUCTION_LIKE_ENVIRONMENTS:
            expected_controls.update(PRODUCTION_SAFETY_CONTROLS)
        missing = sorted(
            control for control in expected_controls if control not in controls
        )
        failed = sorted(control for control, passed in controls.items() if not passed)
        satisfied = sorted(control for control, passed in controls.items() if passed)
        return missing, failed, satisfied

    def _critical_blockers(
        self,
        *,
        failed_controls: list[str],
        missing_controls: list[str],
        linked_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> list[str]:
        blockers = [
            control
            for control in sorted(set(failed_controls + missing_controls))
            if control in CRITICAL_CONTROLS
        ]
        if linked_abuse_audit_event_id:
            blockers.append("linked_abuse_audit_event")
        if linked_revocation_audit_event_id:
            blockers.append("linked_revocation_audit_event")
        return self._dedupe(blockers)

    def _score(
        self,
        *,
        failed_controls: list[str],
        missing_controls: list[str],
        target_environment: str,
        linked_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
        linked_readiness_audit_event_id: str | None,
    ) -> int:
        score = 100
        penalized = set(failed_controls + missing_controls)
        for control in penalized:
            if control in CRITICAL_CONTROLS:
                score -= 15
            elif control in HIGH_CONTROLS:
                score -= 8
            else:
                score -= 4
        if linked_abuse_audit_event_id:
            score -= 20
        if linked_revocation_audit_event_id:
            score -= 20
        if (
            linked_readiness_audit_event_id
            and "blocked" in linked_readiness_audit_event_id.lower()
        ):
            score -= 15
        if target_environment in PRODUCTION_LIKE_ENVIRONMENTS:
            missing_production = penalized.intersection(PRODUCTION_SAFETY_CONTROLS)
            if missing_production:
                score -= 15
        return max(score, 0)

    def _decision(
        self,
        *,
        score: int,
        critical_blockers: list[str],
        failed_controls: list[str],
        missing_controls: list[str],
        linked_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> str:
        control_gaps = set(failed_controls + missing_controls)
        if linked_revocation_audit_event_id:
            return "production_governance_blocked"
        if BLOCKING_SECRET_CONTROLS.intersection(control_gaps):
            return "production_governance_blocked"
        if BLOCKING_EXECUTION_CONTROLS.intersection(control_gaps):
            return "production_governance_blocked"
        if "sensitive_action_guard_available" in control_gaps:
            return "production_governance_blocked"
        if "policy_engine_available" in control_gaps:
            return "production_governance_blocked"
        if linked_abuse_audit_event_id and score < 40:
            return "production_governance_blocked"
        if "abuse_detection_available" in control_gaps and score < 40:
            return "production_governance_blocked"
        if linked_abuse_audit_event_id or "abuse_detection_available" in control_gaps:
            return "production_governance_requires_remediation"
        if score < 40:
            return "production_governance_blocked"
        if score < 65:
            return "production_governance_requires_remediation"
        if score < 85:
            return "production_governance_ready_with_conditions"
        if critical_blockers:
            return "production_governance_insufficient_evidence"
        return "production_governance_ready_for_internal_review"

    def _blocking_flags(
        self,
        *,
        governance_decision: str,
        failed_controls: list[str],
        missing_controls: list[str],
        linked_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> dict[str, bool]:
        control_gaps = set(failed_controls + missing_controls)
        linked_abuse_or_revocation = bool(
            linked_abuse_audit_event_id or linked_revocation_audit_event_id
        )
        return {
            "production_access_blocked": governance_decision
            == "production_governance_blocked"
            or linked_abuse_or_revocation,
            "external_access_blocked": linked_abuse_or_revocation,
            "custodian_access_blocked": "no_real_custodian_access_policy"
            in control_gaps,
            "secret_access_blocked": "no_raw_secret_storage_policy" in control_gaps,
            "sensitive_operations_blocked": "no_real_execution_policy"
            in control_gaps,
            "cloud_deployment_blocked": "no_real_cloud_deployment_policy"
            in control_gaps,
        }

    def _conditional_requirements(
        self,
        governance_decision: str,
        missing_controls: list[str],
        failed_controls: list[str],
    ) -> list[str]:
        requirements: list[str] = []
        if governance_decision != "production_governance_ready_for_internal_review":
            requirements.append("complete_human_governance_review")
        if missing_controls:
            requirements.append("provide_evidence_for_missing_controls")
        if failed_controls:
            requirements.append("remediate_failed_controls")
        if governance_decision == "production_governance_blocked":
            requirements.append("keep_all_production_access_blocked")
        return self._dedupe(requirements)

    def _recommended_next_actions(
        self,
        governance_decision: str,
        missing_controls: list[str],
        failed_controls: list[str],
        linked_abuse_audit_event_id: str | None,
        linked_revocation_audit_event_id: str | None,
    ) -> list[str]:
        actions = ["retain_local_deterministic_safety_boundary"]
        if missing_controls:
            actions.append("collect_governance_evidence_for_missing_controls")
        if failed_controls:
            actions.append("remediate_failed_governance_controls")
        if linked_abuse_audit_event_id:
            actions.append("review_agent_abuse_detection")
        if linked_revocation_audit_event_id:
            actions.append("review_agent_revocation_context")
        if governance_decision == "production_governance_ready_for_internal_review":
            actions.append("prepare_internal_governance_review_pack")
        elif governance_decision == "production_governance_ready_with_conditions":
            actions.append("document_conditions_before_any_future_production_review")
        else:
            actions.append("open_or_update_review_case_before_reassessment")
        return self._dedupe(actions)

    def _summary_next_actions(
        self,
        governance_decision: str,
        critical_blockers: list[str],
        missing_controls: list[str],
    ) -> list[str]:
        actions = ["retain_no_real_execution_boundary"]
        if critical_blockers:
            actions.append("remediate_critical_blockers")
        if missing_controls:
            actions.append("collect_missing_control_evidence")
        if governance_decision == "production_governance_ready_for_internal_review":
            actions.append("route_summary_to_internal_review")
        else:
            actions.append("document_conditions_or_remediation_before_reassessment")
        return self._dedupe(actions)

    def _governance_level(self, score: int) -> str:
        if score >= 85:
            return "high"
        if score >= 65:
            return "medium"
        if score >= 40:
            return "low"
        return "blocked"

    def _audit_event_id(self, assessment_id: str) -> str:
        return f"AUD-AGENT-IDENTITY-GOVERNANCE-{assessment_id}"

    def _correlation_id(self, assessment_id: str) -> str:
        return f"CORR-AGENT-IDENTITY-GOVERNANCE-{assessment_id}"

    def _normalize_id(self, value: str) -> str:
        normalized = value.strip().upper()
        return normalized or "AGENT-GOVERNANCE-ASSESSMENT-001"

    def _dedupe(self, values: list[str]) -> list[str]:
        return list(dict.fromkeys(values))


agent_identity_governance_service = AgentIdentityGovernanceService()
