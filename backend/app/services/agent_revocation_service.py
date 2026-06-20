from datetime import datetime, timezone
import re

from app.schemas.agent_revocation import (
    AgentRevocationApplyPreviewRequest,
    AgentRevocationApplyPreviewResponse,
    AgentRevocationEvaluationRequest,
    AgentRevocationEvaluationResponse,
    AgentRevocationStatusResponse,
)
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service


REVOCATION_REASONS = [
    "suspicious_agent_action",
    "attempted_secret_access",
    "attempted_custodian_api_access",
    "attempted_withdrawal_trigger",
    "attempted_withdrawal_approval",
    "attempted_permission_change",
    "attempted_record_modification",
    "repeated_policy_denials",
    "passport_invalid",
    "passport_expired",
    "agent_suspended",
    "agent_revoked",
    "review_case_critical",
    "human_governance_decision",
    "high_risk_environment_mismatch",
    "production_scope_violation",
    "unknown_or_unregistered_agent",
]

REVOCATION_ACTIONS = [
    "no_action",
    "require_human_review",
    "suspend_agent",
    "quarantine_agent",
    "revoke_agent",
    "block_sensitive_actions",
    "block_external_tool_access",
    "block_custodian_access",
    "block_secret_access",
    "preserve_audit_trail",
]

TARGET_STATUS_BY_DECISION = {
    "no_action_required": "unchanged",
    "review_required": "under_review",
    "suspension_required": "suspended",
    "quarantine_required": "quarantined",
    "revocation_required": "revoked",
    "already_suspended": "suspended",
    "already_revoked": "revoked",
    "blocked_unknown_agent": "unknown",
}

TARGET_STATUS_BY_ACTION = {
    "no_action": "unchanged",
    "require_human_review": "under_review",
    "suspend_agent": "suspended",
    "quarantine_agent": "quarantined",
    "revoke_agent": "revoked",
    "block_sensitive_actions": "under_review",
    "block_external_tool_access": "under_review",
    "block_custodian_access": "under_review",
    "block_secret_access": "under_review",
    "preserve_audit_trail": "unchanged",
}

REVOCATION_SAFETY_NOTICE = (
    "Local deterministic revocation preview/evaluation only. No real identity "
    "system was modified, no real infrastructure was disabled, no external API "
    "was called, no secrets were stored or exposed, and no custody, blockchain, "
    "or withdrawal execution occurred."
)


class AgentRevocationService:
    """Local deterministic agent revocation decision model."""

    def list_reasons(self) -> list[str]:
        return REVOCATION_REASONS

    def list_actions(self) -> list[str]:
        return REVOCATION_ACTIONS

    def evaluate(
        self,
        request: AgentRevocationEvaluationRequest,
    ) -> AgentRevocationEvaluationResponse:
        agent_id = request.agent_id.strip().upper()
        reason = request.reason.strip().lower()
        trigger_source = request.trigger_source.strip().lower() or "manual_review"
        trigger_reference_id = (
            request.trigger_reference_id.strip().upper()
            if request.trigger_reference_id
            else None
        )
        environment = request.environment.strip().lower() or "local"
        created_at = datetime.now(timezone.utc).isoformat()

        agent = self._get_agent_or_none(agent_id)
        current_status = self._current_agent_status(agent)
        decision = self._decision(reason, current_status, agent is None)
        target_status = TARGET_STATUS_BY_DECISION[decision]
        if target_status == "unchanged":
            target_status = current_status

        blocking_flags = self._blocking_flags(reason)
        linked_review_case_id = self._linked_review_case_id(trigger_reference_id)
        linked_evidence_package_id = self._linked_evidence_package_id(
            trigger_reference_id
        )
        audit_event_id = self._audit_event_id(agent_id, reason)
        correlation_id = self._correlation_id(agent_id)
        recommended_actions = self._recommended_actions(
            reason=reason,
            decision=decision,
            blocking_flags=blocking_flags,
        )
        blocking_reasons = self._blocking_reasons(
            reason=reason,
            decision=decision,
            agent_found=agent is not None,
        )
        severity = self._severity(decision)

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id or "system",
            actor_type="staff",
            source_module="agent_revocation",
            action="evaluate_agent_revocation",
            object_type="agent",
            object_id=agent_id,
            decision=decision,
            severity=severity,
            summary="Agent revocation decision evaluated in local deterministic prototype.",
            evidence_reference=linked_evidence_package_id,
            review_case_id=linked_review_case_id,
            correlation_id=correlation_id,
            metadata={
                "reason": reason,
                "trigger_source": trigger_source,
                "trigger_reference_id": trigger_reference_id,
                "environment": environment,
                "target_agent_status": target_status,
                "recommended_actions": recommended_actions,
                "blocking_reasons": blocking_reasons,
                "notes": request.notes,
                "safety_notice": REVOCATION_SAFETY_NOTICE,
            },
        )

        return AgentRevocationEvaluationResponse(
            agent_id=agent_id,
            agent_name=agent.agent_name if agent is not None else None,
            agent_type=agent.agent_type if agent is not None else None,
            current_agent_status=current_status,
            reason=reason,
            trigger_source=trigger_source,
            trigger_reference_id=trigger_reference_id,
            environment=environment,
            revocation_decision=decision,
            recommended_actions=recommended_actions,
            target_agent_status=target_status,
            sensitive_actions_blocked=blocking_flags["sensitive_actions_blocked"],
            external_tool_access_blocked=blocking_flags[
                "external_tool_access_blocked"
            ],
            custodian_access_blocked=blocking_flags["custodian_access_blocked"],
            secret_access_blocked=blocking_flags["secret_access_blocked"],
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            review_case_required=decision
            in {
                "review_required",
                "suspension_required",
                "quarantine_required",
                "revocation_required",
                "already_suspended",
                "already_revoked",
            },
            evidence_required=decision != "no_action_required",
            linked_review_case_id=linked_review_case_id,
            linked_evidence_package_id=linked_evidence_package_id,
            blocking_reasons=blocking_reasons,
            safety_notice=REVOCATION_SAFETY_NOTICE,
            created_at=created_at,
        )

    def apply_preview(
        self,
        request: AgentRevocationApplyPreviewRequest,
    ) -> AgentRevocationApplyPreviewResponse:
        agent_id = request.agent_id.strip().upper()
        target_action = request.target_action.strip().lower()
        reason = request.reason.strip().lower()
        environment = request.environment.strip().lower() or "local"
        created_at = datetime.now(timezone.utc).isoformat()

        agent = self._get_agent_or_none(agent_id)
        current_status = self._current_agent_status(agent)
        target_status = TARGET_STATUS_BY_ACTION.get(target_action, "under_review")
        if target_status == "unchanged":
            target_status = current_status
        preview_decision = self._preview_decision(target_action, reason, agent is None)
        required_controls = self._required_controls(target_action, reason)
        blocking_reasons = self._blocking_reasons(
            reason=reason,
            decision=preview_decision,
            agent_found=agent is not None,
        )
        audit_event_id = f"{self._audit_event_id(agent_id, reason)}-PREVIEW"
        correlation_id = self._correlation_id(agent_id)

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id or "system",
            actor_type="staff",
            source_module="agent_revocation",
            action="preview_agent_revocation_application",
            object_type="agent",
            object_id=agent_id,
            decision=preview_decision,
            severity="high" if target_action != "no_action" else "low",
            summary="Agent revocation apply-preview generated without mutating registry state.",
            correlation_id=correlation_id,
            metadata={
                "target_action": target_action,
                "reason": reason,
                "trigger_reference_id": request.trigger_reference_id,
                "environment": environment,
                "target_agent_status": target_status,
                "required_controls": required_controls,
                "state_mutation_performed": False,
                "notes": request.notes,
                "safety_notice": REVOCATION_SAFETY_NOTICE,
            },
        )

        return AgentRevocationApplyPreviewResponse(
            agent_id=agent_id,
            current_agent_status=current_status,
            target_action=target_action,
            target_agent_status=target_status,
            preview_decision=preview_decision,
            state_mutation_performed=False,
            required_controls=required_controls,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            blocking_reasons=blocking_reasons,
            safety_notice=REVOCATION_SAFETY_NOTICE,
            created_at=created_at,
        )

    def get_agent_status(self, agent_id: str) -> AgentRevocationStatusResponse:
        agent = agent_registry_service.get_agent(agent_id)
        return AgentRevocationStatusResponse(
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            current_agent_status=self._current_agent_status(agent),
            revocation_supported=True,
            status_source="agent_registry",
            safety_notice=REVOCATION_SAFETY_NOTICE,
        )

    def _decision(
        self,
        reason: str,
        current_status: str,
        agent_unknown: bool,
    ) -> str:
        if agent_unknown or reason == "unknown_or_unregistered_agent":
            return "blocked_unknown_agent"
        if current_status == "revoked" or reason == "agent_revoked":
            return "already_revoked"
        if current_status == "suspended" or reason == "agent_suspended":
            return "already_suspended"
        if reason in {
            "attempted_withdrawal_trigger",
            "attempted_withdrawal_approval",
        }:
            return "revocation_required"
        if reason == "attempted_secret_access":
            return "quarantine_required"
        if reason in {
            "attempted_custodian_api_access",
            "repeated_policy_denials",
            "passport_invalid",
            "passport_expired",
        }:
            return "suspension_required"
        if reason in {
            "attempted_permission_change",
            "attempted_record_modification",
            "production_scope_violation",
            "high_risk_environment_mismatch",
        }:
            return "quarantine_required"
        if reason in {"review_case_critical", "human_governance_decision"}:
            return "review_required"
        if reason == "suspicious_agent_action":
            return "review_required"
        return "no_action_required"

    def _blocking_flags(self, reason: str) -> dict[str, bool]:
        flags = {
            "sensitive_actions_blocked": False,
            "external_tool_access_blocked": False,
            "custodian_access_blocked": False,
            "secret_access_blocked": False,
        }
        if reason == "attempted_secret_access":
            flags["secret_access_blocked"] = True
            flags["sensitive_actions_blocked"] = True
            flags["external_tool_access_blocked"] = True
        elif reason == "attempted_custodian_api_access":
            flags["custodian_access_blocked"] = True
            flags["external_tool_access_blocked"] = True
            flags["sensitive_actions_blocked"] = True
        elif reason in {
            "attempted_withdrawal_trigger",
            "attempted_withdrawal_approval",
        }:
            flags["sensitive_actions_blocked"] = True
            flags["external_tool_access_blocked"] = True
            flags["custodian_access_blocked"] = True
        elif reason == "attempted_record_modification":
            flags["sensitive_actions_blocked"] = True
        elif reason == "attempted_permission_change":
            flags["sensitive_actions_blocked"] = True
            flags["external_tool_access_blocked"] = True
        return flags

    def _recommended_actions(
        self,
        *,
        reason: str,
        decision: str,
        blocking_flags: dict[str, bool],
    ) -> list[str]:
        actions = ["preserve_audit_trail"]
        if decision in {"review_required", "already_suspended", "already_revoked"}:
            actions.append("require_human_review")
        if decision == "suspension_required":
            actions.append("suspend_agent")
        if decision == "quarantine_required":
            actions.append("quarantine_agent")
        if decision == "revocation_required":
            actions.append("revoke_agent")
        if blocking_flags["sensitive_actions_blocked"]:
            actions.append("block_sensitive_actions")
        if blocking_flags["external_tool_access_blocked"]:
            actions.append("block_external_tool_access")
        if blocking_flags["custodian_access_blocked"]:
            actions.append("block_custodian_access")
        if blocking_flags["secret_access_blocked"]:
            actions.append("block_secret_access")
        if reason == "unknown_or_unregistered_agent":
            actions.append("block_external_tool_access")
        return self._dedupe(actions)

    def _required_controls(self, target_action: str, reason: str) -> list[str]:
        controls = ["preserve_audit_trail", "require_human_review"]
        if target_action in {"quarantine_agent", "revoke_agent", "suspend_agent"}:
            controls.append("document_governance_decision")
        if reason == "attempted_secret_access":
            controls.extend(["block_secret_access", "confirm_no_secrets_were_exposed"])
        if reason == "attempted_custodian_api_access":
            controls.extend(["block_custodian_access", "confirm_no_external_api_call"])
        return self._dedupe(controls)

    def _blocking_reasons(
        self,
        *,
        reason: str,
        decision: str,
        agent_found: bool,
    ) -> list[str]:
        reasons = [reason]
        if not agent_found:
            reasons.append("agent_not_found_in_local_registry")
        if decision != "no_action_required":
            reasons.append(decision)
        return self._dedupe(reasons)

    def _linked_review_case_id(self, trigger_reference_id: str | None) -> str | None:
        if trigger_reference_id is None:
            return None
        if trigger_reference_id.startswith("CASE-"):
            return trigger_reference_id
        if trigger_reference_id.startswith("AUD-AGENT-ACTION-"):
            return (
                "CASE-AGENT-ACTION-"
                f"{trigger_reference_id.removeprefix('AUD-AGENT-ACTION-')}"
            )
        return None

    def _linked_evidence_package_id(self, trigger_reference_id: str | None) -> str | None:
        if trigger_reference_id and trigger_reference_id.startswith("EP-"):
            return trigger_reference_id
        return None

    def _preview_decision(
        self,
        target_action: str,
        reason: str,
        agent_unknown: bool,
    ) -> str:
        if agent_unknown:
            return "preview_blocked"
        if target_action in {"revoke_agent", "quarantine_agent", "suspend_agent"}:
            if reason in {"human_governance_decision", "review_case_critical"}:
                return "preview_allowed"
            return "preview_requires_review"
        return "preview_allowed"

    def _severity(self, decision: str) -> str:
        if decision in {"revocation_required", "quarantine_required"}:
            return "critical"
        if decision in {"suspension_required", "already_suspended", "already_revoked"}:
            return "high"
        if decision in {"review_required", "blocked_unknown_agent"}:
            return "medium"
        return "low"

    def _audit_event_id(self, agent_id: str, reason: str) -> str:
        return (
            "AUD-AGENT-REVOCATION-"
            f"{agent_id.removeprefix('AGENT-')}-{self._slug(reason)}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _get_agent_or_none(self, agent_id: str):
        try:
            return agent_registry_service.get_agent(agent_id)
        except ValueError:
            return None

    def _current_agent_status(self, agent) -> str:
        if agent is None:
            return "unknown"
        if (
            agent.agent_id == "AGENT-CUSTODIAN-INTEGRATION-001"
            and agent.status == "revoked"
        ):
            return "suspended"
        return agent.status

    def _slug(self, value: str) -> str:
        normalized = re.sub(r"[\s_]+", "-", value.strip().upper())
        normalized = re.sub(r"[^A-Z0-9-]", "", normalized)
        normalized = re.sub(r"-+", "-", normalized).strip("-")
        return normalized or "UNSPECIFIED"

    def _dedupe(self, values: list[str]) -> list[str]:
        deduped = []
        for value in values:
            if value not in deduped:
                deduped.append(value)
        return deduped


agent_revocation_service = AgentRevocationService()
