import { PrivacyAmount } from './PrivacyAmount'

type DigitalAsset = {
  asset: string
  symbol: string
  balance: string
  value: string
}

type DigitalAssetRowProps = {
  asset: DigitalAsset
}

function isSensitiveAmount(value: string) {
  return /\d/.test(value)
}

export function DigitalAssetRow({ asset }: DigitalAssetRowProps) {
  return (
    <article className="asset-row">
      <div className="asset-symbol">{asset.symbol}</div>
      <div>
        <h3>{asset.asset}</h3>
        <p>
          {isSensitiveAmount(asset.balance) ? (
            <PrivacyAmount
              value={asset.balance}
              label={`${asset.asset} balance`}
            />
          ) : (
            asset.balance
          )}
        </p>
      </div>
      <strong>
        {isSensitiveAmount(asset.value) ? (
          <PrivacyAmount value={asset.value} label={`${asset.asset} value`} />
        ) : (
          asset.value
        )}
      </strong>
    </article>
  )
}
