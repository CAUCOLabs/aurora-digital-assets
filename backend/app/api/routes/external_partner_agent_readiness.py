from fastapi import APIRouter

from app.schemas.external_partner_agent_readiness import (
    CustodianAgentReadinessRequest,
    ExternalPartnerReadinessPreviewRequest,
    ExternalPartnerReadinessRequest,
    ExternalPartnerReadinessResponse,
    PartnerTypeDefinition,
    ReadinessControlDefinition,
)
from app.services.external_partner_agent_readiness_service import (
    external_partner_agent_readiness_service,
)


router = APIRouter(
    prefix="/external-partner-agent-readiness",
    tags=["external partner agent readiness"],
)


@router.get("/controls", response_model=list[ReadinessControlDefinition])
def list_controls() -> list[ReadinessControlDefinition]:
    return external_partner_agent_readiness_service.list_controls()


@router.get("/partner-types", response_model=list[PartnerTypeDefinition])
def list_partner_types() -> list[PartnerTypeDefinition]:
    return external_partner_agent_readiness_service.list_partner_types()


@router.post("/evaluate", response_model=ExternalPartnerReadinessResponse)
def evaluate_readiness(
    request: ExternalPartnerReadinessRequest,
) -> ExternalPartnerReadinessResponse:
    return external_partner_agent_readiness_service.evaluate(request)


@router.post(
    "/evaluate-custodian-agent",
    response_model=ExternalPartnerReadinessResponse,
)
def evaluate_custodian_agent(
    request: CustodianAgentReadinessRequest,
) -> ExternalPartnerReadinessResponse:
    return external_partner_agent_readiness_service.evaluate_custodian_agent(request)


@router.post("/readiness-preview", response_model=ExternalPartnerReadinessResponse)
def readiness_preview(
    request: ExternalPartnerReadinessPreviewRequest,
) -> ExternalPartnerReadinessResponse:
    return external_partner_agent_readiness_service.readiness_preview(request)
