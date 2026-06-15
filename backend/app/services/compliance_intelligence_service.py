from app.schemas.compliance_intelligence import (
    DecisionPathStep,
    EvidenceRequirement,
    ExplainAlertResponse,
    PrepareReviewCaseResponse,
    ReviewPriority,
    ReviewerGuidance,
    RiskExplanation,
)
from app.services.audit_service import audit_service


class ComplianceIntelligenceService:
    """Provides deterministic compliance reasoning demo data."""

    def list_risk_explanations(self) -> list[RiskExplanation]:
        return [
            RiskExplanation(
                explanation_id="CI-EXP-2026-001",
                alert_id="FCA-2026-001",
                alert_title="Employee-linked account activity mismatch",
                risk_type="Insider risk",
                severity="critical",
                risk_summary=(
                    "Staff-linked activity exceeds the expected profile and "
                    "includes repeated external transfer behavior."
                ),
                reasoning=(
                    "The activity is connected to a staff-linked profile, "
                    "exceeds expected activity, and includes repeated external "
                    "transfer behavior. Staff-linked anomalies require enhanced "
                    "review and preservation of audit evidence."
                ),
                triggered_controls=[
                    "Employee risk monitoring",
                    "External transfer anomaly monitoring",
                    "Audit evidence preservation",
                ],
                supporting_evidence=[
                    "Staff-linked account indicator",
                    "Activity above expected income profile",
                    "Repeated external transfer pattern",
                ],
                missing_evidence=[
                    "Documented source of funds",
                    "Reviewer conflict-of-interest check",
                    "Transfer purpose documentation",
                ],
                reviewer_questions=[
                    "Is the staff relationship confirmed and documented?",
                    "Does the activity have a legitimate economic purpose?",
                    "Should external transfers remain restricted during review?",
                ],
                recommended_decision="escalate",
                evidence_package_ready=False,
            ),
            RiskExplanation(
                explanation_id="CI-EXP-2026-002",
                alert_id="FCA-2026-002",
                alert_title="New company transaction growth anomaly",
                risk_type="Shell company indicator",
                severity="critical",
                risk_summary=(
                    "A recently created company shows rapid transaction growth "
                    "that is not sufficiently explained by declared activity."
                ),
                reasoning=(
                    "The company is recently created, transaction volume "
                    "increased rapidly, and declared business activity does not "
                    "sufficiently explain the funds movement. Enhanced company "
                    "documentation and source of funds evidence are required."
                ),
                triggered_controls=[
                    "Customer and company KYC",
                    "Source of funds verification",
                    "Transaction pattern monitoring",
                ],
                supporting_evidence=[
                    "Company age below prototype threshold",
                    "Rapid incoming and outgoing funds movement",
                    "Declared activity mismatch indicator",
                ],
                missing_evidence=[
                    "Beneficial ownership evidence",
                    "Source of funds evidence",
                    "Business rationale for transaction volume",
                ],
                reviewer_questions=[
                    "Do company documents explain the observed funds movement?",
                    "Are beneficial owners and controllers documented?",
                    "Is escalation required before further transfers continue?",
                ],
                recommended_decision="escalate",
                evidence_package_ready=False,
            ),
            RiskExplanation(
                explanation_id="CI-EXP-2026-003",
                alert_id="FCA-2026-003",
                alert_title="Structured deposits across linked accounts",
                risk_type="Mule account pattern",
                severity="high",
                risk_summary=(
                    "Linked accounts show repeated smaller deposits followed by "
                    "rapid consolidation to a common destination."
                ),
                reasoning=(
                    "Multiple smaller deposits across linked accounts followed "
                    "by rapid consolidation may indicate mule account or "
                    "structuring behavior. Originators, destination purpose, "
                    "and account links must be validated."
                ),
                triggered_controls=[
                    "Transaction pattern monitoring",
                    "Network risk detection",
                    "Source of funds verification",
                ],
                supporting_evidence=[
                    "Repeated small deposit pattern",
                    "Multiple originators across linked accounts",
                    "Common destination account",
                ],
                missing_evidence=[
                    "Originator relationship evidence",
                    "Destination purpose documentation",
                    "Account link validation notes",
                ],
                reviewer_questions=[
                    "Are the linked accounts controlled by related parties?",
                    "What is the purpose of consolidation?",
                    "Do originators have a legitimate relationship to the account?",
                ],
                recommended_decision="review_required",
                evidence_package_ready=False,
            ),
            RiskExplanation(
                explanation_id="CI-EXP-2026-004",
                alert_id="FCA-2026-004",
                alert_title="Crypto off-ramp risk",
                risk_type="Crypto off-ramp",
                severity="high",
                risk_summary=(
                    "Funds are moving to an external digital asset platform "
                    "while source of funds evidence is incomplete."
                ),
                reasoning=(
                    "Funds are moving from the banking environment to an "
                    "external digital asset platform while source of funds "
                    "evidence is incomplete. Review is required before funds "
                    "leave the bank-controlled environment."
                ),
                triggered_controls=[
                    "Crypto off-ramp monitoring",
                    "Source of funds verification",
                    "Audit evidence generation",
                ],
                supporting_evidence=[
                    "Destination classified as external digital asset platform",
                    "Transfer amount above prototype review threshold",
                    "Incomplete source of funds status",
                ],
                missing_evidence=[
                    "Source of funds evidence",
                    "Destination ownership or relationship evidence",
                    "Reviewer notes on transfer purpose",
                ],
                reviewer_questions=[
                    "Is the destination controlled by the customer?",
                    "Can the customer evidence the source of funds?",
                    "Should transfer execution remain paused until review closes?",
                ],
                recommended_decision="review_required",
                evidence_package_ready=False,
            ),
            RiskExplanation(
                explanation_id="CI-EXP-2026-005",
                alert_id="FCA-2026-005",
                alert_title="Foreign transfer risk",
                risk_type="Foreign transfer risk",
                severity="medium",
                risk_summary=(
                    "Repeated international transfers have unclear economic "
                    "justification and require beneficiary validation."
                ),
                reasoning=(
                    "Repeated international transfers with unclear economic "
                    "justification require beneficiary validation and additional "
                    "purpose-of-transfer documentation."
                ),
                triggered_controls=[
                    "International transfer monitoring",
                    "Beneficiary validation",
                    "Audit evidence generation",
                ],
                supporting_evidence=[
                    "Repeated foreign transfer pattern",
                    "Unclear economic justification",
                    "Beneficiary pattern requires validation",
                ],
                missing_evidence=[
                    "Beneficiary relationship evidence",
                    "Purpose-of-transfer documentation",
                    "Reviewer disposition notes",
                ],
                reviewer_questions=[
                    "Does the customer have a documented beneficiary relationship?",
                    "Is there a clear economic purpose for the transfers?",
                    "Can the alert be closed after documentation is received?",
                ],
                recommended_decision="review_required",
                evidence_package_ready=True,
            ),
        ]

    def list_reviewer_guidance(self) -> list[ReviewerGuidance]:
        return [
            ReviewerGuidance(
                guidance_id="CI-GUIDE-INSIDER",
                title="Insider risk review",
                category="Insider risk",
                description=(
                    "Review staff-linked activity with enhanced independence, "
                    "audit preservation, and transfer control."
                ),
                checklist=[
                    "Confirm staff-linked profile indicator",
                    "Preserve relevant audit trail records",
                    "Check whether reviewer independence is required",
                    "Escalate unresolved staff-linked anomalies",
                ],
                reviewer_action="Escalate if staff-linked activity remains unexplained.",
            ),
            ReviewerGuidance(
                guidance_id="CI-GUIDE-SHELL-COMPANY",
                title="Shell company review",
                category="Company due diligence",
                description=(
                    "Assess whether company age, ownership, declared activity, "
                    "and transaction volume align."
                ),
                checklist=[
                    "Validate company registration and ownership",
                    "Compare declared activity with funds movement",
                    "Request source of funds evidence",
                    "Document rationale before allowing further transfers",
                ],
                reviewer_action="Escalate if ownership or source of funds is incomplete.",
            ),
            ReviewerGuidance(
                guidance_id="CI-GUIDE-STRUCTURED-DEPOSITS",
                title="Structured deposits review",
                category="Transaction monitoring",
                description=(
                    "Review linked deposits, account relationships, and rapid "
                    "movement to a shared destination."
                ),
                checklist=[
                    "Validate originator relationships",
                    "Review account link evidence",
                    "Confirm destination purpose",
                    "Prepare network review notes",
                ],
                reviewer_action="Keep under review until account links are validated.",
            ),
            ReviewerGuidance(
                guidance_id="CI-GUIDE-CRYPTO-OFF-RAMP",
                title="Crypto off-ramp review",
                category="Digital assets",
                description=(
                    "Review external digital asset platform transfers before "
                    "funds leave the bank-controlled environment."
                ),
                checklist=[
                    "Confirm destination type and ownership",
                    "Request source of funds evidence",
                    "Check whether transfer execution should remain paused",
                    "Record reviewer decision and rationale",
                ],
                reviewer_action="Require review before permitting external off-ramp movement.",
            ),
            ReviewerGuidance(
                guidance_id="CI-GUIDE-FOREIGN-TRANSFER",
                title="Foreign transfer review",
                category="Payments monitoring",
                description=(
                    "Validate economic purpose and beneficiary relationships for "
                    "repeated international transfers."
                ),
                checklist=[
                    "Validate beneficiary identity or relationship",
                    "Request purpose-of-transfer documentation",
                    "Review frequency and corridor pattern",
                    "Close only when rationale is documented",
                ],
                reviewer_action="Review required until transfer purpose is evidenced.",
            ),
            ReviewerGuidance(
                guidance_id="CI-GUIDE-EVIDENCE-PACKAGE",
                title="Evidence package readiness",
                category="Case preparation",
                description=(
                    "Check that evidence, reviewer notes, control triggers, and "
                    "audit trail records are available before case packaging."
                ),
                checklist=[
                    "Include triggered controls",
                    "Include supporting evidence",
                    "List missing evidence",
                    "Add reviewer notes and decision rationale",
                    "Attach audit trail references",
                ],
                reviewer_action="Prepare package only when required evidence is tracked.",
            ),
        ]

    def explain_alert(
        self,
        alert_id: str,
        include_evidence_requirements: bool,
    ) -> ExplainAlertResponse:
        explanation = self.get_risk_explanation(alert_id)
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=f"AUD-CI-EXPLAIN-{explanation.alert_id}",
            actor_id="compliance-intelligence-engine",
            actor_type="service",
            source_module="compliance_intelligence",
            action="explain_alert",
            object_type="financial_crime_alert",
            object_id=explanation.alert_id,
            decision=explanation.recommended_decision,
            severity=explanation.severity,
            summary="Compliance Intelligence explanation generated for alert.",
            evidence_reference=explanation.alert_id,
            correlation_id=f"CORR-CI-EXPLAIN-{explanation.alert_id}",
            metadata={
                "include_evidence_requirements": include_evidence_requirements,
                "missing_evidence": explanation.missing_evidence,
            },
        )
        return ExplainAlertResponse(
            alert_id=alert_id,
            explanation=explanation,
            decision_path=self.get_decision_path(explanation),
            evidence_requirements=(
                self.get_evidence_requirements(explanation)
                if include_evidence_requirements
                else []
            ),
            reviewer_next_steps=self.get_reviewer_next_steps(explanation),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
        )

    def prepare_review_case(
        self,
        alert_id: str,
        priority: ReviewPriority,
        reviewer_id: str | None = None,
    ) -> PrepareReviewCaseResponse:
        explanation = self.get_risk_explanation(alert_id)
        assignment = reviewer_id or self.get_recommended_assignment(explanation)
        case_preview_id = f"CI-CASE-PREVIEW-{alert_id.removeprefix('FCA-')}"
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=f"AUD-CI-PREPARE-{explanation.alert_id}",
            actor_id=assignment,
            actor_type="staff",
            source_module="compliance_intelligence",
            action="prepare_review_case",
            object_type="financial_crime_alert",
            object_id=explanation.alert_id,
            decision="case_preview_prepared",
            severity=priority,
            summary="Compliance Intelligence prepared a review case preview.",
            evidence_reference=case_preview_id,
            correlation_id=f"CORR-CI-PREPARE-{explanation.alert_id}",
            metadata={
                "recommended_decision": explanation.recommended_decision,
                "required_evidence": explanation.missing_evidence,
            },
        )

        return PrepareReviewCaseResponse(
            case_preview_id=case_preview_id,
            alert_id=alert_id,
            priority=priority,
            case_title=f"{explanation.alert_title} review",
            case_summary=(
                f"{explanation.risk_summary} Recommended decision: "
                f"{explanation.recommended_decision.replace('_', ' ')}."
            ),
            included_evidence=explanation.supporting_evidence
            + explanation.triggered_controls,
            required_evidence=explanation.missing_evidence,
            recommended_assignment=assignment,
            ready_for_review=bool(
                explanation.supporting_evidence and explanation.triggered_controls
            ),
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
        )

    def get_risk_explanation(self, alert_id: str) -> RiskExplanation:
        normalized_alert_id = alert_id.strip().upper()
        for explanation in self.list_risk_explanations():
            if explanation.alert_id == normalized_alert_id:
                return explanation

        raise ValueError(f"Unknown demo alert id: {alert_id}")

    def get_decision_path(
        self,
        explanation: RiskExplanation,
    ) -> list[DecisionPathStep]:
        decision_action = (
            "Escalate if evidence is insufficient"
            if explanation.recommended_decision == "escalate"
            else "Keep under review if evidence is insufficient"
        )

        return [
            DecisionPathStep(
                step_number=1,
                title="Preserve audit trail",
                description="Retain triggered controls, activity records, and reviewer actions.",
            ),
            DecisionPathStep(
                step_number=2,
                title="Validate customer or entity profile",
                description="Confirm profile, relationship, and expected activity context.",
            ),
            DecisionPathStep(
                step_number=3,
                title="Request missing evidence",
                description="Collect source, ownership, purpose, and reviewer notes as required.",
            ),
            DecisionPathStep(
                step_number=4,
                title=decision_action,
                description="Apply the recommended decision path when evidence remains incomplete.",
            ),
            DecisionPathStep(
                step_number=5,
                title="Prepare evidence package if required",
                description="Package evidence when escalation or formal review is needed.",
            ),
        ]

    def get_evidence_requirements(
        self,
        explanation: RiskExplanation,
    ) -> list[EvidenceRequirement]:
        missing_titles = set(explanation.missing_evidence)

        requirements = [
            ("source-of-funds", "Source of funds evidence", "Funds legitimacy"),
            (
                "entity-ownership",
                "Entity ownership or relationship evidence",
                "Due diligence",
            ),
            ("transaction-purpose", "Transaction purpose evidence", "Transaction monitoring"),
            ("reviewer-notes", "Reviewer notes", "Review record"),
            ("audit-trail", "Audit trail", "Audit evidence"),
        ]

        return [
            EvidenceRequirement(
                requirement_id=f"CI-EVIDENCE-{requirement_id.upper()}",
                title=title,
                category=category,
                description=f"{title} required for {explanation.alert_id}.",
                status=(
                    "missing"
                    if any(title.lower() in item.lower() for item in missing_titles)
                    else "reviewer_required"
                    if title == "Reviewer notes"
                    else "included"
                ),
                required=True,
            )
            for requirement_id, title, category in requirements
        ]

    def get_reviewer_next_steps(self, explanation: RiskExplanation) -> list[str]:
        return [
            "Confirm the triggered controls and supporting evidence.",
            "Request or record all missing evidence items.",
            "Document reviewer questions before disposition.",
            (
                "Escalate the alert with an evidence package."
                if explanation.recommended_decision == "escalate"
                else "Keep the alert under review until evidence is complete."
            ),
        ]

    def get_recommended_assignment(self, explanation: RiskExplanation) -> str:
        if explanation.severity == "critical":
            return "Senior financial crime reviewer"
        if explanation.risk_type in {"Crypto off-ramp", "Foreign transfer risk"}:
            return "Payments and digital assets compliance reviewer"
        return "Financial crime monitoring reviewer"


compliance_intelligence_service = ComplianceIntelligenceService()
