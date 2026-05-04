import { Routes, Route, Navigate } from 'react-router-dom'
import { DashboardPage } from '../pages/DashboardPage'
import { DigitalAssetsPage } from '../pages/DigitalAssetsPage'
import { WalletPage } from '../pages/WalletPage'
import { WithdrawalsPage } from '../pages/WithdrawalsPage'
import { ReportsPage } from '../pages/ReportsPage'

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage />} />
      <Route path="/digital-assets" element={<DigitalAssetsPage />} />
      <Route path="/wallet" element={<WalletPage />} />
      <Route path="/withdrawals" element={<WithdrawalsPage />} />
      <Route path="/reports" element={<ReportsPage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}