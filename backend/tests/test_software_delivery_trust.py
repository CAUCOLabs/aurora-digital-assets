from tests.helpers import request_json


def test_software_delivery_trust_control_matrix():
    status, data = request_json("GET", "/api/software-delivery-trust/control-matrix")

    assert status == 200
    assert "issue_evaluation_controls" in data
    assert "project_evaluation_controls" in data
    assert "release_gate_controls" in data
    assert "evidence_readiness" in data["control_domains"]
    assert "traceability_readiness" in data["control_domains"]
    assert "test_coverage_readiness" in data["control_domains"]


def test_high_quality_issue_ready_for_internal_review():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-issue",
        {
            "issue_key": "QALENS-101",
            "issue_type": "Story",
            "project_key": "QALENS",
            "requirement_quality": 92,
            "acceptance_criteria_readiness": 90,
            "test_coverage_readiness": 88,
            "evidence_readiness": 86,
            "traceability_score": 89,
            "trust_readiness": 91,
            "quality_gate": "READY",
            "risk_level": "low",
            "ai_analysis_available": True,
            "suggested_test_cases_count": 5,
            "linked_parent": True,
            "linked_epic": True,
            "linked_subtasks_count": 2,
            "linked_issues_count": 3,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_ready_for_internal_review"
    assert data["governance_score"] >= 85
    assert data["release_blocked"] is False
    assert data["audit_event_id"] == "AUD-SOFTWARE-DELIVERY-ISSUE-QALENS-101"
    assert data["correlation_id"] == "CORR-SOFTWARE-DELIVERY-ISSUE-QALENS-101"


def test_issue_blocked_until_clarified():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-issue",
        {
            "issue_key": "QALENS-102",
            "project_key": "QALENS",
            "requirement_quality": 35,
            "acceptance_criteria_readiness": 30,
            "test_coverage_readiness": 25,
            "evidence_readiness": 20,
            "traceability_score": 30,
            "trust_readiness": 25,
            "quality_gate": "BLOCKED_UNTIL_CLARIFIED",
            "risk_level": "high",
            "missing_information": ["acceptance criteria missing"],
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_blocked_until_clarified"
    assert data["release_blocked"] is True
    assert data["review_required"] is True
    assert "quality_gate_blocked_until_clarified" in data["blocking_reasons"]


def test_issue_blocked_until_evidence_ready():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-issue",
        {
            "issue_key": "QALENS-103",
            "project_key": "QALENS",
            "requirement_quality": 85,
            "acceptance_criteria_readiness": 85,
            "test_coverage_readiness": 85,
            "evidence_readiness": 45,
            "traceability_score": 85,
            "trust_readiness": 85,
            "quality_gate": "READY",
            "risk_level": "medium",
            "ai_analysis_available": True,
            "suggested_test_cases_count": 4,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_blocked_until_evidence_ready"
    assert "evidence_readiness" in data["missing_controls"]
    assert data["evidence_required"] is True


def test_issue_blocked_until_traceability_ready():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-issue",
        {
            "issue_key": "QALENS-104",
            "project_key": "QALENS",
            "requirement_quality": 85,
            "acceptance_criteria_readiness": 85,
            "test_coverage_readiness": 85,
            "evidence_readiness": 85,
            "traceability_score": 40,
            "trust_readiness": 85,
            "quality_gate": "READY",
            "risk_level": "medium",
            "ai_analysis_available": True,
            "suggested_test_cases_count": 4,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_blocked_until_traceability_ready"
    assert "traceability_readiness" in data["missing_controls"]


def test_issue_blocked_until_test_coverage_ready():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-issue",
        {
            "issue_key": "QALENS-105",
            "project_key": "QALENS",
            "requirement_quality": 85,
            "acceptance_criteria_readiness": 85,
            "test_coverage_readiness": 40,
            "evidence_readiness": 85,
            "traceability_score": 85,
            "trust_readiness": 85,
            "quality_gate": "READY",
            "risk_level": "medium",
            "ai_analysis_available": True,
            "suggested_test_cases_count": 4,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_blocked_until_test_coverage_ready"
    assert "test_coverage_readiness" in data["missing_controls"]


def test_project_blocked_by_quality_gate():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-project",
        {
            "project_key": "QALENS",
            "issue_count": 12,
            "average_requirement_quality": 82,
            "average_acceptance_criteria_readiness": 80,
            "average_test_coverage_readiness": 78,
            "average_evidence_readiness": 75,
            "average_traceability_score": 76,
            "average_trust_readiness": 80,
            "blocked_issues_count": 2,
            "review_required_issues_count": 3,
            "high_risk_issues_count": 1,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_blocked_until_quality_gate_ready"
    assert data["release_blocked"] is True
    assert data["audit_event_id"] == "AUD-SOFTWARE-DELIVERY-PROJECT-QALENS"


def test_project_ready_for_internal_review():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/evaluate-project",
        {
            "project_key": "QALENS",
            "issue_count": 12,
            "average_requirement_quality": 92,
            "average_acceptance_criteria_readiness": 90,
            "average_test_coverage_readiness": 89,
            "average_evidence_readiness": 88,
            "average_traceability_score": 90,
            "average_trust_readiness": 91,
            "blocked_issues_count": 0,
            "review_required_issues_count": 0,
            "high_risk_issues_count": 0,
        },
    )

    assert status == 200
    assert data["governance_decision"] == "software_delivery_ready_for_internal_review"
    assert data["project_score"] >= 85


def test_release_gate_blocked_until_evidence_ready():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/release-gate",
        {
            "release_id": "REL-QALENS-001",
            "project_key": "QALENS",
            "project_score": 90,
            "average_trust_readiness": 90,
            "average_evidence_readiness": 90,
            "average_traceability_score": 90,
            "average_test_coverage_readiness": 90,
            "blocked_issues_count": 0,
            "high_risk_issues_count": 0,
            "evidence_package_ready": False,
            "human_review_completed": True,
            "change_control_approved": True,
            "regulatory_disclaimer_present": True,
        },
    )

    assert status == 200
    assert data["release_gate_decision"] == "software_delivery_blocked_until_evidence_ready"
    assert data["evidence_required"] is True
    assert data["release_blocked"] is True


def test_release_gate_ready_for_internal_review():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/release-gate",
        {
            "release_id": "REL-QALENS-002",
            "project_key": "QALENS",
            "project_score": 92,
            "average_trust_readiness": 91,
            "average_evidence_readiness": 90,
            "average_traceability_score": 90,
            "average_test_coverage_readiness": 89,
            "blocked_issues_count": 0,
            "high_risk_issues_count": 0,
            "evidence_package_ready": True,
            "human_review_completed": True,
            "change_control_approved": True,
            "regulatory_disclaimer_present": True,
        },
    )

    assert status == 200
    assert data["release_gate_decision"] == "software_delivery_ready_for_internal_review"
    assert data["release_score"] >= 85
    assert data["release_blocked"] is False


def test_governance_summary():
    status, data = request_json(
        "POST",
        "/api/software-delivery-trust/governance-summary",
        {
            "target_id": "QALENS-101",
            "target_type": "issue",
            "governance_decision": "software_delivery_ready_for_internal_review",
            "governance_score": 90,
        },
    )

    assert status == 200
    assert data["summary_id"] == "SUMMARY-SOFTWARE-DELIVERY-ISSUE-QALENS-101"
    assert "Software delivery trust summary" in data["title"]
    assert "Local deterministic software delivery trust evaluation only" in data["safety_notice"]
