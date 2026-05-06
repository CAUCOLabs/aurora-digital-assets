import { NavLink, useLocation } from 'react-router-dom'

type TopBarProps = {
  userName: string
}

const navigationItems = [
  { label: 'Home', to: '/' },
  { label: 'Payments', to: '/payments' },
  { label: 'Accounts', to: '/accounts' },
  { label: 'Cards and Currency', to: '/cards' },
  { label: 'Loans', to: '/loans' },
  { label: 'Investments', to: '/investments' },
  {
    label: 'Digital Assets',
    to: '/digital-assets',
    activePaths: ['/buy-sell', '/wallet', '/custody', '/withdrawals'],
  },
  { label: 'Documents', to: '/reports' },
  { label: 'Online Services', to: '/online-services' },
]

export function TopBar({ userName }: TopBarProps) {
  const location = useLocation()

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
        {navigationItems.map((item) => (
          <NavLink
            key={item.label}
            to={item.to}
            className={(props: { isActive: boolean }) =>
              props.isActive || item.activePaths?.includes(location.pathname)
                ? 'active'
                : undefined
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>

      <div className="user-area">
        <span>{userName}</span>
        <button type="button">Log out</button>
      </div>
    </header>
  )
}
