from datetime import datetime, timezone

from app.schemas.sensitive_approval import (
    SensitiveApprovalRequest,
    SensitiveApprovalResponse,
    SensitiveApprovalScenario,
    SensitiveOperation,
)
from app.services.audit_service import audit_service
from app.services.review_case_service import review_case_service


ACTIVE_AI_THREAT_GUARD_STATUSES = {
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
}
CLEARED_AI_THREAT_GUARD_STATUSES = {"mitigated", "closed"}
ACTIVE_SECRET_GUARD_STATUSES = {
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
}
CLEARED_SECRET_GUARD_STATUSES = {"mitigated", "closed"}
SECRET_GUARD_RECOMMENDED_NEXT_ACTION = (
    "keep_sensitive_operation_paused_until_secret_guard_review_is_mitigated_or_closed; "
    "preserve_evidence_without_secret_value; redact_sensitive_material; "
    "restrict_access_to_affected_surface; verify_no_secret_value_is_stored; "
    "require_human_approval_before_continuing; "
    "rotate_exposed_credentials_where_applicable; "
    "verify_lifecycle_closure_before_releasing_operation"
)
SECRET_GUARD_DEFAULT_REASON = (
    "Critical Secret Exposure Guard review case is active. Operation must remain "
    "paused until mitigated or closed."
)
SECRET_GUARD_APPROVAL_GUARDS = {
    "CASE-SECRET-GUARD-CONFIG": {
        "correlation_id": "CORR-SECRET-GUARD-CONFIG",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-CONFIG",
        "reason": (
            "Critical Secret Exposure Guard review case is active for "
            "configuration context. Operation must remain paused until mitigated "
            "or closed."
        ),
    },
    "CASE-SECRET-GUARD-PROMPT-CONTEXT": {
        "correlation_id": "CORR-SECRET-GUARD-PROMPT-CONTEXT",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-PROMPT-CONTEXT",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
    "CASE-SECRET-GUARD-LOGS": {
        "correlation_id": "CORR-SECRET-GUARD-LOGS",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-LOGS",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
    "CASE-SECRET-GUARD-EVIDENCE-PACKAGE": {
        "correlation_id": "CORR-SECRET-GUARD-EVIDENCE-PACKAGE",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-EVIDENCE-PACKAGE",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
    "CASE-SECRET-GUARD-REVIEW-CASE": {
        "correlation_id": "CORR-SECRET-GUARD-REVIEW-CASE",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-REVIEW-CASE",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
    "CASE-SECRET-GUARD-API-RESPONSE": {
        "correlation_id": "CORR-SECRET-GUARD-API-RESPONSE",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-API-RESPONSE",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
    "CASE-SECRET-GUARD-CUSTODIAN-SECRET": {
        "correlation_id": "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-CUSTODIAN-SECRET",
        "reason": (
            "Critical Secret Exposure Guard review case is active for custodian "
            "secret reference. Operation must remain paused until mitigated or "
            "closed."
        ),
    },
    "CASE-SECRET-GUARD-CLOUD-SECRET": {
        "correlation_id": "CORR-SECRET-GUARD-CLOUD-SECRET",
        "audit_event_id": "AUD-APPROVAL-SECRET-GUARD-CLOUD-SECRET",
        "reason": SECRET_GUARD_DEFAULT_REASON,
    },
}
AI_THREAT_APPROVAL_GUARDS = {
    "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN": {
        "correlation_id": "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        "audit_event_id": "AUD-APPROVAL-AI-THREAT-GUARD-SENSITIVE-OPERATION-CHAIN",
        "reason": (
            "Critical AI Threat Defense review case is active for a sensitive "
            "operation chain. Operation must remain paused until mitigated or closed."
        ),
        "recommended_next_action": (
            "keep_sensitive_operation_paused_until_ai_threat_review_is_mitigated_or_closed; "
            "preserve_evidence_package; review_permission_and_endpoint_exposure_signals; "
            "require_human_approval_before_continuing; verify_lifecycle_closure_before_releasing_operation"
        ),
    },
    "CASE-AI-THREAT-SECRET-EXPOSURE": {
        "correlation_id": "CORR-AI-THREAT-SECRET-EXPOSURE",
        "audit_event_id": "AUD-APPROVAL-AI-THREAT-GUARD-SECRET-EXPOSURE",
        "reason": (
            "Critical AI Threat Defense review case indicates possible secret "
            "exposure signal. Operation must remain paused until mitigated or closed."
        ),
        "recommended_next_action": (
            "preserve_evidence; rotate_exposed_credentials_where_applicable; "
            "restrict_operation; require_human_review"
        ),
    },
    "CASE-AI-THREAT-PERMISSION-ABUSE": {
        "correlation_id": "CORR-AI-THREAT-PERMISSION-ABUSE",
        "audit_event_id": "AUD-APPROVAL-AI-THREAT-GUARD-PERMISSION-ABUSE",
        "reason": (
            "AI Threat Defense review case indicates permission abuse risk. "
            "Operation must remain paused until mitigated or closed."
        ),
        "recommended_next_action": (
            "keep_sensitive_operation_paused_until_ai_threat_review_is_mitigated_or_closed; "
            "review_permission_signals; require_human_review"
        ),
    },
    "CASE-AI-THREAT-DOCUMENTATION-EXPOSURE": {
        "correlation_id": "CORR-AI-THREAT-DOCUMENTATION-EXPOSURE",
        "audit_event_id": "AUD-APPROVAL-AI-THREAT-GUARD-DOCUMENTATION-EXPOSURE",
        "reason": (
            "AI Threat Defense review case indicates documentation exposure risk. "
            "Operation must remain paused until mitigated or closed."
        ),
        "recommended_next_action": (
            "keep_sensitive_operation_paused_until_ai_threat_review_is_mitigated_or_closed; "
            "preserve_evidence_package; require_human_review"
        ),
    },
    "CASE-AI-THREAT-API-MAPPING": {
        "correlation_id": "CORR-AI-THREAT-API-MAPPING",
        "audit_event_id": "AUD-APPROVAL-AI-THREAT-GUARD-API-MAPPING",
        "reason": (
            "AI Threat Defense review case indicates API mapping risk. "
            "Operation must remain paused until mitigated or closed."
        ),
        "recommended_next_action": (
            "keep_sensitive_operation_paused_until_ai_threat_review_is_mitigated_or_closed; "
            "review_endpoint_exposure_signals; require_human_review"
        ),
    },
}


class SensitiveApprovalService:
    """Deterministic bank-style step-up approval demo service."""

    def list_operations(self) -> list[SensitiveOperation]:
        return [
            self._operation("login_approval", "Login approval", "Customer login step-up approval.", "customer", "medium", "mobile_approval_simulated", ["new_device", "stale_session"]),
            self._operation("external_wallet_withdrawal", "External wallet withdrawal", "Customer withdrawal to an external wallet.", "customer", "critical", "mobile_approval_simulated", ["new_destination", "high_value", "mobile_rejected"]),
            self._operation("new_wallet_registration", "New wallet registration", "Register a new external wallet destination.", "customer", "high", "mobile_approval_simulated", ["new_destination", "device_change"]),
            self._operation("high_value_buy_sell", "High-value buy/sell", "High-value digital asset buy or sell request.", "customer", "high", "mobile_approval_simulated", ["high_value", "market_risk"]),
            self._operation("digital_asset_invoice_payment", "Digital asset invoice payment", "Digital asset invoice payment approval.", "customer", "medium", "mobile_approval_simulated", ["new_recipient", "high_value"]),
            self._operation("security_device_change", "Security device change", "Change customer security approval device.", "customer", "high", "mobile_approval_simulated", ["device_change", "withdrawal_freeze"]),
            self._operation("close_critical_review_case", "Close critical review case", "Reviewer closure of a critical case.", "reviewer", "critical", "strong_reauthentication_simulated", ["mitigation_not_verified", "critical_case"]),
            self._operation("approve_high_risk_withdrawal", "Approve high-risk withdrawal", "Staff approval for high-risk withdrawal review.", "reviewer", "critical", "dual_control_simulated", ["high_value", "new_destination"]),
            self._operation("generate_sensitive_evidence_package", "Generate sensitive evidence package", "Generate evidence for sensitive internal review.", "staff", "high", "strong_reauthentication_simulated", ["sensitive_evidence"]),
            self._operation("reset_demo_audit_data", "Reset demo audit data", "Admin reset of local prototype audit data.", "admin", "critical", "dual_control_simulated", ["audit_data_reset"]),
            self._operation("override_risk_decision", "Override risk decision", "Admin risk decision override in prototype workflow.", "admin", "critical", "dual_control_simulated", ["override", "audit_required"]),
        ]

    def list_scenarios(self) -> list[SensitiveApprovalScenario]:
        return [
            SensitiveApprovalScenario(
                scenario_id="small_known_wallet_withdrawal",
                title="Small withdrawal to known wallet",
                description="Mobile-approved low-value withdrawal to a known wallet.",
                operation_type="external_wallet_withdrawal",
                sample_payload={
                    "operation_type": "external_wallet_withdrawal",
                    "actor_id": "customer-demo",
                    "actor_type": "customer",
                    "amount_eur": 100,
                    "asset": "BTC",
                    "destination_type": "external_wallet",
                    "destination_id": "known-wallet-demo",
                    "is_new_destination": False,
                    "customer_confirmed": True,
                    "mobile_approval_status": "approved",
                    "device_trusted": True,
                    "session_age_minutes": 4,
                },
                expected_decision="approved",
            ),
            SensitiveApprovalScenario(
                scenario_id="high_value_new_wallet_withdrawal",
                title="High-value new wallet withdrawal",
                description="Mobile-approved request still requires backend review.",
                operation_type="external_wallet_withdrawal",
                sample_payload={
                    "operation_type": "external_wallet_withdrawal",
                    "actor_id": "customer-demo",
                    "actor_type": "customer",
                    "amount_eur": 8000,
                    "asset": "BTC",
                    "destination_type": "external_wallet",
                    "destination_id": "new-wallet-demo",
                    "is_new_destination": True,
                    "customer_confirmed": True,
                    "mobile_approval_status": "approved",
                    "device_trusted": True,
                    "session_age_minutes": 4,
                },
                expected_decision="pending_review",
            ),
            SensitiveApprovalScenario(
                scenario_id="mobile_approval_rejected",
                title="Mobile approval rejected",
                description="Rejected mobile approval blocks the operation.",
                operation_type="external_wallet_withdrawal",
                sample_payload={
                    "operation_type": "external_wallet_withdrawal",
                    "actor_id": "customer-demo",
                    "actor_type": "customer",
                    "amount_eur": 100,
                    "mobile_approval_status": "rejected",
                },
                expected_decision="blocked",
            ),
            SensitiveApprovalScenario(
                scenario_id="security_device_change",
                title="Security device change",
                description="Security device changes need protective follow-up.",
                operation_type="security_device_change",
                sample_payload={
                    "operation_type": "security_device_change",
                    "actor_id": "customer-demo",
                    "actor_type": "customer",
                    "customer_confirmed": True,
                    "mobile_approval_status": "approved",
                },
                expected_decision="pending_review",
            ),
        ]

    def evaluate(self, request: SensitiveApprovalRequest) -> SensitiveApprovalResponse:
        operation = self._find_operation(request.operation_type)
        approval_required = operation.approval_required if operation else True
        step_up_method = operation.step_up_method if operation else "mobile_approval_simulated"
        reasons = ["Sensitive operation evaluated by deterministic prototype policy."]
        decision = "step_up_required"
        risk_level = "medium"
        risk_score = 45
        audit_event_id = f"AUD-APPROVAL-{request.operation_type.upper().replace('_', '-')}"
        correlation_id = f"CORR-APPROVAL-{request.operation_type.upper().replace('_', '-')}"
        evidence_package_ready = False
        review_case_required = False
        review_case_id = None
        recommended_next_action = "complete_step_up_approval"

        if request.mobile_approval_status in {"rejected", "expired"}:
            decision = "blocked"
            risk_level = "high"
            risk_score = 85
            audit_event_id = "AUD-APPROVAL-MOBILE-REJECTED"
            correlation_id = "CORR-APPROVAL-MOBILE-REJECTED"
            reasons.append("Mobile approval was rejected or expired.")
            recommended_next_action = "block_operation_and_record_audit_event"
        elif request.mobile_approval_status != "approved" and approval_required:
            decision = "step_up_required"
            risk_level = "medium"
            risk_score = 55
            reasons.append("Step-up approval is still pending.")
        elif request.operation_type == "external_wallet_withdrawal":
            amount = request.amount_eur or 0
            if amount >= 5000 and request.is_new_destination:
                decision = "pending_review"
                risk_level = "critical"
                risk_score = 92
                audit_event_id = "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET"
                correlation_id = "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET"
                evidence_package_ready = True
                review_case_required = True
                review_case_id = "CASE-APPROVAL-HIGH-VALUE-NEW-WALLET"
                recommended_next_action = "route_to_customer_protection_review"
                reasons.append("High-value withdrawal to a new wallet requires review even after mobile approval.")
            else:
                decision = "approved"
                risk_level = "medium"
                risk_score = 48
                audit_event_id = "AUD-APPROVAL-WITHDRAWAL-KNOWN-WALLET"
                correlation_id = "CORR-APPROVAL-WITHDRAWAL-KNOWN-WALLET"
                recommended_next_action = "allow_sensitive_operation_attempt"
                reasons.append("Known destination and amount are within deterministic prototype threshold.")
        elif request.operation_type == "login_approval":
            decision = "approved"
            risk_level = "low"
            risk_score = 25
            audit_event_id = "AUD-APPROVAL-LOGIN"
            correlation_id = "CORR-APPROVAL-LOGIN"
            recommended_next_action = "allow_authenticated_session"
        elif request.operation_type == "security_device_change":
            decision = "pending_review"
            risk_level = "high"
            risk_score = 78
            audit_event_id = "AUD-APPROVAL-SECURITY-DEVICE-CHANGE"
            correlation_id = "CORR-APPROVAL-SECURITY-DEVICE-CHANGE"
            recommended_next_action = "temporary_withdrawal_freeze"
            reasons.append("Security device changes require customer-protection follow-up.")
        elif request.operation_type == "close_critical_review_case":
            mitigation_verified = bool(request.risk_context.get("mitigation_verified"))
            audit_event_id = "AUD-APPROVAL-REVIEW-CASE-CLOSURE"
            correlation_id = "CORR-APPROVAL-REVIEW-CASE-CLOSURE"
            decision = "approved" if mitigation_verified else "pending_review"
            risk_level = "high"
            risk_score = 70 if mitigation_verified else 82
            recommended_next_action = "close_case" if mitigation_verified else "verify_mitigation_before_closure"
        elif request.operation_type == "generate_sensitive_evidence_package":
            decision = "approved"
            risk_level = "high"
            risk_score = 66
            audit_event_id = "AUD-APPROVAL-SENSITIVE-EVIDENCE"
            correlation_id = "CORR-APPROVAL-SENSITIVE-EVIDENCE"
            recommended_next_action = "generate_deterministic_evidence_package"
        elif request.operation_type == "reset_demo_audit_data":
            decision = "pending_review"
            risk_level = "critical"
            risk_score = 90
            step_up_method = "dual_control_simulated"
            audit_event_id = "AUD-APPROVAL-DEMO-RESET"
            correlation_id = "CORR-APPROVAL-DEMO-RESET"
            recommended_next_action = "require_dual_control_confirmation"
        elif request.operation_type == "override_risk_decision":
            decision = "pending_review"
            risk_level = "critical"
            risk_score = 94
            step_up_method = "dual_control_simulated"
            audit_event_id = "AUD-APPROVAL-RISK-OVERRIDE"
            correlation_id = "CORR-APPROVAL-RISK-OVERRIDE"
            recommended_next_action = "route_override_to_risk_operations"
        else:
            decision = "approved"
            risk_level = operation.sensitivity_level if operation else "medium"
            risk_score = 50
            recommended_next_action = "record_approval_audit_event"

        if not request.device_trusted:
            risk_score = min(100, risk_score + 10)
            reasons.append("Device is not trusted.")
        if request.session_age_minutes > 30:
            risk_score = min(100, risk_score + 10)
            reasons.append("Session age requires additional scrutiny.")

        ai_threat_guard_applied = False
        ai_threat_case_id = None
        ai_threat_case_status = None
        ai_threat_guard_decision = None
        ai_threat_guard_reason = None
        operation_paused_until_review = False
        required_lifecycle_status = None
        secret_guard_applied = False
        secret_guard_case_id = None
        secret_guard_case_status = None
        secret_guard_decision = None
        secret_guard_reason = None
        operation_paused_by_secret_guard = False
        secret_guard_required_lifecycle_status = None

        if request.ai_threat_guard_required and request.linked_ai_threat_case_id:
            normalized_case_id = request.linked_ai_threat_case_id.strip().upper()
            guard = AI_THREAT_APPROVAL_GUARDS.get(normalized_case_id)
            if guard is not None:
                ai_threat_guard_applied = True
                ai_threat_case_id = normalized_case_id
                ai_threat_case_status = (
                    request.ai_threat_guard_status.strip().lower().replace(" ", "_")
                    if request.ai_threat_guard_status
                    else review_case_service.get_lifecycle_status(normalized_case_id)
                )
                ai_threat_guard_reason = (
                    request.ai_threat_guard_reason or guard["reason"]
                )
                required_lifecycle_status = "mitigated_or_closed"

                if ai_threat_case_status in ACTIVE_AI_THREAT_GUARD_STATUSES:
                    operation_paused_until_review = True
                    ai_threat_guard_decision = "pending_review"
                    decision = "blocked" if decision == "blocked" else "pending_review"
                    risk_level = "critical"
                    risk_score = max(risk_score, 96)
                    audit_event_id = guard["audit_event_id"]
                    correlation_id = guard["correlation_id"]
                    evidence_package_ready = True
                    review_case_required = True
                    review_case_id = normalized_case_id
                    recommended_next_action = guard["recommended_next_action"]
                    reasons.append(ai_threat_guard_reason)
                    reasons.append(
                        "Sensitive operation remains paused until the linked AI "
                        "Threat Defense review case is mitigated or closed."
                    )
                elif ai_threat_case_status in CLEARED_AI_THREAT_GUARD_STATUSES:
                    ai_threat_guard_decision = "cleared"
                    reasons.append(
                        "AI Threat Defense guard is cleared because the linked "
                        f"review case status is {ai_threat_case_status}."
                    )
                else:
                    operation_paused_until_review = True
                    ai_threat_guard_decision = "pending_review"
                    decision = "blocked" if decision == "blocked" else "pending_review"
                    risk_level = "critical"
                    risk_score = max(risk_score, 90)
                    audit_event_id = guard["audit_event_id"]
                    correlation_id = guard["correlation_id"]
                    review_case_required = True
                    review_case_id = normalized_case_id
                    recommended_next_action = guard["recommended_next_action"]
                    reasons.append(
                        "AI Threat Defense guard status is not cleared. "
                        "Human review is required before continuing."
                    )

        if request.secret_guard_required and request.linked_secret_guard_case_id:
            normalized_case_id = request.linked_secret_guard_case_id.strip().upper()
            guard = SECRET_GUARD_APPROVAL_GUARDS.get(normalized_case_id)
            if guard is not None:
                secret_guard_applied = True
                secret_guard_case_id = normalized_case_id
                secret_guard_case_status = (
                    request.secret_guard_status.strip().lower().replace(" ", "_")
                    if request.secret_guard_status
                    else review_case_service.get_lifecycle_status(normalized_case_id)
                )
                secret_guard_reason = request.secret_guard_reason or guard["reason"]
                secret_guard_required_lifecycle_status = "mitigated_or_closed"

                if secret_guard_case_status in ACTIVE_SECRET_GUARD_STATUSES:
                    operation_paused_by_secret_guard = True
                    secret_guard_decision = "pending_review"
                    decision = "blocked" if decision == "blocked" else "pending_review"
                    risk_level = "critical"
                    risk_score = max(risk_score, 96)
                    audit_event_id = guard["audit_event_id"]
                    correlation_id = guard["correlation_id"]
                    evidence_package_ready = True
                    review_case_required = True
                    review_case_id = normalized_case_id
                    recommended_next_action = SECRET_GUARD_RECOMMENDED_NEXT_ACTION
                    reasons.append(secret_guard_reason)
                    reasons.append(
                        "Sensitive operation remains paused until the linked "
                        "Secret Exposure Guard review case is mitigated or closed."
                    )
                elif secret_guard_case_status in CLEARED_SECRET_GUARD_STATUSES:
                    secret_guard_decision = "cleared"
                    reasons.append(
                        "Secret Exposure Guard is cleared because the linked "
                        f"review case status is {secret_guard_case_status}."
                    )
                else:
                    operation_paused_by_secret_guard = True
                    secret_guard_decision = "pending_review"
                    decision = "blocked" if decision == "blocked" else "pending_review"
                    risk_level = "critical"
                    risk_score = max(risk_score, 90)
                    audit_event_id = guard["audit_event_id"]
                    correlation_id = guard["correlation_id"]
                    review_case_required = True
                    review_case_id = normalized_case_id
                    recommended_next_action = SECRET_GUARD_RECOMMENDED_NEXT_ACTION
                    reasons.append(
                        "Secret Exposure Guard status is not cleared. Human "
                        "review is required before continuing."
                    )

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.actor_id,
            actor_type=request.actor_type,
            source_module="sensitive_approval",
            action="evaluate_sensitive_operation",
            object_type="sensitive_operation",
            object_id=request.operation_type,
            decision=decision,
            severity=risk_level,
            risk_score=risk_score,
            summary="Sensitive operation approval evaluated by deterministic prototype.",
            evidence_reference="EP-FROM-AUD-APPROVAL-HIGH-VALUE-NEW-WALLET" if evidence_package_ready else None,
            review_case_id=review_case_id,
            correlation_id=correlation_id,
            metadata={
                "amount_eur": request.amount_eur,
                "asset": request.asset,
                "destination_type": request.destination_type,
                "destination_id": request.destination_id,
                "is_new_destination": request.is_new_destination,
                "customer_confirmed": request.customer_confirmed,
                "mobile_approval_status": request.mobile_approval_status,
                "recommended_next_action": recommended_next_action,
                "ai_threat_guard_applied": ai_threat_guard_applied,
                "ai_threat_case_id": ai_threat_case_id,
                "ai_threat_case_status": ai_threat_case_status,
                "ai_threat_guard_decision": ai_threat_guard_decision,
                "operation_paused_until_review": operation_paused_until_review,
                "secret_guard_applied": secret_guard_applied,
                "secret_guard_case_id": secret_guard_case_id,
                "secret_guard_case_status": secret_guard_case_status,
                "secret_guard_decision": secret_guard_decision,
                "operation_paused_by_secret_guard": operation_paused_by_secret_guard,
            },
        )

        return SensitiveApprovalResponse(
            operation_id=operation.operation_id if operation else f"sensitive-op-{request.operation_type}",
            operation_type=request.operation_type,
            actor_id=request.actor_id,
            actor_type=request.actor_type,
            approval_required=approval_required,
            step_up_method=step_up_method,
            mobile_approval_status=request.mobile_approval_status,
            backend_risk_decision=decision,
            risk_level=risk_level,
            risk_score=risk_score,
            reasons=reasons,
            user_message=(
                "Mobile approval is simulated. Backend risk evaluation remains authoritative."
            ),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            evidence_package_ready=evidence_package_ready,
            review_case_required=review_case_required,
            review_case_id=review_case_id,
            recommended_next_action=recommended_next_action,
            ai_threat_guard_applied=ai_threat_guard_applied,
            ai_threat_case_id=ai_threat_case_id,
            ai_threat_case_status=ai_threat_case_status,
            ai_threat_guard_decision=ai_threat_guard_decision,
            ai_threat_guard_reason=ai_threat_guard_reason,
            operation_paused_until_review=operation_paused_until_review,
            required_lifecycle_status=required_lifecycle_status,
            secret_guard_applied=secret_guard_applied,
            secret_guard_case_id=secret_guard_case_id,
            secret_guard_case_status=secret_guard_case_status,
            secret_guard_decision=secret_guard_decision,
            secret_guard_reason=secret_guard_reason,
            operation_paused_by_secret_guard=operation_paused_by_secret_guard,
            secret_guard_required_lifecycle_status=secret_guard_required_lifecycle_status,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _operation(
        self,
        operation_type: str,
        title: str,
        description: str,
        actor_type: str,
        sensitivity_level: str,
        step_up_method: str,
        risk_triggers: list[str],
    ) -> SensitiveOperation:
        return SensitiveOperation(
            operation_id=f"SOP-{operation_type.upper().replace('_', '-')}",
            operation_type=operation_type,
            title=title,
            description=description,
            actor_type=actor_type,
            sensitivity_level=sensitivity_level,
            approval_required=step_up_method != "not_required",
            step_up_method=step_up_method,
            risk_triggers=risk_triggers,
            possible_outcomes=["approved", "pending_review", "blocked", "step_up_required"],
        )

    def _find_operation(self, operation_type: str) -> SensitiveOperation | None:
        return next(
            (
                operation
                for operation in self.list_operations()
                if operation.operation_type == operation_type
            ),
            None,
        )


sensitive_approval_service = SensitiveApprovalService()
