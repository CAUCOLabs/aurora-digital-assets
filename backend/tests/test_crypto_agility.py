import unittest

from tests.helpers import request_json


CRYPTO_AGILITY_PQ_PAYLOAD = {
    "scenario_id": "crypto_agility_post_quantum_readiness_gap",
    "deprecated_algorithm_detected": True,
    "long_lived_key_detected": True,
    "missing_algorithm_versioning": True,
    "missing_key_rotation_policy": True,
    "backup_long_term_risk": True,
    "audit_integrity_gap": True,
    "custody_key_rotation_gap": True,
    "blockchain_protocol_confusion": True,
    "post_quantum_readiness_gap": True,
    "kms_hsm_integration_missing": True,
}


class CryptoAgilityTests(unittest.TestCase):
    def test_crypto_agility_reference_endpoints(self) -> None:
        for path in [
            "/api/crypto-agility/assets",
            "/api/crypto-agility/policies",
            "/api/crypto-agility/key-lifecycle",
            "/api/crypto-agility/scenarios",
        ]:
            status, response = request_json("GET", path)

            self.assertEqual(status, 200)
            self.assertTrue(response)

    def test_post_quantum_readiness_gap_evaluation(self) -> None:
        status, response = request_json(
            "POST",
            "/api/crypto-agility/evaluate-scenario",
            CRYPTO_AGILITY_PQ_PAYLOAD,
        )

        self.assertEqual(status, 200)
        self.assertEqual(response["risk_score"], 100)
        self.assertEqual(response["decision"], "escalate")
        self.assertEqual(response["severity"], "critical")
        self.assertTrue(response["audit_event_created"])
        self.assertEqual(
            response["audit_event_id"],
            "AUD-CRYPTO-AGILITY-PQ-READINESS",
        )
        self.assertEqual(
            response["correlation_id"],
            "CORR-CRYPTO-AGILITY-PQ-READINESS",
        )
        self.assertTrue(response["evidence_package_ready"])
        self.assertTrue(response["affected_domains"])
        self.assertIn("No custom cryptography", response["triggered_controls"])
