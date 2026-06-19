import unittest

from tests.helpers import request_json


class CloudKubernetesGuardrailsTests(unittest.TestCase):
    def test_controls_catalog_contains_required_guardrails(self) -> None:
        status, response = request_json(
            "GET",
            "/api/cloud-kubernetes-guardrails/controls",
        )

        self.assertEqual(status, 200)
        control_ids = {control["control_id"] for control in response}
        self.assertIn("K8S-RBAC-LEAST-PRIVILEGE", control_ids)
        self.assertIn("K8S-SECRET-HANDLING", control_ids)
        self.assertIn("CLOUD-SECRET-MANAGEMENT", control_ids)

    def test_scenarios_catalog_contains_required_scenarios(self) -> None:
        status, response = request_json(
            "GET",
            "/api/cloud-kubernetes-guardrails/scenarios",
        )

        self.assertEqual(status, 200)
        scenario_ids = {scenario["scenario_id"] for scenario in response}
        self.assertIn("cloud_kubernetes_readiness_gap", scenario_ids)
        self.assertIn("deployment_with_active_secret_guard_case", scenario_ids)
        self.assertIn("kubernetes_secret_handling_gap", scenario_ids)

    def test_kubernetes_secret_handling_gap_blocks_deployment(self) -> None:
        status, response = request_json(
            "POST",
            "/api/cloud-kubernetes-guardrails/evaluate",
            {
                "scenario_id": "kubernetes_secret_handling_gap",
                "deployment_target": "future_kubernetes",
                "environment": "future_production",
                "kubernetes_enabled": True,
                "secrets_externalized": False,
                "rbac_least_privilege": False,
                "network_policy_enabled": False,
                "audit_logging_enabled": True,
                "backup_encryption_enabled": True,
                "image_provenance_checked": False,
                "runtime_policy_enabled": False,
                "namespace_isolation_enabled": False,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["decision"], "block_deployment")
        self.assertTrue(response["deployment_guard_applied"])
        self.assertTrue(response["deployment_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CLOUD-K8S-SECRET-HANDLING-GAP",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CLOUD-K8S-SECRET-HANDLING-GAP",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["review_case_id"],
            "CASE-CLOUD-K8S-SECRET-HANDLING-GAP",
        )
        self.assertTrue(
            {
                "K8S-SECRET-HANDLING",
                "CLOUD-SECRET-MANAGEMENT",
            }.intersection(response["missing_controls"])
        )

    def test_active_secret_guard_case_blocks_future_deployment(self) -> None:
        status, response = request_json(
            "POST",
            "/api/cloud-kubernetes-guardrails/evaluate",
            {
                "scenario_id": "deployment_with_active_secret_guard_case",
                "deployment_target": "future_cloud",
                "environment": "future_production",
                "kubernetes_enabled": True,
                "secrets_externalized": True,
                "rbac_least_privilege": True,
                "network_policy_enabled": True,
                "audit_logging_enabled": True,
                "backup_encryption_enabled": True,
                "image_provenance_checked": True,
                "runtime_policy_enabled": True,
                "namespace_isolation_enabled": True,
                "active_secret_guard_case_id": "CASE-SECRET-GUARD-CONFIG",
                "active_secret_guard_case_status": "open",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["decision"], "block_deployment")
        self.assertTrue(response["deployment_blocked"])
        self.assertEqual(
            response["linked_secret_guard_case_id"],
            "CASE-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CLOUD-K8S-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CLOUD-K8S-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertTrue(response["review_case_required"])

    def test_all_controls_satisfied_readiness_does_not_block_deployment(self) -> None:
        status, response = request_json(
            "POST",
            "/api/cloud-kubernetes-guardrails/evaluate",
            {
                "scenario_id": "cloud_kubernetes_readiness_gap",
                "deployment_target": "future_cloud",
                "environment": "prototype",
                "kubernetes_enabled": False,
                "secrets_externalized": True,
                "rbac_least_privilege": True,
                "network_policy_enabled": True,
                "audit_logging_enabled": True,
                "backup_encryption_enabled": True,
                "image_provenance_checked": True,
                "runtime_policy_enabled": True,
                "namespace_isolation_enabled": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["decision"],
            ["allow", "harden", "review_required"],
        )
        self.assertFalse(response["deployment_blocked"])
        self.assertTrue(response["audit_event_created"])
