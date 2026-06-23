/* eslint-disable react-refresh/only-export-components */
import {
  createContext,
  type ReactNode,
  useContext,
  useEffect,
  useMemo,
  useState,
} from 'react'
import {
  defaultLanguage,
  translations,
  type Language,
} from '../i18n/translations'

const languageStorageKey = 'aurora_language'

type Translation = (typeof translations)[Language]

type LanguageContextValue = {
  language: Language
  setLanguage: (language: Language) => void
  t: Translation
}

const LanguageContext = createContext<LanguageContextValue | null>(null)

function getInitialLanguage(): Language {
  const storedLanguage = localStorage.getItem(languageStorageKey)
  return storedLanguage === 'en' || storedLanguage === 'es'
    ? storedLanguage
    : defaultLanguage
}

function normalizePhrase(value: string) {
  return value.replace(/\s+/g, ' ').trim()
}

function createPhraseLookup(language: Language) {
  const lookup = new Map<string, string>()
  const sourceLanguages = Object.keys(translations) as Language[]

  sourceLanguages.forEach((sourceLanguage) => {
    collectTranslationStrings(
      translations[sourceLanguage],
      translations[language],
      lookup,
    )
  })

  return lookup
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null
}

function collectTranslationStrings(
  sourceValue: unknown,
  targetValue: unknown,
  lookup: Map<string, string>,
) {
  if (typeof sourceValue === 'string' && typeof targetValue === 'string') {
    lookup.set(normalizePhrase(sourceValue), targetValue)
    return
  }

  if (!isRecord(sourceValue) || !isRecord(targetValue)) {
    return
  }

  Object.entries(sourceValue).forEach(([key, childSourceValue]) => {
    collectTranslationStrings(childSourceValue, targetValue[key], lookup)
  })
}

function translateDomPhrase(value: string, lookup: Map<string, string>) {
  const normalizedValue = normalizePhrase(value)
  const translatedValue = lookup.get(normalizedValue)

  if (!translatedValue || normalizedValue === translatedValue) {
    return value
  }

  const leadingWhitespace = value.match(/^\s*/)?.[0] ?? ''
  const trailingWhitespace = value.match(/\s*$/)?.[0] ?? ''

  return `${leadingWhitespace}${translatedValue}${trailingWhitespace}`
}

function translateDomText(root: ParentNode, language: Language) {
  const lookup = createPhraseLookup(language)
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
  let textNode = walker.nextNode()

  while (textNode) {
    const nextValue = translateDomPhrase(textNode.nodeValue ?? '', lookup)

    if (nextValue !== textNode.nodeValue) {
      textNode.nodeValue = nextValue
    }

    textNode = walker.nextNode()
  }

  const translatedAttributes = [
    'aria-label',
    'title',
    'placeholder',
  ] as const

  root.querySelectorAll<HTMLElement>('*').forEach((element) => {
    translatedAttributes.forEach((attribute) => {
      const currentValue = element.getAttribute(attribute)

      if (!currentValue) {
        return
      }

      const nextValue = translateDomPhrase(currentValue, lookup)

      if (nextValue !== currentValue) {
        element.setAttribute(attribute, nextValue)
      }
    })
  })
}

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [language, setLanguage] = useState<Language>(getInitialLanguage)

  useEffect(() => {
    localStorage.setItem(languageStorageKey, language)
    document.documentElement.lang = language
  }, [language])

  useEffect(() => {
    translateDomText(document.body, language)

    const observer = new MutationObserver(() => {
      translateDomText(document.body, language)
    })

    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ['aria-label', 'title', 'placeholder'],
      childList: true,
      characterData: true,
      subtree: true,
    })

    return () => observer.disconnect()
  }, [language])

  const value = useMemo(
    () => ({
      language,
      setLanguage,
      t: translations[language],
    }),
    [language],
  )

  return (
    <LanguageContext.Provider value={value}>
      {children}
    </LanguageContext.Provider>
  )
}

export function useLanguage() {
  const context = useContext(LanguageContext)

  if (!context) {
    throw new Error('useLanguage must be used within LanguageProvider.')
  }

  return context
}
