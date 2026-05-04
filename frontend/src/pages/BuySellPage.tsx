import { useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

type TradeSide = 'buy' | 'sell'
type TradeStatus = 'draft' | 'completed'

const marketPrices = {
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
  const [side, setSide] = useState<TradeSide>('buy')
  const [asset, setAsset] = useState<'BTC' | 'ETH'>('BTC')
  const [amount, setAmount] = useState('')
  const [status, setStatus] = useState<TradeStatus>('draft')

  const selectedMarket = marketPrices[asset]
  const numericAmount = Number(amount)
  const isValidAmount = Number.isFinite(numericAmount) && numericAmount > 0

  const estimate = useMemo(() => {
    if (!isValidAmount) {
      return {
        grossEur: 0,
        feeEur: 0,
        spreadEur: 0,
        netEur: 0,
        cryptoAmount: 0,
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
    }
  }, [asset, isValidAmount, numericAmount, selectedMarket.priceEur, side])

  const auditEvents = [
    {
      title: 'Trade form opened',
      detail: 'User entered the simulated buy/sell flow.',
      status: 'Recorded',
    },
    ...(status === 'completed'
      ? [
          {
            title: `${side === 'buy' ? 'Purchase' : 'Sale'} completed`,
            detail:
              side === 'buy'
                ? `${formatEur(estimate.grossEur)} converted into ${formatCrypto(
                    estimate.cryptoAmount,
                    asset,
                  )}.`
                : `${formatCrypto(estimate.cryptoAmount, asset)} converted into ${formatEur(
                    estimate.netEur,
                  )}.`,
            status: 'Completed simulation',
          },
        ]
      : []),
  ]

  function handleSubmit() {
    if (!isValidAmount) return
    setStatus('completed')
  }

  function handleReset() {
    setSide('buy')
    setAsset('BTC')
    setAmount('')
    setStatus('draft')
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
              Simulate a responsible BTC or ETH buy/sell flow with transparent
              price, fee, spread, and risk information.
            </p>
          </div>

          <div className="security-badge">
            <span className={status === 'completed' ? 'status-dot' : 'warning-dot'}></span>
            {status === 'completed' ? 'Completed simulation' : 'Draft'}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Transaction</p>
                  <h2>Order details</h2>
                </div>
                <span className="module-tag">Simulation</span>
              </div>

              <div className="trade-toggle" aria-label="Trade side">
                <button
                  type="button"
                  className={side === 'buy' ? 'toggle-active' : 'secondary-button'}
                  onClick={() => {
                    setSide('buy')
                    setStatus('draft')
                    setAmount('')
                  }}
                >
                  Buy
                </button>
                <button
                  type="button"
                  className={side === 'sell' ? 'toggle-active' : 'secondary-button'}
                  onClick={() => {
                    setSide('sell')
                    setStatus('draft')
                    setAmount('')
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
                      setAsset(event.target.value as 'BTC' | 'ETH')
                      setStatus('draft')
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
                      setStatus('draft')
                    }}
                    placeholder={side === 'buy' ? '50.00' : asset === 'BTC' ? '0.001' : '0.05'}
                    inputMode="decimal"
                  />
                </label>
              </div>

              <div className="withdrawal-preview">
                <div>
                  <p>Market price</p>
                  <strong>{formatEur(selectedMarket.priceEur)}</strong>
                </div>
                <div>
                  <p>Estimated fee</p>
                  <strong>{formatEur(estimate.feeEur)}</strong>
                </div>
                <div>
                  <p>Estimated spread</p>
                  <strong>{formatEur(estimate.spreadEur)}</strong>
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
                    {side === 'buy'
                      ? formatCrypto(estimate.cryptoAmount, asset)
                      : formatEur(estimate.netEur)}
                  </strong>
                  <span>
                    Estimate only. Final settlement would depend on execution
                    price and bank/custody rules.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Available balance</p>
                  <strong>
                    {side === 'buy'
                      ? '2 450,10 €'
                      : formatCrypto(selectedMarket.balance, asset)}
                  </strong>
                  <span>
                    Simulated balance shown for prototype purposes only.
                  </span>
                </div>
              </div>

              <div className="action-row">
                <button type="button" onClick={handleSubmit} disabled={!isValidAmount}>
                  Confirm simulated {side}
                </button>
                <button className="secondary-button" type="button" onClick={handleReset}>
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
            <Panel className="risk-panel">
              <p className="eyebrow">Risk warning</p>
              <h2>Digital assets are volatile</h2>
              <p>
                BTC and ETH prices can move quickly. This prototype shows a
                responsible bank-style confirmation flow, not investment advice.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Transparency</p>
              <h2>Before confirmation</h2>

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
              <h2>Simulation only</h2>
              <p>
                This flow does not execute trades, connect to an exchange, or
                move real funds. All values are mock values.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page simulates a buy/sell flow and
          does not provide financial advice or execute real transactions.
        </section>
      </main>
    </div>
  )
}