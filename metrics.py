# ==========================
# metrics.py
# ==========================

from database import conectar
from datetime import datetime, timedelta


def saldo_total():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(valor)
    FROM transacoes
    WHERE LOWER(tipo)='receita'
    """)

    result = cursor.fetchone()[0]
    conn.close()

    return result or 0


def gastos_ultimos_30_dias():
    conn = conectar()
    cursor = conn.cursor()

    data_limite = datetime.now() - timedelta(days=30)

    cursor.execute("""
    SELECT SUM(valor) FROM transacoes
    WHERE LOWER(tipo)='despesa' AND data >= ?
    """, (data_limite,))

    result = cursor.fetchone()[0]
    conn.close()

    return result or 0


def gastos_mes_atual():
    conn = conectar()
    cursor = conn.cursor()

    mes_atual = datetime.now().strftime('%m')

    cursor.execute("""
    SELECT SUM(valor) FROM transacoes
    WHERE LOWER(tipo)='despesa' AND strftime('%m', data) = ?
    """, (mes_atual,))

    result = cursor.fetchone()[0]
    conn.close()

    return result or 0


def rendimento_cdi(valor, taxa_anual=0.1365, dias=30):
    taxa_diaria = (1 + taxa_anual) ** (1/252) - 1
    return valor * (1 + taxa_diaria) ** dias
