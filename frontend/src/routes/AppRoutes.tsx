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

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage />} />
      <Route path="/payments" element={<PaymentsPage />} />

      <Route path="/accounts" element={<AccountsPage />} />

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

      <Route path="/digital-assets" element={<DigitalAssetsPage />} />
      <Route path="/buy-sell" element={<BuySellPage />} />
      <Route path="/wallet" element={<WalletPage />} />
      <Route path="/withdrawals" element={<WithdrawalsPage />} />
      <Route path="/reports" element={<ReportsPage />} />
      <Route path="/custody" element={<CustodyPage />} />
      <Route path="/operating-model" element={<OperatingModelPage />} />
      <Route path="/compliance-review" element={<ComplianceReviewPage />} />
      <Route path="/admin-demo" element={<DemoAdminPage />} />
      <Route path="/bank-access" element={<BankAccessPage />} />

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
