import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { PrivacyAmount } from '../components/PrivacyAmount'
import {
  evaluateWithdrawal,
  type RiskDecisionResponse,
} from '../services/withdrawalsApi'

type WithdrawalAsset = 'BTC' | 'ETH' | 'USDC' | 'USDT' | 'EURD'
type WalletType =
  | 'Personal self-custody wallet'
  | 'Hardware wallet'
  | 'External crypto service'
  | 'Exchange deposit address'
type WithdrawalStatus =
  | 'draft'
  | 'pending_review'
  | 'auto_approved'
  | 'auto_rejected'
  | 'blocked'
  | 'escalated'

const assetLabels: Record<WithdrawalAsset, string> = {
  BTC: 'BTC — Bitcoin',
  ETH: 'ETH — Ethereum',
  USDC: 'USDC',
  USDT: 'USDT',
  EURD: 'EUR digital asset concept',
}

const assetBalances: Record<WithdrawalAsset, string> = {
  BTC: '0.012450 BTC',
  ETH: '0.184200 ETH',
  USDC: '129.80 USDC',
  USDT: '129.60 USDT',
  EURD: 'Internal settlement concept',
}

const networkOptions: Record<WithdrawalAsset, string[]> = {
  BTC: ['Bitcoin'],
  ETH: ['Ethereum'],
  USDC: ['Ethereum', 'Polygon'],
  USDT: ['Ethereum', 'Tron'],
  EURD: ['Internal settlement only / External withdrawal unavailable concept'],
}

const initialWithdrawal = {
  asset: 'BTC' as WithdrawalAsset,
  amount: '0.001',
  network: 'Bitcoin',
  destinationAddress: '',
  confirmDestinationAddress: '',
  destinationLabel: 'Personal cold wallet',
  walletType: 'Personal self-custody wallet' as WalletType,
}

function parseAmount(value: string) {
  const parsedValue = Number(value.replace(',', '.'))
  return Number.isFinite(parsedValue) && parsedValue > 0 ? parsedValue : 0
}

function isSensitiveAmount(value: string) {
  return /\d/.test(value)
}

function isWithdrawalStatus(value: string): value is WithdrawalStatus {
  return [
    'draft',
    'pending_review',
    'auto_approved',
    'auto_rejected',
    'blocked',
    'escalated',
  ].includes(value)
}

export function WithdrawalsPage() {
  const [asset, setAsset] = useState<WithdrawalAsset>(initialWithdrawal.asset)
  const [network, setNetwork] = useState(initialWithdrawal.network)
  const [amount, setAmount] = useState(initialWithdrawal.amount)
  const [destinationAddress, setDestinationAddress] = useState(
    initialWithdrawal.destinationAddress,
  )
  const [confirmDestinationAddress, setConfirmDestinationAddress] = useState(
    initialWithdrawal.confirmDestinationAddress,
  )
  const [destinationLabel, setDestinationLabel] = useState(
    initialWithdrawal.destinationLabel,
  )
  const [walletType, setWalletType] = useState<WalletType>(
    initialWithdrawal.walletType,
  )
  const [confirmAddressCorrect, setConfirmAddressCorrect] = useState(false)
  const [confirmIrreversible, setConfirmIrreversible] = useState(false)
  const [confirmLeavesProtection, setConfirmLeavesProtection] = useState(false)
  const [confirmNetworkRisk, setConfirmNetworkRisk] = useState(false)
  const [localStatus, setLocalStatus] = useState<WithdrawalStatus>('draft')
  const [backendDecision, setBackendDecision] =
    useState<RiskDecisionResponse | null>(null)
  const [backendError, setBackendError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const amountValue = parseAmount(amount)
  const addressEntered = destinationAddress.trim().length > 0
  const addressesMatch =
    addressEntered &&
    destinationAddress.trim() === confirmDestinationAddress.trim()
  const isEurd = asset === 'EURD'
  const allConfirmationsChecked =
    confirmAddressCorrect &&
    confirmIrreversible &&
    confirmLeavesProtection &&
    confirmNetworkRisk
  const canSubmit =
    amountValue > 0 && addressesMatch && allConfirmationsChecked

  const reviewStatus =
    backendDecision
      ? backendDecision.decision
          .replaceAll('_', ' ')
          .replace(/^\w/, (letter) => letter.toUpperCase())
      : localStatus === 'pending_review'
      ? 'Pending local prototype review'
      : !addressEntered
        ? 'Draft'
        : !addressesMatch
          ? 'Address mismatch'
          : amountValue > 0
            ? 'Ready for review'
            : 'Draft'

  const riskLevel =
    backendDecision
      ? backendDecision.risk_level
          .replace(/^\w/, (letter) => letter.toUpperCase())
      : reviewStatus === 'Address mismatch' ||
          walletType === 'Exchange deposit address'
      ? 'High'
      : addressEntered || walletType === 'External crypto service'
        ? 'Medium'
        : 'Low'

  const auditEvents = useMemo(() => {
    if (backendDecision) {
      return [
        {
          title: 'Evaluation submitted',
          detail: `${amount || '0'} ${asset} external transfer request was sent to the local FastAPI prototype for evaluation. No transfer is executed.`,
          status: 'Submitted',
        },
        {
          title: 'Backend decision returned',
          detail: backendDecision.user_message,
          status: backendDecision.decision.replaceAll('_', ' '),
        },
        ...(backendDecision.case_id
          ? [
              {
                title: 'Review case created',
                detail: `Case ${backendDecision.case_id} was created for compliance review.`,
                status: backendDecision.case_type ?? 'external withdrawal review',
              },
            ]
          : []),
        {
          title: 'Audit event recorded',
          detail: `Audit event type: ${backendDecision.audit_event_type}`,
          status: backendDecision.risk_level,
        },
      ]
    }

    const events = [
      {
        title: 'Withdrawal form opened',
        detail:
          'User opened the simulated external wallet transfer flow.',
        status: 'Recorded',
      },
      {
        title: 'Asset and network selected',
        detail: `${assetLabels[asset]} selected on ${network}.`,
        status: isEurd ? 'Unavailable externally' : 'Recorded',
      },
    ]

    if (addressEntered) {
      events.push({
        title: 'Destination address entered',
        detail: `${walletType} destination captured for review. No transfer is executed in this prototype.`,
        status: addressesMatch ? 'Confirmed' : 'Needs correction',
      })
    }

    if (addressesMatch && amountValue > 0) {
      events.push({
        title: 'Protection review prepared',
        detail:
          'Address confirmation, network compatibility, and external transfer review requirements are ready for manual review.',
        status: 'Ready for review',
      })
    }

    if (localStatus === 'pending_review') {
      events.push({
        title: 'Pending local prototype review',
        detail: `${amount || '0'} ${asset} external transfer request is pending review. No blockchain transaction is executed in this prototype.`,
        status: 'Local fallback',
      })
    }

    return events
  }, [
    addressEntered,
    addressesMatch,
    amount,
    amountValue,
    asset,
    isEurd,
    network,
    backendDecision,
    localStatus,
    walletType,
  ])

  function markDraft() {
    setLocalStatus('draft')
    setBackendDecision(null)
    setBackendError(null)
  }

  function handleAssetChange(nextAsset: WithdrawalAsset) {
    setAsset(nextAsset)
    setNetwork(networkOptions[nextAsset][0])
    markDraft()
  }

  async function handleSubmitReview() {
    if (!canSubmit) return
    setIsSubmitting(true)
    setBackendError(null)

    try {
      const decision = await evaluateWithdrawal({
        asset,
        network,
        amount: amountValue,
        destination_address: destinationAddress.trim(),
        confirm_destination_address: confirmDestinationAddress.trim(),
        wallet_type:
          walletType === 'Hardware wallet' ? 'trusted_address' : 'external_wallet',
      })
      setBackendDecision(decision)
      if (isWithdrawalStatus(decision.decision)) {
        setLocalStatus(decision.decision)
      } else {
        setLocalStatus('pending_review')
      }
    } catch {
      setBackendError(
        'Backend withdrawal evaluation unavailable. Showing local prototype status.',
      )
      setBackendDecision(null)
      setLocalStatus('pending_review')
    } finally {
      setIsSubmitting(false)
    }
  }

  function handleReset() {
    setAsset(initialWithdrawal.asset)
    setNetwork(initialWithdrawal.network)
    setAmount(initialWithdrawal.amount)
    setDestinationAddress(initialWithdrawal.destinationAddress)
    setConfirmDestinationAddress(initialWithdrawal.confirmDestinationAddress)
    setDestinationLabel(initialWithdrawal.destinationLabel)
    setWalletType(initialWithdrawal.walletType)
    setConfirmAddressCorrect(false)
    setConfirmIrreversible(false)
    setConfirmLeavesProtection(false)
    setConfirmNetworkRisk(false)
    setLocalStatus('draft')
    setBackendDecision(null)
    setBackendError(null)
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">External withdrawals</p>
            <h1>External wallet transfer</h1>
            <p>
              Send digital assets from the internal custodial wallet concept to
              a personal wallet or external crypto service.
            </p>
          </div>

          <div className="security-badge">
            <span
              className={
                localStatus === 'pending_review' ? 'warning-dot' : 'status-dot'
              }
            ></span>
            {backendDecision
              ? backendDecision.decision.replaceAll('_', ' ')
              : localStatus === 'pending_review'
                ? 'Pending local review'
                : 'Draft'}
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Asset and amount</p>
                  <h2>Asset and amount</h2>
                </div>
                <span className="module-tag">Simulated balance</span>
              </div>

              <div className="form-grid">
                <label>
                  Asset
                  <select
                    value={asset}
                    onChange={(event) =>
                      handleAssetChange(event.target.value as WithdrawalAsset)
                    }
                  >
                    <option value="BTC">BTC — Bitcoin</option>
                    <option value="ETH">ETH — Ethereum</option>
                    <option value="USDC">USDC</option>
                    <option value="USDT">USDT</option>
                    <option value="EURD">EUR digital asset concept</option>
                  </select>
                </label>

                <div className="assets-summary single-summary">
                  <div>
                    <p>Available balance</p>
                    <strong>
                      {isSensitiveAmount(assetBalances[asset]) ? (
                        <PrivacyAmount
                          value={assetBalances[asset]}
                          label={`${asset} available balance`}
                        />
                      ) : (
                        assetBalances[asset]
                      )}
                    </strong>
                    <span>Balance information is simulated.</span>
                  </div>
                </div>

                <label>
                  Amount
                  <input
                    value={amount}
                    inputMode="decimal"
                    onChange={(event) => {
                      setAmount(event.target.value)
                      markDraft()
                    }}
                  />
                  <span>Use dot or comma as decimal separator.</span>
                  {amountValue <= 0 && (
                    <span className="field-warning">Amount is required.</span>
                  )}
                </label>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Network</p>
                  <h2>Network</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  Network
                  <select
                    value={network}
                    onChange={(event) => {
                      setNetwork(event.target.value)
                      markDraft()
                    }}
                  >
                    {networkOptions[asset].map((networkOption) => (
                      <option value={networkOption} key={networkOption}>
                        {networkOption}
                      </option>
                    ))}
                  </select>
                </label>
              </div>

              {isEurd && (
                <p className="panel-note">
                  EUR digital asset concept is designed for internal settlement
                  in this prototype. External withdrawal is not available.
                </p>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Destination</p>
                  <h2>Destination</h2>
                </div>
                <span className="module-tag">External address</span>
              </div>

              <div className="form-grid">
                <label>
                  Destination address
                  <input
                    value={destinationAddress}
                    onChange={(event) => {
                      setDestinationAddress(event.target.value)
                      markDraft()
                    }}
                    placeholder="Example: bc1q..."
                  />
                </label>

                <label>
                  Confirm destination address
                  <input
                    value={confirmDestinationAddress}
                    onChange={(event) => {
                      setConfirmDestinationAddress(event.target.value)
                      markDraft()
                    }}
                    placeholder="Example: bc1q..."
                  />
                  {addressEntered && !addressesMatch && (
                    <span className="field-warning">
                      Destination addresses do not match.
                    </span>
                  )}
                </label>

                <label>
                  Destination label
                  <input
                    value={destinationLabel}
                    onChange={(event) => {
                      setDestinationLabel(event.target.value)
                      markDraft()
                    }}
                  />
                </label>

                <label>
                  Wallet type
                  <select
                    value={walletType}
                    onChange={(event) => {
                      setWalletType(event.target.value as WalletType)
                      markDraft()
                    }}
                  >
                    <option value="Personal self-custody wallet">
                      Personal self-custody wallet
                    </option>
                    <option value="Hardware wallet">Hardware wallet</option>
                    <option value="External crypto service">
                      External crypto service
                    </option>
                    <option value="Exchange deposit address">
                      Exchange deposit address
                    </option>
                  </select>
                </label>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Protection review</p>
                  <h2>Protection review</h2>
                </div>
                <span className="module-tag">{reviewStatus}</span>
              </div>

              <div className="check-list">
                <div>
                  <span className={addressEntered ? 'status-dot' : 'warning-dot'}></span>
                  Address format check
                </div>
                <div>
                  <span className={addressesMatch ? 'status-dot' : 'warning-dot'}></span>
                  Address confirmation
                </div>
                <div>
                  <span className={!isEurd ? 'status-dot' : 'warning-dot'}></span>
                  Network compatibility evaluated by backend
                </div>
                <div>
                  <span className={addressEntered ? 'warning-dot' : 'status-dot'}></span>
                  New address review
                </div>
                <div>
                  <span className="warning-dot"></span>
                  External transfer review
                </div>
              </div>

              <div className="withdrawal-preview">
                <div>
                  <p>Risk level</p>
                  <strong>{riskLevel}</strong>
                </div>
                <div>
                  <p>Review state</p>
                  <strong>{reviewStatus}</strong>
                </div>
                <div>
                  <p>Execution</p>
                  <strong>Not executed</strong>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">User confirmations</p>
                  <h2>User confirmations</h2>
                </div>
              </div>

              <div className="check-list">
                <label>
                  <input
                    type="checkbox"
                    checked={confirmAddressCorrect}
                    onChange={(event) => {
                      setConfirmAddressCorrect(event.target.checked)
                      markDraft()
                    }}
                  />
                  I confirm the destination address is correct.
                </label>
                <label>
                  <input
                    type="checkbox"
                    checked={confirmIrreversible}
                    onChange={(event) => {
                      setConfirmIrreversible(event.target.checked)
                      markDraft()
                    }}
                  />
                  I understand blockchain transfers are irreversible.
                </label>
                <label>
                  <input
                    type="checkbox"
                    checked={confirmLeavesProtection}
                    onChange={(event) => {
                      setConfirmLeavesProtection(event.target.checked)
                      markDraft()
                    }}
                  />
                  I understand assets may leave the bank protection environment.
                </label>
                <label>
                  <input
                    type="checkbox"
                    checked={confirmNetworkRisk}
                    onChange={(event) => {
                      setConfirmNetworkRisk(event.target.checked)
                      markDraft()
                    }}
                  />
                  I understand wrong network selection may cause permanent loss.
                </label>
              </div>

              <div className="action-row">
                <button
                  type="button"
                  onClick={handleSubmitReview}
                  disabled={!canSubmit || isSubmitting}
                >
                  {isSubmitting ? 'Submitting...' : 'Submit for review'}
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={handleReset}
                >
                  Reset
                </button>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Transfer summary</p>
              <h2>Live summary</h2>

              <div className="summary-list">
                <div>
                  <span>Asset</span>
                  <strong>{assetLabels[asset]}</strong>
                </div>
                <div>
                  <span>Network</span>
                  <strong>{network}</strong>
                </div>
                <div>
                  <span>Amount</span>
                  <strong>
                    {amountValue > 0 ? (
                      <PrivacyAmount
                        value={`${amount} ${asset}`}
                        label="Withdrawal amount"
                      />
                    ) : (
                      'Not entered'
                    )}
                  </strong>
                </div>
                <div>
                  <span>Destination label</span>
                  <strong>{destinationLabel || 'Not entered'}</strong>
                </div>
                <div>
                  <span>Wallet type</span>
                  <strong>{walletType}</strong>
                </div>
                <div>
                  <span>Status</span>
                  <strong>{reviewStatus}</strong>
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Risk warning</p>
              <h2>Irreversible transfer</h2>
              <p>
                Blockchain transfers cannot usually be reversed. Always verify
                the address, network, and wallet provider before submitting.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Review status</p>
              <h2>Transfer protection</h2>
              {backendDecision && (
                <p className="panel-note">
                  Withdrawal evaluation loaded from local FastAPI prototype.
                </p>
              )}
              {backendError && (
                <p className="panel-note">{backendError}</p>
              )}
              {backendDecision && (
                <div className="summary-list">
                  <div>
                    <span>Decision</span>
                    <strong>{backendDecision.decision}</strong>
                  </div>
                  <div>
                    <span>Risk level</span>
                    <strong>{backendDecision.risk_level}</strong>
                  </div>
                  <div>
                    <span>Message</span>
                    <strong>{backendDecision.user_message}</strong>
                  </div>
                  {backendDecision.case_id && (
                    <div>
                      <span>Review case</span>
                      <strong>{backendDecision.case_id}</strong>
                      <Link
                        className="button-link secondary-button"
                        to="/compliance-review"
                      >
                        View in Compliance Review
                      </Link>
                    </div>
                  )}
                  <div>
                    <span>Case required</span>
                    <strong>{backendDecision.case_required ? 'Yes' : 'No'}</strong>
                  </div>
                  {backendDecision.reasons.length > 0 && (
                    <div>
                      <span>Reasons</span>
                      <strong>{backendDecision.reasons.join(', ')}</strong>
                    </div>
                  )}
                </div>
              )}
              {!backendDecision && (
                <div className="summary-list">
                  <div>
                    <span>Decision</span>
                    <strong>{reviewStatus}</strong>
                  </div>
                  <div>
                    <span>Risk level</span>
                    <strong>{riskLevel}</strong>
                  </div>
                </div>
              )}
              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Strong authentication active
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Address review required
                </div>
                <div>
                  <span className="warning-dot"></span>
                  External transfer review active
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  No transfer is executed in this prototype
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Important boundary</p>
              <h2>External transfer only</h2>
              <p>
                Payments to verified business recipients are handled in
                Payments. This page is only for external wallet transfers.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Audit trail</p>
              <h2>Withdrawal evidence timeline</h2>

              <div className="account-list compact-audit-list">
                {auditEvents.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                  </article>
                ))}
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page simulates an external wallet
          transfer flow and does not process real blockchain transactions.
        </section>
      </main>
    </div>
  )
}
