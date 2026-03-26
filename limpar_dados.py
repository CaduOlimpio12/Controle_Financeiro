import sqlite3
import os

DB_NAME = "database.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def apagar_tudo():
    """Apaga todas as transações do banco de dados."""
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transacoes")
        conn.commit()
        conn.close()
        print("✅ Sucesso: Todas as transações foram apagadas. Seu saldo agora é R$ 0,00.")
    except Exception as e:
        print(f"❌ Erro ao apagar tudo: {e}")

def apagar_ultima():
    """Apaga apenas a última transação inserida."""
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transacoes WHERE id = (SELECT MAX(id) FROM transacoes)")
        conn.commit()
        conn.close()
        print("✅ Sucesso: A última transação foi removida.")
    except Exception as e:
        print(f"❌ Erro ao apagar última transação: {e}")

if __name__ == "__main__":
    print("--- Utilitário de Limpeza de Dados ---")
    print("1 - Apagar TUDO (Zerar o sistema)")
    print("2 - Apagar apenas a ÚLTIMA transação")
    
    opcao = input("\nEscolha uma opção (1 ou 2): ")
    
    if opcao == "1":
        confirmar = input("Tem certeza que deseja apagar TUDO? (s/n): ")
        if confirmar.lower() == 's':
            apagar_tudo()
    elif opcao == "2":
        apagar_ultima()
    else:
        print("Opção inválida.")
