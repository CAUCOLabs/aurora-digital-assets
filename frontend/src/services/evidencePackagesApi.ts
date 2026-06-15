import { getJson, postJson } from './apiClient'

export type EvidenceItemStatus =
  | 'included'
  | 'missing'
  | 'reviewer_required'
  | 'optional'
export type EvidencePackageSeverity = 'low' | 'medium' | 'high' | 'critical'
export type EvidencePackageStatus =
  | 'draft'
  | 'ready'
  | 'incomplete'
  | 'escalated'
export type EvidencePackageSourceType = 'alert' | 'review_case' | 'case' | 'audit_event'
export type EvidencePackageType =
  | 'internal_review'
  | 'audit'
  | 'regulator'
  | 'investigation'

export type EvidenceItem = {
  item_id: string
  title: string
  category: string
  status: EvidenceItemStatus
  description: string
  source_module: string
  required: boolean
}

export type EvidenceTimelineEvent = {
  event_id: string
  timestamp: string
  event_type: string
  title: string
  description: string
  source_module: string
}

export type EvidencePackage = {
  package_id: string
  title: string
  source_alert_id?: string | null
  source_case_id?: string | null
  source_audit_event_id?: string | null
  source_module?: string | null
  backend_decision?: string | null
  correlation_id?: string | null
  traceability_summary?: string | null
  audit_context?: Record<string, unknown> | null
  linked_audit_events: string[]
  risk_type: string
  severity: EvidencePackageSeverity
  status: EvidencePackageStatus
  readiness_score: number
  summary: string
  included_evidence: EvidenceItem[]
  missing_evidence: EvidenceItem[]
  triggered_controls: string[]
  reviewer_notes: string[]
  decision_rationale: string
  timeline: EvidenceTimelineEvent[]
  recommended_next_action: string
  created_at: string
}

export type EvidencePackageTemplate = {
  template_id: string
  title: string
  use_case: string
  description: string
  required_items: string[]
}

export type GenerateEvidencePackageRequest = {
  source_type: EvidencePackageSourceType
  source_id: string
  package_type: EvidencePackageType
  reviewer_id?: string | null
}

export type EvidenceReadinessCheck = {
  ready: boolean
  score: number
  blockers: string[]
  warnings: string[]
  recommended_actions: string[]
}

export type GenerateEvidencePackageResponse = {
  package: EvidencePackage
  readiness_check: EvidenceReadinessCheck
  export_available: boolean
  audit_event_created: boolean
  audit_event_id: string
  correlation_id: string
  source_type: EvidencePackageSourceType
  source_id: string
  source_audit_event_id?: string | null
  traceability_summary?: string | null
  evidence_items: EvidenceItem[]
  linked_audit_events: string[]
  recommended_next_steps: string[]
  user_message: string
}

export function getEvidencePackages(): Promise<EvidencePackage[]> {
  return getJson<EvidencePackage[]>('/evidence-packages')
}

export function getEvidencePackageTemplates(): Promise<EvidencePackageTemplate[]> {
  return getJson<EvidencePackageTemplate[]>('/evidence-packages/templates')
}

export function getEvidencePackage(
  packageId: string,
): Promise<EvidencePackage> {
  return getJson<EvidencePackage>(`/evidence-packages/${packageId}`)
}

export function generateEvidencePackage(
  payload: GenerateEvidencePackageRequest,
): Promise<GenerateEvidencePackageResponse> {
  return postJson<
    GenerateEvidencePackageResponse,
    GenerateEvidencePackageRequest
  >('/evidence-packages/generate', payload)
}

export function generateEvidencePackageFromAuditEvent(
  auditEventId: string,
): Promise<GenerateEvidencePackageResponse> {
  return generateEvidencePackage({
    source_type: 'audit_event',
    source_id: auditEventId,
    package_type: 'internal_review',
    reviewer_id: 'reviewer-demo',
  })
}

export function getEvidencePackageReadiness(
  packageId: string,
): Promise<EvidenceReadinessCheck> {
  return getJson<EvidenceReadinessCheck>(
    `/evidence-packages/${packageId}/readiness`,
  )
}
