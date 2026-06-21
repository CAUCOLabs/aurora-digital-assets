import unittest

from tests.helpers import request_json


STRONG_GOVERNANCE_CONTROLS = {
    "agents_have_unique_identity": True,
    "agents_have_human_accountable_owner": True,
    "agents_have_passport": True,
    "passports_are_status_checked": True,
    "passports_can_block_agents": True,
    "permissions_are_explicit": True,
    "permissions_are_deny_by_default": True,
    "actions_are_audited": True,
    "blocked_actions_are_audited": True,
    "evidence_packages_link_to_agent_actions": True,
    "review_cases_link_to_agent_evidence": True,
    "review_lifecycle_available": True,
    "revocation_evaluation_available": True,
    "sensitive_action_guard_available": True,
    "policy_engine_available": True,
    "abuse_detection_available": True,
    "no_raw_secret_storage_policy": True,
    "no_real_execution_policy": True,
    "no_real_custodian_access_policy": True,
    "no_real_blockchain_execution_policy": True,
    "no_real_cloud_deployment_policy": True,
    "emergency_override_cannot_bypass_safety": True,
    "audit_event_ids_deterministic": True,
    "correlation_ids_deterministic": True,
    "human_review_required_for_critical_actions": True,
    "evidence_required_for_high_and_critical_actions": True,
    "external_partner_readiness_available": True,
    "custodian_guardrails_available": True,
    "cloud_kubernetes_guardrails_available": True,
    "secret_exposure_guard_available": True,
    "ai_threat_defense_available": True,
    "sensitive_approval_guard_available": True,
    "production_requires_additional_controls": True,
}


class AgentIdentityGovernanceTests(unittest.TestCase):
    def test_framework_describes_scope_and_safety_boundaries(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-identity-governance/framework",
        )

        self.assertEqual(status, 200)
        self.assertIn(
            "production-grade agent identity governance readiness",
            response["purpose"],
        )
        self.assertIn(
            "no real production deployment",
            response["safety_boundaries"],
        )
        self.assertIn("agent_registry", response["linked_modules"])
        self.assertIn("agent_passports", response["linked_modules"])
        self.assertIn("agent_permissions", response["linked_modules"])
        self.assertIn("agent_policy_engine", response["linked_modules"])
        self.assertIn("agent_abuse_detection", response["linked_modules"])

    def test_control_domains_include_governance_stack(self) -> None:
        status, response = request_json(
            "GET",
            "/api/agent-identity-governance/control-domains",
        )

        self.assertEqual(status, 200)
        domains = {item["domain_id"] for item in response}
        self.assertIn("identity_registration", domains)
        self.assertIn("passport_governance", domains)
        self.assertIn("permission_governance", domains)
        self.assertIn("policy_engine_governance", domains)
        self.assertIn("abuse_detection_governance", domains)
        self.assertIn("production_safety_boundary", domains)

    def test_evaluates_strong_governance_posture(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-identity-governance/evaluate",
            {
                "assessment_id": "AGENT-PRODUCTION-READINESS-001",
                "environment": "local",
                "target_environment": "future_production",
                "controls": STRONG_GOVERNANCE_CONTROLS,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertIn(
            response["governance_decision"],
            [
                "production_governance_ready_for_internal_review",
                "production_governance_ready_with_conditions",
            ],
        )
        self.assertGreaterEqual(response["governance_score"], 85)
        self.assertEqual(response["governance_level"], "high")
        self.assertFalse(response["production_access_blocked"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-AGENT-IDENTITY-GOVERNANCE-AGENT-PRODUCTION-READINESS-001",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-AGENT-IDENTITY-GOVERNANCE-AGENT-PRODUCTION-READINESS-001",
        )

    def test_blocks_missing_no_real_execution_policy(self) -> None:
        controls = dict(STRONG_GOVERNANCE_CONTROLS)
        controls["no_real_execution_policy"] = False

        status, response = request_json(
            "POST",
            "/api/agent-identity-governance/evaluate",
            {
                "assessment_id": "AGENT-GOVERNANCE-BLOCKED-001",
                "controls": controls,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["governance_decision"],
            "production_governance_blocked",
        )
        self.assertTrue(response["production_access_blocked"])
        self.assertTrue(response["sensitive_operations_blocked"])
        self.assertIn("no_real_execution_policy", response["failed_controls"])
        self.assertIn("no secrets stored or exposed", response["safety_notice"].lower())

    def test_linked_revocation_blocks_production_governance(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-identity-governance/evaluate-production-readiness",
            {
                "assessment_id": "AGENT-PRODUCTION-READINESS-REVOCATION-001",
                "controls": STRONG_GOVERNANCE_CONTROLS,
                "linked_revocation_audit_event_id": "AUD-AGENT-REVOCATION-001",
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["governance_decision"],
            "production_governance_blocked",
        )
        self.assertTrue(response["production_access_blocked"])
        self.assertTrue(response["external_access_blocked"])
        self.assertIn(
            "review_agent_revocation_context",
            response["recommended_next_actions"],
        )

    def test_generates_audit_safe_governance_summary(self) -> None:
        status, response = request_json(
            "POST",
            "/api/agent-identity-governance/generate-governance-summary",
            {
                "assessment_id": "AGENT-GOVERNANCE-SUMMARY-001",
                "governance_decision": (
                    "production_governance_requires_remediation"
                ),
                "governance_score": 61,
                "governance_level": "low",
                "critical_blockers": ["policy_engine_available"],
                "missing_controls": ["audit_export_readiness"],
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertTrue(response["audit_safe"])
        self.assertTrue(response["no_secret_material_included"])
        self.assertIn("policy_engine_available", response["critical_blockers"])
        self.assertIn("audit_export_readiness", response["missing_controls"])
        self.assertIn(
            "not a legal or regulatory certification",
            response["safety_notice"],
        )


if __name__ == "__main__":
    unittest.main()
