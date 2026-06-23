import { NavLink, useLocation, useNavigate } from 'react-router-dom'
import { LanguageToggle } from './LanguageToggle'
import { useLanguage } from '../context/LanguageContext'
import { usePrivacyMode } from '../context/PrivacyModeContext'
import { logoutFromBank } from '../services/authApi'

type TopBarProps = {
  userName: string
}

type NavigationLink = {
  label: string
  to: string
}

type MegaMenuColumn = {
  title: string
  links: NavigationLink[]
}

type NavigationItem = NavigationLink & {
  activePaths?: string[]
  menu?: MegaMenuColumn[]
}

const navigationItems: NavigationItem[] = [
  { label: 'Home', to: '/dashboard' },
  {
    label: 'Payments',
    to: '/payments',
    menu: [
      {
        title: 'Payments',
        links: [
          { label: 'New payment', to: '/payments/new' },
          { label: 'Approve payments', to: '/payments/approve' },
          { label: 'International payment', to: '/payments/international' },
          { label: 'Recipients', to: '/payments/recipients' },
          { label: 'Payment limits', to: '/payments/limits' },
        ],
      },
      {
        title: 'Digital asset payments',
        links: [
          { label: 'Digital asset payment', to: '/payments/digital-asset-payment' },
          {
            label: 'Supported business recipients',
            to: '/payments/supported-business-recipients',
          },
          { label: 'Payment asset settings', to: '/payments/asset-settings' },
          { label: 'Payment reporting', to: '/reports' },
        ],
      },
      {
        title: 'E-invoices and agreements',
        links: [
          {
            label: 'Create e-invoice agreement',
            to: '/payments/e-invoice-agreement',
          },
          { label: 'Recurring payment', to: '/payments/recurring' },
          {
            label: 'View and edit payment agreements',
            to: '/payments/payment-agreements',
          },
        ],
      },
      {
        title: 'See also',
        links: [
          { label: 'E-invoice archive', to: '/reports' },
          { label: 'Message and notification settings', to: '/online-services' },
        ],
      },
    ],
  },
  {
    label: 'Accounts',
    to: '/accounts',
    menu: [
      {
        title: 'Balances and transactions',
        links: [
          { label: 'Balances', to: '/accounts/balances' },
          { label: 'Transactions', to: '/accounts/transactions' },
        ],
      },
      {
        title: 'Open account',
        links: [
          { label: 'Current account', to: '/accounts/current-account' },
          {
            label: 'Savings and deposit accounts',
            to: '/accounts/savings-deposits',
          },
          { label: 'Account for a child', to: '/accounts/child-account' },
        ],
      },
      {
        title: 'Frequently asked',
        links: [{ label: 'Account FAQ', to: '/accounts/faq' }],
      },
      {
        title: 'See also',
        links: [
          { label: 'Account statements and bank mail', to: '/reports' },
          { label: 'Message and notification settings', to: '/online-services' },
        ],
      },
    ],
  },
  {
    label: 'Cards and Currency',
    to: '/cards',
    menu: [
      {
        title: 'Cards',
        links: [
          { label: 'Card overview', to: '/cards/overview' },
          { label: 'Apply for a card', to: '/cards/apply' },
          { label: 'Card settings', to: '/cards/settings' },
          { label: 'Card limits', to: '/cards/limits' },
        ],
      },
      {
        title: 'Currency',
        links: [
          { label: 'Currency accounts', to: '/cards/currency-accounts' },
          { label: 'Exchange rates', to: '/cards/exchange-rates' },
          { label: 'Travel money', to: '/cards/travel-money' },
        ],
      },
      {
        title: 'Frequently asked',
        links: [{ label: 'Card FAQ', to: '/cards/faq' }],
      },
      {
        title: 'See also',
        links: [
          { label: 'Card statements', to: '/reports' },
          { label: 'Security settings', to: '/online-services' },
        ],
      },
    ],
  },
  { label: 'Loans', to: '/loans' },
  {
    label: 'Investments',
    to: '/investments',
    menu: [
      {
        title: 'Investments',
        links: [
          { label: 'Investment overview', to: '/investments/overview' },
          { label: 'Funds', to: '/investments/funds' },
          { label: 'Stocks', to: '/investments/stocks' },
          { label: 'Investment accounts', to: '/investments/accounts' },
        ],
      },
      {
        title: 'Trading and custody',
        links: [
          { label: 'Trading', to: '/investments/trading' },
          { label: 'Custody accounts', to: '/investments/custody-accounts' },
          { label: 'Prices', to: '/investments/prices' },
        ],
      },
      {
        title: 'News and analysis',
        links: [
          { label: 'Market news', to: '/investments/market-news' },
          { label: 'Research', to: '/investments/research' },
        ],
      },
      {
        title: 'Help with investing',
        links: [
          { label: 'Investment FAQ', to: '/investments/faq' },
          { label: 'Risk information', to: '/investments/risk-information' },
        ],
      },
    ],
  },
  { label: 'Insurance', to: '/insurance' },
  {
    label: 'Digital Assets',
    to: '/digital-assets',
    activePaths: ['/buy-sell', '/wallet', '/custody', '/withdrawals'],
    menu: [
      {
        title: 'Balances and activity',
        links: [
          { label: 'Overview', to: '/digital-assets' },
          { label: 'Wallet balances', to: '/wallet' },
          { label: 'Transaction history', to: '/reports' },
        ],
      },
      {
        title: 'Manage digital assets',
        links: [
          { label: 'Buy / Sell', to: '/buy-sell' },
          { label: 'External withdrawals', to: '/withdrawals' },
          { label: 'Custody model', to: '/custody' },
        ],
      },
      {
        title: 'Reporting',
        links: [
          { label: 'Tax reports', to: '/reports' },
          { label: 'Export documents', to: '/reports' },
          { label: 'Audit trail', to: '/reports' },
        ],
      },
      {
        title: 'Frequently asked',
        links: [
          { label: 'What is custody?', to: '/custody' },
          { label: 'Are digital assets deposits?', to: '/custody' },
          { label: 'What happens during withdrawal?', to: '/withdrawals' },
        ],
      },
    ],
  },
  { label: 'Documents', to: '/reports' },
  {
    label: 'Online Services',
    to: '/online-services',
    menu: [
      {
        title: 'Online banking',
        links: [
          { label: 'Online banking settings', to: '/online-services' },
          { label: 'Mobile banking', to: '/online-services' },
          { label: 'Strong authentication', to: '/online-services' },
        ],
      },
      {
        title: 'Messages',
        links: [
          { label: 'Message settings', to: '/online-services' },
          { label: 'Email notifications', to: '/online-services' },
          { label: 'SMS notifications', to: '/online-services' },
        ],
      },
      {
        title: 'Security',
        links: [
          { label: 'Login security', to: '/online-services' },
          { label: 'Device management', to: '/online-services' },
          { label: 'Security alerts', to: '/online-services' },
        ],
      },
      {
        title: 'Help',
        links: [
          { label: 'Online services FAQ', to: '/online-services' },
          { label: 'Contact support', to: '/online-services' },
        ],
      },
    ],
  },
]

export function TopBar({ userName }: TopBarProps) {
  const location = useLocation()
  const navigate = useNavigate()
  const { amountsVisible, toggleAmountsVisible } = usePrivacyMode()
  const { t } = useLanguage()
  const phrases = t.phrases as Record<string, string>
  const phrase = (value: string) => phrases[value] ?? value

  const navigationLabels: Record<string, string> = {
    Home: t.navigation.home,
    Payments: t.navigation.payments,
    Accounts: t.navigation.accounts,
    'Cards and Currency': t.navigation.cardsAndCurrency,
    Loans: t.navigation.loans,
    Investments: t.navigation.investments,
    Insurance: t.navigation.insurance,
    'Digital Assets': t.navigation.digitalAssets,
    Documents: t.navigation.documents,
    'Online Services': t.navigation.onlineServices,
  }

  async function handleLogout() {
    const sessionId = localStorage.getItem('aurora_bank_session_id')

    try {
      if (sessionId) {
        await logoutFromBank(sessionId)
      }
    } finally {
      localStorage.removeItem('aurora_bank_session_id')
      navigate('/bank-login')
    }
  }

  return (
    <header className="top-bar">
      <NavLink
        className="brand"
        to="/dashboard"
        aria-label={phrase('Go to online banking dashboard')}
      >
        <div className="brand-mark">A</div>
        <div>
          <p className="brand-name">Aurora Bank</p>
          <p className="brand-subtitle">{t.navigation.onlineBankingDemo}</p>
        </div>
      </NavLink>

      <nav className="main-nav" aria-label={t.navigation.mainNavigation}>
        {navigationItems.map((item) => {
          const hasMegaMenu = Boolean(item.menu)

          return (
            <div
              className={hasMegaMenu ? 'nav-item has-mega-menu' : 'nav-item'}
              key={item.label}
            >
              <NavLink
                to={item.to}
                aria-haspopup={hasMegaMenu ? 'true' : undefined}
                className={(props: { isActive: boolean }) =>
                  props.isActive || item.activePaths?.includes(location.pathname)
                    ? 'main-nav-link active'
                    : 'main-nav-link'
                }
              >
                {navigationLabels[item.label] ?? item.label}
              </NavLink>

              {item.menu ? (
                <div className="mega-menu" aria-label={`${phrase(item.label)} menu`}>
                  {item.menu.map((column) => (
                    <section className="mega-menu-column" key={column.title}>
                      <h2>{phrase(column.title)}</h2>
                      <div className="mega-menu-links">
                        {column.links.map((link) => (
                          <NavLink key={`${column.title}-${link.label}`} to={link.to}>
                            {phrase(link.label)}
                          </NavLink>
                        ))}
                      </div>
                    </section>
                  ))}
                </div>
              ) : null}
            </div>
          )
        })}
      </nav>

      <div className="user-area">
        <button
          type="button"
          className="privacy-toggle"
          aria-pressed={amountsVisible}
          onClick={toggleAmountsVisible}
        >
          {amountsVisible
            ? t.navigation.hideBalances
            : t.navigation.showBalances}
        </button>
        <LanguageToggle />
        <span>{userName}</span>
        <button
          type="button"
          className="secondary-button"
          onClick={() => void handleLogout()}
        >
          {t.navigation.logOut}
        </button>
      </div>
    </header>
  )
}
