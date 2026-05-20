from pydantic import BaseModel


class BankAccount(BaseModel):
    id: str
    name: str
    owner: str
    type: str
    iban: str
    bic: str
    bookBalance: str
    availableBalance: str
    reservedCardPayments: str
    status: str


class BankTransaction(BaseModel):
    id: str
    title: str
    detail: str
    accountName: str
    amount: str
    status: str


class ConnectedDigitalAssetBalance(BaseModel):
    id: str
    name: str
    balance: str
    detail: str
    value: str
