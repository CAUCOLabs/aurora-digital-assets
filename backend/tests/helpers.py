import asyncio
import json
import tempfile
from pathlib import Path
from typing import Any

from app.db import database
from app.storage import sqlite_store


TEST_ROOT = Path(tempfile.mkdtemp(prefix="aurora-backend-tests-"))
database.DATABASE_PATH = TEST_ROOT / "aurora.db"
sqlite_store.DATABASE_PATH = TEST_ROOT / "data" / "aurora_demo.db"

database.initialize_database()
sqlite_store.init_db()

from app.main import app  # noqa: E402


def request_json(
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
) -> tuple[int, Any]:
    return asyncio.run(_request_json(method, path, payload))


async def _request_json(
    method: str,
    path: str,
    payload: dict[str, Any] | None,
) -> tuple[int, Any]:
    body = json.dumps(payload).encode("utf-8") if payload is not None else b""
    response_status = 500
    response_body = bytearray()

    scope = {
        "type": "http",
        "asgi": {"version": "3.0", "spec_version": "2.3"},
        "http_version": "1.1",
        "method": method,
        "scheme": "http",
        "path": path,
        "raw_path": path.encode("ascii"),
        "query_string": b"",
        "headers": [
            (b"host", b"testserver"),
            (b"content-type", b"application/json"),
        ],
        "client": ("127.0.0.1", 50000),
        "server": ("testserver", 80),
    }

    receive_complete = False

    async def receive() -> dict[str, Any]:
        nonlocal receive_complete
        if receive_complete:
            return {"type": "http.disconnect"}
        receive_complete = True
        return {
            "type": "http.request",
            "body": body,
            "more_body": False,
        }

    async def send(message: dict[str, Any]) -> None:
        nonlocal response_status
        if message["type"] == "http.response.start":
            response_status = message["status"]
        elif message["type"] == "http.response.body":
            response_body.extend(message.get("body", b""))

    await app(scope, receive, send)
    if not response_body:
        return response_status, None
    return response_status, json.loads(response_body.decode("utf-8"))
