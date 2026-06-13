from app.schemas.evidence_packages import (
    EvidenceItem,
    EvidencePackage,
    EvidencePackageTemplate,
    EvidenceReadinessCheck,
    EvidenceTimelineEvent,
    GenerateEvidencePackageResponse,
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
                source_case_id=source_id if source_type == "review_case" else None,
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

        readiness_check = self.get_readiness_check(package.package_id)
        return GenerateEvidencePackageResponse(
            package=package,
            readiness_check=readiness_check,
            export_available=readiness_check.ready,
            user_message=(
                "Evidence package generated from deterministic prototype data. "
                "No real legal report, customer data, or regulator filing was created."
            ),
        )

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


evidence_packages_service = EvidencePackagesService()
