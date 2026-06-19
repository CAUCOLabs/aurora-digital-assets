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


class CustodianGuardrailsSensitiveApprovalGuardTests(unittest.TestCase):
    def test_active_custodian_guard_case_blocks_sensitive_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_custodian_guard_case_id": (
                    "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
                ),
                "custodian_guard_required": True,
                "custodian_guard_status": "open",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["backend_risk_decision"], "pending_review")
        self.assertEqual(response["risk_level"], "critical")
        self.assertGreaterEqual(response["risk_score"], 96)
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-CUSTODIAN-GUARD-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(
            response["review_case_id"],
            "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertTrue(response["custodian_guard_applied"])
        self.assertEqual(
            response["custodian_guard_case_id"],
            "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(response["custodian_guard_case_status"], "open")
        self.assertEqual(response["custodian_guard_decision"], "pending_review")
        self.assertTrue(response["operation_paused_by_custodian_guard"])
        self.assertEqual(
            response["custodian_guard_required_lifecycle_status"],
            "mitigated_or_closed",
        )
        self.assertIn(
            "keep_sensitive_operation_paused_until_custodian_guard_review_is_mitigated_or_closed",
            response["recommended_next_action"],
        )

    def test_closed_custodian_guard_case_clears_guard(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_custodian_guard_case_id": (
                    "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
                ),
                "custodian_guard_required": True,
                "custodian_guard_status": "closed",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["custodian_guard_applied"])
        self.assertEqual(response["custodian_guard_decision"], "cleared")
        self.assertFalse(response["operation_paused_by_custodian_guard"])
        self.assertNotEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-CUSTODIAN-GUARD-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(response["backend_risk_decision"], "pending_review")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )

    def test_mitigated_custodian_guard_case_clears_guard(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_custodian_guard_case_id": (
                    "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
                ),
                "custodian_guard_required": True,
                "custodian_guard_status": "mitigated",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["custodian_guard_applied"])
        self.assertEqual(response["custodian_guard_decision"], "cleared")
        self.assertFalse(response["operation_paused_by_custodian_guard"])

    def test_active_asset_segregation_case_blocks_sensitive_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_custodian_guard_case_id": (
                    "CASE-CUSTODIAN-ASSET-SEGREGATION-GAP"
                ),
                "custodian_guard_required": True,
                "custodian_guard_status": "action_required",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-CUSTODIAN-GUARD-ASSET-SEGREGATION-GAP",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertTrue(response["operation_paused_by_custodian_guard"])

    def test_mobile_approved_does_not_override_active_custodian_guard(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                **SENSITIVE_OPERATION_PAYLOAD,
                "linked_custodian_guard_case_id": (
                    "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP"
                ),
                "custodian_guard_required": True,
                "custodian_guard_status": "under_review",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["mobile_approval_status"], "approved")
        self.assertEqual(response["backend_risk_decision"], "pending_review")
        self.assertTrue(response["operation_paused_by_custodian_guard"])
        self.assertEqual(response["custodian_guard_decision"], "pending_review")

    def test_no_custodian_guard_required_preserves_existing_behavior(self) -> None:
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
        self.assertFalse(response["custodian_guard_applied"])
        self.assertFalse(response["operation_paused_by_custodian_guard"])

