import unittest

from tests.helpers import request_json


SENSITIVE_CASE_ID = "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN"
SENSITIVE_PACKAGE_ID = "EP-FROM-AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN"
SENSITIVE_AUDIT_ID = "AUD-AI-THREAT-SENSITIVE-OPERATION-CHAIN"
SENSITIVE_CORRELATION_ID = "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN"


class AIThreatDefenseLifecycleTests(unittest.TestCase):
    def test_a_sensitive_operation_chain_lifecycle_summary(self) -> None:
        status, response = request_json(
            "GET",
            f"/api/review-cases/{SENSITIVE_CASE_ID}/lifecycle",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], SENSITIVE_CASE_ID)
        self.assertIn("allowed_next_statuses", response)
        self.assertIn("lifecycle_progress_percent", response)
        self.assertIn("closure_ready", response)
        self.assertIn(SENSITIVE_AUDIT_ID, response["linked_audit_events"])
        self.assertIn(
            SENSITIVE_PACKAGE_ID,
            response["linked_evidence_packages"],
        )

    def test_b_sensitive_operation_chain_full_lifecycle(self) -> None:
        transitions = [
            (
                "under_review",
                "Review exposed surfaces and preserve evidence.",
                "open",
                "AUD-LIFECYCLE-AI-THREAT-SENSITIVE-OPERATION-CHAIN-UNDER-REVIEW",
            ),
            (
                "action_required",
                "Tighten permissions and keep the sensitive operation paused.",
                "under_review",
                "AUD-LIFECYCLE-AI-THREAT-SENSITIVE-OPERATION-CHAIN-ACTION-REQUIRED",
            ),
            (
                "mitigation_in_progress",
                "Validate object-level authorization and review API surface minimization.",
                "action_required",
                "AUD-LIFECYCLE-AI-THREAT-SENSITIVE-OPERATION-CHAIN-MITIGATION-IN-PROGRESS",
            ),
            (
                "mitigated",
                "Verify mitigation and preserve evidence.",
                "mitigation_in_progress",
                "AUD-LIFECYCLE-AI-THREAT-SENSITIVE-OPERATION-CHAIN-MITIGATED",
            ),
        ]

        for target_status, decision_note, previous_status, audit_event_id in transitions:
            status, response = request_json(
                "POST",
                f"/api/review-cases/{SENSITIVE_CASE_ID}/transition",
                {
                    "target_status": target_status,
                    "reviewer_id": "reviewer-demo",
                    "decision_note": decision_note,
                    "mitigation_action": decision_note,
                    "evidence_package_id": SENSITIVE_PACKAGE_ID,
                },
            )

            self.assertEqual(status, 200)
            self.assertTrue(response["transition_allowed"])
            self.assertEqual(response["previous_status"], previous_status)
            self.assertEqual(response["new_status"], target_status)
            self.assertTrue(response["audit_event_created"])
            self.assertEqual(response["audit_event_id"], audit_event_id)
            self.assertEqual(response["correlation_id"], SENSITIVE_CORRELATION_ID)

        close_status, close_response = request_json(
            "POST",
            f"/api/review-cases/{SENSITIVE_CASE_ID}/close",
            {
                "reviewer_id": "reviewer-demo",
                "decision_note": "Mitigation verified and evidence preserved.",
                "final_decision": "mitigated",
                "evidence_package_id": SENSITIVE_PACKAGE_ID,
            },
        )

        self.assertEqual(close_status, 200)
        self.assertTrue(close_response["transition_allowed"])
        self.assertEqual(close_response["previous_status"], "mitigated")
        self.assertEqual(close_response["new_status"], "closed")
        self.assertTrue(close_response["audit_event_created"])
        self.assertEqual(
            close_response["audit_event_id"],
            "AUD-LIFECYCLE-AI-THREAT-SENSITIVE-OPERATION-CHAIN-CLOSED",
        )
        self.assertEqual(close_response["correlation_id"], SENSITIVE_CORRELATION_ID)

    def test_c_sensitive_operation_chain_rejects_transition_after_closed(self) -> None:
        status, response = request_json(
            "POST",
            f"/api/review-cases/{SENSITIVE_CASE_ID}/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Attempt to reopen a closed defensive review.",
                "evidence_package_id": SENSITIVE_PACKAGE_ID,
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["transition_allowed"])
        self.assertEqual(response["previous_status"], "closed")
        self.assertEqual(response["new_status"], "closed")
        self.assertFalse(response["audit_event_created"])

    def test_d_secret_exposure_transition_preserves_correlation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-AI-THREAT-SECRET-EXPOSURE/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": (
                    "Review controlled documentation, logs, evidence, and "
                    "configuration context."
                ),
                "evidence_package_id": "EP-FROM-AUD-AI-THREAT-SECRET-EXPOSURE",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-AI-THREAT-SECRET-EXPOSURE-UNDER-REVIEW",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SECRET-EXPOSURE",
        )

