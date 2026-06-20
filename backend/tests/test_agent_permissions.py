import unittest

from tests.helpers import request_json


class AgentPermissionsTests(unittest.TestCase):
    def test_permission_catalog_contains_blocked_sensitive_permissions(self) -> None:
        status, response = request_json("GET", "/api/agent-permissions/catalog")

        self.assertEqual(status, 200)
        permissions = {item["permission_id"]: item for item in response}
        self.assertIn("read_audit_events", permissions)
        self.assertIn("access_secrets", permissions)
        self.assertIn("approve_withdrawals", permissions)
        self.assertTrue(permissions["access_secrets"]["blocked_by_default"])
        self.assertTrue(permissions["approve_withdrawals"]["blocked_by_default"])

    def test_permission_profiles_include_default_agent_types(self) -> None:
        status, response = request_json("GET", "/api/agent-permissions/profiles")

        self.assertEqual(status, 200)
        profiles = {item["agent_type"]: item for item in response}
        self.assertIn("compliance_assistant", profiles)
        self.assertIn("risk_analyst_agent", profiles)
        self.assertIn("custodian_integration_agent", profiles)

    def test_compliance_agent_permissions_include_allowed_and_restricted(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-permissions/agents/AGENT-COMPLIANCE-ASSISTANT-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["agent_type"], "compliance_assistant")
        self.assertIn("read_audit_events", response["allowed_permissions"])
        self.assertIn("create_reports", response["allowed_permissions"])
        self.assertIn(
            "access_secrets",
            response["denied_or_restricted_permissions"],
        )

    def test_evaluate_allowed_compliance_permission(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "permission_id": "read_audit_events",
                "resource_type": "audit_event",
                "resource_id": "AUD-DEMO",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "allowed")
        self.assertTrue(response["allowed"])
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-PERMISSION-EVALUATED-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENTS",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )

    def test_evaluate_secret_access_is_blocked(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "permission_id": "access_secrets",
                "resource_type": "secret_reference",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "blocked_secret_access")
        self.assertFalse(response["allowed"])
        self.assertIn("secrets_access_prohibited", response["blocking_reasons"])
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no raw credentials", safety_notice)
        self.assertIn("secrets", safety_notice)

    def test_suspended_custodian_agent_cannot_access_custodian_apis(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/evaluate",
            {
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "permission_id": "access_custodian_apis",
                "resource_type": "future_custodian_api",
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "blocked_by_agent_status")
        self.assertFalse(response["allowed"])
        self.assertIn("agent_status_suspended", response["blocking_reasons"])
        self.assertIn(
            "no real custodian api access",
            response["safety_notice"].lower(),
        )

    def test_grant_preview_create_reports_for_compliance_agent(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/agents/AGENT-COMPLIANCE-ASSISTANT-001/grant-preview",
            {
                "permission_id": "create_reports",
                "scope": ["local_reports"],
                "environment": "local",
                "reviewer_id": "reviewer-demo",
                "justification": "Preview reporting grant for local prototype.",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["grant_preview_decision"],
            {"grant_preview_allowed", "grant_preview_requires_review"},
        )
        self.assertTrue(response["audit_event_created"])
        self.assertIn("audit_event", response["required_controls"])

    def test_grant_preview_access_secrets_is_blocked(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/agents/AGENT-COMPLIANCE-ASSISTANT-001/grant-preview",
            {
                "permission_id": "access_secrets",
                "scope": ["prototype_secret_reference"],
                "environment": "local",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["grant_preview_decision"], "grant_preview_blocked")
        self.assertIn("secrets_access_prohibited", response["blocking_reasons"])
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no raw credentials", safety_notice)
        self.assertIn("tokens", safety_notice)
        self.assertIn("api keys", safety_notice)
        self.assertIn("passwords", safety_notice)
        self.assertIn("private keys", safety_notice)

    def test_unknown_permission_returns_404(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-permissions/evaluate",
            {
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "permission_id": "unknown_permission",
            },
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())

    def test_unknown_agent_returns_404(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-permissions/agents/AGENT-NOT-FOUND",
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())


if __name__ == "__main__":
    unittest.main()
