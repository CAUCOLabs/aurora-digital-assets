from app.schemas.bank_staff import (
    BankCustomerRecordResponse,
    BankStaffOnboardingModelResponse,
    OnboardingStep,
)


class BankStaffService:
    """Provides deterministic bank staff onboarding model content."""

    def get_onboarding_model(self) -> BankStaffOnboardingModelResponse:
        return BankStaffOnboardingModelResponse(
            title="Bank staff customer onboarding model",
            description=(
                "Aurora Digital Assets assumes that the customer is created "
                "through a formal bank-managed onboarding process before any "
                "online banking or digital asset services are available."
            ),
            onboarding_steps=[
                OnboardingStep(
                    step_id="A",
                    title="Identity and document review",
                    description=(
                        "Bank staff review identity documents and basic "
                        "customer information before a relationship is created."
                    ),
                    performed_by="Bank staff",
                    status="Required",
                    evidence_required=[
                        "Passport or national identity document",
                        "Personal identity information",
                        "Contact information",
                    ],
                ),
                OnboardingStep(
                    step_id="B",
                    title="Residency and customer relationship review",
                    description=(
                        "Bank staff confirm residency or another valid basis "
                        "for the customer relationship."
                    ),
                    performed_by="Bank staff",
                    status="Required",
                    evidence_required=[
                        "Finnish residency or valid customer basis",
                        "Address information",
                        "Customer relationship purpose",
                    ],
                ),
                OnboardingStep(
                    step_id="C",
                    title="Income and source-of-funds review",
                    description=(
                        "Bank staff review income information, source of "
                        "funds, and expected account usage."
                    ),
                    performed_by="Bank staff",
                    status="Required",
                    evidence_required=[
                        "Salary information or income evidence",
                        "Source-of-funds explanation",
                        "Expected account usage",
                    ],
                ),
                OnboardingStep(
                    step_id="D",
                    title="Account relationship creation",
                    description=(
                        "The bank creates the customer and account relationship "
                        "inside bank-controlled systems."
                    ),
                    performed_by="Bank staff",
                    status="Bank-controlled",
                    evidence_required=[
                        "Customer record",
                        "Account agreement",
                        "Banking service terms",
                    ],
                ),
                OnboardingStep(
                    step_id="E",
                    title="Bank-issued customer identifier",
                    description=(
                        "The bank issues the customer identifier used for "
                        "simulated online banking access."
                    ),
                    performed_by="Bank system / Bank staff",
                    status="Issued by bank",
                    evidence_required=[
                        "Customer ID",
                        "Account ID",
                        "Online banking access status",
                    ],
                ),
                OnboardingStep(
                    step_id="F",
                    title="Private PIN / secret credential setup",
                    description=(
                        "The customer sets the secret credential privately. "
                        "Staff do not see or record it."
                    ),
                    performed_by="Customer",
                    status="Private customer action",
                    evidence_required=[
                        "Customer enters PIN privately",
                        "Staff must not see the secret credential",
                        "Credential is not displayed back to staff",
                    ],
                ),
                OnboardingStep(
                    step_id="G",
                    title="Strong authentication activation",
                    description=(
                        "Bank staff and the customer activate a strong "
                        "authentication method before protected services are used."
                    ),
                    performed_by="Bank staff and customer",
                    status="Required",
                    evidence_required=[
                        "Mobile key / banking authentication app activation",
                        "Device approval setup",
                        "Strong customer authentication enabled",
                    ],
                ),
                OnboardingStep(
                    step_id="H",
                    title="Digital Assets eligibility check",
                    description=(
                        "The bank system or compliance function evaluates "
                        "eligibility before Digital Assets access is available."
                    ),
                    performed_by="Bank system / Compliance",
                    status="Conditional",
                    evidence_required=[
                        "Active banking relationship",
                        "Identity verification completed",
                        "Source-of-funds reviewed",
                        "Strong authentication enabled",
                        "Digital assets terms acknowledged",
                    ],
                ),
            ],
            credential_model=[
                "The bank issues the customer identifier.",
                "The customer defines the secret PIN or credential privately.",
                "Bank staff must not see or record the customer's secret credential.",
                "The credential is used only as part of the simulated eBanking login flow.",
                "This prototype stores only deterministic demo data and does not implement production credential security.",
            ],
            strong_authentication_model=[
                "Strong authentication is required before accessing protected banking services.",
                "A simulated mobile key approval represents the second factor.",
                "Successful approval creates a simulated banking session.",
                "Sensitive actions can still require additional confirmation or review.",
            ],
            digital_assets_eligibility_model=[
                "Digital Assets access is available only after a valid banking relationship exists.",
                "Eligibility depends on completed identity verification and source-of-funds review.",
                "High-risk digital asset actions can create review cases.",
                "Audit events are persisted for evaluated actions.",
            ],
            boundary_note=(
                "This prototype does not implement real customer onboarding, "
                "real identity verification, real credential issuance, real "
                "source-of-funds checks, or real strong authentication. It "
                "models how Aurora Digital Assets would sit after those "
                "bank-managed controls."
            ),
        )

    def get_customer_record(self) -> BankCustomerRecordResponse:
        return BankCustomerRecordResponse(
            customer_id="CUST-DA-2026-001",
            bank_user_id="12345678",
            name="Claudio Demo",
            relationship_status="Active",
            identity_verification_status="Completed by bank",
            residency_status="Finland resident",
            source_of_funds_status="Reviewed by bank",
            account_id="aurora-current",
            online_banking_enabled=True,
            strong_authentication_enabled=True,
            digital_assets_eligible=True,
            staff_review_status="Completed",
            notes=[
                "Customer relationship created through bank-managed onboarding.",
                "Online banking credentials issued by the bank.",
                "PIN setup is treated as a private customer action.",
                "Digital Assets access remains subject to eligibility and review controls.",
            ],
        )


bank_staff_service = BankStaffService()
