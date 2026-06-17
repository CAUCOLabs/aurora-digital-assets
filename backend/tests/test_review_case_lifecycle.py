import unittest

from tests.helpers import request_json


CASE_ID = "CASE-CRYPTO-AGILITY-PQ-READINESS"
EVIDENCE_PACKAGE_ID = "EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS"


class ReviewCaseLifecycleTests(unittest.TestCase):
    def test_crypto_agility_case_lifecycle(self) -> None:
        transitions = [
            (
                "under_review",
                "Initial review started.",
                "open",
                "under_review",
            ),
            (
                "action_required",
                "Mitigation actions are required.",
                "under_review",
                "action_required",
            ),
            (
                "mitigation_in_progress",
                "Mitigation work started.",
                "action_required",
                "mitigation_in_progress",
            ),
            (
                "mitigated",
                "Mitigation verified.",
                "mitigation_in_progress",
                "mitigated",
            ),
        ]

        for target_status, decision_note, previous_status, new_status in transitions:
            status, response = request_json(
                "POST",
                f"/api/review-cases/{CASE_ID}/transition",
                {
                    "target_status": target_status,
                    "reviewer_id": "reviewer-demo",
                    "decision_note": decision_note,
                    "evidence_package_id": EVIDENCE_PACKAGE_ID,
                },
            )

            self.assertEqual(status, 200)
            self.assertTrue(response["transition_allowed"])
            self.assertEqual(response["previous_status"], previous_status)
            self.assertEqual(response["new_status"], new_status)
            self.assertTrue(response["audit_event_created"])
            self.assertEqual(
                response["correlation_id"],
                "CORR-CRYPTO-AGILITY-PQ-READINESS",
            )

        close_status, close_response = request_json(
            "POST",
            f"/api/review-cases/{CASE_ID}/close",
            {
                "reviewer_id": "reviewer-demo",
                "decision_note": "Mitigation verified and case closed.",
                "final_decision": "mitigated",
                "evidence_package_id": EVIDENCE_PACKAGE_ID,
            },
        )

        self.assertEqual(close_status, 200)
        self.assertTrue(close_response["transition_allowed"])
        self.assertEqual(close_response["new_status"], "closed")
        self.assertTrue(close_response["audit_event_created"])
        self.assertIn("CLOSED", close_response["audit_event_id"])

        invalid_status, invalid_response = request_json(
            "POST",
            f"/api/review-cases/{CASE_ID}/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Attempt to reopen closed case.",
                "evidence_package_id": EVIDENCE_PACKAGE_ID,
            },
        )

        self.assertEqual(invalid_status, 200)
        self.assertFalse(invalid_response["transition_allowed"])
        self.assertEqual(invalid_response["previous_status"], "closed")
        self.assertEqual(invalid_response["new_status"], "closed")
        self.assertFalse(invalid_response["audit_event_created"])

        summary_status, summary = request_json(
            "GET",
            f"/api/review-cases/{CASE_ID}/lifecycle",
        )

        self.assertEqual(summary_status, 200)
        self.assertEqual(summary["current_status"], "closed")
        self.assertIn("allowed_next_statuses", summary)
        self.assertIn("lifecycle_progress_percent", summary)
        self.assertIn(
            "AUD-CRYPTO-AGILITY-PQ-READINESS",
            summary["linked_audit_events"],
        )
        self.assertTrue(
            any("CLOSED" in audit_id for audit_id in summary["linked_audit_events"])
        )
