import unittest

from tests.helpers import request_json


KEY_CASE_ID = "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
KEY_PACKAGE_ID = "EP-FROM-AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
KEY_AUDIT_ID = "AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
KEY_CORRELATION_ID = "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"


class CustodianIntegrationGuardrailsLifecycleTests(unittest.TestCase):
    def test_a_key_management_boundary_lifecycle_summary(self) -> None:
        status, response = request_json(
            "GET",
            f"/api/review-cases/{KEY_CASE_ID}/lifecycle",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], KEY_CASE_ID)
        self.assertEqual(response["current_status"], "open")
        self.assertIn("under_review", response["allowed_next_statuses"])
        self.assertIn(KEY_PACKAGE_ID, response["linked_evidence_packages"])
        self.assertIn(KEY_AUDIT_ID, response["linked_audit_events"])
        self.assertIn(
            "AUD-EVIDENCE-FROM-AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
            response["linked_audit_events"],
        )
        self.assertFalse(response["closure_ready"])

    def test_b_key_management_boundary_transitions_to_under_review(self) -> None:
        status, response = request_json(
            "POST",
            f"/api/review-cases/{KEY_CASE_ID}/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Custodian key management boundary review started.",
                "evidence_package_id": KEY_PACKAGE_ID,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], KEY_CASE_ID)
        self.assertEqual(response["new_status"], "under_review")
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP-UNDER-REVIEW",
        )
        self.assertEqual(response["correlation_id"], KEY_CORRELATION_ID)

    def test_c_key_management_boundary_full_lifecycle_to_closed(self) -> None:
        transitions = [
            (
                "action_required",
                "Define custodian key management boundary and responsibilities.",
                "under_review",
                "AUD-LIFECYCLE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP-ACTION-REQUIRED",
            ),
            (
                "mitigation_in_progress",
                "Verify no custody signing material is stored or handled.",
                "action_required",
                "AUD-LIFECYCLE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP-MITIGATION-IN-PROGRESS",
            ),
            (
                "mitigated",
                "Custodian boundary mitigation verified.",
                "mitigation_in_progress",
                "AUD-LIFECYCLE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP-MITIGATED",
            ),
        ]

        for target_status, decision_note, previous_status, audit_event_id in transitions:
            status, response = request_json(
                "POST",
                f"/api/review-cases/{KEY_CASE_ID}/transition",
                {
                    "target_status": target_status,
                    "reviewer_id": "reviewer-demo",
                    "decision_note": decision_note,
                    "mitigation_action": decision_note,
                    "evidence_package_id": KEY_PACKAGE_ID,
                },
            )

            self.assertEqual(status, 200)
            self.assertTrue(response["transition_allowed"])
            self.assertEqual(response["previous_status"], previous_status)
            self.assertEqual(response["new_status"], target_status)
            self.assertEqual(response["audit_event_id"], audit_event_id)
            self.assertEqual(response["correlation_id"], KEY_CORRELATION_ID)

        close_status, close_response = request_json(
            "POST",
            f"/api/review-cases/{KEY_CASE_ID}/close",
            {
                "reviewer_id": "reviewer-demo",
                "decision_note": "Custodian boundary lifecycle closed.",
                "final_decision": "mitigated",
                "evidence_package_id": KEY_PACKAGE_ID,
            },
        )

        self.assertEqual(close_status, 200)
        self.assertTrue(close_response["transition_allowed"])
        self.assertEqual(close_response["new_status"], "closed")
        self.assertEqual(
            close_response["audit_event_id"],
            "AUD-LIFECYCLE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP-CLOSED",
        )

        summary_status, summary_response = request_json(
            "GET",
            f"/api/review-cases/{KEY_CASE_ID}/lifecycle",
        )
        self.assertEqual(summary_status, 200)
        self.assertEqual(summary_response["current_status"], "closed")

    def test_d_asset_segregation_gap_transition_preserves_context(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-CUSTODIAN-ASSET-SEGREGATION-GAP/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Custodian asset segregation review started.",
                "evidence_package_id": "EP-FROM-AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-CUSTODIAN-ASSET-SEGREGATION-GAP-UNDER-REVIEW",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )

    def test_e_active_secret_guard_case_transition_preserves_context(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Review active Secret Guard dependency before custodian integration.",
                "evidence_package_id": "EP-FROM-AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE-UNDER-REVIEW",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertIn(
            "verify_active_secret_guard_case_is_mitigated_or_closed_before_custodian_integration",
            response["recommended_actions"],
        )

    def test_f_invalid_custodian_lifecycle_transition_is_rejected(self) -> None:
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-CUSTODIAN-LIABILITY-BOUNDARY-GAP/transition",
            {
                "target_status": "mitigated",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Attempt invalid direct mitigation.",
                "evidence_package_id": "EP-FROM-AUD-CUSTODIAN-LIABILITY-BOUNDARY-GAP",
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["transition_allowed"])
        self.assertEqual(response["previous_status"], "open")
        self.assertEqual(response["new_status"], "open")
        self.assertFalse(response["audit_event_created"])
