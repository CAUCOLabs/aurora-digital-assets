# Backend Agent

## Responsibility

Implement the simulated backend for Aurora Digital Assets.

## Stack

- Python
- FastAPI
- Pydantic
- SQLite or local JSON mock data

## Required Domains

- Banking accounts
- Crypto wallet balances
- Buy/Sell simulation
- External withdrawal simulation
- Compliance checks
- Audit log
- Reports

## Rules

- Do not connect to real banking APIs.
- Do not connect to real custody providers.
- Do not store real secrets.
- Use mock data only.
- Keep business logic deterministic and auditable.

## First Milestone

Create FastAPI endpoints that serve mock banking, wallet, market, compliance, and report data.