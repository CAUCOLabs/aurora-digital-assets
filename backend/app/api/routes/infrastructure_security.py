from fastapi import APIRouter

from app.schemas.infrastructure_security import (
    EvaluateInfrastructureSecurityScenarioRequest,
    EvaluateInfrastructureSecurityScenarioResponse,
    InfrastructureSecurityControl,
    InfrastructureSecurityEvent,
    InfrastructureSecurityLayer,
    InfrastructureSecurityScenario,
)
from app.services.infrastructure_security_service import (
    infrastructure_security_service,
)


router = APIRouter(
    prefix="/infrastructure-security",
    tags=["infrastructure security"],
)


@router.get("/controls", response_model=list[InfrastructureSecurityControl])
def list_controls() -> list[InfrastructureSecurityControl]:
    return infrastructure_security_service.list_controls()


@router.get("/events", response_model=list[InfrastructureSecurityEvent])
def list_events() -> list[InfrastructureSecurityEvent]:
    return infrastructure_security_service.list_events()


@router.get("/layers", response_model=list[InfrastructureSecurityLayer])
def list_layers() -> list[InfrastructureSecurityLayer]:
    return infrastructure_security_service.list_layers()


@router.get("/scenarios", response_model=list[InfrastructureSecurityScenario])
def list_scenarios() -> list[InfrastructureSecurityScenario]:
    return infrastructure_security_service.list_scenarios()


@router.post(
    "/evaluate-scenario",
    response_model=EvaluateInfrastructureSecurityScenarioResponse,
)
def evaluate_scenario(
    request: EvaluateInfrastructureSecurityScenarioRequest,
) -> EvaluateInfrastructureSecurityScenarioResponse:
    return infrastructure_security_service.evaluate_scenario(
        scenario_id=request.scenario_id,
        object_authorization_failed=request.object_authorization_failed,
        unsafe_template_input_detected=request.unsafe_template_input_detected,
        pod_privileged=request.pod_privileged,
        service_account_can_read_secrets=request.service_account_can_read_secrets,
        cloud_iam_wildcard_permissions=request.cloud_iam_wildcard_permissions,
        weak_trust_policy=request.weak_trust_policy,
        secret_exposure_detected=request.secret_exposure_detected,
        storage_public_access_detected=request.storage_public_access_detected,
        certificate_exposure_detected=request.certificate_exposure_detected,
        service_principal_overprivileged=request.service_principal_overprivileged,
        deployment_credentials_enabled=request.deployment_credentials_enabled,
        managed_identity_excessive_scope=request.managed_identity_excessive_scope,
        password_reset_privilege_detected=request.password_reset_privilege_detected,
        identity_monitoring_gap=request.identity_monitoring_gap,
        dockerfile_secrets_detected=request.dockerfile_secrets_detected,
        image_uses_latest_tag=request.image_uses_latest_tag,
        container_runs_as_root=request.container_runs_as_root,
        plaintext_secrets_in_manifest=request.plaintext_secrets_in_manifest,
        missing_security_context=request.missing_security_context,
        service_account_token_mounted=request.service_account_token_mounted,
        rbac_wildcard_permissions=request.rbac_wildcard_permissions,
        can_read_kubernetes_secrets=request.can_read_kubernetes_secrets,
        network_policy_missing=request.network_policy_missing,
        resource_limits_missing=request.resource_limits_missing,
        cis_audit_missing=request.cis_audit_missing,
        hardening_verification_missing=request.hardening_verification_missing,
    )
