import json
import unittest

from tests.helpers import request_json


CONFIG_CASE_ID = "CASE-SECRET-GUARD-CONFIG"
CONFIG_PACKAGE_ID = "EP-FROM-AUD-SECRET-GUARD-CONFIG"
CONFIG_AUDIT_ID = "AUD-SECRET-GUARD-CONFIG"
CONFIG_CORRELATION_ID = "CORR-SECRET-GUARD-CONFIG"


class SecretExposureGuardLifecycleTests(unittest.TestCase):
    def test_a_config_secret_guard_lifecycle_summary(self) -> None:
        status, response = request_json(
            "GET",
            f"/api/review-cases/{CONFIG_CASE_ID}/lifecycle",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_id"], CONFIG_CASE_ID)
        self.assertIn("allowed_next_statuses", response)
        self.assertIn("lifecycle_progress_percent", response)
        self.assertIn("closure_ready", response)
        self.assertIn(CONFIG_AUDIT_ID, response["linked_audit_events"])
        self.assertIn(CONFIG_PACKAGE_ID, response["linked_evidence_packages"])

        serialized_response = json.dumps(response).lower()
        self.assertNotIn("private key", serialized_response)
        self.assertNotIn("seed phrase", serialized_response)

    def test_b_config_secret_guard_full_lifecycle(self) -> None:
        transitions = [
            (
                "under_review",
                "Start controlled review and preserve evidence without raw secret value.",
                "open",
                "AUD-LIFECYCLE-SECRET-GUARD-CONFIG-UNDER-REVIEW",
            ),
            (
                "action_required",
                "Redact sensitive material and restrict affected surface access.",
                "under_review",
                "AUD-LIFECYCLE-SECRET-GUARD-CONFIG-ACTION-REQUIRED",
            ),
            (
                "mitigation_in_progress",
                "Verify no raw secret value is stored and prepare mitigation evidence.",
                "action_required",
                "AUD-LIFECYCLE-SECRET-GUARD-CONFIG-MITIGATION-IN-PROGRESS",
            ),
            (
                "mitigated",
                "Mitigation verified and evidence preserved.",
                "mitigation_in_progress",
                "AUD-LIFECYCLE-SECRET-GUARD-CONFIG-MITIGATED",
            ),
        ]

        for target_status, decision_note, previous_status, audit_event_id in transitions:
            status, response = request_json(
                "POST",
                f"/api/review-cases/{CONFIG_CASE_ID}/transition",
                {
                    "target_status": target_status,
                    "reviewer_id": "reviewer-demo",
                    "decision_note": decision_note,
                    "mitigation_action": decision_note,
                    "evidence_package_id": CONFIG_PACKAGE_ID,
                },
            )

            self.assertEqual(status, 200)
            self.assertTrue(response["transition_allowed"])
            self.assertEqual(response["previous_status"], previous_status)
            self.assertEqual(response["new_status"], target_status)
            self.assertTrue(response["audit_event_created"])
            self.assertEqual(response["audit_event_id"], audit_event_id)
            self.assertEqual(response["correlation_id"], CONFIG_CORRELATION_ID)

        close_status, close_response = request_json(
            "POST",
            f"/api/review-cases/{CONFIG_CASE_ID}/close",
            {
                "reviewer_id": "reviewer-demo",
                "decision_note": "Close after mitigation verification.",
                "final_decision": "mitigated",
                "evidence_package_id": CONFIG_PACKAGE_ID,
            },
        )

        self.assertEqual(close_status, 200)
        self.assertTrue(close_response["transition_allowed"])
        self.assertEqual(close_response["previous_status"], "mitigated")
        self.assertEqual(close_response["new_status"], "closed")
        self.assertTrue(close_response["audit_event_created"])
        self.assertEqual(
            close_response["audit_event_id"],
            "AUD-LIFECYCLE-SECRET-GUARD-CONFIG-CLOSED",
        )
        self.assertEqual(close_response["correlation_id"], CONFIG_CORRELATION_ID)

    def test_c_config_secret_guard_rejects_transition_after_closed(self) -> None:
        status, response = request_json(
            "POST",
            f"/api/review-cases/{CONFIG_CASE_ID}/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Attempt to reopen a closed defensive review.",
                "evidence_package_id": CONFIG_PACKAGE_ID,
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["transition_allowed"])
        self.assertEqual(response["previous_status"], "closed")
        self.assertEqual(response["new_status"], "closed")
        self.assertFalse(response["audit_event_created"])

    def test_d_custodian_secret_guard_transition_preserves_context(self) -> None:
        package_id = "EP-FROM-AUD-SECRET-GUARD-CUSTODIAN-SECRET"
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-SECRET-GUARD-CUSTODIAN-SECRET/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Review future custodian boundary and preserve evidence.",
                "evidence_package_id": package_id,
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-SECRET-GUARD-CUSTODIAN-SECRET-UNDER-REVIEW",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
        )
        self.assertEqual(response["linked_evidence_package"], package_id)

    def test_e_cloud_secret_guard_transition_preserves_context(self) -> None:
        package_id = "EP-FROM-AUD-SECRET-GUARD-CLOUD-SECRET"
        status, response = request_json(
            "POST",
            "/api/review-cases/CASE-SECRET-GUARD-CLOUD-SECRET/transition",
            {
                "target_status": "under_review",
                "reviewer_id": "reviewer-demo",
                "decision_note": "Review future cloud boundary and preserve evidence.",
                "evidence_package_id": package_id,
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["transition_allowed"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-LIFECYCLE-SECRET-GUARD-CLOUD-SECRET-UNDER-REVIEW",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CLOUD-SECRET",
        )
        self.assertEqual(response["linked_evidence_package"], package_id)
