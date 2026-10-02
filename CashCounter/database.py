import sqlite3
from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / 'CashCounter.db'

def get_connection():
    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    conn.execute('PRAGMA foreign_keys = ON')

    return conn

def create_tables():
    conn = get_connection()
    try:
        with conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
            )
        ''')
            conn.execute('''
            CREATE TABLE IF NOT EXISTS subscription(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            amount INTEGER NOT NULL CHECK (amount > 0),
            period TEXT NOT NULL CHECK (period IN ("monthly", "yearly")),
            next_payment TEXT NOT NULL,
            payment_day INTEGER NOT NULL CHECK(payment_day BETWEEN 1 AND 31),
            
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')
    finally:
        conn.close()