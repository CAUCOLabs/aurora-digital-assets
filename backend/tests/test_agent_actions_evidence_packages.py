import json
import unittest

from tests.helpers import request_json


def generate_evidence(audit_event_id: str) -> tuple[int, dict]:
    return request_json(
        "POST",
        "/api/evidence-packages/generate",
        {
            "source_type": "audit_event",
            "source_id": audit_event_id,
            "package_type": "internal_review",
            "reviewer_id": "reviewer-demo",
        },
    )


class AgentActionsEvidencePackageTests(unittest.TestCase):
    def test_allowed_read_audit_event_generates_agent_action_evidence(self) -> None:
        status, response = generate_evidence(
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(
            package["package_id"],
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
        )
        self.assertEqual(package["source_module"], "agent_actions")
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )
        self.assertIn("agent", package["risk_type"].lower())
        evidence_text = json.dumps(response["evidence_items"]).lower()
        self.assertTrue(
            "agent identity" in evidence_text or "action attempt" in evidence_text
        )
        self.assertIn("no real action was executed", evidence_text)
        self.assertFalse(package["audit_context"]["review_case_id"])

    def test_blocked_secret_access_generates_critical_evidence(self) -> None:
        status, response = generate_evidence(
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(
            package["package_id"],
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        self.assertEqual(package["source_module"], "agent_actions")
        self.assertEqual(package["severity"], "critical")
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )
        self.assertEqual(
            package["audit_context"]["review_case_id"],
            "CASE-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        evidence_text = json.dumps(response["evidence_items"]).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "api key",
            "token",
            "password",
            "credential value",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, evidence_text)
        self.assertIn(
            "confirm_no_secrets_were_exposed",
            package["recommended_next_action"],
        )

    def test_suspended_custodian_api_attempt_generates_evidence(self) -> None:
        status, response = generate_evidence(
            "AUD-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(
            package["package_id"],
            "EP-FROM-AUD-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        self.assertEqual(package["source_module"], "agent_actions")
        self.assertEqual(package["severity"], "critical")
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        self.assertEqual(
            package["audit_context"]["review_case_id"],
            "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        evidence_text = json.dumps(response["evidence_items"]).lower()
        self.assertIn("no external api was called", evidence_text)
        self.assertIn(
            "verify_agent_identity_and_passport",
            package["recommended_next_action"],
        )

    def test_withdrawal_approval_attempt_generates_evidence(self) -> None:
        status, response = generate_evidence(
            "AUD-AGENT-ACTION-RISK-ANALYST-001-ATTEMPT-WITHDRAWAL-APPROVAL",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(package["severity"], "critical")
        self.assertEqual(
            package["audit_context"]["review_case_id"],
            "CASE-AGENT-ACTION-RISK-ANALYST-001-ATTEMPT-WITHDRAWAL-APPROVAL",
        )
        evidence_text = json.dumps(response["evidence_items"]).lower()
        self.assertIn("no custody, blockchain, or withdrawal execution", evidence_text)
        self.assertIn(
            "keep_sensitive_action_blocked",
            package["recommended_next_action"],
        )

    def test_unknown_agent_action_audit_event_is_graceful(self) -> None:
        status, response = generate_evidence(
            "AUD-AGENT-ACTION-UNKNOWN-AGENT-ATTEMPT-SECRET-ACCESS",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(package["source_module"], "agent_actions")
        self.assertEqual(
            package["package_id"],
            "EP-FROM-AUD-AGENT-ACTION-UNKNOWN-AGENT-ATTEMPT-SECRET-ACCESS",
        )
        evidence_text = json.dumps(response).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "api key",
            "token",
            "password",
            "credential value",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, evidence_text)


if __name__ == "__main__":
    unittest.main()
