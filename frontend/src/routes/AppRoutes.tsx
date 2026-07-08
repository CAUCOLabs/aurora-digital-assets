import { Routes, Route, Navigate } from 'react-router-dom'
import { DashboardPage } from '../pages/DashboardPage'
import { DigitalAssetsPage } from '../pages/DigitalAssetsPage'
import { WalletPage } from '../pages/WalletPage'
import { WithdrawalsPage } from '../pages/WithdrawalsPage'
import { ReportsPage } from '../pages/ReportsPage'
import { AccountStatementsPage } from '../pages/AccountStatementsPage'
import { CardStatementsPage } from '../pages/CardStatementsPage'
import { TaxReportsPage } from '../pages/TaxReportsPage'
import { ExportDocumentsPage } from '../pages/ExportDocumentsPage'
import { AuditTrailPage } from '../pages/AuditTrailPage'
import { BankMailPage } from '../pages/BankMailPage'
import { EvidenceRecordsPage } from '../pages/EvidenceRecordsPage'
import { ComplianceRecordsPage } from '../pages/ComplianceRecordsPage'
import { PlaceholderPage } from '../pages/PlaceholderPage'
import { BuySellPage } from '../pages/BuySellPage'
import { CustodyPage } from '../pages/CustodyPage'
import { OperatingModelPage } from '../pages/OperatingModelPage'
import { PaymentsPage } from '../pages/PaymentsPage'
import { NewPaymentPage } from '../pages/NewPaymentPage'
import { ApprovePaymentsPage } from '../pages/ApprovePaymentsPage'
import { InternationalPaymentPage } from '../pages/InternationalPaymentPage'
import { RecipientsPage } from '../pages/RecipientsPage'
import { PaymentLimitsPage } from '../pages/PaymentLimitsPage'
import { DigitalAssetPaymentPage } from '../pages/DigitalAssetPaymentPage'
import { SupportedBusinessRecipientsPage } from '../pages/SupportedBusinessRecipientsPage'
import { PaymentAssetSettingsPage } from '../pages/PaymentAssetSettingsPage'
import { EInvoiceAgreementPage } from '../pages/EInvoiceAgreementPage'
import { RecurringPaymentPage } from '../pages/RecurringPaymentPage'
import { PaymentAgreementsPage } from '../pages/PaymentAgreementsPage'
import { AccountsPage } from '../pages/AccountsPage'
import { AccountBalancesPage } from '../pages/AccountBalancesPage'
import { AccountTransactionsPage } from '../pages/AccountTransactionsPage'
import { CurrentAccountPage } from '../pages/CurrentAccountPage'
import { SavingsDepositAccountsPage } from '../pages/SavingsDepositAccountsPage'
import { ChildAccountPage } from '../pages/ChildAccountPage'
import { AccountFAQPage } from '../pages/AccountFAQPage'
import { ApiSecurityPage } from '../pages/ApiSecurityPage'
import { AssetRailGovernancePage } from '../pages/AssetRailGovernancePage'
import { CardsPage } from '../pages/CardsPage'
import { CardOverviewPage } from '../pages/CardOverviewPage'
import { ApplyCardPage } from '../pages/ApplyCardPage'
import { CardSettingsPage } from '../pages/CardSettingsPage'
import { CardLimitsPage } from '../pages/CardLimitsPage'
import { CurrencyAccountsPage } from '../pages/CurrencyAccountsPage'
import { ExchangeRatesPage } from '../pages/ExchangeRatesPage'
import { TravelMoneyPage } from '../pages/TravelMoneyPage'
import { CardFAQPage } from '../pages/CardFAQPage'
import { InvestmentOverviewPage } from '../pages/InvestmentOverviewPage'
import { FundsPage } from '../pages/FundsPage'
import { StocksPage } from '../pages/StocksPage'
import { InvestmentAccountsPage } from '../pages/InvestmentAccountsPage'
import { TradingPage } from '../pages/TradingPage'
import { InvestmentCustodyAccountsPage } from '../pages/InvestmentCustodyAccountsPage'
import { InvestmentPricesPage } from '../pages/InvestmentPricesPage'
import { MarketNewsPage } from '../pages/MarketNewsPage'
import { InvestmentResearchPage } from '../pages/InvestmentResearchPage'
import { InvestmentFAQPage } from '../pages/InvestmentFAQPage'
import { InvestmentRiskInformationPage } from '../pages/InvestmentRiskInformationPage'
import { LoansPage } from '../pages/LoansPage'
import { LoansOverviewPage } from '../pages/LoansOverviewPage'
import { LoanApplicationPage } from '../pages/LoanApplicationPage'
import { MortgagePage } from '../pages/MortgagePage'
import { ConsumerLoanPage } from '../pages/ConsumerLoanPage'
import { StudentLoanPage } from '../pages/StudentLoanPage'
import { LoanCalculatorPage } from '../pages/LoanCalculatorPage'
import { RepaymentPlanPage } from '../pages/RepaymentPlanPage'
import { LoanDocumentsPage } from '../pages/LoanDocumentsPage'
import { LoanFAQPage } from '../pages/LoanFAQPage'
import { InsurancePage } from '../pages/InsurancePage'
import { InsuranceOverviewPage } from '../pages/InsuranceOverviewPage'
import { HomeInsurancePage } from '../pages/HomeInsurancePage'
import { TravelInsurancePage } from '../pages/TravelInsurancePage'
import { LifeInsurancePage } from '../pages/LifeInsurancePage'
import { HealthInsurancePage } from '../pages/HealthInsurancePage'
import { InsuranceClaimsPage } from '../pages/InsuranceClaimsPage'
import { InsuranceDocumentsPage } from '../pages/InsuranceDocumentsPage'
import { InsuranceFAQPage } from '../pages/InsuranceFAQPage'
import { ComplianceReviewPage } from '../pages/ComplianceReviewPage'
import { CryptoAgilityPage } from '../pages/CryptoAgilityPage'
import { DemoAdminPage } from '../pages/DemoAdminPage'
import { BankAccessPage } from '../pages/BankAccessPage'
import { BankStaffWorkspacePage } from '../pages/BankStaffWorkspacePage'
import { BankStaffOnboardingPage } from '../pages/BankStaffOnboardingPage'
import { AgentGovernancePage } from '../pages/AgentGovernancePage'
import { ComplianceIntelligencePage } from '../pages/ComplianceIntelligencePage'
import { EvidencePackagesPage } from '../pages/EvidencePackagesPage'
import { FinancialCrimeMonitoringPage } from '../pages/FinancialCrimeMonitoringPage'
import { HumanApprovalIntegrityPage } from '../pages/HumanApprovalIntegrityPage'
import { InfrastructureSecurityPage } from '../pages/InfrastructureSecurityPage'
import { OperationalResiliencePage } from '../pages/OperationalResiliencePage'
import { RiskOperationsPage } from '../pages/RiskOperationsPage'
import { SensitiveApprovalPage } from '../pages/SensitiveApprovalPage'
import { StaffCustomerAccessPage } from '../pages/StaffCustomerAccessPage'
import { TrustEnginePage } from '../pages/TrustEnginePage'
import { BankLoginPage } from '../pages/BankLoginPage'
import { ProtectedRoute } from '../components/ProtectedRoute'
import { BankHomePage } from '../pages/BankHomePage'
import { OnlineServicesPage } from '../pages/OnlineServicesPage'
import { OnlineBankingSettingsPage } from '../pages/OnlineBankingSettingsPage'
import { MobileBankingPage } from '../pages/MobileBankingPage'
import { StrongAuthenticationPage } from '../pages/StrongAuthenticationPage'
import { MessageSettingsPage } from '../pages/MessageSettingsPage'
import { NotificationSettingsPage } from '../pages/NotificationSettingsPage'
import { DeviceManagementPage } from '../pages/DeviceManagementPage'
import { SecurityAlertsPage } from '../pages/SecurityAlertsPage'
import { OnlineServicesFAQPage } from '../pages/OnlineServicesFAQPage'

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
        path="/payments/new"
        element={
          <ProtectedRoute>
            <NewPaymentPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/approve"
        element={
          <ProtectedRoute>
            <ApprovePaymentsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/international"
        element={
          <ProtectedRoute>
            <InternationalPaymentPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/recipients"
        element={
          <ProtectedRoute>
            <RecipientsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/limits"
        element={
          <ProtectedRoute>
            <PaymentLimitsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/digital-asset-payment"
        element={
          <ProtectedRoute>
            <DigitalAssetPaymentPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/supported-business-recipients"
        element={
          <ProtectedRoute>
            <SupportedBusinessRecipientsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/asset-settings"
        element={
          <ProtectedRoute>
            <PaymentAssetSettingsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/e-invoice-agreement"
        element={
          <ProtectedRoute>
            <EInvoiceAgreementPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/recurring"
        element={
          <ProtectedRoute>
            <RecurringPaymentPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/payments/payment-agreements"
        element={
          <ProtectedRoute>
            <PaymentAgreementsPage />
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
      <Route
        path="/accounts/balances"
        element={
          <ProtectedRoute>
            <AccountBalancesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/accounts/transactions"
        element={
          <ProtectedRoute>
            <AccountTransactionsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/accounts/current-account"
        element={
          <ProtectedRoute>
            <CurrentAccountPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/accounts/savings-deposits"
        element={
          <ProtectedRoute>
            <SavingsDepositAccountsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/accounts/child-account"
        element={
          <ProtectedRoute>
            <ChildAccountPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/accounts/faq"
        element={
          <ProtectedRoute>
            <AccountFAQPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/cards"
        element={
          <ProtectedRoute>
            <CardsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/overview"
        element={
          <ProtectedRoute>
            <CardOverviewPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/apply"
        element={
          <ProtectedRoute>
            <ApplyCardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/settings"
        element={
          <ProtectedRoute>
            <CardSettingsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/limits"
        element={
          <ProtectedRoute>
            <CardLimitsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/currency-accounts"
        element={
          <ProtectedRoute>
            <CurrencyAccountsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/exchange-rates"
        element={
          <ProtectedRoute>
            <ExchangeRatesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/travel-money"
        element={
          <ProtectedRoute>
            <TravelMoneyPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/cards/faq"
        element={
          <ProtectedRoute>
            <CardFAQPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/loans"
        element={
          <ProtectedRoute>
            <LoansPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/overview"
        element={
          <ProtectedRoute>
            <LoansOverviewPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/apply"
        element={
          <ProtectedRoute>
            <LoanApplicationPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/mortgage"
        element={
          <ProtectedRoute>
            <MortgagePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/consumer-loan"
        element={
          <ProtectedRoute>
            <ConsumerLoanPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/student-loan"
        element={
          <ProtectedRoute>
            <StudentLoanPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/loan-calculator"
        element={
          <ProtectedRoute>
            <LoanCalculatorPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/repayment-plan"
        element={
          <ProtectedRoute>
            <RepaymentPlanPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/documents"
        element={
          <ProtectedRoute>
            <LoanDocumentsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/loans/faq"
        element={
          <ProtectedRoute>
            <LoanFAQPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/investments"
        element={
          <ProtectedRoute>
            <PlaceholderPage
              eyebrow="Investments"
              title="Investments"
              description="Simulated investments section. The prototype separates traditional investments from Digital Assets."
            />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/overview"
        element={
          <ProtectedRoute>
            <InvestmentOverviewPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/funds"
        element={
          <ProtectedRoute>
            <FundsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/stocks"
        element={
          <ProtectedRoute>
            <StocksPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/accounts"
        element={
          <ProtectedRoute>
            <InvestmentAccountsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/trading"
        element={
          <ProtectedRoute>
            <TradingPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/custody-accounts"
        element={
          <ProtectedRoute>
            <InvestmentCustodyAccountsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/prices"
        element={
          <ProtectedRoute>
            <InvestmentPricesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/market-news"
        element={
          <ProtectedRoute>
            <MarketNewsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/research"
        element={
          <ProtectedRoute>
            <InvestmentResearchPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/faq"
        element={
          <ProtectedRoute>
            <InvestmentFAQPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/investments/risk-information"
        element={
          <ProtectedRoute>
            <InvestmentRiskInformationPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/insurance"
        element={
          <ProtectedRoute>
            <InsurancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/overview"
        element={
          <ProtectedRoute>
            <InsuranceOverviewPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/home"
        element={
          <ProtectedRoute>
            <HomeInsurancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/travel"
        element={
          <ProtectedRoute>
            <TravelInsurancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/life"
        element={
          <ProtectedRoute>
            <LifeInsurancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/health"
        element={
          <ProtectedRoute>
            <HealthInsurancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/claims"
        element={
          <ProtectedRoute>
            <InsuranceClaimsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/documents"
        element={
          <ProtectedRoute>
            <InsuranceDocumentsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/insurance/faq"
        element={
          <ProtectedRoute>
            <InsuranceFAQPage />
          </ProtectedRoute>
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
        path="/reports/account-statements"
        element={
          <ProtectedRoute>
            <AccountStatementsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/card-statements"
        element={
          <ProtectedRoute>
            <CardStatementsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/tax-reports"
        element={
          <ProtectedRoute>
            <TaxReportsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/export-documents"
        element={
          <ProtectedRoute>
            <ExportDocumentsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/audit-trail"
        element={
          <ProtectedRoute>
            <AuditTrailPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/bank-mail"
        element={
          <ProtectedRoute>
            <BankMailPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/evidence-records"
        element={
          <ProtectedRoute>
            <EvidenceRecordsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/reports/compliance-records"
        element={
          <ProtectedRoute>
            <ComplianceRecordsPage />
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
      <Route
        path="/bank-staff"
        element={
          <ProtectedRoute>
            <BankStaffWorkspacePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/onboarding"
        element={
          <ProtectedRoute>
            <BankStaffOnboardingPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/customer-access"
        element={
          <ProtectedRoute>
            <StaffCustomerAccessPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/risk-operations"
        element={
          <ProtectedRoute>
            <RiskOperationsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/trust-engine"
        element={
          <ProtectedRoute>
            <TrustEnginePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/agent-governance"
        element={
          <ProtectedRoute>
            <AgentGovernancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/human-approval-integrity"
        element={
          <ProtectedRoute>
            <HumanApprovalIntegrityPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/financial-crime-monitoring"
        element={
          <ProtectedRoute>
            <FinancialCrimeMonitoringPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/compliance-intelligence"
        element={
          <ProtectedRoute>
            <ComplianceIntelligencePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/evidence-packages"
        element={
          <ProtectedRoute>
            <EvidencePackagesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/operational-resilience"
        element={
          <ProtectedRoute>
            <OperationalResiliencePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/api-security"
        element={
          <ProtectedRoute>
            <ApiSecurityPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/infrastructure-security"
        element={
          <ProtectedRoute>
            <InfrastructureSecurityPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/crypto-agility"
        element={
          <ProtectedRoute>
            <CryptoAgilityPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/asset-rail-governance"
        element={
          <ProtectedRoute>
            <AssetRailGovernancePage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/bank-staff/sensitive-approval"
        element={
          <ProtectedRoute>
            <SensitiveApprovalPage />
          </ProtectedRoute>
        }
      />
      <Route path="/bank-login" element={<BankLoginPage />} />

      <Route
        path="/online-services"
        element={
          <ProtectedRoute>
            <OnlineServicesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/settings"
        element={
          <ProtectedRoute>
            <OnlineBankingSettingsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/mobile-banking"
        element={
          <ProtectedRoute>
            <MobileBankingPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/strong-authentication"
        element={
          <ProtectedRoute>
            <StrongAuthenticationPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/messages"
        element={
          <ProtectedRoute>
            <MessageSettingsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/notifications"
        element={
          <ProtectedRoute>
            <NotificationSettingsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/device-management"
        element={
          <ProtectedRoute>
            <DeviceManagementPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/security-alerts"
        element={
          <ProtectedRoute>
            <SecurityAlertsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/online-services/faq"
        element={
          <ProtectedRoute>
            <OnlineServicesFAQPage />
          </ProtectedRoute>
        }
      />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
