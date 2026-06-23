import { usePrivacyMode } from '../context/PrivacyModeContext'
import { useLanguage } from '../context/LanguageContext'

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
  const { t } = useLanguage()
  const phrases = t.phrases as Record<string, string>
  const phrase = (value: string) => phrases[value] ?? value
  const visibleValue = String(value)
  const classNames = ['privacy-amount', className].filter(Boolean).join(' ')

  return (
    <span
      aria-label={
        amountsVisible ? (label ? phrase(label) : phrase('amount')) : phrase('Hidden amount')
      }
      className={classNames}
    >
      {amountsVisible ? visibleValue : '••••••••'}
    </span>
  )
}
