/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useState, type ReactNode } from 'react'

type PrivacyModeContextValue = {
  amountsVisible: boolean
  toggleAmountsVisible: () => void
}

const PrivacyModeContext = createContext<PrivacyModeContextValue | null>(null)

type PrivacyModeProviderProps = {
  children: ReactNode
}

export function PrivacyModeProvider({ children }: PrivacyModeProviderProps) {
  const [amountsVisible, setAmountsVisible] = useState(false)

  function toggleAmountsVisible() {
    setAmountsVisible((currentValue) => !currentValue)
  }

  return (
    <PrivacyModeContext.Provider
      value={{ amountsVisible, toggleAmountsVisible }}
    >
      {children}
    </PrivacyModeContext.Provider>
  )
}

export function usePrivacyMode() {
  const context = useContext(PrivacyModeContext)

  if (!context) {
    throw new Error('usePrivacyMode must be used inside PrivacyModeProvider.')
  }

  return context
}
