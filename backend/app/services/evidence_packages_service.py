from app.schemas.evidence_packages import (
    EvidenceItem,
    EvidencePackage,
    EvidencePackageTemplate,
    EvidenceReadinessCheck,
    EvidenceTimelineEvent,
    GenerateEvidencePackageResponse,
)
from app.schemas.audit_event import AuditEvent
from app.services.audit_service import audit_service


def _audit_token(value: str) -> str:
    return value.strip().upper().replace("-", "-").replace(" ", "-")


AUDIT_EVENT_PACKAGE_TITLES = {
    "AUD-API-GRAPHQL-PIN": "API security evidence package - GraphQL PIN verification abuse",
    "AUD-OPS-PAYMENTS-DEGRADED": "Operational resilience evidence package - degraded payments dependency",
    "AUD-RISK-RO-ACTION-002": "Risk operations evidence package - review case preparation",
    "AUD-EVIDENCE-FCA-2026-002": "Evidence package audit trail - financial crime alert package generation",
}

INFRASTRUCTURE_AUDIT_EVENT_IDS = {
    "AUD-INFRA-CHAIN-REACTION",
    "AUD-INFRA-OBJECT-AUTH",
    "AUD-INFRA-TEMPLATE",
    "AUD-INFRA-K8S-SECRETS",
    "AUD-INFRA-IAM-TRUST",
    "AUD-INFRA-IAM-WILDCARD",
    "AUD-INFRA-SECRET",
    "AUD-INFRA-AZURE-STORAGE-IDENTITY",
    "AUD-INFRA-K8S-HARDENING-FAILURE",
}

INFRASTRUCTURE_AUDIT_EVENT_CATEGORIES = {
    "AUD-INFRA-CHAIN-REACTION": "cross_layer_chain_reaction",
    "AUD-INFRA-OBJECT-AUTH": "object_authorization",
    "AUD-INFRA-TEMPLATE": "template_safety",
    "AUD-INFRA-K8S-SECRETS": "kubernetes_secret_access",
    "AUD-INFRA-IAM-TRUST": "cloud_iam_trust_policy",
    "AUD-INFRA-IAM-WILDCARD": "cloud_iam_permission_scope",
    "AUD-INFRA-SECRET": "secret_management",
    "AUD-INFRA-AZURE-STORAGE-IDENTITY": "storage_to_identity_chain_reaction",
    "AUD-INFRA-K8S-HARDENING-FAILURE": "runtime_hardening_failure",
}

CRYPTO_AGILITY_AUDIT_EVENT_ID = "AUD-CRYPTO-AGILITY-PQ-READINESS"
SENSITIVE_APPROVAL_HIGH_VALUE_AUDIT_EVENT_ID = (
    "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET"
)


class EvidencePackagesService:
    """Provides deterministic evidence package demo data."""

    def list_packages(self) -> list[EvidencePackage]:
        return [
            EvidencePackage(
                package_id="EP-2026-001",
                title="Employee-linked account activity evidence package",
                source_alert_id="FCA-2026-001",
                risk_type="Insider risk",
                severity="critical",
                status="incomplete",
                readiness_score=68,
                summary=(
                    "Staff-linked account activity shows repeated external "
                    "transfers and requires conflict-of-interest and funds "
                    "evidence before closure."
                ),
                included_evidence=[
                    self._item(
                        "EPI-001-01",
                        "Staff-linked account indicator",
                        "Insider risk",
                        "included",
                        "Demo control identified a relationship between a staff profile and account activity.",
                        "financial_crime_monitoring",
                        True,
                    ),
                    self._item(
                        "EPI-001-02",
                        "External transfer pattern",
                        "Transaction monitoring",
                        "included",
                        "Repeated external transfer activity is attached to the alert record.",
                        "financial_crime_monitoring",
                        True,
                    ),
                    self._item(
                        "EPI-001-03",
                        "Triggered insider risk controls",
                        "Controls",
                        "included",
                        "Employee risk monitoring and audit evidence controls were triggered.",
                        "compliance_intelligence",
                        True,
                    ),
                    self._item(
                        "EPI-001-04",
                        "Audit trail reference",
                        "Audit trail",
                        "included",
                        "Prototype audit event references are included for reviewer traceability.",
                        "audit_events",
                        True,
                    ),
                ],
                missing_evidence=[
                    self._item(
                        "EPI-001-05",
                        "Source of funds evidence",
                        "Funds legitimacy",
                        "missing",
                        "Reviewer still needs documented source of funds support.",
                        "compliance_review",
                        True,
                    ),
                    self._item(
                        "EPI-001-06",
                        "Reviewer conflict-of-interest check",
                        "Reviewer controls",
                        "reviewer_required",
                        "A separate reviewer must confirm no staff conflict before finalizing.",
                        "compliance_review",
                        True,
                    ),
                    self._item(
                        "EPI-001-07",
                        "Transfer purpose documentation",
                        "Customer documentation",
                        "missing",
                        "The purpose of the external transfer has not been documented.",
                        "compliance_review",
                        True,
                    ),
                ],
                triggered_controls=[
                    "Employee risk monitoring",
                    "External transfer enhanced review",
                    "Audit evidence generation",
                ],
                reviewer_notes=[
                    "Do not close package until source of funds evidence is attached.",
                    "Assign independent reviewer because the alert is staff-linked.",
                ],
                decision_rationale=(
                    "The package remains incomplete because required reviewer "
                    "independence and funds evidence have not been recorded."
                ),
                timeline=self._timeline("001", "FCA-2026-001", "2026-06-12T08:20:00+03:00"),
                recommended_next_action=(
                    "Escalate and collect missing evidence before final package closure."
                ),
                created_at="2026-06-12T13:00:00+03:00",
            ),
            EvidencePackage(
                package_id="EP-2026-002",
                title="New company transaction growth evidence package",
                source_alert_id="FCA-2026-002",
                risk_type="Shell company indicator",
                severity="critical",
                status="incomplete",
                readiness_score=72,
                summary=(
                    "Recently created company activity grew faster than the "
                    "declared activity profile and requires beneficial ownership "
                    "and transaction rationale evidence."
                ),
                included_evidence=[
                    self._item("EPI-002-01", "Company age indicator", "Due diligence", "included", "Company registration age is below the prototype review threshold.", "financial_crime_monitoring", True),
                    self._item("EPI-002-02", "Transaction growth anomaly", "Transaction monitoring", "included", "Transaction volume increased rapidly relative to the demo company profile.", "financial_crime_monitoring", True),
                    self._item("EPI-002-03", "Declared activity mismatch", "Business profile", "included", "Funds movement does not align with the declared business activity.", "compliance_intelligence", True),
                    self._item("EPI-002-04", "Compliance intelligence explanation", "Reviewer reasoning", "included", "Generated explanation and reviewer guidance are attached.", "compliance_intelligence", True),
                ],
                missing_evidence=[
                    self._item("EPI-002-05", "Beneficial ownership evidence", "Due diligence", "missing", "Beneficial ownership support has not been attached.", "compliance_review", True),
                    self._item("EPI-002-06", "Source of funds evidence", "Funds legitimacy", "missing", "Source of funds documentation is required before package closure.", "compliance_review", True),
                    self._item("EPI-002-07", "Business rationale for transaction volume", "Business profile", "missing", "Reviewer needs documented rationale for the transaction volume.", "compliance_review", True),
                ],
                triggered_controls=[
                    "Customer and company KYC",
                    "Source of funds verification",
                    "Transaction pattern monitoring",
                ],
                reviewer_notes=[
                    "Request company documentation through the simulated compliance workflow.",
                    "Package should remain incomplete until beneficial ownership evidence is attached.",
                ],
                decision_rationale=(
                    "Critical shell company indicators are supported, but core "
                    "documentation is missing."
                ),
                timeline=self._timeline("002", "FCA-2026-002", "2026-06-12T09:05:00+03:00"),
                recommended_next_action=(
                    "Request company documentation and source of funds evidence."
                ),
                created_at="2026-06-12T13:20:00+03:00",
            ),
            EvidencePackage(
                package_id="EP-2026-003",
                title="Crypto off-ramp review evidence package",
                source_alert_id="FCA-2026-004",
                risk_type="Crypto off-ramp",
                severity="high",
                status="draft",
                readiness_score=80,
                summary=(
                    "External digital asset platform transfer requires reviewer "
                    "decision rationale and destination ownership confirmation."
                ),
                included_evidence=[
                    self._item("EPI-003-01", "Destination classified as external digital asset platform", "Digital assets", "included", "Destination classification is attached to the off-ramp review.", "financial_crime_monitoring", True),
                    self._item("EPI-003-02", "Transfer above prototype review threshold", "Transaction monitoring", "included", "Transfer amount exceeds the prototype review threshold.", "financial_crime_monitoring", True),
                    self._item("EPI-003-03", "Incomplete source of funds status", "Funds legitimacy", "included", "Source of funds status is marked incomplete for review.", "compliance_review", True),
                    self._item("EPI-003-04", "Reviewer questions", "Reviewer reasoning", "included", "Reviewer questions from compliance intelligence are included.", "compliance_intelligence", False),
                ],
                missing_evidence=[
                    self._item("EPI-003-05", "Destination ownership confirmation", "External wallet transfer", "missing", "Customer or reviewer has not confirmed destination ownership.", "withdrawals", True),
                    self._item("EPI-003-06", "Reviewer decision rationale", "Reviewer controls", "reviewer_required", "Reviewer decision rationale must be recorded before completion.", "compliance_review", True),
                ],
                triggered_controls=[
                    "Crypto off-ramp monitoring",
                    "Source of funds verification",
                    "Audit evidence generation",
                ],
                reviewer_notes=[
                    "Pause off-ramp movement in the prototype until the decision is recorded.",
                    "Confirm that this remains a fictional demo review only.",
                ],
                decision_rationale=(
                    "The package has strong monitoring evidence but cannot be "
                    "marked ready without reviewer rationale."
                ),
                timeline=self._timeline("003", "FCA-2026-004", "2026-06-12T11:30:00+03:00"),
                recommended_next_action=(
                    "Pause off-ramp movement until reviewer decision is recorded."
                ),
                created_at="2026-06-12T14:10:00+03:00",
            ),
            EvidencePackage(
                package_id="EP-2026-004",
                title="Foreign transfer monitoring evidence package",
                source_alert_id="FCA-2026-005",
                risk_type="Foreign transfer risk",
                severity="medium",
                status="ready",
                readiness_score=92,
                summary=(
                    "Repeated foreign transfer pattern includes beneficiary "
                    "validation, purpose placeholder, and audit timeline."
                ),
                included_evidence=[
                    self._item("EPI-004-01", "Repeated transfer pattern", "Transaction monitoring", "included", "Repeated foreign transfer pattern is included for reviewer inspection.", "financial_crime_monitoring", True),
                    self._item("EPI-004-02", "Beneficiary validation requirement", "Beneficiary review", "included", "Beneficiary validation requirement is documented.", "compliance_review", True),
                    self._item("EPI-004-03", "Purpose-of-transfer documentation placeholder", "Customer documentation", "included", "Purpose-of-transfer placeholder is attached for prototype review.", "compliance_review", True),
                    self._item("EPI-004-04", "Audit timeline", "Audit trail", "included", "Timeline contains monitoring and readiness events.", "audit_events", True),
                ],
                missing_evidence=[],
                triggered_controls=[
                    "Transaction pattern monitoring",
                    "Audit evidence generation",
                    "Beneficiary pattern validation",
                ],
                reviewer_notes=[
                    "Package is ready for review or prototype export.",
                    "No real legal report is generated by this demo module.",
                ],
                decision_rationale=(
                    "Required evidence is present and no readiness blockers remain."
                ),
                timeline=self._timeline("004", "FCA-2026-005", "2026-06-12T12:05:00+03:00"),
                recommended_next_action="Ready for review or export.",
                created_at="2026-06-12T14:35:00+03:00",
            ),
        ]

    def list_templates(self) -> list[EvidencePackageTemplate]:
        return [
            EvidencePackageTemplate(
                template_id="EPT-INTERNAL-REVIEW",
                title="Internal compliance review package",
                use_case="internal_review",
                description="Reviewer-facing package for internal compliance decisioning.",
                required_items=[
                    "Alert summary",
                    "Triggered controls",
                    "Supporting evidence",
                    "Missing evidence",
                    "Reviewer rationale",
                ],
            ),
            EvidencePackageTemplate(
                template_id="EPT-FC-ESCALATION",
                title="Financial crime escalation package",
                use_case="investigation",
                description="Structured handoff for enhanced investigation workflows.",
                required_items=[
                    "Risk indicators",
                    "Entity profile",
                    "Transaction timeline",
                    "Control rationale",
                    "Escalation recommendation",
                ],
            ),
            EvidencePackageTemplate(
                template_id="EPT-AUDIT",
                title="Audit evidence package",
                use_case="audit",
                description="Audit-oriented package focused on traceability and control evidence.",
                required_items=[
                    "Audit timeline",
                    "Decision record",
                    "Reviewer notes",
                    "Control outputs",
                ],
            ),
            EvidencePackageTemplate(
                template_id="EPT-REGULATOR",
                title="Regulator-facing evidence package",
                use_case="regulator",
                description=(
                    "Prototype structure for regulator-facing documentation readiness. "
                    "It does not create real legal or regulatory reports."
                ),
                required_items=[
                    "Case summary",
                    "Evidence inventory",
                    "Missing evidence statement",
                    "Decision rationale",
                    "Audit trail",
                ],
            ),
            EvidencePackageTemplate(
                template_id="EPT-OFF-RAMP",
                title="Digital asset off-ramp evidence package",
                use_case="internal_review",
                description="Evidence model for transfers to external digital asset destinations.",
                required_items=[
                    "Destination classification",
                    "Source of funds status",
                    "Destination ownership confirmation",
                    "Reviewer decision rationale",
                ],
            ),
        ]

    def get_package(self, package_id: str) -> EvidencePackage | None:
        return next(
            (package for package in self.list_packages() if package.package_id == package_id),
            None,
        )

    def generate_package(
        self,
        source_type: str,
        source_id: str,
        package_type: str,
        reviewer_id: str | None,
    ) -> GenerateEvidencePackageResponse:
        if source_type == "audit_event":
            package = self.get_package_from_audit_event(source_id)
            if package is None:
                package = self._build_generic_audit_event_package(source_id)

            readiness_check = self._build_readiness_check(package)
            audit_event_id = f"AUD-EVIDENCE-FROM-{_audit_token(source_id)}"
            correlation_id = package.correlation_id or f"CORR-EVIDENCE-FROM-{_audit_token(source_id)}"
            audit_event = audit_service.create_audit_event_from_sensitive_action(
                event_id=audit_event_id,
                actor_id=reviewer_id or "evidence-service",
                actor_type="staff" if reviewer_id else "service",
                source_module="evidence_packages",
                action="generate_from_audit_event",
                object_type="audit_event",
                object_id=source_id,
                decision="audit_event_evidence_package_prepared",
                severity=package.severity,
                risk_score=readiness_check.score,
                summary=(
                    "Evidence package prepared from structured audit event."
                ),
                evidence_reference=package.package_id,
                correlation_id=correlation_id,
                metadata={
                    "package_type": package_type,
                    "package_id": package.package_id,
                    "source_correlation_id": package.correlation_id,
                    "linked_audit_events": package.linked_audit_events,
                },
            )
            return self._response(
                package=package,
                readiness_check=readiness_check,
                audit_event_created=audit_event is not None,
                audit_event_id=audit_event.event_id,
                correlation_id=audit_event.correlation_id or "",
                source_type=source_type,
                source_id=source_id,
                user_message=(
                    "Evidence package generated from a structured audit event. "
                    "No real legal report, customer data, or regulator filing was created."
                ),
            )

        mapped_package_ids = {
            "FCA-2026-001": "EP-2026-001",
            "FCA-2026-002": "EP-2026-002",
            "FCA-2026-004": "EP-2026-003",
            "FCA-2026-005": "EP-2026-004",
        }
        package = self.get_package(mapped_package_ids.get(source_id, ""))

        if package is None:
            package = EvidencePackage(
                package_id="EP-DEMO-DRAFT",
                title="Generic draft evidence package",
                source_alert_id=source_id if source_type == "alert" else None,
                source_case_id=source_id if source_type in {"review_case", "case"} else None,
                risk_type="General compliance review",
                severity="medium",
                status="draft",
                readiness_score=45,
                summary=(
                    "Generic deterministic draft package for an unmapped demo source."
                ),
                included_evidence=[
                    self._item("EPI-DRAFT-01", "Source reference", "Source record", "included", "The provided source identifier is recorded for package preparation.", "evidence_packages", True),
                ],
                missing_evidence=[
                    self._item("EPI-DRAFT-02", "Reviewer rationale", "Reviewer controls", "reviewer_required", "Reviewer rationale is required before this draft can be marked ready.", "compliance_review", True),
                    self._item("EPI-DRAFT-03", "Supporting evidence inventory", "Evidence inventory", "missing", "Supporting evidence must be selected from the relevant prototype module.", "evidence_packages", True),
                ],
                triggered_controls=["Audit evidence generation"],
                reviewer_notes=[
                    f"Generated as {package_type} package type.",
                    f"Assigned reviewer: {reviewer_id or 'not assigned'}.",
                ],
                decision_rationale=(
                    "The source is not mapped to a deterministic package, so the "
                    "prototype created a draft requiring reviewer input."
                ),
                timeline=self._timeline("DRAFT", source_id, "2026-06-12T15:00:00+03:00"),
                recommended_next_action=(
                    "Attach supporting evidence and record reviewer rationale."
                ),
                created_at="2026-06-12T15:05:00+03:00",
            )

        readiness_check = self._build_readiness_check(package)
        audit_event_id = f"AUD-EVIDENCE-{_audit_token(source_id)}"
        correlation_id = f"CORR-EVIDENCE-{_audit_token(source_id)}"
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=reviewer_id or "evidence-service",
            actor_type="staff" if reviewer_id else "service",
            source_module="evidence_packages",
            action="generate_package",
            object_type=(
                "financial_crime_alert"
                if source_type == "alert"
                else "review_case"
            ),
            object_id=source_id,
            decision="evidence_package_prepared",
            severity=package.severity,
            risk_score=readiness_check.score,
            summary="Evidence package generated or prepared from source alert/case.",
            evidence_reference=package.package_id,
            correlation_id=correlation_id,
            metadata={
                "package_type": package_type,
                "package_id": package.package_id,
                "export_available": readiness_check.ready,
            },
        )
        return self._response(
            package=package,
            readiness_check=readiness_check,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            source_type=source_type,
            source_id=source_id,
            user_message=(
                "Evidence package generated from deterministic prototype data. "
                "No real legal report, customer data, or regulator filing was created."
            ),
        )

    def get_package_from_audit_event(
        self,
        audit_event_id: str,
    ) -> EvidencePackage | None:
        normalized_audit_event_id = audit_event_id.strip().upper()
        if normalized_audit_event_id == CRYPTO_AGILITY_AUDIT_EVENT_ID:
            return self._build_crypto_agility_audit_event_package()
        if (
            normalized_audit_event_id
            == SENSITIVE_APPROVAL_HIGH_VALUE_AUDIT_EVENT_ID
        ):
            return self._build_sensitive_approval_audit_event_package()

        if normalized_audit_event_id in INFRASTRUCTURE_AUDIT_EVENT_IDS:
            return self._build_infrastructure_audit_event_package(
                normalized_audit_event_id,
            )

        audit_event = self._find_audit_event(audit_event_id)
        if audit_event is None:
            return None
        return self._build_audit_event_package(audit_event)

    def get_readiness_check(self, package_id: str) -> EvidenceReadinessCheck:
        package = self.get_package(package_id)

        if package is None:
            return EvidenceReadinessCheck(
                ready=False,
                score=45,
                blockers=["Package source is not mapped to a deterministic demo package."],
                warnings=["Reviewer must confirm evidence scope before export readiness."],
                recommended_actions=[
                    "Attach supporting evidence.",
                    "Record reviewer rationale.",
                ],
            )

        return self._build_readiness_check(package)

    def _build_readiness_check(
        self,
        package: EvidencePackage,
    ) -> EvidenceReadinessCheck:
        blockers = [
            item.title
            for item in package.missing_evidence
            if item.required and item.status in {"missing", "reviewer_required"}
        ]
        warnings = [
            item.title
            for item in package.missing_evidence
            if not item.required or item.status == "optional"
        ]
        ready = package.status == "ready" and not blockers

        return EvidenceReadinessCheck(
            ready=ready,
            score=package.readiness_score,
            blockers=blockers,
            warnings=warnings
            or (
                []
                if ready
                else ["Package requires reviewer confirmation before export readiness."]
            ),
            recommended_actions=[
                package.recommended_next_action,
                "Retain audit trail references for reviewer traceability.",
            ],
        )

    def _response(
        self,
        *,
        package: EvidencePackage,
        readiness_check: EvidenceReadinessCheck,
        audit_event_created: bool,
        audit_event_id: str,
        correlation_id: str,
        source_type: str,
        source_id: str,
        user_message: str,
    ) -> GenerateEvidencePackageResponse:
        return GenerateEvidencePackageResponse(
            package=package,
            readiness_check=readiness_check,
            export_available=readiness_check.ready,
            audit_event_created=audit_event_created,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            source_type=source_type,
            source_id=source_id,
            source_audit_event_id=package.source_audit_event_id,
            traceability_summary=package.traceability_summary,
            evidence_items=package.included_evidence,
            linked_audit_events=package.linked_audit_events,
            recommended_next_steps=readiness_check.recommended_actions,
            user_message=user_message,
        )

    def _find_audit_event(self, audit_event_id: str) -> AuditEvent | None:
        normalized_audit_event_id = audit_event_id.strip().upper()
        return next(
            (
                event
                for event in audit_service.list_events()
                if event.event_id == normalized_audit_event_id
            ),
            None,
        )

    def _build_generic_audit_event_package(
        self,
        audit_event_id: str,
    ) -> EvidencePackage:
        return EvidencePackage(
            package_id=f"EP-FROM-{_audit_token(audit_event_id)}",
            title="Audit event evidence package",
            source_audit_event_id=audit_event_id,
            source_module="audit_events",
            backend_decision="unknown",
            correlation_id=f"CORR-EVIDENCE-FROM-{_audit_token(audit_event_id)}",
            traceability_summary=(
                "The audit event identifier is recorded, but no deterministic "
                "audit event was found in the prototype audit trail."
            ),
            audit_context={"audit_event_id": audit_event_id},
            linked_audit_events=[audit_event_id],
            risk_type="Audit event traceability",
            severity="medium",
            status="draft",
            readiness_score=45,
            summary="Draft package for an unmapped audit event source.",
            included_evidence=[
                self._item(
                    "EPI-AUDIT-GENERIC-01",
                    "Audit event ID",
                    "Audit trail",
                    "included",
                    f"Source audit event {audit_event_id} is recorded.",
                    "audit_events",
                    True,
                ),
            ],
            missing_evidence=[
                self._item(
                    "EPI-AUDIT-GENERIC-02",
                    "Audit event context",
                    "Traceability",
                    "missing",
                    "Structured audit event context is required before review.",
                    "audit_events",
                    True,
                ),
            ],
            triggered_controls=["Audit evidence generation"],
            reviewer_notes=["Confirm the audit event exists before export."],
            decision_rationale=(
                "The package remains draft because the source audit event was not found."
            ),
            timeline=self._audit_timeline("GENERIC", audit_event_id),
            recommended_next_action="Confirm audit event context before review.",
            created_at="2026-06-15T09:20:00+03:00",
        )

    def _build_crypto_agility_audit_event_package(self) -> EvidencePackage:
        audit_event_id = CRYPTO_AGILITY_AUDIT_EVENT_ID
        correlation_id = "CORR-CRYPTO-AGILITY-PQ-READINESS"
        included_evidence = [
            self._item("EPI-CRYPTO-AGILITY-01", "Cryptographic inventory snapshot", "Inventory", "included", "Simulated cryptographic asset inventory is included for internal review.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-02", "Algorithm version map", "Algorithm versioning", "included", "Algorithm family and policy versioning context is preserved.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-03", "Key lifecycle and rotation posture", "Key lifecycle", "included", "Rotation due, emergency rollover, and audit requirements are mapped.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-04", "Long-term confidentiality risk classification", "Confidentiality", "included", "Long-term confidentiality and harvest-now-decrypt-later risk context is included.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-05", "Backup encryption risk context", "Backup encryption", "included", "Backup encryption policy and long-lived retention risk are documented.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-06", "Audit log integrity context", "Audit integrity", "included", "Audit integrity and long-term verification context is included.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-07", "Custody key governance context", "Custody governance", "included", "External custody key governance boundaries and evidence gaps are recorded.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-08", "Platform crypto vs blockchain protocol separation", "Boundary control", "included", "Aurora platform cryptography is separated from external blockchain protocol cryptography.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-09", "Post-quantum migration readiness assessment", "Post-quantum readiness", "included", "Readiness is monitored as migration planning, without quantum-proof claims.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-10", "KMS/HSM/Key Vault integration gap", "Key governance", "included", "Production key governance integration gaps are included as architectural findings.", "crypto_agility", True),
            self._item("EPI-CRYPTO-AGILITY-11", "Audit event ID and correlation ID", "Audit traceability", "included", f"{audit_event_id} is preserved with correlation ID {correlation_id}.", "audit_events", True),
            self._item("EPI-CRYPTO-AGILITY-12", "Risk Operations escalation context", "Risk operations", "included", "Escalation context is included for cryptographic governance review.", "risk_operations", True),
        ]

        return EvidencePackage(
            package_id="EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS",
            title="Cryptographic Agility and Post-Quantum Readiness Evidence Package",
            source_audit_event_id=audit_event_id,
            source_module="crypto_agility",
            backend_decision="evidence_package_ready",
            correlation_id=correlation_id,
            traceability_summary=(
                f"Crypto-agility audit event {audit_event_id} is linked to "
                f"correlation ID {correlation_id}, domain cryptographic_agility, "
                "and category post_quantum_readiness."
            ),
            audit_context={
                "audit_event_id": audit_event_id,
                "correlation_id": correlation_id,
                "source_module": "crypto_agility",
                "domain": "cryptographic_agility",
                "category": "post_quantum_readiness",
                "readiness": "ready_for_internal_review",
                "evidence_package_ready": True,
            },
            linked_audit_events=[audit_event_id],
            risk_type="Cryptographic agility",
            severity="critical",
            status="ready",
            readiness_score=96,
            summary=(
                "This package summarizes a simulated cryptographic agility "
                "readiness gap involving cryptographic inventory, algorithm "
                "versioning, key rotation, long-term confidentiality risk, "
                "audit integrity, custody key governance, blockchain protocol "
                "separation, and post-quantum migration planning."
            ),
            included_evidence=included_evidence,
            missing_evidence=[],
            triggered_controls=[
                "Cryptographic inventory required",
                "Algorithm versioning required",
                "Key rotation policy required",
                "Long-term confidentiality classification required",
                "No custom cryptography",
                "KMS/HSM/Key Vault integration required",
                "Audit evidence required for key lifecycle events",
                "Blockchain protocol separation required",
                "Post-quantum readiness monitored",
            ],
            reviewer_notes=[
                "Crypto-agility evidence package is ready for internal review.",
                f"Source audit event: {audit_event_id}",
                f"Correlation ID: {correlation_id}",
                "No real cryptographic operation, key material, custody key, KMS, HSM, Key Vault, or post-quantum algorithm was accessed.",
            ],
            decision_rationale=(
                "The crypto-agility scenario produced a deterministic "
                "evidence-ready audit event with preserved governance "
                "traceability."
            ),
            timeline=self._audit_timeline(_audit_token(audit_event_id), audit_event_id),
            recommended_next_action=(
                "Create cryptographic inventory, version algorithms, define key "
                "rotation and emergency rollover procedures, classify long-term "
                "confidentiality risk, preserve audit evidence, and prepare a "
                "standards-based post-quantum migration roadmap."
            ),
            created_at="2026-06-15T09:45:00+03:00",
        )

    def _build_sensitive_approval_audit_event_package(self) -> EvidencePackage:
        audit_event_id = SENSITIVE_APPROVAL_HIGH_VALUE_AUDIT_EVENT_ID
        correlation_id = "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET"
        return EvidencePackage(
            package_id="EP-FROM-AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
            title="Sensitive Approval High-Value New Wallet Evidence Package",
            source_audit_event_id=audit_event_id,
            source_module="sensitive_approval",
            backend_decision="pending_review",
            correlation_id=correlation_id,
            traceability_summary=(
                f"Sensitive approval audit event {audit_event_id} is linked "
                f"to correlation ID {correlation_id}, domain "
                "sensitive_operations_approval, and category "
                "high_value_new_wallet_withdrawal."
            ),
            audit_context={
                "audit_event_id": audit_event_id,
                "correlation_id": correlation_id,
                "domain": "sensitive_operations_approval",
                "category": "high_value_new_wallet_withdrawal",
                "readiness": "ready_for_internal_review",
                "evidence_package_ready": True,
            },
            linked_audit_events=[audit_event_id],
            risk_type="Sensitive operation approval",
            severity="critical",
            status="ready",
            readiness_score=94,
            summary=(
                "This package summarizes a simulated high-value external wallet "
                "withdrawal to a new destination where customer mobile approval "
                "was recorded but backend risk evaluation still required "
                "customer-protection review."
            ),
            included_evidence=[
                self._item("EPI-APPROVAL-01", "Sensitive approval evaluation", "Approval decision", "included", "Backend decision, risk score, and simulated approval context are included.", "sensitive_approval", True),
                self._item("EPI-APPROVAL-02", "Mobile approval simulation status", "Step-up approval", "included", "The prototype records simulated mobile approval status without real push or MFA integration.", "sensitive_approval", True),
                self._item("EPI-APPROVAL-03", "High-value new wallet risk context", "Customer protection", "included", "High value and new destination controls are preserved for review.", "sensitive_approval", True),
                self._item("EPI-APPROVAL-04", "Audit event ID and correlation ID", "Audit traceability", "included", f"{audit_event_id} is preserved with correlation ID {correlation_id}.", "audit_events", True),
                self._item("EPI-APPROVAL-05", "Review case routing context", "Risk operations", "included", "CASE-APPROVAL-HIGH-VALUE-NEW-WALLET is ready for customer-protection review.", "review_cases", True),
            ],
            missing_evidence=[],
            triggered_controls=[
                "Mobile approval simulated",
                "Backend risk decision required",
                "High-value withdrawal review",
                "New wallet destination review",
                "Audit evidence generation",
            ],
            reviewer_notes=[
                "Mobile approval does not automatically mean execution.",
                "Backend risk evaluation remains authoritative.",
                "No real mobile approval, notification, payment, or blockchain execution occurred.",
            ],
            decision_rationale=(
                "The deterministic approval policy routes high-value new-wallet "
                "withdrawals to review even after simulated customer approval."
            ),
            timeline=self._audit_timeline(_audit_token(audit_event_id), audit_event_id),
            recommended_next_action=(
                "Route to Risk Operations / Customer Protection and preserve "
                "approval, destination, risk, and audit evidence."
            ),
            created_at="2026-06-16T11:20:00+03:00",
        )

    def _build_infrastructure_audit_event_package(
        self,
        audit_event_id: str,
    ) -> EvidencePackage:
        correlation_id = audit_event_id.replace("AUD-", "CORR-")
        category = INFRASTRUCTURE_AUDIT_EVENT_CATEGORIES[audit_event_id]
        is_azure_storage_identity = audit_event_id == "AUD-INFRA-AZURE-STORAGE-IDENTITY"
        is_k8s_hardening_failure = audit_event_id == "AUD-INFRA-K8S-HARDENING-FAILURE"
        package_title = (
            "Azure Storage to Identity Risk Evidence Package"
            if is_azure_storage_identity
            else "Container and Kubernetes Hardening Evidence Package"
            if is_k8s_hardening_failure
            else
            "Infrastructure Security Chain Reaction Evidence Package"
            if audit_event_id == "AUD-INFRA-CHAIN-REACTION"
            else "Infrastructure security evidence package"
        )
        domain = (
            "azure_identity_storage_security"
            if is_azure_storage_identity
            else "container_kubernetes_hardening"
            if is_k8s_hardening_failure
            else "infrastructure_security"
        )
        risk_context = (
            "Public storage exposure, certificate handling, service principal "
            "scope, deployment access, managed identity permissions, privileged "
            "identity roles, and monitoring gaps can combine into cloud identity risk."
            if is_azure_storage_identity
            else (
                "Dockerfile secrets, mutable images, root runtime, weak "
                "securityContext, service account tokens, broad RBAC, missing "
                "NetworkPolicies, missing resource limits, CIS audit gaps, and "
                "DevSecOps verification gaps can combine into platform-wide risk."
            )
            if is_k8s_hardening_failure
            else (
                "A backend vulnerability may become a chain reaction if "
                "Kubernetes permissions, cloud IAM trust, IAM policy scope, "
                "or secret management controls are weak."
            )
        )
        summary = (
            "This package summarizes a simulated Azure storage-to-identity "
            "chain reaction risk involving public storage exposure, certificate "
            "handling, service principal scope, deployment access, managed "
            "identity permissions, privileged identity roles, monitoring, audit "
            "evidence, and risk operations."
            if is_azure_storage_identity
            else (
                "This package summarizes a simulated container and Kubernetes "
                "hardening failure involving Dockerfile secrets, root runtime, "
                "weak Kubernetes securityContext, service account token exposure, "
                "broad RBAC, missing NetworkPolicies, missing resource limits, "
                "missing CIS audit, DevSecOps verification gaps, audit evidence, "
                "and risk operations."
            )
            if is_k8s_hardening_failure
            else (
                "This package summarizes a simulated cross-layer infrastructure "
                "security event connecting application authorization, Kubernetes "
                "RBAC, cloud IAM permissions, secrets exposure risk, audit "
                "evidence, and risk operations."
            )
        )
        included_evidence = (
            [
                self._item("EPI-AZURE-INFRA-01", "Azure storage exposure assessment", "Storage exposure", "included", "Simulated public storage exposure assessment is included.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-02", "Certificate protection context", "Certificate protection", "included", "Certificate handling and secure secret management context is recorded.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-03", "Service principal permission review", "Service principal", "included", "Service principal scope and excessive permission risk are mapped for review.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-04", "Deployment access control review", "Deployment access", "included", "Deployment credential posture is included for reviewer inspection.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-05", "Managed identity scope review", "Managed identity", "included", "Managed identity scope and workload permission context is included.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-06", "Password reset privilege review", "Privileged identity", "included", "Privileged identity administration risk is included.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-07", "Key Vault / secret access monitoring context", "Secret monitoring", "included", "Key Vault, secret, certificate, and key access monitoring context is included.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-08", "Identity behavior monitoring context", "Identity monitoring", "included", "Service principal sign-in, managed identity token, role assignment, and password reset monitoring context is included.", "infrastructure_security", True),
                self._item("EPI-AZURE-INFRA-09", "Audit event ID and correlation ID", "Audit traceability", "included", f"{audit_event_id} is preserved with correlation ID {correlation_id}.", "audit_events", True),
                self._item("EPI-AZURE-INFRA-10", "Risk Operations escalation context", "Risk operations", "included", "Escalation context is included for staff review and audit continuity.", "risk_operations", True),
            ]
            if is_azure_storage_identity
            else [
                self._item("EPI-K8S-HARDENING-01", "Dockerfile hardening assessment", "Dockerfile hardening", "included", "Dockerfile hardening context is included for deterministic review.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-02", "Image secret exposure context", "Image secrets", "included", "Image secret exposure context is recorded without inspecting any real image.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-03", "Non-root runtime verification", "Runtime permissions", "included", "Non-root runtime posture is included for reviewer inspection.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-04", "Kubernetes securityContext review", "Runtime hardening", "included", "securityContext hardening controls are mapped for review.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-05", "ServiceAccount token exposure review", "Service account", "included", "ServiceAccount token exposure is included as a deterministic indicator.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-06", "RBAC least privilege review", "RBAC", "included", "RBAC least privilege posture is included for review.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-07", "Kubernetes secret access review", "Kubernetes secrets", "included", "Kubernetes secret access risk is mapped to the evidence package.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-08", "NetworkPolicy isolation review", "Network policy", "included", "NetworkPolicy isolation posture is included.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-09", "Resource request and limit review", "Resource limits", "included", "CPU and memory request/limit posture is included.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-10", "CIS/kube-bench audit context", "CIS audit", "included", "CIS-style audit context is included without running kube-bench.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-11", "DevSecOps hardening verification context", "DevSecOps verification", "included", "Hardening verification evidence context is included.", "infrastructure_security", True),
                self._item("EPI-K8S-HARDENING-12", "Audit event ID and correlation ID", "Audit traceability", "included", f"{audit_event_id} is preserved with correlation ID {correlation_id}.", "audit_events", True),
                self._item("EPI-K8S-HARDENING-13", "Risk Operations escalation context", "Risk operations", "included", "Escalation context is included for staff review and audit continuity.", "risk_operations", True),
            ]
            if is_k8s_hardening_failure
            else [
                self._item("EPI-INFRA-01", "Infrastructure security scenario evaluation", "Scenario evaluation", "included", "Deterministic infrastructure scenario evaluation is included.", "infrastructure_security", True),
                self._item("EPI-INFRA-02", "Affected security layers", "Layer coverage", "included", "Application, Kubernetes, cloud IAM, secrets, audit, and risk operations context is recorded.", "infrastructure_security", True),
                self._item("EPI-INFRA-03", "Triggered infrastructure controls", "Control coverage", "included", "Triggered infrastructure controls are mapped for reviewer inspection.", "infrastructure_security", True),
                self._item("EPI-INFRA-04", "Chain reaction risk score", "Risk score", "included", "The deterministic chain reaction risk score is preserved for internal review.", "infrastructure_security", True),
                self._item("EPI-INFRA-05", "Audit event ID and correlation ID", "Audit traceability", "included", f"{audit_event_id} is preserved with correlation ID {correlation_id}.", "audit_events", True),
                self._item("EPI-INFRA-06", "Recommended hardening action", "Hardening", "included", "Application, Kubernetes, IAM, and secrets controls require hardening review.", "infrastructure_security", True),
                self._item("EPI-INFRA-07", "Evidence readiness confirmation", "Readiness", "included", "Evidence package readiness is confirmed for internal review.", "evidence_packages", True),
                self._item("EPI-INFRA-08", "Risk Operations escalation context", "Risk operations", "included", "Escalation context is included for staff review and audit continuity.", "risk_operations", True),
            ]
        )
        triggered_controls = (
            [
                "Azure private storage control",
                "Certificate protection control",
                "Service principal least privilege control",
                "Deployment access control",
                "Managed identity scope control",
                "Password reset privilege control",
                "Azure identity monitoring control",
                "Key Vault access monitoring control",
                "Storage-to-identity chain containment",
            ]
            if is_azure_storage_identity
            else [
                "Dockerfile hardening control",
                "Image secret exclusion control",
                "Non-root container runtime control",
                "Immutable image reference control",
                "Kubernetes securityContext control",
                "ServiceAccount token control",
                "Kubernetes RBAC least privilege control",
                "NetworkPolicy isolation control",
                "Resource limit enforcement control",
                "Cluster CIS audit control",
                "DevSecOps hardening verification control",
                "Runtime hardening evidence control",
            ]
            if is_k8s_hardening_failure
            else [
                "Object-level authorization guard",
                "Safe template execution control",
                "Kubernetes least privilege RBAC",
                "Service account secret restriction",
                "Cloud IAM trust policy restriction",
                "Cloud IAM permission scope",
                "Secret management control",
                "Cross-layer audit correlation",
                "Chain reaction containment",
            ]
        )

        return EvidencePackage(
            package_id=f"EP-FROM-{_audit_token(audit_event_id)}",
            title=package_title,
            source_audit_event_id=audit_event_id,
            source_module="infrastructure_security",
            backend_decision="evidence_package_ready",
            correlation_id=correlation_id,
            traceability_summary=(
                f"Infrastructure security audit event {audit_event_id} is linked "
                f"to correlation ID {correlation_id}, domain infrastructure_security, "
                f"and category {category}."
            ),
            audit_context={
                "audit_event_id": audit_event_id,
                "correlation_id": correlation_id,
                "domain": domain,
                "category": category,
                "evidence_package_ready": True,
                "readiness": "ready_for_internal_review",
                "risk_context": risk_context,
                "review_questions": (
                    [
                        "Were Dockerfile secrets removed and rotated?",
                        "Does the workload run as non-root?",
                        "Is Kubernetes securityContext enforced?",
                        "Is automatic ServiceAccount token mounting disabled?",
                        "Is RBAC scoped to least privilege?",
                        "Are NetworkPolicies and resource limits defined?",
                        "Is CIS-style and DevSecOps hardening evidence preserved?",
                    ]
                    if is_k8s_hardening_failure
                    else [
                        "Was the original application weakness blocked?",
                        "Could the affected workload read Kubernetes secrets?",
                        "Were IAM trust conditions bound to a specific service account?",
                        "Were IAM permissions scoped to specific resources?",
                        "Was any secret exposed or logged?",
                        "Was the event correlated across application, Kubernetes, IAM, secrets, and risk operations?",
                        "Was escalation required?",
                    ]
                ),
            },
            linked_audit_events=[audit_event_id],
            risk_type="Infrastructure security traceability",
            severity="critical" if audit_event_id != "AUD-INFRA-TEMPLATE" else "high",
            status="ready",
            readiness_score=96
            if is_k8s_hardening_failure
            else 94
            if audit_event_id == "AUD-INFRA-CHAIN-REACTION"
            else 90,
            summary=summary,
            included_evidence=included_evidence,
            missing_evidence=[],
            triggered_controls=triggered_controls,
            reviewer_notes=[
                "Infrastructure evidence package is ready for internal review.",
                f"Source audit event: {audit_event_id}",
                f"Correlation ID: {correlation_id}",
                "No real cloud, Kubernetes, scanning, or secret access was performed.",
            ],
            decision_rationale=(
                "The infrastructure scenario produced a deterministic evidence-ready "
                "audit event with preserved cross-layer correlation."
            ),
            timeline=self._audit_timeline(_audit_token(audit_event_id), audit_event_id),
            recommended_next_action=(
                "Escalate to Risk Operations, preserve audit evidence, and harden "
                "Dockerfile, image secrets, non-root runtime, Kubernetes "
                "securityContext, ServiceAccount token settings, RBAC, "
                "NetworkPolicies, resource limits, CIS audit, and DevSecOps "
                "verification."
                if is_k8s_hardening_failure
                else "Escalate to Risk Operations, preserve audit evidence, and harden "
                "application, Kubernetes, IAM, and secrets controls."
            ),
            created_at="2026-06-15T09:30:00+03:00",
        )

    def _build_audit_event_package(
        self,
        audit_event: AuditEvent,
    ) -> EvidencePackage:
        metadata = audit_event.metadata or {}
        title = AUDIT_EVENT_PACKAGE_TITLES.get(
            audit_event.event_id,
            f"Audit event evidence package - {audit_event.event_id}",
        )
        included_evidence = self._audit_event_items(audit_event)
        traceability_summary = (
            f"Audit event {audit_event.event_id} from "
            f"{audit_event.source_module or audit_event.module} recorded "
            f"decision {audit_event.decision or 'not recorded'} with "
            f"correlation ID {audit_event.correlation_id or 'not recorded'}."
        )
        missing_evidence = [
            self._item(
                f"EPI-{_audit_token(audit_event.event_id)}-MISSING-01",
                "Reviewer rationale",
                "Reviewer controls",
                "reviewer_required",
                "Reviewer must confirm the audit event evidence before package closure.",
                "compliance_review",
                True,
            )
        ]
        readiness_score = self._audit_event_readiness_score(audit_event)

        return EvidencePackage(
            package_id=f"EP-FROM-{_audit_token(audit_event.event_id)}",
            title=title,
            source_audit_event_id=audit_event.event_id,
            source_module=audit_event.source_module or audit_event.module,
            backend_decision=audit_event.decision,
            correlation_id=audit_event.correlation_id,
            traceability_summary=traceability_summary,
            audit_context={
                "audit_event_id": audit_event.event_id,
                "correlation_id": audit_event.correlation_id,
                "source_module": audit_event.source_module or audit_event.module,
                "action": audit_event.action or audit_event.action_type,
                "decision": audit_event.decision,
                "severity": audit_event.severity or audit_event.risk_level,
                "object_type": audit_event.object_type,
                "object_id": audit_event.object_id,
                "summary": audit_event.summary,
                "immutable_note": audit_event.immutable_note,
                "metadata": metadata,
            },
            linked_audit_events=[audit_event.event_id],
            risk_type=self._audit_event_risk_type(audit_event),
            severity=self._normalize_severity(audit_event.severity or audit_event.risk_level),
            status="draft",
            readiness_score=readiness_score,
            summary=audit_event.summary or traceability_summary,
            included_evidence=included_evidence,
            missing_evidence=missing_evidence,
            triggered_controls=self._metadata_list(metadata, "triggered_controls")
            or self._metadata_list(metadata, "controls_activated")
            or ["Audit event correlation"],
            reviewer_notes=[
                f"Source audit event: {audit_event.event_id}",
                f"Correlation ID: {audit_event.correlation_id or 'not recorded'}",
                "Review package remains a deterministic prototype record.",
            ],
            decision_rationale=(
                f"Backend decision '{audit_event.decision or 'not recorded'}' "
                "was preserved from the structured audit event."
            ),
            timeline=self._audit_timeline(_audit_token(audit_event.event_id), audit_event.event_id),
            recommended_next_action=self._audit_event_recommendation(audit_event),
            created_at="2026-06-15T09:20:00+03:00",
        )

    def _audit_event_items(self, audit_event: AuditEvent) -> list[EvidenceItem]:
        metadata = audit_event.metadata or {}
        base_items = [
            ("Audit event ID", audit_event.event_id, "Audit trail"),
            ("Correlation ID", audit_event.correlation_id, "Traceability"),
            ("Source module", audit_event.source_module or audit_event.module, "Source"),
            ("Backend decision", audit_event.decision, "Decision"),
            ("Object reference", f"{audit_event.object_type}: {audit_event.object_id}", "Object"),
            ("Immutable note", audit_event.immutable_note, "Audit trail"),
        ]
        items = [
            self._item(
                f"EPI-{_audit_token(audit_event.event_id)}-{index:02d}",
                title,
                category,
                "included",
                str(value or "Not recorded"),
                "audit_events",
                True,
            )
            for index, (title, value, category) in enumerate(base_items, start=1)
        ]

        for key in [
            "operation_name",
            "attempts",
            "affected_service",
            "dependency_status",
            "customer_impact",
            "paused_operations",
            "required_action",
            "missing_evidence",
            "package_id",
            "package_type",
            "export_available",
        ]:
            if key in metadata:
                items.append(
                    self._item(
                        f"EPI-{_audit_token(audit_event.event_id)}-META-{key.upper()}",
                        key.replace("_", " ").title(),
                        "Audit metadata",
                        "included",
                        str(metadata[key]),
                        "audit_events",
                        True,
                    )
                )

        controls = self._metadata_list(metadata, "triggered_controls") or self._metadata_list(
            metadata,
            "controls_activated",
        )
        for index, control in enumerate(controls, start=1):
            items.append(
                self._item(
                    f"EPI-{_audit_token(audit_event.event_id)}-CTRL-{index:02d}",
                    control,
                    "Triggered controls",
                    "included",
                    "Control preserved from audit event metadata.",
                    "audit_events",
                    True,
                )
            )

        return items

    def _metadata_list(
        self,
        metadata: dict,
        key: str,
    ) -> list[str]:
        value = metadata.get(key)
        return value if isinstance(value, list) else []

    def _audit_event_readiness_score(self, audit_event: AuditEvent) -> int:
        if audit_event.event_id == "AUD-EVIDENCE-FCA-2026-002":
            return 78
        if audit_event.event_id == "AUD-OPS-PAYMENTS-DEGRADED":
            return 84
        if audit_event.event_id == "AUD-API-GRAPHQL-PIN":
            return 86
        if audit_event.event_id == "AUD-RISK-RO-ACTION-002":
            return 82
        return 65

    def _audit_event_risk_type(self, audit_event: AuditEvent) -> str:
        if audit_event.source_module == "api_security":
            return "API security traceability"
        if audit_event.source_module == "operational_resilience":
            return "Operational resilience traceability"
        if audit_event.source_module == "risk_operations":
            return "Risk operations traceability"
        if audit_event.source_module == "evidence_packages":
            return "Evidence generation traceability"
        return "Audit event traceability"

    def _audit_event_recommendation(self, audit_event: AuditEvent) -> str:
        if audit_event.source_module == "api_security":
            return "Review API decision, rate-limit evidence, and request envelope summary."
        if audit_event.source_module == "operational_resilience":
            return "Review continuity controls, paused operations, and dependency recovery path."
        if audit_event.source_module == "risk_operations":
            return "Confirm review case context, priority, and required evidence."
        if audit_event.source_module == "evidence_packages":
            return "Confirm source package readiness, blockers, and audit trail continuity."
        return "Review audit context before package closure."

    def _normalize_severity(self, value: str | None) -> str:
        if value in {"low", "medium", "high", "critical"}:
            return value
        if value == "urgent":
            return "critical"
        return "medium"

    def _item(
        self,
        item_id: str,
        title: str,
        category: str,
        status: str,
        description: str,
        source_module: str,
        required: bool,
    ) -> EvidenceItem:
        return EvidenceItem(
            item_id=item_id,
            title=title,
            category=category,
            status=status,
            description=description,
            source_module=source_module,
            required=required,
        )

    def _timeline(
        self,
        suffix: str,
        alert_id: str,
        alert_timestamp: str,
    ) -> list[EvidenceTimelineEvent]:
        return [
            EvidenceTimelineEvent(
                event_id=f"EPT-{suffix}-01",
                timestamp=alert_timestamp,
                event_type="alert_created",
                title="Monitoring alert created",
                description=f"Demo alert {alert_id} was created by the monitoring layer.",
                source_module="financial_crime_monitoring",
            ),
            EvidenceTimelineEvent(
                event_id=f"EPT-{suffix}-02",
                timestamp="2026-06-12T13:00:00+03:00",
                event_type="evidence_collected",
                title="Evidence inventory prepared",
                description="Included and missing evidence were mapped for reviewer inspection.",
                source_module="evidence_packages",
            ),
            EvidenceTimelineEvent(
                event_id=f"EPT-{suffix}-03",
                timestamp="2026-06-12T14:00:00+03:00",
                event_type="readiness_checked",
                title="Readiness check calculated",
                description="Deterministic readiness score and blockers were calculated.",
                source_module="evidence_packages",
            ),
        ]

    def _audit_timeline(
        self,
        suffix: str,
        audit_event_id: str,
    ) -> list[EvidenceTimelineEvent]:
        return [
            EvidenceTimelineEvent(
                event_id=f"EPT-AUDIT-{suffix}-01",
                timestamp="2026-06-15T09:00:00+03:00",
                event_type="audit_event_recorded",
                title="Audit event recorded",
                description=(
                    f"Structured audit event {audit_event_id} was recorded by "
                    "the backend decision workflow."
                ),
                source_module="audit_events",
            ),
            EvidenceTimelineEvent(
                event_id=f"EPT-AUDIT-{suffix}-02",
                timestamp="2026-06-15T09:10:00+03:00",
                event_type="traceability_context_mapped",
                title="Traceability context mapped",
                description=(
                    "Decision, correlation ID, object reference, and metadata "
                    "were mapped into evidence package context."
                ),
                source_module="evidence_packages",
            ),
            EvidenceTimelineEvent(
                event_id=f"EPT-AUDIT-{suffix}-03",
                timestamp="2026-06-15T09:20:00+03:00",
                event_type="evidence_package_prepared",
                title="Evidence package prepared",
                description=(
                    "Audit-linked evidence package was prepared for reviewer inspection."
                ),
                source_module="evidence_packages",
            ),
        ]


evidence_packages_service = EvidencePackagesService()
