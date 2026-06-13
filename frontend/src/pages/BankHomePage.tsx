import { Link } from 'react-router-dom'
import { LanguageToggle } from '../components/LanguageToggle'
import { Panel } from '../components/Panel'
import { useLanguage } from '../context/LanguageContext'

const publicNavigationHrefs = [
  '#for-you',
  '#services',
  '#services',
  '#services',
  '#contact',
  '#digital-assets',
  '#contact',
]

export function BankHomePage() {
  const { t } = useLanguage()
  const publicNavigation = t.bankHome.publicNavigation.map((label, index) => ({
    label,
    href: publicNavigationHrefs[index],
  }))

  return (
    <div className="bank-shell">
      <header className="top-bar">
        <Link className="brand" to="/" aria-label="Go to Aurora Bank home">
          <div className="brand-mark">A</div>
          <div>
            <p className="brand-name">Aurora Bank</p>
            <p className="brand-subtitle">{t.bankHome.publicConcept}</p>
          </div>
        </Link>

        <nav className="main-nav" aria-label="Public navigation">
          {publicNavigation.map((item) => (
            <div className="nav-item" key={item.label}>
              <a className="main-nav-link" href={item.href}>
                {item.label}
              </a>
            </div>
          ))}
        </nav>

        <div className="user-area">
          <LanguageToggle />
          <Link className="button-link secondary-button" to="/bank-login">
            {t.bankHome.logIn}
          </Link>
        </div>
      </header>

      <main className="page">
        <section className="welcome-card" id="for-you">
          <div>
            <p className="eyebrow">Aurora Bank</p>
            <h1>{t.bankHome.heroTitle}</h1>
            <p>{t.bankHome.heroSubtitle}</p>

            <div className="action-row">
              <Link className="button-link" to="/bank-login">
                {t.bankHome.logInEbanking}
              </Link>
              <Link className="button-link secondary-button" to="/bank-access">
                {t.bankHome.learnDigitalAssets}
              </Link>
            </div>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {t.bankHome.formalAccess}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel id="services">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">{t.bankHome.servicesEyebrow}</p>
                  <h2>{t.bankHome.servicesTitle}</h2>
                </div>
                <span className="module-tag">{t.bankHome.publicInformation}</span>
              </div>

              <div className="account-list">
                {t.bankHome.services.map((service) => (
                  <article className="account-row" key={service.title}>
                    <div>
                      <h3>{service.title}</h3>
                      <p>{service.description}</p>
                    </div>
                    <strong>{t.bankHome.explore}</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel id="digital-assets">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Aurora Digital Assets</p>
                  <h2>{t.bankHome.integratedTitle}</h2>
                </div>
                <span className="module-tag">{t.bankHome.eligibilityApplies}</span>
              </div>

              <p>
                Aurora Digital Assets is presented as a bank-integrated module,
                not a standalone signup service. Access depends on an existing
                customer relationship, authenticated banking session, and
                eligibility checks.
              </p>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">{t.bankHome.securityInformation}</p>
              <h2>{t.bankHome.officialChannels}</h2>
              <p>
                Always access eBanking through the official banking channel.
                Aurora Bank never asks for bank identifiers by email or text
                message.
              </p>
              <Link className="button-link" to="/bank-login">
                {t.bankHome.logInSecurely}
              </Link>
            </Panel>

            <Panel id="contact">
              <p className="eyebrow">{t.bankHome.becomeCustomer}</p>
              <h2>{t.bankHome.contactOnboarding}</h2>
              <p>
                New customer onboarding, document review, and credential
                issuance would be handled through the bank&apos;s formal
                processes outside Aurora Digital Assets.
              </p>
              <div className="action-row vertical-actions">
                <button type="button" className="secondary-button">
                  {t.bankHome.contactBank}
                </button>
                <button type="button" className="secondary-button">
                  {t.bankHome.readServiceInfo}
                </button>
              </div>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real bank services, accounts,
          customer data, or payments are used.
        </section>
      </main>
    </div>
  )
}
