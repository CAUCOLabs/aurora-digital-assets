from datetime import datetime, timezone

from app.schemas.agent_permissions import (
    AgentPermissionDefinition,
    AgentPermissionEvaluationRequest,
    AgentPermissionEvaluationResponse,
    AgentPermissionGrantPreviewRequest,
    AgentPermissionGrantPreviewResponse,
    AgentPermissionProfile,
    AgentPermissionsForAgentResponse,
)
from app.schemas.agent_registry import AgentRegistryDetail
from app.services.agent_passport_service import agent_passport_service
from app.services.agent_registry_service import agent_registry_service
from app.services.audit_service import audit_service


PERMISSION_SAFETY_NOTICE = (
    "Local deterministic permission evaluation only. No real execution, "
    "custodian API access, blockchain transaction, withdrawal approval, "
    "external tool invocation, or credential access is granted."
)

SECRET_SAFETY_NOTICE = (
    "Local deterministic permission evaluation only. No raw credentials, "
    "tokens, API keys, passwords, private keys, seed phrases, or secrets are "
    "stored or exposed."
)

CUSTODIAN_SAFETY_NOTICE = (
    "Local deterministic permission evaluation only. No real custodian API "
    "access is granted."
)

BLOCKED_AGENT_STATUSES = {"suspended", "revoked", "expired"}
HIGH_RISK_LEVELS = {"high", "critical"}
SECRET_PERMISSIONS = {"access_secrets"}
CUSTODY_PERMISSIONS = {"access_custodian_apis"}
WITHDRAWAL_BLOCKED_PERMISSIONS = {"trigger_withdrawals", "approve_withdrawals"}
POLICY_BLOCKED_PERMISSIONS = {
    "delete_or_modify_records",
    "modify_user_permissions",
}


def _permission(
    permission_id: str,
    label: str,
    category: str,
    risk_level: str,
    description: str,
    *,
    sensitive: bool = False,
    human_approval_required: bool = False,
    evidence_required: bool = False,
    review_case_required: bool = False,
    allowed_for_agent_types: list[str] | None = None,
    prohibited_for_agent_types: list[str] | None = None,
    blocked_by_default: bool = True,
) -> AgentPermissionDefinition:
    return AgentPermissionDefinition(
        permission_id=permission_id,
        label=label,
        category=category,
        risk_level=risk_level,
        description=description,
        sensitive=sensitive,
        human_approval_required=human_approval_required,
        evidence_required=evidence_required,
        review_case_required=review_case_required,
        allowed_for_agent_types=allowed_for_agent_types or [],
        prohibited_for_agent_types=prohibited_for_agent_types or [],
        blocked_by_default=blocked_by_default,
    )


PERMISSION_CATALOG = {
    "read_public_data": _permission(
        "read_public_data",
        "Read public data",
        "read_public_data",
        "low",
        "Read non-sensitive prototype public reference data.",
        blocked_by_default=False,
    ),
    "read_internal_documents": _permission(
        "read_internal_documents",
        "Read internal documents",
        "read_internal_documents",
        "medium",
        "Read approved internal prototype documentation.",
    ),
    "read_customer_metadata": _permission(
        "read_customer_metadata",
        "Read customer metadata",
        "read_customer_metadata",
        "high",
        "Read limited mock customer metadata for review workflows.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "read_balances": _permission(
        "read_balances",
        "Read balances",
        "read_balances",
        "high",
        "Read mock balance data.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "read_transactions": _permission(
        "read_transactions",
        "Read transactions",
        "read_transactions",
        "high",
        "Read mock transaction data.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "read_audit_events": _permission(
        "read_audit_events",
        "Read audit events",
        "read_audit_events",
        "medium",
        "Read audit event metadata in the local prototype.",
    ),
    "create_reports": _permission(
        "create_reports",
        "Create reports",
        "create_reports",
        "medium",
        "Prepare deterministic internal reports from approved mock data.",
    ),
    "create_review_cases": _permission(
        "create_review_cases",
        "Create review cases",
        "create_review_cases",
        "medium",
        "Prepare review cases for human governance review.",
        evidence_required=True,
    ),
    "create_evidence_packages": _permission(
        "create_evidence_packages",
        "Create evidence packages",
        "create_evidence_packages",
        "medium",
        "Prepare evidence packages from approved prototype sources.",
        evidence_required=True,
    ),
    "suggest_risk_decisions": _permission(
        "suggest_risk_decisions",
        "Suggest risk decisions",
        "suggest_risk_decisions",
        "high",
        "Suggest non-binding risk triage decisions for human review.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "request_sensitive_operation_approval": _permission(
        "request_sensitive_operation_approval",
        "Request sensitive operation approval",
        "request_sensitive_operation_approval",
        "high",
        "Request human approval for a sensitive operation without executing it.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "modify_configurations": _permission(
        "modify_configurations",
        "Modify configurations",
        "modify_configurations",
        "critical",
        "Modify protected system configuration.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "rotate_keys": _permission(
        "rotate_keys",
        "Rotate keys",
        "rotate_keys",
        "critical",
        "Preview key rotation governance without performing key operations.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "access_secrets": _permission(
        "access_secrets",
        "Access secrets",
        "access_secrets",
        "critical",
        "Access credential or secret material. Always blocked in this prototype.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "trigger_withdrawals": _permission(
        "trigger_withdrawals",
        "Trigger withdrawals",
        "trigger_withdrawals",
        "critical",
        "Trigger withdrawal execution. Always blocked for agents.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "approve_withdrawals": _permission(
        "approve_withdrawals",
        "Approve withdrawals",
        "approve_withdrawals",
        "critical",
        "Approve withdrawal execution. Always blocked for agents.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "modify_user_permissions": _permission(
        "modify_user_permissions",
        "Modify user permissions",
        "modify_user_permissions",
        "critical",
        "Modify user permissions. Blocked by local governance policy.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "access_compliance_evidence": _permission(
        "access_compliance_evidence",
        "Access compliance evidence",
        "access_compliance_evidence",
        "medium",
        "Read approved compliance evidence metadata.",
        evidence_required=True,
    ),
    "export_data": _permission(
        "export_data",
        "Export data",
        "export_data",
        "high",
        "Export data from the prototype. Human review required.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "access_custodian_apis": _permission(
        "access_custodian_apis",
        "Access custodian APIs",
        "access_custodian_apis",
        "critical",
        "Access custodian APIs. Always blocked in this prototype.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "change_cloud_kubernetes_configuration": _permission(
        "change_cloud_kubernetes_configuration",
        "Change cloud Kubernetes configuration",
        "change_cloud_kubernetes_configuration",
        "critical",
        "Change cloud or Kubernetes configuration. Blocked from direct execution.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
    "delete_or_modify_records": _permission(
        "delete_or_modify_records",
        "Delete or modify records",
        "delete_or_modify_records",
        "critical",
        "Delete or modify protected records. Blocked by local governance policy.",
        sensitive=True,
        human_approval_required=True,
        evidence_required=True,
        review_case_required=True,
    ),
}

PROFILE_MAP = {
    "compliance_assistant": {
        "allowed": [
            "read_audit_events",
            "access_compliance_evidence",
            "create_review_cases",
            "create_evidence_packages",
            "create_reports",
        ],
        "denied": [
            "read_balances",
            "read_transactions",
            "export_data",
            "approve_withdrawals",
            "access_secrets",
        ],
    },
    "risk_analyst_agent": {
        "allowed": [
            "read_audit_events",
            "read_customer_metadata",
            "create_review_cases",
            "suggest_risk_decisions",
            "request_sensitive_operation_approval",
        ],
        "denied": [
            "approve_withdrawals",
            "trigger_withdrawals",
            "modify_user_permissions",
            "access_secrets",
        ],
    },
    "reporting_agent": {
        "allowed": [
            "create_reports",
            "read_public_data",
            "read_internal_documents",
        ],
        "denied": [
            "read_balances",
            "export_data",
            "read_transactions",
            "access_secrets",
        ],
    },
    "security_monitoring_agent": {
        "allowed": [
            "read_audit_events",
            "create_review_cases",
            "create_evidence_packages",
            "suggest_risk_decisions",
        ],
        "denied": [
            "rotate_keys",
            "access_secrets",
            "modify_configurations",
            "change_cloud_kubernetes_configuration",
        ],
    },
    "custodian_integration_agent": {
        "allowed": [
            "access_compliance_evidence",
            "read_audit_events",
            "create_review_cases",
            "create_evidence_packages",
        ],
        "denied": [
            "access_custodian_apis",
            "trigger_withdrawals",
            "approve_withdrawals",
            "access_secrets",
            "rotate_keys",
        ],
    },
    "high_risk_operation_agent": {
        "allowed": [
            "request_sensitive_operation_approval",
            "create_review_cases",
            "create_evidence_packages",
        ],
        "denied": [
            "trigger_withdrawals",
            "approve_withdrawals",
            "modify_configurations",
            "modify_user_permissions",
            "access_secrets",
            "access_custodian_apis",
            "delete_or_modify_records",
        ],
    },
}


class AgentPermissionsService:
    """Deny-by-default deterministic permission model for prototype agents."""

    def list_catalog(self) -> list[AgentPermissionDefinition]:
        return [
            self._permission_with_agent_type_scope(
                PERMISSION_CATALOG[permission_id]
            )
            for permission_id in sorted(PERMISSION_CATALOG)
        ]

    def list_profiles(self) -> list[AgentPermissionProfile]:
        return [
            self._profile(agent_type)
            for agent_type in sorted(PROFILE_MAP)
        ]

    def get_agent_permissions(
        self,
        agent_id: str,
    ) -> AgentPermissionsForAgentResponse:
        agent = self._get_agent(agent_id)
        passport = agent_passport_service.validate_passport(agent.agent_id)
        profile = self._profile(agent.agent_type)
        return AgentPermissionsForAgentResponse(
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            agent_status=agent.status,
            passport_id=passport.passport_id,
            profile=profile,
            allowed_permissions=profile.allowed_permissions,
            denied_or_restricted_permissions=(
                profile.denied_or_restricted_permissions
            ),
            safety_notice=PERMISSION_SAFETY_NOTICE,
        )

    def evaluate(
        self,
        request: AgentPermissionEvaluationRequest,
    ) -> AgentPermissionEvaluationResponse:
        agent = self._get_agent(request.agent_id)
        permission = self._get_permission(request.permission_id)
        passport = agent_passport_service.validate_passport(agent.agent_id)
        decision, reasons = self._evaluate_decision(
            agent=agent,
            permission=permission,
            passport_valid=passport.passport_valid,
            environment=request.environment,
        )
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event_id = self._evaluation_audit_event_id(
            agent.agent_id,
            permission.permission_id,
        )
        correlation_id = self._correlation_id(agent.agent_id)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_permissions",
            action="evaluate_agent_permission",
            object_type="agent_permission",
            object_id=f"{agent.agent_id}:{permission.permission_id}",
            decision=decision,
            severity=permission.risk_level,
            summary="Agent permission evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            metadata={
                "agent_type": agent.agent_type,
                "agent_status": agent.status,
                "permission_id": permission.permission_id,
                "resource_type": request.resource_type,
                "resource_id": request.resource_id,
                "environment": request.environment,
                "action_context": request.action_context,
                "blocking_reasons": reasons,
                "safety_notice": self._safety_notice(permission.permission_id),
            },
        )
        return AgentPermissionEvaluationResponse(
            agent_id=agent.agent_id,
            agent_name=agent.agent_name,
            agent_type=agent.agent_type,
            agent_status=agent.status,
            passport_id=passport.passport_id,
            permission_id=permission.permission_id,
            permission_label=permission.label,
            permission_category=permission.category,
            permission_risk_level=permission.risk_level,
            resource_type=request.resource_type,
            resource_id=request.resource_id,
            environment=request.environment,
            decision=decision,
            allowed=decision == "allowed",
            human_approval_required=self._human_approval_required(
                permission,
                decision,
            ),
            evidence_required=permission.evidence_required
            or permission.risk_level in HIGH_RISK_LEVELS,
            review_case_required=permission.review_case_required
            or permission.risk_level in HIGH_RISK_LEVELS,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            blocking_reasons=reasons,
            recommended_next_action=self._evaluation_next_action(decision),
            safety_notice=self._safety_notice(permission.permission_id),
            created_at=created_at,
        )

    def grant_preview(
        self,
        agent_id: str,
        request: AgentPermissionGrantPreviewRequest,
    ) -> AgentPermissionGrantPreviewResponse:
        agent = self._get_agent(agent_id)
        permission = self._get_permission(request.permission_id)
        decision, reasons = self._grant_preview_decision(
            agent=agent,
            permission=permission,
            environment=request.environment,
        )
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event_id = self._grant_preview_audit_event_id(
            agent.agent_id,
            permission.permission_id,
        )
        correlation_id = self._correlation_id(agent.agent_id)
        required_controls = self._required_controls(permission, decision)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id,
            actor_type="staff",
            source_module="agent_permissions",
            action="preview_agent_permission_grant",
            object_type="agent_permission_grant_preview",
            object_id=f"{agent.agent_id}:{permission.permission_id}",
            decision=decision,
            severity=permission.risk_level,
            summary=(
                "Agent permission grant preview evaluated without creating a "
                "persistent grant."
            ),
            correlation_id=correlation_id,
            metadata={
                "agent_type": agent.agent_type,
                "agent_status": agent.status,
                "permission_id": permission.permission_id,
                "scope": request.scope,
                "environment": request.environment,
                "expires_at": request.expires_at.isoformat()
                if request.expires_at
                else None,
                "justification": request.justification,
                "required_controls": required_controls,
                "blocking_reasons": reasons,
                "persistent_grant_created": False,
                "safety_notice": self._safety_notice(permission.permission_id),
            },
        )
        return AgentPermissionGrantPreviewResponse(
            agent_id=agent.agent_id,
            permission_id=permission.permission_id,
            grant_preview_decision=decision,
            scope=request.scope,
            environment=request.environment,
            expires_at=(
                request.expires_at.isoformat() if request.expires_at else None
            ),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            required_controls=required_controls,
            blocking_reasons=reasons,
            recommended_next_action=self._grant_preview_next_action(decision),
            safety_notice=self._safety_notice(permission.permission_id),
            created_at=created_at,
        )

    def _evaluate_decision(
        self,
        *,
        agent: AgentRegistryDetail,
        permission: AgentPermissionDefinition,
        passport_valid: bool,
        environment: str,
    ) -> tuple[str, list[str]]:
        normalized_environment = environment.strip().lower()
        if agent.status in BLOCKED_AGENT_STATUSES:
            return "blocked_by_agent_status", [f"agent_status_{agent.status}"]
        if not passport_valid:
            return "blocked_by_passport", ["agent_passport_not_valid"]
        if normalized_environment == "production":
            return "blocked_by_policy", ["production_execution_prohibited"]
        if permission.permission_id in SECRET_PERMISSIONS:
            return "blocked_secret_access", ["secrets_access_prohibited"]
        if permission.permission_id in CUSTODY_PERMISSIONS:
            return "blocked_custody_execution", ["custodian_api_access_prohibited"]
        if permission.permission_id in WITHDRAWAL_BLOCKED_PERMISSIONS:
            return "blocked_sensitive_action", [
                "agent_withdrawal_execution_prohibited"
            ]
        if permission.permission_id in POLICY_BLOCKED_PERMISSIONS:
            return "blocked_by_policy", ["permission_blocked_by_governance_policy"]

        profile = PROFILE_MAP.get(agent.agent_type, {"allowed": [], "denied": []})
        if permission.permission_id in profile["denied"]:
            return "blocked_by_policy", ["permission_restricted_by_agent_profile"]
        if permission.permission_id not in profile["allowed"]:
            return "denied", ["permission_not_explicitly_granted"]
        if permission.human_approval_required or permission.sensitive:
            return "requires_human_approval", ["human_approval_required"]
        return "allowed", []

    def _grant_preview_decision(
        self,
        *,
        agent: AgentRegistryDetail,
        permission: AgentPermissionDefinition,
        environment: str,
    ) -> tuple[str, list[str]]:
        normalized_environment = environment.strip().lower()
        if agent.status in BLOCKED_AGENT_STATUSES:
            return "grant_preview_blocked", [f"agent_status_{agent.status}"]
        if permission.permission_id in SECRET_PERMISSIONS:
            return "grant_preview_blocked", ["secrets_access_prohibited"]
        if permission.permission_id in WITHDRAWAL_BLOCKED_PERMISSIONS:
            return "grant_preview_blocked", ["withdrawal_execution_prohibited"]
        if permission.permission_id in CUSTODY_PERMISSIONS:
            return "grant_preview_blocked", ["custodian_api_access_prohibited"]
        if normalized_environment == "production":
            return "grant_preview_requires_review", [
                "production_environment_requires_review"
            ]
        if permission.permission_id in POLICY_BLOCKED_PERMISSIONS:
            return "grant_preview_blocked", [
                "permission_blocked_by_governance_policy"
            ]
        if permission.permission_id == "rotate_keys":
            return "grant_preview_requires_review", [
                "key_rotation_requires_human_review",
                "no_real_key_operation_performed",
            ]
        if permission.risk_level in HIGH_RISK_LEVELS:
            return "grant_preview_requires_review", [
                f"{permission.risk_level}_risk_permission_requires_review"
            ]
        return "grant_preview_allowed", []

    def _profile(self, agent_type: str) -> AgentPermissionProfile:
        profile = PROFILE_MAP.get(agent_type, {"allowed": [], "denied": []})
        return AgentPermissionProfile(
            agent_type=agent_type,
            allowed_permissions=profile["allowed"],
            denied_or_restricted_permissions=profile["denied"],
            safety_notice=PERMISSION_SAFETY_NOTICE,
        )

    def _get_agent(self, agent_id: str) -> AgentRegistryDetail:
        return agent_registry_service.get_agent(agent_id)

    def _get_permission(self, permission_id: str) -> AgentPermissionDefinition:
        normalized_permission_id = permission_id.strip().lower()
        permission = PERMISSION_CATALOG.get(normalized_permission_id)
        if permission is None:
            raise ValueError("Agent permission was not found.")
        return self._permission_with_agent_type_scope(permission)

    def _permission_with_agent_type_scope(
        self,
        permission: AgentPermissionDefinition,
    ) -> AgentPermissionDefinition:
        allowed_for_agent_types = [
            agent_type
            for agent_type, profile in PROFILE_MAP.items()
            if permission.permission_id in profile["allowed"]
        ]
        prohibited_for_agent_types = [
            agent_type
            for agent_type, profile in PROFILE_MAP.items()
            if permission.permission_id in profile["denied"]
        ]
        return permission.model_copy(
            update={
                "allowed_for_agent_types": sorted(allowed_for_agent_types),
                "prohibited_for_agent_types": sorted(prohibited_for_agent_types),
            }
        )

    def _human_approval_required(
        self,
        permission: AgentPermissionDefinition,
        decision: str,
    ) -> bool:
        if decision in {"allowed", "denied"}:
            return permission.human_approval_required
        if decision in {"blocked_secret_access", "blocked_custody_execution"}:
            return permission.human_approval_required
        return permission.human_approval_required or permission.sensitive

    def _required_controls(
        self,
        permission: AgentPermissionDefinition,
        decision: str,
    ) -> list[str]:
        controls = ["explicit_scope", "audit_event", "deny_by_default_policy"]
        if decision == "grant_preview_requires_review":
            controls.extend(["human_governance_review", "review_case"])
        if permission.evidence_required:
            controls.append("evidence_package")
        if permission.human_approval_required:
            controls.append("human_approval")
        if permission.permission_id == "rotate_keys":
            controls.append("no_real_key_operation")
        return controls

    def _safety_notice(self, permission_id: str) -> str:
        if permission_id in SECRET_PERMISSIONS:
            return SECRET_SAFETY_NOTICE
        if permission_id in CUSTODY_PERMISSIONS:
            return CUSTODIAN_SAFETY_NOTICE
        return PERMISSION_SAFETY_NOTICE

    def _evaluation_audit_event_id(
        self,
        agent_id: str,
        permission_id: str,
    ) -> str:
        permission_slug = permission_id.upper().replace("_", "-")
        return (
            "AUD-AGENT-PERMISSION-EVALUATED-"
            f"{agent_id.removeprefix('AGENT-')}-{permission_slug}"
        )

    def _grant_preview_audit_event_id(
        self,
        agent_id: str,
        permission_id: str,
    ) -> str:
        permission_slug = permission_id.upper().replace("_", "-")
        return (
            "AUD-AGENT-PERMISSION-GRANT-PREVIEW-"
            f"{agent_id.removeprefix('AGENT-')}-{permission_slug}"
        )

    def _correlation_id(self, agent_id: str) -> str:
        return f"CORR-AGENT-{agent_id.removeprefix('AGENT-')}"

    def _evaluation_next_action(self, decision: str) -> str:
        if decision == "allowed":
            return "record_permission_evaluation_without_granting_execution_rights"
        if decision == "requires_human_approval":
            return "route_permission_request_to_human_review_before_any_action"
        return "deny_permission_and_preserve_audit_trail"

    def _grant_preview_next_action(self, decision: str) -> str:
        if decision == "grant_preview_allowed":
            return "record_preview_only_and_require_future_persistent_grant_workflow"
        if decision == "grant_preview_requires_review":
            return "route_permission_grant_preview_to_human_governance_review"
        return "block_permission_grant_preview_and_preserve_audit_trail"


agent_permissions_service = AgentPermissionsService()
