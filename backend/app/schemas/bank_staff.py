from pydantic import BaseModel


class OnboardingStep(BaseModel):
    step_id: str
    title: str
    description: str
    performed_by: str
    status: str
    evidence_required: list[str]


class BankStaffOnboardingModelResponse(BaseModel):
    title: str
    description: str
    onboarding_steps: list[OnboardingStep]
    credential_model: list[str]
    strong_authentication_model: list[str]
    digital_assets_eligibility_model: list[str]
    boundary_note: str


class BankCustomerRecordResponse(BaseModel):
    customer_id: str
    bank_user_id: str
    name: str
    relationship_status: str
    identity_verification_status: str
    residency_status: str
    source_of_funds_status: str
    account_id: str
    online_banking_enabled: bool
    strong_authentication_enabled: bool
    digital_assets_eligible: bool
    staff_review_status: str
    notes: list[str]
