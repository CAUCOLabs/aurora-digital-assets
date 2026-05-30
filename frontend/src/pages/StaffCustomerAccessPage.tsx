import { useState } from 'react'
import { Panel } from '../components/Panel'
import { TopBar } from '../components/TopBar'
import {
  approveStaffCustomerAuthorization,
  lookupStaffCustomer,
  requestStaffCustomerAuthorization,
  type AuthorizationMethod,
  type LookupType,
  type StaffCustomerAccessApprovalResponse,
  type StaffCustomerAuthorizationResponse,
  type StaffCustomerLookupResponse,
} from '../services/staffCustomerAccessApi'

const accessControls = [
  'Customer lookup required',
  'Sensitive details locked by default',
  'Customer authorization required',
  'Temporary access only',
  'Audit event concept',
]

const authorizationMethods = [
  'Mobile banking approval',
  'Private branch credential entry',
]

const prototypeLimitations = [
  'No real staff identity',
  'No real mobile app integration',
  'No real credential capture',
  'No production access control',
]

const lookupTypeLabels: Record<LookupType, string> = {
  customer_id: 'Customer ID',
  bank_user_id: 'Bank user ID',
  passport_or_id: 'Passport / ID',
}

const methodLabels: Record<AuthorizationMethod, string> = {
  mobile_approval: 'Mobile approval request',
  private_branch_entry: 'Private branch credential entry',
}

function formatBoolean(value: boolean) {
  return value ? 'Enabled' : 'Not enabled'
}

export function StaffCustomerAccessPage() {
  const [lookupType, setLookupType] = useState<LookupType>('customer_id')
  const [lookupValue, setLookupValue] = useState('CUST-DA-2026-001')
  const [lookupResult, setLookupResult] =
    useState<StaffCustomerLookupResponse | null>(null)
  const [authorizationRequest, setAuthorizationRequest] =
    useState<StaffCustomerAuthorizationResponse | null>(null)
  const [approvalResult, setApprovalResult] =
    useState<StaffCustomerAccessApprovalResponse | null>(null)
  const [isWorking, setIsWorking] = useState(false)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const customerId = lookupResult?.customer_id
  const hasLockedRecord =
    lookupResult?.status === 'found' && lookupResult.access_state === 'locked'
  const hasPendingAuthorization =
    authorizationRequest?.status === 'pending_customer_authorization'
  const unlockedRecord =
    approvalResult?.status === 'authorized'
      ? approvalResult.customer_record
      : null

  async function handleLookup() {
    setIsWorking(true)
    setErrorMessage(null)
    setAuthorizationRequest(null)
    setApprovalResult(null)

    try {
      const response = await lookupStaffCustomer({
        lookup_type: lookupType,
        lookup_value: lookupValue,
      })
      setLookupResult(response)
    } catch {
      setErrorMessage('Customer lookup is unavailable in the local prototype.')
    } finally {
      setIsWorking(false)
    }
  }

  async function handleRequestAuthorization(method: AuthorizationMethod) {
    if (!customerId) {
      return
    }

    setIsWorking(true)
    setErrorMessage(null)
    setApprovalResult(null)

    try {
      const response = await requestStaffCustomerAuthorization({
        customer_id: customerId,
        method,
      })
      setAuthorizationRequest(response)
    } catch {
      setErrorMessage(
        'Authorization request is unavailable in the local prototype.',
      )
    } finally {
      setIsWorking(false)
    }
  }

  async function handleApproval(approved: boolean) {
    if (!authorizationRequest?.request_id) {
      return
    }

    setIsWorking(true)
    setErrorMessage(null)

    try {
      const response = await approveStaffCustomerAuthorization({
        request_id: authorizationRequest.request_id,
        approved,
      })
      setApprovalResult(response)
    } catch {
      setErrorMessage(
        'Customer authorization decision is unavailable in the local prototype.',
      )
    } finally {
      setIsWorking(false)
    }
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Staff access model</p>
            <h1>Staff Customer Access Authorization</h1>
            <p>
              Sensitive customer data stays locked until the identified customer
              authorizes temporary staff access through a simulated bank channel.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Customer-authorized access
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Customer lookup</p>
                  <h2>Find demo customer</h2>
                </div>
                <span className="module-tag">Locked by default</span>
              </div>

              <div className="form-grid">
                <label>
                  <span>Lookup type</span>
                  <select
                    value={lookupType}
                    onChange={(event) =>
                      setLookupType(event.target.value as LookupType)
                    }
                  >
                    {Object.entries(lookupTypeLabels).map(([value, label]) => (
                      <option key={value} value={value}>
                        {label}
                      </option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Lookup value</span>
                  <input
                    value={lookupValue}
                    onChange={(event) => setLookupValue(event.target.value)}
                  />
                </label>
              </div>

              <div className="action-row">
                <button onClick={handleLookup} disabled={isWorking}>
                  Search customer
                </button>
              </div>

              {errorMessage && <p className="panel-note">{errorMessage}</p>}
              {lookupResult && (
                <p className="panel-note">{lookupResult.user_message}</p>
              )}
            </Panel>

            {hasLockedRecord && (
              <Panel className="risk-panel">
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">Locked customer record</p>
                    <h2>{lookupResult.customer_name}</h2>
                  </div>
                  <span className="module-tag">
                    {lookupResult.access_state}
                  </span>
                </div>
                <div className="summary-list">
                  <div>
                    <span>Customer ID</span>
                    <strong>{lookupResult.customer_id}</strong>
                  </div>
                  <div>
                    <span>Relationship status</span>
                    <strong>{lookupResult.relationship_status}</strong>
                  </div>
                </div>
                <p>
                  Sensitive customer details are locked until the customer
                  authorizes staff access.
                </p>
              </Panel>
            )}

            {hasLockedRecord && (
              <Panel>
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">Authorization method</p>
                    <h2>Request customer approval</h2>
                  </div>
                </div>

                <div className="action-row">
                  <button
                    onClick={() =>
                      void handleRequestAuthorization('mobile_approval')
                    }
                    disabled={isWorking}
                  >
                    Send mobile approval request
                  </button>
                  <button
                    className="secondary-button"
                    onClick={() =>
                      void handleRequestAuthorization('private_branch_entry')
                    }
                    disabled={isWorking}
                  >
                    Private branch credential entry
                  </button>
                </div>
              </Panel>
            )}

            {hasPendingAuthorization && (
              <Panel>
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">Pending authorization</p>
                    <h2>Waiting for customer decision</h2>
                  </div>
                  <span className="module-tag">
                    {authorizationRequest.access_state}
                  </span>
                </div>

                <div className="summary-list">
                  <div>
                    <span>Request ID</span>
                    <strong>{authorizationRequest.request_id}</strong>
                  </div>
                  <div>
                    <span>Method</span>
                    <strong>
                      {authorizationRequest.method
                        ? methodLabels[authorizationRequest.method]
                        : 'Unknown'}
                    </strong>
                  </div>
                  <div>
                    <span>Status</span>
                    <strong>{authorizationRequest.status}</strong>
                  </div>
                </div>

                <p>{authorizationRequest.user_message}</p>

                <div className="action-row">
                  <button
                    onClick={() => void handleApproval(true)}
                    disabled={isWorking}
                  >
                    Approve simulated customer authorization
                  </button>
                  <button
                    className="secondary-button"
                    onClick={() => void handleApproval(false)}
                    disabled={isWorking}
                  >
                    Reject simulated customer authorization
                  </button>
                </div>
              </Panel>
            )}

            {approvalResult?.status === 'rejected' && (
              <Panel className="risk-panel">
                <p className="eyebrow">Authorization rejected</p>
                <h2>Record remains locked</h2>
                <p>{approvalResult.user_message}</p>
              </Panel>
            )}

            {unlockedRecord && (
              <Panel>
                <div className="panel-header">
                  <div>
                    <p className="eyebrow">Unlocked customer record</p>
                    <h2>{unlockedRecord.name}</h2>
                  </div>
                  <span className="module-tag">
                    {approvalResult?.access_expires_in_minutes} min access
                  </span>
                </div>

                <p>
                  Temporary staff access granted for this simulated session.
                </p>

                <div className="summary-list">
                  <div>
                    <span>Customer ID</span>
                    <strong>{unlockedRecord.customer_id}</strong>
                  </div>
                  <div>
                    <span>Bank user ID</span>
                    <strong>{unlockedRecord.bank_user_id}</strong>
                  </div>
                  <div>
                    <span>Account ID</span>
                    <strong>{unlockedRecord.account_id}</strong>
                  </div>
                  <div>
                    <span>Relationship status</span>
                    <strong>{unlockedRecord.relationship_status}</strong>
                  </div>
                  <div>
                    <span>Identity verification</span>
                    <strong>
                      {unlockedRecord.identity_verification_status}
                    </strong>
                  </div>
                  <div>
                    <span>Source of funds</span>
                    <strong>{unlockedRecord.source_of_funds_status}</strong>
                  </div>
                  <div>
                    <span>Online banking</span>
                    <strong>
                      {formatBoolean(unlockedRecord.online_banking_enabled)}
                    </strong>
                  </div>
                  <div>
                    <span>Strong authentication</span>
                    <strong>
                      {formatBoolean(
                        unlockedRecord.strong_authentication_enabled,
                      )}
                    </strong>
                  </div>
                  <div>
                    <span>Digital Assets eligible</span>
                    <strong>
                      {unlockedRecord.digital_assets_eligible ? 'Yes' : 'No'}
                    </strong>
                  </div>
                </div>
              </Panel>
            )}

            <Panel className="risk-panel">
              <p className="eyebrow">Boundary note</p>
              <h2>Prototype scope</h2>
              <p>
                This prototype does not implement real staff identity, real
                mobile approval, real credential entry, real document
                verification, or production access control.
              </p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Staff access controls</p>
              <h2>Customer permission first</h2>
              <div className="check-list">
                {accessControls.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Authorization methods</p>
              <h2>Simulated customer approval</h2>
              <div className="check-list">
                {authorizationMethods.map((item) => (
                  <div key={item}>
                    <span className="status-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Prototype limitation</p>
              <h2>No production access control</h2>
              <div className="check-list">
                {prototypeLimitations.map((item) => (
                  <div key={item}>
                    <span className="warning-dot"></span>
                    {item}
                  </div>
                ))}
              </div>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}
