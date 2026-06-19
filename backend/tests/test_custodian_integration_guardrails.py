import unittest

from tests.helpers import request_json


SATISFIED_CUSTODIAN_PAYLOAD = {
    "integration_target": "future_regulated_custodian",
    "environment": "future_production",
    "custodian_regulated": True,
    "asset_segregation_confirmed": True,
    "liability_boundary_defined": True,
    "sla_contract_signed": True,
    "audit_reports_available": True,
    "insurance_coverage_confirmed": True,
    "transfer_limits_configured": True,
    "withdrawal_approval_required": True,
    "api_access_controls_defined": True,
    "key_management_boundary_defined": True,
    "incident_reporting_defined": True,
    "reconciliation_defined": True,
    "evidence_export_available": True,
    "regulatory_reporting_defined": True,
    "responsibility_matrix_defined": True,
    "aurora_custodian_boundary_defined": True,
    "future_cloud_k8s_boundary_defined": True,
}


class CustodianIntegrationGuardrailsTests(unittest.TestCase):
    def test_controls_catalog_contains_required_guardrails(self) -> None:
        status, response = request_json(
            "GET",
            "/api/custodian-integration-guardrails/controls",
        )

        self.assertEqual(status, 200)
        control_ids = {control["control_id"] for control in response}
        self.assertIn("CUSTODIAN-ASSET-SEGREGATION", control_ids)
        self.assertIn("CUSTODIAN-KEY-MANAGEMENT-BOUNDARY", control_ids)
        self.assertIn("BANK-CUSTODIAN-RESPONSIBILITY-MATRIX", control_ids)

    def test_scenarios_catalog_contains_required_scenarios(self) -> None:
        status, response = request_json(
            "GET",
            "/api/custodian-integration-guardrails/scenarios",
        )

        self.assertEqual(status, 200)
        scenario_ids = {scenario["scenario_id"] for scenario in response}
        self.assertIn("custodian_missing_asset_segregation", scenario_ids)
        self.assertIn("custodian_key_management_boundary_gap", scenario_ids)
        self.assertIn("integration_with_active_secret_guard_case", scenario_ids)

    def test_key_management_boundary_gap_blocks_integration(self) -> None:
        status, response = request_json(
            "POST",
            "/api/custodian-integration-guardrails/evaluate",
            {
                **SATISFIED_CUSTODIAN_PAYLOAD,
                "scenario_id": "custodian_key_management_boundary_gap",
                "key_management_boundary_defined": False,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["decision"], "block_integration")
        self.assertTrue(response["integration_guard_applied"])
        self.assertTrue(response["integration_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["review_case_id"],
            "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertIn(
            "CUSTODIAN-KEY-MANAGEMENT-BOUNDARY",
            response["missing_controls"],
        )

    def test_asset_segregation_gap_blocks_integration(self) -> None:
        status, response = request_json(
            "POST",
            "/api/custodian-integration-guardrails/evaluate",
            {
                **SATISFIED_CUSTODIAN_PAYLOAD,
                "scenario_id": "custodian_missing_asset_segregation",
                "asset_segregation_confirmed": False,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "block_integration")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertEqual(
            response["review_case_id"],
            "CASE-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertIn(
            "CUSTODIAN-ASSET-SEGREGATION",
            response["missing_controls"],
        )

    def test_active_secret_guard_case_blocks_future_integration(self) -> None:
        status, response = request_json(
            "POST",
            "/api/custodian-integration-guardrails/evaluate",
            {
                **SATISFIED_CUSTODIAN_PAYLOAD,
                "scenario_id": "integration_with_active_secret_guard_case",
                "active_secret_guard_case_id": "CASE-SECRET-GUARD-CONFIG",
                "active_secret_guard_case_status": "open",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["decision"], "block_integration")
        self.assertTrue(response["integration_blocked"])
        self.assertEqual(
            response["linked_secret_guard_case_id"],
            "CASE-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertTrue(response["review_case_required"])

    def test_all_controls_satisfied_readiness_does_not_block_integration(
        self,
    ) -> None:
        status, response = request_json(
            "POST",
            "/api/custodian-integration-guardrails/evaluate",
            {
                **SATISFIED_CUSTODIAN_PAYLOAD,
                "scenario_id": "custodian_readiness_gap",
                "environment": "prototype",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["decision"],
            ["allow", "harden", "review_required"],
        )
        self.assertFalse(response["integration_blocked"])
        self.assertTrue(response["audit_event_created"])
