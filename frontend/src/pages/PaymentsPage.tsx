import { useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

type PaymentMethod = 'eur-transfer' | 'digital-asset'
type PaymentAsset = 'EURD' | 'USDC' | 'USDT' | 'BTC' | 'ETH'
type PaymentStatus = 'draft' | 'ready' | 'submitted'

const invoice = {
  recipient: 'Aurora Telecom Oyj',
  businessAccountStatus: 'Active',
  digitalAssetPayments: 'Enabled',
  invoiceNumber: '90495185862',
  referenceNumber: '80 60206 95479',
  dueDate: '19.05.2026',
  amountEur: 120.45,
  currency: 'EUR',
  payerAccount: 'Aurora Current Account',
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

function formatAssetAmount(value: number, asset: PaymentAsset) {
  if (asset === 'BTC') return `${value.toFixed(8)} BTC`
  if (asset === 'ETH') return `${value.toFixed(6)} ETH`
  if (asset === 'EURD') return `${value.toFixed(2)} EURD`
  return `${value.toFixed(2)} ${asset}`
}

export function PaymentsPage() {
  const [paymentMethod, setPaymentMethod] =
    useState<PaymentMethod>('eur-transfer')
  const [paymentAsset, setPaymentAsset] = useState<PaymentAsset>('EURD')
  const [status, setStatus] = useState<PaymentStatus>('draft')

  const recipientEligible = true
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
    const totalCostEur = invoice.amountEur + serviceFee + settlementFee
    const selectedRate = assetRates[paymentAsset]
    const assetAmount = totalCostEur / selectedRate

    return {
      totalCostEur,
      assetAmount,
      selectedRate,
    }
  }, [paymentAsset, serviceFee, settlementFee])

  const auditEvents = [
    {
      title: 'Payment form opened',
      detail: 'User opened the simulated invoice payment flow.',
      status: 'Recorded',
    },
    {
      title: 'Recipient eligibility checked',
      detail:
        'Business recipient has an active Aurora Bank account and accepts digital asset payments.',
      status: 'Eligible',
    },
    ...(paymentMethod === 'digital-asset'
      ? [
          {
            title: 'Digital asset payment method selected',
            detail: `${assetLabels[paymentAsset]} selected for invoice payment.`,
            status: 'Estimated',
          },
        ]
      : []),
    ...(status === 'submitted'
      ? [
          {
            title: 'Payment submitted',
            detail:
              paymentMethod === 'digital-asset'
                ? `Invoice payment submitted using ${assetLabels[paymentAsset]}. Recipient settlement remains linked to the invoice reference.`
                : 'Invoice payment submitted as a standard EUR bank transfer.',
            status: 'Submitted',
          },
        ]
      : []),
  ]

  function handleSubmit() {
    setStatus('submitted')
  }

  function handleReset() {
    setPaymentMethod('eur-transfer')
    setPaymentAsset('EURD')
    setStatus('draft')
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Payments</p>
            <h1>Invoice payment</h1>
            <p>
              Pay a standard invoice using a normal EUR bank transfer or, when
              the recipient supports it, a controlled digital asset payment.
            </p>
          </div>

          <div className="security-badge">
            <span
              className={status === 'submitted' ? 'status-dot' : 'warning-dot'}
            ></span>
            {status === 'submitted' ? 'Submitted' : 'Draft'}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">New payment</p>
                  <h2>Invoice details</h2>
                </div>
                <span className="module-tag">Mock invoice</span>
              </div>

              <div className="form-grid">
                <label>
                  Recipient
                  <input value={invoice.recipient} readOnly />
                </label>

                <label>
                  Invoice number
                  <input value={invoice.invoiceNumber} readOnly />
                </label>

                <label>
                  Reference number
                  <input value={invoice.referenceNumber} readOnly />
                </label>

                <label>
                  Due date
                  <input value={invoice.dueDate} readOnly />
                </label>

                <label>
                  Amount
                  <input value={formatEur(invoice.amountEur)} readOnly />
                </label>

                <label>
                  Payer account
                  <input value={invoice.payerAccount} readOnly />
                </label>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Payment method</p>
                  <h2>Select how to pay</h2>
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
                    setStatus('draft')
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
                    setStatus('draft')
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
                          setStatus('draft')
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
                      <input value="Recipient receives EUR" readOnly />
                    </label>
                  </div>

                  <div className="withdrawal-preview">
                    <div>
                      <p>Invoice amount</p>
                      <strong>{formatEur(invoice.amountEur)}</strong>
                    </div>
                    <div>
                      <p>Estimated asset amount</p>
                      <strong>
                        {formatAssetAmount(estimate.assetAmount, paymentAsset)}
                      </strong>
                    </div>
                    <div>
                      <p>Total estimated cost</p>
                      <strong>{formatEur(estimate.totalCostEur)}</strong>
                    </div>
                  </div>

                  <div className="assets-summary trade-summary">
                    <div>
                      <p>Service fee</p>
                      <strong>{formatEur(serviceFee)}</strong>
                      <span>{feeExplanation}</span>
                    </div>

                    <div className="custody-card">
                      <p>Settlement fee</p>
                      <strong>{formatEur(settlementFee)}</strong>
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
                      The invoice is paid using normal banking payment rails.
                    </span>
                  </div>

                  <div className="custody-card">
                    <p>Total amount</p>
                    <strong>{formatEur(invoice.amountEur)}</strong>
                    <span>
                      The recipient, reference number, and due date remain
                      attached to the payment.
                    </span>
                  </div>
                </div>
              )}

              <div className="action-row">
                <button type="button" onClick={handleSubmit}>
                  Submit payment
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

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Audit trail</p>
                  <h2>Payment evidence timeline</h2>
                </div>
                <span className="module-tag">Deterministic log</span>
              </div>

              <div className="account-list">
                {auditEvents.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Recipient eligibility</p>
              <h2>Verified business recipient</h2>

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
              <p className="eyebrow">Supported payment assets</p>
              <h2>Payment-oriented assets</h2>

              <ul className="notification-list">
                <li>
                  EUR digital asset concept is the internal no-extra-fee
                  prototype option
                </li>
                <li>
                  USDC and USDT may involve additional settlement costs in this
                  simulation
                </li>
                <li>
                  BTC and ETH are shown as optional volatile assets with
                  additional settlement costs
                </li>
              </ul>
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
