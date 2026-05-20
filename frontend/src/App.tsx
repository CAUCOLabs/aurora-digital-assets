import './App.css'
import { BrowserRouter } from 'react-router-dom'
import { PrivacyModeProvider } from './context/PrivacyModeContext'
import { AppRoutes } from './routes/AppRoutes'

function App() {
  return (
    <PrivacyModeProvider>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </PrivacyModeProvider>
  )
}

export default App
