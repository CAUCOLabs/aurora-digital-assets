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

export function DigitalAssetRow({ asset }: DigitalAssetRowProps) {
  return (
    <article className="asset-row">
      <div className="asset-symbol">{asset.symbol}</div>
      <div>
        <h3>{asset.asset}</h3>
        <p>
          <PrivacyAmount
            value={asset.balance}
            label={`${asset.asset} balance`}
          />
        </p>
      </div>
      <strong>
        <PrivacyAmount value={asset.value} label={`${asset.asset} value`} />
      </strong>
    </article>
  )
}
