import { Routes, Route, Navigate } from 'react-router-dom'
import { DashboardPage } from '../pages/DashboardPage'
import { DigitalAssetsPage } from '../pages/DigitalAssetsPage'
import { WalletPage } from '../pages/WalletPage'
import { WithdrawalsPage } from '../pages/WithdrawalsPage'
import { ReportsPage } from '../pages/ReportsPage'
import { PlaceholderPage } from '../pages/PlaceholderPage'
import { BuySellPage } from '../pages/BuySellPage'
import { CustodyPage } from '../pages/CustodyPage'
import { OperatingModelPage } from '../pages/OperatingModelPage'
import { PaymentsPage } from '../pages/PaymentsPage'
import { AccountsPage } from '../pages/AccountsPage'
import { CardsPage } from '../pages/CardsPage'
import { ComplianceReviewPage } from '../pages/ComplianceReviewPage'
import { DemoAdminPage } from '../pages/DemoAdminPage'
import { BankAccessPage } from '../pages/BankAccessPage'
import { BankLoginPage } from '../pages/BankLoginPage'
import { ProtectedRoute } from '../components/ProtectedRoute'
import { BankHomePage } from '../pages/BankHomePage'

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<BankHomePage />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <DashboardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments"
        element={
          <ProtectedRoute>
            <PaymentsPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/accounts"
        element={
          <ProtectedRoute>
            <AccountsPage />
          </ProtectedRoute>
        }
      />

      <Route path="/cards" element={<CardsPage />} />

      <Route
        path="/loans"
        element={
          <PlaceholderPage
            eyebrow="Loans"
            title="Loans"
            description="Simulated loans section for the Aurora Bank online banking prototype."
          />
        }
      />

      <Route
        path="/investments"
        element={
          <PlaceholderPage
            eyebrow="Investments"
            title="Investments"
            description="Simulated investments section. The prototype separates traditional investments from Digital Assets."
          />
        }
      />

      <Route
        path="/insurance"
        element={
          <PlaceholderPage
            eyebrow="Insurance"
            title="Insurance"
            description="Simulated insurance section for the Aurora Bank online banking prototype."
          />
        }
      />

      <Route
        path="/digital-assets"
        element={
          <ProtectedRoute>
            <DigitalAssetsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/buy-sell"
        element={
          <ProtectedRoute>
            <BuySellPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/wallet"
        element={
          <ProtectedRoute>
            <WalletPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/withdrawals"
        element={
          <ProtectedRoute>
            <WithdrawalsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports"
        element={
          <ProtectedRoute>
            <ReportsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/custody"
        element={
          <ProtectedRoute>
            <CustodyPage />
          </ProtectedRoute>
        }
      />
      <Route path="/operating-model" element={<OperatingModelPage />} />
      <Route
        path="/compliance-review"
        element={
          <ProtectedRoute>
            <ComplianceReviewPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/admin-demo"
        element={
          <ProtectedRoute>
            <DemoAdminPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-access"
        element={
          <ProtectedRoute>
            <BankAccessPage />
          </ProtectedRoute>
        }
      />
      <Route path="/bank-login" element={<BankLoginPage />} />

      <Route
        path="/online-services"
        element={
          <PlaceholderPage
            eyebrow="Online Services"
            title="Online Services"
            description="Simulated online and mobile services section for the Aurora Bank online banking prototype."
          />
        }
      />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
