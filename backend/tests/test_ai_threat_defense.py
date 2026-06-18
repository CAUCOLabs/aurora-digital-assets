import unittest

from tests.helpers import request_json


class AIThreatDefenseTests(unittest.TestCase):
    def test_surfaces_include_sensitive_operations_and_config_secrets(self) -> None:
        status, response = request_json("GET", "/api/ai-threat-defense/surfaces")

        self.assertEqual(status, 200)
        self.assertIsInstance(response, list)

        surface_ids = {surface["surface_id"] for surface in response}
        self.assertIn("SENSITIVE-OPERATIONS", surface_ids)
        self.assertIn("CONFIG-SECRETS", surface_ids)

    def test_scenarios_include_phase_one_catalog(self) -> None:
        status, response = request_json("GET", "/api/ai-threat-defense/scenarios")

        self.assertEqual(status, 200)

        scenario_ids = {scenario["scenario_id"] for scenario in response}
        self.assertIn("ai_assisted_api_mapping", scenario_ids)
        self.assertIn("ai_assisted_sensitive_operation_chain", scenario_ids)
        self.assertIn("ai_assisted_secret_exposure_signal", scenario_ids)

    def test_sensitive_operation_chain_escalates_to_review(self) -> None:
        status, response = request_json(
            "POST",
            "/api/ai-threat-defense/evaluate-scenario",
            {
                "scenario_id": "ai_assisted_sensitive_operation_chain",
                "actor_type": "external_actor",
                "suspected_automation": True,
                "endpoint_enumeration": True,
                "sensitive_operation_chain": True,
                "permission_anomaly": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["decision"], "review_required")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["review_case_id"],
            "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )

    def test_secret_exposure_signal_requires_review(self) -> None:
        status, response = request_json(
            "POST",
            "/api/ai-threat-defense/evaluate-scenario",
            {
                "scenario_id": "ai_assisted_secret_exposure_signal",
                "actor_type": "unknown",
                "suspected_automation": True,
                "secret_exposure_signal": True,
                "documentation_exposure": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["review_case_id"],
            "CASE-AI-THREAT-SECRET-EXPOSURE",
        )

    def test_api_mapping_with_moderate_signals_stays_below_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/ai-threat-defense/evaluate-scenario",
            {
                "scenario_id": "ai_assisted_api_mapping",
                "actor_type": "unknown",
                "endpoint_enumeration": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertGreaterEqual(response["risk_score"], 60)
        self.assertIn(response["severity"], {"medium", "high"})
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(response["audit_event_id"], "AUD-AI-THREAT-API-MAPPING")
        self.assertFalse(response["review_case_required"])
