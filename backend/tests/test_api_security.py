import unittest

from tests.helpers import request_json


class ApiSecurityScenarioTests(unittest.TestCase):
    def test_graphql_pin_scenario_creates_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/api-security/evaluate-scenario",
            {
                "scenario_id": "graphql_batching_pin_verification",
                "operation_name": "verifyTransferPin",
                "attempts": 8,
                "object_authorized": True,
                "batching_detected": True,
                "sensitive_fields_requested": False,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "block")
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_required"])
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(response["audit_event_id"], "AUD-API-GRAPHQL-PIN")
        self.assertEqual(response["correlation_id"], "CORR-API-GRAPHQL-PIN")
