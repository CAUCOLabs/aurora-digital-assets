from fastapi import APIRouter, HTTPException

from app.schemas.evidence_packages import (
    EvidencePackage,
    EvidencePackageTemplate,
    EvidenceReadinessCheck,
    GenerateEvidencePackageRequest,
    GenerateEvidencePackageResponse,
)
from app.services.evidence_packages_service import evidence_packages_service


router = APIRouter(prefix="/evidence-packages", tags=["evidence packages"])


@router.get("", response_model=list[EvidencePackage])
def list_evidence_packages() -> list[EvidencePackage]:
    return evidence_packages_service.list_packages()


@router.get("/templates", response_model=list[EvidencePackageTemplate])
def list_evidence_package_templates() -> list[EvidencePackageTemplate]:
    return evidence_packages_service.list_templates()


@router.post("/generate", response_model=GenerateEvidencePackageResponse)
def generate_evidence_package(
    request: GenerateEvidencePackageRequest,
) -> GenerateEvidencePackageResponse:
    return evidence_packages_service.generate_package(
        source_type=request.source_type,
        source_id=request.source_id,
        package_type=request.package_type,
        reviewer_id=request.reviewer_id,
    )


@router.get(
    "/from-audit-event/{audit_event_id}",
    response_model=EvidencePackage,
)
def get_evidence_package_from_audit_event(
    audit_event_id: str,
) -> EvidencePackage:
    package = evidence_packages_service.get_package_from_audit_event(audit_event_id)
    if package is None:
        raise HTTPException(status_code=404, detail="Audit event not found.")
    return package


@router.get("/{package_id}", response_model=EvidencePackage)
def get_evidence_package(package_id: str) -> EvidencePackage:
    package = evidence_packages_service.get_package(package_id)
    if package is None:
        raise HTTPException(status_code=404, detail="Evidence package not found.")
    return package


@router.get("/{package_id}/readiness", response_model=EvidenceReadinessCheck)
def get_evidence_package_readiness(package_id: str) -> EvidenceReadinessCheck:
    package = evidence_packages_service.get_package(package_id)
    if package is None:
        raise HTTPException(status_code=404, detail="Evidence package not found.")
    return evidence_packages_service.get_readiness_check(package_id)
