from datetime import datetime, timedelta, timezone
from sqlite3 import Row
from uuid import uuid4

from app.db.database import get_connection
from app.schemas.auth import (
    AuthCustomerInfo,
    BankLoginRequest,
    BankLoginResponse,
    BankSessionResponse,
    LogoutResponse,
    MobileApprovalResponse,
)


class AuthService:
    """Implements simulated banking access challenges and sessions."""

    def login(self, request: BankLoginRequest) -> BankLoginResponse:
        with get_connection() as connection:
            customer = connection.execute(
                """
                SELECT customer_id, name, account_id, relationship_status
                FROM bank_customers
                WHERE bank_user_id = ? AND pin = ?
                """,
                (request.bank_user_id, request.pin),
            ).fetchone()

            if customer is None:
                return BankLoginResponse(
                    status="rejected",
                    challenge_id=None,
                    message="Invalid bank-issued credentials.",
                )

            challenge_id = f"CHALLENGE-{uuid4().hex}"
            created_at = datetime.now(timezone.utc)
            connection.execute(
                """
                INSERT INTO auth_challenges (
                    challenge_id,
                    customer_id,
                    status,
                    created_at,
                    expires_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    challenge_id,
                    customer["customer_id"],
                    "pending_mobile_approval",
                    created_at.isoformat(),
                    (created_at + timedelta(minutes=2)).isoformat(),
                ),
            )

        return BankLoginResponse(
            status="pending_mobile_approval",
            challenge_id=challenge_id,
            customer=self._customer_info(customer),
            message="Credentials accepted. Mobile key approval required.",
        )

    def process_mobile_approval(
        self,
        challenge_id: str,
        approved: bool,
    ) -> MobileApprovalResponse:
        with get_connection() as connection:
            challenge = connection.execute(
                """
                SELECT
                    challenge.challenge_id,
                    challenge.customer_id,
                    challenge.status,
                    challenge.expires_at,
                    customer.name,
                    customer.account_id,
                    customer.relationship_status
                FROM auth_challenges AS challenge
                JOIN bank_customers AS customer
                    ON customer.customer_id = challenge.customer_id
                WHERE challenge.challenge_id = ?
                """,
                (challenge_id,),
            ).fetchone()

            if not self._can_approve(challenge):
                return MobileApprovalResponse(
                    status="rejected",
                    session_id=None,
                    redirect_to="/bank-login",
                    message="Mobile key approval request is not available.",
                )

            if not approved:
                connection.execute(
                    """
                    UPDATE auth_challenges
                    SET status = ?
                    WHERE challenge_id = ?
                    """,
                    ("rejected", challenge_id),
                )
                return MobileApprovalResponse(
                    status="rejected",
                    session_id=None,
                    customer=self._customer_info(challenge),
                    redirect_to="/bank-login",
                    message="Mobile key approval rejected.",
                )

            connection.execute(
                """
                UPDATE auth_challenges
                SET status = ?
                WHERE challenge_id = ?
                """,
                ("approved", challenge_id),
            )
            session_id = f"SESSION-{uuid4().hex}"
            created_at = datetime.now(timezone.utc)
            connection.execute(
                """
                INSERT INTO bank_sessions (
                    session_id,
                    customer_id,
                    status,
                    created_at,
                    expires_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    session_id,
                    challenge["customer_id"],
                    "active",
                    created_at.isoformat(),
                    (created_at + timedelta(minutes=30)).isoformat(),
                ),
            )

        return MobileApprovalResponse(
            status="authenticated",
            session_id=session_id,
            customer=self._customer_info(challenge),
            redirect_to="/",
            message="Strong authentication completed. Banking session established.",
        )

    def get_session(self, session_id: str) -> BankSessionResponse:
        with get_connection() as connection:
            session = connection.execute(
                """
                SELECT
                    session.status,
                    session.expires_at,
                    customer.customer_id,
                    customer.name,
                    customer.account_id,
                    customer.relationship_status
                FROM bank_sessions AS session
                JOIN bank_customers AS customer
                    ON customer.customer_id = session.customer_id
                WHERE session.session_id = ?
                """,
                (session_id,),
            ).fetchone()

        if session is None or not self._is_active_session(session):
            return BankSessionResponse(authenticated=False)

        return BankSessionResponse(
            authenticated=True,
            customer_id=session["customer_id"],
            customer_name=session["name"],
            account_id=session["account_id"],
            relationship_status=session["relationship_status"],
        )

    def logout(self, session_id: str) -> LogoutResponse:
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE bank_sessions
                SET status = ?
                WHERE session_id = ?
                """,
                ("logged_out", session_id),
            )

        return LogoutResponse(
            status="logged_out",
            message="Simulated banking session logged out.",
        )

    def _can_approve(self, challenge: Row | None) -> bool:
        if challenge is None or challenge["status"] != "pending_mobile_approval":
            return False

        return datetime.fromisoformat(challenge["expires_at"]) > datetime.now(
            timezone.utc
        )

    def _is_active_session(self, session: Row) -> bool:
        return session["status"] == "active" and datetime.fromisoformat(
            session["expires_at"]
        ) > datetime.now(timezone.utc)

    def _customer_info(self, customer: Row) -> AuthCustomerInfo:
        return AuthCustomerInfo(
            customer_id=customer["customer_id"],
            customer_name=customer["name"],
            account_id=customer["account_id"],
            relationship_status=customer["relationship_status"],
        )


auth_service = AuthService()
