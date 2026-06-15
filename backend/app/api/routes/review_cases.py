from fastapi import APIRouter, HTTPException

from app.schemas.review_case import ReviewCase, ReviewCaseDecisionRequest
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


@router.get("/{case_id}", response_model=ReviewCase)
def get_review_case(case_id: str) -> ReviewCase:
    review_case = review_case_service.get_case(case_id)
    if review_case is None:
        raise HTTPException(status_code=404, detail="Review case not found.")
    return review_case


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
