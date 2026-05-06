import { NavLink } from 'react-router-dom'

type TopBarProps = {
  userName: string
}

const navigationItems = [
  { label: 'Home', to: '/' },
  { label: 'Payments', to: '/payments' },
  { label: 'Accounts', to: '/accounts' },
  { label: 'Cards and Currency', to: '/cards' },
  { label: 'Investments', to: '/investments' },
  { label: 'Digital Assets', to: '/digital-assets' },
  { label: 'Buy / Sell', to: '/buy-sell' },
  { label: 'Wallet', to: '/wallet' },
  { label: 'Custody', to: '/custody' },
  { label: 'Withdrawals', to: '/withdrawals' },
  { label: 'Reports', to: '/reports' },
]

export function TopBar({ userName }: TopBarProps) {
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
              props.isActive ? 'active' : undefined
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
