from app.schemas.api_security import (
    ApiSecurityControl,
    ApiSecurityEvent,
    ApiSecurityScenario,
    ApiSecuritySurface,
    ApiSensitiveOperation,
    EvaluateApiSecurityScenarioResponse,
)
from app.services.audit_service import audit_service


def _audit_token(value: str) -> str:
    return (
        value.strip()
        .upper()
        .replace("-", "_")
        .replace(" ", "_")
    )


class ApiSecurityService:
    """Provides deterministic API security control center demo data."""

    def list_controls(self) -> list[ApiSecurityControl]:
        return [
            ApiSecurityControl(
                control_id="apisec-ctrl-batching",
                title="GraphQL batching restriction",
                category="batching",
                description=(
                    "Restricts multi-operation envelopes for sensitive resolver "
                    "actions such as PIN verification, transfer authorization, "
                    "session token issuance, and credential reset."
                ),
                protected_operations=[
                    "verifyTransferPin",
                    "authorizeTransfer",
                    "issueSessionToken",
                    "resetCredential",
                ],
                decision_model=(
                    "One request = one sensitive operation = one authorization "
                    "decision = one audit event."
                ),
                evidence_outputs=[
                    "api_envelope_inspection",
                    "sensitive_operation_count",
                    "blocked_batching_audit_event",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-business-rate-limit",
                title="Business action rate limiting",
                category="rate_limit",
                description=(
                    "Applies rate limits to sensitive business actions rather "
                    "than only raw HTTP request counts."
                ),
                protected_operations=[
                    "PIN_VERIFY",
                    "TRANSFER_AUTHORIZE",
                    "TOKEN_ISSUE",
                    "BENEFICIARY_CHANGE",
                ],
                decision_model=(
                    "Limits apply by user, session, device, operation, target "
                    "object, failed attempts, and risk level."
                ),
                evidence_outputs=[
                    "business_action_counter",
                    "device_attempt_snapshot",
                    "rate_limit_decision_record",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-object-auth",
                title="Object-level authorization",
                category="authorization",
                description=(
                    "Checks ownership and staff entitlement before returning "
                    "sensitive account, transfer, wallet, or customer objects."
                ),
                protected_operations=[
                    "accountLookup",
                    "transferLookup",
                    "walletAccess",
                    "staffCustomerAccess",
                ],
                decision_model=(
                    "Authenticated user must also be authorized for the target "
                    "object."
                ),
                evidence_outputs=[
                    "object_authorization_decision",
                    "ownership_scope_snapshot",
                    "access_denial_audit_event",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-schema-exposure",
                title="Sensitive field exposure control",
                category="schema_exposure",
                description=(
                    "Prevents sensitive recovery, risk, profile, and device trust "
                    "fields from being exposed through public API contracts."
                ),
                protected_operations=[
                    "userProfile",
                    "accountRecovery",
                    "riskProfile",
                    "deviceTrust",
                ],
                decision_model=(
                    "Sensitive fields must not be exposed in public API contracts "
                    "unless explicitly required and authorized."
                ),
                evidence_outputs=[
                    "schema_field_review",
                    "sensitive_field_request_log",
                    "contract_exposure_exception_record",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-high-risk-mutation",
                title="High-risk mutation control",
                category="mutation_control",
                description=(
                    "Requires stronger backend checks for transfers, beneficiary "
                    "changes, and external digital asset wallet withdrawals."
                ),
                protected_operations=[
                    "createTransfer",
                    "changeBeneficiary",
                    "externalWalletWithdrawal",
                ],
                decision_model=(
                    "High-risk mutations require idempotency, ownership validation, "
                    "step-up authentication, and audit logging."
                ),
                evidence_outputs=[
                    "idempotency_key_record",
                    "mutation_risk_score",
                    "step_up_challenge_record",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-token-monitoring",
                title="Token issuance monitoring",
                category="token_security",
                description=(
                    "Monitors session token issuance, refresh, and device trust "
                    "token behavior for unusual repetition or context mismatch."
                ),
                protected_operations=[
                    "issueSessionToken",
                    "refreshSession",
                    "deviceTrustToken",
                ],
                decision_model=(
                    "Token issuance must be monitored for repetition, device "
                    "mismatch, and unusual session behavior."
                ),
                evidence_outputs=[
                    "token_issue_attempt_counter",
                    "session_context_snapshot",
                    "device_trust_delta",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-audit-logging",
                title="Audit logging for sensitive actions",
                category="audit_logging",
                description=(
                    "Creates audit evidence for every sensitive action decision "
                    "made at the backend boundary."
                ),
                protected_operations=["all sensitive operations"],
                decision_model="Every sensitive operation creates an audit event.",
                evidence_outputs=[
                    "api_security_audit_event",
                    "authorization_decision_record",
                    "risk_score_snapshot",
                ],
                enabled=True,
            ),
            ApiSecurityControl(
                control_id="apisec-ctrl-step-up",
                title="Step-up authentication",
                category="step_up_authentication",
                description=(
                    "Requires stronger verification before high-risk account, "
                    "payment, credential, or wallet actions can continue."
                ),
                protected_operations=[
                    "largeTransfer",
                    "externalWithdrawal",
                    "credentialChange",
                ],
                decision_model=(
                    "Higher-risk operations require stronger verification before "
                    "execution."
                ),
                evidence_outputs=[
                    "step_up_required_event",
                    "challenge_delivery_record",
                    "review_queue_reference",
                ],
                enabled=True,
            ),
        ]

    def list_events(self) -> list[ApiSecurityEvent]:
        return [
            ApiSecurityEvent(
                event_id="APISEC-2026-001",
                title="GraphQL batching attempt on PIN verification",
                api_surface="graphql",
                operation_name="verifyTransferPin",
                risk_type="GraphQL batching abuse",
                severity="critical",
                decision="block",
                status="blocked",
                triggered_controls=[
                    "GraphQL batching restriction",
                    "Business action rate limiting",
                    "Audit logging for sensitive actions",
                ],
                business_action="PIN_VERIFY",
                summary=(
                    "Multiple PIN verification attempts were detected inside a "
                    "single API envelope."
                ),
                recommended_action=(
                    "Block the request, increment business action attempt "
                    "counters, and preserve audit evidence."
                ),
                audit_event="audit-api-security-pin-batching-001",
                created_at="2026-06-14T09:10:00+03:00",
            ),
            ApiSecurityEvent(
                event_id="APISEC-2026-002",
                title="Object-level authorization failure on transfer lookup",
                api_surface="graphql",
                operation_name="transfer",
                risk_type="Object access violation",
                severity="critical",
                decision="block",
                status="blocked",
                triggered_controls=[
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                affected_object="transfer-demo-foreign-object",
                business_action="TRANSFER_LOOKUP",
                summary=(
                    "Authenticated session attempted to access a transfer object "
                    "outside its allowed ownership scope."
                ),
                recommended_action=(
                    "Return not found, block object disclosure, and preserve "
                    "authorization failure evidence."
                ),
                audit_event="audit-api-security-object-auth-002",
                created_at="2026-06-14T09:16:00+03:00",
            ),
            ApiSecurityEvent(
                event_id="APISEC-2026-003",
                title="Sensitive field exposure request",
                api_surface="graphql",
                operation_name="userProfile",
                risk_type="Sensitive schema exposure",
                severity="high",
                decision="review_required",
                status="under_review",
                triggered_controls=[
                    "Sensitive field exposure control",
                    "Audit logging for sensitive actions",
                ],
                business_action="USER_PROFILE_READ",
                summary=(
                    "Request attempted to access fields that should not be "
                    "exposed through the public API contract."
                ),
                recommended_action=(
                    "Review schema exposure and restrict sensitive fields from "
                    "public queries."
                ),
                audit_event="audit-api-security-schema-exposure-003",
                created_at="2026-06-14T09:24:00+03:00",
            ),
            ApiSecurityEvent(
                event_id="APISEC-2026-004",
                title="High-risk transfer mutation requires step-up",
                api_surface="graphql",
                operation_name="createTransfer",
                risk_type="High-risk mutation",
                severity="high",
                decision="step_up_required",
                status="under_review",
                triggered_controls=[
                    "High-risk mutation control",
                    "Step-up authentication",
                    "Audit logging for sensitive actions",
                ],
                business_action="TRANSFER_CREATE",
                summary=(
                    "Transfer mutation exceeded prototype risk threshold and "
                    "requires stronger verification before execution."
                ),
                recommended_action=(
                    "Require step-up authentication and create an audit event "
                    "before continuing."
                ),
                audit_event="audit-api-security-transfer-step-up-004",
                created_at="2026-06-14T09:31:00+03:00",
            ),
            ApiSecurityEvent(
                event_id="APISEC-2026-005",
                title="Token issuance anomaly",
                api_surface="auth",
                operation_name="issueSessionToken",
                risk_type="Token issuance anomaly",
                severity="medium",
                decision="review_required",
                status="new",
                triggered_controls=[
                    "Token issuance monitoring",
                    "Business action rate limiting",
                ],
                business_action="TOKEN_ISSUE",
                summary=(
                    "Repeated token issuance attempts were detected for the same "
                    "session and device context."
                ),
                recommended_action=(
                    "Throttle token issuance and review session trust signals."
                ),
                audit_event="audit-api-security-token-issue-005",
                created_at="2026-06-14T09:42:00+03:00",
            ),
            ApiSecurityEvent(
                event_id="APISEC-2026-006",
                title="Beneficiary mutation abuse pattern",
                api_surface="payments",
                operation_name="changeBeneficiary",
                risk_type="Beneficiary mutation abuse",
                severity="high",
                decision="step_up_required",
                status="escalated",
                triggered_controls=[
                    "High-risk mutation control",
                    "Business action rate limiting",
                    "Step-up authentication",
                ],
                business_action="BENEFICIARY_CHANGE",
                summary=(
                    "Repeated beneficiary changes were detected before attempted "
                    "transfer execution."
                ),
                recommended_action=(
                    "Require step-up authentication, cooldown, and compliance "
                    "review if pattern continues."
                ),
                audit_event="audit-api-security-beneficiary-006",
                created_at="2026-06-14T09:55:00+03:00",
            ),
        ]

    def list_surfaces(self) -> list[ApiSecuritySurface]:
        return [
            self._surface(
                "surface-customer-graphql",
                "Customer GraphQL API",
                "graphql",
                "Concentrates customer-facing reads and mutations where batching, resolver authorization, and schema exposure need strict controls.",
                ["verifyTransferPin", "authorizeTransfer", "userProfile"],
                [
                    "GraphQL batching restriction",
                    "Object-level authorization",
                    "Sensitive field exposure control",
                ],
                "restricted",
            ),
            self._surface(
                "surface-payment-auth",
                "Payment authorization API",
                "rest",
                "Authorizes payment creation, transfer confirmation, and beneficiary changes with business action limits.",
                ["createTransfer", "authorizeTransfer", "changeBeneficiary"],
                [
                    "Business action rate limiting",
                    "High-risk mutation control",
                    "Step-up authentication",
                ],
                "hardened",
            ),
            self._surface(
                "surface-digital-assets-withdrawal",
                "Digital assets withdrawal API",
                "rest",
                "Controls simulated external wallet withdrawals as high-risk irreversible actions requiring stronger verification.",
                ["externalWalletWithdrawal", "walletAccess"],
                [
                    "High-risk mutation control",
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                "restricted",
            ),
            self._surface(
                "surface-auth-token",
                "Authentication and token API",
                "auth",
                "Issues and refreshes simulated session credentials while monitoring repetition and device context anomalies.",
                ["issueSessionToken", "refreshSession", "deviceTrustToken"],
                [
                    "Token issuance monitoring",
                    "Business action rate limiting",
                    "Audit logging for sensitive actions",
                ],
                "monitored",
            ),
            self._surface(
                "surface-staff-access",
                "Staff customer access API",
                "internal_api",
                "Requires explicit customer authorization and staff entitlement before customer object access.",
                ["staffCustomerAccess", "accountLookup", "walletAccess"],
                [
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                "hardened",
            ),
            self._surface(
                "surface-reporting-audit",
                "Reporting and audit API",
                "internal_api",
                "Provides read access to evidence records while preserving audit trail integrity.",
                ["auditEventLookup", "reportExport", "caseEvidenceAccess"],
                [
                    "Object-level authorization",
                    "Sensitive field exposure control",
                    "Audit logging for sensitive actions",
                ],
                "monitored",
            ),
        ]

    def list_sensitive_operations(self) -> list[ApiSensitiveOperation]:
        return [
            self._operation(
                "op-pin-verify",
                "verifyTransferPin",
                "pin",
                "critical",
                [
                    "GraphQL batching restriction",
                    "Business action rate limiting",
                    "Audit logging for sensitive actions",
                ],
                True,
                False,
                False,
            ),
            self._operation(
                "op-transfer-authorize",
                "authorizeTransfer",
                "transfer",
                "critical",
                [
                    "Business action rate limiting",
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                True,
                True,
                False,
            ),
            self._operation(
                "op-transfer-create",
                "createTransfer",
                "transfer",
                "high",
                [
                    "High-risk mutation control",
                    "Step-up authentication",
                    "Audit logging for sensitive actions",
                ],
                True,
                True,
                False,
            ),
            self._operation(
                "op-beneficiary-change",
                "changeBeneficiary",
                "beneficiary",
                "high",
                [
                    "High-risk mutation control",
                    "Business action rate limiting",
                    "Step-up authentication",
                ],
                True,
                True,
                False,
            ),
            self._operation(
                "op-token-issue",
                "issueSessionToken",
                "token",
                "high",
                [
                    "Token issuance monitoring",
                    "Business action rate limiting",
                    "Audit logging for sensitive actions",
                ],
                True,
                False,
                False,
            ),
            self._operation(
                "op-account-lookup",
                "accountLookup",
                "account_lookup",
                "medium",
                [
                    "Object-level authorization",
                    "Sensitive field exposure control",
                ],
                True,
                False,
                True,
            ),
            self._operation(
                "op-transfer-lookup",
                "transferLookup",
                "transfer",
                "high",
                [
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                True,
                False,
                True,
            ),
            self._operation(
                "op-wallet-withdrawal",
                "externalWalletWithdrawal",
                "wallet_withdrawal",
                "critical",
                [
                    "High-risk mutation control",
                    "Step-up authentication",
                    "Audit logging for sensitive actions",
                ],
                True,
                True,
                False,
            ),
            self._operation(
                "op-staff-customer-access",
                "staffCustomerAccess",
                "staff_access",
                "critical",
                [
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
                True,
                True,
                False,
            ),
        ]

    def list_scenarios(self) -> list[ApiSecurityScenario]:
        return [
            ApiSecurityScenario(
                scenario_id="graphql_batching_pin_verification",
                title="GraphQL batching PIN verification",
                description=(
                    "Multiple PIN verification attempts are sent through one "
                    "GraphQL envelope."
                ),
                risk_indicators=[
                    "batching_detected",
                    "high_attempt_count",
                    "pin_operation",
                ],
                expected_decision="block",
                recommended_controls=[
                    "GraphQL batching restriction",
                    "Business action rate limiting",
                    "Audit logging for sensitive actions",
                ],
            ),
            ApiSecurityScenario(
                scenario_id="object_level_authorization_failure",
                title="Object-level authorization failure",
                description=(
                    "An authenticated session requests an object outside its "
                    "authorized ownership scope."
                ),
                risk_indicators=["object_authorized_false", "object_lookup"],
                expected_decision="block",
                recommended_controls=[
                    "Object-level authorization",
                    "Audit logging for sensitive actions",
                ],
            ),
            ApiSecurityScenario(
                scenario_id="sensitive_field_exposure",
                title="Sensitive field exposure",
                description=(
                    "A public query requests recovery, risk, or device trust "
                    "fields."
                ),
                risk_indicators=["sensitive_fields_requested", "public_contract"],
                expected_decision="review_required",
                recommended_controls=[
                    "Sensitive field exposure control",
                    "Audit logging for sensitive actions",
                ],
            ),
            ApiSecurityScenario(
                scenario_id="high_risk_transfer_mutation",
                title="High-risk transfer mutation",
                description=(
                    "A transfer mutation exceeds the prototype risk threshold "
                    "and requires stronger verification."
                ),
                risk_indicators=["transfer_operation", "high_risk_mutation"],
                expected_decision="step_up_required",
                recommended_controls=[
                    "High-risk mutation control",
                    "Step-up authentication",
                    "Audit logging for sensitive actions",
                ],
            ),
            ApiSecurityScenario(
                scenario_id="token_issuance_anomaly",
                title="Token issuance anomaly",
                description=(
                    "Repeated token issuance attempts occur for the same "
                    "session and device context."
                ),
                risk_indicators=["token_operation", "high_attempt_count"],
                expected_decision="review_required",
                recommended_controls=[
                    "Token issuance monitoring",
                    "Business action rate limiting",
                ],
            ),
            ApiSecurityScenario(
                scenario_id="beneficiary_mutation_abuse",
                title="Beneficiary mutation abuse",
                description=(
                    "Repeated beneficiary changes occur before transfer "
                    "execution."
                ),
                risk_indicators=["beneficiary_operation", "high_attempt_count"],
                expected_decision="step_up_required",
                recommended_controls=[
                    "High-risk mutation control",
                    "Business action rate limiting",
                    "Step-up authentication",
                ],
            ),
        ]

    def evaluate_scenario(
        self,
        scenario_id: str,
        operation_name: str,
        attempts: int,
        object_authorized: bool,
        batching_detected: bool,
        sensitive_fields_requested: bool,
    ) -> EvaluateApiSecurityScenarioResponse:
        operation_name_lower = operation_name.lower()
        triggered_controls: list[str] = ["Audit logging for sensitive actions"]
        score = 15
        reasons = ["Baseline sensitive API inspection is active."]

        if batching_detected:
            score += 35
            triggered_controls.append("GraphQL batching restriction")
            reasons.append("Batching was detected for a sensitive API operation.")

        if not object_authorized:
            score += 45
            triggered_controls.append("Object-level authorization")
            reasons.append("The target object is outside the authorized scope.")

        if sensitive_fields_requested:
            score += 30
            triggered_controls.append("Sensitive field exposure control")
            reasons.append("Sensitive fields were requested through the API contract.")

        if attempts > 10:
            score += 30
            triggered_controls.append("Business action rate limiting")
            reasons.append("The attempt count is above the critical threshold.")
        elif attempts > 5:
            score += 20
            triggered_controls.append("Business action rate limiting")
            reasons.append("The attempt count exceeds the business action threshold.")

        if any(
            marker in operation_name_lower
            for marker in ["pin", "transfer", "token", "withdrawal", "beneficiary"]
        ):
            score += 20
            reasons.append("The operation is sensitive for financial authorization.")

        if any(marker in operation_name_lower for marker in ["transfer", "withdrawal", "beneficiary"]):
            triggered_controls.append("High-risk mutation control")
            triggered_controls.append("Step-up authentication")

        if "token" in operation_name_lower or "session" in operation_name_lower:
            triggered_controls.append("Token issuance monitoring")

        score = min(score, 100)
        unique_controls = list(dict.fromkeys(triggered_controls))

        if score >= 85:
            severity = "critical"
            decision = "block"
            recommended_action = (
                "Block the API request, preserve the audit event, and route the "
                "case for security review."
            )
        elif score >= 70:
            severity = "high"
            decision = "step_up_required"
            recommended_action = (
                "Require step-up authentication before the operation can continue."
            )
        elif score >= 50:
            severity = "medium"
            decision = "review_required"
            recommended_action = (
                "Queue the API activity for review and keep enhanced monitoring active."
            )
        else:
            severity = "low"
            decision = "allow"
            recommended_action = (
                "Allow the operation while recording the authorization and audit decision."
            )

        if scenario_id == "graphql_batching_pin_verification":
            audit_event_id = "AUD-API-GRAPHQL-PIN"
            correlation_id = "CORR-API-GRAPHQL-PIN"
        else:
            audit_event_id = f"AUD-API-{_audit_token(scenario_id)}"
            correlation_id = f"CORR-API-{_audit_token(scenario_id)}"

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="api-security-engine",
            actor_type="service",
            source_module="api_security",
            action="evaluate_scenario",
            object_type="api_scenario",
            object_id=scenario_id,
            decision=decision,
            severity=severity,
            risk_score=score,
            summary="API security scenario evaluation and backend decision.",
            correlation_id=correlation_id,
            metadata={
                "operation_name": operation_name,
                "attempts": attempts,
                "object_authorized": object_authorized,
                "batching_detected": batching_detected,
                "sensitive_fields_requested": sensitive_fields_requested,
                "triggered_controls": unique_controls,
            },
        )

        return EvaluateApiSecurityScenarioResponse(
            risk_score=score,
            severity=severity,
            decision=decision,
            triggered_controls=unique_controls,
            audit_event_required=True,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            recommended_action=recommended_action,
            explanation=(
                f"Scenario {scenario_id} evaluated for {operation_name}. "
                + " ".join(reasons)
            ),
        )

    def _surface(
        self,
        surface_id: str,
        name: str,
        surface_type: str,
        risk_summary: str,
        sensitive_operations: list[str],
        controls_applied: list[str],
        status: str,
    ) -> ApiSecuritySurface:
        return ApiSecuritySurface(
            surface_id=surface_id,
            name=name,
            surface_type=surface_type,
            risk_summary=risk_summary,
            sensitive_operations=sensitive_operations,
            controls_applied=controls_applied,
            status=status,
        )

    def _operation(
        self,
        operation_id: str,
        name: str,
        category: str,
        risk_level: str,
        required_controls: list[str],
        audit_required: bool,
        step_up_required: bool,
        batching_allowed: bool,
    ) -> ApiSensitiveOperation:
        return ApiSensitiveOperation(
            operation_id=operation_id,
            name=name,
            category=category,
            risk_level=risk_level,
            required_controls=required_controls,
            audit_required=audit_required,
            step_up_required=step_up_required,
            batching_allowed=batching_allowed,
        )


api_security_service = ApiSecurityService()
