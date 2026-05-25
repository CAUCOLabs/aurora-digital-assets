import { useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { PrivacyAmount } from '../components/PrivacyAmount'
import {
  evaluateBuySell,
  type BuySellAsset,
  type BuySellEvaluateResponse,
  type BuySellSide,
} from '../services/buySellApi'

type TradeStatus = 'draft' | 'ready' | 'evaluated'

const marketPrices: Record<
  BuySellAsset,
  {
    name: string
    priceEur: number
    balance: number
  }
> = {
  BTC: {
    name: 'Bitcoin',
    priceEur: 69500,
    balance: 0.01245,
  },
  ETH: {
    name: 'Ethereum',
    priceEur: 2066.88,
    balance: 0.1842,
  },
}

const feeRate = 0.01
const spreadRate = 0.005

function formatEur(value: number) {
  return new Intl.NumberFormat('fi-FI', {
    style: 'currency',
    currency: 'EUR',
  }).format(value)
}

function formatCrypto(value: number, asset: string) {
  return `${value.toFixed(asset === 'BTC' ? 8 : 6)} ${asset}`
}

export function BuySellPage() {
  const [side, setSide] = useState<BuySellSide>('buy')
  const [asset, setAsset] = useState<BuySellAsset>('BTC')
  const [amount, setAmount] = useState('')
  const [status, setStatus] = useState<TradeStatus>('draft')
  const [backendEvaluation, setBackendEvaluation] =
    useState<BuySellEvaluateResponse | null>(null)
  const [backendError, setBackendError] = useState<string | null>(null)
  const [isEvaluating, setIsEvaluating] = useState(false)

  const selectedMarket = marketPrices[asset]
  const numericAmount = Number(amount.replace(',', '.'))
  const isValidAmount = Number.isFinite(numericAmount) && numericAmount > 0

  const localEstimate = useMemo(() => {
    if (!isValidAmount) {
      return {
        grossEur: 0,
        feeEur: 0,
        spreadEur: 0,
        netEur: 0,
        cryptoAmount: 0,
        marketPriceEur: selectedMarket.priceEur,
      }
    }

    if (side === 'buy') {
      const grossEur = numericAmount
      const feeEur = grossEur * feeRate
      const spreadEur = grossEur * spreadRate
      const netEur = grossEur - feeEur - spreadEur
      const cryptoAmount = netEur / selectedMarket.priceEur

      return {
        grossEur,
        feeEur,
        spreadEur,
        netEur,
        cryptoAmount,
        marketPriceEur: selectedMarket.priceEur,
      }
    }

    const cryptoAmount = numericAmount
    const grossEur = cryptoAmount * selectedMarket.priceEur
    const feeEur = grossEur * feeRate
    const spreadEur = grossEur * spreadRate
    const netEur = grossEur - feeEur - spreadEur

    return {
      grossEur,
      feeEur,
      spreadEur,
      netEur,
      cryptoAmount,
      marketPriceEur: selectedMarket.priceEur,
    }
  }, [isValidAmount, numericAmount, selectedMarket.priceEur, side])

  const displayedEstimate = backendEvaluation?.estimate
    ? {
        grossEur: backendEvaluation.estimate.gross_eur,
        feeEur: backendEvaluation.estimate.fee_eur,
        spreadEur: backendEvaluation.estimate.spread_eur,
        netEur: backendEvaluation.estimate.net_eur,
        cryptoAmount: backendEvaluation.estimate.estimated_asset_amount,
        marketPriceEur: backendEvaluation.estimate.market_price_eur,
      }
    : localEstimate

  const visibleStatus: TradeStatus =
    status === 'evaluated' ? 'evaluated' : isValidAmount ? 'ready' : 'draft'

  const backendAuditEvents = backendEvaluation
    ? [
        {
          title: 'Buy/sell evaluation submitted',
          detail: `${side === 'buy' ? 'Buy' : 'Sell'} ${asset} request was submitted to the local FastAPI prototype.`,
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

  const localAuditEvents = [
    {
      title: 'Trade form opened',
      detail: 'User entered the simulated buy/sell flow.',
      status: 'Recorded',
    },
    {
      title: 'Local estimate prepared',
      detail:
        side === 'buy'
          ? `${formatEur(displayedEstimate.grossEur)} estimated into ${formatCrypto(
              displayedEstimate.cryptoAmount,
              asset,
            )}.`
          : `${formatCrypto(displayedEstimate.cryptoAmount, asset)} estimated into ${formatEur(
              displayedEstimate.netEur,
            )}.`,
      status: isValidAmount ? 'Ready' : 'Draft',
    },
  ]

  const visibleAuditEvents = backendAuditEvents ?? localAuditEvents

  function resetEvaluation() {
    setStatus('draft')
    setBackendEvaluation(null)
    setBackendError(null)
  }

  async function handleSubmit() {
    if (!isValidAmount) return

    setIsEvaluating(true)
    setBackendError(null)

    try {
      const evaluation = await evaluateBuySell({
        side,
        asset,
        amount: numericAmount,
        source_account_id: 'aurora-current',
      })

      setBackendEvaluation(evaluation)
      setStatus('evaluated')
    } catch {
      setBackendEvaluation(null)
      setBackendError(
        'Backend buy/sell evaluation unavailable. Showing local prototype estimate.',
      )
      setStatus('evaluated')
    } finally {
      setIsEvaluating(false)
    }
  }

  function handleReset() {
    setSide('buy')
    setAsset('BTC')
    setAmount('')
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
            <p className="eyebrow">Buy / Sell</p>
            <h1>Digital assets transaction</h1>
            <p>
              Evaluate a responsible BTC or ETH buy/sell request with transparent
              price, fee, spread, and risk information.
            </p>
          </div>

          <div className="security-badge">
            <span
              className={
                visibleStatus === 'evaluated' ? 'status-dot' : 'warning-dot'
              }
            ></span>
            {visibleStatus === 'evaluated'
              ? 'Evaluated'
              : visibleStatus === 'ready'
                ? 'Ready'
                : 'Draft'}
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Transaction</p>
                  <h2>Order details</h2>
                </div>
                <span className="module-tag">
                  {backendEvaluation ? 'Backend evaluation' : 'Prototype estimate'}
                </span>
              </div>

              {backendError && <p className="panel-note">{backendError}</p>}
              {backendEvaluation && (
                <p className="panel-note">
                  Buy/sell evaluation loaded from local FastAPI prototype.
                </p>
              )}

              <div className="trade-toggle" aria-label="Trade side">
                <button
                  type="button"
                  className={side === 'buy' ? 'toggle-active' : 'secondary-button'}
                  onClick={() => {
                    setSide('buy')
                    setAmount('')
                    resetEvaluation()
                  }}
                >
                  Buy
                </button>
                <button
                  type="button"
                  className={side === 'sell' ? 'toggle-active' : 'secondary-button'}
                  onClick={() => {
                    setSide('sell')
                    setAmount('')
                    resetEvaluation()
                  }}
                >
                  Sell
                </button>
              </div>

              <div className="form-grid">
                <label>
                  Asset
                  <select
                    value={asset}
                    onChange={(event) => {
                      setAsset(event.target.value as BuySellAsset)
                      resetEvaluation()
                    }}
                  >
                    <option value="BTC">BTC — Bitcoin</option>
                    <option value="ETH">ETH — Ethereum</option>
                  </select>
                </label>

                <label>
                  {side === 'buy' ? 'Amount in EUR' : `Amount in ${asset}`}
                  <input
                    value={amount}
                    onChange={(event) => {
                      setAmount(event.target.value)
                      resetEvaluation()
                    }}
                    placeholder={
                      side === 'buy'
                        ? '50.00'
                        : asset === 'BTC'
                          ? '0.001'
                          : '0.05'
                    }
                    inputMode="decimal"
                  />
                  {!isValidAmount && amount.length > 0 && (
                    <span className="field-warning">
                      Amount must be greater than zero.
                    </span>
                  )}
                </label>
              </div>

              <div className="withdrawal-preview">
                <div>
                  <p>Market price</p>
                  <strong>
                    <PrivacyAmount
                      value={formatEur(displayedEstimate.marketPriceEur)}
                      label={`${asset} market price`}
                    />
                  </strong>
                </div>
                <div>
                  <p>Estimated fee</p>
                  <strong>
                    <PrivacyAmount
                      value={formatEur(displayedEstimate.feeEur)}
                      label="Estimated fee"
                    />
                  </strong>
                </div>
                <div>
                  <p>Estimated spread</p>
                  <strong>
                    <PrivacyAmount
                      value={formatEur(displayedEstimate.spreadEur)}
                      label="Estimated spread"
                    />
                  </strong>
                </div>
              </div>

              <div className="assets-summary trade-summary">
                <div>
                  <p>
                    {side === 'buy'
                      ? 'Estimated crypto received'
                      : 'Estimated EUR received'}
                  </p>
                  <strong>
                    <PrivacyAmount
                      value={
                        side === 'buy'
                          ? formatCrypto(displayedEstimate.cryptoAmount, asset)
                          : formatEur(displayedEstimate.netEur)
                      }
                      label={
                        side === 'buy'
                          ? 'Estimated crypto received'
                          : 'Estimated EUR received'
                      }
                    />
                  </strong>
                  <span>
                    Estimate only. No real market execution, settlement, or
                    custody movement occurs in this prototype.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Available balance</p>
                  <strong>
                    <PrivacyAmount
                      value={
                        side === 'buy'
                          ? '2 450,10 €'
                          : formatCrypto(selectedMarket.balance, asset)
                      }
                      label="Available balance"
                    />
                  </strong>
                  <span>
                    Simulated balance shown for prototype purposes only.
                  </span>
                </div>
              </div>

              <div className="action-row">
                <button
                  type="button"
                  onClick={handleSubmit}
                  disabled={!isValidAmount || isEvaluating}
                >
                  {isEvaluating
                    ? 'Evaluating...'
                    : `Evaluate simulated ${side}`}
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
                  <h2>Transaction evidence timeline</h2>
                </div>
                <span className="module-tag">
                  {backendEvaluation ? 'Backend audit concept' : 'Local draft'}
                </span>
              </div>

              <div className="account-list">
                {visibleAuditEvents.map((event) => (
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
            <Panel className="risk-panel">
              <p className="eyebrow">Risk warning</p>
              <h2>Digital assets are volatile</h2>
              <p>
                BTC and ETH prices can move quickly. This prototype shows a
                responsible bank-style evaluation flow, not investment advice.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Evaluation result</p>
              <h2>
                {backendEvaluation
                  ? backendEvaluation.decision.replaceAll('_', ' ')
                  : visibleStatus === 'ready'
                    ? 'Ready for evaluation'
                    : 'Draft'}
              </h2>

              {backendEvaluation ? (
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
              ) : (
                <p>
                  Enter an amount and evaluate the request. The backend will
                  return a simulated decision, risk level, estimate, and review
                  requirement.
                </p>
              )}
            </Panel>

            <Panel>
              <p className="eyebrow">Transparency</p>
              <h2>Before evaluation</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Estimated price visible
                </div>
                <div>
                  <span className="status-dot"></span>
                  Fee and spread visible
                </div>
                <div>
                  <span className="status-dot"></span>
                  Custody notice included
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Tax consequences may apply
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Product boundary</p>
              <h2>Evaluation only</h2>
              <p>
                This flow does not execute trades, connect to an exchange, move
                real funds, or transfer crypto assets. It only evaluates a
                simulated request using the local backend prototype.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page evaluates a simulated buy/sell
          request and does not provide financial advice or execute real
          transactions.
        </section>
      </main>
    </div>
  )
}