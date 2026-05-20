import { usePrivacyMode } from '../context/PrivacyModeContext'

type PrivacyAmountProps = {
  value: string | number
  label?: string
  className?: string
}

export function PrivacyAmount({
  value,
  label,
  className,
}: PrivacyAmountProps) {
  const { amountsVisible } = usePrivacyMode()
  const visibleValue = String(value)
  const classNames = ['privacy-amount', className].filter(Boolean).join(' ')

  return (
    <span
      aria-label={amountsVisible ? (label ?? 'amount') : 'Hidden amount'}
      className={classNames}
    >
      {amountsVisible ? visibleValue : '••••••••'}
    </span>
  )
}
