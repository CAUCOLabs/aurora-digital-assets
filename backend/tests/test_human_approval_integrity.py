import unittest

from tests.helpers import request_json


class HumanApprovalIntegrityTests(unittest.TestCase):
    def test_rules_describe_human_review_integrity_boundaries(self) -> None:
        status, response = request_json(
            "GET",
            "/api/human-approval-integrity/rules",
        )

        self.assertEqual(status, 200)
        rules = response["rules"]
        self.assertIn("human review is not a trust anchor", rules)
        self.assertIn(
            "no single human can override critical system block",
            rules,
        )
        self.assertIn("dual control required for critical actions", rules)
        self.assertIn("segregation of duties required", rules)

    def test_risk_signals_include_approval_integrity_categories(self) -> None:
        status, response = request_json(
            "GET",
            "/api/human-approval-integrity/risk-signals",
        )

        self.assertEqual(status, 200)
        signals = response["risk_signals"]
        self.assertIn("reviewer_conflict_of_interest", signals)
        self.assertIn("reviewer_single_point_of_failure", signals)
        self.assertIn("approval_after_system_block", signals)
        self.assertIn("emergency_override_abuse", signals)
        self.assertIn("segregation_of_duties_violation", signals)

    def test_evaluate_blocks_reviewer_after_critical_system_block(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/evaluate",
            {
                "reviewer_id": "reviewer-demo",
                "operation_type": "external_wallet_withdrawal",
                "approval_context": "sensitive_operation_review",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 8000,
                "asset": "BTC",
                "destination_type": "external_wallet",
                "destination_id": "new-wallet-demo",
                "environment": "local",
                "critical_system_block_active": True,
                "emergency_override_requested": True,
                "linked_agent_abuse_audit_event_id": (
                    "AUD-AGENT-ABUSE-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                "linked_agent_revocation_audit_event_id": (
                    "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
                "second_reviewer_id": None,
                "second_reviewer_independent": False,
                "sensitive_approvals_last_24h": 12,
                "override_attempts_last_24h": 3,
                "outside_working_hours": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["approval_allowed"])
        self.assertTrue(response["operation_paused"])
        self.assertTrue(response["critical_override_blocked"])
        self.assertTrue(response["emergency_override_blocked"])
        self.assertTrue(response["second_reviewer_required"])
        self.assertTrue(response["escalation_required"])
        self.assertIn(
            response["integrity_decision"],
            [
                "reviewer_integrity_blocks_override",
                "reviewer_integrity_blocks_sensitive_operation",
                "reviewer_integrity_blocks_approval",
            ],
        )
        self.assertTrue(
            {
                "approval_after_system_block",
                "emergency_override_abuse",
            }.intersection(response["detected_signals"])
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-HUMAN-APPROVAL-INTEGRITY-REVIEWER-DEMO-"
            "EXTERNAL-WALLET-WITHDRAWAL",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-HUMAN-APPROVAL-INTEGRITY-REVIEWER-DEMO",
        )
        self.assertIn("no legal accusation", response["safety_notice"])
        self.assertIn("no real approval granted", response["safety_notice"])

    def test_evaluate_blocks_reviewer_approving_own_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/evaluate",
            {
                "reviewer_id": "reviewer-demo",
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "reviewer-demo",
                "actor_type": "staff",
                "amount_eur": 3000,
                "environment": "local",
                "reviewer_is_actor": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["approval_allowed"])
        self.assertFalse(response["segregation_of_duties_satisfied"])
        self.assertTrue(
            {
                "reviewer_approved_own_case",
                "segregation_of_duties_violation",
            }.intersection(response["detected_signals"])
        )
        self.assertIn(
            response["integrity_decision"],
            [
                "reviewer_integrity_blocks_approval",
                "reviewer_integrity_blocks_sensitive_operation",
            ],
        )

    def test_high_value_approval_without_second_reviewer_pauses(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/evaluate",
            {
                "reviewer_id": "reviewer-demo",
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 12000,
                "environment": "local",
                "critical_system_block_active": False,
                "second_reviewer_id": None,
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["second_reviewer_required"])
        self.assertTrue(
            not response["approval_allowed"] or response["operation_paused"]
        )
        self.assertIn(
            response["integrity_decision"],
            [
                "reviewer_integrity_requires_second_reviewer",
                "reviewer_integrity_requires_escalation",
            ],
        )
        self.assertTrue(
            {
                "reviewer_single_point_of_failure",
                "dual_control_missing",
            }.intersection(response["detected_signals"])
        )

    def test_clean_dual_control_can_continue(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/evaluate",
            {
                "reviewer_id": "reviewer-demo",
                "operation_type": "compliance_case_review",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 1000,
                "environment": "local",
                "critical_system_block_active": False,
                "second_reviewer_id": "reviewer-independent-demo",
                "second_reviewer_independent": True,
                "reviewer_has_conflict": False,
                "sensitive_approvals_last_24h": 1,
                "override_attempts_last_24h": 0,
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["integrity_decision"],
            ["reviewer_integrity_clear", "reviewer_integrity_monitor"],
        )
        self.assertTrue(response["approval_allowed"])
        self.assertTrue(
            response["dual_control_satisfied"]
            or not response["second_reviewer_required"]
        )
        self.assertIn(response["integrity_level"], ["clear", "monitor"])

    def test_sensitive_approval_with_critical_block_pauses(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/evaluate-sensitive-approval",
            {
                "reviewer_id": "reviewer-demo",
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 8000,
                "asset": "BTC",
                "destination_type": "external_wallet",
                "destination_id": "new-wallet-demo",
                "critical_system_block_active": True,
                "emergency_override_requested": True,
                "second_reviewer_id": None,
                "second_reviewer_independent": False,
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["sensitive_approval_recommendation"],
            [
                "pause_for_second_reviewer",
                "escalate_to_compliance",
                "block_human_approval",
                "block_sensitive_operation",
            ],
        )
        self.assertTrue(response["operation_paused_by_human_integrity_guard"])
        self.assertTrue(
            response["operation_paused_until_second_reviewer"]
            or response["operation_paused_until_compliance_review"]
        )
        self.assertIn("no real approval granted", response["safety_notice"])

    def test_dual_control_preview_missing_independent_reviewer(self) -> None:
        status, response = request_json(
            "POST",
            "/api/human-approval-integrity/dual-control-preview",
            {
                "primary_reviewer_id": "reviewer-demo",
                "operation_type": "external_wallet_withdrawal",
                "priority": "critical",
                "critical_system_block_active": True,
                "primary_reviewer_has_conflict": False,
                "second_reviewer_id": None,
                "second_reviewer_independent": False,
                "reviewer_is_actor": False,
                "emergency_override_requested": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["dual_control_required"])
        self.assertFalse(response["dual_control_satisfied"])
        self.assertFalse(response["approval_allowed"])
        self.assertTrue(response["operation_paused"])
        self.assertIn(
            response["preview_decision"],
            [
                "dual_control_requires_second_reviewer",
                "dual_control_blocks_approval",
            ],
        )
        self.assertIn("deterministic preview only", response["safety_notice"])


if __name__ == "__main__":
    unittest.main()
