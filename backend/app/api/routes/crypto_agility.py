from fastapi import APIRouter

from app.schemas.crypto_agility import (
    CryptoAgilityScenario,
    CryptoAlgorithmPolicy,
    CryptoAsset,
    CryptoKeyLifecycleItem,
    EvaluateCryptoAgilityScenarioRequest,
    EvaluateCryptoAgilityScenarioResponse,
)
from app.services.crypto_agility_service import crypto_agility_service


router = APIRouter(
    prefix="/crypto-agility",
    tags=["crypto agility"],
)


@router.get("/assets", response_model=list[CryptoAsset])
def list_assets() -> list[CryptoAsset]:
    return crypto_agility_service.list_assets()


@router.get("/policies", response_model=list[CryptoAlgorithmPolicy])
def list_policies() -> list[CryptoAlgorithmPolicy]:
    return crypto_agility_service.list_policies()


@router.get("/key-lifecycle", response_model=list[CryptoKeyLifecycleItem])
def list_key_lifecycle() -> list[CryptoKeyLifecycleItem]:
    return crypto_agility_service.list_key_lifecycle()


@router.get("/scenarios", response_model=list[CryptoAgilityScenario])
def list_scenarios() -> list[CryptoAgilityScenario]:
    return crypto_agility_service.list_scenarios()


@router.post(
    "/evaluate-scenario",
    response_model=EvaluateCryptoAgilityScenarioResponse,
)
def evaluate_scenario(
    request: EvaluateCryptoAgilityScenarioRequest,
) -> EvaluateCryptoAgilityScenarioResponse:
    return crypto_agility_service.evaluate_scenario(
        scenario_id=request.scenario_id,
        deprecated_algorithm_detected=request.deprecated_algorithm_detected,
        long_lived_key_detected=request.long_lived_key_detected,
        missing_algorithm_versioning=request.missing_algorithm_versioning,
        missing_key_rotation_policy=request.missing_key_rotation_policy,
        backup_long_term_risk=request.backup_long_term_risk,
        audit_integrity_gap=request.audit_integrity_gap,
        custody_key_rotation_gap=request.custody_key_rotation_gap,
        blockchain_protocol_confusion=request.blockchain_protocol_confusion,
        post_quantum_readiness_gap=request.post_quantum_readiness_gap,
        kms_hsm_integration_missing=request.kms_hsm_integration_missing,
    )
