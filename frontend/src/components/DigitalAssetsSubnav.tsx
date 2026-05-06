import { NavLink } from 'react-router-dom'

const digitalAssetsItems = [
  { label: 'Overview', to: '/digital-assets' },
  { label: 'Buy / Sell', to: '/buy-sell' },
  { label: 'Wallet', to: '/wallet' },
  { label: 'Custody', to: '/custody' },
  { label: 'Withdrawals', to: '/withdrawals' },
  { label: 'Reports', to: '/reports' },
]

export function DigitalAssetsSubnav() {
  return (
    <nav className="module-subnav" aria-label="Digital Assets navigation">
      {digitalAssetsItems.map((item) => (
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
  )
}
