import json
import unittest

from tests.helpers import request_json


class AgentPolicyEngineTests(unittest.TestCase):
    def test_lists_policy_categories(self) -> None:
        status, response = request_json("GET", "/api/agent-policy-engine/policies")

        self.assertEqual(status, 200)
        categories = {policy["policy_category"] for policy in response}
        self.assertIn("identity_policy", categories)
        self.assertIn("passport_policy", categories)
        self.assertIn("permission_policy", categories)
        self.assertIn("sensitive_action_policy", categories)
        self.assertIn("emergency_override_policy", categories)
        self.assertIn("prototype_safety_policy", categories)

    def test_lists_decision_types(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-policy-engine/decision-types",
        )

        self.assertEqual(status, 200)
        decision_types = {decision["decision_type"] for decision in response}
        self.assertIn("policy_allow", decision_types)
        self.assertIn("policy_require_human_review", decision_types)
        self.assertIn("policy_block_secret_access", decision_types)
        self.assertIn("policy_block_custodian_access", decision_types)
        self.assertIn("policy_block_withdrawal_execution", decision_types)
        self.assertIn("policy_block_by_revocation", decision_types)

    def test_evaluate_custodian_api_access_blocks_with_policy_trace(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "policy_context": "agent_sensitive_action_guard",
                "requested_action": "attempt_custodian_api_access",
                "permission_id": "access_custodian_apis",
                "environment": "local",
                "agent_status": "suspended",
                "passport_decision": "passport_status_blocked",
                "permission_decision": "blocked_by_agent_status",
                "sensitive_action_type": "attempt_custodian_api_access",
                "linked_review_case_id": (
                    "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                "linked_review_case_status": "open",
                "linked_revocation_audit_event_id": (
                    "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["policy_decision"],
            [
                "policy_block_custodian_access",
                "policy_block_by_revocation",
                "policy_block_by_status",
            ],
        )
        self.assertFalse(response["allowed"])
        self.assertTrue(response["operation_paused"])
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            (
                "AUD-AGENT-POLICY-CUSTODIAN-INTEGRATION-001-"
                "ATTEMPT-CUSTODIAN-API-ACCESS"
            ),
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        for policy in [
            "identity_policy",
            "passport_policy",
            "permission_policy",
            "sensitive_action_policy",
            "revocation_policy",
        ]:
            with self.subTest(policy=policy):
                self.assertIn(policy, response["applied_policies"])
        self.assertIn("no external api called", response["safety_notice"].lower())

    def test_evaluate_secret_access_with_emergency_override_blocks(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "policy_context": "agent_sensitive_action_guard",
                "requested_action": "attempt_secret_access",
                "permission_id": "access_secrets",
                "environment": "local",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "blocked_secret_access",
                "sensitive_action_type": "attempt_secret_access",
                "emergency_override_requested": True,
                "human_review_confirmed": True,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["policy_decision"],
            ["policy_block_secret_access", "policy_block_emergency_override"],
        )
        self.assertFalse(response["allowed"])
        self.assertTrue(response["secret_access_blocked"])
        self.assertTrue(response["emergency_override_blocked"])
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["risk_level"], "critical")
        self.assertTrue(
            {
                "secrets_access_prohibited",
                "emergency_override_not_allowed",
            }.intersection(response["blocking_reasons"])
        )
        self.assertIn("no secrets stored or exposed", response["safety_notice"].lower())

    def test_evaluate_withdrawal_approval_blocks_execution(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate",
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "policy_context": "sensitive_approval",
                "requested_action": "attempt_withdrawal_approval",
                "permission_id": "approve_withdrawals",
                "environment": "local",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "blocked_sensitive_action",
                "sensitive_action_type": "attempt_withdrawal_approval",
                "amount_eur": 8000,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["policy_decision"],
            ["policy_block_withdrawal_execution", "policy_block_sensitive_action"],
        )
        self.assertFalse(response["allowed"])
        self.assertTrue(response["withdrawal_execution_blocked"])
        self.assertTrue(response["operation_paused"])
        self.assertEqual(response["risk_level"], "critical")
        self.assertIn(
            "no custody, blockchain, or withdrawal execution occurred",
            response["safety_notice"].lower(),
        )

    def test_evaluate_low_risk_metadata_action_allows_with_audit(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "policy_context": "metadata_review",
                "requested_action": "read_metadata",
                "permission_id": "read_audit_events",
                "environment": "local",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "allowed",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["policy_decision"],
            ["policy_allow", "policy_allow_with_audit"],
        )
        self.assertTrue(response["allowed"])
        self.assertFalse(response["operation_paused"])
        self.assertTrue(response["audit_required"])
        self.assertIn(response["risk_level"], ["low", "medium"])

    def test_evaluate_context_derives_suspended_custodian_status(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate-context",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "context_type": "agent_sensitive_action_guard",
                "requested_action": "attempt_custodian_api_access",
                "sensitive_action_type": "attempt_custodian_api_access",
                "permission_id": "access_custodian_apis",
                "environment": "local",
                "linked_revocation_audit_event_id": (
                    "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["allowed"])
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["operation_paused"])
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )

    def test_explain_secret_access_decision_is_audit_safe(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/explain-decision",
            {
                "policy_decision": "policy_block_secret_access",
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "requested_action": "attempt_secret_access",
                "blocking_reasons": ["secrets_access_prohibited"],
                "applied_policies": [
                    "sensitive_action_policy",
                    "prototype_safety_policy",
                ],
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["audit_safe"])
        self.assertTrue(response["no_secret_material_included"])
        self.assertIn("blocked secret access", response["explanation"].lower())
        self.assertIn("no secrets are included", response["safety_notice"].lower())

    def test_unknown_agent_context_does_not_crash_or_expose_secrets(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-policy-engine/evaluate-context",
            {
                "agent_id": "AGENT-UNKNOWN-001",
                "context_type": "metadata_review",
                "requested_action": "read_metadata",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["policy_decision"],
            ["policy_invalid_context", "policy_block_agent"],
        )
        self.assertFalse(response["allowed"])
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


if __name__ == "__main__":
    unittest.main()
