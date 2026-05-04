import { TopBar } from '../components/TopBar'
import { Panel } from '../components/Panel'

export function WithdrawalsPage() {
  return (
    <div className="bank-shell">
      <TopBar userName="Claudio Demo" />

      <main className="page">
        <section className="welcome-card">
          <div>
            <p className="eyebrow">External withdrawals</p>
            <h1>External wallet transfer</h1>
            <p>
              Simulate a controlled withdrawal flow from the internal wallet to
              a personal external wallet.
            </p>
          </div>

          <div className="security-badge">
            <span className="warning-dot"></span>
            Review required
          </div>
        </section>

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
                  <select>
                    <option>BTC — Bitcoin</option>
                    <option>ETH — Ethereum</option>
                  </select>
                </label>

                <label>
                  Network
                  <select>
                    <option>Bitcoin</option>
                    <option>Ethereum</option>
                  </select>
                </label>

                <label>
                  Destination address
                  <input placeholder="Enter external wallet address" />
                </label>

                <label>
                  Amount
                  <input placeholder="0.001 BTC" />
                </label>
              </div>

              <div className="action-row">
                <button type="button">Run security check</button>
                <button className="secondary-button" type="button">
                  Save draft
                </button>
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
              <h2>Compliance checks</h2>
              <div className="check-list">
                <div>
                  <span className="status-dot"></span>
                  KYC verified
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Address review required
                </div>
                <div>
                  <span className="warning-dot"></span>
                  Security delay may apply
                </div>
              </div>
            </Panel>
          </aside>
        </section>
      </main>
    </div>
  )
}