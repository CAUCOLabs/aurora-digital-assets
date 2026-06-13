import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { AccountRow } from '../components/AccountRow'
import { DigitalAssetRow } from '../components/DigitalAssetRow'
import { PrivacyAmount } from '../components/PrivacyAmount'
import { useLanguage } from '../context/LanguageContext'
import {
  accounts as fallbackAccounts,
  digitalAssets as fallbackDigitalAssets,
  notifications,
} from '../data/dashboardData'
import { listAccounts, type BankAccount } from '../services/accountsApi'
import {
  getCustodyStatus,
  listWalletBalances,
  type CustodyStatus,
  type WalletBalance,
} from '../services/digitalAssetsApi'

function formatEur(value: number) {
  return new Intl.NumberFormat('fi-FI', {
    style: 'currency',
    currency: 'EUR',
  }).format(value)
}

function parseEuroAmount(value: string) {
  const normalized = value
    .replace(/[^\d,.-]/g, '')
    .replace(/\s/g, '')
    .replace(',', '.')

  const parsed = Number(normalized)
  return Number.isFinite(parsed) ? parsed : 0
}

function isMoneyValue(value: string) {
  return /\d/.test(value) && value.includes('€')
}

function toDashboardAccount(account: BankAccount) {
  return {
    name: account.name,
    type: `${account.type} · ${account.status}`,
    balance: account.availableBalance,
    maskedIban: account.iban,
  }
}

function toDashboardAsset(asset: WalletBalance) {
  return {
    asset: asset.name,
    symbol: asset.symbol,
    balance: asset.balance,
    value: asset.estimatedValue,
  }
}

export function DashboardPage() {
  const { t } = useLanguage()
  const [backendAccounts, setBackendAccounts] = useState<BankAccount[]>([])
  const [walletBalances, setWalletBalances] = useState<WalletBalance[]>([])
  const [custodyStatus, setCustodyStatus] = useState<CustodyStatus | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [backendError, setBackendError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchDashboardData() {
      setIsLoading(true)

      try {
        const [accountsResponse, walletResponse, custodyResponse] =
          await Promise.all([
            listAccounts(),
            listWalletBalances(),
            getCustodyStatus(),
          ])

        setBackendAccounts(accountsResponse)
        setWalletBalances(walletResponse)
        setCustodyStatus(custodyResponse)
        setBackendError(null)
      } catch {
        setBackendAccounts([])
        setWalletBalances([])
        setCustodyStatus(null)
        setBackendError(
          'Backend dashboard data unavailable. Showing local prototype fallback.',
        )
      } finally {
        setIsLoading(false)
      }
    }

    void fetchDashboardData()
  }, [])

  const visibleAccounts =
    backendAccounts.length > 0
      ? backendAccounts.map(toDashboardAccount)
      : fallbackAccounts

  const visibleDigitalAssets =
    walletBalances.length > 0
      ? walletBalances.map(toDashboardAsset)
      : fallbackDigitalAssets

  const totalDigitalAssetsValue = useMemo(() => {
    if (walletBalances.length === 0) return '1 245,80 €'

    const total = walletBalances
      .filter((asset) => isMoneyValue(asset.estimatedValue))
      .reduce((sum, asset) => sum + parseEuroAmount(asset.estimatedValue), 0)

    return formatEur(total)
  }, [walletBalances])

  const custodyMode =
    custodyStatus?.custodyMode ?? 'Internal custodial wallet concept'

  const custodySummary = custodyStatus
    ? [
        custodyStatus.auditTrailEnabled ? 'Audit trail enabled' : null,
        custodyStatus.externalWithdrawalsRequireReview
          ? 'External withdrawals require review'
          : null,
      ]
        .filter(Boolean)
        .join(' · ')
    : 'Digital assets access active · Audit trail enabled'

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">{t.dashboard.welcomeBack}</p>
            <h1>{t.dashboard.financialOverview}</h1>
            <p>{t.dashboard.subtitle}</p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.dashboard.strongAuthActive}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.dashboard.accounts}</p>
                  <h2>{t.dashboard.yourAccounts}</h2>
                </div>
                <Link className="button-link secondary-button" to="/payments">
                  {t.dashboard.newPayment}
                </Link>
              </div>

              {isLoading && (
                <p className="panel-note">{t.dashboard.loadingDashboard}</p>
              )}
              {backendError && <p className="panel-note">{backendError}</p>}
              {!backendError && !isLoading && (
                <p className="panel-note">
                  {t.dashboard.dashboardLoaded}
                </p>
              )}

              <div className="account-list">
                {visibleAccounts.map((account) => (
                  <AccountRow key={account.name} account={account} />
                ))}
              </div>
            </Panel>

            <Panel id="digital-assets">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.dashboard.digitalAssets}</p>
                  <h2>{t.dashboard.wallet}</h2>
                </div>
                <span className="module-tag">
                  {walletBalances.length > 0
                    ? t.dashboard.backendModule
                    : t.dashboard.conceptModule}
                </span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>{t.dashboard.totalDigitalAssetsValue}</p>
                  <strong>
                    <PrivacyAmount
                      value={totalDigitalAssetsValue}
                      label={t.dashboard.totalDigitalAssetsValue}
                    />
                  </strong>
                  <span>{t.dashboard.volatilityNotice}</span>
                </div>

                <div className="custody-card">
                  <p>{t.dashboard.custodyStatus}</p>
                  <strong>{custodyMode}</strong>
                  <span>{custodySummary}</span>
                </div>
              </div>

              <div className="asset-list">
                {visibleDigitalAssets.map((asset) => (
                  <DigitalAssetRow key={asset.symbol} asset={asset} />
                ))}
              </div>

              <div className="action-row">
                <Link className="button-link" to="/buy-sell">
                  {t.dashboard.buy}
                </Link>
                <Link className="button-link" to="/buy-sell">
                  {t.dashboard.sell}
                </Link>
                <Link className="button-link" to="/withdrawals">
                  {t.dashboard.withdraw}
                </Link>
                <Link className="button-link secondary-button" to="/reports">
                  {t.common.reports}
                </Link>
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">{t.dashboard.notifications}</p>
              <h2>{t.dashboard.importantMessages}</h2>

              <ul className="notification-list">
                {notifications.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">{t.dashboard.userProtection}</p>
              <h2>{t.dashboard.riskNotice}</h2>
              <p>{t.dashboard.riskNoticeCopy}</p>
              <Link className="button-link secondary-button" to="/digital-assets">
                {t.dashboard.readRiskInformation}
              </Link>
            </Panel>

            <Panel>
              <p className="eyebrow">{t.dashboard.protectionStatus}</p>
              <h2>{t.dashboard.protection}</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Strong authentication active
                </div>
                <div>
                  <span className="status-dot"></span>
                  Transaction monitoring enabled
                </div>
                <div>
                  <span
                    className={
                      custodyStatus?.auditTrailEnabled
                        ? 'status-dot'
                        : 'warning-dot'
                    }
                  ></span>
                  Audit trail{' '}
                  {custodyStatus?.auditTrailEnabled ? 'enabled' : 'concept'}
                </div>
                <div>
                  <span
                    className={
                      custodyStatus?.externalWithdrawalsRequireReview
                        ? 'warning-dot'
                        : 'status-dot'
                    }
                  ></span>
                  External withdrawals require review
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Digital assets are separate from deposits
                </div>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. Not affiliated with any bank. No real
          bank APIs, no real custody, no private keys, and no real customer data.
        </section>
      </main>
    </div>
  )
}
