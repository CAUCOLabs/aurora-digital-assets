import unittest

from tests.helpers import request_json


class AgentActionsTests(unittest.TestCase):
    def test_action_types_include_blocked_sensitive_attempts(self) -> None:
        status, response = request_json("GET", "/api/agent-actions/action-types")

        self.assertEqual(status, 200)
        action_types = {item["action_type"]: item for item in response}
        self.assertIn("read_audit_event", action_types)
        self.assertIn("attempt_secret_access", action_types)
        self.assertIn("attempt_custodian_api_access", action_types)
        self.assertTrue(action_types["attempt_secret_access"]["blocked_by_default"])
        self.assertTrue(
            action_types["attempt_withdrawal_approval"]["blocked_by_default"]
        )

    def test_recent_actions_include_demo_events(self) -> None:
        status, response = request_json("GET", "/api/agent-actions/recent")

        self.assertEqual(status, 200)
        self.assertGreaterEqual(len(response), 3)
        custodian_events = [
            item
            for item in response
            if item["agent_id"] == "AGENT-CUSTODIAN-INTEGRATION-001"
        ]
        self.assertTrue(custodian_events)
        self.assertIn(
            custodian_events[0]["action_outcome"],
            {
                "blocked_by_agent_status",
                "blocked_custody_execution",
                "blocked_sensitive_action",
            },
        )

    def test_evaluate_and_record_allowed_compliance_read_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "action_type": "read_audit_event",
                "permission_id": "read_audit_events",
                "resource_type": "audit_event",
                "resource_id": "AUD-DEMO",
                "environment": "local",
                "request_id": "REQ-AGENT-ACTION-DEMO-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["action_event_id"],
            "ACT-AGENT-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )
        self.assertEqual(response["permission_decision"], "allowed")
        self.assertEqual(response["action_outcome"], "allowed")
        self.assertTrue(response["allowed"])
        self.assertIn("no real action executed", response["safety_notice"].lower())

    def test_evaluate_and_record_blocked_secret_access(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "action_type": "attempt_secret_access",
                "permission_id": "access_secrets",
                "resource_type": "secret_reference",
                "environment": "local",
                "request_id": "REQ-AGENT-ACTION-SECRET-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["action_outcome"], "blocked_secret_access")
        self.assertFalse(response["allowed"])
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["risk_level"], "critical")
        self.assertTrue(response["evidence_required"])
        self.assertTrue(response["review_case_required"])
        self.assertIn("secrets_access_prohibited", response["blocking_reasons"])
        self.assertIn("no secrets stored or exposed", response["safety_notice"].lower())

    def test_evaluate_and_record_suspended_custodian_api_attempt(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "action_type": "attempt_custodian_api_access",
                "permission_id": "access_custodian_apis",
                "resource_type": "future_custodian_api",
                "environment": "local",
                "request_id": "REQ-AGENT-ACTION-CUSTODIAN-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["action_event_id"],
            "ACT-AGENT-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        self.assertEqual(response["permission_decision"], "blocked_by_agent_status")
        self.assertEqual(response["action_outcome"], "blocked_by_agent_status")
        self.assertFalse(response["allowed"])
        self.assertGreaterEqual(response["risk_score"], 95)
        self.assertTrue(response["evidence_required"])
        self.assertTrue(response["review_case_required"])
        self.assertIn("agent_status_suspended", response["blocking_reasons"])
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no external api called", safety_notice)
        self.assertIn("no custody", safety_notice)

    def test_evaluate_and_record_withdrawal_approval_attempt(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-RISK-ANALYST-001",
                "action_type": "attempt_withdrawal_approval",
                "permission_id": "approve_withdrawals",
                "resource_type": "external_wallet_withdrawal",
                "environment": "local",
                "request_id": "REQ-AGENT-ACTION-WITHDRAWAL-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["action_outcome"], "blocked_sensitive_action")
        self.assertFalse(response["allowed"])
        self.assertEqual(response["risk_level"], "critical")
        self.assertTrue(response["review_case_required"])
        self.assertIn(
            "no custody, blockchain, or withdrawal execution performed",
            response["safety_notice"].lower(),
        )

    def test_unknown_action_type_returns_404(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "action_type": "unknown_action",
                "permission_id": "read_audit_events",
            },
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())

    def test_unknown_agent_returns_404(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/evaluate-and-record",
            {
                "agent_id": "AGENT-NOT-FOUND",
                "action_type": "read_audit_event",
                "permission_id": "read_audit_events",
            },
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())

    def test_recorded_action_can_be_fetched_by_id(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-actions/record",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "action_type": "create_report",
                "permission_id": "create_reports",
                "resource_type": "report",
                "resource_id": "REPORT-DEMO",
                "request_id": "REQ-AGENT-ACTION-REPORT-001",
                "declared_outcome": "allowed",
            },
        )

        self.assertEqual(status, 200)
        action_event_id = response["action_event_id"]
        get_status, get_response = request_json(
            "GET",
            f"/api/agent-actions/{action_event_id}",
        )
        self.assertEqual(get_status, 200)
        self.assertEqual(get_response["action_event_id"], action_event_id)


if __name__ == "__main__":
    unittest.main()
