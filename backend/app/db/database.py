import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parents[2] / "aurora.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """Create local prototype persistence tables if they do not exist."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_events (
                event_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                module TEXT NOT NULL,
                action_type TEXT NOT NULL,
                status TEXT NOT NULL,
                risk_level TEXT,
                decision TEXT,
                reasons TEXT NOT NULL,
                case_id TEXT,
                user_message TEXT
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS bank_customers (
                customer_id TEXT PRIMARY KEY,
                bank_user_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                pin TEXT NOT NULL,
                account_id TEXT NOT NULL,
                relationship_status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS auth_challenges (
                challenge_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS bank_sessions (
                session_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO bank_customers (
                customer_id,
                bank_user_id,
                name,
                pin,
                account_id,
                relationship_status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "CUST-DA-2026-001",
                "12345678",
                "Claudio Demo",
                "1234",
                "aurora-current",
                "Active",
                "2026-01-01T00:00:00+00:00",
            ),
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS review_cases (
                case_id TEXT PRIMARY KEY,
                created_at TEXT NOT NULL,
                case_type TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL,
                risk_level TEXT NOT NULL,
                reasons TEXT NOT NULL,
                customer TEXT NOT NULL,
                action_type TEXT NOT NULL,
                asset TEXT NOT NULL,
                amount REAL NOT NULL,
                network TEXT NOT NULL,
                destination_address TEXT NOT NULL,
                wallet_type TEXT NOT NULL,
                reviewer_decision TEXT,
                reviewer_notes TEXT
            )
            """
        )
