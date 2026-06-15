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
            correlation_id = f"CORR-EVIDENCE-FROM-{_audit_token(source_id)}"
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
