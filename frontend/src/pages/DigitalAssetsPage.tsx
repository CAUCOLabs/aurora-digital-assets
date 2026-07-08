import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'
import { PrivacyAmount } from '../components/PrivacyAmount'
import { useLanguage } from '../context/LanguageContext'
import { digitalAssets } from '../data/dashboardData'
import {
  getCustodyStatus,
  listDigitalAssetActivity,
  listSupportedDigitalAssets,
  listWalletBalances,
  type CustodyStatus,
  type DigitalAssetActivity,
  type SupportedDigitalAsset,
  type WalletBalance,
} from '../services/digitalAssetsApi'

const fallbackSupportedAssets: SupportedDigitalAsset[] = [
  {
    symbol: 'BTC',
    name: 'Bitcoin',
    category: 'Investment / holding asset',
    supported_actions: ['buy', 'sell', 'hold', 'external_withdrawal'],
    status: 'Active',
    risk_note:
      'Volatile cryptoasset rail example. External withdrawals require review.',
  },
  {
    symbol: 'ETH',
    name: 'Ethereum',
    category: 'Investment / holding asset',
    supported_actions: ['buy', 'sell', 'hold', 'external_withdrawal'],
    status: 'Active',
    risk_note:
      'Volatile cryptoasset rail example. External withdrawals require review.',
  },
]

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
    id: 'fallback-btc-purchase',
    title: 'BTC purchase completed',
    detail: '50,00 € from Aurora Current Account',
    status: 'Completed',
    amount: '0.00072 BTC',
    module: 'Buy / Sell',
  },
  {
    id: 'fallback-eth-purchase',
    title: 'ETH purchase completed',
    detail: '25,00 € from Aurora Current Account',
    status: 'Completed',
    amount: '0.0121 ETH',
    module: 'Buy / Sell',
  },
  {
    id: 'fallback-btc-withdrawal',
    title: 'External BTC withdrawal',
    detail: '0.001 BTC transfer request',
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
    'Strong authentication active',
    'Transaction monitoring enabled',
    'Tax reporting enabled',
    'External withdrawals require review',
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

export function DigitalAssetsPage() {
  const { t } = useLanguage()
  const labels = t.digitalAssetsPage
  const [supportedAssets, setSupportedAssets] = useState<
    SupportedDigitalAsset[]
  >([])
  const [walletBalances, setWalletBalances] = useState<WalletBalance[]>([])
  const [activity, setActivity] = useState<DigitalAssetActivity[]>([])
  const [custodyStatus, setCustodyStatus] = useState<CustodyStatus | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  const visibleSupportedAssets =
    supportedAssets.length > 0 ? supportedAssets : fallbackSupportedAssets
  const visibleWalletBalances =
    walletBalances.length > 0 ? walletBalances : fallbackWalletBalances
  const visibleActivity = activity.length > 0 ? activity : fallbackActivity
  const visibleCustodyStatus = custodyStatus ?? fallbackCustodyStatus
  const totalEstimatedValue = formatTotalEstimatedValue(visibleWalletBalances)

  useEffect(() => {
    async function fetchDigitalAssetsData() {
      setIsLoading(true)

      try {
        const [assets, balances, activityItems, custody] = await Promise.all([
          listSupportedDigitalAssets(),
          listWalletBalances(),
          listDigitalAssetActivity(),
          getCustodyStatus(),
        ])

        setSupportedAssets(assets)
        setWalletBalances(balances)
        setActivity(activityItems)
        setCustodyStatus(custody)
        setBackendError(null)
      } catch {
        setSupportedAssets(fallbackSupportedAssets)
        setWalletBalances(fallbackWalletBalances)
        setActivity(fallbackActivity)
        setCustodyStatus(fallbackCustodyStatus)
        setBackendError(
          'Backend digital asset data unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchDigitalAssetsData()
  }, [])

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{labels.eyebrow}</p>
            <h1>Aurora Digital Assets</h1>
            <p>{labels.heroSubtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Digital assets access active
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Overview</p>
                  <h2>Total digital assets value</h2>
                </div>
                <span className="module-tag">Concept module</span>
              </div>

              {isLoading && (
                <p className="panel-note">Loading digital asset data...</p>
              )}
              {backendError ? (
                <p className="panel-note">{backendError}</p>
              ) : (
                !isLoading && (
                  <p className="panel-note">
                    Digital asset data loaded from local FastAPI prototype.
                  </p>
                )
              )}

              <div className="assets-summary">
                <div>
                  <p>Current estimated value</p>
                  <strong>
                    <PrivacyAmount
                      value={totalEstimatedValue}
                      label="Current estimated value"
                    />
                  </strong>
                  <span>
                    This value is based on mock market prices and is shown for
                    prototype purposes only.
                  </span>
                </div>

                <div className="custody-card">
                  <p>Custody model</p>
                  <strong>{visibleCustodyStatus.custodyMode}</strong>
                  <span>
                    Custody and control model depend on asset rail
                    classification. Digital assets may lose value.
                  </span>
                </div>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{labels.assetRailPhase}</p>
                  <h2>{labels.assetRailGovernance}</h2>
                </div>
                <span className="module-tag">{labels.controlModelFirst}</span>
              </div>
              <p>{labels.assetRailBody}</p>

              <div className="account-list">
                {labels.assetRailRows.map((rail) => (
                  <article className="account-row" key={rail.name}>
                    <div>
                      <h3>{rail.name}</h3>
                      <p>
                        <strong>{labels.rail}</strong> {rail.rail}
                      </p>
                      <span>
                        {labels.controlModel}: {rail.controlModel}
                      </span>
                    </div>
                    <strong>{labels.governanceExample}</strong>
                  </article>
                ))}
              </div>

              <div className="action-row">
                <Link
                  className="button-link"
                  to="/bank-staff/asset-rail-governance"
                >
                  {labels.openStaffGovernanceView}
                </Link>
                <Link
                  className="button-link secondary-button"
                  to="/reports/audit-trail"
                >
                  {labels.viewAuditTrail}
                </Link>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Wallet</p>
                  <h2>Your digital assets</h2>
                </div>
                <Link className="button-link secondary-button" to="/wallet">
                  View wallet
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
                  <p className="eyebrow">Recent activity</p>
                  <h2>Digital asset transactions</h2>
                </div>
              </div>

              <div className="account-list">
                {visibleActivity.map((item) => (
                  <article className="account-row" key={item.id}>
                    <div>
                      <h3>{item.title}</h3>
                      <p>{item.module}</p>
                      {isSensitiveAmount(item.detail) ? (
                        <span>
                          <PrivacyAmount
                            value={item.detail}
                            label={`${item.title} detail`}
                          />
                        </span>
                      ) : (
                        <span>{item.detail}</span>
                      )}
                      <span>{item.status}</span>
                    </div>
                    <strong>
                      {isSensitiveAmount(item.amount) ? (
                        <PrivacyAmount
                          value={item.amount}
                          label={`${item.title} amount`}
                        />
                      ) : (
                        item.amount
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
              <h2>Manage digital assets</h2>

              <div className="action-row vertical-actions">
                <Link className="button-link" to="/buy-sell">
                  Buy digital assets
                </Link>
                <Link className="button-link" to="/buy-sell">
                  Sell digital assets
                </Link>
                <Link className="button-link" to="/withdrawals">
                  External withdrawal
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  Tax reports
                </Link>
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Risk notice</p>
              <h2>Before you continue</h2>
              <p>
                Crypto assets are volatile. External wallet transfers are
                irreversible and may require additional review before approval.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.assetRailPhase}</p>
              <h2>{labels.digitalEuroNotBtc}</h2>
              <p>{labels.digitalEuroNotBtcBody}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">{labels.cryptoassetControlPath}</p>
              <h2>{labels.cryptoassetsDifferentPath}</h2>
              <p>{labels.cryptoassetsDifferentPathBody}</p>
            </Panel>

            <Panel>
              <p className="eyebrow">Available assets</p>
              <h2>Supported assets</h2>

              <div className="check-list">
                {visibleSupportedAssets.map((asset) => (
                  <div key={asset.symbol}>
                    <span className="status-dot"></span>
                    {asset.symbol} · {asset.status}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Protection status</p>
              <h2>Protection enabled</h2>

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
          </aside>
        </section>

        <section className="disclaimer">
          {labels.safetyNotice}
        </section>
      </main>
    </div>
  )
}
