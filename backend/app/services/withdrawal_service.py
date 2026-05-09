from app.schemas.risk_review import RiskDecisionResponse
from app.schemas.withdrawal import WithdrawalEvaluateRequest
from app.services.audit_service import AuditService, audit_service
from app.services.risk_review_engine import RiskReviewEngine
from app.services.review_case_service import (
    ReviewCaseService,
    review_case_service,
)


class WithdrawalService:
    """Application service for simulated withdrawal workflows."""

    def __init__(
        self,
        risk_review_engine: RiskReviewEngine | None = None,
        audit_log: AuditService | None = None,
        review_cases: ReviewCaseService | None = None,
    ) -> None:
        self.risk_review_engine = risk_review_engine or RiskReviewEngine()
        self.audit_log = audit_log or audit_service
        self.review_cases = review_cases or review_case_service

    def evaluate_withdrawal(
        self,
        request: WithdrawalEvaluateRequest,
    ) -> RiskDecisionResponse:
        decision = self.risk_review_engine.evaluate_withdrawal(request)
        case_id = None

        if decision.case_required:
            review_case = self.review_cases.create_withdrawal_case(request, decision)
            case_id = review_case.case_id

        self.audit_log.record_event(
            module="withdrawals",
            action_type=decision.audit_event_type,
            status=decision.decision,
            risk_level=decision.risk_level,
            decision=decision.decision,
            reasons=decision.reasons,
            case_id=case_id,
            user_message=decision.user_message,
        )

        return decision.model_copy(update={"case_id": case_id})
