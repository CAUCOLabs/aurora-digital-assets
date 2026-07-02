from fastapi import APIRouter

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
from app.services.asset_rail_governance_service import asset_rail_governance_service


router = APIRouter(
    prefix="/asset-rail-governance",
    tags=["asset rail governance"],
)


@router.get("/asset-types", response_model=list[AssetRailTypeItem])
def list_asset_types() -> list[AssetRailTypeItem]:
    return asset_rail_governance_service.list_asset_types()


@router.get("/rail-types", response_model=list[AssetRailTypeItem])
def list_rail_types() -> list[AssetRailTypeItem]:
    return asset_rail_governance_service.list_rail_types()


@router.get("/control-matrix", response_model=list[AssetRailControlMatrixItem])
def get_control_matrix() -> list[AssetRailControlMatrixItem]:
    return asset_rail_governance_service.control_matrix()


@router.post("/classify", response_model=AssetRailClassificationResponse)
def classify_asset_rail(
    request: AssetRailClassificationRequest,
) -> AssetRailClassificationResponse:
    return asset_rail_governance_service.classify(request)


@router.post(
    "/evaluate-controls",
    response_model=AssetRailControlEvaluationResponse,
)
def evaluate_controls(
    request: AssetRailControlEvaluationRequest,
) -> AssetRailControlEvaluationResponse:
    return asset_rail_governance_service.evaluate_controls(request)


@router.post(
    "/governance-summary",
    response_model=AssetRailGovernanceSummaryResponse,
)
def governance_summary(
    request: AssetRailGovernanceSummaryRequest,
) -> AssetRailGovernanceSummaryResponse:
    return asset_rail_governance_service.governance_summary(request)
