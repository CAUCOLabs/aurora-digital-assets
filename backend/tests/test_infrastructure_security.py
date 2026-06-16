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

    def test_evaluate_azure_storage_identity_scenario_creates_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/infrastructure-security/evaluate-scenario",
            {
                "scenario_id": "azure_storage_to_identity_chain_reaction",
                "object_authorization_failed": False,
                "unsafe_template_input_detected": False,
                "pod_privileged": False,
                "service_account_can_read_secrets": False,
                "cloud_iam_wildcard_permissions": False,
                "weak_trust_policy": False,
                "secret_exposure_detected": False,
                "storage_public_access_detected": True,
                "certificate_exposure_detected": True,
                "service_principal_overprivileged": True,
                "deployment_credentials_enabled": True,
                "managed_identity_excessive_scope": True,
                "password_reset_privilege_detected": True,
                "identity_monitoring_gap": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["decision"], "escalate")
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertIn(
            "Azure private storage control",
            response["triggered_controls"],
        )
