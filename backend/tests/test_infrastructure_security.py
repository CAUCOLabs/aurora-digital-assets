import unittest

from tests.helpers import request_json


class InfrastructureSecurityTests(unittest.TestCase):
    def test_evaluate_chain_reaction_scenario_creates_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/infrastructure-security/evaluate-scenario",
            {
                "scenario_id": "app_to_cloud_chain_reaction",
                "object_authorization_failed": True,
                "unsafe_template_input_detected": True,
                "pod_privileged": False,
                "service_account_can_read_secrets": True,
                "cloud_iam_wildcard_permissions": True,
                "weak_trust_policy": True,
                "secret_exposure_detected": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["decision"], "escalate")
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(response["audit_event_id"], "AUD-INFRA-CHAIN-REACTION")
        self.assertEqual(response["correlation_id"], "CORR-INFRA-CHAIN-REACTION")
        self.assertTrue(response["evidence_package_ready"])
        self.assertGreater(len(response["affected_layers"]), 0)

    def test_catalog_endpoints_return_demo_data(self) -> None:
        for path in [
            "/api/infrastructure-security/controls",
            "/api/infrastructure-security/events",
            "/api/infrastructure-security/layers",
            "/api/infrastructure-security/scenarios",
        ]:
            with self.subTest(path=path):
                status, response = request_json("GET", path)

                self.assertEqual(status, 200)
                self.assertGreater(len(response), 0)
