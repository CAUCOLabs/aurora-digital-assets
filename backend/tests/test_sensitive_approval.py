import unittest

from tests.helpers import request_json


class SensitiveApprovalTests(unittest.TestCase):
    def test_operations_catalog(self) -> None:
        status, response = request_json(
            "GET",
            "/api/sensitive-approval/operations",
        )

        self.assertEqual(status, 200)
        self.assertTrue(response)
        self.assertTrue(
            any(
                operation["operation_type"] == "external_wallet_withdrawal"
                for operation in response
            )
        )

    def test_small_known_wallet_withdrawal_is_approved(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 100,
                "asset": "BTC",
                "destination_type": "external_wallet",
                "destination_id": "known-wallet-demo",
                "is_new_destination": False,
                "customer_confirmed": True,
                "mobile_approval_status": "approved",
                "device_trusted": True,
                "session_age_minutes": 4,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["backend_risk_decision"], "approved")
        self.assertTrue(response["audit_event_created"])

    def test_high_value_new_wallet_withdrawal_requires_review(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
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
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["backend_risk_decision"], "pending_review")
        self.assertTrue(response["review_case_required"])
        self.assertEqual(
            response["review_case_id"],
            "CASE-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertTrue(response["evidence_package_ready"])

    def test_mobile_approval_rejected_blocks_operation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/sensitive-approval/evaluate",
            {
                "operation_type": "external_wallet_withdrawal",
                "actor_id": "customer-demo",
                "actor_type": "customer",
                "amount_eur": 100,
                "mobile_approval_status": "rejected",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["backend_risk_decision"], "blocked")
        self.assertEqual(
            response["audit_event_id"],
            "AUD-APPROVAL-MOBILE-REJECTED",
        )

    def test_high_value_approval_evidence_package_and_review_case(self) -> None:
        package_status, package_response = request_json(
            "POST",
            "/api/evidence-packages/generate",
            {
                "source_type": "audit_event",
                "source_id": "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
                "package_type": "internal_review",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(package_status, 200)
        self.assertEqual(
            package_response["package"]["package_id"],
            "EP-FROM-AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertEqual(
            package_response["correlation_id"],
            "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertIn(
            "Sensitive Approval",
            package_response["package"]["title"],
        )

        case_status, case_response = request_json(
            "POST",
            "/api/review-cases/create-from-evidence-package",
            {
                "package_id": "EP-FROM-AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
                "source_audit_event_id": "AUD-APPROVAL-HIGH-VALUE-NEW-WALLET",
                "correlation_id": "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET",
                "reviewer_id": "reviewer-demo",
                "priority": "critical",
            },
        )

        self.assertEqual(case_status, 200)
        self.assertEqual(
            case_response["case_id"],
            "CASE-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
        self.assertEqual(case_response["case_type"], "sensitive_approval_review")
        self.assertEqual(
            case_response["correlation_id"],
            "CORR-APPROVAL-HIGH-VALUE-NEW-WALLET",
        )
