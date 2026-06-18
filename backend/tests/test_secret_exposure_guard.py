import unittest

from tests.helpers import request_json


class SecretExposureGuardTests(unittest.TestCase):
    def test_surfaces_catalog_includes_required_surfaces(self) -> None:
        status, response = request_json(
            "GET",
            "/api/secret-exposure-guard/surfaces",
        )

        self.assertEqual(status, 200)
        surface_ids = {surface["surface_id"] for surface in response}
        self.assertIn("CONFIG-ENV", surface_ids)
        self.assertIn("PROMPTS-AI-WORKFLOW", surface_ids)
        self.assertIn("EVIDENCE-PACKAGES", surface_ids)

    def test_signals_catalog_includes_required_signal_types(self) -> None:
        status, response = request_json(
            "GET",
            "/api/secret-exposure-guard/signals",
        )

        self.assertEqual(status, 200)
        self.assertIn("possible_secret_in_prompt_context", response)
        self.assertIn("possible_secret_in_config", response)
        self.assertIn("possible_custodian_secret_reference", response)

    def test_prompt_context_signal_creates_safe_escalation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/secret-exposure-guard/evaluate",
            {
                "signal_type": "possible_secret_in_prompt_context",
                "surface_id": "PROMPTS-AI-WORKFLOW",
                "source_reference": "internal-ai-workflow-note",
                "contains_secret_like_pattern": True,
                "contains_api_token_reference": True,
                "exposure_scope": "prompt_context",
                "ai_assisted_context": True,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(response["severity"], {"high", "critical"})
        self.assertIn(
            response["decision"],
            {"review_required", "block", "elevate"},
        )
        self.assertFalse(response["secret_value_stored"])
        self.assertFalse(response["raw_secret_echoed"])
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-SECRET-GUARD-PROMPT-CONTEXT",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-PROMPT-CONTEXT",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertIn(
            "preserve_evidence_without_secret_value",
            response["recommended_next_actions"],
        )

    def test_config_signal_with_raw_secret_metadata_blocks_safely(self) -> None:
        status, response = request_json(
            "POST",
            "/api/secret-exposure-guard/evaluate",
            {
                "signal_type": "possible_secret_in_config",
                "surface_id": "CONFIG-ENV",
                "source_reference": "local-env-file",
                "contains_raw_secret_value": True,
                "contains_credential_label": True,
                "contains_api_token_reference": True,
                "exposure_scope": "repository",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["severity"], "critical")
        self.assertIn(response["decision"], {"block", "review_required"})
        self.assertFalse(response["secret_value_stored"])
        self.assertFalse(response["raw_secret_echoed"])
        self.assertEqual(response["audit_event_id"], "AUD-SECRET-GUARD-CONFIG")
        self.assertEqual(
            response["correlation_id"],
            "CORR-SECRET-GUARD-CONFIG",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])
        self.assertTrue(response["operation_guard_recommended"])

    def test_custodian_signal_links_to_ai_threat_secret_exposure_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/secret-exposure-guard/evaluate",
            {
                "signal_type": "possible_custodian_secret_reference",
                "surface_id": "FUTURE-CUSTODIAN-SECRETS",
                "contains_custodian_secret_reference": True,
                "exposure_scope": "internal",
                "ai_assisted_context": True,
                "linked_ai_threat_case_id": "CASE-AI-THREAT-SECRET-EXPOSURE",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["severity"], "critical")
        self.assertFalse(response["secret_value_stored"])
        self.assertFalse(response["raw_secret_echoed"])
        self.assertEqual(
            response["ai_threat_case_id"],
            "CASE-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertEqual(
            response["review_case_id"],
            "CASE-AI-THREAT-SECRET-EXPOSURE",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["review_case_required"])

    def test_low_risk_documentation_signal_does_not_create_review_case(self) -> None:
        status, response = request_json(
            "POST",
            "/api/secret-exposure-guard/evaluate",
            {
                "signal_type": "possible_secret_in_documentation",
                "surface_id": "DOCS-README",
                "source_reference": "public-safe-documentation-check",
                "exposure_scope": "unknown",
            },
        )

        self.assertEqual(status, 200)
        self.assertFalse(response["secret_value_stored"])
        self.assertFalse(response["raw_secret_echoed"])
        self.assertIn(response["decision"], {"allow", "redact"})
        self.assertFalse(response["review_case_required"])
