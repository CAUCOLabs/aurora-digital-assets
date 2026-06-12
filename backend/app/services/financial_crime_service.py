from app.schemas.financial_crime import (
    EvaluateDemoActivityResponse,
    FinancialCrimeAlert,
    MonitoringControl,
    RiskScenario,
)


class FinancialCrimeService:
    """Provides deterministic financial crime monitoring demo data."""

    def list_risk_scenarios(self) -> list[RiskScenario]:
        return [
            RiskScenario(
                scenario_id="employee-linked-activity-mismatch",
                title="Employee-linked account activity mismatch",
                description=(
                    "Detects account activity connected to a staff profile that "
                    "does not align with expected income or declared purpose."
                ),
                risk_indicators=[
                    "Employee-linked account",
                    "External transfers above expected profile",
                    "Enhanced monitoring required",
                ],
            ),
            RiskScenario(
                scenario_id="shell-company-explosive-growth",
                title="Newly created company with explosive transaction growth",
                description=(
                    "Flags a recently created company whose funds movement grows "
                    "faster than expected for the declared business activity."
                ),
                risk_indicators=[
                    "Company age below 30 days",
                    "Rapid transaction volume increase",
                    "Business activity mismatch",
                ],
            ),
            RiskScenario(
                scenario_id="structured-deposits-linked-accounts",
                title="Structured deposits across linked accounts",
                description=(
                    "Identifies repeated smaller deposits across connected "
                    "accounts followed by movement to a common destination."
                ),
                risk_indicators=[
                    "Repeated small deposits",
                    "Multiple originators",
                    "Common destination account",
                ],
            ),
            RiskScenario(
                scenario_id="crypto-off-ramp-external-platform",
                title="Crypto off-ramp to external platform",
                description=(
                    "Reviews transfers from bank accounts to external digital "
                    "asset platforms where source of funds evidence is incomplete."
                ),
                risk_indicators=[
                    "External crypto platform transfer",
                    "Incomplete source of funds",
                    "Manual review required",
                ],
            ),
            RiskScenario(
                scenario_id="foreign-transfer-risk",
                title="Foreign transfer risk",
                description=(
                    "Monitors repeated international transfers where the economic "
                    "justification or beneficiary pattern needs validation."
                ),
                risk_indicators=[
                    "Repeated foreign transfers",
                    "Unclear economic justification",
                    "Beneficiary pattern validation",
                ],
            ),
            RiskScenario(
                scenario_id="network-linked-entities",
                title="Network-linked entities",
                description=(
                    "Finds connections between employees, customers, accounts, "
                    "companies, and wallets that may require enhanced review."
                ),
                risk_indicators=[
                    "Shared counterparties",
                    "Connected accounts or wallets",
                    "Evidence graph required",
                ],
            ),
        ]

    def list_monitoring_controls(self) -> list[MonitoringControl]:
        return [
            MonitoringControl(
                control_id="employee-risk-monitoring",
                title="Employee risk monitoring",
                category="Insider risk",
                description=(
                    "Compares staff-linked activity against expected profiles and "
                    "requires escalation for unexplained anomalies."
                ),
                evidence_outputs=["Staff link evidence", "Activity profile variance"],
            ),
            MonitoringControl(
                control_id="customer-company-kyc",
                title="Customer and company KYC",
                category="Due diligence",
                description=(
                    "Checks customer and company records before digital asset or "
                    "external transfer activity is allowed to progress."
                ),
                evidence_outputs=["KYC status", "Company registration age"],
            ),
            MonitoringControl(
                control_id="source-of-funds-verification",
                title="Source of funds verification",
                category="Funds legitimacy",
                description=(
                    "Requires source of funds evidence when transaction volume or "
                    "destination risk exceeds prototype thresholds."
                ),
                evidence_outputs=["Source of funds status", "Reviewer notes"],
            ),
            MonitoringControl(
                control_id="transaction-pattern-monitoring",
                title="Transaction pattern monitoring",
                category="Transaction monitoring",
                description=(
                    "Detects structuring, rapid movement, and inconsistent funds "
                    "flows across accounts and companies."
                ),
                evidence_outputs=["Triggered rules", "Transaction timeline"],
            ),
            MonitoringControl(
                control_id="crypto-off-ramp-monitoring",
                title="Crypto off-ramp monitoring",
                category="Digital assets",
                description=(
                    "Flags transfers to external digital asset platforms for "
                    "review before money leaves the banking environment."
                ),
                evidence_outputs=["Destination type", "Off-ramp risk rationale"],
            ),
            MonitoringControl(
                control_id="network-risk-detection",
                title="Network risk detection",
                category="Entity network",
                description=(
                    "Identifies linked customers, accounts, companies, wallets, "
                    "and staff references for enhanced investigation."
                ),
                evidence_outputs=["Linked entity graph", "Shared counterparty list"],
            ),
            MonitoringControl(
                control_id="audit-evidence-generation",
                title="Audit evidence generation",
                category="Audit trail",
                description=(
                    "Records triggered controls, reviewer actions, and escalation "
                    "rationale for later inspection."
                ),
                evidence_outputs=["Case record", "Decision rationale"],
            ),
        ]

    def list_demo_alerts(self) -> list[FinancialCrimeAlert]:
        return [
            FinancialCrimeAlert(
                alert_id="FCA-2026-001",
                title="Employee-linked account activity mismatch",
                risk_type="Insider risk",
                severity="critical",
                entity_type="employee",
                entity_name="Staff Member A",
                amount_eur=74500,
                status="escalated",
                triggered_rules=[
                    "Employee account activity exceeds expected income profile",
                    "Multiple external transfers detected",
                    "Staff-linked account requires enhanced monitoring",
                ],
                recommended_action=(
                    "Escalate to financial crime investigation and restrict "
                    "external transfer progression until reviewed."
                ),
                linked_review_case_id="CASE-FC-2026-001",
                evidence_summary=(
                    "Staff-linked account activity exceeds the expected profile "
                    "and includes repeated external transfers."
                ),
                created_at="2026-06-12T08:20:00+03:00",
            ),
            FinancialCrimeAlert(
                alert_id="FCA-2026-002",
                title="New company transaction growth anomaly",
                risk_type="Shell company indicator",
                severity="critical",
                entity_type="company",
                entity_name="Nova IT Services Ltd",
                amount_eur=128900,
                status="under_review",
                triggered_rules=[
                    "Company age below 30 days",
                    "Transaction volume increased rapidly",
                    "Declared business activity inconsistent with funds movement",
                ],
                recommended_action=(
                    "Request enhanced company documentation and source of funds "
                    "evidence before permitting further transfers."
                ),
                linked_review_case_id="CASE-FC-2026-002",
                evidence_summary=(
                    "Recently created company shows rapid incoming and outgoing "
                    "funds movement inconsistent with declared activity."
                ),
                created_at="2026-06-12T09:05:00+03:00",
            ),
            FinancialCrimeAlert(
                alert_id="FCA-2026-003",
                title="Structured deposits across linked accounts",
                risk_type="Mule account pattern",
                severity="high",
                entity_type="account",
                entity_name="Linked Account Cluster 04",
                amount_eur=38400,
                status="new",
                triggered_rules=[
                    "Repeated small deposits",
                    "Multiple originators",
                    "Rapid movement to common destination",
                ],
                recommended_action=(
                    "Open network review case and validate originators, account "
                    "links, and destination purpose."
                ),
                evidence_summary=(
                    "Linked account cluster shows repeated smaller deposits and "
                    "rapid consolidation to one destination."
                ),
                created_at="2026-06-12T10:15:00+03:00",
            ),
            FinancialCrimeAlert(
                alert_id="FCA-2026-004",
                title="Crypto off-ramp risk",
                risk_type="Crypto off-ramp",
                severity="high",
                entity_type="transaction",
                entity_name="External Crypto Platform Transfer",
                amount_eur=56500,
                status="under_review",
                triggered_rules=[
                    "Funds moved from bank account to crypto platform",
                    "Source of funds incomplete",
                    "High-risk pattern requires review",
                ],
                recommended_action=(
                    "Require source of funds evidence and compliance review "
                    "before transfer execution."
                ),
                linked_review_case_id="CASE-FC-2026-004",
                evidence_summary=(
                    "Transfer to an external digital asset platform is above the "
                    "prototype threshold with incomplete funds evidence."
                ),
                created_at="2026-06-12T11:30:00+03:00",
            ),
            FinancialCrimeAlert(
                alert_id="FCA-2026-005",
                title="Foreign transfer risk",
                risk_type="Foreign transfer risk",
                severity="medium",
                entity_type="transaction",
                entity_name="International Transfer Corridor",
                amount_eur=22400,
                status="new",
                triggered_rules=[
                    "Repeated international transfers",
                    "Unclear economic justification",
                    "Beneficiary pattern requires validation",
                ],
                recommended_action=(
                    "Validate beneficiary pattern and economic justification "
                    "before closing the monitoring alert."
                ),
                evidence_summary=(
                    "Repeated international transfers require additional "
                    "economic justification and beneficiary validation."
                ),
                created_at="2026-06-12T12:05:00+03:00",
            ),
        ]

    def evaluate_demo_activity(
        self,
        scenario_id: str,
        amount_eur: float,
        entity_type: str,
    ) -> EvaluateDemoActivityResponse:
        normalized_scenario = scenario_id.strip().lower()
        normalized_entity_type = entity_type.strip().lower()
        score = 15
        triggered_rules: list[str] = ["Demo monitoring baseline applied"]

        if amount_eur > 50000:
            score += 35
            triggered_rules.append("Amount exceeds EUR 50,000 review threshold")
        elif amount_eur >= 10000:
            score += 15
            triggered_rules.append("Amount exceeds EUR 10,000 monitoring threshold")

        if (
            "employee" in normalized_scenario
            or "shell-company" in normalized_scenario
            or normalized_entity_type in {"employee", "company"}
        ):
            score += 35
            triggered_rules.append("Scenario requires enhanced insider or company review")

        if "crypto" in normalized_scenario:
            score += 25
            triggered_rules.append("External digital asset platform risk detected")

        if "foreign" in normalized_scenario:
            score += 20
            triggered_rules.append("Foreign transfer pattern requires validation")

        if "structured" in normalized_scenario or "network" in normalized_scenario:
            score += 20
            triggered_rules.append("Linked entity or structuring indicator detected")

        score = min(score, 100)

        if score >= 80:
            severity = "critical"
            decision = "escalate"
            recommended_action = (
                "Escalate to financial crime review and preserve audit evidence "
                "before any external money movement."
            )
        elif score >= 50:
            severity = "high"
            decision = "review_required"
            recommended_action = (
                "Create a review case and request supporting documentation before "
                "allowing the activity to continue."
            )
        elif score >= 30:
            severity = "medium"
            decision = "review_required"
            recommended_action = (
                "Route to standard monitoring review and retain the generated "
                "evidence summary."
            )
        else:
            severity = "low"
            decision = "allow"
            recommended_action = (
                "Allow in the prototype while recording the monitoring result."
            )

        return EvaluateDemoActivityResponse(
            risk_score=score,
            severity=severity,
            decision=decision,
            triggered_rules=triggered_rules,
            recommended_action=recommended_action,
            explanation=(
                "Deterministic prototype score based on scenario type, entity "
                "type, amount, and whether funds may leave the banking system."
            ),
        )


financial_crime_service = FinancialCrimeService()
