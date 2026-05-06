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

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage />} />

      <Route
        path="/payments"
        element={
          <PlaceholderPage
            eyebrow="Payments"
            title="Payments"
            description="Simulated payments section for the Aurora Bank online banking prototype."
          />
        }
      />

      <Route
        path="/accounts"
        element={
          <PlaceholderPage
            eyebrow="Accounts"
            title="Accounts"
            description="Simulated accounts section showing where traditional banking account tools would appear."
          />
        }
      />

      <Route
        path="/cards"
        element={
          <PlaceholderPage
            eyebrow="Cards and Currency"
            title="Cards and Currency"
            description="Simulated cards and currency section for the banking portal."
          />
        }
      />

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

      <Route
        path="/online-services"
        element={
          <PlaceholderPage
            eyebrow="Online Services"
            title="Online Services"
            description="Simulated online services section for user settings, service messages, and bank portal tools."
          />
        }
      />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
