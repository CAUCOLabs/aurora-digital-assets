import { useState } from 'react'
import { Link } from 'react-router-dom'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

const cardProducts = [
  {
    name: 'Aurora Platinum',
    features: [
      'Combined credit/debit card concept',
      'Travel protection concept',
      'Minimum credit limit: 4 000 €',
    ],
  },
  {
    name: 'Aurora Gold',
    features: [
      'Everyday and travel card concept',
      'Purchase protection concept',
      'Minimum credit limit: 2 000 €',
    ],
  },
  {
    name: 'Aurora Debit',
    features: [
      'Debit card for daily use',
      'Purchases debited directly from account',
    ],
  },
]

const currencyServices = [
  'Currency accounts',
  'Exchange rates',
  'Travel money',
  'Currency calculator',
]

const seeAlsoLinks = [
  { label: 'Card statements', to: '/reports' },
  { label: 'Payment receipts', to: '/reports' },
  { label: 'Security settings', to: '/online-services' },
  { label: 'Online services', to: '/online-services' },
]

const paymentFreeMonthOptions = [
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  '10',
  '11',
  '12',
]

export function CardsPage() {
  const [cardholder, setCardholder] = useState('Claudio Demo')
  const [phoneNumber, setPhoneNumber] = useState('+358 40 123 4567')
  const [cardNumber, setCardNumber] = useState('•••• 2044')
  const [dueDateChange, setDueDateChange] = useState('15th day of month')
  const [minimumPayment, setMinimumPayment] = useState('10% of balance')
  const [paymentFreeMonths, setPaymentFreeMonths] = useState<string[]>([])
  const [otherRequest, setOtherRequest] = useState('')
  const [requestSubmitted, setRequestSubmitted] = useState(false)

  const canSubmit =
    cardholder.trim().length > 0 &&
    phoneNumber.trim().length > 0 &&
    cardNumber.trim().length > 0

  function updatePaymentFreeMonth(month: string) {
    setPaymentFreeMonths((currentMonths) =>
      currentMonths.includes(month)
        ? currentMonths.filter((currentMonth) => currentMonth !== month)
        : [...currentMonths, month],
    )
    setRequestSubmitted(false)
  }

  function handleSubmit() {
    if (!canSubmit) return
    setRequestSubmitted(true)
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">Cards and Currency</p>
            <h1>Cards and currency</h1>
            <p>
              View your cards, card status, card settings, and currency services
              from one banking section.
            </p>
          </div>

          <div className="security-badge">
            <span className="status-dot"></span>
            {requestSubmitted ? 'Request submitted' : 'Card security active'}
          </div>
        </section>

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Your cards</p>
                  <h2>Aurora Debit Online</h2>
                </div>
                <span className="module-tag">Active</span>
              </div>

              <div className="assets-summary">
                <div>
                  <p>Card</p>
                  <strong>Aurora Debit Online</strong>
                  <span>Cardholder: Claudio Demo</span>
                </div>

                <div className="custody-card">
                  <p>Card number</p>
                  <strong>•••• 2044</strong>
                  <span>Type: Debit · Valid until: 05/27</span>
                </div>
              </div>

              <div className="assets-summary trade-summary">
                <div>
                  <p>Card status</p>
                  <strong>Active</strong>
                  <span>Online purchases and card limits are available.</span>
                </div>
              </div>

              <div className="action-row">
                <Link className="button-link secondary-button" to="/cards">
                  Card details
                </Link>
                <Link className="button-link secondary-button" to="/cards">
                  Card settings
                </Link>
                <Link className="button-link secondary-button" to="/cards">
                  Card limits
                </Link>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Apply for a card</p>
                  <h2>Card products</h2>
                </div>
                <span className="module-tag">Simulated applications</span>
              </div>

              <div className="account-list">
                {cardProducts.map((product) => (
                  <article className="account-row" key={product.name}>
                    <div>
                      <h3>{product.name}</h3>
                      {product.features.map((feature) => (
                        <p key={feature}>{feature}</p>
                      ))}
                    </div>
                    <Link className="button-link secondary-button" to="/cards">
                      Apply
                    </Link>
                  </article>
                ))}
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Card change request</p>
                  <h2>Request card changes</h2>
                </div>
                <span className="module-tag">
                  {requestSubmitted ? 'Request submitted' : 'Draft request'}
                </span>
              </div>

              <div className="form-grid">
                <label>
                  Cardholder
                  <input
                    value={cardholder}
                    onChange={(event) => {
                      setCardholder(event.target.value)
                      setRequestSubmitted(false)
                    }}
                  />
                </label>

                <label>
                  Phone number
                  <input
                    value={phoneNumber}
                    onChange={(event) => {
                      setPhoneNumber(event.target.value)
                      setRequestSubmitted(false)
                    }}
                  />
                </label>

                <label>
                  Card number
                  <input
                    value={cardNumber}
                    onChange={(event) => {
                      setCardNumber(event.target.value)
                      setRequestSubmitted(false)
                    }}
                  />
                </label>

                <label>
                  Requested due date change
                  <select
                    value={dueDateChange}
                    onChange={(event) => {
                      setDueDateChange(event.target.value)
                      setRequestSubmitted(false)
                    }}
                  >
                    <option>15th day of month</option>
                    <option>Last day of month</option>
                    <option>No change requested</option>
                  </select>
                </label>

                <label>
                  Minimum payment option
                  <select
                    value={minimumPayment}
                    onChange={(event) => {
                      setMinimumPayment(event.target.value)
                      setRequestSubmitted(false)
                    }}
                  >
                    <option>10% of balance</option>
                    <option>20% of balance</option>
                    <option>Full balance</option>
                  </select>
                </label>

                <label>
                  Other change request
                  <textarea
                    value={otherRequest}
                    onChange={(event) => {
                      setOtherRequest(event.target.value)
                      setRequestSubmitted(false)
                    }}
                    rows={4}
                  />
                </label>
              </div>

              <div className="check-list">
                {paymentFreeMonthOptions.map((month) => (
                  <label key={month}>
                    <input
                      type="checkbox"
                      checked={paymentFreeMonths.includes(month)}
                      onChange={() => updatePaymentFreeMonth(month)}
                    />
                    Payment-free month {month}
                  </label>
                ))}
              </div>

              <div className="action-row">
                <button
                  type="button"
                  onClick={handleSubmit}
                  disabled={!canSubmit}
                >
                  Submit change request
                </button>
                {requestSubmitted && <span>Request submitted</span>}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel>
              <p className="eyebrow">Currency services</p>
              <h2>Currency tools</h2>

              <div className="check-list">
                {currencyServices.map((service) => (
                  <div key={service}>
                    <span className="status-dot"></span>
                    {service}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">Card security</p>
              <h2>Controls active</h2>

              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Card security active
                </div>
                <div>
                  <span className="status-dot"></span>
                  Online purchases protected
                </div>
                <div>
                  <span className="status-dot"></span>
                  Card limits available
                </div>
                <div>
                  <span className="status-dot"></span>
                  Suspicious activity monitoring enabled
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">See also</p>
              <h2>Related services</h2>

              <div className="check-list">
                {seeAlsoLinks.map((link) => (
                  <Link key={link.label} to={link.to}>
                    <span className="status-dot"></span>
                    {link.label}
                  </Link>
                ))}
              </div>
            </Panel>

            <Panel className="risk-panel">
              <p className="eyebrow">Prototype note</p>
              <h2>Simulated card services</h2>
              <p>
                This page simulates card and currency services. No real cards,
                card numbers, credit products, currency exchange, or customer
                data are used.
              </p>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. No real cards, card applications, card
          changes, currency exchange, or customer data are used.
        </section>
      </main>
    </div>
  )
}
