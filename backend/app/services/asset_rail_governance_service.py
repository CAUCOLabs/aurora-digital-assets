from datetime import datetime, timezone
import re

from app.schemas.asset_rail_governance import (
    AssetRailClassificationRequest,
    AssetRailClassificationResponse,
    AssetRailControlEvaluationRequest,
    AssetRailControlEvaluationResponse,
    AssetRailControlMatrixItem,
    AssetRailGovernanceSummaryRequest,
    AssetRailGovernanceSummaryResponse,
    AssetRailTypeItem,
)
from app.services.audit_service import audit_service


ASSET_TYPES = [
    "digital_euro_cbdc",
    "foreign_cbdc",
    "tokenized_deposit",
    "regulated_stablecoin_emt",
    "asset_referenced_token",
    "cryptoasset",
    "security_token",
    "custodied_digital_asset",
    "unknown_digital_asset",
]

RAIL_TYPES = [
    "central_bank_money_rail",
    "psp_intermediated_payment_rail",
    "internal_bank_ledger_rail",
    "regulated_stablecoin_issuer_rail",
    "asset_referenced_token_issuer_rail",
    "external_crypto_custody_rail",
    "blockchain_execution_rail",
    "securities_settlement_rail",
    "unknown_or_unverified_rail",
]

CONTROL_DOMAINS = [
    "asset_classification",
    "settlement_rail",
    "custody_model",
    "issuer_governance",
    "redemption_governance",
    "reserve_governance",
    "psp_intermediation",
    "bank_ledger_controls",
    "custodian_readiness",
    "wallet_boundary",
    "private_key_boundary",
    "blockchain_execution_boundary",
    "securities_controls",
    "holding_limits",
    "offline_online_mode",
    "privacy_controls",
    "aml_controls",
    "evidence_review",
    "human_approval_integrity",
    "agent_governance",
    "operational_resilience",
    "regulatory_disclaimer",
]

CONTROL_DECISIONS = [
    "digital_euro_psp_controls_required",
    "central_bank_money_controls_required",
    "tokenized_deposit_bank_ledger_controls_required",
    "stablecoin_issuer_controls_required",
    "stablecoin_redemption_controls_required",
    "asset_referenced_token_controls_required",
    "external_custodian_controls_required",
    "blockchain_execution_controls_required",
    "securities_controls_required",
    "unknown_asset_blocked_pending_classification",
    "asset_rail_governance_ready_for_internal_review",
    "asset_rail_governance_requires_remediation",
    "asset_rail_governance_blocked",
    "asset_rail_governance_insufficient_evidence",
]

SAFETY_NOTICE = (
    "Local deterministic asset rail governance evaluation only. No real digital "
    "euro, CBDC, stablecoin, cryptoasset, custody, PSP, banking, blockchain, "
    "cloud, or settlement integration is performed. No real assets, customer "
    "data, private keys, credentials, secrets, payments, redemptions, or "
    "transfers are used. This is not legal advice or regulatory certification."
)

EVALUATION_FIELDS = {
    "asset_classification": "asset_classification_confirmed",
    "settlement_rail": "settlement_rail_confirmed",
    "custody_model": "custody_model_confirmed",
    "issuer_governance": "issuer_governance_defined",
    "redemption_governance": "redemption_model_defined",
    "reserve_governance": "reserve_model_defined",
    "psp_intermediation": "psp_intermediation_defined",
    "bank_ledger_controls": "bank_ledger_controls_defined",
    "custodian_readiness": "custodian_readiness_completed",
    "private_key_boundary": "private_key_boundary_defined",
    "blockchain_execution_boundary": "blockchain_execution_boundary_defined",
    "securities_controls": "securities_controls_defined",
    "holding_limits": "holding_limits_defined",
    "offline_online_mode": "offline_online_mode_defined",
    "privacy_controls": "privacy_controls_defined",
    "aml_controls": "aml_controls_defined",
    "evidence_review": "evidence_review_defined",
    "human_approval_integrity": "human_approval_integrity_required",
    "agent_governance": "agent_governance_required",
    "operational_resilience": "operational_resilience_defined",
    "regulatory_disclaimer": "regulatory_disclaimer_present",
}

SCORE_PENALTIES = {
    "asset_classification": 25,
    "settlement_rail": 20,
    "custody_model": 20,
    "issuer_governance": 25,
    "redemption_governance": 20,
    "reserve_governance": 20,
    "psp_intermediation": 25,
    "bank_ledger_controls": 25,
    "custodian_readiness": 25,
    "private_key_boundary": 30,
    "blockchain_execution_boundary": 30,
    "securities_controls": 25,
    "holding_limits": 15,
    "offline_online_mode": 10,
    "privacy_controls": 15,
    "aml_controls": 20,
    "evidence_review": 15,
    "human_approval_integrity": 15,
    "agent_governance": 15,
    "operational_resilience": 15,
    "regulatory_disclaimer": 20,
}


class AssetRailGovernanceService:
    """Deterministic local asset rail classification and control evaluation."""

    def list_asset_types(self) -> list[AssetRailTypeItem]:
        return [
            AssetRailTypeItem(type_id=asset_type, description=asset_type.replace("_", " "))
            for asset_type in ASSET_TYPES
        ]

    def list_rail_types(self) -> list[AssetRailTypeItem]:
        return [
            AssetRailTypeItem(type_id=rail_type, description=rail_type.replace("_", " "))
            for rail_type in RAIL_TYPES
        ]

    def control_matrix(self) -> list[AssetRailControlMatrixItem]:
        return [
            AssetRailControlMatrixItem(
                asset_type=asset_type,
                default_rail_type=self._defaults_for(asset_type)["rail_type"],
                required_control_domains=self._defaults_for(asset_type)["required"],
                not_applicable_control_domains=self._defaults_for(asset_type)["not_applicable"],
                control_decisions=self._defaults_for(asset_type)["decisions"],
            )
            for asset_type in ASSET_TYPES
        ]

    def classify(
        self,
        request: AssetRailClassificationRequest,
    ) -> AssetRailClassificationResponse:
        asset_symbol = self._safe_identifier(request.asset_symbol)
        profile = self._classification_profile(request)
        audit_event_id = self._classification_audit_event_id(asset_symbol)
        correlation_id = self._correlation_id(asset_symbol)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id or "system",
            actor_type="staff",
            source_module="asset_rail_governance",
            action="classify_asset_rail",
            object_type="asset_rail_classification",
            object_id=asset_symbol,
            decision=profile["classification_level"],
            severity="medium" if profile["asset_type"] != "unknown_digital_asset" else "critical",
            risk_score=100 - profile["classification_confidence"],
            summary="Asset rail classified in local deterministic prototype.",
            correlation_id=correlation_id,
            metadata={
                "environment": request.environment,
                "asset_type": profile["asset_type"],
                "rail_type": profile["rail_type"],
                "control_decisions": profile["control_decisions"],
                "safety_notice": SAFETY_NOTICE,
            },
        )
        return AssetRailClassificationResponse(
            asset_symbol=asset_symbol,
            asset_name=request.asset_name,
            asset_type=profile["asset_type"],
            rail_type=profile["rail_type"],
            custody_model=profile["custody_model"],
            settlement_model=profile["settlement_model"],
            primary_control_domains=profile["required_controls"],
            required_controls=profile["required_controls"],
            not_applicable_controls=profile["not_applicable_controls"],
            control_decisions=profile["control_decisions"],
            classification_confidence=profile["classification_confidence"],
            classification_level=profile["classification_level"],
            external_custodian_required=profile["external_custodian_required"],
            blockchain_execution_required=profile["blockchain_execution_required"],
            psp_intermediation_required=profile["psp_intermediation_required"],
            bank_ledger_controls_required=profile["bank_ledger_controls_required"],
            issuer_controls_required=profile["issuer_controls_required"],
            redemption_controls_required=profile["redemption_controls_required"],
            reserve_controls_required=profile["reserve_controls_required"],
            privacy_controls_required=profile["privacy_controls_required"],
            holding_limits_required=profile["holding_limits_required"],
            evidence_required=profile["evidence_required"],
            review_required=profile["review_required"],
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            safety_notice=self._safety_notice_for(profile["asset_type"]),
            created_at=created_at,
        )

    def evaluate_controls(
        self,
        request: AssetRailControlEvaluationRequest,
    ) -> AssetRailControlEvaluationResponse:
        asset_symbol = self._safe_identifier(request.asset_symbol)
        asset_type = self._normalize_known(request.asset_type, ASSET_TYPES, "unknown_digital_asset")
        rail_type = self._normalize_known(request.rail_type, RAIL_TYPES, "unknown_or_unverified_rail")
        required = self._required_controls_for_evaluation(asset_type, rail_type)
        not_applicable = self._not_applicable_controls(asset_type)
        satisfied, missing = self._control_status(request, required)
        blocking_reasons = self._blocking_reasons(request, asset_type, rail_type, missing)
        score = self._score(missing)
        level = self._governance_level(score)
        decision = self._governance_decision(
            asset_type=asset_type,
            score=score,
            blocking_reasons=blocking_reasons,
            missing_controls=missing,
        )
        flags = self._requirement_flags(asset_type, rail_type)
        audit_event_id = self._controls_audit_event_id(asset_symbol)
        correlation_id = self._correlation_id(asset_symbol)
        created_at = datetime.now(timezone.utc).isoformat()
        audit_event = audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id=request.reviewer_id or "system",
            actor_type="staff",
            source_module="asset_rail_governance",
            action="evaluate_asset_rail_controls",
            object_type="asset_rail_control_evaluation",
            object_id=asset_symbol,
            decision=decision,
            severity="critical" if decision == "asset_rail_governance_blocked" else level,
            risk_score=100 - score,
            summary="Asset rail controls evaluated in local deterministic prototype.",
            correlation_id=correlation_id,
            metadata={
                "environment": request.environment,
                "asset_type": asset_type,
                "rail_type": rail_type,
                "missing_controls": missing,
                "blocking_reasons": blocking_reasons,
                "linked_custodian_guard_case_id": request.linked_custodian_guard_case_id,
                "linked_human_integrity_audit_event_id": request.linked_human_integrity_audit_event_id,
                "linked_agent_governance_audit_event_id": request.linked_agent_governance_audit_event_id,
                "safety_notice": SAFETY_NOTICE,
            },
        )
        return AssetRailControlEvaluationResponse(
            asset_symbol=asset_symbol,
            asset_type=asset_type,
            rail_type=rail_type,
            governance_decision=decision,
            governance_score=score,
            governance_level=level,
            satisfied_controls=satisfied,
            missing_controls=missing,
            not_applicable_controls=not_applicable,
            required_control_domains=required,
            blocking_reasons=blocking_reasons,
            recommended_next_actions=self._recommended_next_actions(decision, missing, blocking_reasons),
            external_custodian_required=flags["external_custodian_required"],
            blockchain_execution_required=flags["blockchain_execution_required"],
            psp_intermediation_required=flags["psp_intermediation_required"],
            bank_ledger_controls_required=flags["bank_ledger_controls_required"],
            issuer_controls_required=flags["issuer_controls_required"],
            redemption_controls_required=flags["redemption_controls_required"],
            reserve_controls_required=flags["reserve_controls_required"],
            evidence_required=bool(missing or blocking_reasons),
            review_required=decision != "asset_rail_governance_ready_for_internal_review",
            audit_event_created=audit_event is not None,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            safety_notice=SAFETY_NOTICE,
            created_at=created_at,
        )

    def governance_summary(
        self,
        request: AssetRailGovernanceSummaryRequest,
    ) -> AssetRailGovernanceSummaryResponse:
        asset_symbol = self._safe_identifier(request.asset_symbol)
        score = max(min(request.governance_score, 100), 0)
        return AssetRailGovernanceSummaryResponse(
            summary_id=f"SUMMARY-ASSET-RAIL-{asset_symbol}",
            title="Asset Rail Governance Summary",
            asset_symbol=asset_symbol,
            asset_type=self._normalize_known(request.asset_type, ASSET_TYPES, "unknown_digital_asset"),
            rail_type=self._normalize_known(request.rail_type, RAIL_TYPES, "unknown_or_unverified_rail"),
            summary_points=[
                "Asset rail classification is treated as the first governance step.",
                f"Current deterministic governance decision: {request.governance_decision}.",
                f"Current deterministic governance score: {score}.",
            ],
            risk_notes=self._summary_risk_notes(request.governance_decision, score),
            required_next_steps=self._summary_next_steps(request.governance_decision, score),
            safety_notice=SAFETY_NOTICE,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def _classification_profile(self, request: AssetRailClassificationRequest) -> dict:
        declared = (request.declared_asset_type or "").strip().lower()
        if request.is_central_bank_money or declared == "digital_euro_cbdc":
            asset_type = "digital_euro_cbdc"
        elif declared == "foreign_cbdc":
            asset_type = "foreign_cbdc"
        elif request.is_bank_liability or declared == "tokenized_deposit":
            asset_type = "tokenized_deposit"
        elif (request.is_stablecoin and request.is_e_money_token) or declared == "regulated_stablecoin_emt":
            asset_type = "regulated_stablecoin_emt"
        elif request.is_asset_referenced_token or declared == "asset_referenced_token":
            asset_type = "asset_referenced_token"
        elif request.is_cryptoasset or declared == "cryptoasset":
            asset_type = "cryptoasset"
        elif request.is_security_token or declared == "security_token":
            asset_type = "security_token"
        elif declared == "custodied_digital_asset":
            asset_type = "custodied_digital_asset"
        else:
            asset_type = "unknown_digital_asset"

        defaults = self._defaults_for(asset_type)
        rail_type = self._resolve_rail_type(request, asset_type, defaults["rail_type"])
        flags = self._classification_flags(request, asset_type, rail_type)
        required = self._dedupe(defaults["required"] + flags["additional_required"])
        not_applicable = self._dedupe(defaults["not_applicable"])
        decisions = self._dedupe(defaults["decisions"] + flags["additional_decisions"])
        confidence = 90 if asset_type != "unknown_digital_asset" else 30
        if request.declared_asset_type and request.declared_asset_type.strip().lower() not in ASSET_TYPES:
            confidence -= 15
        if flags["blocking_reasons"]:
            confidence -= 25
        confidence = max(min(confidence, 100), 0)
        classification_level = (
            "blocked"
            if asset_type == "unknown_digital_asset" or flags["blocking_reasons"]
            else "classified"
        )
        return {
            "asset_type": asset_type,
            "rail_type": rail_type,
            "custody_model": flags["custody_model"],
            "settlement_model": flags["settlement_model"],
            "required_controls": required,
            "not_applicable_controls": not_applicable,
            "control_decisions": decisions,
            "classification_confidence": confidence,
            "classification_level": classification_level,
            "evidence_required": asset_type == "unknown_digital_asset" or bool(flags["blocking_reasons"]),
            "review_required": asset_type == "unknown_digital_asset" or bool(flags["blocking_reasons"]),
            **flags,
        }

    def _defaults_for(self, asset_type: str) -> dict:
        defaults = {
            "digital_euro_cbdc": {
                "rail_type": "central_bank_money_rail",
                "required": [
                    "asset_classification",
                    "settlement_rail",
                    "psp_intermediation",
                    "holding_limits",
                    "offline_online_mode",
                    "privacy_controls",
                    "aml_controls",
                    "evidence_review",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": [
                    "private_key_boundary",
                    "external_crypto_custody_rail",
                    "blockchain_execution_boundary",
                ],
                "decisions": [
                    "digital_euro_psp_controls_required",
                    "central_bank_money_controls_required",
                ],
            },
            "tokenized_deposit": {
                "rail_type": "internal_bank_ledger_rail",
                "required": [
                    "asset_classification",
                    "settlement_rail",
                    "bank_ledger_controls",
                    "evidence_review",
                    "human_approval_integrity",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["external_crypto_custody_rail"],
                "decisions": ["tokenized_deposit_bank_ledger_controls_required"],
            },
            "regulated_stablecoin_emt": {
                "rail_type": "regulated_stablecoin_issuer_rail",
                "required": [
                    "issuer_governance",
                    "redemption_governance",
                    "reserve_governance",
                    "aml_controls",
                    "evidence_review",
                    "human_approval_integrity",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["central_bank_money_rail", "bank_ledger_controls"],
                "decisions": [
                    "stablecoin_issuer_controls_required",
                    "stablecoin_redemption_controls_required",
                ],
            },
            "asset_referenced_token": {
                "rail_type": "asset_referenced_token_issuer_rail",
                "required": [
                    "issuer_governance",
                    "redemption_governance",
                    "reserve_governance",
                    "aml_controls",
                    "evidence_review",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["central_bank_money_rail", "bank_ledger_controls"],
                "decisions": ["asset_referenced_token_controls_required"],
            },
            "cryptoasset": {
                "rail_type": "external_crypto_custody_rail",
                "required": [
                    "custodian_readiness",
                    "wallet_boundary",
                    "private_key_boundary",
                    "blockchain_execution_boundary",
                    "aml_controls",
                    "evidence_review",
                    "human_approval_integrity",
                    "agent_governance",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["central_bank_money_rail", "bank_ledger_controls"],
                "decisions": [
                    "external_custodian_controls_required",
                    "blockchain_execution_controls_required",
                ],
            },
            "security_token": {
                "rail_type": "securities_settlement_rail",
                "required": [
                    "securities_controls",
                    "settlement_rail",
                    "custody_model",
                    "evidence_review",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["central_bank_money_rail"],
                "decisions": ["securities_controls_required"],
            },
            "foreign_cbdc": {
                "rail_type": "psp_intermediated_payment_rail",
                "required": [
                    "asset_classification",
                    "settlement_rail",
                    "psp_intermediation",
                    "holding_limits",
                    "privacy_controls",
                    "aml_controls",
                    "evidence_review",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": [
                    "private_key_boundary",
                    "external_crypto_custody_rail",
                    "blockchain_execution_boundary",
                ],
                "decisions": ["central_bank_money_controls_required"],
            },
            "custodied_digital_asset": {
                "rail_type": "external_crypto_custody_rail",
                "required": [
                    "asset_classification",
                    "settlement_rail",
                    "custody_model",
                    "custodian_readiness",
                    "wallet_boundary",
                    "aml_controls",
                    "evidence_review",
                    "human_approval_integrity",
                    "operational_resilience",
                    "regulatory_disclaimer",
                ],
                "not_applicable": ["central_bank_money_rail", "bank_ledger_controls"],
                "decisions": ["external_custodian_controls_required"],
            },
        }
        return defaults.get(
            asset_type,
            {
                "rail_type": "unknown_or_unverified_rail",
                "required": ["asset_classification", "evidence_review", "regulatory_disclaimer"],
                "not_applicable": [],
                "decisions": ["unknown_asset_blocked_pending_classification"],
            },
        )

    def _resolve_rail_type(
        self,
        request: AssetRailClassificationRequest,
        asset_type: str,
        default_rail_type: str,
    ) -> str:
        declared = (request.declared_rail_type or "").strip().lower()
        if declared in RAIL_TYPES:
            return declared
        if asset_type == "digital_euro_cbdc" and request.distributed_by_psp:
            return "psp_intermediated_payment_rail"
        if asset_type == "cryptoasset" and request.uses_blockchain_execution and not request.uses_external_custodian:
            return "blockchain_execution_rail"
        return default_rail_type

    def _classification_flags(
        self,
        request: AssetRailClassificationRequest,
        asset_type: str,
        rail_type: str,
    ) -> dict:
        external_custodian_required = (
            asset_type in {"cryptoasset", "custodied_digital_asset"}
            and request.uses_external_custodian
        )
        blockchain_execution_required = request.uses_blockchain_execution and asset_type in {
            "cryptoasset",
            "regulated_stablecoin_emt",
            "asset_referenced_token",
        }
        psp_required = asset_type == "digital_euro_cbdc"
        bank_ledger_required = asset_type == "tokenized_deposit"
        issuer_required = asset_type in {"regulated_stablecoin_emt", "asset_referenced_token"}
        redemption_required = issuer_required
        reserve_required = issuer_required
        holding_limits_required = asset_type == "digital_euro_cbdc" or request.holding_limits_required
        privacy_required = asset_type == "digital_euro_cbdc" or request.privacy_controls_required
        additional_required = []
        additional_decisions = []
        blocking_reasons = []
        if external_custodian_required:
            additional_decisions.append("external_custodian_controls_required")
        if blockchain_execution_required:
            additional_decisions.append("blockchain_execution_controls_required")
        if request.uses_private_keys:
            additional_required.append("private_key_boundary")
        if asset_type == "digital_euro_cbdc" and request.uses_external_custodian:
            blocking_reasons.append("digital_euro_external_custodian_contradiction")
        if asset_type == "digital_euro_cbdc" and request.uses_private_keys:
            blocking_reasons.append("digital_euro_private_key_boundary_contradiction")
        if asset_type == "digital_euro_cbdc" and request.uses_blockchain_execution:
            blocking_reasons.append("digital_euro_blockchain_execution_contradiction")
        if asset_type == "tokenized_deposit" and request.uses_external_custodian:
            blocking_reasons.append("tokenized_deposit_external_custody_requires_remediation")
        custody_model = "none_required_for_prototype"
        if external_custodian_required:
            custody_model = "external_regulated_custodian_controls_required"
        elif bank_ledger_required:
            custody_model = "bank_liability_internal_ledger_controls"
        elif issuer_required:
            custody_model = "issuer_and_service_model_governance"
        elif asset_type == "security_token":
            custody_model = "securities_custody_and_settlement_governance"
        settlement_model = rail_type.replace("_", " ")
        return {
            "external_custodian_required": external_custodian_required,
            "blockchain_execution_required": blockchain_execution_required,
            "psp_intermediation_required": psp_required,
            "bank_ledger_controls_required": bank_ledger_required,
            "issuer_controls_required": issuer_required,
            "redemption_controls_required": redemption_required,
            "reserve_controls_required": reserve_required,
            "privacy_controls_required": privacy_required,
            "holding_limits_required": holding_limits_required,
            "additional_required": additional_required,
            "additional_decisions": additional_decisions,
            "blocking_reasons": blocking_reasons,
            "custody_model": custody_model,
            "settlement_model": settlement_model,
        }

    def _required_controls_for_evaluation(self, asset_type: str, rail_type: str) -> list[str]:
        required = list(self._defaults_for(asset_type)["required"])
        if rail_type == "external_crypto_custody_rail":
            required.append("custodian_readiness")
        if rail_type == "blockchain_execution_rail":
            required.append("blockchain_execution_boundary")
        return self._dedupe(required)

    def _not_applicable_controls(self, asset_type: str) -> list[str]:
        return self._defaults_for(asset_type)["not_applicable"]

    def _control_status(
        self,
        request: AssetRailControlEvaluationRequest,
        required: list[str],
    ) -> tuple[list[str], list[str]]:
        values = request.controls.model_dump()
        missing = [
            control
            for control in required
            if not values.get(EVALUATION_FIELDS.get(control, ""), False)
        ]
        satisfied = [
            control
            for control, field in EVALUATION_FIELDS.items()
            if values.get(field, False)
        ]
        return sorted(satisfied), sorted(missing)

    def _blocking_reasons(
        self,
        request: AssetRailControlEvaluationRequest,
        asset_type: str,
        rail_type: str,
        missing: list[str],
    ) -> list[str]:
        blockers = []
        if asset_type == "unknown_digital_asset":
            blockers.append("unknown_asset_blocked_pending_classification")
        if asset_type == "digital_euro_cbdc" and rail_type in {
            "external_crypto_custody_rail",
            "blockchain_execution_rail",
        }:
            blockers.append("digital_euro_external_custodian_contradiction")
        if asset_type == "stablecoin" and "issuer_governance" in missing:
            blockers.append("stablecoin_without_issuer_governance")
        if asset_type == "regulated_stablecoin_emt" and "issuer_governance" in missing:
            blockers.append("stablecoin_without_issuer_governance")
        if asset_type == "cryptoasset" and "private_key_boundary" in missing:
            blockers.append("cryptoasset_private_key_boundary_missing")
        if "regulatory_disclaimer" in missing:
            blockers.append("regulatory_disclaimer_missing_requires_remediation")
        return self._dedupe(blockers)

    def _score(self, missing: list[str]) -> int:
        score = 100
        for control in set(missing):
            score -= SCORE_PENALTIES.get(control, 5)
        return max(score, 0)

    def _governance_level(self, score: int) -> str:
        if score >= 85:
            return "high"
        if score >= 65:
            return "medium"
        if score >= 40:
            return "elevated"
        return "blocked"

    def _governance_decision(
        self,
        *,
        asset_type: str,
        score: int,
        blocking_reasons: list[str],
        missing_controls: list[str],
    ) -> str:
        if asset_type == "unknown_digital_asset":
            return "asset_rail_governance_blocked"
        if any("contradiction" in reason for reason in blocking_reasons):
            return "asset_rail_governance_blocked"
        if "asset_classification" in missing_controls:
            return "asset_rail_governance_insufficient_evidence"
        if score >= 85 and not blocking_reasons:
            return "asset_rail_governance_ready_for_internal_review"
        if score >= 40:
            return "asset_rail_governance_requires_remediation"
        return "asset_rail_governance_blocked"

    def _requirement_flags(self, asset_type: str, rail_type: str) -> dict[str, bool]:
        return {
            "external_custodian_required": rail_type == "external_crypto_custody_rail"
            or asset_type == "cryptoasset",
            "blockchain_execution_required": rail_type == "blockchain_execution_rail"
            or asset_type == "cryptoasset",
            "psp_intermediation_required": asset_type == "digital_euro_cbdc",
            "bank_ledger_controls_required": asset_type == "tokenized_deposit",
            "issuer_controls_required": asset_type
            in {"regulated_stablecoin_emt", "asset_referenced_token"},
            "redemption_controls_required": asset_type
            in {"regulated_stablecoin_emt", "asset_referenced_token"},
            "reserve_controls_required": asset_type
            in {"regulated_stablecoin_emt", "asset_referenced_token"},
        }

    def _recommended_next_actions(
        self,
        decision: str,
        missing: list[str],
        blockers: list[str],
    ) -> list[str]:
        actions = ["retain_local_deterministic_no_real_execution_boundary"]
        if missing:
            actions.append("collect_asset_rail_control_evidence")
        if blockers:
            actions.append("open_internal_asset_rail_review")
        if decision == "asset_rail_governance_ready_for_internal_review":
            actions.append("prepare_asset_rail_governance_review_pack")
        elif decision == "asset_rail_governance_blocked":
            actions.append("keep_asset_rail_blocked_pending_classification_or_remediation")
        else:
            actions.append("remediate_missing_asset_rail_controls_before_reassessment")
        return self._dedupe(actions)

    def _summary_risk_notes(self, decision: str, score: int) -> list[str]:
        notes = ["Summary is based on deterministic prototype data only."]
        if "blocked" in decision or score < 40:
            notes.append("Asset rail remains blocked until classification and control gaps are resolved.")
        elif score < 85:
            notes.append("Control gaps require remediation before internal review readiness.")
        else:
            notes.append("No production, custody, settlement, or regulatory certification is implied.")
        return notes

    def _summary_next_steps(self, decision: str, score: int) -> list[str]:
        if "blocked" in decision or score < 40:
            return ["retain_block", "complete_classification_evidence", "route_to_internal_review"]
        if score < 85:
            return ["remediate_missing_controls", "refresh_evidence", "reassess_asset_rail"]
        return ["prepare_internal_review_pack", "retain_prototype_safety_notice"]

    def _safety_notice_for(self, asset_type: str) -> str:
        if asset_type == "digital_euro_cbdc":
            return f"{SAFETY_NOTICE} No real digital euro integration is performed."
        return SAFETY_NOTICE

    def _safe_identifier(self, value: str) -> str:
        normalized = re.sub(r"[^A-Za-z0-9-]+", "-", value.strip().upper()).strip("-")
        return normalized or "UNKNOWN-ASSET"

    def _normalize_known(self, value: str, allowed: list[str], fallback: str) -> str:
        normalized = value.strip().lower()
        return normalized if normalized in allowed else fallback

    def _classification_audit_event_id(self, asset_symbol: str) -> str:
        return f"AUD-ASSET-RAIL-CLASSIFICATION-{asset_symbol}"

    def _controls_audit_event_id(self, asset_symbol: str) -> str:
        return f"AUD-ASSET-RAIL-CONTROLS-{asset_symbol}"

    def _correlation_id(self, asset_symbol: str) -> str:
        return f"CORR-ASSET-RAIL-{asset_symbol}"

    def _dedupe(self, values: list[str]) -> list[str]:
        return list(dict.fromkeys(values))


asset_rail_governance_service = AssetRailGovernanceService()
