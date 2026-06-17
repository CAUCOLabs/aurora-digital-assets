from app.schemas.crypto_agility import (
    CryptoAgilityScenario,
    CryptoAlgorithmPolicy,
    CryptoAsset,
    CryptoKeyLifecycleItem,
    EvaluateCryptoAgilityScenarioResponse,
)
from app.services.audit_service import audit_service


CRYPTO_AGILITY_CONTROLS = [
    "Cryptographic inventory required",
    "Algorithm versioning required",
    "Key rotation policy required",
    "Long-term confidentiality classification required",
    "No custom cryptography",
    "KMS/HSM/Key Vault integration required",
    "Audit evidence required for key lifecycle events",
    "Blockchain protocol separation required",
    "Post-quantum readiness monitored",
]


class CryptoAgilityService:
    """Provides deterministic cryptographic agility control center data."""

    def list_assets(self) -> list[CryptoAsset]:
        return [
            CryptoAsset(
                asset_id="CRYPTO-ASSET-TLS-001",
                name="TLS / HTTPS Certificates",
                domain="tls",
                owner="Platform Security",
                data_classification="internal",
                current_algorithm="RSA-2048 / ECDSA-P256 simulated",
                algorithm_family="certificate",
                algorithm_version="tls-policy-v1",
                key_location="cloud_secret_manager",
                rotation_period_days=365,
                last_rotated_at="2026-01-15T09:00:00+03:00",
                next_rotation_due="2027-01-15T09:00:00+03:00",
                long_term_confidentiality_required=False,
                harvest_now_decrypt_later_risk="low",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="Certificate inventory and renewal posture are simulated.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-SESSION-001",
                name="Session Token Signing",
                domain="session_tokens",
                owner="Identity Engineering",
                data_classification="confidential",
                current_algorithm="HS256 / RS256 simulated policy",
                algorithm_family="signature",
                algorithm_version="token-policy-v1",
                key_location="application_config",
                rotation_period_days=90,
                last_rotated_at="2026-03-01T10:00:00+03:00",
                next_rotation_due="2026-05-30T10:00:00+03:00",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="medium",
                migration_readiness="gap_detected",
                blockchain_protocol_dependency=False,
                notes="Demo policy highlights missing production key governance.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-APIKEY-001",
                name="API Key Lifecycle",
                domain="api_keys",
                owner="API Security",
                data_classification="confidential",
                current_algorithm="opaque-token-policy",
                algorithm_family="symmetric",
                algorithm_version="api-key-policy-v1",
                key_location="cloud_secret_manager",
                rotation_period_days=90,
                last_rotated_at="2026-04-10T12:00:00+03:00",
                next_rotation_due="2026-07-09T12:00:00+03:00",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="medium",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="Opaque token lifecycle is architectural only.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-DB-001",
                name="Database Encryption",
                domain="database_encryption",
                owner="Data Platform",
                data_classification="regulated",
                current_algorithm="AES-256 simulated policy",
                algorithm_family="symmetric",
                algorithm_version="db-encryption-policy-v1",
                key_location="key_vault",
                rotation_period_days=180,
                last_rotated_at="2026-01-20T08:30:00+03:00",
                next_rotation_due="2026-07-19T08:30:00+03:00",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="high",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="No real database encryption operation is performed.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-BACKUP-001",
                name="Backup Encryption",
                domain="backup_encryption",
                owner="Resilience Engineering",
                data_classification="critical",
                current_algorithm="AES-256 simulated policy",
                algorithm_family="symmetric",
                algorithm_version="backup-encryption-policy-v1",
                key_location="key_vault",
                rotation_period_days=180,
                last_rotated_at="2025-12-12T08:00:00+03:00",
                next_rotation_due="2026-06-10T08:00:00+03:00",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="critical",
                migration_readiness="gap_detected",
                blockchain_protocol_dependency=False,
                notes="Long-lived backup confidentiality is the primary risk.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-AUDIT-001",
                name="Audit Log Integrity",
                domain="audit_integrity",
                owner="Audit Engineering",
                data_classification="regulated",
                current_algorithm="HMAC / signing-policy simulated",
                algorithm_family="hash",
                algorithm_version="audit-integrity-policy-v1",
                key_location="simulated",
                rotation_period_days=180,
                last_rotated_at="2026-02-01T08:00:00+03:00",
                next_rotation_due="2026-07-31T08:00:00+03:00",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="high",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="Tamper-evidence and long-term verification are modeled.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-WALLET-001",
                name="Wallet Key Boundary",
                domain="wallet_keys",
                owner="Digital Assets Architecture",
                data_classification="critical",
                current_algorithm="external-blockchain-signature-policy",
                algorithm_family="external_blockchain",
                algorithm_version="wallet-boundary-policy-v1",
                key_location="external_provider",
                rotation_period_days=0,
                last_rotated_at="not_applicable",
                next_rotation_due="not_applicable",
                long_term_confidentiality_required=False,
                harvest_now_decrypt_later_risk="medium",
                migration_readiness="not_assessed",
                blockchain_protocol_dependency=True,
                notes=(
                    "Aurora must separate its platform cryptography from "
                    "external blockchain protocol cryptography."
                ),
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-CUSTODY-001",
                name="Custody Key Governance",
                domain="custody_keys",
                owner="Custody Governance",
                data_classification="critical",
                current_algorithm="external-custody-policy",
                algorithm_family="custody",
                algorithm_version="custody-governance-policy-v1",
                key_location="external_provider",
                rotation_period_days=0,
                last_rotated_at="not_assessed",
                next_rotation_due="not_assessed",
                long_term_confidentiality_required=True,
                harvest_now_decrypt_later_risk="critical",
                migration_readiness="not_assessed",
                blockchain_protocol_dependency=True,
                notes="Custody internals are represented as external provider boundaries.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-MTLS-001",
                name="Microservice Communication",
                domain="microservice_communication",
                owner="Platform Engineering",
                data_classification="internal",
                current_algorithm="mTLS certificate policy simulated",
                algorithm_family="certificate",
                algorithm_version="mtls-policy-v1",
                key_location="cloud_secret_manager",
                rotation_period_days=180,
                last_rotated_at="2026-02-15T09:00:00+03:00",
                next_rotation_due="2026-08-14T09:00:00+03:00",
                long_term_confidentiality_required=False,
                harvest_now_decrypt_later_risk="low",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="Service-to-service certificate posture is simulated.",
            ),
            CryptoAsset(
                asset_id="CRYPTO-ASSET-CLOUDCERT-001",
                name="Cloud Certificates",
                domain="cloud_certificates",
                owner="Cloud Platform",
                data_classification="internal",
                current_algorithm="cloud-managed-certificate-policy",
                algorithm_family="certificate",
                algorithm_version="cloud-cert-policy-v1",
                key_location="cloud_secret_manager",
                rotation_period_days=365,
                last_rotated_at="2026-01-10T08:00:00+03:00",
                next_rotation_due="2027-01-10T08:00:00+03:00",
                long_term_confidentiality_required=False,
                harvest_now_decrypt_later_risk="low",
                migration_readiness="partial",
                blockchain_protocol_dependency=False,
                notes="Cloud certificate governance is represented as policy data.",
            ),
        ]

    def list_policies(self) -> list[CryptoAlgorithmPolicy]:
        return [
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-INVENTORY",
                algorithm_family="certificate",
                approved_current=["TLS certificate policy", "mTLS certificate policy"],
                deprecated=["unversioned certificate inventory"],
                migration_candidates=["standards-based certificate agility plan"],
                status="active",
                reason="Algorithm inventory is required before safe migration.",
                crypto_owner="Platform Security",
                evidence_outputs=["Cryptographic inventory snapshot"],
            ),
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-VERSIONING",
                algorithm_family="signature",
                approved_current=["versioned signing policy"],
                deprecated=["unversioned signing configuration"],
                migration_candidates=["algorithm abstraction with policy versions"],
                status="migration_required",
                reason="Token and signature policies must be versioned.",
                crypto_owner="Identity Engineering",
                evidence_outputs=["Algorithm version map"],
            ),
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-KEY-ROTATION",
                algorithm_family="symmetric",
                approved_current=["documented key rotation policy"],
                deprecated=["long-lived unrotated keys"],
                migration_candidates=["KMS/HSM/Key Vault governed rotation"],
                status="migration_required",
                reason="Sensitive keys need rotation and emergency rollover evidence.",
                crypto_owner="Cryptographic Governance",
                evidence_outputs=["Key lifecycle and rotation posture"],
            ),
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-LONG-TERM-CONFIDENTIALITY",
                algorithm_family="symmetric",
                approved_current=["long-term confidentiality classification"],
                deprecated=["unclassified backup retention"],
                migration_candidates=["backup confidentiality migration roadmap"],
                status="monitored",
                reason="Backups and regulated data may remain sensitive for years.",
                crypto_owner="Data Protection",
                evidence_outputs=["Long-term confidentiality risk classification"],
            ),
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-NO-CUSTOM-CRYPTO",
                algorithm_family="hash",
                approved_current=["standards-based approved libraries only"],
                deprecated=["custom cryptographic primitives"],
                migration_candidates=["approved provider abstraction"],
                status="active",
                reason="Aurora must not invent cryptographic algorithms.",
                crypto_owner="Security Architecture",
                evidence_outputs=["Architecture decision record"],
            ),
            CryptoAlgorithmPolicy(
                policy_id="CRYPTO-POLICY-PQ-READINESS",
                algorithm_family="key_exchange",
                approved_current=["post-quantum readiness monitored"],
                deprecated=["quantum-proof marketing claims"],
                migration_candidates=["future standards-based migration plan"],
                status="monitored",
                reason="Readiness can be monitored without claiming quantum-proof security.",
                crypto_owner="Cryptographic Governance",
                evidence_outputs=["Post-quantum migration readiness assessment"],
            ),
        ]

    def list_key_lifecycle(self) -> list[CryptoKeyLifecycleItem]:
        return [
            CryptoKeyLifecycleItem(
                key_id="KEY-TLS-CERT-POLICY-001",
                asset_id="CRYPTO-ASSET-TLS-001",
                purpose="HTTPS certificate lifecycle",
                status="active",
                storage_boundary="cloud-managed certificate store",
                rotation_required=True,
                emergency_rollover_ready=True,
                audit_required=True,
                reviewer_note="Certificate rotation is tracked as simulated policy.",
            ),
            CryptoKeyLifecycleItem(
                key_id="KEY-SESSION-SIGNING-001",
                asset_id="CRYPTO-ASSET-SESSION-001",
                purpose="Session token signing policy",
                status="rotation_due",
                storage_boundary="application configuration boundary",
                rotation_required=True,
                emergency_rollover_ready=False,
                audit_required=True,
                reviewer_note="Production design should move to governed key storage.",
            ),
            CryptoKeyLifecycleItem(
                key_id="KEY-BACKUP-ENC-001",
                asset_id="CRYPTO-ASSET-BACKUP-001",
                purpose="Backup encryption policy",
                status="rotation_due",
                storage_boundary="key vault policy boundary",
                rotation_required=True,
                emergency_rollover_ready=False,
                audit_required=True,
                reviewer_note="Critical long-term confidentiality evidence is required.",
            ),
            CryptoKeyLifecycleItem(
                key_id="KEY-AUDIT-INTEGRITY-001",
                asset_id="CRYPTO-ASSET-AUDIT-001",
                purpose="Audit integrity policy",
                status="active",
                storage_boundary="simulated audit integrity boundary",
                rotation_required=True,
                emergency_rollover_ready=True,
                audit_required=True,
                reviewer_note="Long-term audit verification should be reviewed.",
            ),
            CryptoKeyLifecycleItem(
                key_id="KEY-CUSTODY-GOVERNANCE-001",
                asset_id="CRYPTO-ASSET-CUSTODY-001",
                purpose="External custody key governance evidence",
                status="deprecated",
                storage_boundary="external provider boundary",
                rotation_required=True,
                emergency_rollover_ready=False,
                audit_required=True,
                reviewer_note="Aurora needs evidence of provider governance and boundaries.",
            ),
        ]

    def list_scenarios(self) -> list[CryptoAgilityScenario]:
        return [
            self._scenario(
                "crypto_inventory_gap",
                "Cryptographic inventory gap",
                "Aurora cannot migrate cryptography safely if it does not know where cryptography is used.",
                ["CRYPTO-ASSET-TLS-001", "CRYPTO-ASSET-SESSION-001"],
                ["missing inventory", "unknown algorithm usage"],
                "review_required",
                ["Cryptographic inventory required"],
            ),
            self._scenario(
                "deprecated_algorithm_detected",
                "Deprecated algorithm detected",
                "An algorithm marked as deprecated is still used in a sensitive domain.",
                ["CRYPTO-ASSET-SESSION-001"],
                ["deprecated algorithm", "sensitive domain"],
                "migration_required",
                ["Algorithm versioning required", "No custom cryptography"],
            ),
            self._scenario(
                "long_lived_key_without_rotation",
                "Long-lived key without rotation",
                "A sensitive key exceeds its rotation window.",
                ["CRYPTO-ASSET-SESSION-001", "CRYPTO-ASSET-BACKUP-001"],
                ["long-lived key", "rotation overdue"],
                "harden_required",
                ["Key rotation policy required"],
            ),
            self._scenario(
                "backup_harvest_now_decrypt_later_risk",
                "Backup long-term confidentiality risk",
                "Long-lived backups may require stronger migration planning because data may remain sensitive for years.",
                ["CRYPTO-ASSET-BACKUP-001"],
                ["critical backup risk", "long-term confidentiality"],
                "migration_required",
                ["Long-term confidentiality classification required"],
            ),
            self._scenario(
                "audit_log_integrity_gap",
                "Audit log integrity gap",
                "Audit trails require tamper-evidence and long-term verification.",
                ["CRYPTO-ASSET-AUDIT-001"],
                ["integrity gap", "long-term verification"],
                "review_required",
                ["Audit evidence required for key lifecycle events"],
            ),
            self._scenario(
                "custody_key_rotation_gap",
                "Custody key rotation gap",
                "Custody-related key governance lacks migration and rotation evidence.",
                ["CRYPTO-ASSET-CUSTODY-001"],
                ["custody governance gap", "missing rotation evidence"],
                "escalate",
                ["KMS/HSM/Key Vault integration required"],
            ),
            self._scenario(
                "blockchain_protocol_confusion",
                "Platform crypto confused with blockchain crypto",
                "Aurora must separate platform cryptography from Bitcoin/Ethereum protocol cryptography.",
                ["CRYPTO-ASSET-WALLET-001", "CRYPTO-ASSET-CUSTODY-001"],
                ["blockchain protocol dependency", "boundary confusion"],
                "review_required",
                ["Blockchain protocol separation required"],
            ),
            self._scenario(
                "crypto_agility_post_quantum_readiness_gap",
                "Post-quantum migration readiness gap",
                "Aurora lacks inventory, abstraction, algorithm versioning, key lifecycle evidence, and migration planning.",
                [
                    "CRYPTO-ASSET-TLS-001",
                    "CRYPTO-ASSET-SESSION-001",
                    "CRYPTO-ASSET-APIKEY-001",
                    "CRYPTO-ASSET-DB-001",
                    "CRYPTO-ASSET-BACKUP-001",
                    "CRYPTO-ASSET-AUDIT-001",
                    "CRYPTO-ASSET-CUSTODY-001",
                    "CRYPTO-ASSET-CLOUDCERT-001",
                ],
                ["post-quantum readiness gap", "missing migration roadmap"],
                "escalate",
                CRYPTO_AGILITY_CONTROLS,
            ),
        ]

    def evaluate_scenario(
        self,
        *,
        scenario_id: str,
        deprecated_algorithm_detected: bool,
        long_lived_key_detected: bool,
        missing_algorithm_versioning: bool,
        missing_key_rotation_policy: bool,
        backup_long_term_risk: bool,
        audit_integrity_gap: bool,
        custody_key_rotation_gap: bool,
        blockchain_protocol_confusion: bool,
        post_quantum_readiness_gap: bool,
        kms_hsm_integration_missing: bool,
    ) -> EvaluateCryptoAgilityScenarioResponse:
        score = 10
        affected_domains: list[str] = []
        triggered_controls = ["Cryptographic inventory required", "No custom cryptography"]
        reasons = ["Baseline cryptographic agility inspection is active."]

        def add(condition: bool, points: int, domains: list[str], controls: list[str], reason: str) -> None:
            nonlocal score
            if not condition:
                return
            score += points
            affected_domains.extend(domains)
            triggered_controls.extend(controls)
            reasons.append(reason)

        add(
            deprecated_algorithm_detected,
            18,
            ["session_tokens", "api_keys"],
            ["Algorithm versioning required"],
            "A deprecated or unversioned algorithm policy was detected.",
        )
        add(
            long_lived_key_detected,
            15,
            ["database_encryption", "backup_encryption"],
            ["Key rotation policy required"],
            "A sensitive long-lived key exceeded its expected rotation posture.",
        )
        add(
            missing_algorithm_versioning,
            15,
            ["tls", "session_tokens", "cloud_certificates"],
            ["Algorithm versioning required"],
            "Algorithm versioning is missing for migration planning.",
        )
        add(
            missing_key_rotation_policy,
            15,
            ["api_keys", "session_tokens", "custody_keys"],
            ["Key rotation policy required"],
            "Key rotation policy evidence is missing.",
        )
        add(
            backup_long_term_risk,
            18,
            ["backup_encryption", "database_encryption"],
            ["Long-term confidentiality classification required"],
            "Long-term backup confidentiality risk is elevated.",
        )
        add(
            audit_integrity_gap,
            12,
            ["audit_integrity"],
            ["Audit evidence required for key lifecycle events"],
            "Audit integrity and long-term verification evidence is incomplete.",
        )
        add(
            custody_key_rotation_gap,
            16,
            ["custody_keys"],
            ["KMS/HSM/Key Vault integration required"],
            "Custody key governance and rotation evidence is incomplete.",
        )
        add(
            blockchain_protocol_confusion,
            10,
            ["custody_keys"],
            ["Blockchain protocol separation required"],
            "Platform cryptography was confused with blockchain protocol cryptography.",
        )
        add(
            post_quantum_readiness_gap,
            18,
            ["tls", "session_tokens", "api_keys", "cloud_certificates"],
            ["Post-quantum readiness monitored"],
            "Post-quantum migration readiness has a standards-planning gap.",
        )
        add(
            kms_hsm_integration_missing,
            12,
            ["database_encryption", "backup_encryption", "custody_keys"],
            ["KMS/HSM/Key Vault integration required"],
            "Production-grade KMS/HSM/Key Vault governance is missing.",
        )

        if scenario_id == "crypto_agility_post_quantum_readiness_gap":
            affected_domains.extend(
                [
                    "tls",
                    "session_tokens",
                    "api_keys",
                    "database_encryption",
                    "backup_encryption",
                    "audit_integrity",
                    "custody_keys",
                    "cloud_certificates",
                ]
            )
            triggered_controls.extend(CRYPTO_AGILITY_CONTROLS)

        score = min(score, 100)
        unique_domains = list(dict.fromkeys(affected_domains))
        unique_controls = list(dict.fromkeys(triggered_controls))

        if score >= 90:
            severity = "critical"
            decision = "escalate"
        elif score >= 70:
            severity = "high"
            decision = "migration_required"
        elif score >= 45:
            severity = "medium"
            decision = "harden_required"
        elif score >= 25:
            severity = "medium"
            decision = "review_required"
        else:
            severity = "low"
            decision = "allow"

        if scenario_id == "crypto_agility_post_quantum_readiness_gap":
            audit_event_id = "AUD-CRYPTO-AGILITY-PQ-READINESS"
            correlation_id = "CORR-CRYPTO-AGILITY-PQ-READINESS"
            crypto_agility_risk = (
                "Critical crypto-agility gap involving missing inventory, "
                "algorithm versioning, key rotation policy, backup long-term "
                "confidentiality risk, audit integrity gaps, custody key "
                "governance, blockchain protocol separation, and post-quantum "
                "migration readiness."
            )
        else:
            audit_token = scenario_id.strip().upper().replace("_", "-")
            audit_event_id = f"AUD-CRYPTO-AGILITY-{audit_token}"
            correlation_id = f"CORR-CRYPTO-AGILITY-{audit_token}"
            crypto_agility_risk = "Crypto-agility controls require review."

        recommended_action = (
            "Create cryptographic inventory, version algorithms, define key "
            "rotation policies, classify long-term confidentiality risks, "
            "separate Aurora platform cryptography from blockchain protocol "
            "cryptography, and prepare a standards-based post-quantum migration "
            "roadmap without claiming quantum-proof security."
        )

        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="crypto-agility-engine",
            actor_type="service",
            source_module="crypto_agility",
            action="evaluate_scenario",
            object_type="crypto_agility_scenario",
            object_id=scenario_id,
            decision=decision,
            severity=severity,
            risk_score=score,
            summary="Cryptographic agility scenario evaluation recorded.",
            evidence_reference=(
                "EP-FROM-AUD-CRYPTO-AGILITY-PQ-READINESS"
                if scenario_id == "crypto_agility_post_quantum_readiness_gap"
                else None
            ),
            correlation_id=correlation_id,
            metadata={
                "affected_domains": unique_domains,
                "triggered_controls": unique_controls,
                "prototype_boundary": (
                    "No real cryptographic operation, key material, wallet key, "
                    "custody key, KMS, HSM, Key Vault, or post-quantum algorithm "
                    "was accessed or executed."
                ),
            },
        )

        return EvaluateCryptoAgilityScenarioResponse(
            risk_score=score,
            severity=severity,
            decision=decision,
            affected_domains=unique_domains,
            crypto_agility_risk=crypto_agility_risk,
            triggered_controls=unique_controls,
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event.event_id,
            correlation_id=audit_event.correlation_id or "",
            evidence_package_ready=scenario_id == "crypto_agility_post_quantum_readiness_gap",
            recommended_action=recommended_action,
            explanation=(
                "Deterministic prototype evaluation. No real cryptographic "
                "operation, key material, wallet key, custody key, KMS, HSM, "
                "Key Vault, or post-quantum algorithm was accessed or executed. "
                + " ".join(reasons)
            ),
        )

    def _scenario(
        self,
        scenario_id: str,
        title: str,
        description: str,
        affected_assets: list[str],
        risk_indicators: list[str],
        expected_decision: str,
        recommended_controls: list[str],
    ) -> CryptoAgilityScenario:
        return CryptoAgilityScenario(
            scenario_id=scenario_id,
            title=title,
            description=description,
            affected_assets=affected_assets,
            risk_indicators=risk_indicators,
            expected_decision=expected_decision,
            recommended_controls=recommended_controls,
        )


crypto_agility_service = CryptoAgilityService()
