import hashlib
import sqlite3
import secrets
import hmac

from database import get_connection

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        600_600
    ).hex()

def register_user(username, password):
    username = username.strip()

    if len(username) < 3:
        raise ValueError("Логин должен содержать минимум 3 символа")
    elif len(password) < 8:
        raise ValueError("Пароль должен содержать минимум 8 символов")

    salt = secrets.token_hex(16)
    password_hash = hash_password(password, salt)

    conn = get_connection()
    try:
        with conn:
            conn.execute(
                """
                INSERT INTO users (user_name, password_hash, salt)
                VALUES (?, ?, ?)
                """,
                (username, password_hash, salt)
            )
    except sqlite3.InternalError:
        raise ValueError("Этот логин уже занят") from None
    finally:
        conn.close()

def login(username, password):
    conn = get_connection()
    try:
        user = conn.execute(
            """
            SELECT * FROM users
            WHERE user_name = ?
            """, (username.strip(),)
        ).fetchone()
    finally:
        conn.close()

    if user is None:
        raise ValueError("Неверный логин или пароль.")

    entered_hash = hash_password(password, user["salt"])

    if not hmac.compare_digest(user["password_hash"], entered_hash):
        raise ValueError("Неверный логин или пароль")

    return{
        "id": user["id"],
        "username": user["user_name"]
    }

