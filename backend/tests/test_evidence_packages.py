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
