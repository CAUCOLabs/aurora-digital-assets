import { PrivacyAmount } from './PrivacyAmount'

type Account = {
  name: string
  type: string
  balance: string
  maskedIban: string
}

type AccountRowProps = {
  account: Account
}

export function AccountRow({ account }: AccountRowProps) {
  return (
    <article className="account-row">
      <div>
        <h3>{account.name}</h3>
        <p>{account.type}</p>
        <span>{account.maskedIban}</span>
      </div>
      <strong>
        <PrivacyAmount value={account.balance} label={`${account.name} balance`} />
      </strong>
    </article>
  )
}
