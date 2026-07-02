import unittest

from tests.helpers import request_json


COMPLETE_CONTROLS = {
    "asset_classification_confirmed": True,
    "settlement_rail_confirmed": True,
    "custody_model_confirmed": True,
    "issuer_governance_defined": True,
    "redemption_model_defined": True,
    "reserve_model_defined": True,
    "psp_intermediation_defined": True,
    "bank_ledger_controls_defined": True,
    "custodian_readiness_completed": True,
    "private_key_boundary_defined": True,
    "blockchain_execution_boundary_defined": True,
    "securities_controls_defined": True,
    "holding_limits_defined": True,
    "offline_online_mode_defined": True,
    "privacy_controls_defined": True,
    "aml_controls_defined": True,
    "evidence_review_defined": True,
    "human_approval_integrity_required": True,
    "agent_governance_required": True,
    "operational_resilience_defined": True,
    "regulatory_disclaimer_present": True,
}


class AssetRailGovernanceTests(unittest.TestCase):
    def test_lists_asset_and_rail_types(self) -> None:
        status, asset_types = request_json(
            "GET",
            "/api/asset-rail-governance/asset-types",
        )
        self.assertEqual(status, 200)
        self.assertIn(
            "digital_euro_cbdc",
            {item["type_id"] for item in asset_types},
        )
        self.assertIn(
            "cryptoasset",
            {item["type_id"] for item in asset_types},
        )

        status, rail_types = request_json(
            "GET",
            "/api/asset-rail-governance/rail-types",
        )
        self.assertEqual(status, 200)
        self.assertIn(
            "central_bank_money_rail",
            {item["type_id"] for item in rail_types},
        )
        self.assertIn(
            "external_crypto_custody_rail",
            {item["type_id"] for item in rail_types},
        )

    def test_control_matrix_separates_digital_euro_from_crypto_custody(self) -> None:
        status, response = request_json(
            "GET",
            "/api/asset-rail-governance/control-matrix",
        )

        self.assertEqual(status, 200)
        matrix = {item["asset_type"]: item for item in response}
        self.assertEqual(
            matrix["digital_euro_cbdc"]["default_rail_type"],
            "central_bank_money_rail",
        )
        self.assertIn(
            "psp_intermediation",
            matrix["digital_euro_cbdc"]["required_control_domains"],
        )
        self.assertIn(
            "external_custodian_controls_required",
            matrix["cryptoasset"]["control_decisions"],
        )

    def test_classifies_digital_euro_as_central_bank_money_without_custodian(self) -> None:
        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/classify",
            {
                "asset_symbol": "EUR-DIGITAL",
                "asset_name": "Digital Euro Prototype",
                "declared_asset_type": "digital_euro_cbdc",
                "is_central_bank_money": True,
                "distributed_by_psp": True,
                "holding_limits_required": True,
                "privacy_controls_required": True,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["asset_type"], "digital_euro_cbdc")
        self.assertEqual(response["rail_type"], "psp_intermediated_payment_rail")
        self.assertTrue(response["psp_intermediation_required"])
        self.assertFalse(response["external_custodian_required"])
        self.assertFalse(response["blockchain_execution_required"])
        self.assertIn("psp_intermediation", response["required_controls"])
        self.assertIn("No real digital euro integration", response["safety_notice"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-ASSET-RAIL-CLASSIFICATION-EUR-DIGITAL",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-ASSET-RAIL-EUR-DIGITAL",
        )

    def test_classifies_cryptoasset_with_custodian_and_blockchain_boundaries(self) -> None:
        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/classify",
            {
                "asset_symbol": "BTC",
                "declared_asset_type": "cryptoasset",
                "is_cryptoasset": True,
                "uses_external_custodian": True,
                "uses_blockchain_execution": True,
                "uses_private_keys": True,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["asset_type"], "cryptoasset")
        self.assertEqual(response["rail_type"], "external_crypto_custody_rail")
        self.assertTrue(response["external_custodian_required"])
        self.assertTrue(response["blockchain_execution_required"])
        self.assertIn("private_key_boundary", response["required_controls"])
        self.assertIn(
            "blockchain_execution_controls_required",
            response["control_decisions"],
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-ASSET-RAIL-CLASSIFICATION-BTC",
        )

    def test_blocks_digital_euro_external_custody_contradiction(self) -> None:
        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/evaluate-controls",
            {
                "asset_symbol": "EUR-DIGITAL",
                "asset_type": "digital_euro_cbdc",
                "rail_type": "external_crypto_custody_rail",
                "controls": COMPLETE_CONTROLS,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["governance_decision"],
            "asset_rail_governance_blocked",
        )
        self.assertIn(
            "digital_euro_external_custodian_contradiction",
            response["blocking_reasons"],
        )
        self.assertEqual(
            response["audit_event_id"],
            "AUD-ASSET-RAIL-CONTROLS-EUR-DIGITAL",
        )

    def test_evaluates_stablecoin_missing_issuer_controls_as_remediation(self) -> None:
        controls = dict(COMPLETE_CONTROLS)
        controls["issuer_governance_defined"] = False

        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/evaluate-controls",
            {
                "asset_symbol": "EURS",
                "asset_type": "regulated_stablecoin_emt",
                "rail_type": "regulated_stablecoin_issuer_rail",
                "controls": controls,
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["governance_decision"],
            "asset_rail_governance_requires_remediation",
        )
        self.assertLess(response["governance_score"], 85)
        self.assertIn("issuer_governance", response["missing_controls"])
        self.assertIn("stablecoin_without_issuer_governance", response["blocking_reasons"])
        self.assertTrue(response["issuer_controls_required"])
        self.assertTrue(response["redemption_controls_required"])
        self.assertTrue(response["reserve_controls_required"])

    def test_unknown_asset_is_blocked_pending_classification(self) -> None:
        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/classify",
            {
                "asset_symbol": "mystery asset",
                "asset_name": "Unknown Digital Asset",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["asset_symbol"], "MYSTERY-ASSET")
        self.assertEqual(response["asset_type"], "unknown_digital_asset")
        self.assertEqual(response["rail_type"], "unknown_or_unverified_rail")
        self.assertTrue(response["evidence_required"])
        self.assertTrue(response["review_required"])
        self.assertIn(
            "unknown_asset_blocked_pending_classification",
            response["control_decisions"],
        )

    def test_governance_summary_is_audit_safe(self) -> None:
        status, response = request_json(
            "POST",
            "/api/asset-rail-governance/governance-summary",
            {
                "asset_symbol": "BTC",
                "asset_type": "cryptoasset",
                "rail_type": "external_crypto_custody_rail",
                "governance_decision": "asset_rail_governance_requires_remediation",
                "governance_score": 70,
                "reviewer_id": "reviewer-demo",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["summary_id"], "SUMMARY-ASSET-RAIL-BTC")
        self.assertEqual(response["asset_type"], "cryptoasset")
        self.assertIn("remediate_missing_controls", response["required_next_steps"])
        self.assertIn(
            "not legal advice or regulatory certification",
            response["safety_notice"],
        )


if __name__ == "__main__":
    unittest.main()
