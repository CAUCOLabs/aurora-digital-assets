import unittest

from tests.helpers import request_json


class AgentRegistryTests(unittest.TestCase):
    def test_agent_types_include_sensitive_custodian_agent(self) -> None:
        status, response = request_json("GET", "/api/agent-registry/types")

        self.assertEqual(status, 200)
        types_by_id = {item["type_id"]: item for item in response}
        self.assertIn("compliance_assistant", types_by_id)
        self.assertIn("custodian_integration_agent", types_by_id)
        self.assertIn("high_risk_operation_agent", types_by_id)
        self.assertTrue(types_by_id["custodian_integration_agent"]["sensitive_by_default"])

    def test_agent_statuses_define_allowed_to_act(self) -> None:
        status, response = request_json("GET", "/api/agent-registry/statuses")

        self.assertEqual(status, 200)
        statuses = {item["status"]: item["allowed_to_act"] for item in response}
        self.assertTrue(statuses["active"])
        self.assertFalse(statuses["suspended"])
        self.assertFalse(statuses["revoked"])
        self.assertFalse(statuses["expired"])

    def test_agent_list_contains_demo_agents(self) -> None:
        status, response = request_json("GET", "/api/agent-registry/agents")

        self.assertEqual(status, 200)
        agent_ids = {item["agent_id"] for item in response}
        self.assertIn("AGENT-COMPLIANCE-ASSISTANT-001", agent_ids)
        self.assertIn("AGENT-RISK-ANALYST-001", agent_ids)
        self.assertIn("AGENT-CUSTODIAN-INTEGRATION-001", agent_ids)

    def test_get_custodian_integration_demo_agent(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-registry/agents/AGENT-CUSTODIAN-INTEGRATION-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["agent_type"], "custodian_integration_agent")
        self.assertEqual(response["status"], "suspended")
        self.assertEqual(response["risk_level"], "critical")
        self.assertEqual(
            response["human_accountable_party"],
            "Security Architecture Lead",
        )
        safety_notice = response["safety_notice"].lower()
        self.assertTrue(
            "no custodian" in safety_notice
            or "no autonomous execution" in safety_notice
        )

    def test_register_local_reporting_agent(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-registry/register",
            {
                "agent_name": "Monthly Board Reporting Agent",
                "agent_type": "reporting_agent",
                "owner_user_id": "user-reporting-demo",
                "owner_organization": "Aurora Demo Bank",
                "human_accountable_party": "Reporting Lead",
                "environment": "local",
                "risk_level": "medium",
                "purpose": (
                    "Prepare deterministic board reporting summaries from "
                    "approved internal reporting data."
                ),
                "connected_tools": ["reporting_api"],
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["agent_id"].startswith("AGENT-REPORTING-AGENT-"))
        self.assertEqual(response["status"], "active")
        self.assertEqual(response["registry_decision"], "registration_allowed")
        self.assertTrue(response["audit_event_created"])
        self.assertTrue(
            response["audit_event_id"].startswith("AUD-AGENT-REGISTERED-")
        )
        self.assertTrue(response["correlation_id"].startswith("CORR-AGENT-"))
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no permissions granted yet", safety_notice)
        self.assertIn("no secrets stored", safety_notice)

    def test_production_high_risk_operation_agent_requires_review(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-registry/register",
            {
                "agent_name": "Production Withdrawal Automation Agent",
                "agent_type": "high_risk_operation_agent",
                "owner_user_id": "user-ops-demo",
                "owner_organization": "Aurora Demo Bank",
                "human_accountable_party": "Head of Operations",
                "environment": "production",
                "risk_level": "critical",
                "purpose": (
                    "Prototype registration only. No real withdrawals or custody "
                    "execution."
                ),
                "connected_tools": ["sensitive_approval"],
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["registry_decision"],
            "registration_requires_review",
        )
        self.assertEqual(response["risk_level"], "critical")
        self.assertIn(
            "no autonomous execution granted",
            response["safety_notice"].lower(),
        )
        self.assertTrue(response["audit_event_created"])

    def test_update_custodian_agent_status_to_revoked(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-registry/agents/AGENT-CUSTODIAN-INTEGRATION-001/status",
            {
                "target_status": "revoked",
                "reviewer_id": "reviewer-demo",
                "decision_note": (
                    "Suspended custodian integration readiness agent revoked "
                    "during local governance test."
                ),
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["previous_status"], "suspended")
        self.assertEqual(response["new_status"], "revoked")
        self.assertTrue(response["status_update_allowed"])
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-STATUS-CUSTODIAN-INTEGRATION-001-REVOKED",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )
        self.assertIn(
            "block_future_actions",
            response["recommended_next_action"],
        )

    def test_unknown_agent_type_registration_is_rejected(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-registry/register",
            {
                "agent_name": "Unknown Agent",
                "agent_type": "unknown_agent_type",
                "owner_user_id": "user-demo",
                "owner_organization": "Aurora Demo Bank",
                "human_accountable_party": "Reviewer",
                "purpose": "Invalid registration test.",
            },
        )

        self.assertEqual(status, 400)
        self.assertIn("unknown agent type", response["detail"].lower())

    def test_unknown_agent_id_returns_404(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-registry/agents/AGENT-NOT-FOUND",
        )

        self.assertEqual(status, 404)
        self.assertIn("not found", response["detail"].lower())

