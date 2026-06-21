import json
import unittest

from tests.helpers import request_json


class AgentAbuseDetectionTests(unittest.TestCase):
    def test_lists_supported_signals(self) -> None:
        status, response = request_json("GET", "/api/agent-abuse-detection/signals")

        self.assertEqual(status, 200)
        signals = {item["signal_category"] for item in response}
        self.assertIn("secret_access_attempt", signals)
        self.assertIn("custodian_access_attempt", signals)
        self.assertIn("withdrawal_execution_attempt", signals)
        self.assertIn("emergency_override_abuse", signals)
        self.assertIn("post_suspension_activity", signals)

    def test_lists_supported_patterns(self) -> None:
        status, response = request_json("GET", "/api/agent-abuse-detection/patterns")

        self.assertEqual(status, 200)
        patterns = {item["pattern_id"] for item in response}
        self.assertIn("repeated_denied_permissions", patterns)
        self.assertIn("custodian_access_after_suspension", patterns)
        self.assertIn("withdrawal_approval_attempt", patterns)
        self.assertIn("revoked_agent_activity", patterns)

    def test_evaluate_suspended_custodian_api_attempt(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "detection_context": "agent_policy_engine",
                "agent_status": "suspended",
                "passport_decision": "passport_status_blocked",
                "permission_decision": "blocked_by_agent_status",
                "policy_decision": "policy_block_custodian_access",
                "sensitive_action_type": "attempt_custodian_api_access",
                "requested_action": "attempt_custodian_api_access",
                "revocation_decision": "already_suspended",
                "linked_review_case_id": (
                    "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                "linked_review_case_status": "open",
                "linked_revocation_audit_event_id": (
                    "AUD-AGENT-REVOCATION-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
                "environment": "local",
                "post_suspension_attempt_count": 1,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["abuse_detected"])
        self.assertIn(response["abuse_level"], ["high", "critical"])
        self.assertIn(
            response["abuse_decision"],
            [
                "quarantine_agent_recommended",
                "create_review_case",
                "revoke_agent_recommended",
            ],
        )
        self.assertTrue(
            {
                "custodian_access_attempt",
                "attempt_custodian_api_access",
            }.intersection(response["detected_signals"])
        )
        self.assertTrue(
            {
                "post_suspension_activity",
                "agent_status_suspended",
            }.intersection(response["detected_signals"])
        )
        self.assertTrue(response["custodian_access_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertTrue(response["review_case_required"])
        self.assertTrue(response["evidence_required"])
        self.assertIn(
            response["audit_event_id"],
            [
                (
                    "AUD-AGENT-ABUSE-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                (
                    "AUD-AGENT-ABUSE-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPTED-CUSTODIAN-API-ACCESS"
                ),
            ],
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        self.assertIn("no external api called", response["safety_notice"].lower())

    def test_evaluate_secret_access_with_emergency_override_abuse(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "detection_context": "agent_policy_engine",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "blocked_secret_access",
                "policy_decision": "policy_block_secret_access",
                "sensitive_action_type": "attempt_secret_access",
                "requested_action": "attempt_secret_access",
                "environment": "local",
                "emergency_override_count": 2,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["abuse_detected"])
        self.assertEqual(response["abuse_score"], 100)
        self.assertEqual(response["abuse_level"], "critical")
        self.assertIn(
            response["abuse_decision"],
            ["quarantine_agent_recommended", "revoke_agent_recommended"],
        )
        self.assertTrue(response["secret_access_blocked"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertTrue(
            {
                "secret_access_attempt",
                "attempt_secret_access",
            }.intersection(response["detected_signals"])
        )
        self.assertTrue(
            {
                "emergency_override_abuse",
                "emergency_override_requested",
            }.intersection(response["detected_signals"])
        )
        self.assertIn("no secrets stored or exposed", response["safety_notice"].lower())

    def test_evaluate_withdrawal_approval_attempt(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "detection_context": "sensitive_approval",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "blocked_sensitive_action",
                "policy_decision": "policy_block_withdrawal_execution",
                "sensitive_action_type": "attempt_withdrawal_approval",
                "requested_action": "attempt_withdrawal_approval",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["abuse_detected"])
        self.assertEqual(response["abuse_level"], "critical")
        self.assertIn(
            response["abuse_decision"],
            ["revoke_agent_recommended", "quarantine_agent_recommended"],
        )
        self.assertTrue(response["withdrawal_execution_blocked"])
        self.assertTrue(response["sensitive_actions_blocked"])
        self.assertTrue(response["external_tool_access_blocked"])
        self.assertIn(
            "no custody, blockchain, or withdrawal execution occurred",
            response["safety_notice"].lower(),
        )

    def test_evaluate_repeated_denied_permissions(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "detection_context": "agent_permissions",
                "agent_status": "active",
                "permission_decision": "denied",
                "requested_action": "read_transactions",
                "environment": "local",
                "denied_attempt_count": 5,
                "blocked_policy_count": 3,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["abuse_detected"])
        self.assertIn(response["abuse_level"], ["medium", "high", "critical"])
        self.assertTrue(
            {
                "repeated_denied_permissions",
                "repeated_policy_denials",
            }.intersection(response["detected_signals"])
        )
        self.assertIn(
            response["abuse_decision"],
            [
                "require_human_review",
                "create_review_case",
                "quarantine_agent_recommended",
            ],
        )

    def test_evaluate_low_risk_normal_action(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "detection_context": "metadata_review",
                "agent_status": "active",
                "passport_decision": "passport_valid",
                "permission_decision": "allowed",
                "policy_decision": "policy_allow_with_audit",
                "requested_action": "read_metadata",
                "environment": "local",
                "denied_attempt_count": 0,
                "blocked_policy_count": 0,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["abuse_detected"])
        self.assertIn(response["abuse_decision"], ["no_abuse_detected", "monitor_agent"])
        self.assertIn(response["abuse_level"], ["none", "low"])
        self.assertFalse(response["sensitive_actions_blocked"])

    def test_evaluate_sequence_secret_then_withdrawal(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate-sequence",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
                "events": [
                    {
                        "event_id": (
                            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-"
                            "ATTEMPT-SECRET-ACCESS"
                        ),
                        "event_type": "agent_action",
                        "decision": "blocked_secret_access",
                        "action_type": "attempt_secret_access",
                        "permission_id": "access_secrets",
                        "risk_level": "critical",
                        "blocked": True,
                    },
                    {
                        "event_id": (
                            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-"
                            "ATTEMPT-WITHDRAWAL-APPROVAL"
                        ),
                        "event_type": "agent_action",
                        "decision": "blocked_sensitive_action",
                        "action_type": "attempt_withdrawal_approval",
                        "permission_id": "approve_withdrawals",
                        "risk_level": "critical",
                        "blocked": True,
                    },
                ],
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["abuse_detected"])
        self.assertEqual(response["abuse_level"], "critical")
        self.assertIn(
            "suspicious_secret_then_withdrawal_sequence",
            response["matched_patterns"],
        )
        self.assertEqual(response["critical_event_count"], 2)
        self.assertEqual(response["blocked_event_count"], 2)
        self.assertTrue(response["withdrawal_execution_blocked"])
        self.assertTrue(response["secret_access_blocked"])

    def test_recommend_response_for_critical_abuse(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/recommend-response",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "abuse_decision": "quarantine_agent_recommended",
                "abuse_level": "critical",
                "detected_signals": [
                    "secret_access_attempt",
                    "emergency_override_abuse",
                ],
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["escalation_required"])
        self.assertTrue(response["quarantine_recommended"])
        self.assertIn("preserve_audit_trail", response["recommended_actions"])
        self.assertIn("create_review_case", response["recommended_actions"])
        self.assertTrue(response["audit_safe"])

    def test_unknown_agent_or_empty_context_does_not_crash(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-abuse-detection/evaluate",
            {
                "agent_id": "AGENT-UNKNOWN-001",
                "detection_context": "",
                "requested_action": "",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
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
