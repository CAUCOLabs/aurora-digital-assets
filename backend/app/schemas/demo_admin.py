from pydantic import BaseModel


class DemoStatusResponse(BaseModel):
    audit_events_count: int
    review_cases_count: int
    pending_cases_count: int
    approved_cases_count: int
    rejected_cases_count: int
    database: str
    message: str


class DemoResetResponse(BaseModel):
    status: str
    deleted_audit_events: int
    deleted_review_cases: int
    message: str


class DemoSeedResponse(BaseModel):
    status: str
    created_audit_events: int
    created_review_cases: int
    message: str
