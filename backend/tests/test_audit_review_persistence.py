import unittest

from app.schemas.audit_event import AuditEvent
from app.schemas.review_case import ReviewCase
from app.storage.sqlite_store import (
    init_db,
    list_persisted_audit_events,
    list_persisted_review_cases,
    save_audit_event,
    save_review_case,
)
from tests.helpers import request_json


class AuditReviewPersistenceTests(unittest.TestCase):
    def test_audit_events_endpoint_includes_persisted_records(self) -> None:
        request_json(
            "POST",
            "/api/api-security/evaluate-scenario",
            {
                "scenario_id": "graphql_batching_pin_verification",
                "operation_name": "verifyTransferPin",
                "attempts": 8,
                "object_authorized": True,
                "batching_detected": True,
                "sensitive_fields_requested": False,
            },
        )
        request_json(
            "POST",
            "/api/risk-operations/create-review-case",
            {
                "action_id": "RO-ACTION-002",
                "reviewer_id": "reviewer-demo",
                "priority": "urgent",
            },
        )

        status, response = request_json("GET", "/api/audit-events")

        self.assertEqual(status, 200)
        self.assertIsInstance(response, list)
        event_ids = {event["event_id"] for event in response}
        self.assertIn("AUD-API-GRAPHQL-PIN", event_ids)
        self.assertIn("AUD-RISK-RO-ACTION-002", event_ids)
        self.assertTrue(any(event["persisted"] for event in response))

    def test_review_cases_endpoint_includes_persisted_review_case(self) -> None:
        request_json(
            "POST",
            "/api/risk-operations/create-review-case",
            {
                "action_id": "RO-ACTION-002",
                "reviewer_id": "reviewer-demo",
                "priority": "urgent",
            },
        )

        status, response = request_json("GET", "/api/review-cases")

        self.assertEqual(status, 200)
        self.assertIsInstance(response, list)
        matching_cases = [
            review_case
            for review_case in response
            if review_case["source_action_id"] == "RO-ACTION-002"
            and review_case["audit_event_id"] == "AUD-RISK-RO-ACTION-002"
            and review_case["persisted"]
        ]
        self.assertTrue(matching_cases)

    def test_sqlite_storage_helpers_round_trip_records(self) -> None:
        init_db()
        audit_event = AuditEvent(
            event_id="AUD-TEST-STORAGE",
            timestamp="2026-06-15T09:00:00+00:00",
            module="api_security",
            action_type="evaluate_scenario",
            status="created",
            risk_level="medium",
            decision="review_required",
            reasons=["Storage helper test audit event."],
            actor_id="storage-test",
            actor_type="service",
            source_module="api_security",
            action="evaluate_scenario",
            object_type="test_object",
            object_id="storage-test-object",
            severity="medium",
            risk_score=50,
            summary="Storage helper test audit event.",
            correlation_id="CORR-TEST-STORAGE",
            immutable_note="Prototype test record.",
            metadata={"test": True},
        )
        save_audit_event(audit_event)

        review_case = ReviewCase(
            case_id="CASE-TEST-STORAGE",
            created_at="2026-06-15T09:00:00+00:00",
            case_type="storage_test_review",
            title="Storage helper review case",
            status="Pending review",
            risk_level="medium",
            reasons=["Storage helper test review case."],
            customer="Aurora Bank internal prototype",
            action_type="storage_test_case_prepared",
            asset="digital_assets_controls",
            amount=0.0,
            network="internal_review_workflow",
            destination_address="storage-test",
            wallet_type="internal_review",
        )
        save_review_case(
            review_case,
            source_module="risk_operations",
            source_id="storage-test",
            source_action_id="RO-ACTION-TEST",
            reviewer_id="reviewer-demo",
            recommended_next_action="Review storage helper test case.",
            audit_event_id="AUD-TEST-STORAGE",
            correlation_id="CORR-TEST-STORAGE",
            metadata={"test": True},
        )

        audit_events = list_persisted_audit_events()
        review_cases = list_persisted_review_cases()

        self.assertIn(
            "AUD-TEST-STORAGE",
            {event.event_id for event in audit_events},
        )
        self.assertIn(
            "CASE-TEST-STORAGE",
            {case.case_id for case in review_cases},
        )
