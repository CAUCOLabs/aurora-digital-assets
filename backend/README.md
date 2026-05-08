# Aurora Digital Assets Backend

FastAPI backend skeleton for the Aurora Digital Assets bank-integrated crypto wallet framework prototype.

## Purpose

This backend is structured for future banking, custody, compliance, audit, and reporting integrations. The current implementation is intentionally minimal and simulated: it exposes a health endpoint only and does not connect to real bank APIs, custody providers, crypto services, AML providers, or blockchain networks.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Health Endpoint

```text
http://localhost:8000/api/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "aurora-digital-assets-backend",
  "version": "0.1"
}
```

## Prototype Disclaimer

Aurora Digital Assets is a concept prototype. This backend uses simulated behavior only. It does not process real financial transactions, store real customer data, manage private keys, perform AML screening, or execute blockchain operations.
