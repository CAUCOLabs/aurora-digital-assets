import json
import unittest

from tests.helpers import request_json


CRITICAL_READY_CONTROLS = {
    "legal_entity_verified": True,
    "regulatory_status_verified": True,
    "responsibility_matrix_defined": True,
    "liability_boundary_defined": True,
    "incident_reporting_defined": True,
    "security_assessment_completed": True,
    "access_control_model_defined": True,
    "least_privilege_enforced": True,
    "credential_boundary_defined": True,
    "no_raw_secret_exchange_confirmed": True,
    "human_approval_required_for_sensitive_actions": True,
    "agent_passport_required": True,
    "agent_permissions_defined": True,
    "agent_policy_engine_required": True,
    "agent_abuse_detection_required": True,
    "agent_sensitive_action_guard_required": True,
    "agent_revocation_required": True,
}

CUSTODIAN_READY_CONTROLS = {
    **CRITICAL_READY_CONTROLS,
    "custodian_asset_segregation_confirmed": True,
    "custodian_key_management_boundary_defined": True,
    "custodian_withdrawal_policy_defined": True,
    "custodian_reconciliation_defined": True,
    "custodian_regulatory_reporting_defined": True,
}


class ExternalPartnerAgentReadinessTests(unittest.TestCase):
    def test_lists_readiness_controls(self) -> None:
        status, response = request_json(
            "GET",
            "/api/external-partner-agent-readiness/controls",
        )

        self.assertEqual(status, 200)
        controls = {item["control_id"] for item in response}
        self.assertIn("legal_entity_verified", controls)
        self.assertIn("no_raw_secret_exchange_confirmed", controls)
        self.assertIn("agent_policy_engine_required", controls)
        self.assertIn("custodian_key_management_boundary_defined", controls)

    def test_lists_partner_types(self) -> None:
        status, response = request_json(
            "GET",
            "/api/external-partner-agent-readiness/partner-types",
        )

        self.assertEqual(status, 200)
        partner_types = {item["partner_type"] for item in response}
        self.assertIn("regulated_custodian", partner_types)
        self.assertIn("bank_partner", partner_types)
        self.assertIn("external_ai_agent_vendor", partner_types)
        self.assertIn("internal_partner_agent", partner_types)

    def test_blocks_custodian_agent_missing_key_management_boundary(self) -> None:
        controls = dict(CUSTODIAN_READY_CONTROLS)
        controls["custodian_key_management_boundary_defined"] = False

        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate",
            {
                "partner_id": "CUSTODIAN-DEMO-001",
                "partner_name": "Demo Regulated Custodian",
                "partner_type": "regulated_custodian",
                "environment": "local",
                "intended_integration_scope": "metadata_only_review",
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "agent_type": "custodian_integration_agent",
                "controls": controls,
                "linked_agent_passport_id": "PASS-CUSTODIAN-INTEGRATION-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["readiness_decision"],
            "block_custodian_agent_readiness",
        )
        self.assertTrue(response["custodian_access_blocked"])
        self.assertFalse(response["secret_exchange_blocked"])
        self.assertTrue(response["human_review_required"])
        self.assertTrue(response["review_case_required"])
        self.assertTrue(
            "custodian_key_management_boundary_defined"
            in response["missing_controls"]
            or "custodian_key_management_boundary_defined"
            in response["failed_controls"]
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-EXTERNAL-PARTNER-READINESS-CUSTODIAN-DEMO-001",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-EXTERNAL-PARTNER-CUSTODIAN-DEMO-001",
        )
        safety_notice = response["safety_notice"].lower()
        self.assertIn("no real custodian api access", safety_notice)
        self.assertIn("no credentials created or exchanged", safety_notice)

    def test_blocks_missing_secret_exchange_controls(self) -> None:
        controls = dict(CRITICAL_READY_CONTROLS)
        controls["no_raw_secret_exchange_confirmed"] = False
        controls["credential_boundary_defined"] = False

        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate",
            {
                "partner_id": "BANK-PARTNER-001",
                "partner_name": "Demo Bank Partner",
                "partner_type": "bank_partner",
                "controls": controls,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["readiness_decision"],
            ["block_secret_exchange", "block_external_access"],
        )
        self.assertTrue(response["secret_exchange_blocked"])
        self.assertTrue(
            response["external_access_blocked"]
            or response["sensitive_operations_blocked"]
        )
        self.assertIn("no secrets stored or exposed", response["safety_notice"].lower())

    def test_blocks_partner_with_linked_abuse_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate",
            {
                "partner_id": "EXTERNAL-AI-VENDOR-001",
                "partner_name": "Demo External AI Vendor",
                "partner_type": "external_ai_agent_vendor",
                "controls": CRITICAL_READY_CONTROLS,
                "linked_agent_abuse_audit_event_id": (
                    "AUD-AGENT-ABUSE-CUSTODIAN-INTEGRATION-001-"
                    "ATTEMPT-CUSTODIAN-API-ACCESS"
                ),
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["readiness_decision"], "block_external_access")
        self.assertTrue(response["external_access_blocked"])
        self.assertTrue(response["human_review_required"])
        self.assertIn(
            "review_agent_abuse_detection",
            response["recommended_next_actions"],
        )

    def test_ready_internal_partner_agent(self) -> None:
        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate",
            {
                "partner_id": "INTERNAL-PARTNER-001",
                "partner_name": "Internal Partner Agent",
                "partner_type": "internal_partner_agent",
                "agent_id": "AGENT-COMPLIANCE-ASSISTANT-001",
                "controls": CRITICAL_READY_CONTROLS,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["readiness_decision"],
            ["ready_for_internal_review", "ready_with_conditions"],
        )
        self.assertGreaterEqual(response["readiness_score"], 65)
        self.assertFalse(response["external_access_blocked"])
        self.assertFalse(response["secret_exchange_blocked"])
        self.assertIn("no external access granted", response["safety_notice"].lower())

    def test_evaluate_custodian_agent_ready_controls(self) -> None:
        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate-custodian-agent",
            {
                "partner_id": "CUSTODIAN-READY-001",
                "partner_name": "Ready Demo Custodian",
                "agent_id": "AGENT-CUSTODIAN-INTEGRATION-001",
                "controls": CUSTODIAN_READY_CONTROLS,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["partner_type"], "regulated_custodian")
        self.assertGreaterEqual(response["readiness_score"], 85)
        self.assertIn(
            response["readiness_decision"],
            ["ready_for_internal_review", "ready_with_conditions"],
        )
        self.assertIn("local deterministic readiness evaluation", response["safety_notice"].lower())
        self.assertIn("no partner onboarded", response["safety_notice"].lower())

    def test_readiness_preview_has_preview_partner_id(self) -> None:
        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/readiness-preview",
            {
                "partner_type": "external_ai_agent_vendor",
                "controls": CRITICAL_READY_CONTROLS,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["partner_id"], "PREVIEW-PARTNER")
        self.assertTrue(response["audit_event_created"])
        self.assertIn("no partner onboarded", response["safety_notice"].lower())

    def test_unknown_partner_type_does_not_crash_or_expose_secrets(self) -> None:
        status, response = request_json(
            "POST",
            "/api/external-partner-agent-readiness/evaluate",
            {
                "partner_id": "UNKNOWN-PARTNER-001",
                "partner_name": "Unknown Partner",
                "partner_type": "unknown_partner",
                "controls": {},
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["readiness_decision"], "insufficient_evidence")
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
