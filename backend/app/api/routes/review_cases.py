from fastapi import APIRouter, HTTPException

from app.schemas.review_case import (
    CreateReviewCaseFromEvidencePackageRequest,
    CreateReviewCaseFromEvidencePackageResponse,
    ReviewCase,
    ReviewCaseAction,
    ReviewCaseActionRequest,
    ReviewCaseCloseRequest,
    ReviewCaseDecisionRequest,
    ReviewCaseLifecycleSummary,
    ReviewCaseLifecycleTransitionRequest,
    ReviewCaseLifecycleTransitionResponse,
)
from app.services.audit_service import audit_service
from app.services.review_case_service import (
    REVIEW_DECISION_STATUSES,
    review_case_service,
)


router = APIRouter(prefix="/review-cases", tags=["review cases"])


@router.get("", response_model=list[ReviewCase])
def list_review_cases() -> list[ReviewCase]:
    return review_case_service.list_cases()


@router.get("/persisted", response_model=list[ReviewCase])
def list_persisted_review_cases() -> list[ReviewCase]:
    return review_case_service.list_persisted_cases()


@router.post(
    "/create-from-evidence-package",
    response_model=CreateReviewCaseFromEvidencePackageResponse,
)
def create_review_case_from_evidence_package(
    request: CreateReviewCaseFromEvidencePackageRequest,
) -> CreateReviewCaseFromEvidencePackageResponse:
    return review_case_service.create_from_evidence_package(
        package_id=request.package_id,
        source_audit_event_id=request.source_audit_event_id,
        correlation_id=request.correlation_id,
        reviewer_id=request.reviewer_id,
        priority=request.priority,
    )


@router.get("/{case_id}", response_model=ReviewCase)
def get_review_case(case_id: str) -> ReviewCase:
    review_case = review_case_service.get_case(case_id)
    if review_case is None:
        raise HTTPException(status_code=404, detail="Review case not found.")
    return review_case


@router.get("/{case_id}/lifecycle", response_model=ReviewCaseLifecycleSummary)
def get_review_case_lifecycle(case_id: str) -> ReviewCaseLifecycleSummary:
    return review_case_service.get_lifecycle_summary(case_id)


@router.post(
    "/{case_id}/transition",
    response_model=ReviewCaseLifecycleTransitionResponse,
)
def transition_review_case_lifecycle(
    case_id: str,
    request: ReviewCaseLifecycleTransitionRequest,
) -> ReviewCaseLifecycleTransitionResponse:
    return review_case_service.transition_lifecycle(
        case_id=case_id,
        target_status=request.target_status,
        reviewer_id=request.reviewer_id,
        decision_note=request.decision_note,
        mitigation_action=request.mitigation_action,
        evidence_package_id=request.evidence_package_id,
        risk_acceptance=request.risk_acceptance,
    )


@router.post("/{case_id}/actions", response_model=ReviewCaseAction)
def add_review_case_lifecycle_action(
    case_id: str,
    request: ReviewCaseActionRequest,
) -> ReviewCaseAction:
    return review_case_service.add_lifecycle_action(
        case_id=case_id,
        action_type=request.action_type,
        actor_id=request.actor_id,
        note=request.note,
    )


@router.post(
    "/{case_id}/close",
    response_model=ReviewCaseLifecycleTransitionResponse,
)
def close_review_case_lifecycle(
    case_id: str,
    request: ReviewCaseCloseRequest,
) -> ReviewCaseLifecycleTransitionResponse:
    return review_case_service.close_lifecycle_case(
        case_id=case_id,
        reviewer_id=request.reviewer_id,
        decision_note=request.decision_note,
        final_decision=request.final_decision,
        evidence_package_id=request.evidence_package_id,
        risk_acceptance=request.risk_acceptance,
    )


@router.post("/{case_id}/decision", response_model=ReviewCase)
def record_review_case_decision(
    case_id: str,
    request: ReviewCaseDecisionRequest,
) -> ReviewCase:
    if request.decision not in REVIEW_DECISION_STATUSES:
        raise HTTPException(status_code=400, detail="Unsupported reviewer decision.")

    review_case = review_case_service.record_decision(
        case_id=case_id,
        decision=request.decision,
        notes=request.notes,
    )
    if review_case is None:
        raise HTTPException(status_code=404, detail="Review case not found.")

    audit_service.record_event(
        module="review_cases",
        action_type="reviewer_decision_recorded",
        status=review_case.status,
        case_id=case_id,
        user_message="Reviewer decision recorded.",
    )
    return review_case
