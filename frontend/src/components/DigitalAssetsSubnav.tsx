import { NavLink } from 'react-router-dom'
import { useLanguage } from '../context/LanguageContext'

const digitalAssetsItems = [
  { label: 'Overview', to: '/digital-assets' },
  { label: 'Buy / Sell', to: '/buy-sell' },
  { label: 'Wallet', to: '/wallet' },
  { label: 'Custody', to: '/custody' },
  { label: 'Withdrawals', to: '/withdrawals' },
  { label: 'Reports', to: '/reports' },
]

export function DigitalAssetsSubnav() {
  const { t } = useLanguage()
  const phrases = t.phrases as Record<string, string>
  const phrase = (value: string) => phrases[value] ?? value

  return (
    <nav
      className="module-subnav"
      aria-label={phrase('Digital Assets navigation')}
    >
      {digitalAssetsItems.map((item) => (
        <NavLink
          key={item.label}
          to={item.to}
          className={(props: { isActive: boolean }) =>
            props.isActive ? 'active' : undefined
          }
        >
          {phrase(item.label)}
        </NavLink>
      ))}
    </nav>
  )
}
