import json
import unittest

from tests.helpers import request_json


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


class AgentActionsReviewCaseTests(unittest.TestCase):
    def test_blocked_secret_access_evidence_package_creates_review_case(
        self,
    ) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        self.assertEqual(response["case_type"], "agent_action_review")
        self.assertEqual(response["source_module"], "agent_actions")
        self.assertEqual(response["priority"], "critical")
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["status"], "open")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )
        self.assertIn(
            "confirm_no_secrets_were_exposed",
            response["recommended_actions"],
        )
        self.assertIn(
            "verify_agent_identity_and_passport",
            response["recommended_actions"],
        )

    def test_suspended_custodian_agent_api_attempt_creates_review_case(
        self,
    ) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
            "AUD-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
            "CORR-AGENT-CUSTODIAN-INTEGRATION-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-AGENT-ACTION-CUSTODIAN-INTEGRATION-001-ATTEMPT-CUSTODIAN-API-ACCESS",
        )
        self.assertEqual(response["case_type"], "agent_action_review")
        self.assertEqual(response["source_module"], "agent_actions")
        self.assertEqual(response["priority"], "critical")
        self.assertEqual(response["severity"], "critical")
        self.assertEqual(response["status"], "open")
        self.assertEqual(
            response["assigned_team"],
            "Risk Operations / Security Architecture",
        )
        self.assertIn(
            "confirm_no_real_custodian_api_call_occurred",
            response["recommended_actions"],
        )
        self.assertIn(
            "keep_custodian_integration_blocked",
            response["recommended_actions"],
        )
        self.assertIn(
            "review_agent_status_and_scope",
            response["recommended_actions"],
        )

    def test_withdrawal_approval_attempt_creates_review_case(self) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-RISK-ANALYST-001-ATTEMPT-WITHDRAWAL-APPROVAL",
            "AUD-AGENT-ACTION-RISK-ANALYST-001-ATTEMPT-WITHDRAWAL-APPROVAL",
            "CORR-AGENT-RISK-ANALYST-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["case_id"],
            "CASE-AGENT-ACTION-RISK-ANALYST-001-ATTEMPT-WITHDRAWAL-APPROVAL",
        )
        self.assertEqual(response["case_type"], "agent_action_review")
        self.assertEqual(response["source_module"], "agent_actions")
        self.assertEqual(response["severity"], "critical")
        self.assertIn(
            "confirm_no_withdrawal_execution_occurred",
            response["recommended_actions"],
        )
        self.assertIn(
            "keep_sensitive_operation_blocked",
            response["recommended_actions"],
        )

    def test_lower_risk_read_audit_event_creates_governance_review_case(
        self,
    ) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-READ-AUDIT-EVENT",
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
            priority="medium",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_type"], "agent_action_review")
        self.assertEqual(response["source_module"], "agent_actions")
        self.assertIn(response["severity"], ["low", "medium"])
        self.assertEqual(response["status"], "open")
        self.assertIn(
            "preserve_agent_action_audit_trail",
            response["recommended_actions"],
        )

    def test_unknown_agent_action_evidence_package_is_deterministic(
        self,
    ) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-UNKNOWN-AGENT-ATTEMPT-SECRET-ACCESS",
            "AUD-AGENT-ACTION-UNKNOWN-AGENT-ATTEMPT-SECRET-ACCESS",
            "CORR-AGENT-UNKNOWN-AGENT",
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["case_type"], "agent_action_review")
        self.assertEqual(response["source_module"], "agent_actions")
        self.assertEqual(
            response["case_id"],
            "CASE-AGENT-ACTION-UNKNOWN-AGENT-ATTEMPT-SECRET-ACCESS",
        )
        response_text = json.dumps(response).lower()
        for disallowed_text in (
            "private key",
            "seed phrase",
            "api key",
            "token",
            "password",
            "credential value",
        ):
            with self.subTest(disallowed_text=disallowed_text):
                self.assertNotIn(disallowed_text, response_text)

    def test_agent_action_review_case_response_links_traceability(
        self,
    ) -> None:
        status, response = create_review_case(
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
            "CORR-AGENT-COMPLIANCE-ASSISTANT-001",
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["linked_evidence_package"],
            "EP-FROM-AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        self.assertEqual(
            response["linked_audit_event"],
            "AUD-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-REVIEW-FROM-EP-AGENT-ACTION-COMPLIANCE-ASSISTANT-001-ATTEMPT-SECRET-ACCESS",
        )
        traceability = response["traceability_summary"].lower()
        self.assertIn("metadata-only", traceability)
        self.assertIn("no real action was executed", traceability)
        self.assertIn("no external api was called", traceability)


if __name__ == "__main__":
    unittest.main()
