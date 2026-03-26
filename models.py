# ==========================
# models.py
# ==========================

from database import conectar


def inserir_transacao(pessoa, tipo, valor, categoria, data):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transacoes (pessoa, tipo, valor, categoria, data)
    VALUES (?, ?, ?, ?, ?)
    """, (pessoa, tipo, valor, categoria, data))

    conn.commit()
    conn.close()