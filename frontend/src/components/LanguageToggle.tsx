import { useLanguage } from '../context/LanguageContext'
import { type Language } from '../i18n/translations'

export function LanguageToggle() {
  const { language, setLanguage, t } = useLanguage()

  return (
    <label className="language-toggle">
      <span>{t.common.language}</span>
      <select
        value={language}
        aria-label={t.common.language}
        onChange={(event) => setLanguage(event.target.value as Language)}
      >
        <option value="en">EN</option>
        <option value="es">ES</option>
      </select>
    </label>
  )
}
