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
                }
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
