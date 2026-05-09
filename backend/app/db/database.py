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
