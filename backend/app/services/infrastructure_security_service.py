from app.schemas.infrastructure_security import (
    EvaluateInfrastructureSecurityScenarioResponse,
    InfrastructureSecurityControl,
    InfrastructureSecurityEvent,
    InfrastructureSecurityLayer,
    InfrastructureSecurityScenario,
)
from app.services.audit_service import audit_service


AUDIT_IDS_BY_SCENARIO = {
    "object_authorization_to_data_exposure": "AUD-INFRA-OBJECT-AUTH",
    "unsafe_template_to_runtime_exposure": "AUD-INFRA-TEMPLATE",
    "pod_rbac_secret_read": "AUD-INFRA-K8S-SECRETS",
    "weak_irsa_trust_policy": "AUD-INFRA-IAM-TRUST",
    "wildcard_iam_permission": "AUD-INFRA-IAM-WILDCARD",
    "plaintext_secret_exposure": "AUD-INFRA-SECRET",
    "app_to_cloud_chain_reaction": "AUD-INFRA-CHAIN-REACTION",
    "azure_storage_to_identity_chain_reaction": "AUD-INFRA-AZURE-STORAGE-IDENTITY",
    "container_kubernetes_hardening_failure": "AUD-INFRA-K8S-HARDENING-FAILURE",
}

CORRELATION_IDS_BY_SCENARIO = {
    scenario_id: audit_id.replace("AUD-", "CORR-")
    for scenario_id, audit_id in AUDIT_IDS_BY_SCENARIO.items()
}


class InfrastructureSecurityService:
    """Deterministic infrastructure security control center demo service."""

    def list_controls(self) -> list[InfrastructureSecurityControl]:
        return [
            self._control(
                "infrasec-ctrl-object-auth",
                "Object-level authorization guard",
                "application",
                "object_authorization",
                "Prevents authenticated sessions from reading or changing objects outside their ownership or staff authorization scope.",
                ["accounts", "transfers", "reports", "wallets", "KYC documents"],
                "Authenticated identity must match object ownership or staff authorization.",
                ["object_authorization_decision", "access_denial_audit_event"],
            ),
            self._control(
                "infrasec-ctrl-template-safety",
                "Safe template execution control",
                "application",
                "template_safety",
                "Allows user data in approved rendering flows while blocking user-controlled executable templates.",
                ["reports", "invoices", "emails", "PDF generation"],
                "Users may provide data, but not executable templates.",
                ["template_source_record", "escaped_input_record"],
            ),
            self._control(
                "infrasec-ctrl-k8s-rbac",
                "Kubernetes least privilege RBAC",
                "kubernetes",
                "rbac",
                "Restricts simulated web workloads from creating pods, listing secrets, or accessing unrelated namespaces.",
                ["service accounts", "config maps", "pods", "namespaces"],
                "Web workloads must not create pods, list secrets, or access unrelated namespaces.",
                ["rbac_permission_snapshot", "service_account_scope_record"],
            ),
            self._control(
                "infrasec-ctrl-namespace-isolation",
                "Namespace isolation control",
                "kubernetes",
                "namespace_isolation",
                "Keeps application, compliance, and reporting workloads isolated unless a business-approved path exists.",
                ["fintech-app namespace", "compliance namespace", "reporting namespace"],
                "Workloads must not access unrelated namespaces unless explicitly authorized.",
                ["namespace_boundary_record", "cross_namespace_denial"],
            ),
            self._control(
                "infrasec-ctrl-service-account-secrets",
                "Service account secret restriction",
                "kubernetes",
                "service_account",
                "Models a default-deny posture for Kubernetes secret reads by application service accounts.",
                ["Kubernetes secrets", "application credentials", "API tokens"],
                "Service accounts should not read secrets by default.",
                ["secret_read_entitlement_record", "secret_rotation_trigger"],
            ),
            self._control(
                "infrasec-ctrl-iam-trust",
                "Cloud IAM trust policy restriction",
                "cloud_iam",
                "iam_trust",
                "Binds simulated cloud role trust to a specific namespace and service account subject.",
                ["workload identity", "IRSA role", "cloud service role"],
                "Cloud role trust must bind to a specific namespace and service account.",
                ["trust_policy_condition_snapshot", "role_assumption_decision"],
            ),
            self._control(
                "infrasec-ctrl-iam-permissions",
                "Cloud IAM permission scope",
                "cloud_iam",
                "iam_permissions",
                "Requires business-aware cloud permissions scoped to the resources needed by the workload.",
                ["transaction table", "audit table", "reports bucket"],
                "IAM policies must avoid wildcard actions and wildcard resources.",
                ["iam_policy_scope_review", "resource_condition_record"],
            ),
            self._control(
                "infrasec-ctrl-secret-management",
                "Secret management control",
                "secrets",
                "secret_management",
                "Keeps simulated secrets centralized, scoped, rotated, and out of code, runtime logs, and shared configuration.",
                ["API keys", "signing keys", "database credentials", "third-party tokens"],
                "Secrets must be centralized, rotated, scoped, and never logged.",
                ["secret_location_record", "rotation_status_snapshot"],
            ),
            self._control(
                "infrasec-ctrl-audit-correlation",
                "Cross-layer audit correlation",
                "audit",
                "logging",
                "Connects application, Kubernetes, IAM, secrets, and database signals into a single audit trail.",
                [
                    "application logs",
                    "Kubernetes service account usage",
                    "IAM role assumption",
                    "secret access",
                    "database access",
                ],
                "Security events must correlate across application, Kubernetes, IAM, secrets, and data access.",
                ["cross_layer_correlation_id", "audit_event_record"],
            ),
            self._control(
                "infrasec-ctrl-chain-containment",
                "Chain reaction containment",
                "risk_operations",
                "chain_containment",
                "Escalates cross-layer weakness before an application issue can become infrastructure or data compromise.",
                [
                    "backend API",
                    "runtime environment",
                    "cloud identity",
                    "sensitive financial data",
                ],
                "One vulnerable layer must not allow uncontrolled movement to the next layer.",
                ["risk_operations_escalation", "evidence_readiness_flag"],
            ),
            self._control(
                "infrasec-ctrl-dockerfile-hardening",
                "Dockerfile hardening control",
                "kubernetes",
                "dockerfile_hardening",
                "Models Dockerfile review for minimal, reproducible runtime images before deployment.",
                ["container images", "runtime environment", "production services"],
                "A Dockerfile that works is not automatically safe. Runtime images must be pinned, minimal, reproducible, and reviewed.",
                ["dockerfile_review_record", "runtime_image_hardening_evidence"],
            ),
            self._control(
                "infrasec-ctrl-image-secret-exclusion",
                "Image secret exclusion control",
                "secrets",
                "image_secret_exposure",
                "Prevents simulated credential-like values from being represented in image layers, Dockerfiles, manifests, or build artifacts.",
                ["API keys", "database URLs", "JWT secrets", "payment provider tokens"],
                "Secrets must never be baked into Dockerfiles, image layers, manifests, or build artifacts.",
                ["image_secret_exclusion_record", "secret_rotation_trigger"],
            ),
            self._control(
                "infrasec-ctrl-non-root-runtime",
                "Non-root container runtime control",
                "kubernetes",
                "non_root_runtime",
                "Requires business service containers to run without root privileges in the deterministic prototype model.",
                ["container process", "filesystem access", "runtime permissions"],
                "Business services should run as non-root with explicit user and group IDs.",
                ["runtime_user_record", "non_root_enforcement_evidence"],
            ),
            self._control(
                "infrasec-ctrl-minimal-dependency-surface",
                "Minimal dependency surface control",
                "application",
                "dependency_surface",
                "Keeps the simulated application dependency surface intentional, pinned, reviewed, and limited to production needs.",
                ["dependency tree", "package lockfile", "supply chain"],
                "Dependencies should be intentional, pinned, reviewed, scanned, and limited to production needs.",
                ["dependency_inventory", "production_dependency_review"],
            ),
            self._control(
                "infrasec-ctrl-immutable-image-reference",
                "Immutable image reference control",
                "kubernetes",
                "image_version_pinning",
                "Requires production workload references to avoid mutable latest tags in the deterministic manifest model.",
                ["image registry", "deployment traceability"],
                "Production workloads must avoid latest and use pinned versions or immutable digests.",
                ["image_reference_record", "deployment_traceability_record"],
            ),
            self._control(
                "infrasec-ctrl-k8s-security-context",
                "Kubernetes securityContext control",
                "kubernetes",
                "kubernetes_security_context",
                "Models pod and container securityContext hardening for non-root execution and reduced runtime privileges.",
                ["pod runtime", "container runtime"],
                "Workloads should enforce runAsNonRoot, allowPrivilegeEscalation false, readOnlyRootFilesystem true, seccomp RuntimeDefault, and dropped capabilities.",
                ["security_context_snapshot", "runtime_restriction_evidence"],
            ),
            self._control(
                "infrasec-ctrl-service-account-token-control",
                "ServiceAccount token control",
                "kubernetes",
                "service_account_token_control",
                "Prevents simulated business workloads from receiving Kubernetes API tokens when cluster API access is not required.",
                ["Kubernetes API token", "service account identity"],
                "Most business applications should not automatically receive Kubernetes API tokens.",
                ["service_account_token_mount_record", "api_token_justification"],
            ),
            self._control(
                "infrasec-ctrl-k8s-rbac-least-privilege",
                "Kubernetes RBAC least privilege control",
                "kubernetes",
                "kubernetes_rbac_least_privilege",
                "Restricts simulated workload RBAC from wildcard actions, secret reads, pod creation, and cross-namespace access.",
                ["Kubernetes API", "secrets", "configmaps", "pods", "deployments"],
                "Business workloads should not have wildcard RBAC, secret read access, pod creation, or cross-namespace permissions.",
                ["rbac_least_privilege_review", "secret_access_denial_record"],
            ),
            self._control(
                "infrasec-ctrl-network-policy-isolation",
                "NetworkPolicy isolation control",
                "kubernetes",
                "network_policy_isolation",
                "Models default-deny namespace traffic posture and explicit allow paths for required service communication.",
                ["internal services", "databases", "namespaces", "east-west traffic"],
                "A secure cluster denies traffic by default and only allows explicitly required connections.",
                ["network_policy_snapshot", "allowed_traffic_record"],
            ),
            self._control(
                "infrasec-ctrl-resource-limit-enforcement",
                "Resource limit enforcement control",
                "kubernetes",
                "resource_limit_enforcement",
                "Requires simulated workloads to define CPU and memory requests and limits for platform stability.",
                ["node resources", "cluster stability", "workload availability"],
                "Every workload should define CPU and memory requests and limits.",
                ["resource_request_limit_record", "workload_stability_evidence"],
            ),
            self._control(
                "infrasec-ctrl-cluster-cis-audit",
                "Cluster CIS audit control",
                "audit",
                "cluster_cis_audit",
                "Models periodic CIS-style hardening verification evidence without running kube-bench or accessing a cluster.",
                ["API server", "kubelet", "etcd", "node configuration", "control plane configuration"],
                "Cluster hardening should be periodically verified against CIS-style benchmarks such as kube-bench, without giving normal applications elevated host visibility.",
                ["cis_audit_schedule_record", "cluster_hardening_attestation"],
            ),
            self._control(
                "infrasec-ctrl-devsecops-hardening-verification",
                "DevSecOps hardening verification control",
                "audit",
                "devsecops_verification",
                "Requires build and deployment hardening checks to produce deterministic review evidence in the prototype.",
                ["CI/CD pipeline", "deployment manifests", "container images"],
                "Security controls should produce evidence. Builds/deployments should fail if critical hardening controls are missing.",
                ["pipeline_hardening_gate_record", "deployment_verification_evidence"],
            ),
            self._control(
                "infrasec-ctrl-runtime-hardening-evidence",
                "Runtime hardening evidence control",
                "risk_operations",
                "runtime_hardening_evidence",
                "Connects container, Kubernetes, audit, and risk operations evidence for internal review.",
                ["audit trail", "review cases", "runtime hardening posture"],
                "Runtime hardening gaps must preserve evidence and route critical chain risk into review.",
                ["runtime_hardening_evidence_package", "risk_operations_review_case"],
            ),
            self._control(
                "infrasec-ctrl-azure-storage-private",
                "Azure private storage control",
                "secrets",
                "cloud_storage_access",
                "Models private-by-default storage posture for simulated internal financial assets.",
                ["blob containers", "reports", "exports", "backups", "operational files"],
                "Sensitive storage must be private by default. Anonymous public access is not allowed for internal financial assets.",
                ["storage_access_posture_record", "anonymous_access_denial"],
            ),
            self._control(
                "infrasec-ctrl-azure-certificate-protection",
                "Certificate protection control",
                "secrets",
                "certificate_protection",
                "Treats certificates as identity credentials requiring secure secret management.",
                ["service principal certificates", "private keys", "signing credentials"],
                "Certificates are identity credentials and must be stored in secure secret management, not public storage, source code, or deployment folders.",
                ["certificate_location_record", "credential_rotation_record"],
            ),
            self._control(
                "infrasec-ctrl-azure-sp-least-privilege",
                "Service principal least privilege control",
                "cloud_iam",
                "service_principal_least_privilege",
                "Restricts simulated app registrations and automation identities to purpose-specific permissions.",
                ["service principals", "app registrations", "automation identities"],
                "One workload, one identity, one purpose, minimum permissions, specific scope, monitored usage.",
                ["service_principal_scope_review", "role_assignment_snapshot"],
            ),
            self._control(
                "infrasec-ctrl-azure-deployment-access",
                "Deployment access control",
                "cloud_iam",
                "deployment_access_control",
                "Models deployment credentials and CI/CD identities as privileged access paths.",
                ["App Service deployment credentials", "production deployment flows", "CI/CD identities"],
                "Deployment access is privileged access. Basic deployment credentials should be disabled if not required.",
                ["deployment_credential_status", "deployment_change_audit_record"],
            ),
            self._control(
                "infrasec-ctrl-azure-managed-identity-scope",
                "Managed identity scope control",
                "cloud_iam",
                "managed_identity_scope",
                "Requires managed identities to remain narrowly scoped despite reducing stored secrets.",
                ["managed identities", "workload tokens", "cloud resource permissions"],
                "Managed identities reduce stored secrets, but must still be narrowly scoped.",
                ["managed_identity_scope_review", "token_usage_monitoring_record"],
            ),
            self._control(
                "infrasec-ctrl-azure-password-reset-privilege",
                "Password reset privilege control",
                "cloud_iam",
                "privileged_identity_management",
                "Prevents application identities from holding standing identity administration privileges.",
                ["privileged roles", "password reset permissions", "identity administration permissions"],
                "Application identities should not have standing password reset or administrative identity privileges.",
                ["privileged_role_review", "password_reset_permission_record"],
            ),
            self._control(
                "infrasec-ctrl-azure-identity-monitoring",
                "Azure identity monitoring control",
                "audit",
                "identity_monitoring",
                "Models monitoring for abnormal service principal, managed identity, and role assignment behavior.",
                ["service principal sign-ins", "managed identity token usage", "role assignments", "password resets"],
                "Security monitoring must detect abnormal identity behavior early.",
                ["identity_behavior_alert", "role_assignment_audit_record"],
            ),
            self._control(
                "infrasec-ctrl-azure-key-vault-monitoring",
                "Key Vault access monitoring control",
                "secrets",
                "key_vault_monitoring",
                "Models logging and review for secret, certificate, and key access.",
                ["Key Vault secrets", "certificates", "keys"],
                "Secret and certificate access must be logged, monitored, and reviewed.",
                ["key_vault_access_log", "secret_access_review"],
            ),
            self._control(
                "infrasec-ctrl-azure-storage-identity-containment",
                "Storage-to-identity chain containment",
                "risk_operations",
                "storage_identity_chain_containment",
                "Escalates storage exposure before it can become cloud identity compromise.",
                ["storage", "certificates", "service principals", "deployment flows", "managed identities", "privileged roles"],
                "A storage exposure should not become cloud identity compromise.",
                ["risk_operations_escalation", "azure_identity_evidence_readiness_flag"],
            ),
        ]

    def list_events(self) -> list[InfrastructureSecurityEvent]:
        return [
            self._event(
                "INFRASEC-2026-001",
                "Application object authorization failure",
                "application",
                "initial_access",
                "IDOR / object-level authorization failure",
                "critical",
                "block",
                "blocked",
                [
                    "Object-level authorization guard",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "transfer-demo-foreign-object",
                "Authenticated session attempted to access an object outside its authorization scope.",
                "If not blocked, this could expose sensitive financial data and trigger downstream abuse.",
                "Return not found, block disclosure, create audit event, and review object access logic.",
                "AUD-INFRA-OBJECT-AUTH",
                "CORR-INFRA-OBJECT-AUTH",
                "2026-06-14T11:05:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-002",
                "Unsafe template execution attempt",
                "application",
                "privilege_expansion",
                "Server-side template execution risk",
                "high",
                "block",
                "blocked",
                ["Safe template execution control", "Cross-layer audit correlation"],
                "report-renderer",
                "User-controlled input attempted to influence server-side template execution.",
                "Unsafe template execution could expose runtime context, secrets, or service metadata.",
                "Use predefined templates only, escape user data, and audit report generation.",
                "AUD-INFRA-TEMPLATE",
                "CORR-INFRA-TEMPLATE",
                "2026-06-14T11:14:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-003",
                "Service account can read Kubernetes secrets",
                "kubernetes",
                "secret_exposure",
                "Excessive Kubernetes RBAC permission",
                "critical",
                "harden_required",
                "under_review",
                [
                    "Kubernetes least privilege RBAC",
                    "Service account secret restriction",
                    "Chain reaction containment",
                ],
                "web-api service account",
                "The web API workload has a simulated permission allowing secret reads.",
                "A backend compromise could become secret exposure.",
                "Remove secret read permission, scope role to required config only, and rotate exposed secrets if needed.",
                "AUD-INFRA-K8S-SECRETS",
                "CORR-INFRA-K8S-SECRETS",
                "2026-06-14T11:22:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-004",
                "Weak cloud IAM trust policy",
                "cloud_iam",
                "cloud_role_misuse",
                "Weak workload identity trust condition",
                "critical",
                "harden_required",
                "under_review",
                ["Cloud IAM trust policy restriction", "Cross-layer audit correlation"],
                "aurora-web-api-role",
                "The simulated trust policy is not sufficiently bound to namespace and service account.",
                "The wrong workload could assume a cloud role.",
                "Bind trust policy to a specific namespace and service account subject.",
                "AUD-INFRA-IAM-TRUST",
                "CORR-INFRA-IAM-TRUST",
                "2026-06-14T11:31:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-005",
                "Wildcard IAM permission detected",
                "cloud_iam",
                "cloud_role_misuse",
                "Overbroad IAM policy",
                "critical",
                "harden_required",
                "under_review",
                ["Cloud IAM permission scope", "Chain reaction containment"],
                "AuroraTransactions table access",
                "Simulated workload policy contains wildcard-like access that should be narrowed.",
                "Compromised workload could access more resources than required.",
                "Restrict actions, resources, conditions, and environment-specific scope.",
                "AUD-INFRA-IAM-WILDCARD",
                "CORR-INFRA-IAM-WILDCARD",
                "2026-06-14T11:38:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-006",
                "Plaintext secret exposure in runtime configuration",
                "secrets",
                "secret_exposure",
                "Secret management failure",
                "high",
                "harden_required",
                "under_review",
                ["Secret management control", "Cross-layer audit correlation"],
                "api-token-demo",
                "Simulated runtime configuration exposes a plaintext token pattern.",
                "Secret exposure could enable unauthorized downstream service access.",
                "Move secret to managed secret storage, rotate it, and ensure logs never expose it.",
                "AUD-INFRA-SECRET",
                "CORR-INFRA-SECRET",
                "2026-06-14T11:46:00+03:00",
            ),
            self._event(
                "INFRASEC-2026-007",
                "Application-to-cloud chain reaction risk",
                "risk_operations",
                "evidence_required",
                "Cross-layer compromise path",
                "critical",
                "escalate",
                "escalated",
                [
                    "Object-level authorization guard",
                    "Kubernetes least privilege RBAC",
                    "Cloud IAM permission scope",
                    "Secret management control",
                    "Chain reaction containment",
                ],
                "Aurora financial platform control plane",
                "Multiple simulated weak controls could allow an application bug to become an infrastructure incident.",
                "Application issue could move into Kubernetes, IAM, secrets, and sensitive data access.",
                "Escalate to Risk Operations, create audit event, prepare evidence package, and harden controls.",
                "AUD-INFRA-CHAIN-REACTION",
                "CORR-INFRA-CHAIN-REACTION",
                "2026-06-14T11:58:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-001",
                "Secrets detected in container image configuration",
                "secrets",
                "secret_exposure",
                "Secrets baked into image",
                "critical",
                "harden_required",
                "under_review",
                ["Image secret exclusion control", "Dockerfile hardening control"],
                "payments-service-image",
                "A simulated container image contains secret-like configuration values.",
                "If pushed or copied, the image itself becomes a credential exposure risk.",
                "Remove secrets from image layers, rotate exposed credentials, use secure secret management, and scan build artifacts.",
                "AUD-INFRA-K8S-IMAGE-SECRETS",
                "CORR-INFRA-K8S-IMAGE-SECRETS",
                "2026-06-16T09:00:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-002",
                "Container runs as root",
                "kubernetes",
                "privilege_expansion",
                "Root container runtime",
                "high",
                "harden_required",
                "under_review",
                ["Non-root container runtime control", "Kubernetes securityContext control"],
                "payments-service-container",
                "A simulated workload runs without an explicit non-root user.",
                "A compromised app process may have unnecessary container-level privileges.",
                "Set USER in Dockerfile and enforce runAsNonRoot in Kubernetes.",
                "AUD-INFRA-K8S-ROOT-RUNTIME",
                "CORR-INFRA-K8S-ROOT-RUNTIME",
                "2026-06-16T09:08:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-003",
                "Weak Kubernetes securityContext",
                "kubernetes",
                "privilege_expansion",
                "Missing runtime restrictions",
                "critical",
                "harden_required",
                "under_review",
                [
                    "Kubernetes securityContext control",
                    "Non-root container runtime control",
                    "Runtime hardening evidence control",
                ],
                "payments-service-deployment",
                "A simulated deployment is missing key runtime hardening controls.",
                "Missing allowPrivilegeEscalation, readOnlyRootFilesystem, dropped capabilities, or seccomp may increase blast radius.",
                "Enforce securityContext, drop Linux capabilities, disable privilege escalation, use read-only root filesystem, and define controlled writable volumes.",
                "AUD-INFRA-K8S-SECURITY-CONTEXT",
                "CORR-INFRA-K8S-SECURITY-CONTEXT",
                "2026-06-16T09:16:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-004",
                "ServiceAccount token mounted unnecessarily",
                "kubernetes",
                "lateral_movement",
                "Unnecessary Kubernetes API access path",
                "high",
                "review_required",
                "under_review",
                ["ServiceAccount token control", "Kubernetes RBAC least privilege control"],
                "payments-service-account",
                "A simulated business workload receives a Kubernetes API token despite not needing cluster API access.",
                "A compromised workload could become a Kubernetes API client.",
                "Set automountServiceAccountToken false and provide explicit RBAC only when justified.",
                "AUD-INFRA-K8S-SA-TOKEN",
                "CORR-INFRA-K8S-SA-TOKEN",
                "2026-06-16T09:24:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-005",
                "Broad Kubernetes RBAC permission",
                "kubernetes",
                "lateral_movement",
                "RBAC wildcard permission",
                "critical",
                "harden_required",
                "under_review",
                [
                    "Kubernetes RBAC least privilege control",
                    "ServiceAccount token control",
                    "Image secret exclusion control",
                ],
                "payments-service-role",
                "A simulated workload has excessive Kubernetes API permissions.",
                "A compromised pod could list secrets, inspect cluster resources, create jobs, or access unrelated namespaces.",
                "Remove wildcard permissions, deny secret access by default, and scope permissions to exact resources.",
                "AUD-INFRA-K8S-BROAD-RBAC",
                "CORR-INFRA-K8S-BROAD-RBAC",
                "2026-06-16T09:32:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-006",
                "NetworkPolicy missing",
                "kubernetes",
                "lateral_movement",
                "Unrestricted east-west traffic",
                "high",
                "harden_required",
                "under_review",
                ["NetworkPolicy isolation control", "Chain reaction containment"],
                "production namespace",
                "A simulated namespace lacks default-deny NetworkPolicy.",
                "A compromised pod could scan or reach unrelated internal services.",
                "Apply default deny ingress/egress and allow only explicitly required traffic.",
                "AUD-INFRA-K8S-NETWORK-POLICY",
                "CORR-INFRA-K8S-NETWORK-POLICY",
                "2026-06-16T09:40:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-007",
                "Cluster CIS audit missing",
                "kubernetes",
                "evidence_required",
                "Unverified cluster hardening",
                "high",
                "review_required",
                "under_review",
                ["Cluster CIS audit control", "DevSecOps hardening verification control"],
                "kubernetes-cluster-baseline",
                "A simulated Kubernetes environment lacks CIS/kube-bench style audit evidence.",
                "A hardened deployment may still run on a weak cluster configuration.",
                "Schedule controlled CIS benchmark verification and preserve audit evidence.",
                "AUD-INFRA-K8S-CIS-AUDIT",
                "CORR-INFRA-K8S-CIS-AUDIT",
                "2026-06-16T09:48:00+03:00",
            ),
            self._event(
                "INFRASEC-K8S-2026-008",
                "Container-to-cluster hardening failure",
                "risk_operations",
                "evidence_required",
                "Container and Kubernetes hardening chain reaction",
                "critical",
                "escalate",
                "escalated",
                [
                    "Dockerfile hardening control",
                    "Image secret exclusion control",
                    "Non-root container runtime control",
                    "Kubernetes securityContext control",
                    "ServiceAccount token control",
                    "Kubernetes RBAC least privilege control",
                    "NetworkPolicy isolation control",
                    "Resource limit enforcement control",
                    "Cluster CIS audit control",
                    "DevSecOps hardening verification control",
                    "Runtime hardening evidence control",
                ],
                "Aurora Kubernetes runtime boundary",
                "Multiple simulated weak controls could allow a vulnerable container to become a Kubernetes platform incident.",
                "Secrets in images, root runtime, weak securityContext, broad RBAC, missing NetworkPolicies, and missing verification can combine into platform-wide risk.",
                "Escalate to Risk Operations, create audit evidence, prepare review case, and harden Dockerfile, image, runtime, RBAC, NetworkPolicies, and verification controls.",
                "AUD-INFRA-K8S-HARDENING-FAILURE",
                "CORR-INFRA-K8S-HARDENING-FAILURE",
                "2026-06-16T09:56:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-001",
                "Public storage exposure detected",
                "secrets",
                "initial_access",
                "Exposed cloud storage",
                "critical",
                "harden_required",
                "under_review",
                ["Azure private storage control", "Storage-to-identity chain containment"],
                "aurora-internal-reports-container",
                "A simulated storage container exposes internal financial platform assets.",
                "Exposed storage could reveal certificates, metadata, reports, or credentials.",
                "Disable anonymous access, classify files, move credentials to secure secret storage, and review storage access logs.",
                "AUD-INFRA-AZURE-STORAGE-001",
                "CORR-INFRA-AZURE-STORAGE-001",
                "2026-06-15T10:00:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-002",
                "Certificate exposed through storage artifact",
                "secrets",
                "secret_exposure",
                "Certificate exposure",
                "critical",
                "harden_required",
                "under_review",
                ["Certificate protection control", "Key Vault access monitoring control"],
                "service-principal-certificate-demo",
                "A simulated certificate artifact is exposed outside secure secret management.",
                "A leaked certificate can become a leaked cloud identity.",
                "Revoke and rotate certificate, move credential to Key Vault, and review app registration credential activity.",
                "AUD-INFRA-AZURE-CERTIFICATE",
                "CORR-INFRA-AZURE-CERTIFICATE",
                "2026-06-15T10:08:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-003",
                "Overprivileged service principal",
                "cloud_iam",
                "cloud_role_misuse",
                "Service principal excessive permissions",
                "critical",
                "harden_required",
                "under_review",
                ["Service principal least privilege control", "Azure identity monitoring control"],
                "aurora-deployment-sp",
                "A simulated service principal has broad permissions beyond its workload purpose.",
                "A compromised credential could access unrelated financial resources.",
                "Reduce role scope, assign ownership, monitor sign-ins, and review role assignments.",
                "AUD-INFRA-AZURE-SP-SCOPE",
                "CORR-INFRA-AZURE-SP-SCOPE",
                "2026-06-15T10:16:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-004",
                "Deployment credential risk",
                "cloud_iam",
                "privilege_expansion",
                "Deployment access exposure",
                "high",
                "review_required",
                "under_review",
                ["Deployment access control", "Azure identity monitoring control"],
                "app-service-deployment-profile",
                "A simulated deployment credential remains enabled without clear operational need.",
                "Deployment access can modify runtime behavior and influence sensitive workflows.",
                "Disable unused basic deployment credentials, use secure CI/CD identity, require approvals, and monitor deployment changes.",
                "AUD-INFRA-AZURE-DEPLOYMENT",
                "CORR-INFRA-AZURE-DEPLOYMENT",
                "2026-06-15T10:24:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-005",
                "Managed identity has excessive resource scope",
                "cloud_iam",
                "lateral_movement",
                "Managed identity excessive permissions",
                "critical",
                "harden_required",
                "under_review",
                ["Managed identity scope control", "Azure identity monitoring control"],
                "aurora-managed-identity",
                "A simulated managed identity can access resources outside its business purpose.",
                "A compromised workload could use the managed identity to reach unrelated systems.",
                "Scope permissions to specific resources, separate identities per workload, and monitor token/resource usage.",
                "AUD-INFRA-AZURE-MANAGED-IDENTITY",
                "CORR-INFRA-AZURE-MANAGED-IDENTITY",
                "2026-06-15T10:32:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-006",
                "Application identity has password reset capability",
                "cloud_iam",
                "privilege_expansion",
                "Privileged identity administration",
                "critical",
                "escalate",
                "escalated",
                ["Password reset privilege control", "Azure identity monitoring control"],
                "aurora-automation-identity",
                "A simulated application identity has sensitive password reset privileges.",
                "Application identity compromise could become identity administration compromise.",
                "Remove standing password reset privilege, require PIM/MFA/approval for privileged actions, and monitor identity administration events.",
                "AUD-INFRA-AZURE-PASSWORD-RESET",
                "CORR-INFRA-AZURE-PASSWORD-RESET",
                "2026-06-15T10:40:00+03:00",
            ),
            self._event(
                "INFRASEC-AZURE-2026-007",
                "Azure storage-to-identity chain reaction risk",
                "risk_operations",
                "evidence_required",
                "Storage-to-identity compromise chain",
                "critical",
                "escalate",
                "escalated",
                [
                    "Azure private storage control",
                    "Certificate protection control",
                    "Service principal least privilege control",
                    "Deployment access control",
                    "Managed identity scope control",
                    "Password reset privilege control",
                    "Azure identity monitoring control",
                    "Key Vault access monitoring control",
                    "Storage-to-identity chain containment",
                ],
                "Aurora Azure identity security boundary",
                "Multiple simulated weak controls could allow exposed storage to become cloud identity compromise.",
                "Public storage could expose credentials, enable service principal misuse, affect deployment access, misuse managed identities, and reach identity administration privileges.",
                "Escalate to Risk Operations, create audit evidence, prepare review case, and harden storage, certificates, service principals, deployment controls, managed identities, and monitoring.",
                "AUD-INFRA-AZURE-STORAGE-IDENTITY",
                "CORR-INFRA-AZURE-STORAGE-IDENTITY",
                "2026-06-15T10:48:00+03:00",
            ),
        ]

    def list_layers(self) -> list[InfrastructureSecurityLayer]:
        return [
            self._layer(
                "layer-application",
                "Application Security",
                "application",
                "restricted",
                "Object access and template rendering are controlled at the backend boundary.",
                ["Object-level authorization guard", "Safe template execution control"],
                ["object access denials", "template source selection"],
            ),
            self._layer(
                "layer-kubernetes",
                "Kubernetes Runtime Security",
                "kubernetes",
                "review_required",
                "Workload identity, RBAC, namespace access, runtime restrictions, and secret reads require least privilege review.",
                [
                    "Kubernetes least privilege RBAC",
                    "Namespace isolation control",
                    "Service account secret restriction",
                    "Dockerfile hardening control",
                    "Non-root container runtime control",
                    "Immutable image reference control",
                    "Kubernetes securityContext control",
                    "ServiceAccount token control",
                    "Kubernetes RBAC least privilege control",
                    "NetworkPolicy isolation control",
                    "Resource limit enforcement control",
                ],
                [
                    "service account permissions",
                    "namespace access attempts",
                    "securityContext gaps",
                    "network policy coverage",
                    "resource limit coverage",
                ],
            ),
            self._layer(
                "layer-cloud-iam",
                "Cloud IAM Security",
                "cloud_iam",
                "restricted",
                "Role trust and permissions are modeled as narrow, workload-bound, and resource-scoped.",
                ["Cloud IAM trust policy restriction", "Cloud IAM permission scope"],
                ["role assumption", "wildcard permission indicators"],
            ),
            self._layer(
                "layer-secrets",
                "Secrets Security",
                "secrets",
                "monitored",
                "Secret access is simulated as centralized, scoped, rotated, redacted from logs, and excluded from image artifacts.",
                ["Secret management control", "Image secret exclusion control"],
                [
                    "secret access attempts",
                    "rotation status",
                    "log redaction checks",
                    "image secret indicators",
                ],
            ),
            self._layer(
                "layer-audit",
                "Audit Evidence",
                "audit",
                "hardened",
                "Cross-layer events use deterministic correlation IDs for later evidence package preparation.",
                [
                    "Cross-layer audit correlation",
                    "Cluster CIS audit control",
                    "DevSecOps hardening verification control",
                ],
                [
                    "audit event creation",
                    "correlation ID propagation",
                    "CIS audit evidence",
                    "hardening verification evidence",
                ],
            ),
            self._layer(
                "layer-risk-operations",
                "Risk Operations",
                "risk_operations",
                "monitored",
                "Cross-layer chain reaction risk is escalated for staff review before sensitive operations continue.",
                ["Chain reaction containment", "Runtime hardening evidence control"],
                [
                    "escalated infrastructure events",
                    "critical chain risk count",
                    "runtime hardening review cases",
                ],
            ),
        ]

    def list_scenarios(self) -> list[InfrastructureSecurityScenario]:
        return [
            self._scenario(
                "object_authorization_to_data_exposure",
                "Object authorization to data exposure",
                "A user-controlled object ID attempts to access a financial object outside the authorized scope.",
                "application",
                ["application", "audit", "risk_operations"],
                ["object_authorization_failed", "sensitive_object_requested"],
                "block",
                ["Object-level authorization guard", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "unsafe_template_to_runtime_exposure",
                "Unsafe template to runtime exposure",
                "User-controlled input attempts to influence server-side template execution.",
                "application",
                ["application", "secrets", "audit"],
                ["unsafe_template_input_detected", "runtime_context_access"],
                "block",
                ["Safe template execution control", "Secret management control"],
            ),
            self._scenario(
                "pod_rbac_secret_read",
                "Pod RBAC secret read",
                "A simulated web workload has service account permissions that could read Kubernetes secrets.",
                "kubernetes",
                ["kubernetes", "secrets", "risk_operations"],
                ["service_account_can_read_secrets", "pod_privileged"],
                "harden_required",
                ["Kubernetes least privilege RBAC", "Service account secret restriction"],
            ),
            self._scenario(
                "weak_irsa_trust_policy",
                "Weak workload identity trust policy",
                "A cloud role trust policy is not bound narrowly enough to the expected namespace and service account.",
                "cloud_iam",
                ["kubernetes", "cloud_iam", "audit"],
                ["weak_trust_policy", "unexpected_workload_identity"],
                "harden_required",
                ["Cloud IAM trust policy restriction", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "wildcard_iam_permission",
                "Wildcard IAM permission",
                "A simulated cloud IAM policy allows wildcard-like actions or resources for a financial data workload.",
                "cloud_iam",
                ["cloud_iam", "audit", "risk_operations"],
                ["cloud_iam_wildcard_permissions", "sensitive_resource_scope"],
                "harden_required",
                ["Cloud IAM permission scope", "Chain reaction containment"],
            ),
            self._scenario(
                "plaintext_secret_exposure",
                "Plaintext secret exposure",
                "A simulated runtime configuration exposes a token-like value that should be managed centrally.",
                "secrets",
                ["secrets", "audit", "risk_operations"],
                ["secret_exposure_detected", "runtime_configuration"],
                "harden_required",
                ["Secret management control", "Cross-layer audit correlation"],
            ),
            self._scenario(
                "app_to_cloud_chain_reaction",
                "Application-to-cloud chain reaction",
                "Multiple weak controls could allow an application issue to move through Kubernetes, IAM, secrets, and data access.",
                "application",
                [
                    "application",
                    "kubernetes",
                    "cloud_iam",
                    "secrets",
                    "audit",
                    "risk_operations",
                ],
                [
                    "object_authorization_failed",
                    "unsafe_template_input_detected",
                    "service_account_can_read_secrets",
                    "cloud_iam_wildcard_permissions",
                    "weak_trust_policy",
                    "secret_exposure_detected",
                ],
                "escalate",
                [
                    "Object-level authorization guard",
                    "Kubernetes least privilege RBAC",
                    "Cloud IAM permission scope",
                    "Secret management control",
                    "Chain reaction containment",
                ],
            ),
            self._scenario(
                "azure_storage_to_identity_chain_reaction",
                "Azure storage-to-identity chain reaction",
                "Models how exposed storage, leaked certificates, overprivileged service principals, weak deployment controls, excessive managed identities, and password reset privileges can combine into cloud identity risk.",
                "secrets",
                [
                    "public_storage_exposure",
                    "certificate_exposure",
                    "service_principal_misuse",
                    "deployment_access_abuse",
                    "managed_identity_lateral_movement",
                    "password_reset_privilege",
                    "weak_monitoring",
                    "audit_evidence_required",
                    "risk_operations_escalation",
                ],
                [
                    "storage_public_access_detected",
                    "certificate_exposure_detected",
                    "service_principal_overprivileged",
                    "deployment_credentials_enabled",
                    "managed_identity_excessive_scope",
                    "password_reset_privilege_detected",
                    "identity_monitoring_gap",
                ],
                "escalate",
                [
                    "Azure private storage control",
                    "Certificate protection control",
                    "Service principal least privilege control",
                    "Deployment access control",
                    "Managed identity scope control",
                    "Password reset privilege control",
                    "Azure identity monitoring control",
                    "Key Vault access monitoring control",
                    "Storage-to-identity chain containment",
                ],
            ),
            self._scenario(
                "container_kubernetes_hardening_failure",
                "Container and Kubernetes hardening failure",
                "Models how an insecure Dockerfile and weak Kubernetes deployment can allow one compromised service to become a platform-wide incident.",
                "kubernetes",
                [
                    "dockerfile_secret_exposure",
                    "root_container_runtime",
                    "weak_kubernetes_security_context",
                    "service_account_token_mounted",
                    "broad_rbac_permissions",
                    "missing_network_policy",
                    "missing_resource_limits",
                    "missing_cis_audit",
                    "missing_devsecops_verification",
                    "audit_evidence_required",
                    "risk_operations_escalation",
                ],
                [
                    "dockerfile_secrets_detected",
                    "image_uses_latest_tag",
                    "container_runs_as_root",
                    "plaintext_secrets_in_manifest",
                    "missing_security_context",
                    "service_account_token_mounted",
                    "rbac_wildcard_permissions",
                    "can_read_kubernetes_secrets",
                    "network_policy_missing",
                    "resource_limits_missing",
                    "cis_audit_missing",
                    "hardening_verification_missing",
                ],
                "escalate",
                [
                    "Dockerfile hardening control",
                    "Image secret exclusion control",
                    "Non-root container runtime control",
                    "Immutable image reference control",
                    "Kubernetes securityContext control",
                    "ServiceAccount token control",
                    "Kubernetes RBAC least privilege control",
                    "NetworkPolicy isolation control",
                    "Resource limit enforcement control",
                    "Cluster CIS audit control",
                    "DevSecOps hardening verification control",
                ],
            ),
        ]

    def evaluate_scenario(
        self,
        *,
        scenario_id: str,
        object_authorization_failed: bool,
        unsafe_template_input_detected: bool,
        pod_privileged: bool,
        service_account_can_read_secrets: bool,
        cloud_iam_wildcard_permissions: bool,
        weak_trust_policy: bool,
        secret_exposure_detected: bool,
        storage_public_access_detected: bool = False,
        certificate_exposure_detected: bool = False,
        service_principal_overprivileged: bool = False,
        deployment_credentials_enabled: bool = False,
        managed_identity_excessive_scope: bool = False,
        password_reset_privilege_detected: bool = False,
        identity_monitoring_gap: bool = False,
        dockerfile_secrets_detected: bool = False,
        image_uses_latest_tag: bool = False,
        container_runs_as_root: bool = False,
        plaintext_secrets_in_manifest: bool = False,
        missing_security_context: bool = False,
        service_account_token_mounted: bool = False,
        rbac_wildcard_permissions: bool = False,
        can_read_kubernetes_secrets: bool = False,
        network_policy_missing: bool = False,
        resource_limits_missing: bool = False,
        cis_audit_missing: bool = False,
        hardening_verification_missing: bool = False,
    ) -> EvaluateInfrastructureSecurityScenarioResponse:
        if scenario_id == "azure_storage_to_identity_chain_reaction":
            return self._evaluate_azure_storage_identity_scenario(
                storage_public_access_detected=storage_public_access_detected,
                certificate_exposure_detected=certificate_exposure_detected,
                service_principal_overprivileged=service_principal_overprivileged,
                deployment_credentials_enabled=deployment_credentials_enabled,
                managed_identity_excessive_scope=managed_identity_excessive_scope,
                password_reset_privilege_detected=password_reset_privilege_detected,
                identity_monitoring_gap=identity_monitoring_gap,
            )
        if scenario_id == "container_kubernetes_hardening_failure":
            return self._evaluate_container_kubernetes_hardening_scenario(
                dockerfile_secrets_detected=dockerfile_secrets_detected,
                image_uses_latest_tag=image_uses_latest_tag,
                container_runs_as_root=container_runs_as_root,
                plaintext_secrets_in_manifest=plaintext_secrets_in_manifest,
                missing_security_context=missing_security_context,
                service_account_token_mounted=service_account_token_mounted,
                rbac_wildcard_permissions=rbac_wildcard_permissions,
                can_read_kubernetes_secrets=can_read_kubernetes_secrets,
                network_policy_missing=network_policy_missing,
                resource_limits_missing=resource_limits_missing,
                cis_audit_missing=cis_audit_missing,
                hardening_verification_missing=hardening_verification_missing,
            )

        score = 10
        affected_layers = set[str]()
        triggered_controls = set[str]()
        risk_reasons: list[str] = []

        checks = [
            (
                object_authorization_failed,
                35,
                ["application", "audit", "risk_operations"],
                [
                    "Object-level authorization guard",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "object authorization failed",
            ),
            (
                unsafe_template_input_detected,
                25,
                ["application", "secrets", "audit"],
                [
                    "Safe template execution control",
                    "Secret management control",
                    "Cross-layer audit correlation",
                ],
                "unsafe template input detected",
            ),
            (
                pod_privileged,
                25,
                ["kubernetes", "risk_operations"],
                [
                    "Kubernetes least privilege RBAC",
                    "Namespace isolation control",
                    "Chain reaction containment",
                ],
                "privileged pod configuration",
            ),
            (
                service_account_can_read_secrets,
                35,
                ["kubernetes", "secrets", "risk_operations"],
                [
                    "Kubernetes least privilege RBAC",
                    "Service account secret restriction",
                    "Secret management control",
                    "Chain reaction containment",
                ],
                "service account can read secrets",
            ),
            (
                cloud_iam_wildcard_permissions,
                35,
                ["cloud_iam", "audit", "risk_operations"],
                [
                    "Cloud IAM permission scope",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "wildcard IAM permissions",
            ),
            (
                weak_trust_policy,
                30,
                ["kubernetes", "cloud_iam", "audit"],
                [
                    "Cloud IAM trust policy restriction",
                    "Cross-layer audit correlation",
                ],
                "weak cloud IAM trust policy",
            ),
            (
                secret_exposure_detected,
                30,
                ["secrets", "audit", "risk_operations"],
                [
                    "Secret management control",
                    "Cross-layer audit correlation",
                    "Chain reaction containment",
                ],
                "secret exposure detected",
            ),
        ]

        for enabled, points, layers, controls, reason in checks:
            if enabled:
                score += points
                affected_layers.update(layers)
                triggered_controls.update(controls)
                risk_reasons.append(reason)

        true_flags = len(risk_reasons)
        if true_flags >= 4:
            score += 15
        elif true_flags >= 2:
            score += 8

        if not affected_layers:
            affected_layers.add("application")
            triggered_controls.add("Cross-layer audit correlation")
            risk_reasons.append("no high-risk infrastructure indicator selected")

        risk_score = min(score, 100)
        severity = self._severity_for_score(risk_score)
        decision = self._decision_for_score(risk_score)
        audit_event_id = AUDIT_IDS_BY_SCENARIO.get(
            scenario_id,
            f"AUD-INFRA-{scenario_id.upper().replace('-', '_')}",
        )
        correlation_id = CORRELATION_IDS_BY_SCENARIO.get(
            scenario_id,
            f"CORR-INFRA-{scenario_id.upper().replace('-', '_')}",
        )
        evidence_package_ready = severity in {"high", "critical"}
        chain_reaction_risk = self._chain_reaction_risk(true_flags)
        recommended_action = self._recommended_action(decision)
        explanation = (
            "Deterministic prototype evaluation based on "
            f"{', '.join(risk_reasons)}. Evidence can be prepared later from "
            f"audit event {audit_event_id}."
        )

        audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="infrastructure-security-engine",
            actor_type="service",
            source_module="infrastructure_security",
            action="evaluate_scenario",
            object_type="infrastructure_security_scenario",
            object_id=scenario_id,
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=explanation,
            correlation_id=correlation_id,
            metadata={
                "prototype": True,
                "affected_layers": sorted(affected_layers),
                "chain_reaction_risk": chain_reaction_risk,
                "evidence_package_ready": evidence_package_ready,
            },
        )

        return EvaluateInfrastructureSecurityScenarioResponse(
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            affected_layers=sorted(affected_layers),
            chain_reaction_risk=chain_reaction_risk,
            triggered_controls=sorted(triggered_controls),
            audit_event_created=True,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=evidence_package_ready,
            recommended_action=recommended_action,
            explanation=explanation,
        )

    def _evaluate_azure_storage_identity_scenario(
        self,
        *,
        storage_public_access_detected: bool,
        certificate_exposure_detected: bool,
        service_principal_overprivileged: bool,
        deployment_credentials_enabled: bool,
        managed_identity_excessive_scope: bool,
        password_reset_privilege_detected: bool,
        identity_monitoring_gap: bool,
    ) -> EvaluateInfrastructureSecurityScenarioResponse:
        score = 10
        affected_layers = set[str]()
        triggered_controls = set[str]()
        risk_reasons: list[str] = []
        checks = [
            (
                storage_public_access_detected,
                35,
                ["secrets", "audit", "risk_operations"],
                ["Azure private storage control", "Storage-to-identity chain containment"],
                "public storage exposure detected",
            ),
            (
                certificate_exposure_detected,
                35,
                ["secrets", "cloud_iam", "audit"],
                ["Certificate protection control", "Key Vault access monitoring control"],
                "certificate exposure detected",
            ),
            (
                service_principal_overprivileged,
                35,
                ["cloud_iam", "audit", "risk_operations"],
                ["Service principal least privilege control", "Azure identity monitoring control"],
                "service principal overprivileged",
            ),
            (
                deployment_credentials_enabled,
                25,
                ["cloud_iam", "audit"],
                ["Deployment access control", "Azure identity monitoring control"],
                "deployment credentials enabled",
            ),
            (
                managed_identity_excessive_scope,
                35,
                ["cloud_iam", "audit", "risk_operations"],
                ["Managed identity scope control", "Azure identity monitoring control"],
                "managed identity excessive scope",
            ),
            (
                password_reset_privilege_detected,
                35,
                ["cloud_iam", "audit", "risk_operations"],
                ["Password reset privilege control", "Azure identity monitoring control"],
                "password reset privilege detected",
            ),
            (
                identity_monitoring_gap,
                25,
                ["audit", "risk_operations"],
                ["Azure identity monitoring control", "Storage-to-identity chain containment"],
                "identity monitoring gap",
            ),
        ]
        for enabled, points, layers, controls, reason in checks:
            if enabled:
                score += points
                affected_layers.update(layers)
                triggered_controls.update(controls)
                risk_reasons.append(reason)

        true_flags = len(risk_reasons)
        if true_flags >= 5:
            score += 20
        elif true_flags >= 3:
            score += 12
        elif true_flags >= 2:
            score += 6

        if not affected_layers:
            affected_layers.add("cloud_iam")
            triggered_controls.add("Azure identity monitoring control")
            risk_reasons.append("no Azure identity chain indicator selected")

        risk_score = min(score, 100)
        if risk_score >= 85:
            severity = "critical"
            decision = "escalate"
        elif risk_score >= 70:
            severity = "critical"
            decision = "harden_required"
        elif risk_score >= 50:
            severity = "high"
            decision = "review_required"
        else:
            severity = "medium"
            decision = "review_required"

        audit_event_id = "AUD-INFRA-AZURE-STORAGE-IDENTITY"
        correlation_id = "CORR-INFRA-AZURE-STORAGE-IDENTITY"
        chain_reaction_risk = (
            "Critical Azure storage-to-identity chain reaction path involving "
            "exposed storage, certificate exposure, service principal permissions, "
            "deployment access, managed identity scope, password reset privilege, "
            "and monitoring gaps."
        )
        recommended_action = (
            "Escalate to Risk Operations, preserve audit evidence, and harden "
            "storage access, certificate handling, service principal scope, "
            "deployment controls, managed identity permissions, privileged "
            "identity roles, and monitoring."
        )
        explanation = (
            "Deterministic prototype evaluation. No real Azure environment, "
            "storage account, identity, certificate, or secret was accessed."
        )
        audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="infrastructure-security-engine",
            actor_type="service",
            source_module="infrastructure_security",
            action="evaluate_scenario",
            object_type="infrastructure_security_scenario",
            object_id="azure_storage_to_identity_chain_reaction",
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=explanation,
            correlation_id=correlation_id,
            metadata={
                "prototype": True,
                "affected_layers": sorted(affected_layers),
                "chain_reaction_risk": chain_reaction_risk,
                "evidence_package_ready": True,
                "risk_reasons": risk_reasons,
            },
        )
        return EvaluateInfrastructureSecurityScenarioResponse(
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            affected_layers=sorted(affected_layers),
            chain_reaction_risk=chain_reaction_risk,
            triggered_controls=sorted(triggered_controls),
            audit_event_created=True,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=True,
            recommended_action=recommended_action,
            explanation=explanation,
        )

    def _evaluate_container_kubernetes_hardening_scenario(
        self,
        *,
        dockerfile_secrets_detected: bool,
        image_uses_latest_tag: bool,
        container_runs_as_root: bool,
        plaintext_secrets_in_manifest: bool,
        missing_security_context: bool,
        service_account_token_mounted: bool,
        rbac_wildcard_permissions: bool,
        can_read_kubernetes_secrets: bool,
        network_policy_missing: bool,
        resource_limits_missing: bool,
        cis_audit_missing: bool,
        hardening_verification_missing: bool,
    ) -> EvaluateInfrastructureSecurityScenarioResponse:
        score = 10
        affected_layers = set[str]()
        triggered_controls = set[str]()
        risk_reasons: list[str] = []
        checks = [
            (
                dockerfile_secrets_detected,
                35,
                ["secrets", "kubernetes", "audit"],
                ["Dockerfile hardening control", "Image secret exclusion control"],
                "dockerfile secrets detected",
            ),
            (
                image_uses_latest_tag,
                20,
                ["kubernetes", "audit"],
                ["Immutable image reference control", "DevSecOps hardening verification control"],
                "image uses latest tag",
            ),
            (
                container_runs_as_root,
                30,
                ["kubernetes", "risk_operations"],
                ["Non-root container runtime control", "Kubernetes securityContext control"],
                "container runs as root",
            ),
            (
                plaintext_secrets_in_manifest,
                35,
                ["secrets", "kubernetes", "audit"],
                ["Image secret exclusion control", "Secret management control"],
                "plaintext secrets in manifest",
            ),
            (
                missing_security_context,
                35,
                ["kubernetes", "risk_operations"],
                ["Kubernetes securityContext control", "Runtime hardening evidence control"],
                "missing Kubernetes securityContext",
            ),
            (
                service_account_token_mounted,
                30,
                ["kubernetes", "risk_operations"],
                ["ServiceAccount token control", "Kubernetes RBAC least privilege control"],
                "service account token mounted",
            ),
            (
                rbac_wildcard_permissions,
                35,
                ["kubernetes", "secrets", "risk_operations"],
                ["Kubernetes RBAC least privilege control", "ServiceAccount token control"],
                "RBAC wildcard permissions",
            ),
            (
                can_read_kubernetes_secrets,
                35,
                ["kubernetes", "secrets", "risk_operations"],
                ["Kubernetes RBAC least privilege control", "Image secret exclusion control"],
                "can read Kubernetes secrets",
            ),
            (
                network_policy_missing,
                30,
                ["kubernetes", "risk_operations"],
                ["NetworkPolicy isolation control", "Chain reaction containment"],
                "network policy missing",
            ),
            (
                resource_limits_missing,
                20,
                ["kubernetes", "risk_operations"],
                ["Resource limit enforcement control", "Runtime hardening evidence control"],
                "resource limits missing",
            ),
            (
                cis_audit_missing,
                30,
                ["kubernetes", "audit", "risk_operations"],
                ["Cluster CIS audit control", "Runtime hardening evidence control"],
                "CIS audit missing",
            ),
            (
                hardening_verification_missing,
                30,
                ["audit", "risk_operations"],
                ["DevSecOps hardening verification control", "Runtime hardening evidence control"],
                "hardening verification missing",
            ),
        ]

        for enabled, points, layers, controls, reason in checks:
            if enabled:
                score += points
                affected_layers.update(layers)
                triggered_controls.update(controls)
                risk_reasons.append(reason)

        true_flags = len(risk_reasons)
        if true_flags >= 8:
            score += 25
        elif true_flags >= 5:
            score += 18
        elif true_flags >= 3:
            score += 10
        elif true_flags >= 2:
            score += 5

        if not affected_layers:
            affected_layers.add("kubernetes")
            triggered_controls.add("DevSecOps hardening verification control")
            risk_reasons.append("no container or Kubernetes hardening indicator selected")

        risk_score = min(score, 100)
        if risk_score >= 85:
            severity = "critical"
            decision = "escalate"
        elif risk_score >= 70:
            severity = "critical"
            decision = "harden_required"
        elif risk_score >= 50:
            severity = "high"
            decision = "review_required"
        else:
            severity = "medium"
            decision = "review_required"

        audit_event_id = "AUD-INFRA-K8S-HARDENING-FAILURE"
        correlation_id = "CORR-INFRA-K8S-HARDENING-FAILURE"
        chain_reaction_risk = (
            "Critical container-to-Kubernetes hardening failure path involving "
            "secrets in images, root runtime, weak securityContext, service "
            "account token exposure, broad RBAC, missing NetworkPolicies, "
            "missing resource limits, missing CIS audit, and missing DevSecOps "
            "verification."
        )
        recommended_action = (
            "Escalate to Risk Operations, preserve audit evidence, and harden "
            "Dockerfile, image secrets, non-root runtime, Kubernetes "
            "securityContext, ServiceAccount token settings, RBAC, "
            "NetworkPolicies, resource limits, CIS audit, and DevSecOps "
            "verification."
        )
        explanation = (
            "Deterministic prototype evaluation. No real Docker image, "
            "Kubernetes cluster, scanner, kube-bench run, or secret was accessed."
        )
        audit_service.create_audit_event_from_sensitive_action(
            event_id=audit_event_id,
            actor_id="infrastructure-security-engine",
            actor_type="service",
            source_module="infrastructure_security",
            action="evaluate_scenario",
            object_type="infrastructure_security_scenario",
            object_id="container_kubernetes_hardening_failure",
            decision=decision,
            severity=severity,
            risk_score=risk_score,
            summary=explanation,
            correlation_id=correlation_id,
            metadata={
                "prototype": True,
                "affected_layers": sorted(affected_layers),
                "chain_reaction_risk": chain_reaction_risk,
                "evidence_package_ready": True,
                "risk_reasons": risk_reasons,
                "triggered_controls": sorted(triggered_controls),
            },
        )
        return EvaluateInfrastructureSecurityScenarioResponse(
            risk_score=risk_score,
            severity=severity,
            decision=decision,
            affected_layers=sorted(affected_layers),
            chain_reaction_risk=chain_reaction_risk,
            triggered_controls=sorted(triggered_controls),
            audit_event_created=True,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=True,
            recommended_action=recommended_action,
            explanation=explanation,
        )

    def _control(
        self,
        control_id: str,
        title: str,
        layer: str,
        category: str,
        description: str,
        protected_assets: list[str],
        decision_model: str,
        evidence_outputs: list[str],
    ) -> InfrastructureSecurityControl:
        return InfrastructureSecurityControl(
            control_id=control_id,
            title=title,
            layer=layer,
            category=category,
            description=description,
            protected_assets=protected_assets,
            decision_model=decision_model,
            evidence_outputs=evidence_outputs,
            enabled=True,
        )

    def _event(
        self,
        event_id: str,
        title: str,
        affected_layer: str,
        chain_stage: str,
        risk_type: str,
        severity: str,
        decision: str,
        status: str,
        triggered_controls: list[str],
        affected_asset: str,
        summary: str,
        chain_reaction_risk: str,
        recommended_action: str,
        audit_event_id: str,
        correlation_id: str,
        created_at: str,
    ) -> InfrastructureSecurityEvent:
        return InfrastructureSecurityEvent(
            event_id=event_id,
            title=title,
            affected_layer=affected_layer,
            chain_stage=chain_stage,
            risk_type=risk_type,
            severity=severity,
            decision=decision,
            status=status,
            triggered_controls=triggered_controls,
            affected_asset=affected_asset,
            summary=summary,
            chain_reaction_risk=chain_reaction_risk,
            recommended_action=recommended_action,
            audit_event_id=audit_event_id,
            correlation_id=correlation_id,
            evidence_package_ready=severity in {"high", "critical"},
            created_at=created_at,
        )

    def _layer(
        self,
        layer_id: str,
        name: str,
        layer_type: str,
        posture: str,
        risk_summary: str,
        controls_applied: list[str],
        monitored_signals: list[str],
    ) -> InfrastructureSecurityLayer:
        return InfrastructureSecurityLayer(
            layer_id=layer_id,
            name=name,
            layer_type=layer_type,
            posture=posture,
            risk_summary=risk_summary,
            controls_applied=controls_applied,
            monitored_signals=monitored_signals,
        )

    def _scenario(
        self,
        scenario_id: str,
        title: str,
        description: str,
        starting_layer: str,
        possible_chain: list[str],
        risk_indicators: list[str],
        expected_decision: str,
        recommended_controls: list[str],
    ) -> InfrastructureSecurityScenario:
        return InfrastructureSecurityScenario(
            scenario_id=scenario_id,
            title=title,
            description=description,
            starting_layer=starting_layer,
            possible_chain=possible_chain,
            risk_indicators=risk_indicators,
            expected_decision=expected_decision,
            recommended_controls=recommended_controls,
        )

    def _severity_for_score(self, risk_score: int) -> str:
        if risk_score >= 70:
            return "critical"
        if risk_score >= 50:
            return "high"
        if risk_score >= 30:
            return "medium"
        return "low"

    def _decision_for_score(self, risk_score: int) -> str:
        if risk_score >= 85:
            return "escalate"
        if risk_score >= 70:
            return "harden_required"
        if risk_score >= 50:
            return "review_required"
        return "allow"

    def _chain_reaction_risk(self, true_flags: int) -> str:
        if true_flags >= 4:
            return (
                "Critical chain reaction path across application, Kubernetes, "
                "cloud IAM, secrets, audit evidence, and risk operations."
            )
        if true_flags >= 2:
            return (
                "Elevated chain reaction risk because multiple control layers "
                "require review before sensitive operations continue."
            )
        if true_flags == 1:
            return "Single-layer issue detected and contained with audit evidence."
        return "No chain reaction path selected in this deterministic scenario."

    def _recommended_action(self, decision: str) -> str:
        if decision == "escalate":
            return (
                "Escalate to Risk Operations, preserve cross-layer audit evidence, "
                "and harden application, Kubernetes, IAM, and secrets controls."
            )
        if decision == "harden_required":
            return (
                "Harden the affected control layer, preserve audit evidence, and "
                "prepare an evidence package if review is required."
            )
        if decision == "review_required":
            return "Open a staff review, validate control scope, and keep the audit correlation record."
        return "Allow the scenario to continue with standard monitoring."


infrastructure_security_service = InfrastructureSecurityService()
