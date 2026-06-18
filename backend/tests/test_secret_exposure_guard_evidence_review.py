import json
import unittest

from tests.helpers import request_json


class SecretExposureGuardEvidenceReviewTests(unittest.TestCase):
    def test_generate_config_secret_guard_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-SECRET-GUARD-CONFIG",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(response["correlation_id"], "CORR-SECRET-GUARD-CONFIG")
        self.assertEqual(response["package"]["source_module"], "secret_exposure_guard")
        self.assertEqual(response["package"]["severity"], "critical")
        self.assertEqual(response["package"]["status"], "ready")
        self.assertIn("readiness_score", response["package"])
        self.assertIn(
            "AUD-SECRET-GUARD-CONFIG",
            response["linked_audit_events"],
        )
        self.assertIn(
            "without storing or echoing",
            response["traceability_summary"],
        )
        self.assertFalse(response["package"]["audit_context"]["secret_value_stored"])
        self.assertFalse(response["package"]["audit_context"]["raw_secret_echoed"])

        serialized_response = json.dumps(response).lower()
        self.assertNotIn("private key", serialized_response)
        self.assertNotIn("seed phrase", serialized_response)

    def test_create_config_secret_guard_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-SECRET-GUARD-CONFIG",
                "source_audit_event_id": "AUD-SECRET-GUARD-CONFIG",
                "correlation_id": "CORR-SECRET-GUARD-CONFIG",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], "CASE-SECRET-GUARD-CONFIG")
        self.assertEqual(response["case_type"], "secret_exposure_review")
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(
            response["source_package_id"],
            "EP-FROM-AUD-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(response["correlation_id"], "CORR-SECRET-GUARD-CONFIG")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertEqual(response["status"], "open")

    def test_generate_prompt_context_secret_guard_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-SECRET-GUARD-PROMPT-CONTEXT",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-SECRET-GUARD-PROMPT-CONTEXT",
        )
        self.assertEqual(response["package"]["source_module"], "secret_exposure_guard")
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-PROMPT-CONTEXT",
        )
        self.assertIn(
            "without storing or echoing raw secret values",
            response["traceability_summary"],
        )

    def test_create_custodian_secret_guard_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-SECRET-GUARD-CUSTODIAN-SECRET",
                "source_audit_event_id": "AUD-SECRET-GUARD-CUSTODIAN-SECRET",
                "correlation_id": "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-SECRET-GUARD-CUSTODIAN-SECRET",
        )
        self.assertEqual(response["case_type"], "secret_exposure_review")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Custodian Oversight",
        )
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
        )

    def test_generate_cloud_secret_guard_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-SECRET-GUARD-CLOUD-SECRET",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-SECRET-GUARD-CLOUD-SECRET",
        )
        self.assertEqual(response["package"]["source_module"], "secret_exposure_guard")
        self.assertEqual(response["package"]["severity"], "critical")
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CLOUD-SECRET",
        )
