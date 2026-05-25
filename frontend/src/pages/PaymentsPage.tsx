import { useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { PrivacyAmount } from '../components/PrivacyAmount'
import { primaryBankAccount } from '../data/bankAccounts'
import {
  evaluateDigitalAssetPayment,
  type DigitalAssetPaymentEvaluateResponse,
} from '../services/paymentsApi'

type PaymentMethod = 'eur-transfer' | 'digital-asset'
type PaymentAsset = 'EURD' | 'USDC' | 'USDT' | 'BTC' | 'ETH'
type PaymentStatus = 'draft' | 'ready' | 'submitted'
type RecipientMode = 'own' | 'saved' | 'new'
type ScheduleMode = 'one-time' | 'recurring'
type DetailsMode = 'reference' | 'message'

const initialInvoice = {
  recipient: 'Aurora Telecom Oyj',
  invoiceNumber: '90495185862',
  referenceNumber: '80 60206 95479',
  dueDate: '19.05.2026',
  amount: '120.45',
  payerAccount: 'Aurora Current Account',
  recipientIban: 'FI98 0000 0000 5678 90',
}

const assetRates: Record<PaymentAsset, number> = {
  EURD: 1,
  USDC: 0.928,
  USDT: 0.926,
  BTC: 69500,
  ETH: 2066.88,
}

const assetLabels: Record<PaymentAsset, string> = {
  EURD: 'EUR digital asset concept',
  USDC: 'USDC',
  USDT: 'USDT',
  BTC: 'BTC — Bitcoin',
  ETH: 'ETH — Ethereum',
}

function formatEur(value: number) {
  return new Intl.NumberFormat('fi-FI', {
    style: 'currency',
    currency: 'EUR',
  }).format(value)
}

function formatAssetAmount(value: number, asset: PaymentAsset | string) {
  if (asset === 'BTC') return `${value.toFixed(8)} BTC`
  if (asset === 'ETH') return `${value.toFixed(6)} ETH`
  if (asset === 'EURD') return `${value.toFixed(2)} EURD`
  return `${value.toFixed(2)} ${asset}`
}

export function PaymentsPage() {
  const [recipient, setRecipient] = useState(initialInvoice.recipient)
  const [recipientMode, setRecipientMode] = useState<RecipientMode>('saved')
  const [recipientIban, setRecipientIban] = useState(initialInvoice.recipientIban)
  const [saveRecipient, setSaveRecipient] = useState(false)
  const [moveToApprovalQueue, setMoveToApprovalQueue] = useState(false)
  const [scheduleMode, setScheduleMode] = useState<ScheduleMode>('one-time')
  const [detailsMode, setDetailsMode] = useState<DetailsMode>('reference')
  const [referenceNumber, setReferenceNumber] = useState(
    initialInvoice.referenceNumber,
  )
  const [message, setMessage] = useState('')
  const [dueDate, setDueDate] = useState(initialInvoice.dueDate)
  const [amount, setAmount] = useState(initialInvoice.amount)
  const [payerAccount, setPayerAccount] = useState(initialInvoice.payerAccount)
  const [paymentMethod, setPaymentMethod] =
    useState<PaymentMethod>('eur-transfer')
  const [paymentAsset, setPaymentAsset] = useState<PaymentAsset>('EURD')
  const [status, setStatus] = useState<PaymentStatus>('draft')
  const [backendEvaluation, setBackendEvaluation] =
    useState<DigitalAssetPaymentEvaluateResponse | null>(null)
  const [backendError, setBackendError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const parsedAmount = Number(amount.replace(',', '.'))
  const amountIsValid = Number.isFinite(parsedAmount) && parsedAmount > 0
  const amountEur = amountIsValid ? parsedAmount : 0

  const currentRecipient =
    recipientMode === 'own'
      ? 'Own account not selected'
      : recipient.trim() || 'Selected business recipient'

  const hasRecipient = recipientMode !== 'own' && recipient.trim().length > 0
  const detailsValue =
    detailsMode === 'reference' ? referenceNumber.trim() : message.trim()
  const recipientEligible = recipientMode !== 'own' && recipient.trim().length > 0

  const digitalAssetReferenceReady =
    paymentMethod !== 'digital-asset' ||
    (detailsMode === 'reference' && referenceNumber.trim().length > 0)

  const canSubmit =
    amountEur > 0 &&
    dueDate.trim().length > 0 &&
    payerAccount.trim().length > 0 &&
    hasRecipient &&
    detailsValue.length > 0 &&
    digitalAssetReferenceReady &&
    (paymentMethod !== 'digital-asset' || recipientEligible)

  const visibleStatus: PaymentStatus =
    status === 'submitted' ? 'submitted' : canSubmit ? 'ready' : 'draft'

  const isInternalDigitalAssetSettlement =
    paymentMethod === 'digital-asset' && paymentAsset === 'EURD'
  const isExternalDigitalAssetPayment =
    paymentMethod === 'digital-asset' && paymentAsset !== 'EURD'

  const serviceFee = isExternalDigitalAssetPayment ? 1.2 : 0
  const settlementFee = isExternalDigitalAssetPayment ? 0.3 : 0

  const feeExplanation = isInternalDigitalAssetSettlement
    ? 'Internal EUR digital asset settlement concept. No additional processing fee in this prototype.'
    : 'Simulated bank service fee for external digital asset payment processing.'

  const settlementExplanation = isInternalDigitalAssetSettlement
    ? 'Internal settlement concept. The invoice reference is preserved.'
    : 'Simulated settlement fee. The invoice reference is preserved.'

  const estimate = useMemo(() => {
    const totalCostEur = amountEur + serviceFee + settlementFee
    const selectedRate = assetRates[paymentAsset]
    const assetAmount = totalCostEur / selectedRate

    return {
      totalCostEur,
      assetAmount,
      selectedRate,
    }
  }, [amountEur, paymentAsset, serviceFee, settlementFee])

  const displayedEstimate = backendEvaluation?.estimate
    ? {
        invoiceAmountEur: backendEvaluation.estimate.invoice_amount_eur,
        totalCostEur: backendEvaluation.estimate.total_estimated_cost_eur,
        assetAmount: backendEvaluation.estimate.estimated_asset_amount,
        conversionRateEur: backendEvaluation.estimate.conversion_rate_eur,
        serviceFee: backendEvaluation.estimate.service_fee_eur,
        settlementFee: backendEvaluation.estimate.settlement_fee_eur,
        paymentAsset: backendEvaluation.estimate.payment_asset,
        recipientSettlement: backendEvaluation.estimate.recipient_settlement,
      }
    : {
        invoiceAmountEur: amountEur,
        totalCostEur: estimate.totalCostEur,
        assetAmount: estimate.assetAmount,
        conversionRateEur: estimate.selectedRate,
        serviceFee,
        settlementFee,
        paymentAsset,
        recipientSettlement: 'Recipient receives EUR',
      }

  const localAuditEvents = [
    {
      title: 'Payment form opened',
      detail: `User opened the simulated payment flow for ${currentRecipient}.`,
      status: 'Recorded',
    },
    {
      title: 'Recipient eligibility checked',
      detail: `${currentRecipient} is treated as a verified Aurora Bank business recipient for invoice ${initialInvoice.invoiceNumber}.`,
      status: 'Eligible',
    },
    ...(paymentMethod === 'digital-asset'
      ? [
          {
            title: 'Digital asset payment method selected',
            detail: `${assetLabels[paymentAsset]} selected for invoice ${initialInvoice.invoiceNumber} with ${
              detailsMode === 'reference' ? 'reference' : 'message'
            } ${detailsValue || 'not yet provided'}.`,
            status: 'Estimated',
          },
        ]
      : [
          {
            title: 'EUR bank transfer selected',
            detail: `Standard EUR transfer selected for invoice ${initialInvoice.invoiceNumber} with ${
              detailsMode === 'reference' ? 'reference' : 'message'
            } ${detailsValue || 'not yet provided'}.`,
            status: 'Estimated',
          },
        ]),
    {
      title: 'Payment amount estimated',
      detail: `Current editable amount is ${formatEur(amountEur)} for ${currentRecipient}.`,
      status: amountEur > 0 ? 'Ready' : 'Draft',
    },
    ...(canSubmit
      ? [
          {
            title: 'Payment form validated',
            detail: `${currentRecipient}, payment details, date, payer account, and amount are present.`,
            status: 'Ready',
          },
        ]
      : []),
    ...(status === 'submitted'
      ? [
          {
            title: 'Payment submitted to prototype evaluation',
            detail:
              paymentMethod === 'digital-asset'
                ? `Invoice ${initialInvoice.invoiceNumber} was submitted to the local backend evaluation flow using ${assetLabels[paymentAsset]}. No real payment was executed.`
                : `Invoice ${initialInvoice.invoiceNumber} was submitted as a local simulated EUR bank transfer. No real payment was executed.`,
            status: 'Submitted',
          },
        ]
      : []),
  ]

  const backendAuditEvents = backendEvaluation
    ? [
        {
          title: 'Payment evaluation submitted',
          detail: `Digital asset payment evaluation was submitted to the local FastAPI prototype for ${currentRecipient}.`,
          status: 'Submitted',
        },
        {
          title: 'Backend decision returned',
          detail: backendEvaluation.user_message,
          status: backendEvaluation.decision.replaceAll('_', ' '),
        },
        ...(backendEvaluation.case_id
          ? [
              {
                title: 'Review case created',
                detail: `Case ${backendEvaluation.case_id} was created for internal review.`,
                status: 'Case created',
              },
            ]
          : []),
        {
          title: 'Audit event recorded',
          detail: backendEvaluation.audit_event_type.replaceAll('_', ' '),
          status: 'Recorded',
        },
      ]
    : null

  const visibleAuditEvents = backendAuditEvents ?? localAuditEvents

  function markDraft() {
    setStatus('draft')
    setBackendEvaluation(null)
    setBackendError(null)
  }

  function updateEditableField(
    value: string,
    updateValue: (nextValue: string) => void,
  ) {
    updateValue(value)
    markDraft()
  }

  async function handleSubmit() {
    if (!canSubmit) return

    setIsSubmitting(true)
    setBackendError(null)

    if (paymentMethod !== 'digital-asset') {
      setStatus('submitted')
      setIsSubmitting(false)
      return
    }

    try {
      const evaluation = await evaluateDigitalAssetPayment({
        recipient_name: recipient.trim(),
        invoice_number: initialInvoice.invoiceNumber,
        reference_number: referenceNumber.trim(),
        amount_eur: amountEur,
        payment_asset: paymentAsset,
        source_account_id: primaryBankAccount.id,
      })

      setBackendEvaluation(evaluation)
      setStatus('submitted')
    } catch {
      setBackendError(
        'Backend digital asset payment evaluation unavailable. Showing local prototype estimate.',
      )
      setBackendEvaluation(null)
      setStatus('submitted')
    } finally {
      setIsSubmitting(false)
    }
  }

  function handleReset() {
    setRecipient(initialInvoice.recipient)
    setRecipientMode('saved')
    setRecipientIban(initialInvoice.recipientIban)
    setSaveRecipient(false)
    setMoveToApprovalQueue(false)
    setScheduleMode('one-time')
    setDetailsMode('reference')
    setReferenceNumber(initialInvoice.referenceNumber)
    setMessage('')
    setDueDate(initialInvoice.dueDate)
    setAmount(initialInvoice.amount)
    setPayerAccount(initialInvoice.payerAccount)
    setPaymentMethod('eur-transfer')
    setPaymentAsset('EURD')
    setStatus('draft')
    setBackendEvaluation(null)
    setBackendError(null)
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Payments</p>
            <h1>New payment</h1>
            <p>
              Create a standard bank payment or, when the recipient supports it,
              a controlled digital asset payment.
            </p>
          </div>

          <div className="security-badge">
            <span
              className={
                visibleStatus === 'draft' ? 'warning-dot' : 'status-dot'
              }
            ></span>
            {visibleStatus === 'submitted'
              ? 'Submitted'
              : visibleStatus === 'ready'
                ? 'Ready'
                : 'Draft'}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Amount</p>
                  <h2>Amount</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  Amount
                  <input
                    value={amount}
                    inputMode="decimal"
                    onChange={(event) =>
                      updateEditableField(event.target.value, setAmount)
                    }
                  />
                  <span>Use dot or comma as decimal separator.</span>
                  {!amountIsValid && (
                    <span className="field-warning">Amount is required.</span>
                  )}
                </label>

                <label>
                  Currency
                  <select defaultValue="EUR">
                    <option value="EUR">EUR</option>
                  </select>
                </label>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">From account</p>
                  <h2>From account</h2>
                </div>
              </div>

              <div className="form-grid">
                <label>
                  Payer account
                  <select
                    value={payerAccount}
                    onChange={(event) =>
                      updateEditableField(event.target.value, setPayerAccount)
                    }
                  >
                    <option value={primaryBankAccount.name}>
                      {primaryBankAccount.name}
                    </option>
                  </select>
                </label>

                <div className="assets-summary single-summary">
                  <div>
                    <p>Available balance</p>
                    <strong>
                      <PrivacyAmount
                        value={primaryBankAccount.availableBalance}
                        label="Available balance"
                      />
                    </strong>
                    <span>
                      {primaryBankAccount.type} · {primaryBankAccount.iban}
                    </span>
                  </div>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">To recipient</p>
                  <h2>To recipient</h2>
                </div>
                <span className="module-tag">Simulated recipient data</span>
              </div>

              <div className="trade-toggle" aria-label="Recipient type">
                <button
                  type="button"
                  className={
                    recipientMode === 'own'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setRecipientMode('own')
                    markDraft()
                  }}
                >
                  Own accounts
                </button>

                <button
                  type="button"
                  className={
                    recipientMode === 'saved'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setRecipientMode('saved')
                    setRecipient(initialInvoice.recipient)
                    markDraft()
                  }}
                >
                  Saved recipient
                </button>

                <button
                  type="button"
                  className={
                    recipientMode === 'new'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setRecipientMode('new')
                    markDraft()
                  }}
                >
                  New recipient
                </button>
              </div>

              {recipientMode === 'own' && (
                <p className="panel-note">
                  Own account transfers are shown as a placeholder in this
                  prototype.
                </p>
              )}

              {recipientMode === 'saved' && (
                <div className="form-grid">
                  <label>
                    Saved recipient
                    <input
                      value={recipient}
                      onChange={(event) =>
                        updateEditableField(event.target.value, setRecipient)
                      }
                    />
                  </label>
                </div>
              )}

              {recipientMode === 'new' && (
                <div className="form-grid">
                  <label>
                    Recipient name
                    <input
                      value={recipient}
                      onChange={(event) =>
                        updateEditableField(event.target.value, setRecipient)
                      }
                    />
                  </label>

                  <label>
                    IBAN
                    <input
                      value={recipientIban}
                      onChange={(event) =>
                        updateEditableField(
                          event.target.value,
                          setRecipientIban,
                        )
                      }
                    />
                  </label>

                  <label className="checkbox-label">
                    <input
                      type="checkbox"
                      checked={saveRecipient}
                      onChange={(event) => {
                        setSaveRecipient(event.target.checked)
                        markDraft()
                      }}
                    />
                    Save recipient
                  </label>
                </div>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Date</p>
                  <h2>Date</h2>
                </div>
              </div>

              <div className="trade-toggle" aria-label="Payment schedule">
                <button
                  type="button"
                  className={
                    scheduleMode === 'one-time'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setScheduleMode('one-time')
                    markDraft()
                  }}
                >
                  One-time payment
                </button>

                <button
                  type="button"
                  className={
                    scheduleMode === 'recurring'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setScheduleMode('recurring')
                    markDraft()
                  }}
                >
                  Recurring payment
                </button>
              </div>

              <div className="form-grid">
                <label>
                  Payment date
                  <input
                    value={dueDate}
                    onChange={(event) =>
                      updateEditableField(event.target.value, setDueDate)
                    }
                  />
                </label>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Details</p>
                  <h2>Details</h2>
                </div>
              </div>

              <div className="trade-toggle" aria-label="Payment details type">
                <button
                  type="button"
                  className={
                    detailsMode === 'reference'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setDetailsMode('reference')
                    markDraft()
                  }}
                >
                  Reference number
                </button>

                <button
                  type="button"
                  className={
                    detailsMode === 'message'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setDetailsMode('message')
                    markDraft()
                  }}
                >
                  Message
                </button>
              </div>

              <div className="form-grid">
                {detailsMode === 'reference' ? (
                  <label>
                    Reference number
                    <input
                      value={referenceNumber}
                      onChange={(event) =>
                        updateEditableField(
                          event.target.value,
                          setReferenceNumber,
                        )
                      }
                    />
                  </label>
                ) : (
                  <label>
                    Message
                    <input
                      value={message}
                      onChange={(event) =>
                        updateEditableField(event.target.value, setMessage)
                      }
                    />
                  </label>
                )}
              </div>

              {paymentMethod === 'digital-asset' &&
                detailsMode === 'message' && (
                  <p className="field-warning">
                    Digital asset invoice payments require a reference number so
                    the invoice record can be preserved.
                  </p>
                )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Payment method</p>
                  <h2>Payment method</h2>
                </div>
                <span className="module-tag">Banking flow</span>
              </div>

              <div className="trade-toggle" aria-label="Payment method">
                <button
                  type="button"
                  className={
                    paymentMethod === 'eur-transfer'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setPaymentMethod('eur-transfer')
                    markDraft()
                  }}
                >
                  EUR bank transfer
                </button>

                <button
                  type="button"
                  className={
                    paymentMethod === 'digital-asset'
                      ? 'toggle-active'
                      : 'secondary-button'
                  }
                  onClick={() => {
                    setPaymentMethod('digital-asset')
                    markDraft()
                  }}
                  disabled={!recipientEligible}
                >
                  Digital asset payment
                </button>
              </div>

              {paymentMethod === 'digital-asset' && (
                <>
                  <div className="form-grid">
                    <label>
                      Digital asset
                      <select
                        value={paymentAsset}
                        onChange={(event) => {
                          setPaymentAsset(event.target.value as PaymentAsset)
                          markDraft()
                        }}
                      >
                        <option value="EURD">EUR digital asset concept</option>
                        <option value="USDC">USDC</option>
                        <option value="USDT">USDT</option>
                        <option value="BTC">BTC — Bitcoin</option>
                        <option value="ETH">ETH — Ethereum</option>
                      </select>
                    </label>

                    <label>
                      Recipient settlement
                      <input value={displayedEstimate.recipientSettlement} readOnly />
                    </label>
                  </div>

                  <div className="withdrawal-preview">
                    <div>
                      <p>Invoice amount</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(displayedEstimate.invoiceAmountEur)}
                          label="Invoice amount"
                        />
                      </strong>
                    </div>
                    <div>
                      <p>Estimated asset amount</p>
                      <strong>
                        <PrivacyAmount
                          value={formatAssetAmount(
                            displayedEstimate.assetAmount,
                            displayedEstimate.paymentAsset,
                          )}
                          label="Estimated asset amount"
                        />
                      </strong>
                    </div>
                    <div>
                      <p>Total estimated cost</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(displayedEstimate.totalCostEur)}
                          label="Total estimated cost"
                        />
                      </strong>
                    </div>
                  </div>

                  <div className="summary-list">
                    <div>
                      <span>Conversion rate</span>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(displayedEstimate.conversionRateEur)}
                          label="Conversion rate"
                        />
                      </strong>
                    </div>
                    <div>
                      <span>Recipient settlement</span>
                      <strong>{displayedEstimate.recipientSettlement}</strong>
                    </div>
                    {backendEvaluation && (
                      <>
                        <div>
                          <span>Backend decision</span>
                          <strong>{backendEvaluation.decision}</strong>
                        </div>
                        <div>
                          <span>Risk level</span>
                          <strong>{backendEvaluation.risk_level}</strong>
                        </div>
                      </>
                    )}
                  </div>

                  <div className="assets-summary trade-summary">
                    <div>
                      <p>Service fee</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(displayedEstimate.serviceFee)}
                          label="Service fee"
                        />
                      </strong>
                      <span>{feeExplanation}</span>
                    </div>

                    <div className="custody-card">
                      <p>Settlement fee</p>
                      <strong>
                        <PrivacyAmount
                          value={formatEur(displayedEstimate.settlementFee)}
                          label="Settlement fee"
                        />
                      </strong>
                      <span>{settlementExplanation}</span>
                    </div>
                  </div>
                </>
              )}

              {paymentMethod === 'eur-transfer' && (
                <div className="assets-summary trade-summary">
                  <div>
                    <p>Payment type</p>
                    <strong>Standard EUR bank transfer</strong>
                    <span>
                      The invoice is paid using normal banking payment rails in
                      the product concept. No real payment is executed here.
                    </span>
                  </div>

                  <div className="custody-card">
                    <p>Total amount</p>
                    <strong>
                      <PrivacyAmount
                        value={formatEur(amountEur)}
                        label="Total amount"
                      />
                    </strong>
                    <span>
                      The recipient, reference number, and due date remain
                      attached to the payment.
                    </span>
                  </div>
                </div>
              )}
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Settings</p>
                  <h2>Settings</h2>
                </div>
              </div>

              <div className="check-list">
                <label>
                  <input
                    type="checkbox"
                    checked={moveToApprovalQueue}
                    onChange={(event) => {
                      setMoveToApprovalQueue(event.target.checked)
                      markDraft()
                    }}
                  />
                  Move to approval queue
                </label>
              </div>

              <div className="action-row">
                <button
                  type="button"
                  onClick={handleSubmit}
                  disabled={!canSubmit || isSubmitting}
                >
                  {isSubmitting ? 'Submitting...' : 'Submit payment'}
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
              <p className="eyebrow">Payment details</p>
              <h2>Live summary</h2>

              <div className="summary-list">
                <div>
                  <span>Amount</span>
                  <strong>
                    <PrivacyAmount
                      value={formatEur(amountEur)}
                      label="Payment amount"
                    />
                  </strong>
                </div>
                <div>
                  <span>From</span>
                  <strong>{payerAccount || 'Not selected'}</strong>
                </div>
                <div>
                  <span>To</span>
                  <strong>{currentRecipient}</strong>
                </div>
                <div>
                  <span>Date</span>
                  <strong>{dueDate || 'Not selected'}</strong>
                </div>
                <div>
                  <span>Details</span>
                  <strong>{detailsValue || 'Not provided'}</strong>
                </div>
                <div>
                  <span>Payment method</span>
                  <strong>
                    {paymentMethod === 'digital-asset'
                      ? `Digital asset payment · ${paymentAsset}`
                      : 'EUR bank transfer'}
                  </strong>
                </div>
                <div>
                  <span>Status</span>
                  <strong>
                    {backendEvaluation
                      ? backendEvaluation.decision
                      : visibleStatus === 'submitted'
                        ? 'Submitted'
                        : visibleStatus === 'ready'
                          ? 'Ready'
                          : 'Draft'}
                  </strong>
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Recipient eligibility</p>
              <h2>{currentRecipient}</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Aurora Bank business account active
                </div>
                <div>
                  <span className="status-dot"></span>
                  Digital asset payments enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  Invoice reference preserved
                </div>
                <div>
                  <span className="status-dot"></span>
                  Recipient settlement preference available
                </div>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Important boundary</p>
              <h2>Not an external wallet transfer</h2>
              <p>
                This payment flow is only for eligible business recipients inside
                the banking environment. Payments to arbitrary wallet addresses
                are handled separately through External Withdrawals.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Payment protection</p>
              <h2>Controls active</h2>

              {backendError && <p className="panel-note">{backendError}</p>}
              {backendEvaluation && (
                <p className="panel-note">
                  Digital asset payment evaluation loaded from local FastAPI
                  prototype.
                </p>
              )}

              {backendEvaluation && (
                <div className="summary-list">
                  <div>
                    <span>Decision</span>
                    <strong>{backendEvaluation.decision}</strong>
                  </div>
                  <div>
                    <span>Risk level</span>
                    <strong>{backendEvaluation.risk_level}</strong>
                  </div>
                  <div>
                    <span>Message</span>
                    <strong>{backendEvaluation.user_message}</strong>
                  </div>
                  <div>
                    <span>Case required</span>
                    <strong>{backendEvaluation.case_required ? 'Yes' : 'No'}</strong>
                  </div>
                  {backendEvaluation.case_id && (
                    <div>
                      <span>Review case</span>
                      <strong>{backendEvaluation.case_id}</strong>
                    </div>
                  )}
                  <div>
                    <span>Reasons</span>
                    <strong>{backendEvaluation.reasons.join(', ')}</strong>
                  </div>
                </div>
              )}

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Recipient validation
                </div>
                <div>
                  <span className="status-dot"></span>
                  Payment reference preserved
                </div>
                <div>
                  <span className="status-dot"></span>
                  Transaction monitoring enabled
                </div>
                <div>
                  <span className="status-dot"></span>
                  Audit trail enabled
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Digital asset values may fluctuate
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Audit trail</p>
              <h2>Payment evidence timeline</h2>

              <div className="account-list compact-audit-list">
                {visibleAuditEvents.map((event) => (
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
          Independent concept prototype. This page simulates invoice payment
          flows and does not process real payments, bank transfers, crypto
          transactions, or settlement.
        </section>
      </main>
    </div>
  )
}