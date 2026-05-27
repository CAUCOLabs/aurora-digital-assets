import { useEffect, useState, type ReactNode } from 'react'
import { Navigate } from 'react-router-dom'
import { getSession } from '../services/authApi'
import { Panel } from './Panel'

type ProtectedRouteProps = {
  children: ReactNode
}

type SessionCheckState = 'checking' | 'authenticated' | 'unauthenticated'

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const [sessionState, setSessionState] = useState<SessionCheckState>(() =>
    localStorage.getItem('aurora_bank_session_id')
      ? 'checking'
      : 'unauthenticated',
  )

  useEffect(() => {
    let active = true
    const sessionId = localStorage.getItem('aurora_bank_session_id')

    if (!sessionId) {
      return
    }
    const storedSessionId = sessionId

    async function checkSession() {
      try {
        const session = await getSession(storedSessionId)

        if (!active) {
          return
        }

        if (session.authenticated) {
          setSessionState('authenticated')
        } else {
          localStorage.removeItem('aurora_bank_session_id')
          setSessionState('unauthenticated')
        }
      } catch {
        if (!active) {
          return
        }

        localStorage.removeItem('aurora_bank_session_id')
        setSessionState('unauthenticated')
      }
    }

    void checkSession()

    return () => {
      active = false
    }
  }, [])

  if (sessionState === 'checking') {
    return (
      <div className="bank-shell">
        <main className="page">
          <Panel>
            <p className="eyebrow">Aurora eBanking</p>
            <h2>Checking banking session...</h2>
          </Panel>
        </main>
      </div>
    )
  }

  if (sessionState === 'unauthenticated') {
    return <Navigate to="/bank-login" replace />
  }

  return children
}
