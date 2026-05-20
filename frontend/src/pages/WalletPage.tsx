import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { PrivacyAmount } from '../components/PrivacyAmount'
import { digitalAssets } from '../data/dashboardData'
import {
  getCustodyStatus,
  listDigitalAssetActivity,
  listWalletBalances,
  type CustodyStatus,
  type DigitalAssetActivity,
  type WalletBalance,
} from '../services/digitalAssetsApi'

const fallbackWalletBalances: WalletBalance[] = digitalAssets.map((asset) => ({
  id: `${asset.symbol.toLowerCase()}-fallback`,
  symbol: asset.symbol,
  name: asset.asset,
  balance: asset.balance,
  estimatedValue: asset.value,
  custodyMode: 'Internal custodial wallet concept',
  status: 'Active',
}))

const fallbackActivity: DigitalAssetActivity[] = [
  {
    id: 'fallback-btc-received',
    title: 'BTC purchase received',
    detail: '0.00072 BTC added to internal wallet',
    status: 'Completed',
    amount: '0.00072 BTC',
    module: 'Buy / Sell',
  },
  {
    id: 'fallback-eth-received',
    title: 'ETH purchase received',
    detail: '0.0121 ETH added to internal wallet',
    status: 'Completed',
    amount: '0.0121 ETH',
    module: 'Buy / Sell',
  },
  {
    id: 'fallback-btc-withdrawal',
    title: 'External BTC withdrawal request',
    detail: '0.001 BTC pending review',
    status: 'Pending review',
    amount: '0.001 BTC',
    module: 'Withdrawals',
  },
]

const fallbackCustodyStatus: CustodyStatus = {
  custodyMode: 'Internal custodial wallet concept',
  privateKeysExposed: false,
  assetsSeparateFromDeposits: true,
  auditTrailEnabled: true,
  externalWithdrawalsRequireReview: true,
  userMessage:
    'Digital assets are visible inside online banking, but the user does not manage private keys directly in this prototype.',
  controls: [
    'Internal custodial wallet concept',
    'User does not manage private keys',
    'Audit trail enabled',
    'Digital assets are separate from deposits',
  ],
}

function isSensitiveAmount(value: string) {
  return /\d/.test(value)
}

function formatTotalEstimatedValue(walletBalances: WalletBalance[]) {
  const total = walletBalances.reduce((sum, asset) => {
    if (!asset.estimatedValue.includes('€')) return sum

    const normalizedValue = asset.estimatedValue
      .replace('€', '')
      .replaceAll(' ', '')
      .replace(',', '.')

    const parsedValue = Number(normalizedValue)
    return Number.isFinite(parsedValue) ? sum + parsedValue : sum
  }, 0)

  return new Intl.NumberFormat('fi-FI', {
    style: 'currency',
    currency: 'EUR',
  }).format(total)
}

function mapWalletBalanceToRow(asset: WalletBalance) {
  return {
    asset: asset.name,
    symbol: asset.symbol,
    balance: asset.balance,
    value: asset.estimatedValue,
  }
}

export function WalletPage() {
  const [walletBalances, setWalletBalances] = useState<WalletBalance[]>([])
  const [activity, setActivity] = useState<DigitalAssetActivity[]>([])
  const [custodyStatus, setCustodyStatus] = useState<CustodyStatus | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  const visibleWalletBalances =
    walletBalances.length > 0 ? walletBalances : fallbackWalletBalances
  const visibleActivity = activity.length > 0 ? activity : fallbackActivity
  const visibleCustodyStatus = custodyStatus ?? fallbackCustodyStatus
  const totalEstimatedValue = formatTotalEstimatedValue(visibleWalletBalances)

  useEffect(() => {
    async function fetchWalletData() {
      setIsLoading(true)

      try {
        const [balances, activityItems, custody] = await Promise.all([
          listWalletBalances(),
          listDigitalAssetActivity(),
          getCustodyStatus(),
        ])

        setWalletBalances(balances)
        setActivity(activityItems)
        setCustodyStatus(custody)
        setBackendError(null)
      } catch {
        setWalletBalances(fallbackWalletBalances)
        setActivity(fallbackActivity)
        setCustodyStatus(fallbackCustodyStatus)
        setBackendError(
          'Backend wallet data unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchWalletData()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Wallet</p>
            <h1>Internal digital assets wallet</h1>
            <p>
              View simulated assets held through the Aurora Bank custodial
              wallet concept, including balances, custody status, and wallet
              activity.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Audit trail enabled
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Wallet summary</h2>
                </div>
                <span className="module-tag">Custodial concept</span>
              </div>

              {isLoading && <p className="panel-note">Loading wallet data...</p>}
              {backendError ? (
                <p className="panel-note">{backendError}</p>
              ) : (
                !isLoading && (
                  <p className="panel-note">
                    Wallet data loaded from local FastAPI prototype.
                  </p>
                )
              )}

              <div className="assets-summary">
                <div>
                  <p>Total wallet value</p>
                  <strong>
                    <PrivacyAmount
                      value={totalEstimatedValue}
                      label="Total wallet value"
                    />
                  </strong>
                  <span>
                    Estimated value based on mock market prices. Digital assets
                    are separate from bank deposits.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Custody model</p>
                  <strong>{visibleCustodyStatus.custodyMode}</strong>
                  <span>{visibleCustodyStatus.userMessage}</span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Balances</p>
                  <h2>Wallet assets</h2>
                </div>
                <Link className="button-link secondary-button" to="/buy-sell">
                  Buy / Sell
                </Link>
              </div>

              <div className="asset-list">
                {visibleWalletBalances.map((asset) => (
                  <DigitalAssetRow
                    key={asset.id}
                    asset={mapWalletBalanceToRow(asset)}
                  />
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Activity</p>
                  <h2>Wallet activity</h2>
                </div>
                <span className="module-tag">
                  {backendError ? 'Fallback events' : 'Backend events'}
                </span>
              </div>

              <div className="account-list">
                {visibleActivity.map((event) => (
                  <article className="account-row" key={event.id}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.module}</p>
                      {isSensitiveAmount(event.detail) ? (
                        <span>
                          <PrivacyAmount
                            value={event.detail}
                            label={`${event.title} detail`}
                          />
                        </span>
                      ) : (
                        <span>{event.detail}</span>
                      )}
                      <span>{event.status}</span>
                    </div>
                    <strong>
                      {isSensitiveAmount(event.amount) ? (
                        <PrivacyAmount
                          value={event.amount}
                          label={`${event.title} amount`}
                        />
                      ) : (
                        event.amount
                      )}
                    </strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Quick actions</p>
              <h2>Manage wallet</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/buy-sell">
                  Buy / Sell
                </Link>
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Tax reports
                </Link>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Custody</p>
              <h2>Custody status</h2>
              <div className="check-list">
                {visibleCustodyStatus.controls.map((control) => (
                  <div key={control}>
                    <span
                      className={
                        control.toLowerCase().includes('separate')
                          ? 'warning-dot'
                          : 'status-dot'
                      }
                    ></span>
                    {control}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Important</p>
              <h2>No private key access</h2>
              <p>{visibleCustodyStatus.userMessage}</p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page simulates an internal
          custodial wallet and does not store real crypto assets, private keys,
          or customer data.
        </section>
      </main>
    </div>
  )
}
