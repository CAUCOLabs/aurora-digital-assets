from datetime import datetime, timezone

from app.schemas.human_approval_integrity import (
    HumanApprovalIntegrityEvaluationRequest,
    HumanApprovalIntegrityEvaluationResponse,
    HumanApprovalIntegrityRiskSignalsResponse,
    HumanApprovalIntegrityRulesResponse,
    HumanDualControlPreviewRequest,
    HumanDualControlPreviewResponse,
    HumanSensitiveApprovalIntegrityRequest,
    HumanSensitiveApprovalIntegrityResponse,
)
from app.services.audit_service import audit_service


RISK_SIGNALS = [
    "reviewer_conflict_of_interest",
    "reviewer_single_point_of_failure",
    "excessive_sensitive_approvals",
    "repeated_override_attempts",
    "approval_after_system_block",
    "approval_against_critical_evidence",
    "approval_outside_working_hours",
    "approval_velocity_anomaly",
    "same_reviewer_repeated_destination",
    "reviewer_linked_to_case_actor",
    "reviewer_approved_own_case",
    "reviewer_ignored_revocation_signal",
    "reviewer_ignored_abuse_signal",
    "reviewer_ignored_secret_exposure_signal",
    "reviewer_ignored_custodian_guardrail",
    "emergency_override_pressure",
    "emergency_override_abuse",
    "dual_control_missing",
    "segregation_of_duties_violation",
    "insufficient_reviewer_independence",
    "post_approval_audit_required",
]

RULES = [
    "human review is not a trust anchor",
    "no single human can override critical system block",
    "dual control required for critical actions",
    "segregation of duties required",
    "emergency override cannot bypass safety",
    "human review is never sufficient by itself to clear secret exposure, agent abuse, agent revocation, custodian guardrail, AI threat, withdrawal execution, or real execution restrictions",
]

SAFETY_NOTICE = (
    "Local deterministic human approval integrity evaluation only. No real "
    "employee monitoring, no legal accusation or criminal finding, no real "
    "approval granted, no real banking, custody, blockchain, cloud, or "
    "withdrawal execution occurred, and no secrets were stored or exposed."
)

PREVIEW_SAFETY_NOTICE = (
    "Local deterministic preview only. No real employee monitoring, no legal "
    "accusation or criminal finding, no real approval granted, no real banking, "
    "custody, blockchain, cloud, or withdrawal execution occurred, and no "
    "secrets were stored or exposed."
)

CRITICAL_CONTEXT_LINKS = {
    "linked_agent_abuse_audit_event_id": "reviewer_ignored_abuse_signal",
    "linked_agent_revocation_audit_event_id": "reviewer_ignored_revocation_signal",
    "linked_secret_guard_case_id": "reviewer_ignored_secret_exposure_signal",
    "linked_custodian_guard_case_id": "reviewer_ignored_custodian_guardrail",
    "linked_ai_threat_case_id": "approval_against_critical_evidence",
}


class HumanApprovalIntegrityService:
    """Deterministic reviewer-integrity controls for local prototype approvals."""

    def rules(self) -> HumanApprovalIntegrityRulesResponse:
        return HumanApprovalIntegrityRulesResponse(
            rules=RULES,
            safety_notice=SAFETY_NOTICE,
        )

    def risk_signals(self) -> HumanApprovalIntegrityRiskSignalsResponse:
        return HumanApprovalIntegrityRiskSignalsResponse(
            risk_signals=RISK_SIGNALS,
            safety_notice=SAFETY_NOTICE,
        )

    def evaluate(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> HumanApprovalIntegrityEvaluationResponse:
        reviewer_id = request.reviewer_id.strip() or "unknown-reviewer"
        operation_type = request.operation_type.strip() or "sensitive_operation"
        detected_signals = self._detected_signals(request)
        score = self._score(request)
        level = self._integrity_level(score)
        second_reviewer_required = self._second_reviewer_required(request)
        escalation_required = self._escalation_required(request, score)
        dual_control_satisfied = (
            not second_reviewer_required
            or bool(request.second_reviewer_id and request.second_reviewer_independent)
        )
        segregation_satisfied = not request.reviewer_is_actor
        critical_override_blocked = request.critical_system_block_active
        emergency_override_blocked = self._emergency_override_blocked(request)
        post_audit_required = (
            request.amount_eur > 5000
            or escalation_required
            or bool(set(detected_signals).intersection(CRITICAL_CONTEXT_LINKS.values()))
        )
        blocking_reasons = self._blocking_reasons(
            request=request,
            second_reviewer_required=second_reviewer_required,
            dual_control_satisfied=dual_control_satisfied,
            segregation_satisfied=segregation_satisfied,
            emergency_override_blocked=emergency_override_blocked,
        )
        decision = self._decision(
            request=request,
            score=score,
            second_reviewer_required=second_reviewer_required,
            escalation_required=escalation_required,
            blocking_reasons=blocking_reasons,
        )
        approval_allowed = not blocking_reasons and decision in {
            "reviewer_integrity_clear",
            "reviewer_integrity_monitor",
        }
        operation_paused = not approval_allowed
        audit_event_id = self._audit_event_id(reviewer_id, operation_type)
        correlation_id = self._correlation_id(reviewer_id)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=reviewer_id,
            actor_type="staff",
            source_module="human_approval_integrity",
            action="evaluate_human_approval_integrity",
            object_type="human_approval_integrity_evaluation",
            object_id=operation_type,
            decision=decision,
            severity="critical" if level == "blocked" else level,
            summary=(
                "Human approval integrity evaluated in local deterministic "
                "prototype."
            ),
            correlation_id=correlation_id,
            risk_score=100 - score,
            evidence_reference=request.linked_evidence_package_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "approval_context": request.approval_context,
                "actor_id": request.actor_id,
                "actor_type": request.actor_type,
                "amount_eur": request.amount_eur,
                "asset": request.asset,
                "destination_type": request.destination_type,
                "destination_id": request.destination_id,
                "environment": request.environment,
                "detected_signals": detected_signals,
                "blocking_reasons": blocking_reasons,
                "safety_notice": SAFETY_NOTICE,
            },
        )
        return HumanApprovalIntegrityEvaluationResponse(
            reviewer_id=reviewer_id,
            operation_type=operation_type,
            approval_context=request.approval_context,
            integrity_decision=decision,
            integrity_score=score,
            integrity_level=level,
            approval_allowed=approval_allowed,
            operation_paused=operation_paused,
            second_reviewer_required=second_reviewer_required,
            escalation_required=escalation_required,
            post_approval_audit_required=post_audit_required,
            dual_control_satisfied=dual_control_satisfied,
            segregation_of_duties_satisfied=segregation_satisfied,
            critical_override_blocked=critical_override_blocked,
            emergency_override_blocked=emergency_override_blocked,
            detected_signals=detected_signals,
            blocking_reasons=blocking_reasons,
            recommended_next_actions=self._recommended_next_actions(
                decision=decision,
                second_reviewer_required=second_reviewer_required,
                escalation_required=escalation_required,
                post_audit_required=post_audit_required,
            ),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            linked_review_case_id=request.linked_review_case_id,
            linked_evidence_package_id=request.linked_evidence_package_id,
            linked_audit_event_id=request.linked_audit_event_id,
            safety_notice=SAFETY_NOTICE,
            created_at=created_at,
        )

    def evaluate_sensitive_approval(
        self,
        request: HumanSensitiveApprovalIntegrityRequest,
    ) -> HumanSensitiveApprovalIntegrityResponse:
        human_integrity = self.evaluate(
            HumanApprovalIntegrityEvaluationRequest(
                reviewer_id=request.reviewer_id,
                operation_type=request.operation_type,
                approval_context="sensitive_approval_integrity_review",
                actor_id=request.actor_id,
                actor_type=request.actor_type,
                amount_eur=request.amount_eur,
                asset=request.asset,
                destination_type=request.destination_type,
                destination_id=request.destination_id,
                linked_review_case_id=request.linked_review_case_id,
                linked_evidence_package_id=request.linked_evidence_package_id,
                linked_agent_abuse_audit_event_id=(
                    request.linked_agent_abuse_audit_event_id
                ),
                linked_agent_revocation_audit_event_id=(
                    request.linked_agent_revocation_audit_event_id
                ),
                critical_system_block_active=request.critical_system_block_active,
                emergency_override_requested=request.emergency_override_requested,
                reviewer_is_actor=request.reviewer_is_actor,
                reviewer_has_conflict=request.reviewer_has_conflict,
                second_reviewer_id=request.second_reviewer_id,
                second_reviewer_independent=request.second_reviewer_independent,
                sensitive_approvals_last_24h=request.sensitive_approvals_last_24h,
                override_attempts_last_24h=request.override_attempts_last_24h,
                outside_working_hours=request.outside_working_hours,
            )
        )
        recommendation = self._sensitive_recommendation(human_integrity)
        return HumanSensitiveApprovalIntegrityResponse(
            human_integrity=human_integrity,
            sensitive_approval_recommendation=recommendation,
            operation_paused_by_human_integrity_guard=human_integrity.operation_paused,
            operation_paused_until_second_reviewer=(
                human_integrity.second_reviewer_required
                and not human_integrity.dual_control_satisfied
            ),
            operation_paused_until_compliance_review=(
                human_integrity.escalation_required
            ),
            audit_event_id=human_integrity.audit_event_id,
            correlation_id=human_integrity.correlation_id,
            safety_notice=SAFETY_NOTICE,
        )

    def dual_control_preview(
        self,
        request: HumanDualControlPreviewRequest,
    ) -> HumanDualControlPreviewResponse:
        priority = request.priority.strip().lower() or "medium"
        dual_control_required = (
            priority in {"high", "critical"}
            or request.critical_system_block_active
            or request.primary_reviewer_has_conflict
            or request.emergency_override_requested
            or request.reviewer_is_actor
        )
        independence_satisfied = bool(
            request.second_reviewer_id and request.second_reviewer_independent
        )
        dual_control_satisfied = (
            not dual_control_required or independence_satisfied
        )
        blocking_reasons: list[str] = []
        if request.critical_system_block_active:
            blocking_reasons.append("critical_system_block_active")
        if request.reviewer_is_actor:
            blocking_reasons.append("segregation_of_duties_violation")
        if dual_control_required and not request.second_reviewer_id:
            blocking_reasons.append("second_reviewer_required")
        elif dual_control_required and not request.second_reviewer_independent:
            blocking_reasons.append("independent_second_reviewer_required")
        if request.primary_reviewer_has_conflict:
            blocking_reasons.append("primary_reviewer_conflict")
        if request.emergency_override_requested and request.critical_system_block_active:
            blocking_reasons.append("emergency_override_blocked")

        preview_decision = self._dual_control_decision(
            dual_control_required=dual_control_required,
            dual_control_satisfied=dual_control_satisfied,
            independence_satisfied=independence_satisfied,
            blocking_reasons=blocking_reasons,
        )
        approval_allowed = dual_control_satisfied and not blocking_reasons
        operation_paused = not approval_allowed
        audit_event_id = self._audit_event_id(
            request.primary_reviewer_id,
            f"dual_control_preview_{request.operation_type}",
        )
        correlation_id = self._correlation_id(request.primary_reviewer_id)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.primary_reviewer_id,
            actor_type="staff",
            source_module="human_approval_integrity",
            action="preview_dual_control",
            object_type="human_dual_control_preview",
            object_id=request.operation_type,
            decision=preview_decision,
            severity="critical" if priority == "critical" else "high",
            summary="Dual control preview evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            metadata={
                "priority": priority,
                "blocking_reasons": blocking_reasons,
                "safety_notice": PREVIEW_SAFETY_NOTICE,
            },
        )
        return HumanDualControlPreviewResponse(
            primary_reviewer_id=request.primary_reviewer_id,
            second_reviewer_id=request.second_reviewer_id,
            operation_type=request.operation_type,
            dual_control_required=dual_control_required,
            dual_control_satisfied=dual_control_satisfied,
            independence_satisfied=independence_satisfied,
            preview_decision=preview_decision,
            approval_allowed=approval_allowed,
            operation_paused=operation_paused,
            blocking_reasons=self._dedupe(blocking_reasons),
            recommended_next_actions=self._dual_control_actions(
                preview_decision,
                blocking_reasons,
            ),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            safety_notice=PREVIEW_SAFETY_NOTICE,
            created_at=created_at,
        )

    def _detected_signals(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> list[str]:
        signals: list[str] = []
        if request.reviewer_has_conflict:
            signals.append("reviewer_conflict_of_interest")
        if request.critical_system_block_active:
            signals.append("approval_after_system_block")
        if request.emergency_override_requested:
            signals.append("emergency_override_pressure")
        if request.emergency_override_requested and request.override_attempts_last_24h > 2:
            signals.append("emergency_override_abuse")
        if request.reviewer_is_actor:
            signals.extend(
                ["reviewer_approved_own_case", "segregation_of_duties_violation"]
            )
        if request.reviewer_is_case_owner:
            signals.append("reviewer_linked_to_case_actor")
        if request.sensitive_approvals_last_24h > 10:
            signals.extend(["excessive_sensitive_approvals", "approval_velocity_anomaly"])
        if request.override_attempts_last_24h > 2:
            signals.append("repeated_override_attempts")
        if request.same_destination_approvals_last_7d > 3:
            signals.append("same_reviewer_repeated_destination")
        if request.outside_working_hours and request.amount_eur > 5000:
            signals.append("approval_outside_working_hours")
        if self._second_reviewer_required(request) and not request.second_reviewer_id:
            signals.extend(["reviewer_single_point_of_failure", "dual_control_missing"])
        elif (
            self._second_reviewer_required(request)
            and not request.second_reviewer_independent
        ):
            signals.append("insufficient_reviewer_independence")
        for field_name, signal in CRITICAL_CONTEXT_LINKS.items():
            if getattr(request, field_name):
                signals.append(signal)
        if request.amount_eur > 5000 or request.critical_system_block_active:
            signals.append("post_approval_audit_required")
        return self._dedupe(signals)

    def _score(self, request: HumanApprovalIntegrityEvaluationRequest) -> int:
        score = 100
        if request.critical_system_block_active:
            score -= 40
        if request.emergency_override_requested:
            score -= 25
        if request.reviewer_is_actor:
            score -= 40
        if request.reviewer_has_conflict:
            score -= 35
        if request.reviewer_is_case_owner and self._is_critical_context(request):
            score -= 20
        if self._second_reviewer_required(request) and not request.second_reviewer_id:
            score -= 25
        if (
            self._second_reviewer_required(request)
            and request.second_reviewer_id
            and not request.second_reviewer_independent
        ):
            score -= 25
        if request.sensitive_approvals_last_24h > 10:
            score -= 20
        if request.override_attempts_last_24h > 2:
            score -= 25
        if request.same_destination_approvals_last_7d > 3:
            score -= 20
        if request.outside_working_hours and request.amount_eur > 5000:
            score -= 15
        for field_name in CRITICAL_CONTEXT_LINKS:
            if getattr(request, field_name):
                score -= 20 if field_name == "linked_ai_threat_case_id" else 25
        return max(score, 0)

    def _integrity_level(self, score: int) -> str:
        if score >= 85:
            return "clear"
        if score >= 65:
            return "monitor"
        if score >= 40:
            return "elevated"
        return "blocked"

    def _decision(
        self,
        *,
        request: HumanApprovalIntegrityEvaluationRequest,
        score: int,
        second_reviewer_required: bool,
        escalation_required: bool,
        blocking_reasons: list[str],
    ) -> str:
        if request.critical_system_block_active:
            if request.emergency_override_requested:
                return "reviewer_integrity_blocks_override"
            return "reviewer_integrity_blocks_sensitive_operation"
        if self._has_critical_link(request) and score < 65:
            return "reviewer_integrity_blocks_sensitive_operation"
        if request.reviewer_is_actor or "reviewer_conflict" in blocking_reasons:
            return "reviewer_integrity_blocks_approval"
        if score < 40:
            return "reviewer_integrity_blocks_approval"
        if escalation_required:
            return "reviewer_integrity_requires_escalation"
        if second_reviewer_required:
            return "reviewer_integrity_requires_second_reviewer"
        if score < 65:
            return "reviewer_integrity_requires_second_reviewer"
        if score < 85:
            return "reviewer_integrity_monitor"
        if blocking_reasons:
            return "reviewer_integrity_insufficient_evidence"
        return "reviewer_integrity_clear"

    def _blocking_reasons(
        self,
        *,
        request: HumanApprovalIntegrityEvaluationRequest,
        second_reviewer_required: bool,
        dual_control_satisfied: bool,
        segregation_satisfied: bool,
        emergency_override_blocked: bool,
    ) -> list[str]:
        reasons: list[str] = []
        if request.critical_system_block_active:
            reasons.append("critical_system_block_active")
        if emergency_override_blocked:
            reasons.append("emergency_override_blocked")
        if not segregation_satisfied:
            reasons.append("segregation_of_duties_violation")
        if request.reviewer_has_conflict and self._is_critical_context(request):
            reasons.append("reviewer_conflict")
        if second_reviewer_required and not dual_control_satisfied:
            reasons.append("dual_control_missing_or_not_independent")
        if self._has_critical_link(request):
            reasons.append("linked_critical_guardrail_context")
        return self._dedupe(reasons)

    def _second_reviewer_required(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> bool:
        return (
            request.critical_system_block_active
            or request.amount_eur > 5000
            or request.emergency_override_requested
            or request.reviewer_has_conflict
            or request.reviewer_is_actor
            or self._has_critical_link(request)
            or (request.reviewer_is_case_owner and self._is_critical_context(request))
        )

    def _escalation_required(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
        score: int,
    ) -> bool:
        return (
            request.critical_system_block_active
            or request.amount_eur > 25000
            or request.sensitive_approvals_last_24h > 10
            or request.override_attempts_last_24h > 2
            or request.same_destination_approvals_last_7d > 3
            or self._has_critical_link(request)
            or score < 65
        )

    def _emergency_override_blocked(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> bool:
        if not request.emergency_override_requested:
            return False
        return (
            request.critical_system_block_active
            or request.amount_eur > 5000
            or request.override_attempts_last_24h > 2
            or request.reviewer_has_conflict
            or request.reviewer_is_actor
            or self._has_critical_link(request)
        )

    def _is_critical_context(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> bool:
        critical_terms = {"critical", "withdrawal", "override", "custodian"}
        operation = request.operation_type.lower()
        context = request.approval_context.lower()
        return (
            request.critical_system_block_active
            or request.amount_eur > 5000
            or any(term in operation or term in context for term in critical_terms)
            or self._has_critical_link(request)
        )

    def _has_critical_link(
        self,
        request: HumanApprovalIntegrityEvaluationRequest,
    ) -> bool:
        return any(getattr(request, field_name) for field_name in CRITICAL_CONTEXT_LINKS)

    def _recommended_next_actions(
        self,
        *,
        decision: str,
        second_reviewer_required: bool,
        escalation_required: bool,
        post_audit_required: bool,
    ) -> list[str]:
        actions = ["record_human_integrity_audit_event_only_no_real_approval_granted"]
        if second_reviewer_required:
            actions.append("require_independent_second_reviewer")
        if escalation_required:
            actions.append("escalate_to_compliance_review")
        if post_audit_required:
            actions.append("prepare_post_approval_audit_review")
        if "blocks" in decision:
            actions.append("keep_sensitive_operation_paused")
        return self._dedupe(actions)

    def _sensitive_recommendation(
        self,
        human_integrity: HumanApprovalIntegrityEvaluationResponse,
    ) -> str:
        if human_integrity.integrity_decision == "reviewer_integrity_blocks_sensitive_operation":
            return "block_sensitive_operation"
        if "blocks" in human_integrity.integrity_decision:
            return "block_human_approval"
        if human_integrity.escalation_required:
            return "escalate_to_compliance"
        if human_integrity.second_reviewer_required:
            return "pause_for_second_reviewer"
        return "continue_standard_approval"

    def _dual_control_decision(
        self,
        *,
        dual_control_required: bool,
        dual_control_satisfied: bool,
        independence_satisfied: bool,
        blocking_reasons: list[str],
    ) -> str:
        if "critical_system_block_active" in blocking_reasons:
            return "dual_control_blocks_approval"
        if not dual_control_required:
            return "dual_control_not_required"
        if dual_control_satisfied:
            return "dual_control_satisfied"
        if not independence_satisfied and "second_reviewer_required" not in blocking_reasons:
            return "dual_control_requires_independent_reviewer"
        return "dual_control_requires_second_reviewer"

    def _dual_control_actions(
        self,
        preview_decision: str,
        blocking_reasons: list[str],
    ) -> list[str]:
        actions = ["record_dual_control_preview_only_no_real_approval_granted"]
        if preview_decision == "dual_control_requires_second_reviewer":
            actions.append("assign_independent_second_reviewer")
        if preview_decision == "dual_control_requires_independent_reviewer":
            actions.append("replace_second_reviewer_with_independent_reviewer")
        if preview_decision == "dual_control_blocks_approval":
            actions.append("keep_operation_paused_and_escalate")
        if blocking_reasons:
            actions.append("retain_audit_trail_for_blocking_reasons")
        return self._dedupe(actions)

    def _audit_event_id(self, reviewer_id: str, operation_type: str) -> str:
        return (
            "AUD-HUMAN-APPROVAL-INTEGRITY-"
            f"{self._token(reviewer_id)}-{self._token(operation_type)}"
        )

    def _correlation_id(self, reviewer_id: str) -> str:
        return f"CORR-HUMAN-APPROVAL-INTEGRITY-{self._token(reviewer_id)}"

    def _token(self, value: str) -> str:
        token = value.strip().upper().replace("_", "-").replace(" ", "-")
        return "-".join(part for part in token.split("-") if part) or "UNKNOWN"

    def _dedupe(self, values: list[str]) -> list[str]:
        return list(dict.fromkeys(values))


human_approval_integrity_service = HumanApprovalIntegrityService()
