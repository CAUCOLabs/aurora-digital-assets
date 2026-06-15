import unittest

from tests.helpers import request_json


class OperationalResilienceScenarioTests(unittest.TestCase):
    def test_payments_dependency_failure_creates_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/operational-resilience/evaluate-scenario",
            {
                "scenario_id": "payment_dependency_failure",
                "affected_service": "payments",
                "dependency_status": "degraded",
                "customer_impact": "high",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "escalate_incident")
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(response["audit_event_id"], "AUD-OPS-PAYMENTS-DEGRADED")
        self.assertEqual(
            response["correlation_id"],
            "CORR-OPS-PAYMENTS-DEGRADED",
        )
