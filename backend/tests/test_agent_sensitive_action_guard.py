import json
import unittest

from tests.helpers import request_json


class AgentSensitiveActionGuardTests(unittest.TestCase):
    def test_lists_rules_and_sensitive_actions(self) -> None:
        rules_status, rules = request_json(
            "GET",
            "/api/agent-sensitive-action-guard/rules",
        )
        actions_status, actions = request_json(
            "GET",
            "/api/agent-sensitive-action-guard/sensitive-actions",
        )

        self.assertEqual(rules_status, 200)
        self.assertEqual(actions_status, 200)
        self.assertTrue(
            any(rule["guard_decision"] == "block_by_agent_status" for rule in rules)
        )
        action_types = {action["sensitive_action_type"] for action in actions}
        self.assertIn("request_sensitive_operation_approval", action_types)
        self.assertIn("attempt_secret_access", action_types)
        self.assertIn("attempt_withdrawal_approval", action_types)

    def test_blocks_secret_access_attempt_without_exposing_secret_values(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "sensitive_action_type": "attempt_secret_access",
                "resource_type": "configuration",
                "resource_id": "demo-secret-reference",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["guard_decision"], "block_secret_access")
        self.assertFalse(response["allowed"])
        self.assertTrue(response["operation_paused"])
        self.assertTrue(response["secret_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            (
                "AUD-AGENT-SENSITIVE-GUARD-COMPLIANCE-ASSISTANT-001-"
                "ATTEMPT-SECRET-ACCESS"
            ),
        )
        response_text = json.dumps(response).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "api key",
            "token",
            "password",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, response_text)

    def test_requires_review_for_risk_agent_sensitive_approval_request(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "sensitive_action_type": "request_sensitive_operation_approval",
                "operation_type": "external_wallet_withdrawal",
                "resource_type": "sensitive_operation",
                "resource_id": "SOP-DEMO-001",
                "amount_eur": 2500,
                "asset": "BTC",
                "destination_type": "external_wallet",
                "destination_id": "wallet-demo",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["guard_decision"], "require_human_review")
        self.assertTrue(response["human_review_required"])
        self.assertTrue(response["operation_paused"])
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["recommended_next_action"],
            "pause_operation_and_route_agent_context_to_human_review",
        )

    def test_allows_review_case_creation_after_human_review_confirmed(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "sensitive_action_type": "create_review_case",
                "permission_id": "create_review_cases",
                "resource_type": "evidence_package",
                "resource_id": "EP-DEMO",
                "human_review_confirmed": True,
                "linked_evidence_package_id": "EP-DEMO",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["guard_decision"], "allow_agent_participation")
        self.assertTrue(response["allowed"])
        self.assertFalse(response["operation_paused"])
        self.assertFalse(response["sensitive_action_blocked"])
        self.assertEqual(response["linked_evidence_package_id"], "EP-DEMO")

    def test_blocks_suspended_agent_by_status(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "sensitive_action_type": "request_custodian_integration_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(response["agent_status"], ["suspended", "revoked"])
        self.assertEqual(response["guard_decision"], "block_by_agent_status")
        self.assertFalse(response["allowed"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertIn(
            f"agent_status_{response['agent_status']}",
            response["blocking_reasons"],
        )

    def test_custodian_api_attempt_sets_guard_ids_and_blocking_flags(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "sensitive_action_type": "attempt_custodian_api_access",
                "linked_revocation_audit_event_id": (
                    "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["audit_event_id"],
            (
                "AUD-AGENT-SENSITIVE-GUARD-CUSTODIAN-INTEGRATION-001-"
                "ATTEMPT-CUSTODIAN-API-ACCESS"
            ),
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        self.assertFalse(response["allowed"])
        self.assertTrue(response["operation_paused"])
        self.assertTrue(response["sensitive_action_blocked"])
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertIn(
            "linked_revocation_audit_event_requires_human_governance_review",
            response["blocking_reasons"],
        )

    def test_blocks_active_review_case_context(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-sensitive-action-guard/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "sensitive_action_type": "create_evidence_package",
                "permission_id": "create_evidence_packages",
                "linked_review_case_id": "CASE-AGENT-ACTION-DEMO-ACTIVE",
                "human_review_confirmed": True,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["guard_decision"], "block_by_review_case_status")
        self.assertTrue(response["operation_paused"])
        self.assertEqual(
            response["linked_review_case_id"],
            "CASE-AGENT-ACTION-DEMO-ACTIVE",
        )

    def test_sensitive_approval_context_pauses_for_agent_review(self) -> None:
        status, response = request_json(
            "POST",
            (
                "/api/agent-sensitive-action-guard/"
                "evaluate-sensitive-approval-context"
            ),
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "customer-demo",
                "amount_eur": 1500,
                "asset": "ETH",
                "destination_type": "external_wallet",
                "destination_id": "wallet-demo",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["sensitive_approval_recommendation"],
            "pause_for_agent_review",
        )
        self.assertTrue(response["operation_paused_by_agent_guard"])
        self.assertTrue(response["operation_paused_until_human_review"])
        self.assertEqual(
            response["agent_guard"]["guard_decision"],
            "require_human_review",
        )


if __name__ == "__main__":
    unittest.main()
