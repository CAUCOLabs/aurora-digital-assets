import { NavLink, useLocation, useNavigate } from 'react-router-dom'
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
          { label: 'New payment', to: '/payments' },
          { label: 'Approve payments', to: '/payments' },
          { label: 'International payment', to: '/payments' },
          { label: 'Recipients', to: '/payments' },
          { label: 'Payment limits', to: '/payments' },
        ],
      },
      {
        title: 'Digital asset payments',
        links: [
          { label: 'Digital asset payment', to: '/payments' },
          { label: 'Supported business recipients', to: '/payments' },
          { label: 'Payment asset settings', to: '/payments' },
          { label: 'Payment reporting', to: '/reports' },
        ],
      },
      {
        title: 'E-invoices and agreements',
        links: [
          { label: 'Create e-invoice agreement', to: '/payments' },
          { label: 'Recurring payment', to: '/payments' },
          { label: 'View and edit payment agreements', to: '/payments' },
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
          { label: 'Balances', to: '/accounts' },
          { label: 'Transactions', to: '/accounts' },
        ],
      },
      {
        title: 'Open account',
        links: [
          { label: 'Current account', to: '/accounts' },
          { label: 'Savings and deposit accounts', to: '/accounts' },
          { label: 'Account for a child', to: '/accounts' },
        ],
      },
      {
        title: 'Frequently asked',
        links: [{ label: 'Account FAQ', to: '/accounts' }],
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
          { label: 'Card overview', to: '/cards' },
          { label: 'Apply for a card', to: '/cards' },
          { label: 'Card settings', to: '/cards' },
          { label: 'Card limits', to: '/cards' },
        ],
      },
      {
        title: 'Currency',
        links: [
          { label: 'Currency accounts', to: '/cards' },
          { label: 'Exchange rates', to: '/cards' },
          { label: 'Travel money', to: '/cards' },
        ],
      },
      {
        title: 'Frequently asked',
        links: [{ label: 'Card FAQ', to: '/cards' }],
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
          { label: 'Investment overview', to: '/investments' },
          { label: 'Funds', to: '/investments' },
          { label: 'Stocks', to: '/investments' },
          { label: 'Investment accounts', to: '/investments' },
        ],
      },
      {
        title: 'Trading and custody',
        links: [
          { label: 'Trading', to: '/investments' },
          { label: 'Custody accounts', to: '/investments' },
          { label: 'Prices', to: '/investments' },
        ],
      },
      {
        title: 'News and analysis',
        links: [
          { label: 'Market news', to: '/investments' },
          { label: 'Research', to: '/investments' },
        ],
      },
      {
        title: 'Help with investing',
        links: [
          { label: 'Investment FAQ', to: '/investments' },
          { label: 'Risk information', to: '/investments' },
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
      <div className="brand">
        <div className="brand-mark">A</div>
        <div>
          <p className="brand-name">Aurora Bank</p>
          <p className="brand-subtitle">Online Banking Demo</p>
        </div>
      </div>

      <nav className="main-nav" aria-label="Main navigation">
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
                {item.label}
              </NavLink>

              {item.menu ? (
                <div className="mega-menu" aria-label={`${item.label} menu`}>
                  {item.menu.map((column) => (
                    <section className="mega-menu-column" key={column.title}>
                      <h2>{column.title}</h2>
                      <div className="mega-menu-links">
                        {column.links.map((link) => (
                          <NavLink key={`${column.title}-${link.label}`} to={link.to}>
                            {link.label}
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
          {amountsVisible ? 'Hide balances' : 'Show balances'}
        </button>
        <span>{userName}</span>
        <button
          type="button"
          className="secondary-button"
          onClick={() => void handleLogout()}
        >
          Log out
        </button>
      </div>
    </header>
  )
}
