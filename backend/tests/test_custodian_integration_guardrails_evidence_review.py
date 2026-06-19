import json
import unittest

from tests.helpers import request_json


def generate_evidence(audit_event_id: str) -> tuple[int, dict]:
    return request_json(
        "POST",
        "/api/evidence-packages/generate",
        {
            "source_type": "audit_event",
            "source_id": audit_event_id,
            "package_type": "internal_review",
            "reviewer_id": "reviewer-demo",
        },
    )


def create_review_case(
    package_id: str,
    audit_event_id: str,
    correlation_id: str,
    priority: str = "critical",
) -> tuple[int, dict]:
    return request_json(
        "POST",
        "/api/review-cases/create-from-evidence-package",
        {
            "package_id": package_id,
            "source_audit_event_id": audit_event_id,
            "correlation_id": correlation_id,
            "reviewer_id": "reviewer-demo",
            "priority": priority,
        },
    )


class CustodianIntegrationGuardrailsEvidenceReviewTests(unittest.TestCase):
    def test_key_management_boundary_gap_generates_evidence_package(self) -> None:
        status, response = generate_evidence(
            "AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )

        self.assertEqual(status, 200)
        package = response["package"]
        self.assertEqual(
            package["package_id"],
            "EP-FROM-AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(
            package["source_module"],
            "custodian_integration_guardrails",
        )
        self.assertEqual(package["severity"], "critical")
        self.assertEqual(
            response["correlation_id"],
            "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(
            package["audit_context"]["review_case_id"]
            if "review_case_id" in package["audit_context"]
            else "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
            "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertIn(
            "future regulated custodian integration guardrail",
            json.dumps(response["evidence_items"]).lower(),
        )

        evidence_text = json.dumps(response["evidence_items"]).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "token",
            "password",
            "api key",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, evidence_text)

    def test_key_management_boundary_gap_creates_review_case(self) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
            "AUD-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
            "CORR-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-CUSTODIAN-KEY-MANAGEMENT-BOUNDARY-GAP",
        )
        self.assertEqual(response["case_type"], "custodian_integration_review")
        self.assertEqual(
            response["source_module"],
            "custodian_integration_guardrails",
        )
        self.assertEqual(response["priority"], "critical")
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["status"], "open")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertIn(
            "block_future_custodian_integration_until_controls_are_verified",
            response["recommended_actions"],
        )
        self.assertIn(
            "define_key_management_boundary",
            response["recommended_actions"],
        )
        self.assertIn(
            "verify_no_private_keys_or_custody_secrets_are_stored",
            response["recommended_actions"],
        )
        self.assertIn(
            "require_security_architecture_approval",
            response["recommended_actions"],
        )
        self.assertIn("create_human_review_case", response["recommended_actions"])

    def test_asset_segregation_gap_generates_evidence_and_review_case(
        self,
    ) -> None:
        evidence_status, evidence_response = generate_evidence(
            "AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertEqual(evidence_status, 200)
        self.assertEqual(
            evidence_response["package"]["package_id"],
            "EP-FROM-AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )

        case_status, case_response = create_review_case(
            "EP-FROM-AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
            "AUD-CUSTODIAN-ASSET-SEGREGATION-GAP",
            "CORR-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertEqual(case_status, 200)
        self.assertEqual(
            case_response["case_id"],
            "CASE-CUSTODIAN-ASSET-SEGREGATION-GAP",
        )
        self.assertEqual(
            case_response["case_type"],
            "custodian_integration_review",
        )
        self.assertIn(case_response["severity"], ["critical", "high"])

    def test_active_secret_guard_case_generates_evidence_and_review_case(
        self,
    ) -> None:
        evidence_status, evidence_response = generate_evidence(
            "AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(evidence_status, 200)
        self.assertEqual(
            evidence_response["package"]["package_id"],
            "EP-FROM-AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(
            evidence_response["package"]["correlation_id"],
            "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )

        case_status, case_response = create_review_case(
            "EP-FROM-AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
            "AUD-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
            "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(case_status, 200)
        self.assertEqual(
            case_response["case_id"],
            "CASE-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        self.assertEqual(
            case_response["case_type"],
            "custodian_integration_review",
        )
        self.assertEqual(
            case_response["source_module"],
            "custodian_integration_guardrails",
        )
        self.assertEqual(
            case_response["correlation_id"],
            "CORR-CUSTODIAN-ACTIVE-SECRET-GUARD-CASE",
        )
        actions = " ".join(case_response["recommended_actions"])
        self.assertIn(
            "verify_ai_threat_secret_guard_and_cloud_cases_are_mitigated_or_closed",
            actions,
        )

    def test_unknown_custodian_audit_event_uses_generic_package(self) -> None:
        status, response = generate_evidence(
            "AUD-CUSTODIAN-NOT-MAPPED-DEMO",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["package"]["package_id"],
            "EP-FROM-AUD-CUSTODIAN-NOT-MAPPED-DEMO",
        )
        self.assertEqual(response["package"]["source_module"], "audit_events")
