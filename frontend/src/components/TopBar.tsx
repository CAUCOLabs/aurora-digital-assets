type TopBarProps = {
  userName: string
}

const navigationItems = [
  { label: 'Home', href: '#home', active: true },
  { label: 'Payments', href: '#payments' },
  { label: 'Accounts', href: '#accounts' },
  { label: 'Cards and Currency', href: '#cards' },
  { label: 'Investments', href: '#investments' },
  { label: 'Digital Assets', href: '#digital-assets' },
  { label: 'Reports', href: '#reports' },
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
          <a
            key={item.label}
            className={item.active ? 'active' : undefined}
            href={item.href}
          >
            {item.label}
          </a>
        ))}
      </nav>

      <div className="user-area">
        <span>{userName}</span>
        <button type="button">Log out</button>
      </div>
    </header>
  )
}