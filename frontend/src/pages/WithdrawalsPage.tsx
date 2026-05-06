import { useMemo, useState } from 'react'
import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'
import { DigitalAssetsSubnav } from '../components/DigitalAssetsSubnav'

type WithdrawalStatus = 'draft' | 'pending_review'

export function WithdrawalsPage() {
  const [asset, setAsset] = useState('BTC')
  const [network, setNetwork] = useState('Bitcoin')
  const [address, setAddress] = useState('')
  const [amount, setAmount] = useState('')
  const [status, setStatus] = useState<WithdrawalStatus>('draft')
  const [securityCheckRun, setSecurityCheckRun] = useState(false)

  const canSubmit = address.trim().length > 12 && amount.trim().length > 0

  const auditEvents = useMemo(() => {
    const events = [
      {
        title: 'Withdrawal form opened',
        detail: 'User entered external wallet transfer flow.',
        status: 'Recorded',
      },
    ]

    if (securityCheckRun) {
      events.push({
        title: 'Protection review completed',
        detail: 'Address format, user profile, and withdrawal policy reviewed.',
        status: 'Passed',
      })
    }

    if (status === 'pending_review') {
      events.push({
        title: 'Withdrawal submitted for review',
        detail: `${amount || '0'} ${asset} transfer request is pending compliance review.`,
        status: 'Pending review',
      })
    }

    return events
  }, [asset, amount, securityCheckRun, status])

  function handleSecurityCheck() {
    setSecurityCheckRun(true)
  }

  function handleSubmitReview() {
    if (!canSubmit) return
    setSecurityCheckRun(true)
    setStatus('pending_review')
  }

  function handleReset() {
    setAsset('BTC')
    setNetwork('Bitcoin')
    setAddress('')
    setAmount('')
    setStatus('draft')
    setSecurityCheckRun(false)
  }

  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">External withdrawals</p>
            <h1>External wallet transfer</h1>
            <p>
              Simulate a controlled withdrawal flow from the internal digital
              assets wallet to a personal external wallet.
            </p>
          </div>

          <div className="security-badge">
            <span
              className={status === 'pending_review' ? 'warning-dot' : 'status-dot'}
            ></span>
            {status === 'pending_review' ? 'Pending review' : 'Draft'}
          </div>
        </section>

        <DigitalAssetsSubnav />

        <section className="content-grid">
          <div className="left-column">
            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Transfer request</p>
                  <h2>Withdrawal details</h2>
                </div>
                <span className="module-tag">Simulation</span>
              </div>

              <div className="form-grid">
                <label>
                  Asset
                  <select
                    value={asset}
                    onChange={(event) => {
                      const nextAsset = event.target.value
                      setAsset(nextAsset)
                      setNetwork(nextAsset === 'BTC' ? 'Bitcoin' : 'Ethereum')
                    }}
                  >
                    <option value="BTC">BTC — Bitcoin</option>
                    <option value="ETH">ETH — Ethereum</option>
                  </select>
                </label>

                <label>
                  Network
                  <select
                    value={network}
                    onChange={(event) => setNetwork(event.target.value)}
                  >
                    {asset === 'BTC' ? (
                      <option value="Bitcoin">Bitcoin</option>
                    ) : (
                      <option value="Ethereum">Ethereum</option>
                    )}
                  </select>
                </label>

                <label>
                  Destination address
                  <input
                    value={address}
                    onChange={(event) => setAddress(event.target.value)}
                    placeholder={
                      asset === 'BTC'
                        ? 'Example: bc1q...'
                        : 'Example: 0x...'
                    }
                  />
                </label>

                <label>
                  Amount
                  <input
                    value={amount}
                    onChange={(event) => setAmount(event.target.value)}
                    placeholder={asset === 'BTC' ? '0.001 BTC' : '0.05 ETH'}
                  />
                </label>
              </div>

              <div className="withdrawal-preview">
                <div>
                  <p>Selected asset</p>
                  <strong>{asset}</strong>
                </div>
                <div>
                  <p>Network</p>
                  <strong>{network}</strong>
                </div>
                <div>
                  <p>Status</p>
                  <strong>
                    {status === 'pending_review' ? 'Pending review' : 'Draft'}
                  </strong>
                </div>
              </div>

              <div className="action-row">
                <button type="button" onClick={handleSecurityCheck}>
                  Run protection review
                </button>
                <button
                  type="button"
                  onClick={handleSubmitReview}
                  disabled={!canSubmit}
                >
                  Submit for review
                </button>
                <button
                  className="secondary-button"
                  type="button"
                  onClick={handleReset}
                >
                  Reset
                </button>
              </div>
            </Panel>

            <Panel>
              <div className="panel-header">
                <div>
                  <p className="eyebrow">Audit trail</p>
                  <h2>Withdrawal evidence timeline</h2>
                </div>
                <span className="module-tag">Deterministic log</span>
              </div>

              <div className="account-list">
                {auditEvents.map((event) => (
                  <article className="account-row" key={event.title}>
                    <div>
                      <h3>{event.title}</h3>
                      <p>{event.detail}</p>
                      <span>{event.status}</span>
                    </div>
                    <strong>{event.status}</strong>
                  </article>
                ))}
              </div>
            </Panel>
          </div>

          <aside className="right-column">
            <Panel className="risk-panel">
              <p className="eyebrow">Risk warning</p>
              <h2>Irreversible transfer</h2>
              <p>
                Blockchain transfers cannot be reversed. Always verify the
                address, network, and amount before continuing.
              </p>
            </Panel>

            <Panel>
              <p className="eyebrow">Review status</p>
              <h2>Transfer protection</h2>
              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  Strong authentication active
                </div>
                <div>
                  <span className={securityCheckRun ? 'status-dot' : 'warning-dot'}></span>
                  Address review {securityCheckRun ? 'completed' : 'required'}
                </div>
                <div>
                  <span className="warning-dot"></span>
                  External transfer review active
                </div>
                <div>
                  <span
                    className={
                      status === 'pending_review' ? 'warning-dot' : 'status-dot'
                    }
                  ></span>
                  {status === 'pending_review'
                    ? 'Manual review pending'
                    : 'No active withdrawal request'}
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="eyebrow">User protection</p>
              <h2>Before submitting</h2>
              <ul className="notification-list">
                <li>Confirm that the destination address belongs to you.</li>
                <li>Confirm that the selected network matches your wallet.</li>
                <li>Understand that external transfers are not reversible.</li>
                <li>Large or unusual withdrawals may require manual review.</li>
              </ul>
            </Panel>
          </aside>
        </section>

        <section className="disclaimer">
          Independent concept prototype. This page simulates an external wallet
          transfer flow and does not process real blockchain transactions.
        </section>
      </main>
    </div>
  )
}
