from pydantic import BaseModel


class BankSessionModelResponse(BaseModel):
    title: str
    description: str
    customer_access_steps: list[str]
    authentication_controls: list[str]
    session_controls: list[str]
    boundary_note: str


class IntegrationLayer(BaseModel):
    name: str
    responsibility: str
    examples: list[str]


class BankIntegrationModelResponse(BaseModel):
    title: str
    description: str
    integration_layers: list[IntegrationLayer]
    payment_rails_note: str
    digital_assets_module_note: str
    boundary_note: str
