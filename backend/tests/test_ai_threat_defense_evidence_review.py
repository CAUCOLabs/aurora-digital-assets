import unittest

from tests.helpers import request_json


class AIThreatDefenseEvidenceReviewTests(unittest.TestCase):
    def test_generate_sensitive_operation_chain_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(response["package"]["source_module"], "ai_threat_defense")
        self.assertEqual(response["package"]["severity"], "critical")
        self.assertEqual(response["package"]["status"], "ready")
        self.assertIn(
            "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
            response["linked_audit_events"],
        )

    def test_create_sensitive_operation_chain_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "source_audit_event_id": "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "correlation_id": "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(response["case_type"], "ai_assisted_threat_review")
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["status"], "open")
        self.assertTrue(response["audit_event_created"])

        lifecycle_status, lifecycle = request_json(
            "GET",
            "/api/review-cases/CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN/lifecycle",
        )

        self.assertEqual(lifecycle_status, 200)
        self.assertEqual(
            lifecycle["case_id"],
            "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(lifecycle["current_status"], "open")
        self.assertIn(
            "EP-FROM-AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
            lifecycle["linked_evidence_packages"],
        )
        self.assertIn(
            "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
            lifecycle["linked_audit_events"],
        )

    def test_generate_secret_exposure_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-AI-THREAT-SECRET-EXPOSURE",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertEqual(response["package"]["severity"], "critical")
        self.assertEqual(response["package"]["source_module"], "ai_threat_defense")
        self.assertIn(
            "AUD-AI-THREAT-SECRET-EXPOSURE",
            response["linked_audit_events"],
        )

    def test_create_secret_exposure_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-AI-THREAT-SECRET-EXPOSURE",
                "source_audit_event_id": "AUD-AI-THREAT-SECRET-EXPOSURE",
                "correlation_id": "CORR-AI-THREAT-SECRET-EXPOSURE",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], "CASE-AI-THREAT-SECRET-EXPOSURE")
        self.assertEqual(response["case_type"], "ai_assisted_threat_review")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_created"])
