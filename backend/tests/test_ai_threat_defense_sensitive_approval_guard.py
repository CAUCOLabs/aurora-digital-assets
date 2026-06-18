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


class AIThreatDefenseSensitiveApprovalGuardTests(unittest.TestCase):
    def test_active_sensitive_operation_chain_case_pauses_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_ai_threat_case_id": (
                    "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN"
                ),
                "ai_threat_guard_required": True,
                "ai_threat_guard_status": "open",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["ai_threat_guard_applied"])
        self.assertEqual(
            response["ai_threat_case_id"],
            "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(response["ai_threat_case_status"], "open")
        self.assertTrue(response["operation_paused_until_review"])
        self.assertNotEqual(response["backend_risk_decision"], "approved")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-AI-THREAT-GUARD-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SENSITIVE-OPERATION-CHAIN",
        )
        self.assertEqual(
            response["required_lifecycle_status"],
            "mitigated_or_closed",
        )

    def test_active_secret_exposure_case_pauses_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_ai_threat_case_id": "CASE-AI-THREAT-SECRET-EXPOSURE",
                "ai_threat_guard_required": True,
                "ai_threat_guard_status": "under_review",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["ai_threat_guard_applied"])
        self.assertTrue(response["operation_paused_until_review"])
        self.assertNotEqual(response["backend_risk_decision"], "approved")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-AI-THREAT-GUARD-SECRET-EXPOSURE",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertIn(
            "preserve_evidence",
            response["recommended_next_action"],
        )
        self.assertIn(
            "rotate_exposed_credentials_where_applicable",
            response["recommended_next_action"],
        )
        self.assertNotIn("seed", response["recommended_next_action"].lower())
        self.assertNotIn("private key", response["recommended_next_action"].lower())

    def test_no_linked_ai_threat_case_keeps_existing_behavior(self) -> None:
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
        self.assertFalse(response["ai_threat_guard_applied"])
        self.assertFalse(response["operation_paused_until_review"])

    def test_cleared_ai_threat_case_does_not_force_guard_block(self) -> None:
        for lifecycle_status in ("mitigated", "closed"):
            with self.subTest(lifecycle_status=lifecycle_status):
                status, response = request_json(
                    "POST",
                    "/api/sensitive-approval/evaluate",
                    {
                        **SENSITIVE_OPERATION_PAYLOAD,
                        "linked_ai_threat_case_id": (
                            "CASE-AI-THREAT-SENSITIVE-OPERATION-CHAIN"
                        ),
                        "ai_threat_guard_required": True,
                        "ai_threat_guard_status": lifecycle_status,
                    },
                )

                self.assertEqual(status, 200)
                self.assertTrue(response["ai_threat_guard_applied"])
                self.assertEqual(
                    response["ai_threat_case_status"],
                    lifecycle_status,
                )
                self.assertEqual(response["ai_threat_guard_decision"], "cleared")
                self.assertFalse(response["operation_paused_until_review"])
                self.assertEqual(
                    response["audit_event_id"],
                    "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
                )
                self.assertEqual(
                    response["backend_risk_decision"],
                    "pending_review",
                )
