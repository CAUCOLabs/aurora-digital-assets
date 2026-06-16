import unittest

from tests.helpers import request_json


class ReviewCasesFromEvidencePackageTests(unittest.TestCase):
    def test_create_infrastructure_review_case_from_evidence_package(self) -> None:
        payload = {
            "package_id": "EP-FROM-AUD-INFRA-CHAIN-REACTION",
            "source_audit_event_id": "AUD-INFRA-CHAIN-REACTION",
            "correlation_id": "CORR-INFRA-CHAIN-REACTION",
            "reviewer_id": "reviewer-demo",
            "priority": "critical",
        }

        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            payload,
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], "CASE-INFRA-CHAIN-REACTION")
        self.assertEqual(
            response["source_package_id"],
            "EP-FROM-AUD-INFRA-CHAIN-REACTION",
        )
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-INFRA-CHAIN-REACTION",
        )
        self.assertEqual(response["correlation_id"], "CORR-INFRA-CHAIN-REACTION")
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["priority"], "critical")
        self.assertIn(response["status"], ["open", "under_review", "review_required"])
        self.assertIn(
            "EP-FROM-AUD-INFRA-CHAIN-REACTION",
            response["linked_evidence_packages"],
        )
        self.assertIn(
            "AUD-INFRA-CHAIN-REACTION",
            response["linked_audit_events"],
        )
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-REVIEW-FROM-EP-INFRA-CHAIN-REACTION",
        )

        list_status, cases = request_json("GET", "/api/review-cases")

        self.assertEqual(list_status, 200)
        self.assertTrue(
            any(
                review_case["case_id"] == "CASE-INFRA-CHAIN-REACTION"
                for review_case in cases
            )
        )

    def test_create_azure_storage_identity_review_case_from_evidence_package(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
                "source_audit_event_id": "AUD-INFRA-AZURE-STORAGE-IDENTITY",
                "correlation_id": "CORR-INFRA-AZURE-STORAGE-IDENTITY",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], "CASE-INFRA-AZURE-STORAGE-IDENTITY")
        self.assertEqual(
            response["source_package_id"],
            "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertEqual(response["severity"], "critical")
        self.assertIn(
            "EP-FROM-AUD-INFRA-AZURE-STORAGE-IDENTITY",
            response["linked_evidence_packages"],
        )
        self.assertIn(
            "AUD-INFRA-AZURE-STORAGE-IDENTITY",
            response["linked_audit_events"],
        )
        self.assertTrue(response["audit_event_created"])
