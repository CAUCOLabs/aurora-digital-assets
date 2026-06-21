from datetime import datetime, timezone

from app.schemas.agent_abuse_detection import (
    AgentAbuseDetectionRequest,
    AgentAbuseDetectionResponse,
    AgentAbusePatternDefinition,
    AgentAbuseResponseRecommendationRequest,
    AgentAbuseResponseRecommendationResponse,
    AgentAbuseSequenceRequest,
    AgentAbuseSequenceResponse,
    AgentAbuseSignalDefinition,
)
from app.services.audit_service import audit_service


SIGNAL_DEFINITIONS = [
    ("permission_abuse", "Repeated denied or restricted permission attempts.", 70),
    ("secret_access_attempt", "Attempt to access secret material.", 100),
    ("custodian_access_attempt", "Attempt to access custodian APIs.", 95),
    ("withdrawal_execution_attempt", "Attempt to trigger or approve withdrawals.", 100),
    ("privilege_escalation_attempt", "Attempt to change permissions.", 90),
    ("record_tampering_attempt", "Attempt to modify audit or review records.", 90),
    ("emergency_override_abuse", "Repeated emergency override attempts.", 75),
    ("environment_scope_violation", "Production-like environment scope violation.", 85),
    ("repeated_policy_denial", "Repeated blocked policy decisions.", 75),
    ("post_suspension_activity", "Activity after suspension, quarantine, or revocation.", 90),
    ("passport_permission_mismatch", "Passport and permission decisions do not align.", 80),
    ("suspicious_action_sequence", "Suspicious sequence of blocked high-risk actions.", 95),
]

PATTERN_DEFINITIONS = [
    ("repeated_denied_permissions", "Multiple denied permission decisions."),
    ("secret_access_attempt", "Secret access action or policy signal."),
    ("custodian_access_after_suspension", "Custodian access attempt after suspension."),
    ("withdrawal_approval_attempt", "Attempted withdrawal approval."),
    ("emergency_override_repeated", "Repeated emergency override attempts."),
    ("permission_escalation_attempt", "Attempted permission change."),
    ("audit_record_tampering_attempt", "Attempted audit or review record modification."),
    ("production_scope_violation", "Action attempted in production-like environment."),
    ("suspicious_secret_then_withdrawal_sequence", "Secret access followed by withdrawal action."),
    ("blocked_policy_spike", "Multiple blocked policy decisions."),
    ("revoked_agent_activity", "Activity by revoked agent."),
]

SIGNAL_WEIGHTS = {
    "attempted_secret_access": 100,
    "attempt_secret_access": 100,
    "attempted_custodian_api_access": 95,
    "attempt_custodian_api_access": 95,
    "attempted_withdrawal_trigger": 100,
    "attempt_withdrawal_trigger": 100,
    "attempted_withdrawal_approval": 100,
    "attempt_withdrawal_approval": 100,
    "attempted_permission_change": 90,
    "attempt_permission_change": 90,
    "attempted_record_modification": 90,
    "attempt_record_modification": 90,
    "emergency_override_requested": 75,
    "linked_revocation_audit_event": 85,
    "policy_block_secret_access": 100,
    "policy_block_custodian_access": 95,
    "policy_block_withdrawal_execution": 100,
    "policy_block_by_revocation": 95,
    "agent_status_suspended": 85,
    "agent_status_revoked": 100,
    "agent_status_quarantined": 95,
    "passport_status_blocked": 80,
    "repeated_denied_permissions": 70,
    "repeated_policy_denials": 75,
    "post_suspension_activity": 90,
    "production_scope_violation": 85,
}

SECRET_ACTIONS = {"attempt_secret_access", "attempted_secret_access"}
CUSTODIAN_ACTIONS = {
    "attempt_custodian_api_access",
    "attempted_custodian_api_access",
}
WITHDRAWAL_ACTIONS = {
    "attempt_withdrawal_trigger",
    "attempted_withdrawal_trigger",
    "attempt_withdrawal_approval",
    "attempted_withdrawal_approval",
}
PERMISSION_ESCALATION_ACTIONS = {
    "attempt_permission_change",
    "attempted_permission_change",
}
RECORD_TAMPERING_ACTIONS = {
    "attempt_record_modification",
    "attempted_record_modification",
}
PRODUCTION_LIKE_ENVIRONMENTS = {"production", "future_production"}

ABUSE_SAFETY_NOTICE = (
    "Local deterministic abuse detection only. No real action executed, no "
    "external API called, no secrets stored or exposed, and no custody, "
    "blockchain, or withdrawal execution occurred."
)

RECOMMENDATION_SAFETY_NOTICE = (
    "Local deterministic abuse response recommendation only. No real action "
    "executed, no external API called, and no secret material is included."
)


class AgentAbuseDetectionService:
    """Deterministic abuse signal evaluator for local agent governance metadata."""

    def list_signals(self) -> list[AgentAbuseSignalDefinition]:
        return [
            AgentAbuseSignalDefinition(
                signal_category=signal,
                description=description,
                default_weight=weight,
            )
            for signal, description, weight in SIGNAL_DEFINITIONS
        ]

    def list_patterns(self) -> list[AgentAbusePatternDefinition]:
        return [
            AgentAbusePatternDefinition(pattern_id=pattern, description=description)
            for pattern, description in PATTERN_DEFINITIONS
        ]

    def evaluate(
        self,
        request: AgentAbuseDetectionRequest,
    ) -> AgentAbuseDetectionResponse:
        agent_id = request.agent_id.strip().upper()
        detection_context = request.detection_context.strip().lower()
        action = self._action_name(request.sensitive_action_type, request.requested_action)
        signals, patterns = self._detect_signals_and_patterns(request, action)
        abuse_score = self._abuse_score(request, signals)
        abuse_level = self._abuse_level(abuse_score)
        abuse_decision = self._abuse_decision(
            abuse_level=abuse_level,
            action=action,
            agent_status=(request.agent_status or "").strip().lower(),
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
        )
        flags = self._blocking_flags(
            action=action,
            agent_status=(request.agent_status or "").strip().lower(),
            signals=signals,
            abuse_decision=abuse_decision,
        )
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event_id = self._audit_event_id(agent_id, action)
        correlation_id = self._correlation_id(agent_id)
        recommended_actions = self._recommended_actions(abuse_decision, abuse_level)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_abuse_detection",
            action="evaluate_agent_abuse",
            object_type="agent_abuse_detection",
            object_id=f"{agent_id}:{action}",
            decision=abuse_decision,
            severity=abuse_level if abuse_level != "none" else "low",
            risk_score=abuse_score,
            summary="Agent abuse signals evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            evidence_reference=request.linked_evidence_package_id,
            review_case_id=request.linked_review_case_id,
            metadata={
                "detection_context": detection_context,
                "agent_status": request.agent_status,
                "passport_decision": request.passport_decision,
                "permission_decision": request.permission_decision,
                "policy_decision": request.policy_decision,
                "sensitive_action_type": request.sensitive_action_type,
                "requested_action": request.requested_action,
                "revocation_decision": request.revocation_decision,
                "linked_review_case_status": request.linked_review_case_status,
                "environment": request.environment,
                "detected_signals": signals,
                "matched_patterns": patterns,
                "safety_notice": ABUSE_SAFETY_NOTICE,
            },
        )
        return AgentAbuseDetectionResponse(
            agent_id=agent_id,
            detection_context=detection_context,
            abuse_detected=abuse_score >= 30,
            abuse_decision=abuse_decision,
            abuse_score=abuse_score,
            abuse_level=abuse_level,
            detected_signals=signals,
            matched_patterns=patterns,
            recommended_actions=recommended_actions,
            sensitive_actions_blocked=flags["sensitive_actions_blocked"],
            secret_access_blocked=flags["secret_access_blocked"],
            custodian_access_blocked=flags["custodian_access_blocked"],
            withdrawal_execution_blocked=flags["withdrawal_execution_blocked"],
            external_tool_access_blocked=flags["external_tool_access_blocked"],
            review_case_required=abuse_level in {"medium", "high", "critical"},
            evidence_required=abuse_level in {"medium", "high", "critical"},
            revocation_recommended=abuse_decision == "revoke_agent_recommended",
            quarantine_recommended=abuse_decision == "quarantine_agent_recommended",
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            linked_review_case_id=request.linked_review_case_id,
            linked_evidence_package_id=request.linked_evidence_package_id,
            linked_revocation_audit_event_id=request.linked_revocation_audit_event_id,
            safety_notice=ABUSE_SAFETY_NOTICE,
            created_at=created_at,
        )

    def evaluate_sequence(
        self,
        request: AgentAbuseSequenceRequest,
    ) -> AgentAbuseSequenceResponse:
        actions = [
            (event.action_type or event.decision or event.event_type).strip().lower()
            for event in request.events
        ]
        blocked_count = sum(1 for event in request.events if event.blocked)
        critical_count = sum(
            1 for event in request.events if (event.risk_level or "").lower() == "critical"
        )
        high_count = sum(
            1
            for event in request.events
            if (event.risk_level or "").lower() in {"high", "critical"}
        )
        action_for_audit = actions[-1] if actions else "sequence_review"
        denied_attempt_count = sum(
            1 for event in request.events if (event.decision or "").lower() == "denied"
        )
        base_request = AgentAbuseDetectionRequest(
            agent_id=request.agent_id,
            detection_context="agent_abuse_sequence",
            requested_action=action_for_audit,
            sensitive_action_type=action_for_audit,
            environment=request.environment,
            denied_attempt_count=denied_attempt_count,
            blocked_policy_count=blocked_count,
            reviewer_id=request.reviewer_id,
        )
        response = self.evaluate(base_request)
        signals = list(response.detected_signals)
        patterns = list(response.matched_patterns)
        if "attempt_secret_access" in actions and any(
            action in WITHDRAWAL_ACTIONS for action in actions
        ):
            signals = self._dedupe(signals + ["suspicious_action_sequence"])
            patterns = self._dedupe(
                patterns + ["suspicious_secret_then_withdrawal_sequence"]
            )
        if critical_count:
            signals = self._dedupe(signals + ["critical_sequence_events"])
        score = min(100, max(response.abuse_score, 95 if critical_count >= 2 else 0))
        level = self._abuse_level(score)
        decision = self._abuse_decision(
            abuse_level=level,
            action=action_for_audit,
            agent_status="",
            linked_revocation_audit_event_id=None,
        )
        flags = self._blocking_flags(
            action=action_for_audit,
            agent_status="",
            signals=signals + actions,
            abuse_decision=decision,
        )
        return AgentAbuseSequenceResponse(
            **response.model_dump(
                exclude={
                    "abuse_detected",
                    "abuse_decision",
                    "abuse_score",
                    "abuse_level",
                    "detected_signals",
                    "matched_patterns",
                    "sensitive_actions_blocked",
                    "secret_access_blocked",
                    "custodian_access_blocked",
                    "withdrawal_execution_blocked",
                    "external_tool_access_blocked",
                    "review_case_required",
                    "evidence_required",
                    "revocation_recommended",
                    "quarantine_recommended",
                }
            ),
            abuse_detected=score >= 30,
            abuse_decision=decision,
            abuse_score=score,
            abuse_level=level,
            detected_signals=signals,
            matched_patterns=patterns,
            sensitive_actions_blocked=flags["sensitive_actions_blocked"],
            secret_access_blocked=flags["secret_access_blocked"],
            custodian_access_blocked=flags["custodian_access_blocked"],
            withdrawal_execution_blocked=flags["withdrawal_execution_blocked"],
            external_tool_access_blocked=flags["external_tool_access_blocked"],
            review_case_required=level in {"medium", "high", "critical"},
            evidence_required=level in {"medium", "high", "critical"},
            revocation_recommended=decision == "revoke_agent_recommended",
            quarantine_recommended=decision == "quarantine_agent_recommended",
            sequence_event_count=len(request.events),
            high_risk_event_count=high_count,
            blocked_event_count=blocked_count,
            critical_event_count=critical_count,
        )

    def recommend_response(
        self,
        request: AgentAbuseResponseRecommendationRequest,
    ) -> AgentAbuseResponseRecommendationResponse:
        decision = request.abuse_decision.strip().lower()
        level = request.abuse_level.strip().lower()
        recommended_actions = self._recommended_actions(decision, level)
        return AgentAbuseResponseRecommendationResponse(
            agent_id=request.agent_id.strip().upper(),
            abuse_decision=decision,
            abuse_level=level,
            recommended_response=self._recommended_response(decision, level),
            recommended_actions=recommended_actions,
            escalation_required=level in {"medium", "high", "critical"}
            or decision != "no_abuse_detected",
            revocation_recommended=decision == "revoke_agent_recommended",
            quarantine_recommended=decision == "quarantine_agent_recommended",
            safety_notice=RECOMMENDATION_SAFETY_NOTICE,
            audit_safe=True,
        )

    def _detect_signals_and_patterns(
        self,
        request: AgentAbuseDetectionRequest,
        action: str,
    ) -> tuple[list[str], list[str]]:
        signals: list[str] = []
        patterns: list[str] = []
        agent_status = (request.agent_status or "").strip().lower()
        passport_decision = (request.passport_decision or "").strip().lower()
        permission_decision = (request.permission_decision or "").strip().lower()
        policy_decision = (request.policy_decision or "").strip().lower()
        revocation_decision = (request.revocation_decision or "").strip().lower()
        environment = request.environment.strip().lower()

        if action in SECRET_ACTIONS or policy_decision == "policy_block_secret_access":
            signals.extend(["secret_access_attempt", action])
            patterns.append("secret_access_attempt")
        if action in CUSTODIAN_ACTIONS or policy_decision == "policy_block_custodian_access":
            signals.extend(["custodian_access_attempt", action])
            if agent_status == "suspended":
                patterns.append("custodian_access_after_suspension")
        if action in WITHDRAWAL_ACTIONS or policy_decision == "policy_block_withdrawal_execution":
            signals.extend(["withdrawal_execution_attempt", action])
            if "approval" in action:
                patterns.append("withdrawal_approval_attempt")
        if action in PERMISSION_ESCALATION_ACTIONS:
            signals.extend(["privilege_escalation_attempt", action])
            patterns.append("permission_escalation_attempt")
        if action in RECORD_TAMPERING_ACTIONS:
            signals.extend(["record_tampering_attempt", action])
            patterns.append("audit_record_tampering_attempt")
        if request.emergency_override_count >= 2:
            signals.extend(["emergency_override_abuse", "emergency_override_requested"])
            patterns.append("emergency_override_repeated")
        if environment in PRODUCTION_LIKE_ENVIRONMENTS:
            signals.append("production_scope_violation")
            patterns.append("production_scope_violation")
        if request.denied_attempt_count >= 3 or permission_decision == "denied":
            signals.append("repeated_denied_permissions")
            patterns.append("repeated_denied_permissions")
        if request.blocked_policy_count >= 3 or policy_decision.startswith("policy_block"):
            signals.append("repeated_policy_denials")
            patterns.append("blocked_policy_spike")
        if request.post_suspension_attempt_count >= 1:
            signals.append("post_suspension_activity")
        if agent_status in {"suspended", "revoked", "quarantined"}:
            signals.append(f"agent_status_{agent_status}")
            if agent_status == "revoked":
                patterns.append("revoked_agent_activity")
            else:
                signals.append("post_suspension_activity")
        if passport_decision == "passport_status_blocked":
            signals.append("passport_status_blocked")
        if request.linked_revocation_audit_event_id or policy_decision == "policy_block_by_revocation":
            signals.append("linked_revocation_audit_event")
        if revocation_decision in {"already_suspended", "already_revoked"}:
            signals.append(f"revocation_decision_{revocation_decision}")
        if passport_decision == "passport_valid" and permission_decision.startswith("blocked"):
            signals.append("passport_permission_mismatch")
        return self._dedupe(signals), self._dedupe(patterns)

    def _abuse_score(
        self,
        request: AgentAbuseDetectionRequest,
        signals: list[str],
    ) -> int:
        score = max([SIGNAL_WEIGHTS.get(signal, 0) for signal in signals] or [0])
        if request.denied_attempt_count >= 3:
            score += 20
        if request.blocked_policy_count >= 3:
            score += 20
        if request.emergency_override_count >= 2:
            score += 25
        if request.post_suspension_attempt_count >= 1:
            score += 25
        if request.environment.strip().lower() in PRODUCTION_LIKE_ENVIRONMENTS:
            score += 15
        return min(score, 100)

    def _abuse_level(self, score: int) -> str:
        if score <= 29:
            return "none"
        if score <= 59:
            return "low"
        if score <= 79:
            return "medium"
        if score <= 94:
            return "high"
        return "critical"

    def _abuse_decision(
        self,
        *,
        abuse_level: str,
        action: str,
        agent_status: str,
        linked_revocation_audit_event_id: str | None,
    ) -> str:
        if action in {"attempt_withdrawal_approval", "attempted_withdrawal_approval"}:
            return "revoke_agent_recommended"
        if action in {"attempt_withdrawal_trigger", "attempted_withdrawal_trigger"}:
            return "revoke_agent_recommended"
        if agent_status == "revoked":
            return "revoke_agent_recommended"
        if action in SECRET_ACTIONS:
            return "quarantine_agent_recommended"
        if action in CUSTODIAN_ACTIONS and agent_status == "suspended":
            return "quarantine_agent_recommended"
        if linked_revocation_audit_event_id and action in SECRET_ACTIONS | CUSTODIAN_ACTIONS | WITHDRAWAL_ACTIONS:
            return "quarantine_agent_recommended"
        return {
            "none": "no_abuse_detected",
            "low": "monitor_agent",
            "medium": "require_human_review",
            "high": "create_review_case",
            "critical": "quarantine_agent_recommended",
        }[abuse_level]

    def _blocking_flags(
        self,
        *,
        action: str,
        agent_status: str,
        signals: list[str],
        abuse_decision: str,
    ) -> dict[str, bool]:
        signal_set = set(signals)
        secret = (
            action in SECRET_ACTIONS
            or "secret_access_attempt" in signal_set
            or bool(signal_set & SECRET_ACTIONS)
        )
        custodian = (
            action in CUSTODIAN_ACTIONS
            or "custodian_access_attempt" in signal_set
            or bool(signal_set & CUSTODIAN_ACTIONS)
        )
        withdrawal = (
            action in WITHDRAWAL_ACTIONS
            or "withdrawal_execution_attempt" in signal_set
            or bool(signal_set & WITHDRAWAL_ACTIONS)
        )
        sensitive = (
            secret
            or custodian
            or withdrawal
            or action in PERMISSION_ESCALATION_ACTIONS
            or action in RECORD_TAMPERING_ACTIONS
            or agent_status in {"suspended", "revoked", "quarantined"}
            or abuse_decision
            in {
                "suspend_agent_recommended",
                "quarantine_agent_recommended",
                "revoke_agent_recommended",
                "block_sensitive_actions",
            }
        )
        external = (
            sensitive
            or custodian
            or withdrawal
            or abuse_decision == "block_external_tool_access"
        )
        return {
            "sensitive_actions_blocked": sensitive,
            "secret_access_blocked": secret,
            "custodian_access_blocked": custodian,
            "withdrawal_execution_blocked": withdrawal,
            "external_tool_access_blocked": external,
        }

    def _recommended_actions(self, abuse_decision: str, abuse_level: str) -> list[str]:
        actions = ["preserve_audit_trail"]
        if abuse_level in {"medium", "high", "critical"}:
            actions.append("create_review_case")
        if abuse_decision in {
            "quarantine_agent_recommended",
            "revoke_agent_recommended",
            "suspend_agent_recommended",
        }:
            actions.append("block_sensitive_actions")
            actions.append("block_external_tool_access")
        if abuse_decision == "quarantine_agent_recommended":
            actions.append("quarantine_agent_review")
        if abuse_decision == "revoke_agent_recommended":
            actions.append("prepare_agent_revocation_review")
        if abuse_decision == "no_abuse_detected":
            actions.append("continue_monitoring")
        return self._dedupe(actions)

    def _recommended_response(self, abuse_decision: str, abuse_level: str) -> str:
        if abuse_decision == "revoke_agent_recommended":
            return "prepare_revocation_review_and_block_sensitive_actions"
        if abuse_decision == "quarantine_agent_recommended":
            return "quarantine_agent_pending_human_review"
        if abuse_level in {"high", "critical"}:
            return "create_review_case_and_block_sensitive_actions"
        if abuse_level == "medium":
            return "require_human_review_and_continue_monitoring"
        return "monitor_agent_activity"

    def _action_name(self, sensitive_action_type: str | None, requested_action: str | None) -> str:
        return (sensitive_action_type or requested_action or "unspecified_action").strip().lower()

    def _audit_event_id(self, agent_id: str, action: str) -> str:
        return f"AUD-AGENT-ABUSE-{agent_id.removeprefix('AGENT-')}-{self._slug(action)}"

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _slug(self, value: str) -> str:
        return value.strip().upper().replace("_", "-")

    def _dedupe(self, values: list[str]) -> list[str]:
        deduped = []
        for value in values:
            if value and value not in deduped:
                deduped.append(value)
        return deduped


agent_abuse_detection_service = AgentAbuseDetectionService()
