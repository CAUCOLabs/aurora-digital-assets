import unittest

from tests.helpers import request_json


class EvidencePackageAuditEventTests(unittest.TestCase):
    def test_generate_evidence_package_from_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-API-GRAPHQL-PIN",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["source_type"], "audit_event")
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-API-GRAPHQL-PIN",
        )
        self.assertTrue(response["correlation_id"])
        self.assertTrue(response["traceability_summary"])
        self.assertTrue(response["audit_event_created"])
        self.assertIn(
            "AUD-EVIDENCE-FROM-AUD-API-GRAPHQL-PIN",
            response["audit_event_id"],
        )
        self.assertTrue(response["evidence_items"])

    def test_generate_infrastructure_evidence_package_from_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-INFRA-CHAIN-REACTION",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["source_type"], "audit_event")
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-INFRA-CHAIN-REACTION",
        )
        self.assertEqual(response["correlation_id"], "CORR-INFRA-CHAIN-REACTION")
        self.assertIn(
            "AUD-INFRA-CHAIN-REACTION",
            response["linked_audit_events"],
        )
        self.assertIn("Infrastructure Security", response["package"]["title"])
        self.assertEqual(
            response["package"]["audit_context"]["domain"],
            "infrastructure_security",
        )
        self.assertEqual(response["package"]["status"], "ready")
        self.assertTrue(response["readiness_check"]["ready"])
        self.assertTrue(response["evidence_items"])

    def test_generate_azure_storage_identity_evidence_package_from_audit_event(self) -> None:
        status, response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-INFRA-AZURE-STORAGE-IDENTITY",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["source_audit_event_id"],
            "AUD-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-INFRA-AZURE-STORAGE-IDENTITY",
        )
        self.assertIn(
            "AUD-INFRA-AZURE-STORAGE-IDENTITY",
            response["linked_audit_events"],
        )
        self.assertEqual(
            response["package"]["source_module"],
            "infrastructure_security",
        )
        self.assertEqual(
            response["package"]["audit_context"]["domain"],
            "azure_identity_storage_security",
        )
