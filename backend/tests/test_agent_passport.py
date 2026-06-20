import unittest

from tests.helpers import request_json


class AgentPassportTests(unittest.TestCase):
    def test_passport_templates_include_required_restrictions(self) -> None:
        status, response = request_json("GET", "/api/agent-passports/templates")

        self.assertEqual(status, 200)
        templates = {item["agent_type"]: item for item in response}
        self.assertIn("custodian_integration_agent", templates)
        self.assertIn("high_risk_operation_agent", templates)
        self.assertIn(
            "no_autonomous_execution",
            templates["custodian_integration_agent"]["explicit_restrictions"],
        )
        self.assertIn(
            "custodian_guardrail_review_required",
            templates["custodian_integration_agent"]["explicit_restrictions"],
        )

    def test_local_medium_risk_compliance_agent_passport_is_valid(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-passports/AGENT-COMPLIANCE-ASSISTANT-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["passport_id"], "PASS-COMPLIANCE-ASSISTANT-001")
        self.assertEqual(response["passport_decision"], "passport_valid")
        self.assertTrue(response["passport_valid"])
        self.assertFalse(response["audit_event_created"])
        self.assertFalse(response["autonomous_execution_allowed"])
        self.assertFalse(response["custody_execution_allowed"])
        self.assertFalse(response["secrets_access_allowed"])
        self.assertFalse(response["sensitive_action_allowed"])
        self.assertFalse(response["external_tool_access_allowed"])
        self.assertIn(
            "suggest_compliance_follow_up",
            response["declared_capabilities"],
        )
        self.assertIn("no_private_key_access", response["explicit_restrictions"])
        self.assertIn(
            "no raw credentials stored",
            response["credential_reference_policy"].lower(),
        )

    def test_high_risk_agent_passport_requires_review(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-passports/AGENT-RISK-ANALYST-001/validate",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["passport_decision"], "passport_requires_review")
        self.assertFalse(response["passport_valid"])
        self.assertTrue(response["review_required"])
        self.assertTrue(response["evidence_required"])
        self.assertIn(
            "high_risk_requires_review",
            response["blocking_reasons"],
        )
        self.assertIn("summarize_risk_cases", response["declared_capabilities"])

    def test_blocked_custodian_agent_passport_is_status_blocked(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-passports/AGENT-CUSTODIAN-INTEGRATION-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["passport_id"],
            "PASS-CUSTODIAN-INTEGRATION-001",
        )
        self.assertEqual(response["passport_decision"], "passport_status_blocked")
        self.assertFalse(response["passport_valid"])
        self.assertTrue(response["evidence_required"])
        self.assertIn(response["status"], {"suspended", "revoked"})
        self.assertIn(
            f"agent_status_{response['status']}",
            response["blocking_reasons"],
        )
        self.assertIn(
            "integration_blocked_until_controls_verified",
            response["explicit_restrictions"],
        )
        self.assertIn(
            "read_custodian_evidence_metadata",
            response["declared_capabilities"],
        )

    def test_generate_passport_creates_deterministic_audit_reference(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-passports/generate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-PASSPORT-GENERATED-COMPLIANCE-ASSISTANT-001",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )
        self.assertEqual(response["passport_decision"], "passport_valid")

    def test_unknown_agent_passport_returns_404(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-passports/AGENT-NOT-FOUND",
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())


if __name__ == "__main__":
    unittest.main()
