from datetime import datetime, timezone

from app.schemas.secret_exposure_guard import (
    SecretExposureGuardEvaluationRequest,
    SecretExposureGuardEvaluationResponse,
    SecretExposureSurface,
)
from app.services.audit_service import audit_service


SIGNAL_BASE_SCORES = {
    "possible_secret_in_documentation": 65,
    "possible_secret_in_logs": 75,
    "possible_secret_in_prompt_context": 80,
    "possible_secret_in_config": 85,
    "possible_secret_in_evidence_package": 85,
    "possible_secret_in_review_case": 80,
    "possible_secret_in_api_response": 85,
    "possible_secret_in_test_fixture": 65,
    "possible_custodian_secret_reference": 90,
    "possible_cloud_secret_reference": 90,
}

SIGNAL_MAPPINGS = {
    "possible_secret_in_documentation": (
        "AUD-SECRET-GUARD-DOCUMENTATION",
        "CORR-SECRET-GUARD-DOCUMENTATION",
        "CASE-SECRET-GUARD-DOCUMENTATION",
    ),
    "possible_secret_in_logs": (
        "AUD-SECRET-GUARD-LOGS",
        "CORR-SECRET-GUARD-LOGS",
        "CASE-SECRET-GUARD-LOGS",
    ),
    "possible_secret_in_prompt_context": (
        "AUD-SECRET-GUARD-PROMPT-CONTEXT",
        "CORR-SECRET-GUARD-PROMPT-CONTEXT",
        "CASE-SECRET-GUARD-PROMPT-CONTEXT",
    ),
    "possible_secret_in_config": (
        "AUD-SECRET-GUARD-CONFIG",
        "CORR-SECRET-GUARD-CONFIG",
        "CASE-SECRET-GUARD-CONFIG",
    ),
    "possible_secret_in_evidence_package": (
        "AUD-SECRET-GUARD-EVIDENCE-PACKAGE",
        "CORR-SECRET-GUARD-EVIDENCE-PACKAGE",
        "CASE-SECRET-GUARD-EVIDENCE-PACKAGE",
    ),
    "possible_secret_in_review_case": (
        "AUD-SECRET-GUARD-REVIEW-CASE",
        "CORR-SECRET-GUARD-REVIEW-CASE",
        "CASE-SECRET-GUARD-REVIEW-CASE",
    ),
    "possible_secret_in_api_response": (
        "AUD-SECRET-GUARD-API-RESPONSE",
        "CORR-SECRET-GUARD-API-RESPONSE",
        "CASE-SECRET-GUARD-API-RESPONSE",
    ),
    "possible_secret_in_test_fixture": (
        "AUD-SECRET-GUARD-TEST-FIXTURE",
        "CORR-SECRET-GUARD-TEST-FIXTURE",
        "CASE-SECRET-GUARD-TEST-FIXTURE",
    ),
    "possible_custodian_secret_reference": (
        "AUD-SECRET-GUARD-CUSTODIAN-SECRET",
        "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
        "CASE-SECRET-GUARD-CUSTODIAN-SECRET",
    ),
    "possible_cloud_secret_reference": (
        "AUD-SECRET-GUARD-CLOUD-SECRET",
        "CORR-SECRET-GUARD-CLOUD-SECRET",
        "CASE-SECRET-GUARD-CLOUD-SECRET",
    ),
}


class SecretExposureGuardService:
    """Deterministic metadata-only secret exposure guard."""

    def list_surfaces(self) -> list[SecretExposureSurface]:
        return [
            self._surface("DOCS-README", "README documentation", "documentation", "medium"),
            self._surface("DOCS-SECURITY", "Security documentation", "documentation", "high"),
            self._surface("DOCS-ARCHITECTURE", "Architecture documentation", "documentation", "high"),
            self._surface("LOGS-BACKEND", "Backend logs", "logs", "high"),
            self._surface("LOGS-FRONTEND", "Frontend logs", "logs", "high"),
            self._surface("PROMPTS-AI-WORKFLOW", "AI workflow prompts", "prompt_context", "critical"),
            self._surface("CONFIG-ENV", "Environment configuration", "configuration", "critical"),
            self._surface("CONFIG-LOCAL", "Local configuration", "configuration", "high"),
            self._surface("EVIDENCE-PACKAGES", "Evidence packages", "evidence", "critical"),
            self._surface("REVIEW-CASES", "Review cases", "review_workflow", "high"),
            self._surface("API-RESPONSES", "API responses", "backend_api", "high"),
            self._surface("TEST-FIXTURES", "Test fixtures", "testing", "medium"),
            self._surface("FUTURE-CLOUD-SECRETS", "Future cloud secret references", "future_cloud", "critical"),
            self._surface("FUTURE-CUSTODIAN-SECRETS", "Future custodian secret references", "future_custodian", "critical"),
        ]

    def list_signals(self) -> list[str]:
        return list(SIGNAL_BASE_SCORES.keys())

    def evaluate(
        self,
        request: SecretExposureGuardEvaluationRequest,
    ) -> SecretExposureGuardEvaluationResponse:
        signal_type = request.signal_type.strip()
        if signal_type not in SIGNAL_BASE_SCORES:
            raise ValueError(f"Unknown secret exposure signal: {signal_type}")

        surface_id = request.surface_id.strip().upper()
        if surface_id not in {surface.surface_id for surface in self.list_surfaces()}:
            raise ValueError(f"Unknown secret exposure surface: {surface_id}")

        risk_score = self._risk_score(signal_type, request)
        severity = self._severity(risk_score)
        decision = self._decision(request, risk_score, severity)
        audit_event_id, correlation_id, review_case_id = SIGNAL_MAPPINGS[signal_type]
        ai_threat_case_id = self._normalized_ai_threat_case_id(
            request.linked_ai_threat_case_id
        )

        if ai_threat_case_id == "CASE-AI-THREAT-SECRET-EXPOSURE":
            audit_event_id = "AUD-SECRET-GUARD-LINKED-AI-THREAT-SECRET-EXPOSURE"
            correlation_id = "CORR-AI-THREAT-SECRET-EXPOSURE"
            review_case_id = "CASE-AI-THREAT-SECRET-EXPOSURE"

        evidence_package_ready = severity in {"medium", "high", "critical"}
        review_case_required = severity in {"high", "critical"}
        operation_guard_recommended = severity == "critical"
        effective_review_case_id = review_case_id if review_case_required else None
        recommended_next_actions = self._recommended_next_actions(
            request=request,
            severity=severity,
            review_case_required=review_case_required,
            operation_guard_recommended=operation_guard_recommended,
            ai_threat_case_id=ai_threat_case_id,
        )

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type=self._audit_actor_type(request.actor_type),
            source_module="secret_exposure_guard",
            action="evaluate_secret_exposure_signal",
            object_type="secret_exposure_signal",
            object_id=signal_type,
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=(
                "Secret Exposure Guard evaluated metadata-only exposure signals. "
                "No raw secret value was stored or echoed."
            ),
            evidence_reference=(
                f"EP-FROM-{audit_event_id}" if evidence_package_ready else None
            ),
            review_case_id=effective_review_case_id,
            correlation_id=correlation_id,
            metadata={
                "surface_id": surface_id,
                "source_reference": request.source_reference,
                "exposure_scope": request.exposure_scope,
                "ai_assisted_context": request.ai_assisted_context,
                "ai_threat_case_id": ai_threat_case_id,
                "secret_value_stored": False,
                "raw_secret_echoed": False,
                "recommended_next_actions": recommended_next_actions,
            },
        )

        return SecretExposureGuardEvaluationResponse(
            signal_type=signal_type,
            surface_id=surface_id,
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            secret_value_stored=False,
            raw_secret_echoed=False,
            ai_threat_case_id=ai_threat_case_id,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or correlation_id,
            evidence_package_ready=evidence_package_ready,
            review_case_required=review_case_required,
            review_case_id=effective_review_case_id,
            operation_guard_recommended=operation_guard_recommended,
            recommended_next_actions=recommended_next_actions,
            created_at=datetime.now(timezone.utc),
        )

    def _risk_score(
        self,
        signal_type: str,
        request: SecretExposureGuardEvaluationRequest,
    ) -> int:
        if signal_type == "possible_secret_in_documentation" and not self._has_secret_indicator(request):
            return 35

        score = SIGNAL_BASE_SCORES[signal_type]
        if request.contains_raw_secret_value:
            score += 25
        if request.contains_secret_like_pattern:
            score += 15
        if request.contains_credential_label:
            score += 10
        if request.contains_private_key_reference:
            score += 20
        if request.contains_seed_phrase_reference:
            score += 20
        if request.contains_api_token_reference:
            score += 15
        if request.contains_cloud_secret_reference:
            score += 20
        if request.contains_custodian_secret_reference:
            score += 20
        score += {
            "public": 25,
            "repository": 15,
            "logs": 15,
            "prompt_context": 20,
            "evidence_package": 15,
            "review_case": 15,
        }.get(request.exposure_scope, 0)
        if request.ai_assisted_context:
            score += 15
        return min(score, 100)

    def _severity(self, risk_score: int) -> str:
        if risk_score >= 85:
            return "critical"
        if risk_score >= 65:
            return "high"
        if risk_score >= 40:
            return "medium"
        return "low"

    def _decision(
        self,
        request: SecretExposureGuardEvaluationRequest,
        risk_score: int,
        severity: str,
    ) -> str:
        if request.contains_raw_secret_value and risk_score >= 90:
            return "block"
        if (
            request.contains_cloud_secret_reference
            or request.contains_custodian_secret_reference
        ) and severity == "critical":
            return "review_required"
        if severity == "critical":
            return "review_required"
        if severity == "high":
            return "elevate"
        if severity == "medium":
            return "redact"
        return "allow"

    def _recommended_next_actions(
        self,
        *,
        request: SecretExposureGuardEvaluationRequest,
        severity: str,
        review_case_required: bool,
        operation_guard_recommended: bool,
        ai_threat_case_id: str | None,
    ) -> list[str]:
        actions = [
            "verify_no_secret_value_is_stored",
            "redact_sensitive_material",
        ]
        if severity in {"medium", "high", "critical"}:
            actions.append("preserve_evidence_without_secret_value")
        if request.contains_raw_secret_value or request.contains_credential_label:
            actions.append("rotate_exposed_credentials_where_applicable")
        if severity in {"high", "critical"}:
            actions.append("restrict_access_to_affected_surface")
        if review_case_required:
            actions.append("create_human_review_case")
        if request.exposure_scope == "prompt_context":
            actions.append("review_prompt_context_exposure")
        if request.signal_type == "possible_secret_in_documentation":
            actions.append("review_documentation_exposure")
        if request.exposure_scope in {"logs", "repository"} or request.signal_type == "possible_secret_in_config":
            actions.append("review_config_and_logs")
        if operation_guard_recommended:
            actions.append("pause_sensitive_operations_if_related")
        if severity == "critical":
            actions.append("notify_security_architecture_team")
        if ai_threat_case_id:
            actions.append("correlate_with_ai_threat_defense_case")
        return list(dict.fromkeys(actions))

    def _has_secret_indicator(
        self,
        request: SecretExposureGuardEvaluationRequest,
    ) -> bool:
        return any(
            [
                request.contains_raw_secret_value,
                request.contains_secret_like_pattern,
                request.contains_credential_label,
                request.contains_private_key_reference,
                request.contains_seed_phrase_reference,
                request.contains_api_token_reference,
                request.contains_cloud_secret_reference,
                request.contains_custodian_secret_reference,
                request.ai_assisted_context,
                request.exposure_scope in {
                    "public",
                    "repository",
                    "logs",
                    "prompt_context",
                    "evidence_package",
                    "review_case",
                },
            ]
        )

    def _normalized_ai_threat_case_id(self, case_id: str | None) -> str | None:
        if not case_id:
            return None
        normalized = case_id.strip().upper()
        return normalized or None

    def _audit_actor_type(self, actor_type: str) -> str:
        normalized = actor_type.strip().lower()
        if normalized in {"staff", "system", "customer", "service"}:
            return normalized
        return "system"

    def _surface(
        self,
        surface_id: str,
        title: str,
        category: str,
        sensitivity_level: str,
    ) -> SecretExposureSurface:
        return SecretExposureSurface(
            surface_id=surface_id,
            title=title,
            category=category,
            description=(
                "Metadata-only defensive surface for secret exposure guard evaluation."
            ),
            sensitivity_level=sensitivity_level,
        )


secret_exposure_guard_service = SecretExposureGuardService()
