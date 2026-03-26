# ==========================
# chatbot.py (SEM API)
# ==========================

from metrics import saldo_total, gastos_ultimos_30_dias, gastos_mes_atual, rendimento_cdi


def responder(pergunta):
    pergunta = pergunta.lower()

    saldo = saldo_total()
    gastos_30 = gastos_ultimos_30_dias()
    gastos_mes = gastos_mes_atual()
    rendimento = rendimento_cdi(saldo)

    if "saldo" in pergunta:
        return f"O saldo atual do casal é R$ {saldo:.2f}"

    elif "30 dias" in pergunta:
        return f"Nos últimos 30 dias vocês gastaram R$ {gastos_30:.2f}"

    elif "mês" in pergunta:
        return f"Neste mês vocês gastaram R$ {gastos_mes:.2f}"

    elif "cdi" in pergunta or "rendimento" in pergunta:
        return f"O saldo renderia aproximadamente R$ {rendimento:.2f} em 30 dias a 100% do CDI"

    elif "gastei" in pergunta or "gastamos" in pergunta:
        return f"Gasto no mês atual: R$ {gastos_mes:.2f}"

    else:
        return "Não entendi sua pergunta. Tente algo como: saldo, gastos do mês ou últimos 30 dias."
