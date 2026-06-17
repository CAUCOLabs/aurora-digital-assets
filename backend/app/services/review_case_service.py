import json
from datetime import datetime, timezone
from sqlite3 import Row

from app.db.database import get_connection
from app.schemas.buy_sell import BuySellEvaluateRequest, BuySellEvaluateResponse
from app.schemas.payment import (
    DigitalAssetPaymentEvaluateRequest,
    DigitalAssetPaymentEvaluateResponse,
)
from app.schemas.review_case import (
    CreateReviewCaseFromEvidencePackageResponse,
    ReviewCase,
    ReviewCaseAction,
    ReviewCaseLifecycleSummary,
    ReviewCaseLifecycleTransitionResponse,
)
from app.services.audit_service import audit_service
from app.schemas.risk_review import RiskDecisionResponse
from app.schemas.withdrawal import WithdrawalEvaluateRequest
from app.storage.sqlite_store import (
    get_review_case_by_id,
    list_persisted_review_cases,
    save_review_case,
)


REVIEW_DECISION_STATUSES = {
    "approve": "Approved",
    "reject": "Rejected",
    "request_information": "More information needed",
    "delay": "Delayed",
    "escalate": "Escalated",
}

LIFECYCLE_STATUSES = [
    "open",
    "under_review",
    "action_required",
    "mitigation_in_progress",
    "mitigated",
    "closed",
]

STANDARD_LIFECYCLE_TRANSITIONS = {
    "open": "under_review",
    "under_review": "action_required",
    "action_required": "mitigation_in_progress",
    "mitigation_in_progress": "mitigated",
    "mitigated": "closed",
}

DETERMINISTIC_CASE_CONTEXT = {
    "CASE-INFRA-CHAIN-REACTION": {
        "title": "Infrastructure Security Chain Reaction Review Case",
        "case_type": "infrastructure_security_review",
        "source_package_id": "EP-FROM-AUD-INFRA-CHAIN-REACTION",
        "source_audit_event_id": "AUD-INFRA-CHAIN-REACTION",
        "correlation_id": "CORR-INFRA-CHAIN-REACTION",
        "audit_slug": "INFRA-CHAIN",
        "risk_level": "critical",
    },
    "CASE-INFRA-AZURE-STORAGE-IDENTITY": {
        "title": "Azure Storage to Identity Risk Review Case",
        "case_type": "azure_identity_storage_security_review",
        "source_package_id": "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
        "source_audit_event_id": "AUD-INFRA-AZURE-STORAGE-IDENTITY",
        "correlation_id": "CORR-INFRA-AZURE-STORAGE-IDENTITY",
        "audit_slug": "AZURE-IDENTITY",
        "risk_level": "critical",
    },
    "CASE-INFRA-K8S-HARDENING-FAILURE": {
        "title": "Container and Kubernetes Hardening Review Case",
        "case_type": "container_kubernetes_hardening_review",
        "source_package_id": "EP-FROM-AUD-INFRA-K8S-HARDENING-FAILURE",
        "source_audit_event_id": "AUD-INFRA-K8S-HARDENING-FAILURE",
        "correlation_id": "CORR-INFRA-K8S-HARDENING-FAILURE",
        "audit_slug": "K8S-HARDENING",
        "risk_level": "critical",
    },
    "CASE-CRYPTO-AGILITY-PQ-READINESS": {
        "title": "Cryptographic Agility and Post-Quantum Readiness Review Case",
        "case_type": "cryptographic_agility_review",
        "source_package_id": "EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS",
        "source_audit_event_id": "AUD-CRYPTO-AGILITY-PQ-READINESS",
        "correlation_id": "CORR-CRYPTO-AGILITY-PQ-READINESS",
        "audit_slug": "CRYPTO-AGILITY",
        "risk_level": "critical",
    },
}


class ReviewCaseService:
    """SQLite-backed case store for simulated compliance review workflows."""

    def create_withdrawal_case(
        self,
        request: WithdrawalEvaluateRequest,
        decision: RiskDecisionResponse,
    ) -> ReviewCase:
        asset = request.asset.strip().upper()
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "external_withdrawal_review",
            title=f"External {asset} withdrawal",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=request.amount,
            network=request.network.strip(),
            destination_address=request.destination_address.strip(),
            wallet_type=request.wallet_type.strip(),
        )
        self._insert_case(case)
        return case

    def create_digital_asset_payment_case(
        self,
        request: DigitalAssetPaymentEvaluateRequest,
        decision: DigitalAssetPaymentEvaluateResponse,
    ) -> ReviewCase:
        asset = request.payment_asset.strip().upper()
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "digital_asset_payment_review",
            title="Digital asset invoice payment",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=request.amount_eur,
            network="banking settlement",
            destination_address=request.recipient_name.strip(),
            wallet_type="verified_business_recipient",
        )
        self._insert_case(case)
        return case

    def create_buy_sell_case(
        self,
        request: BuySellEvaluateRequest,
        decision: BuySellEvaluateResponse,
    ) -> ReviewCase:
        asset = request.asset.strip().upper()
        gross_eur = decision.estimate.gross_eur if decision.estimate else 0.0
        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=decision.case_type or "buy_sell_review",
            title="Digital asset buy/sell review",
            status="Pending review",
            risk_level=decision.risk_level,
            reasons=decision.reasons,
            customer="Claudio Demo",
            action_type=decision.audit_event_type,
            asset=asset,
            amount=gross_eur,
            network="banking settlement",
            destination_address="Aurora Digital Assets Wallet",
            wallet_type="internal_custodial_wallet_concept",
        )
        self._insert_case(case)
        return case

    def create_risk_operations_case(
        self,
        *,
        title: str,
        summary: str,
        required_action: str,
        missing_evidence: list[str],
        source_action_id: str,
        source_id: str,
        reviewer_id: str,
        priority: str,
        risk_type: str,
    ) -> ReviewCase:
        reasons = [
            summary,
            f"Required action: {required_action}",
            f"Source action: {source_action_id}",
            f"Assigned reviewer: {reviewer_id}",
        ]
        if missing_evidence:
            reasons.append(
                "Missing evidence: " + ", ".join(missing_evidence)
            )

        case = ReviewCase(
            case_id=self._next_case_id(),
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type="risk_operations_review",
            title=title,
            status="Pending review",
            risk_level=priority,
            reasons=reasons,
            customer="Aurora Bank internal prototype",
            action_type="risk_operations_review_case_prepared",
            asset="digital_assets_controls",
            amount=0.0,
            network="internal_review_workflow",
            destination_address=source_id,
            wallet_type=risk_type,
        )
        self._insert_case(case)
        return case

    def create_from_evidence_package(
        self,
        *,
        package_id: str,
        source_audit_event_id: str,
        correlation_id: str,
        reviewer_id: str,
        priority: str,
    ) -> CreateReviewCaseFromEvidencePackageResponse:
        normalized_package_id = package_id.strip().upper()
        normalized_audit_event_id = source_audit_event_id.strip().upper()
        normalized_correlation_id = correlation_id.strip().upper()
        normalized_priority = priority.strip().lower()
        if normalized_package_id == "EP-FROM-AUD-INFRA-CHAIN-REACTION":
            case_id = "CASE-INFRA-CHAIN-REACTION"
            title = "Infrastructure Security Chain Reaction Review Case"
            case_type = "infrastructure_security_review"
            assigned_team = "Risk Operations / Infrastructure Security"
            review_reason = (
                "Critical evidence package indicates a simulated "
                "application-to-cloud chain reaction path involving application "
                "authorization, Kubernetes RBAC, cloud IAM, secrets, audit "
                "evidence, and risk operations."
            )
            severity = "critical"
            audit_event_id = "AUD-REVIEW-FROM-EP-INFRA-CHAIN-REACTION"
            linked_audit_events = [
                normalized_audit_event_id,
                "AUD-EVIDENCE-FROM-AUD-INFRA-CHAIN-REACTION",
            ]
            recommended_actions = [
                "Review object-level authorization controls.",
                "Review safe template execution controls.",
                "Review Kubernetes RBAC and service account permissions.",
                "Review cloud IAM trust conditions.",
                "Review IAM wildcard permissions.",
                "Review secret management and rotation posture.",
                "Preserve audit and evidence traceability.",
                "Escalate or close after internal review.",
            ]
        elif normalized_package_id == "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY":
            case_id = "CASE-INFRA-AZURE-STORAGE-IDENTITY"
            title = "Azure Storage to Identity Risk Review Case"
            case_type = "azure_identity_storage_security_review"
            assigned_team = "Risk Operations / Cloud Identity Security"
            review_reason = (
                "Critical evidence package indicates a simulated Azure "
                "storage-to-identity chain reaction path involving exposed "
                "storage, certificate exposure, service principal permissions, "
                "deployment access, managed identity scope, privileged identity "
                "roles, and monitoring gaps."
            )
            severity = "critical"
            audit_event_id = "AUD-REVIEW-FROM-EP-INFRA-AZURE-STORAGE-IDENTITY"
            linked_audit_events = [
                normalized_audit_event_id,
                "AUD-EVIDENCE-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
            ]
            recommended_actions = [
                "Review Azure storage public access posture.",
                "Review certificate storage and rotation posture.",
                "Review service principal permission scope.",
                "Review deployment credential controls.",
                "Review managed identity resource scope.",
                "Review privileged identity and password reset permissions.",
                "Review identity and Key Vault monitoring coverage.",
                "Escalate or close after internal review.",
            ]
        elif normalized_package_id == "EP-FROM-AUD-INFRA-K8S-HARDENING-FAILURE":
            case_id = "CASE-INFRA-K8S-HARDENING-FAILURE"
            title = "Container and Kubernetes Hardening Review Case"
            case_type = "container_kubernetes_hardening_review"
            assigned_team = "Risk Operations / Kubernetes Security"
            review_reason = (
                "Critical evidence package indicates a simulated "
                "container-to-Kubernetes hardening failure involving image "
                "secrets, root runtime, weak securityContext, service account "
                "token exposure, broad RBAC, missing NetworkPolicies, missing "
                "resource limits, missing CIS audit, and missing DevSecOps "
                "verification."
            )
            severity = "critical"
            audit_event_id = "AUD-REVIEW-FROM-EP-INFRA-K8S-HARDENING-FAILURE"
            linked_audit_events = [
                normalized_audit_event_id,
                "AUD-EVIDENCE-FROM-AUD-INFRA-K8S-HARDENING-FAILURE",
            ]
            recommended_actions = [
                "Review Dockerfile hardening and image secret exclusion.",
                "Review non-root runtime and Kubernetes securityContext posture.",
                "Review ServiceAccount token mounting and RBAC least privilege.",
                "Review Kubernetes secret access restrictions.",
                "Review NetworkPolicy isolation and resource limits.",
                "Review CIS-style audit and DevSecOps hardening evidence.",
                "Escalate or close after internal review.",
            ]
        elif normalized_package_id == "EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS":
            case_id = "CASE-CRYPTO-AGILITY-PQ-READINESS"
            title = "Cryptographic Agility and Post-Quantum Readiness Review Case"
            case_type = "cryptographic_agility_review"
            assigned_team = "Risk Operations / Cryptographic Governance"
            review_reason = (
                "Critical evidence package indicates a simulated cryptographic "
                "agility and post-quantum readiness gap involving inventory, "
                "algorithm versioning, key rotation, long-term confidentiality, "
                "audit integrity, custody key governance, blockchain protocol "
                "separation, and migration planning."
            )
            severity = "critical"
            audit_event_id = "AUD-REVIEW-FROM-EP-CRYPTO-AGILITY-PQ-READINESS"
            linked_audit_events = [
                normalized_audit_event_id,
                "AUD-EVIDENCE-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS",
            ]
            recommended_actions = [
                "Complete cryptographic inventory.",
                "Version all algorithms and key policies.",
                "Define key rotation and emergency rollover procedures.",
                "Classify long-term confidentiality risks.",
                "Separate Aurora platform cryptography from external blockchain protocol cryptography.",
                "Define KMS/HSM/Key Vault integration roadmap.",
                "Prepare standards-based post-quantum migration plan.",
                "Preserve audit and evidence traceability.",
                "Escalate or close after internal review.",
            ]
        else:
            case_id = f"CASE-FROM-{normalized_package_id}"
            title = "Evidence Package Review Case"
            case_type = "evidence_package_review"
            assigned_team = "Compliance Review"
            review_reason = (
                "Evidence package was routed into formal compliance review."
            )
            severity = normalized_priority or "medium"
            audit_event_id = f"AUD-REVIEW-FROM-{normalized_package_id}"
            linked_audit_events = [normalized_audit_event_id]
            recommended_actions = [
                "Review package evidence and traceability.",
                "Record reviewer decision rationale.",
            ]

        case = ReviewCase(
            case_id=case_id,
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=case_type,
            title=title,
            status="open",
            risk_level=normalized_priority,
            reasons=[
                review_reason,
                f"Source evidence package: {normalized_package_id}",
                f"Source audit event: {normalized_audit_event_id}",
                f"Correlation ID: {normalized_correlation_id}",
            ],
            customer="Aurora Bank internal prototype",
            action_type="evidence_package_review_case_created",
            asset="digital_assets_controls",
            amount=0.0,
            network="internal_review_workflow",
            destination_address=normalized_package_id,
            wallet_type="infrastructure_security_evidence_package",
        )
        self._insert_case(case)

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=reviewer_id or "reviewer-demo",
            actor_type="staff",
            source_module="review_cases",
            action="create_from_evidence_package",
            object_type="evidence_package",
            object_id=normalized_package_id,
            decision="review_case_created",
            severity=severity,
            summary="Review case created from evidence package.",
            evidence_reference=normalized_package_id,
            review_case_id=case_id,
            correlation_id=normalized_correlation_id,
            metadata={
                "source_audit_event_id": normalized_audit_event_id,
                "linked_audit_events": linked_audit_events,
                "linked_evidence_packages": [normalized_package_id],
                "assigned_team": assigned_team,
                "review_reason": review_reason,
                "recommended_actions": recommended_actions,
            },
        )
        persisted_case = self.persist_case_trace(
            case,
            source_module="evidence_packages",
            source_id=normalized_package_id,
            source_action_id=normalized_audit_event_id,
            reviewer_id=reviewer_id,
            recommended_next_action="; ".join(recommended_actions),
            audit_event_id=audit_event.event_id,
            correlation_id=normalized_correlation_id,
            metadata={
                "case_type": case_type,
                "severity": severity,
                "assigned_team": assigned_team,
                "review_reason": review_reason,
                "source_package_id": normalized_package_id,
                "source_audit_event_id": normalized_audit_event_id,
                "linked_audit_events": linked_audit_events,
                "linked_evidence_packages": [normalized_package_id],
                "recommended_actions": recommended_actions,
                "source_domain": "infrastructure_security"
                if normalized_package_id
                in {
                    "EP-FROM-AUD-INFRA-CHAIN-REACTION",
                    "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
                    "EP-FROM-AUD-INFRA-K8S-HARDENING-FAILURE",
                }
                else "crypto_agility"
                if normalized_package_id
                == "EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS"
                else "evidence_packages",
            },
        )

        return CreateReviewCaseFromEvidencePackageResponse(
            case_id=case_id,
            title=title,
            source_package_id=normalized_package_id,
            source_audit_event_id=normalized_audit_event_id,
            correlation_id=normalized_correlation_id,
            case_type=case_type,
            priority=normalized_priority,
            severity=severity,
            status=persisted_case.status,
            assigned_team=assigned_team,
            review_reason=review_reason,
            linked_audit_events=linked_audit_events,
            linked_evidence_packages=[normalized_package_id],
            recommended_actions=recommended_actions,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            created_at=persisted_case.created_at,
        )

    def list_cases(self) -> list[ReviewCase]:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                FROM review_cases
                ORDER BY case_id ASC
                """
            ).fetchall()

        return self._merge_cases(
            [self._row_to_case(row) for row in rows],
            list_persisted_review_cases(),
        )

    def get_case(self, case_id: str) -> ReviewCase | None:
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                FROM review_cases
                WHERE case_id = ?
                """,
                (case_id,),
            ).fetchone()

        if row is None:
            return get_review_case_by_id(case_id)
        return self._row_to_case(row)

    def list_persisted_cases(self) -> list[ReviewCase]:
        return list_persisted_review_cases()

    def transition_lifecycle(
        self,
        *,
        case_id: str,
        target_status: str,
        reviewer_id: str,
        decision_note: str,
        mitigation_action: str | None = None,
        evidence_package_id: str | None = None,
        risk_acceptance: bool = False,
    ) -> ReviewCaseLifecycleTransitionResponse:
        normalized_case_id = case_id.strip().upper()
        case = self._resolve_lifecycle_case(normalized_case_id)
        previous_status = self._normalize_lifecycle_status(case.status)
        allowed = self._transition_allowed(
            previous_status=previous_status,
            target_status=target_status,
            risk_acceptance=risk_acceptance,
        )
        created_at = datetime.now(timezone.utc).isoformat()
        correlation_id = self._case_correlation_id(case)
        recommended_next_status = self._recommended_next_status(
            previous_status if not allowed else target_status,
            risk_acceptance=risk_acceptance,
        )

        if not allowed:
            return ReviewCaseLifecycleTransitionResponse(
                case_id=normalized_case_id,
                previous_status=previous_status,
                new_status=previous_status,
                transition_allowed=False,
                lifecycle_stage=previous_status,
                reviewer_id=reviewer_id,
                decision_note=(
                    decision_note
                    or f"Transition to {target_status} is not allowed."
                ),
                mitigation_action=mitigation_action,
                linked_evidence_package=evidence_package_id,
                audit_event_created=False,
                audit_event_id="",
                correlation_id=correlation_id,
                recommended_next_status=recommended_next_status,
                created_at=created_at,
            )

        audit_event_id = self._lifecycle_audit_event_id(
            normalized_case_id,
            target_status,
        )
        action_type = self._action_type_for_status(
            target_status,
            risk_acceptance=risk_acceptance,
        )
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=reviewer_id,
            actor_type="staff",
            source_module="review_cases",
            action="lifecycle_transition",
            object_type="review_case",
            object_id=normalized_case_id,
            decision=target_status,
            severity=case.risk_level,
            summary=(
                f"Review case lifecycle transitioned from {previous_status} "
                f"to {target_status}. {decision_note}"
            ),
            evidence_reference=evidence_package_id,
            review_case_id=normalized_case_id,
            correlation_id=correlation_id,
            metadata={
                "previous_status": previous_status,
                "new_status": target_status,
                "mitigation_action": mitigation_action,
                "risk_acceptance": risk_acceptance,
            },
        )

        action = ReviewCaseAction(
            action_id=self._next_lifecycle_action_id(case),
            case_id=normalized_case_id,
            action_type=action_type,
            actor_id=reviewer_id,
            note=decision_note,
            created_at=created_at,
            audit_event_id=audit_event.event_id,
        )
        updated_case = case.model_copy(update={"status": target_status})
        self._persist_lifecycle_case(
            updated_case,
            action=action,
            audit_event_id=audit_event.event_id,
            evidence_package_id=evidence_package_id,
            final_decision="risk_accepted"
            if risk_acceptance and target_status == "closed"
            else None,
        )
        self._update_primary_case_status(normalized_case_id, target_status)

        return ReviewCaseLifecycleTransitionResponse(
            case_id=normalized_case_id,
            previous_status=previous_status,
            new_status=target_status,
            transition_allowed=True,
            lifecycle_stage=target_status,
            reviewer_id=reviewer_id,
            decision_note=decision_note,
            mitigation_action=mitigation_action,
            linked_evidence_package=evidence_package_id,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=correlation_id,
            recommended_next_status=self._recommended_next_status(
                target_status,
                risk_acceptance=risk_acceptance,
            ),
            created_at=created_at,
        )

    def add_lifecycle_action(
        self,
        *,
        case_id: str,
        action_type: str,
        actor_id: str,
        note: str,
    ) -> ReviewCaseAction:
        normalized_case_id = case_id.strip().upper()
        case = self._resolve_lifecycle_case(normalized_case_id)
        correlation_id = self._case_correlation_id(case)
        audit_event_id = (
            f"AUD-LIFECYCLE-{self._case_audit_slug(normalized_case_id)}-"
            f"ACTION-{action_type.strip().upper().replace('_', '-')}"
        )
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=actor_id,
            actor_type="staff",
            source_module="review_cases",
            action="lifecycle_action",
            object_type="review_case",
            object_id=normalized_case_id,
            decision=action_type,
            severity=case.risk_level,
            summary=f"Review case lifecycle action recorded: {note}",
            review_case_id=normalized_case_id,
            correlation_id=correlation_id,
            metadata={"action_type": action_type},
        )
        action = ReviewCaseAction(
            action_id=self._next_lifecycle_action_id(case),
            case_id=normalized_case_id,
            action_type=action_type,
            actor_id=actor_id,
            note=note,
            created_at=datetime.now(timezone.utc).isoformat(),
            audit_event_id=audit_event.event_id,
        )
        self._persist_lifecycle_case(
            case,
            action=action,
            audit_event_id=audit_event.event_id,
            evidence_package_id=None,
        )
        return action

    def close_lifecycle_case(
        self,
        *,
        case_id: str,
        reviewer_id: str,
        decision_note: str,
        final_decision: str,
        evidence_package_id: str | None = None,
        risk_acceptance: bool = False,
    ) -> ReviewCaseLifecycleTransitionResponse:
        response = self.transition_lifecycle(
            case_id=case_id,
            target_status="closed",
            reviewer_id=reviewer_id,
            decision_note=decision_note,
            mitigation_action=f"Final decision: {final_decision}",
            evidence_package_id=evidence_package_id,
            risk_acceptance=risk_acceptance,
        )
        if response.transition_allowed:
            case = self._resolve_lifecycle_case(case_id.strip().upper())
            self._persist_lifecycle_case(
                case,
                action=None,
                audit_event_id=response.audit_event_id,
                evidence_package_id=evidence_package_id,
                final_decision=final_decision,
            )
        return response

    def get_lifecycle_summary(self, case_id: str) -> ReviewCaseLifecycleSummary:
        normalized_case_id = case_id.strip().upper()
        case = self._resolve_lifecycle_case(normalized_case_id)
        status = self._normalize_lifecycle_status(case.status)
        metadata = case.metadata or {}
        actions = [
            ReviewCaseAction(**action)
            for action in metadata.get("lifecycle_actions", [])
            if isinstance(action, dict)
        ]
        linked_evidence_packages = self._linked_evidence_packages(case)
        linked_audit_events = self._linked_audit_events(case)
        lifecycle_audit_events = [
            action.audit_event_id
            for action in actions
            if action.audit_event_id is not None
        ]
        for audit_event_id in lifecycle_audit_events:
            if audit_event_id not in linked_audit_events:
                linked_audit_events.append(audit_event_id)

        return ReviewCaseLifecycleSummary(
            case_id=normalized_case_id,
            current_status=status,
            allowed_next_statuses=self._allowed_next_statuses(status),
            lifecycle_progress_percent=self._lifecycle_progress_percent(status),
            actions=actions,
            linked_evidence_packages=linked_evidence_packages,
            linked_audit_events=linked_audit_events,
            final_decision=metadata.get("final_decision"),
            closure_ready=status == "mitigated",
        )

    def persist_case_trace(
        self,
        case: ReviewCase,
        *,
        source_module: str | None = None,
        source_id: str | None = None,
        source_action_id: str | None = None,
        reviewer_id: str | None = None,
        recommended_next_action: str | None = None,
        audit_event_id: str | None = None,
        correlation_id: str | None = None,
        metadata: dict | None = None,
    ) -> ReviewCase:
        return save_review_case(
            case,
            source_module=source_module,
            source_id=source_id,
            source_action_id=source_action_id,
            reviewer_id=reviewer_id,
            recommended_next_action=recommended_next_action,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            metadata=metadata,
        )

    def record_decision(
        self,
        case_id: str,
        decision: str,
        notes: str | None,
    ) -> ReviewCase | None:
        case = self.get_case(case_id)
        if case is None:
            return None

        status = REVIEW_DECISION_STATUSES[decision]
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE review_cases
                SET reviewer_decision = ?,
                    reviewer_notes = ?,
                    status = ?
                WHERE case_id = ?
                """,
                (decision, notes, status, case_id),
            )

        return self.get_case(case_id)

    def _resolve_lifecycle_case(self, case_id: str) -> ReviewCase:
        stored_case = get_review_case_by_id(case_id)
        if stored_case is not None:
            return stored_case

        existing_case = self.get_case(case_id)
        if existing_case is not None:
            return existing_case

        context = DETERMINISTIC_CASE_CONTEXT.get(case_id)
        if context is None:
            context = {
                "title": f"Review Case {case_id}",
                "case_type": "evidence_package_review",
                "source_package_id": None,
                "source_audit_event_id": None,
                "correlation_id": f"CORR-LIFECYCLE-{case_id}",
                "risk_level": "medium",
            }

        case = ReviewCase(
            case_id=case_id,
            created_at=datetime.now(timezone.utc).isoformat(),
            case_type=context["case_type"],
            title=context["title"],
            status="open",
            risk_level=context["risk_level"],
            reasons=[
                "Deterministic lifecycle review case resolved for prototype workflow."
            ],
            customer="Aurora Bank internal prototype",
            action_type="review_case_lifecycle_prepared",
            asset="digital_assets_controls",
            amount=0.0,
            network="internal_review_workflow",
            destination_address=context.get("source_package_id") or case_id,
            wallet_type="review_case_lifecycle",
        )
        return save_review_case(
            case,
            source_module="evidence_packages",
            source_id=context.get("source_package_id"),
            source_action_id=context.get("source_audit_event_id"),
            reviewer_id=None,
            recommended_next_action="Start lifecycle review.",
            audit_event_id=None,
            correlation_id=context["correlation_id"],
            metadata={
                "source_package_id": context.get("source_package_id"),
                "source_audit_event_id": context.get("source_audit_event_id"),
                "linked_evidence_packages": [
                    context["source_package_id"]
                ]
                if context.get("source_package_id")
                else [],
                "linked_audit_events": [
                    context["source_audit_event_id"]
                ]
                if context.get("source_audit_event_id")
                else [],
                "lifecycle_actions": [],
            },
        )

    def _normalize_lifecycle_status(self, status: str) -> str:
        normalized = status.strip().lower().replace(" ", "_")
        if normalized in LIFECYCLE_STATUSES:
            return normalized
        if normalized in {"pending_review", "review_required", "recorded"}:
            return "open"
        if normalized in {"approved", "rejected", "escalated"}:
            return "closed"
        return "open"

    def _transition_allowed(
        self,
        *,
        previous_status: str,
        target_status: str,
        risk_acceptance: bool,
    ) -> bool:
        if previous_status == "closed":
            return False
        if STANDARD_LIFECYCLE_TRANSITIONS.get(previous_status) == target_status:
            return True
        if target_status == "closed" and risk_acceptance:
            return previous_status in {"open", "under_review", "action_required"}
        return False

    def _allowed_next_statuses(self, current_status: str) -> list[str]:
        if current_status == "closed":
            return []
        next_status = STANDARD_LIFECYCLE_TRANSITIONS.get(current_status)
        statuses = [next_status] if next_status else []
        if current_status in {"open", "under_review", "action_required"}:
            statuses.append("closed")
        return [status for status in statuses if status is not None]

    def _recommended_next_status(
        self,
        current_status: str,
        *,
        risk_acceptance: bool,
    ) -> str | None:
        if current_status == "closed":
            return None
        if risk_acceptance and current_status in {
            "open",
            "under_review",
            "action_required",
        }:
            return "closed"
        return STANDARD_LIFECYCLE_TRANSITIONS.get(current_status)

    def _lifecycle_progress_percent(self, status: str) -> int:
        progress = {
            "open": 0,
            "under_review": 20,
            "action_required": 40,
            "mitigation_in_progress": 60,
            "mitigated": 80,
            "closed": 100,
        }
        return progress.get(status, 0)

    def _case_audit_slug(self, case_id: str) -> str:
        context = DETERMINISTIC_CASE_CONTEXT.get(case_id)
        if context and context.get("audit_slug"):
            return context["audit_slug"]
        return case_id.replace("CASE-", "").replace("_", "-")

    def _lifecycle_audit_event_id(self, case_id: str, target_status: str) -> str:
        return (
            f"AUD-LIFECYCLE-{self._case_audit_slug(case_id)}-"
            f"{target_status.upper().replace('_', '-')}"
        )

    def _case_correlation_id(self, case: ReviewCase) -> str:
        context = DETERMINISTIC_CASE_CONTEXT.get(case.case_id)
        if case.correlation_id:
            return case.correlation_id
        if context:
            return context["correlation_id"]
        return f"CORR-LIFECYCLE-{case.case_id}"

    def _action_type_for_status(
        self,
        target_status: str,
        *,
        risk_acceptance: bool,
    ) -> str:
        if risk_acceptance and target_status == "closed":
            return "risk_accepted"
        return {
            "under_review": "evidence_reviewed",
            "action_required": "mitigation_requested",
            "mitigation_in_progress": "mitigation_started",
            "mitigated": "mitigation_verified",
            "closed": "case_closed",
        }.get(target_status, "reviewer_note")

    def _next_lifecycle_action_id(self, case: ReviewCase) -> str:
        actions = case.metadata.get("lifecycle_actions", []) if case.metadata else []
        return f"RCA-{case.case_id}-{len(actions) + 1:03d}"

    def _linked_evidence_packages(self, case: ReviewCase) -> list[str]:
        metadata = case.metadata or {}
        linked = [
            item
            for item in metadata.get("linked_evidence_packages", [])
            if isinstance(item, str)
        ]
        source_package = metadata.get("source_package_id") or case.source_id
        if isinstance(source_package, str) and source_package not in linked:
            linked.append(source_package)
        context = DETERMINISTIC_CASE_CONTEXT.get(case.case_id)
        if context and context.get("source_package_id") not in linked:
            linked.append(context["source_package_id"])
        return linked

    def _linked_audit_events(self, case: ReviewCase) -> list[str]:
        metadata = case.metadata or {}
        linked = [
            item
            for item in metadata.get("linked_audit_events", [])
            if isinstance(item, str)
        ]
        source_audit_event = metadata.get("source_audit_event_id") or case.source_action_id
        if isinstance(source_audit_event, str) and source_audit_event not in linked:
            linked.append(source_audit_event)
        context = DETERMINISTIC_CASE_CONTEXT.get(case.case_id)
        if context and context.get("source_audit_event_id") not in linked:
            linked.append(context["source_audit_event_id"])
        return linked

    def _persist_lifecycle_case(
        self,
        case: ReviewCase,
        *,
        action: ReviewCaseAction | None,
        audit_event_id: str,
        evidence_package_id: str | None,
        final_decision: str | None = None,
    ) -> ReviewCase:
        metadata = dict(case.metadata or {})
        actions = [
            item
            for item in metadata.get("lifecycle_actions", [])
            if isinstance(item, dict)
        ]
        if action is not None:
            actions.append(action.model_dump())
        metadata["lifecycle_actions"] = actions

        linked_audit_events = self._linked_audit_events(case)
        if audit_event_id and audit_event_id not in linked_audit_events:
            linked_audit_events.append(audit_event_id)
        metadata["linked_audit_events"] = linked_audit_events

        linked_evidence_packages = self._linked_evidence_packages(case)
        if (
            evidence_package_id
            and evidence_package_id not in linked_evidence_packages
        ):
            linked_evidence_packages.append(evidence_package_id)
        metadata["linked_evidence_packages"] = linked_evidence_packages

        if final_decision is not None:
            metadata["final_decision"] = final_decision

        context = DETERMINISTIC_CASE_CONTEXT.get(case.case_id, {})
        metadata.setdefault("source_package_id", context.get("source_package_id"))
        metadata.setdefault(
            "source_audit_event_id",
            context.get("source_audit_event_id"),
        )

        return save_review_case(
            case,
            source_module=case.source_module or "evidence_packages",
            source_id=case.source_id or context.get("source_package_id"),
            source_action_id=case.source_action_id
            or context.get("source_audit_event_id"),
            reviewer_id=case.reviewer_id,
            recommended_next_action=case.recommended_next_action,
            audit_event_id=audit_event_id or case.audit_event_id,
            correlation_id=self._case_correlation_id(case),
            metadata=metadata,
        )

    def _update_primary_case_status(self, case_id: str, status: str) -> None:
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE review_cases
                SET status = ?
                WHERE case_id = ?
                """,
                (status, case_id),
            )

    def _next_case_id(self) -> str:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT case_id FROM review_cases"
            ).fetchall()

        sequence_numbers = [
            int(row["case_id"].rsplit("-", 1)[-1])
            for row in rows
            if row["case_id"].startswith("CASE-DA-2026-")
        ]
        next_sequence = max(sequence_numbers, default=0) + 1
        return f"CASE-DA-2026-{next_sequence:03d}"

    def _insert_case(self, case: ReviewCase) -> None:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO review_cases (
                    case_id,
                    created_at,
                    case_type,
                    title,
                    status,
                    risk_level,
                    reasons,
                    customer,
                    action_type,
                    asset,
                    amount,
                    network,
                    destination_address,
                    wallet_type,
                    reviewer_decision,
                    reviewer_notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    case.case_id,
                    case.created_at,
                    case.case_type,
                    case.title,
                    case.status,
                    case.risk_level,
                    json.dumps(case.reasons),
                    case.customer,
                    case.action_type,
                    case.asset,
                    case.amount,
                    case.network,
                    case.destination_address,
                    case.wallet_type,
                    case.reviewer_decision,
                    case.reviewer_notes,
                ),
            )
        save_review_case(case)

    def _row_to_case(self, row: Row) -> ReviewCase:
        return ReviewCase(
            case_id=row["case_id"],
            created_at=row["created_at"],
            case_type=row["case_type"],
            title=row["title"],
            status=row["status"],
            risk_level=row["risk_level"],
            reasons=json.loads(row["reasons"]),
            customer=row["customer"],
            action_type=row["action_type"],
            asset=row["asset"],
            amount=row["amount"],
            network=row["network"],
            destination_address=row["destination_address"],
            wallet_type=row["wallet_type"],
            reviewer_decision=row["reviewer_decision"],
            reviewer_notes=row["reviewer_notes"],
        )

    def _merge_cases(
        self,
        base_cases: list[ReviewCase],
        persisted_cases: list[ReviewCase],
    ) -> list[ReviewCase]:
        merged = {case.case_id: case for case in base_cases}
        for case in persisted_cases:
            merged[case.case_id] = case
        return sorted(merged.values(), key=lambda case: case.case_id)


review_case_service = ReviewCaseService()
