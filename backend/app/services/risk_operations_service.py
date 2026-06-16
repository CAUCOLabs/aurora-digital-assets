from app.schemas.risk_operations import (
    EscalationSummary,
    RiskActionItem,
    RiskOperationsLink,
    RiskOperationsMetric,
    RiskOperationsOverview,
    RiskOperationsReviewCaseResponse,
    UnifiedTimelineEvent,
)
from app.services.audit_service import audit_service
from app.services.review_case_service import review_case_service


REVIEW_CASE_TITLES = {
    "RO-ACTION-001": "Insider risk escalation review",
    "RO-ACTION-002": "Shell company evidence review",
    "RO-ACTION-003": "Crypto off-ramp operational review",
    "RO-ACTION-004": "Payments degradation operational review",
    "RO-ACTION-005": "Foreign transfer evidence review",
    "RO-ACTION-006": "Structured deposits compliance review",
    "RO-ACTION-007": "Infrastructure chain reaction review",
}


class RiskOperationsService:
    """Provides deterministic cross-module risk operations demo data."""

    def get_overview(self) -> RiskOperationsOverview:
        return RiskOperationsOverview(
            generated_at="2026-06-14T12:00:00+03:00",
            metrics=[
                self._metric(
                    "rom-active-fc-alerts",
                    "Active financial crime alerts",
                    "5",
                    "warning",
                    "Open monitoring alerts requiring staff visibility.",
                    "financial_crime",
                ),
                self._metric(
                    "rom-critical-fc-alerts",
                    "Critical financial crime alerts",
                    "2",
                    "critical",
                    "Critical alerts linked to insider risk and shell company indicators.",
                    "financial_crime",
                ),
                self._metric(
                    "rom-incomplete-evidence",
                    "Evidence packages incomplete",
                    "2",
                    "critical",
                    "Evidence packages with missing required documentation.",
                    "evidence_packages",
                ),
                self._metric(
                    "rom-active-incidents",
                    "Operational incidents active",
                    "3",
                    "warning",
                    "Operational resilience incidents that are open or under investigation.",
                    "operational_resilience",
                ),
                self._metric(
                    "rom-paused-operations",
                    "Operations paused",
                    "4",
                    "critical",
                    "Sensitive transfers and external digital asset movements remain paused.",
                    "operational_resilience",
                ),
                self._metric(
                    "rom-review-ready-packages",
                    "Review-ready evidence packages",
                    "1",
                    "attention",
                    "Evidence packages ready for review or prototype export.",
                    "evidence_packages",
                ),
                self._metric(
                    "rom-critical-escalations",
                    "Critical escalations",
                    "2",
                    "critical",
                    "Critical escalations require reviewer attention.",
                    "compliance_review",
                ),
                self._metric(
                    "rom-staff-action-items",
                    "Staff action items",
                    "7",
                    "warning",
                    "Unified action queue items across risk, evidence, and resilience.",
                    "reports",
                ),
                self._metric(
                    "rom-infrastructure-chain-risks",
                    "Infrastructure chain risks",
                    "1",
                    "critical",
                    "Application-to-cloud chain reaction risk requiring infrastructure security review.",
                    "infrastructure_security",
                ),
            ],
            highest_priority="urgent",
            operating_mode="restricted_operations",
            summary=(
                "Financial crime alerts, evidence gaps, and operational resilience "
                "incidents are active. Sensitive transfers and external digital "
                "asset movement should remain paused until review and evidence "
                "requirements are satisfied."
            ),
            recommended_focus=[
                "Review critical financial crime alerts",
                "Complete missing evidence for shell company and insider risk packages",
                "Monitor payments degradation and digital asset withdrawal pause",
                "Review application-to-cloud infrastructure security chain risk",
                "Preserve audit trail and reviewer rationale",
                "Prepare escalation-ready evidence packages",
            ],
        )

    def list_action_queue(self) -> list[RiskActionItem]:
        return [
            RiskActionItem(
                action_id="RO-ACTION-001",
                title="Escalate employee-linked account activity",
                source_module="financial_crime",
                source_id="FCA-2026-001",
                priority="urgent",
                status="escalated",
                risk_type="Insider risk",
                summary=(
                    "Employee-linked account activity has critical indicators "
                    "and must remain escalated until independent review is complete."
                ),
                required_action=(
                    "Assign independent reviewer and preserve evidence before closing."
                ),
                missing_evidence=[
                    "Source of funds evidence",
                    "Reviewer conflict-of-interest check",
                ],
                related_links=[
                    self._link("Open financial crime monitoring", "/bank-staff/financial-crime-monitoring", "FCA-2026-001"),
                    self._link("Prepare evidence package", "/bank-staff/evidence-packages", "EP-2026-001"),
                ],
                created_at="2026-06-14T08:20:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-002",
                title="Complete shell company evidence package",
                source_module="evidence_packages",
                source_id="EP-2026-002",
                priority="urgent",
                status="blocked",
                risk_type="Shell company indicator",
                summary=(
                    "The shell company indicator package is blocked because "
                    "required ownership and funds evidence is missing."
                ),
                required_action=(
                    "Request company documentation and keep package incomplete "
                    "until evidence is attached."
                ),
                missing_evidence=[
                    "Beneficial ownership evidence",
                    "Source of funds evidence",
                    "Business rationale for transaction volume",
                ],
                related_links=[
                    self._link("Open evidence packages", "/bank-staff/evidence-packages", "EP-2026-002"),
                    self._link("Open compliance review", "/compliance-review", "CASE-FC-2026-002"),
                ],
                created_at="2026-06-14T08:45:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-003",
                title="Review crypto off-ramp pause",
                source_module="operational_resilience",
                source_id="OR-2026-003",
                priority="high",
                status="in_progress",
                risk_type="Crypto off-ramp",
                summary=(
                    "External digital asset movement is paused while operational "
                    "and compliance reviews remain open."
                ),
                required_action=(
                    "Keep external withdrawal paused until operational and "
                    "compliance review close."
                ),
                missing_evidence=[
                    "Destination ownership confirmation",
                    "Reviewer decision rationale",
                ],
                related_links=[
                    self._link("Open operational resilience", "/bank-staff/operational-resilience", "OR-2026-003"),
                    self._link("Open compliance intelligence", "/bank-staff/compliance-intelligence", "FCA-2026-004"),
                ],
                created_at="2026-06-14T10:40:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-004",
                title="Monitor payments processing degradation",
                source_module="operational_resilience",
                source_id="OR-2026-001",
                priority="high",
                status="in_progress",
                risk_type="Operational resilience",
                summary=(
                    "Payments processing remains degraded with restricted "
                    "operations active for sensitive transfers."
                ),
                required_action=(
                    "Maintain restricted payments mode and monitor dependency recovery."
                ),
                missing_evidence=[],
                related_links=[
                    self._link("Open operational resilience", "/bank-staff/operational-resilience", "OR-2026-001"),
                    self._link("Open reports", "/reports", "audit-trail"),
                ],
                created_at="2026-06-14T08:10:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-005",
                title="Prepare foreign transfer package for review",
                source_module="evidence_packages",
                source_id="EP-2026-004",
                priority="medium",
                status="ready",
                risk_type="Foreign transfer risk",
                summary=(
                    "Foreign transfer evidence package is ready and has no "
                    "current readiness blockers."
                ),
                required_action="Package is ready for review or prototype export.",
                missing_evidence=[],
                related_links=[
                    self._link("Open evidence packages", "/bank-staff/evidence-packages", "EP-2026-004"),
                    self._link("Open reports", "/reports", "EP-2026-004"),
                ],
                created_at="2026-06-14T09:35:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-006",
                title="Explain structured deposits alert",
                source_module="compliance_intelligence",
                source_id="FCA-2026-003",
                priority="medium",
                status="new",
                risk_type="Mule account pattern",
                summary=(
                    "Structured deposit activity needs reviewer explanation "
                    "and supporting evidence before case preparation."
                ),
                required_action=(
                    "Generate reviewer explanation and prepare case if account "
                    "links remain unclear."
                ),
                missing_evidence=[
                    "Originator relationship evidence",
                    "Destination purpose documentation",
                ],
                related_links=[
                    self._link("Open compliance intelligence", "/bank-staff/compliance-intelligence", "FCA-2026-003"),
                    self._link("Open financial crime monitoring", "/bank-staff/financial-crime-monitoring", "FCA-2026-003"),
                ],
                created_at="2026-06-14T11:05:00+03:00",
            ),
            RiskActionItem(
                action_id="RO-ACTION-007",
                title="Review application-to-cloud chain reaction risk",
                source_module="infrastructure_security",
                source_id="INFRASEC-2026-007",
                priority="urgent",
                status="escalated",
                risk_type="Cross-layer infrastructure security",
                summary=(
                    "Multiple simulated control weaknesses could allow an "
                    "application issue to move into Kubernetes, IAM, secrets, "
                    "and sensitive data access."
                ),
                required_action=(
                    "Review the Infrastructure Security Control Center result, "
                    "preserve audit evidence, and confirm hardening actions."
                ),
                missing_evidence=[
                    "Infrastructure control owner confirmation",
                    "Kubernetes RBAC hardening record",
                    "Cloud IAM scope review",
                ],
                related_links=[
                    self._link(
                        "Open infrastructure security",
                        "/bank-staff/infrastructure-security",
                        "INFRASEC-2026-007",
                    ),
                    self._link(
                        "Open evidence packages",
                        "/bank-staff/evidence-packages",
                        "AUD-INFRA-CHAIN-REACTION",
                    ),
                    self._link(
                        "Open infrastructure review case",
                        "/compliance-review",
                        "CASE-INFRA-CHAIN-REACTION",
                    ),
                ],
                created_at="2026-06-14T11:58:00+03:00",
            ),
        ]

    def list_unified_timeline(self) -> list[UnifiedTimelineEvent]:
        return [
            self._event(
                "RO-TL-001",
                "2026-06-14T08:20:00+03:00",
                "financial_crime",
                "alert_created",
                "critical",
                "Financial crime alert created",
                "Employee-linked account activity alert entered the monitoring queue.",
                "FCA-2026-001",
                "Keep alert escalated and assign independent reviewer.",
            ),
            self._event(
                "RO-TL-002",
                "2026-06-14T08:45:00+03:00",
                "evidence_packages",
                "readiness_calculated",
                "critical",
                "Evidence package readiness calculated",
                "Shell company evidence package remains incomplete with required evidence gaps.",
                "EP-2026-002",
                "Request company documentation and source of funds evidence.",
            ),
            self._event(
                "RO-TL-003",
                "2026-06-14T09:10:00+03:00",
                "compliance_intelligence",
                "explanation_generated",
                "high",
                "Compliance explanation generated",
                "Compliance intelligence prepared reviewer reasoning for a high-risk off-ramp review.",
                "FCA-2026-004",
                "Attach reviewer rationale before movement is resumed.",
            ),
            self._event(
                "RO-TL-004",
                "2026-06-14T10:40:00+03:00",
                "operational_resilience",
                "incident_opened",
                "high",
                "Operational incident opened",
                "Digital assets external withdrawal pause was opened as an operational resilience incident.",
                "OR-2026-003",
                "Keep external withdrawals paused pending operational review.",
            ),
            self._event(
                "RO-TL-005",
                "2026-06-14T10:41:00+03:00",
                "operational_resilience",
                "fallback_activated",
                "high",
                "Fallback mode activated",
                "Digital assets withdrawal pause fallback mode was activated.",
                "OR-2026-003",
                "Maintain portfolio viewing and reporting while movement remains paused.",
            ),
            self._event(
                "RO-TL-006",
                "2026-06-14T10:42:00+03:00",
                "compliance_review",
                "sensitive_operations_paused",
                "critical",
                "Sensitive operations paused",
                "External wallet withdrawals, off-ramp execution, and high-risk transfers remain paused.",
                "RO-ACTION-003",
                "Do not resume sensitive operations until review conditions are met.",
            ),
            self._event(
                "RO-TL-007",
                "2026-06-14T10:43:00+03:00",
                "reports",
                "audit_trail_preserved",
                "medium",
                "Audit trail preserved",
                "Risk operations timeline, control activations, and reviewer actions were preserved.",
                "audit-trail",
                "Continue preserving reviewer rationale and evidence outputs.",
            ),
            self._event(
                "RO-TL-008",
                "2026-06-14T11:58:00+03:00",
                "infrastructure_security",
                "review_case_linked",
                "critical",
                "Infrastructure review case linked",
                "CASE-INFRA-CHAIN-REACTION is related to the infrastructure security chain reaction escalation.",
                "CASE-INFRA-CHAIN-REACTION",
                "Review evidence package EP-FROM-AUD-INFRA-CHAIN-REACTION and preserve cross-layer traceability.",
            ),
        ]

    def list_escalation_summary(self) -> list[EscalationSummary]:
        return [
            EscalationSummary(
                summary_id="RO-ESC-001",
                title="Critical financial crime escalations",
                severity="critical",
                escalation_type="financial_crime",
                open_items=2,
                blocked_items=1,
                ready_items=0,
                summary=(
                    "Critical insider risk and shell company indicators require "
                    "reviewer attention and evidence preservation."
                ),
                recommended_action=(
                    "Assign independent review and keep critical cases escalated."
                ),
            ),
            EscalationSummary(
                summary_id="RO-ESC-002",
                title="Evidence blockers",
                severity="critical",
                escalation_type="evidence_gap",
                open_items=2,
                blocked_items=2,
                ready_items=0,
                summary=(
                    "Required ownership, funds, and reviewer rationale evidence "
                    "is still missing from blocked packages."
                ),
                recommended_action=(
                    "Collect required documents before closing packages or resuming movement."
                ),
            ),
            EscalationSummary(
                summary_id="RO-ESC-003",
                title="Operational resilience incidents",
                severity="high",
                escalation_type="operational_resilience",
                open_items=3,
                blocked_items=0,
                ready_items=1,
                summary=(
                    "Payments degradation and digital assets withdrawal pause "
                    "remain active with restricted operations."
                ),
                recommended_action=(
                    "Maintain fallback modes and monitor dependency recovery."
                ),
            ),
            EscalationSummary(
                summary_id="RO-ESC-004",
                title="Review-ready items",
                severity="medium",
                escalation_type="compliance_review",
                open_items=1,
                blocked_items=0,
                ready_items=1,
                summary=(
                    "Foreign transfer evidence package is ready for review or "
                    "prototype export."
                ),
                recommended_action="Route ready item to reviewer workflow.",
            ),
            EscalationSummary(
                summary_id="RO-ESC-005",
                title="Infrastructure security escalation",
                severity="critical",
                escalation_type="infrastructure_security",
                open_items=1,
                blocked_items=0,
                ready_items=1,
                summary=(
                    "CASE-INFRA-CHAIN-REACTION is linked to the critical "
                    "application-to-cloud evidence package and audit trail."
                ),
                recommended_action=(
                    "Review infrastructure controls, evidence package, and "
                    "correlation ID before closure."
                ),
            ),
        ]

    def create_review_case(
        self,
        *,
        action_id: str,
        reviewer_id: str,
        priority: str,
    ) -> RiskOperationsReviewCaseResponse | None:
        action = self._find_action(action_id)
        if action is None:
            return None

        case_title = REVIEW_CASE_TITLES[action.action_id]
        recommended_next_action = (
            "Complete missing evidence before reviewer decision."
            if action.missing_evidence
            else "Route ready item to reviewer workflow."
        )
        case_summary = (
            f"{action.summary} Required action: {action.required_action}"
        )
        review_case = review_case_service.create_risk_operations_case(
            title=case_title,
            summary=action.summary,
            required_action=action.required_action,
            missing_evidence=action.missing_evidence,
            source_action_id=action.action_id,
            source_id=action.source_id,
            reviewer_id=reviewer_id,
            priority=priority,
            risk_type=action.risk_type,
        )
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=f"AUD-RISK-{action.action_id}",
            actor_id=reviewer_id,
            actor_type="staff",
            source_module="risk_operations",
            action="prepare_review_case",
            object_type="risk_action",
            object_id=action.action_id,
            decision="review_case_prepared",
            severity=priority,
            summary="Risk Operations action prepared a review case.",
            evidence_reference=action.source_id,
            review_case_id=review_case.case_id,
            correlation_id=f"CORR-RISK-{action.action_id}",
            metadata={
                "required_action": action.required_action,
                "missing_evidence": action.missing_evidence,
            },
        )
        review_case_service.persist_case_trace(
            review_case,
            source_module="risk_operations",
            source_id=action.source_id,
            source_action_id=action.action_id,
            reviewer_id=reviewer_id,
            recommended_next_action=recommended_next_action,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id,
            metadata={
                "risk_type": action.risk_type,
                "required_action": action.required_action,
                "missing_evidence": action.missing_evidence,
            },
        )

        return RiskOperationsReviewCaseResponse(
            status="created",
            review_case_id=review_case.case_id,
            source_action_id=action.action_id,
            case_title=case_title,
            case_summary=case_summary,
            recommended_next_action=recommended_next_action,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            user_message="Review case prepared from risk operations action.",
            required_action=action.required_action,
            missing_evidence=action.missing_evidence,
        )

    def _find_action(self, action_id: str) -> RiskActionItem | None:
        return next(
            (
                action
                for action in self.list_action_queue()
                if action.action_id == action_id
            ),
            None,
        )

    def _metric(
        self,
        metric_id: str,
        label: str,
        value: str,
        status: str,
        description: str,
        source_module: str,
    ) -> RiskOperationsMetric:
        return RiskOperationsMetric(
            metric_id=metric_id,
            label=label,
            value=value,
            status=status,
            description=description,
            source_module=source_module,
        )

    def _link(
        self,
        label: str,
        route: str,
        entity_id: str | None = None,
    ) -> RiskOperationsLink:
        return RiskOperationsLink(label=label, route=route, entity_id=entity_id)

    def _event(
        self,
        event_id: str,
        timestamp: str,
        source_module: str,
        event_type: str,
        severity: str,
        title: str,
        description: str,
        related_entity_id: str,
        recommended_action: str,
    ) -> UnifiedTimelineEvent:
        return UnifiedTimelineEvent(
            event_id=event_id,
            timestamp=timestamp,
            source_module=source_module,
            event_type=event_type,
            severity=severity,
            title=title,
            description=description,
            related_entity_id=related_entity_id,
            recommended_action=recommended_action,
        )


risk_operations_service = RiskOperationsService()
