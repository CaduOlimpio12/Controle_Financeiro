# ==========================
# database.py
# ==========================

import sqlite3
from config import DB_NAME


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa TEXT,
        tipo TEXT,
        valor REAL,
        categoria TEXT,
        data DATE
    )
    """)

    conn.commit()
    conn.close()