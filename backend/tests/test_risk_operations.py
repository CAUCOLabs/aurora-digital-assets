import unittest

from tests.helpers import request_json


class RiskOperationsReviewCaseTests(unittest.TestCase):
    def test_create_review_case_from_shell_company_action(self) -> None:
        status, response = request_json(
            "POST",
            "/api/risk-operations/create-review-case",
            {
                "action_id": "RO-ACTION-002",
                "reviewer_id": "reviewer-demo",
                "priority": "urgent",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["status"], "created")
        self.assertEqual(response["source_action_id"], "RO-ACTION-002")
        self.assertIn("Shell company", response["case_title"])
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(response["audit_event_id"], "AUD-RISK-RO-ACTION-002")
        self.assertEqual(response["correlation_id"], "CORR-RISK-RO-ACTION-002")
        self.assertTrue(response["missing_evidence"])
