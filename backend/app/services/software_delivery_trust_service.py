from datetime import datetime, timezone
import re

from app.schemas.software_delivery_trust import (
    SoftwareDeliveryGovernanceSummaryRequest,
    SoftwareDeliveryGovernanceSummaryResponse,
    SoftwareDeliveryIssueEvaluationRequest,
    SoftwareDeliveryIssueEvaluationResponse,
    SoftwareDeliveryProjectEvaluationRequest,
    SoftwareDeliveryProjectEvaluationResponse,
    SoftwareDeliveryReleaseGateRequest,
    SoftwareDeliveryReleaseGateResponse,
)

SAFETY_NOTICE = (
    "Local deterministic software delivery trust evaluation only. No real QALens, Jira, Git, "
    "CI/CD, deployment, banking, custody, PSP, digital euro, blockchain, cloud, customer data, "
    "private key, credential, secret, production release, or external execution is used or performed. "
    "This is not legal advice, regulatory certification, or production release approval."
)

CONTROL_DOMAINS = [
    "requirement_quality",
    "acceptance_criteria_readiness",
    "test_coverage_readiness",
    "evidence_readiness",
    "traceability_readiness",
    "trust_readiness",
    "risk_level",
    "quality_gate",
    "project_readiness",
    "release_readiness",
    "ai_analysis_quality",
    "compliance_alignment",
    "security_review",
    "auditability",
    "change_control",
    "human_review",
    "agent_review",
    "regulatory_disclaimer",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "-", value.strip().upper()).strip("-")
    return cleaned or "UNKNOWN"


def clamp_score(value: float) -> int:
    return max(0, min(100, int(round(value))))


def level_for(score: int) -> str:
    if score >= 85:
        return "high"
    if score >= 65:
        return "medium"
    if score >= 40:
        return "elevated"
    return "blocked"


def control_matrix() -> dict:
    return {
        "phase": 28,
        "name": "Software Delivery Trust Gateway",
        "control_domains": CONTROL_DOMAINS,
        "issue_evaluation_controls": [
            "requirement_quality",
            "acceptance_criteria_readiness",
            "test_coverage_readiness",
            "evidence_readiness",
            "traceability_readiness",
            "trust_readiness",
            "quality_gate",
        ],
        "project_evaluation_controls": [
            "project_readiness",
            "blocked_issues_count",
            "review_required_issues_count",
            "high_risk_issues_count",
            "critical_risks",
        ],
        "release_gate_controls": [
            "release_readiness",
            "evidence_package_ready",
            "human_review_completed",
            "change_control_approved",
            "regulatory_disclaimer_present",
        ],
        "safety_notice": SAFETY_NOTICE,
    }


def evaluate_issue(req: SoftwareDeliveryIssueEvaluationRequest) -> SoftwareDeliveryIssueEvaluationResponse:
    score = (
        req.requirement_quality * 0.20
        + req.acceptance_criteria_readiness * 0.15
        + req.test_coverage_readiness * 0.20
        + req.evidence_readiness * 0.20
        + req.traceability_score * 0.15
        + req.trust_readiness * 0.10
    )

    missing_controls: list[str] = []
    blocking_reasons: list[str] = []
    satisfied_controls: list[str] = []

    thresholds = [
        ("requirement_quality", req.requirement_quality),
        ("acceptance_criteria_readiness", req.acceptance_criteria_readiness),
        ("test_coverage_readiness", req.test_coverage_readiness),
        ("evidence_readiness", req.evidence_readiness),
        ("traceability_readiness", req.traceability_score),
        ("trust_readiness", req.trust_readiness),
    ]

    for control, value in thresholds:
        if value >= 60:
            satisfied_controls.append(control)
        else:
            missing_controls.append(control)

    if req.quality_gate == "BLOCKED_UNTIL_CLARIFIED":
        score -= 30
        blocking_reasons.append("quality_gate_blocked_until_clarified")
    elif req.quality_gate == "BLOCKED_UNTIL_EVIDENCE_READY":
        score -= 25
        blocking_reasons.append("quality_gate_blocked_until_evidence_ready")
    elif req.quality_gate == "BLOCKED_UNTIL_TRACEABILITY_READY":
        score -= 25
        blocking_reasons.append("quality_gate_blocked_until_traceability_ready")
    elif req.quality_gate == "BLOCKED_UNTIL_TEST_COVERAGE_READY":
        score -= 25
        blocking_reasons.append("quality_gate_blocked_until_test_coverage_ready")

    if req.risk_level.lower() == "high":
        score -= 10
        blocking_reasons.append("high_risk_level")
    elif req.risk_level.lower() == "critical":
        score -= 25
        blocking_reasons.append("critical_risk_level")

    if not req.ai_analysis_available:
        score -= 5
        missing_controls.append("ai_analysis_quality")
    if req.suggested_test_cases_count == 0:
        score -= 10
        missing_controls.append("test_case_generation")
    if req.blocking_risks:
        score -= 10
        blocking_reasons.append("blocking_risks_present")
    if req.missing_information:
        score -= 10
        blocking_reasons.append("missing_information_present")

    governance_score = clamp_score(score)

    if req.quality_gate == "BLOCKED_UNTIL_CLARIFIED":
        decision = "software_delivery_blocked_until_clarified"
    elif req.evidence_readiness < 60:
        decision = "software_delivery_blocked_until_evidence_ready"
        blocking_reasons.append("evidence_readiness_below_threshold")
    elif req.traceability_score < 60:
        decision = "software_delivery_blocked_until_traceability_ready"
        blocking_reasons.append("traceability_readiness_below_threshold")
    elif req.test_coverage_readiness < 60:
        decision = "software_delivery_blocked_until_test_coverage_ready"
        blocking_reasons.append("test_coverage_readiness_below_threshold")
    elif governance_score < 40:
        decision = "software_delivery_governance_blocked"
    elif governance_score < 85 or blocking_reasons:
        decision = "software_delivery_review_required"
    else:
        decision = "software_delivery_ready_for_internal_review"

    evidence_required = req.evidence_readiness < 85 or "evidence_readiness" in missing_controls
    review_required = decision != "software_delivery_ready_for_internal_review"
    release_blocked = decision not in {
        "software_delivery_ready_for_internal_review",
        "software_delivery_review_required",
    }

    actions = []
    if "evidence_readiness" in missing_controls:
        actions.append("Prepare evidence package before release review.")
    if "traceability_readiness" in missing_controls:
        actions.append("Link parent, epic, subtasks, issues, and delivery evidence.")
    if "test_coverage_readiness" in missing_controls or "test_case_generation" in missing_controls:
        actions.append("Add test cases and improve coverage readiness.")
    if req.missing_information:
        actions.append("Clarify missing requirements before quality gate approval.")
    if not actions:
        actions.append("Route software delivery for internal trust review.")

    safe = safe_id(req.issue_key)
    return SoftwareDeliveryIssueEvaluationResponse(
        issue_key=req.issue_key,
        project_key=req.project_key,
        governance_decision=decision,
        governance_score=governance_score,
        governance_level=level_for(governance_score),
        quality_gate=req.quality_gate,
        satisfied_controls=sorted(set(satisfied_controls)),
        missing_controls=sorted(set(missing_controls)),
        blocking_reasons=sorted(set(blocking_reasons)),
        recommended_next_actions=actions,
        evidence_required=evidence_required,
        review_required=review_required,
        release_blocked=release_blocked,
        audit_event_created=True,
        audit_event_id=f"AUD-SOFTWARE-DELIVERY-ISSUE-{safe}",
        correlation_id=f"CORR-SOFTWARE-DELIVERY-ISSUE-{safe}",
        safety_notice=SAFETY_NOTICE,
        created_at=now_iso(),
    )


def evaluate_project(req: SoftwareDeliveryProjectEvaluationRequest) -> SoftwareDeliveryProjectEvaluationResponse:
    score = (
        req.average_requirement_quality
        + req.average_acceptance_criteria_readiness
        + req.average_test_coverage_readiness
        + req.average_evidence_readiness
        + req.average_traceability_score
        + req.average_trust_readiness
    ) / 6

    missing_controls = []
    blocking_reasons = []

    if req.blocked_issues_count > 0:
        score -= 20
        blocking_reasons.append("blocked_issues_present")
    if req.review_required_issues_count > 0:
        score -= 10
        blocking_reasons.append("review_required_issues_present")
    if req.high_risk_issues_count > 0:
        score -= 15
        blocking_reasons.append("high_risk_issues_present")
    if req.critical_risks:
        score -= 25
        blocking_reasons.append("critical_risks_present")

    if req.average_evidence_readiness < 60:
        missing_controls.append("evidence_readiness")
    if req.average_traceability_score < 60:
        missing_controls.append("traceability_readiness")
    if req.average_test_coverage_readiness < 60:
        missing_controls.append("test_coverage_readiness")

    project_score = clamp_score(score)

    if req.blocked_issues_count > 0:
        decision = "software_delivery_blocked_until_quality_gate_ready"
    elif req.average_evidence_readiness < 60:
        decision = "software_delivery_blocked_until_evidence_ready"
    elif req.average_traceability_score < 60:
        decision = "software_delivery_blocked_until_traceability_ready"
    elif req.average_test_coverage_readiness < 60:
        decision = "software_delivery_blocked_until_test_coverage_ready"
    elif project_score >= 85 and not blocking_reasons:
        decision = "software_delivery_ready_for_internal_review"
    elif project_score >= 40:
        decision = "software_delivery_review_required"
    else:
        decision = "software_delivery_governance_blocked"

    safe = safe_id(req.project_key)
    return SoftwareDeliveryProjectEvaluationResponse(
        project_key=req.project_key,
        governance_decision=decision,
        project_score=project_score,
        project_level=level_for(project_score),
        blocking_reasons=sorted(set(blocking_reasons)),
        missing_controls=sorted(set(missing_controls)),
        recommended_next_actions=["Resolve blocked issues and prepare review-ready delivery evidence."],
        evidence_required=req.average_evidence_readiness < 85,
        review_required=decision != "software_delivery_ready_for_internal_review",
        release_blocked=decision != "software_delivery_ready_for_internal_review",
        audit_event_created=True,
        audit_event_id=f"AUD-SOFTWARE-DELIVERY-PROJECT-{safe}",
        correlation_id=f"CORR-SOFTWARE-DELIVERY-PROJECT-{safe}",
        safety_notice=SAFETY_NOTICE,
        created_at=now_iso(),
    )


def evaluate_release_gate(req: SoftwareDeliveryReleaseGateRequest) -> SoftwareDeliveryReleaseGateResponse:
    score = (
        req.project_score * 0.30
        + req.average_trust_readiness * 0.20
        + req.average_evidence_readiness * 0.20
        + req.average_traceability_score * 0.15
        + req.average_test_coverage_readiness * 0.15
    )

    missing_controls = []
    blocking_reasons = []

    if req.blocked_issues_count > 0:
        score -= 30
        blocking_reasons.append("blocked_issues_present")
    if req.high_risk_issues_count > 0:
        score -= 15
        blocking_reasons.append("high_risk_issues_present")
    if req.unresolved_critical_risks:
        score -= 30
        blocking_reasons.append("unresolved_critical_risks_present")
    if not req.evidence_package_ready:
        score -= 20
        missing_controls.append("evidence_package_ready")
    if not req.human_review_completed:
        score -= 15
        missing_controls.append("human_review_completed")
    if not req.change_control_approved:
        score -= 20
        missing_controls.append("change_control_approved")
    if not req.regulatory_disclaimer_present:
        score -= 20
        missing_controls.append("regulatory_disclaimer_present")

    release_score = clamp_score(score)

    if req.blocked_issues_count > 0:
        decision = "software_delivery_blocked_until_quality_gate_ready"
    elif req.unresolved_critical_risks:
        decision = "software_delivery_governance_blocked"
    elif not req.evidence_package_ready:
        decision = "software_delivery_blocked_until_evidence_ready"
    elif not req.change_control_approved:
        decision = "software_delivery_blocked_until_release_ready"
    elif release_score >= 85 and not missing_controls and not blocking_reasons:
        decision = "software_delivery_ready_for_internal_review"
    elif release_score >= 40:
        decision = "software_delivery_review_required"
    else:
        decision = "software_delivery_governance_blocked"

    safe_release = safe_id(req.release_id)
    return SoftwareDeliveryReleaseGateResponse(
        release_id=req.release_id,
        project_key=req.project_key,
        release_gate_decision=decision,
        release_score=release_score,
        release_level=level_for(release_score),
        blocking_reasons=sorted(set(blocking_reasons)),
        missing_controls=sorted(set(missing_controls)),
        recommended_next_actions=["Resolve release gate blockers before production approval."],
        evidence_required=not req.evidence_package_ready,
        review_required=decision != "software_delivery_ready_for_internal_review",
        release_blocked=decision != "software_delivery_ready_for_internal_review",
        audit_event_created=True,
        audit_event_id=f"AUD-SOFTWARE-DELIVERY-RELEASE-{safe_release}",
        correlation_id=f"CORR-SOFTWARE-DELIVERY-RELEASE-{safe_release}",
        safety_notice=SAFETY_NOTICE,
        created_at=now_iso(),
    )


def governance_summary(req: SoftwareDeliveryGovernanceSummaryRequest) -> SoftwareDeliveryGovernanceSummaryResponse:
    target_type = safe_id(req.target_type)
    target_id = safe_id(req.target_id)
    return SoftwareDeliveryGovernanceSummaryResponse(
        summary_id=f"SUMMARY-SOFTWARE-DELIVERY-{target_type}-{target_id}",
        title=f"Software delivery trust summary for {req.target_id}",
        target_id=req.target_id,
        target_type=req.target_type,
        summary_points=[
            f"Governance decision: {req.governance_decision}",
            f"Governance score: {req.governance_score}",
            "Software delivery trust signals are evaluated as deterministic prototype controls.",
        ],
        risk_notes=[
            "This summary does not approve a real production release.",
            "Human review, evidence readiness, and change control remain required for regulated operations.",
        ],
        required_next_steps=[
            "Review missing controls.",
            "Prepare evidence package.",
            "Route to internal governance review.",
        ],
        safety_notice=SAFETY_NOTICE,
        created_at=now_iso(),
    )
