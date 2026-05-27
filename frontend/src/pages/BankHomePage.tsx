import { Link } from 'react-router-dom'
import { Panel } from '../components/Panel'

const publicNavigation = [
  { label: 'For you', href: '#for-you' },
  { label: 'For businesses', href: '#services' },
  { label: 'Private Banking', href: '#services' },
  { label: 'Daily banking', href: '#services' },
  { label: 'Customer service', href: '#contact' },
  { label: 'Digital Assets', href: '#digital-assets' },
  { label: 'Documents', href: '#contact' },
]

const serviceCards = [
  {
    title: 'Accounts and payments',
    description:
      'Everyday account and payment service concepts for customers with an Aurora Bank relationship.',
  },
  {
    title: 'Housing loan concept',
    description:
      'Structured guidance for major life decisions within a formal banking relationship.',
  },
  {
    title: 'Savings and investments',
    description:
      'Clear information and responsible planning concepts for long-term finances.',
  },
  {
    title: 'Digital Assets module',
    description:
      'Eligible customers may access simulated digital asset services through authenticated eBanking.',
  },
  {
    title: 'Customer service',
    description:
      'Support pathways for banking questions, documents, and service information.',
  },
  {
    title: 'Security and strong authentication',
    description:
      'Bank-issued credentials and strong authentication protect access to personal services.',
  },
]

export function BankHomePage() {
  return (
    <div className="bank-shell">
      <header className="top-bar">
        <Link className="brand" to="/" aria-label="Go to Aurora Bank home">
          <div className="brand-mark">A</div>
          <div>
            <p className="brand-name">Aurora Bank</p>
            <p className="brand-subtitle">Public banking website concept</p>
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
          <Link className="button-link secondary-button" to="/bank-login">
            Log in
          </Link>
        </div>
      </header>

      <main className="page">
        <section className="welcome-card" id="for-you">
          <div>
            <p className="eyebrow">Aurora Bank</p>
            <h1>Banking services for everyday life</h1>
            <p>
              Access accounts, payments, documents, and eligible digital asset
              services through a formal banking relationship.
            </p>

            <div className="action-row">
              <Link className="button-link" to="/bank-login">
                Log in to eBanking
              </Link>
              <Link className="button-link secondary-button" to="/bank-access">
                Learn about Aurora Digital Assets
              </Link>
            </div>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            Formal banking access
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel id="services">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Services and life situations</p>
                  <h2>How can Aurora Bank help?</h2>
                </div>
                <span className="module-tag">Public information</span>
              </div>

              <div className="account-list">
                {serviceCards.map((service) => (
                  <article className="account-row" key={service.title}>
                    <div>
                      <h3>{service.title}</h3>
                      <p>{service.description}</p>
                    </div>
                    <strong>Explore</strong>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel id="digital-assets">
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Aurora Digital Assets</p>
                  <h2>Integrated within online banking</h2>
                </div>
                <span className="module-tag">Eligibility applies</span>
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
              <p className="eyebrow">Security information</p>
              <h2>Use official banking channels</h2>
              <p>
                Always access eBanking through the official banking channel.
                Aurora Bank never asks for bank identifiers by email or text
                message.
              </p>
              <Link className="button-link" to="/bank-login">
                Log in securely
              </Link>
            </Panel>

            <Panel id="contact">
              <p className="eyebrow">Become a customer</p>
              <h2>Contact and onboarding</h2>
              <p>
                New customer onboarding, document review, and credential
                issuance would be handled through the bank&apos;s formal
                processes outside Aurora Digital Assets.
              </p>
              <div className="action-row vertical-actions">
                <button type="button" className="secondary-button">
                  Contact Aurora Bank
                </button>
                <button type="button" className="secondary-button">
                  Read service information
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
