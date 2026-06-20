import json
import unittest

from tests.helpers import request_json


class AgentRevocationTests(unittest.TestCase):
    def test_revocation_reasons_include_agent_governance_triggers(self) -> None:
        status, response = request_json("GET", "/api/agent-revocation/reasons")

        self.assertEqual(status, 200)
        self.assertIn("attempted_secret_access", response)
        self.assertIn("attempted_custodian_api_access", response)
        self.assertIn("attempted_withdrawal_approval", response)
        self.assertIn("review_case_critical", response)

    def test_revocation_actions_include_blocking_and_audit_actions(self) -> None:
        status, response = request_json("GET", "/api/agent-revocation/actions")

        self.assertEqual(status, 200)
        self.assertIn("suspend_agent", response)
        self.assertIn("quarantine_agent", response)
        self.assertIn("revoke_agent", response)
        self.assertIn("block_secret_access", response)
        self.assertIn("preserve_audit_trail", response)

    def test_evaluate_custodian_api_attempt_for_suspended_agent(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-revocation/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "reason": "attempted_custodian_api_access",
                "trigger_source": "agent_action_review_case",
                "trigger_reference_id": (
                    "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["agent_id"], "AGENT-CUSTODIAN-INTEGRATION-001")
        self.assertEqual(response["current_agent_status"], "suspended")
        self.assertIn(
            response["revocation_decision"],
            ["already_suspended", "quarantine_required", "suspension_required"],
        )
        self.assertIn(response["target_agent_status"], ["suspended", "quarantined"])
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-ATTEMPTED-CUSTODIAN-API-ACCESS",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        self.assertEqual(
            response["linked_review_case_id"],
            "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no real identity system was modified", safety_notice)
        self.assertIn("no external api was called", safety_notice)

    def test_evaluate_secret_access_attempt_for_compliance_assistant(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-revocation/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "reason": "attempted_secret_access",
                "trigger_source": "agent_action_audit_event",
                "trigger_reference_id": (
                    "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-"
                    "ATTEMPT-SECRET-ACCESS"
                ),
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["revocation_decision"],
            ["quarantine_required", "revocation_required"],
        )
        self.assertIn(response["target_agent_status"], ["quarantined", "revoked"])
        self.assertTrue(response["secret_access_blocked"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertEqual(
            response["linked_review_case_id"],
            "CASE-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        self.assertIn(
            "no secrets were stored or exposed",
            response["safety_notice"].lower(),
        )

    def test_evaluate_withdrawal_approval_attempt_for_risk_analyst(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-revocation/evaluate",
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "reason": "attempted_withdrawal_approval",
                "trigger_source": "agent_action_review_case",
                "trigger_reference_id": (
                    "CASE-AGENT-ACTION-RISK-ANALYST-001-"
                    "ATTEMPT-WITHDRAWAL-APPROVAL"
                ),
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["revocation_decision"],
            ["revocation_required", "quarantine_required"],
        )
        self.assertIn(response["target_agent_status"], ["revoked", "quarantined"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertIn(
            "no custody, blockchain, or withdrawal execution occurred",
            response["safety_notice"].lower(),
        )

    def test_apply_preview_for_quarantine_does_not_mutate_registry(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-revocation/apply-preview",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "target_action": "quarantine_agent",
                "reason": "attempted_secret_access",
                "trigger_reference_id": (
                    "CASE-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-"
                    "ATTEMPT-SECRET-ACCESS"
                ),
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["preview_decision"],
            ["preview_allowed", "preview_requires_review"],
        )
        self.assertEqual(response["target_agent_status"], "quarantined")
        self.assertFalse(response["state_mutation_performed"])
        self.assertIn("preserve_audit_trail", response["required_controls"])
        safety_notice = response["safety_notice"].lower()
        self.assertIn("deterministic revocation preview", safety_notice)
        self.assertIn("no real identity system was modified", safety_notice)

    def test_get_agent_revocation_status_uses_registry_status(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-revocation/agents/AGENT-CUSTODIAN-INTEGRATION-001/status",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["current_agent_status"], "suspended")
        self.assertTrue(response["revocation_supported"])
        self.assertEqual(response["status_source"], "agent_registry")

    def test_unknown_agent_evaluation_is_graceful(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-revocation/evaluate",
            {
                "agent_id": "AGENT-UNKNOWN-001",
                "reason": "unknown_or_unregistered_agent",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["revocation_decision"], "blocked_unknown_agent")
        response_text = json.dumps(response).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "api key",
            "token",
            "password",
            "credential value",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, response_text)


if __name__ == "__main__":
    unittest.main()
