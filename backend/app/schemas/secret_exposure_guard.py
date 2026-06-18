from datetime import datetime
from typing import Literal

from pydantic import BaseModel


SecretExposureSeverity = Literal["low", "medium", "high", "critical"]
SecretExposureDecision = Literal[
    "allow",
    "redact",
    "elevate",
    "block",
    "review_required",
]
SecretExposureScope = Literal[
    "internal",
    "public",
    "repository",
    "logs",
    "prompt_context",
    "evidence_package",
    "review_case",
    "unknown",
]


class SecretExposureSurface(BaseModel):
    surface_id: str
    title: str
    category: str
    description: str
    sensitivity_level: SecretExposureSeverity


class SecretExposureGuardEvaluationRequest(BaseModel):
    signal_type: str
    surface_id: str
    source_reference: str | None = None
    actor_type: str = "unknown"
    contains_raw_secret_value: bool = False
    contains_secret_like_pattern: bool = False
    contains_credential_label: bool = False
    contains_private_key_reference: bool = False
    contains_seed_phrase_reference: bool = False
    contains_api_token_reference: bool = False
    contains_cloud_secret_reference: bool = False
    contains_custodian_secret_reference: bool = False
    exposure_scope: SecretExposureScope = "unknown"
    ai_assisted_context: bool = False
    linked_ai_threat_case_id: str | None = None
    reviewer_id: str = "system"


class SecretExposureGuardEvaluationResponse(BaseModel):
    signal_type: str
    surface_id: str
    risk_score: int
    severity: SecretExposureSeverity
    decision: SecretExposureDecision
    secret_value_stored: bool
    raw_secret_echoed: bool
    ai_threat_case_id: str | None = None
    audit_event_created: bool
    audit_event_id: str
    correlation_id: str
    evidence_package_ready: bool
    review_case_required: bool
    review_case_id: str | None = None
    operation_guard_recommended: bool
    recommended_next_actions: list[str]
    created_at: datetime
