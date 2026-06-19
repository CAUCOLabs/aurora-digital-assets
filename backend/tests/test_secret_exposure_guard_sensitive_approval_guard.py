import json
import unittest

from tests.helpers import request_json


SENSITIVE_OPERATION_PAYLOAD = {
    "operation_type": "external_wallet_withdrawal",
    "actor_id": "customer-demo",
    "actor_type": "customer",
    "amount_eur": 8000,
    "asset": "BTC",
    "destination_type": "external_wallet",
    "destination_id": "new-wallet-demo",
    "is_new_destination": True,
    "customer_confirmed": True,
    "mobile_approval_status": "approved",
    "device_trusted": True,
    "session_age_minutes": 4,
}


class SecretExposureGuardSensitiveApprovalGuardTests(unittest.TestCase):
    def test_active_config_case_pauses_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_secret_guard_case_id": "CASE-SECRET-GUARD-CONFIG",
                "secret_guard_required": True,
                "secret_guard_status": "open",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["secret_guard_applied"])
        self.assertEqual(
            response["secret_guard_case_id"],
            "CASE-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(response["secret_guard_case_status"], "open")
        self.assertTrue(response["operation_paused_by_secret_guard"])
        self.assertNotEqual(response["backend_risk_decision"], "approved")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CONFIG",
        )
        self.assertEqual(response["review_case_id"], "CASE-SECRET-GUARD-CONFIG")
        self.assertEqual(
            response["secret_guard_required_lifecycle_status"],
            "mitigated_or_closed",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertIn(
            "preserve_evidence_without_secret_value",
            response["recommended_next_action"],
        )
        self.assertIn(
            "redact_sensitive_material",
            response["recommended_next_action"],
        )
        self.assertIn(
            "restrict_access_to_affected_surface",
            response["recommended_next_action"],
        )
        self.assertIn(
            "verify_no_secret_value_is_stored",
            response["recommended_next_action"],
        )
        self.assertIn(
            "require_human_approval_before_continuing",
            response["recommended_next_action"],
        )

    def test_active_custodian_secret_case_pauses_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_secret_guard_case_id": (
                    "CASE-SECRET-GUARD-CUSTODIAN-SECRET"
                ),
                "secret_guard_required": True,
                "secret_guard_status": "under_review",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["secret_guard_applied"])
        self.assertTrue(response["operation_paused_by_secret_guard"])
        self.assertNotEqual(response["backend_risk_decision"], "approved")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-SECRET-GUARD-CUSTODIAN-SECRET",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CUSTODIAN-SECRET",
        )
        self.assertEqual(
            response["review_case_id"],
            "CASE-SECRET-GUARD-CUSTODIAN-SECRET",
        )

    def test_no_linked_secret_guard_case_keeps_existing_behavior(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            SENSITIVE_OPERATION_PAYLOAD,
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["backend_risk_decision"], "pending_review")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertFalse(response["secret_guard_applied"])
        self.assertFalse(response["operation_paused_by_secret_guard"])

    def test_cleared_secret_guard_case_does_not_force_guard_block(self) -> None:
        for lifecycle_status in ("mitigated", "closed"):
            with self.subTest(lifecycle_status=lifecycle_status):
                status, response = request_json(
                    "POST",
                    "/api/sensitive-approval/evaluate",
                    {
                        **SENSITIVE_OPERATION_PAYLOAD,
                        "linked_secret_guard_case_id": "CASE-SECRET-GUARD-CONFIG",
                        "secret_guard_required": True,
                        "secret_guard_status": lifecycle_status,
                    },
                )

                self.assertEqual(status, 200)
                self.assertTrue(response["secret_guard_applied"])
                self.assertEqual(
                    response["secret_guard_case_status"],
                    lifecycle_status,
                )
                self.assertEqual(response["secret_guard_decision"], "cleared")
                self.assertFalse(response["operation_paused_by_secret_guard"])
                self.assertEqual(
                    response["audit_event_id"],
                    "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
                )
                self.assertEqual(
                    response["backend_risk_decision"],
                    "pending_review",
                )

    def test_active_secret_guard_response_does_not_include_secret_examples(
        self,
    ) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_secret_guard_case_id": (
                    "CASE-SECRET-GUARD-CUSTODIAN-SECRET"
                ),
                "secret_guard_required": True,
                "secret_guard_status": "under_review",
            },
        )

        self.assertEqual(status, 200)
        response_text = json.dumps(response).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "password",
            "token",
            "mnemonic",
            "raw secret",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, response_text)
