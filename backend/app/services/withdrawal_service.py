from app.schemas.risk_review import RiskDecisionResponse
from app.schemas.withdrawal import WithdrawalEvaluateRequest
from app.services.risk_review_engine import RiskReviewEngine


class WithdrawalService:
    """Application service for simulated withdrawal workflows."""

    def __init__(self, risk_review_engine: RiskReviewEngine | None = None) -> None:
        self.risk_review_engine = risk_review_engine or RiskReviewEngine()

    def evaluate_withdrawal(
        self,
        request: WithdrawalEvaluateRequest,
    ) -> RiskDecisionResponse:
        return self.risk_review_engine.evaluate_withdrawal(request)
