from app.schemas.operational_resilience import (
    DependencyStatus,
    EvaluateResilienceScenarioResponse,
    FallbackMode,
    IncidentTimelineEvent,
    ResilienceControl,
    ResilienceIncident,
    ServiceHealthStatus,
)
from app.services.audit_service import audit_service


def _audit_token(value: str) -> str:
    return (
        value.strip()
        .upper()
        .replace("-", "_")
        .replace(" ", "_")
    )


class OperationalResilienceService:
    """Provides deterministic operational resilience demo data."""

    def list_service_health(self) -> list[ServiceHealthStatus]:
        return [
            ServiceHealthStatus(
                service_id="svc-auth",
                name="eBanking authentication",
                category="authentication",
                status="degraded",
                availability_percent=96.8,
                customer_impact="medium",
                fallback_available=True,
                current_mode="degraded",
                recommended_action=(
                    "Enable additional monitoring and keep sensitive actions "
                    "behind strong authentication."
                ),
            ),
            ServiceHealthStatus(
                service_id="svc-payments",
                name="Payments processing",
                category="payments",
                status="degraded",
                availability_percent=94.2,
                customer_impact="high",
                fallback_available=True,
                current_mode="degraded",
                recommended_action=(
                    "Pause high-risk outgoing transfers and keep balance "
                    "viewing available."
                ),
            ),
            ServiceHealthStatus(
                service_id="svc-digital-assets",
                name="Digital assets custody operations",
                category="digital_assets",
                status="paused",
                availability_percent=100.0,
                customer_impact="medium",
                fallback_available=True,
                current_mode="read_only",
                recommended_action=(
                    "Keep portfolio view available but pause external "
                    "withdrawals until review."
                ),
            ),
            ServiceHealthStatus(
                service_id="svc-reporting",
                name="Reporting and audit trail",
                category="reporting",
                status="healthy",
                availability_percent=99.9,
                customer_impact="none",
                fallback_available=True,
                current_mode="normal",
                recommended_action="Continue audit evidence recording.",
            ),
            ServiceHealthStatus(
                service_id="svc-staff-operations",
                name="Staff operations workspace",
                category="staff_operations",
                status="healthy",
                availability_percent=99.5,
                customer_impact="none",
                fallback_available=True,
                current_mode="normal",
                recommended_action=(
                    "Continue incident triage and reviewer workflows."
                ),
            ),
        ]

    def list_dependencies(self) -> list[DependencyStatus]:
        return [
            DependencyStatus(
                dependency_id="dep-core-banking",
                name="Core banking dependency",
                dependency_type="internal",
                status="healthy",
                affected_services=["Accounts", "Payments processing"],
                risk_summary=(
                    "Core account records remain available for viewing and "
                    "staff review."
                ),
            ),
            DependencyStatus(
                dependency_id="dep-payment-rail",
                name="Payment rail connector",
                dependency_type="payment_rail",
                status="degraded",
                affected_services=["Payments processing"],
                risk_summary=(
                    "Outgoing transfer confirmation is slower than the "
                    "prototype continuity threshold."
                ),
            ),
            DependencyStatus(
                dependency_id="dep-auth-provider",
                name="Authentication provider",
                dependency_type="authentication",
                status="degraded",
                affected_services=["eBanking authentication", "Customer access layer"],
                risk_summary=(
                    "Strong authentication remains available with elevated "
                    "monitoring for sensitive actions."
                ),
            ),
            DependencyStatus(
                dependency_id="dep-digital-assets",
                name="External digital asset platform connector",
                dependency_type="custody",
                status="unknown",
                affected_services=["Digital assets custody operations"],
                risk_summary=(
                    "External movement is paused while read-only custody "
                    "records remain available."
                ),
            ),
            DependencyStatus(
                dependency_id="dep-audit-storage",
                name="Audit evidence storage",
                dependency_type="reporting",
                status="healthy",
                affected_services=["Reporting and audit trail", "Staff operations workspace"],
                risk_summary="Evidence preservation and audit trail capture are active.",
            ),
            DependencyStatus(
                dependency_id="dep-notifications",
                name="Customer notification channel",
                dependency_type="external",
                status="healthy",
                affected_services=["Customer access layer", "Payments processing"],
                risk_summary=(
                    "Customer communication path is available for service "
                    "status messaging."
                ),
            ),
        ]

    def list_fallback_modes(self) -> list[FallbackMode]:
        return [
            FallbackMode(
                fallback_id="fb-read-only",
                title="Read-only customer mode",
                status="available",
                description=(
                    "Customers can view balances, account history, reports, "
                    "and digital asset portfolio records."
                ),
                allowed_operations=["account viewing", "reports viewing", "portfolio view"],
                paused_operations=["credential changes", "external transfers"],
            ),
            FallbackMode(
                fallback_id="fb-payments-restricted",
                title="Payments restricted mode",
                status="active",
                description=(
                    "Payment visibility remains available while higher-risk "
                    "payment execution is restricted."
                ),
                allowed_operations=["balance viewing", "account history", "low-risk internal review"],
                paused_operations=["high-risk outgoing transfers", "large external transfers"],
                activation_reason="Payment rail connector degradation.",
            ),
            FallbackMode(
                fallback_id="fb-digital-assets-pause",
                title="Digital assets withdrawal pause",
                status="active",
                description=(
                    "Custody records stay available while external digital "
                    "asset movement is paused."
                ),
                allowed_operations=["portfolio view", "reporting", "compliance review"],
                paused_operations=["external wallet withdrawals", "off-ramp execution"],
                activation_reason="Operational review of external connector status.",
            ),
            FallbackMode(
                fallback_id="fb-manual-review",
                title="Manual review queue mode",
                status="available",
                description=(
                    "Sensitive operations are routed to staff review before "
                    "the prototype records a simulated decision."
                ),
                allowed_operations=["manual review", "audit evidence recording"],
                paused_operations=["automatic sensitive action approval"],
            ),
            FallbackMode(
                fallback_id="fb-staff-command",
                title="Staff incident command mode",
                status="available",
                description=(
                    "Operations staff coordinate triage, evidence capture, "
                    "dependency review, and customer impact tracking."
                ),
                allowed_operations=["staff incident review", "audit trail recording"],
                paused_operations=["new sensitive customer actions", "external transfers"],
            ),
        ]

    def list_controls(self) -> list[ResilienceControl]:
        return [
            self._control(
                "orc-payment-throttle",
                "Payment transfer throttling",
                "Payments continuity",
                "Reduces payment execution volume while dependency status is reviewed.",
                True,
                ["payment_throttle_event", "transfer_restriction_audit"],
            ),
            self._control(
                "orc-high-risk-pause",
                "High-risk transfer pause",
                "Customer protection",
                "Pauses large or higher-risk outgoing transfers during degraded service.",
                True,
                ["paused_operation_record", "review_queue_entry"],
            ),
            self._control(
                "orc-auth-monitoring",
                "Strong authentication monitoring",
                "Authentication continuity",
                "Adds monitoring for authentication retries and sensitive action attempts.",
                True,
                ["authentication_monitoring_event"],
            ),
            self._control(
                "orc-sensitive-lock",
                "Sensitive action lock",
                "Access protection",
                "Keeps credential changes and sensitive customer actions paused.",
                True,
                ["sensitive_action_lock_record"],
            ),
            self._control(
                "orc-withdrawal-pause",
                "External withdrawal pause",
                "Digital assets custody",
                "Pauses external wallet withdrawals while records remain viewable.",
                True,
                ["withdrawal_pause_record", "custody_review_evidence"],
            ),
            self._control(
                "orc-evidence-preservation",
                "Audit event preservation",
                "Audit evidence",
                "Preserves timeline, decision, dependency, and control activation records.",
                True,
                ["incident_timeline", "control_activation_log"],
            ),
            self._control(
                "orc-traffic-shaping",
                "Traffic shaping",
                "Access continuity",
                "Limits abnormal access patterns while preserving staff command access.",
                True,
                ["traffic_shaping_record", "edge_monitoring_event"],
            ),
            self._control(
                "orc-notification-readiness",
                "Customer notification readiness",
                "Customer impact",
                "Prepares clear customer status messaging for service degradation.",
                False,
                ["customer_notification_draft"],
            ),
        ]

    def list_incidents(self) -> list[ResilienceIncident]:
        return [
            ResilienceIncident(
                incident_id="OR-2026-001",
                title="Payments processing degradation",
                affected_service="Payments processing",
                severity="high",
                status="investigating",
                failure_type="dependency_failure",
                customer_impact="high",
                summary=(
                    "Payment rail connector degradation is affecting payment "
                    "execution while account visibility remains available."
                ),
                controls_activated=[
                    "Payment transfer throttling",
                    "High-risk transfer pause",
                    "Audit event preservation",
                ],
                fallback_mode="Payments restricted mode",
                paused_operations=["high-risk outgoing transfers", "large external transfers"],
                available_operations=["balance viewing", "account history", "low-risk internal review"],
                recommended_action=(
                    "Keep payment viewing available, pause sensitive transfers, "
                    "and escalate dependency review."
                ),
                audit_evidence=[
                    "payment_throttle_event",
                    "transfer_restriction_audit",
                    "dependency_status_snapshot",
                ],
                timeline=self._timeline("001", "payments", "2026-06-14T08:10:00+03:00"),
                created_at="2026-06-14T08:10:00+03:00",
            ),
            ResilienceIncident(
                incident_id="OR-2026-002",
                title="eBanking authentication degradation",
                affected_service="eBanking authentication",
                severity="medium",
                status="mitigated",
                failure_type="service_degradation",
                customer_impact="medium",
                summary=(
                    "Strong authentication is slower than normal, so sensitive "
                    "actions remain locked while read-only access continues."
                ),
                controls_activated=[
                    "Strong authentication monitoring",
                    "Sensitive action lock",
                    "Customer session review",
                ],
                fallback_mode="Read-only customer mode",
                paused_operations=["digital asset withdrawals", "credential changes"],
                available_operations=["account viewing", "reports viewing"],
                recommended_action=(
                    "Maintain read-only access while authentication stability is confirmed."
                ),
                audit_evidence=[
                    "authentication_monitoring_event",
                    "sensitive_action_lock_record",
                    "customer_session_review",
                ],
                timeline=self._timeline("002", "authentication", "2026-06-14T09:25:00+03:00"),
                created_at="2026-06-14T09:25:00+03:00",
            ),
            ResilienceIncident(
                incident_id="OR-2026-003",
                title="Digital assets external withdrawal pause",
                affected_service="Digital assets custody operations",
                severity="high",
                status="open",
                failure_type="fallback_activation",
                customer_impact="medium",
                summary=(
                    "External withdrawal and off-ramp execution are paused "
                    "while custody records, portfolio viewing, reporting, and "
                    "review workflows remain available."
                ),
                controls_activated=[
                    "External withdrawal pause",
                    "Compliance review queue",
                    "Evidence package generation",
                ],
                fallback_mode="Digital assets withdrawal pause",
                paused_operations=["external wallet withdrawals", "off-ramp execution"],
                available_operations=["portfolio view", "reporting", "compliance review"],
                recommended_action=(
                    "Keep custody records available but pause external movement "
                    "until operational review closes."
                ),
                audit_evidence=[
                    "withdrawal_pause_record",
                    "custody_review_evidence",
                    "evidence_package_reference",
                ],
                timeline=self._timeline("003", "digital_assets", "2026-06-14T10:40:00+03:00"),
                created_at="2026-06-14T10:40:00+03:00",
            ),
            ResilienceIncident(
                incident_id="OR-2026-004",
                title="DDoS-like traffic spike at edge layer",
                affected_service="Customer access layer",
                severity="critical",
                status="investigating",
                failure_type="traffic_spike",
                customer_impact="severe",
                summary=(
                    "Abnormal access traffic is affecting customer entry points. "
                    "Staff command access and evidence recording remain available."
                ),
                controls_activated=[
                    "Traffic shaping",
                    "Rate limiting",
                    "Incident audit trail",
                    "Staff command mode",
                ],
                fallback_mode="Staff incident command mode",
                paused_operations=["new sensitive customer actions", "external transfers"],
                available_operations=["staff incident review", "audit trail recording"],
                recommended_action=(
                    "Escalate incident, preserve logs, keep critical operations "
                    "in restricted mode."
                ),
                audit_evidence=[
                    "traffic_shaping_record",
                    "edge_monitoring_event",
                    "incident_command_log",
                ],
                timeline=self._timeline("004", "access_layer", "2026-06-14T11:15:00+03:00"),
                created_at="2026-06-14T11:15:00+03:00",
            ),
        ]

    def get_incident(self, incident_id: str) -> ResilienceIncident | None:
        return next(
            (incident for incident in self.list_incidents() if incident.incident_id == incident_id),
            None,
        )

    def evaluate_scenario(
        self,
        scenario_id: str,
        affected_service: str,
        dependency_status: str,
        customer_impact: str,
    ) -> EvaluateResilienceScenarioResponse:
        normalized_service = affected_service.lower()
        normalized_dependency = dependency_status.lower()
        normalized_impact = customer_impact.lower()

        score = 15
        controls = ["Audit event preservation"]
        available_operations = ["staff incident review", "audit trail recording"]
        paused_operations: list[str] = []

        if normalized_service in {"payments", "authentication", "digital_assets"}:
            score += 25
        elif normalized_service in {"core_banking", "staff_operations"}:
            score += 15
        elif normalized_service == "reporting":
            score += 5

        if normalized_dependency == "outage":
            score += 35
        elif normalized_dependency == "degraded":
            score += 20
        elif normalized_dependency == "unknown":
            score += 15

        if normalized_impact == "severe":
            score += 35
        elif normalized_impact == "high":
            score += 25
        elif normalized_impact == "medium":
            score += 15
        elif normalized_impact == "low":
            score += 5

        if normalized_service == "payments":
            controls.extend(["Payment transfer throttling", "High-risk transfer pause"])
            available_operations.extend(["balance viewing", "account history"])
            paused_operations.extend(["high-risk outgoing transfers", "large external transfers"])
        elif normalized_service == "authentication":
            controls.extend(["Strong authentication monitoring", "Sensitive action lock"])
            available_operations.extend(["account viewing", "reports viewing"])
            paused_operations.extend(["credential changes", "new sensitive customer actions"])
        elif normalized_service == "digital_assets":
            controls.extend(["External withdrawal pause", "Compliance review queue"])
            available_operations.extend(["portfolio view", "reporting", "compliance review"])
            paused_operations.extend(["external wallet withdrawals", "off-ramp execution"])
        else:
            controls.append("Staff command mode")
            available_operations.append("dependency review")
            if normalized_impact in {"high", "severe"}:
                paused_operations.append("new sensitive customer actions")

        score = min(score, 100)
        decision = self._decision_for_score(score)
        severity = self._severity_for_score(score)
        recommended_action = self._recommended_action(decision)
        if scenario_id == "payment_dependency_failure":
            audit_event_id = "AUD-OPS-PAYMENTS-DEGRADED"
            correlation_id = "CORR-OPS-PAYMENTS-DEGRADED"
        else:
            audit_event_id = f"AUD-OPS-{_audit_token(scenario_id)}"
            correlation_id = f"CORR-OPS-{_audit_token(scenario_id)}"

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="resilience-engine",
            actor_type="service",
            source_module="operational_resilience",
            action="evaluate_scenario",
            object_type="resilience_scenario",
            object_id=scenario_id,
            decision=decision,
            severity=severity,
            risk_score=score,
            summary=(
                "Operational resilience scenario evaluation and control activation."
            ),
            correlation_id=correlation_id,
            metadata={
                "affected_service": affected_service,
                "dependency_status": dependency_status,
                "customer_impact": customer_impact,
                "controls_activated": controls,
                "paused_operations": paused_operations,
            },
        )

        return EvaluateResilienceScenarioResponse(
            resilience_score=score,
            severity=severity,
            decision=decision,
            controls_activated=controls,
            available_operations=available_operations,
            paused_operations=paused_operations,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            recommended_action=recommended_action,
            explanation=(
                f"Scenario {scenario_id} scored {score}/100 because service "
                f"sensitivity, dependency status '{dependency_status}', and "
                f"customer impact '{customer_impact}' were evaluated using "
                "deterministic prototype rules."
            ),
        )

    def _control(
        self,
        control_id: str,
        title: str,
        category: str,
        description: str,
        activated: bool,
        evidence_outputs: list[str],
    ) -> ResilienceControl:
        return ResilienceControl(
            control_id=control_id,
            title=title,
            category=category,
            description=description,
            activated=activated,
            evidence_outputs=evidence_outputs,
        )

    def _timeline(
        self,
        incident_suffix: str,
        source_module: str,
        opened_at: str,
    ) -> list[IncidentTimelineEvent]:
        return [
            IncidentTimelineEvent(
                event_id=f"ORE-{incident_suffix}-01",
                timestamp=opened_at,
                event_type="incident_opened",
                title="Incident opened",
                description="Operational resilience incident record was created.",
                source_module=source_module,
            ),
            IncidentTimelineEvent(
                event_id=f"ORE-{incident_suffix}-02",
                timestamp=opened_at.replace(":00+03:00", ":30+03:00"),
                event_type="controls_activated",
                title="Controls activated",
                description="Continuity controls and audit evidence capture were activated.",
                source_module="operational_resilience",
            ),
            IncidentTimelineEvent(
                event_id=f"ORE-{incident_suffix}-03",
                timestamp=opened_at.replace(":00+03:00", ":45+03:00"),
                event_type="fallback_review",
                title="Fallback mode reviewed",
                description="Available and paused operations were reviewed for staff action.",
                source_module="staff_operations",
            ),
        ]

    def _decision_for_score(self, score: int) -> str:
        if score >= 85:
            return "escalate_incident"
        if score >= 70:
            return "activate_fallback"
        if score >= 50:
            return "pause_sensitive_operations"
        if score >= 30:
            return "degraded_mode"
        return "normal_operations"

    def _severity_for_score(self, score: int) -> str:
        if score >= 85:
            return "critical"
        if score >= 65:
            return "high"
        if score >= 35:
            return "medium"
        return "low"

    def _recommended_action(self, decision: str) -> str:
        actions = {
            "normal_operations": "Continue normal operations and monitor evidence outputs.",
            "degraded_mode": "Keep service available with additional monitoring.",
            "pause_sensitive_operations": "Pause sensitive operations and preserve audit evidence.",
            "activate_fallback": "Activate fallback mode and route sensitive actions to review.",
            "escalate_incident": "Escalate incident, activate command mode, and preserve logs.",
        }
        return actions[decision]


operational_resilience_service = OperationalResilienceService()
