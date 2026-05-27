from app.schemas.bank_access import (
    BankIntegrationModelResponse,
    BankSessionModelResponse,
    IntegrationLayer,
)


class BankAccessService:
    """Provides deterministic bank integration boundary content for the prototype."""

    def get_session_model(self) -> BankSessionModelResponse:
        return BankSessionModelResponse(
            title="Bank-managed customer access",
            description=(
                "Aurora Digital Assets assumes that the customer already has an "
                "active banking relationship and bank-issued online banking "
                "credentials."
            ),
            customer_access_steps=[
                "Customer opens a bank account through the bank's formal onboarding process.",
                "Identity, documents, residency, and source-of-funds information are reviewed by the bank.",
                "The bank issues online banking credentials to the customer.",
                "The customer signs in using a bank-issued user identifier and secret credential.",
                "The sign-in is confirmed using strong authentication, such as a mobile key or banking authentication application.",
                "Only after a valid banking session is established can the customer access eligible digital asset services.",
            ],
            authentication_controls=[
                "Bank-issued customer identifier",
                "Secret credential or PIN known only to the customer",
                "Strong customer authentication",
                "Mobile approval flow",
                "Session timeout and re-authentication",
            ],
            session_controls=[
                "No direct customer signup inside Aurora Digital Assets",
                "Digital assets access depends on the existing banking relationship",
                "Sensitive actions can require additional confirmation",
                "Higher-risk requests can trigger compliance review",
                "Audit events are recorded for evaluated digital asset actions",
            ],
            boundary_note=(
                "Aurora Digital Assets does not replace bank onboarding, customer "
                "identity verification, account opening, or strong authentication. "
                "It is designed as a module that could operate after the bank has "
                "established a valid customer relationship and authenticated session."
            ),
        )

    def get_integration_model(self) -> BankIntegrationModelResponse:
        return BankIntegrationModelResponse(
            title="Bank infrastructure integration model",
            description=(
                "Aurora Digital Assets is modelled as a protected module within "
                "the bank's existing channels, service boundaries, controls, "
                "and reporting environment."
            ),
            integration_layers=[
                IntegrationLayer(
                    name="Customer channels",
                    responsibility="Customer-facing web and mobile banking channels.",
                    examples=[
                        "Online banking portal",
                        "Mobile banking application",
                        "Digital Assets module entry point",
                    ],
                ),
                IntegrationLayer(
                    name="Authentication and session layer",
                    responsibility=(
                        "Validates that the customer has an authenticated bank "
                        "session before protected services are available."
                    ),
                    examples=[
                        "Bank-issued credentials",
                        "Strong customer authentication",
                        "Mobile approval",
                        "Session management",
                    ],
                ),
                IntegrationLayer(
                    name="API gateway and service layer",
                    responsibility=(
                        "Routes banking and digital asset requests to backend "
                        "services and enforces service boundaries."
                    ),
                    examples=[
                        "Accounts API",
                        "Payments API",
                        "Digital Assets API",
                        "Review Cases API",
                        "Audit Events API",
                    ],
                ),
                IntegrationLayer(
                    name="Core banking and account ledger",
                    responsibility=(
                        "Maintains customer accounts, balances, account status, "
                        "and account transactions."
                    ),
                    examples=[
                        "Current account",
                        "Book balance",
                        "Available balance",
                        "Account transaction history",
                    ],
                ),
                IntegrationLayer(
                    name="Payments engine",
                    responsibility=(
                        "Evaluates and routes payment instructions through the "
                        "bank's existing payment infrastructure."
                    ),
                    examples=[
                        "EUR bank transfers",
                        "Invoice payment references",
                        "Payment status",
                        "Payment audit trail",
                    ],
                ),
                IntegrationLayer(
                    name="Compliance, fraud, and risk controls",
                    responsibility=(
                        "Evaluates higher-risk activity and supports human-review "
                        "workflows."
                    ),
                    examples=[
                        "Transaction monitoring",
                        "Fraud controls",
                        "AML review concept",
                        "Manual review cases",
                        "Reviewer decisions",
                    ],
                ),
                IntegrationLayer(
                    name="Reporting and evidence",
                    responsibility=(
                        "Collects audit evidence, review outcomes, and reporting data."
                    ),
                    examples=[
                        "Audit events",
                        "Review cases",
                        "Tax summary concept",
                        "Evidence package preparation",
                    ],
                ),
                IntegrationLayer(
                    name="External payment and settlement rails",
                    responsibility=(
                        "Represents the bank's existing connections to external "
                        "payment and settlement infrastructure."
                    ),
                    examples=[
                        "SEPA credit transfers",
                        "Instant payment rails",
                        "Central bank settlement systems",
                        "Correspondent banking / international messaging where applicable",
                    ],
                ),
            ],
            payment_rails_note=(
                "Aurora Digital Assets does not connect directly to SWIFT, SEPA, "
                "TARGET services, instant payment systems, or any live payment rail. "
                "In a real bank, those connections would be handled by the bank's "
                "existing payment infrastructure and core banking environment."
            ),
            digital_assets_module_note=(
                "Digital asset payment, buy/sell, and withdrawal flows are evaluated "
                "before any hypothetical execution. The current prototype only "
                "creates deterministic decisions, audit events, and review cases."
            ),
            boundary_note=(
                "This prototype models the integration boundary. It does not "
                "implement real payment clearing, settlement, custody, blockchain "
                "execution, AML screening, or customer authentication."
            ),
        )


bank_access_service = BankAccessService()
