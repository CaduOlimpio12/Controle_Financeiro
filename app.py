# ==========================
# app.py (COMPLETO E CORRIGIDO)
# ==========================

from flask import Flask, request, jsonify, render_template, redirect, url_for, session

from database import criar_tabela, conectar
from models import inserir_transacao
from chatbot import responder
from auth import validar_login
from metrics import saldo_total, gastos_ultimos_30_dias, gastos_mes_atual, rendimento_cdi

app = Flask(__name__)
app.secret_key = "segredo123"


# ==========================
# LOGIN
# ==========================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if validar_login(username, password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', erro="Login inválido")

    return render_template('login.html')


# ==========================
# HOME
# ==========================
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('index.html', user=session['user'])


# ==========================
# LOGOUT
# ==========================
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ==========================
# ADICIONAR TRANSAÇÃO
# ==========================
@app.route('/add', methods=['POST'])
def add():
    if 'user' not in session:
        return jsonify({"erro": "não autorizado"}), 401

    data = request.get_json()

    inserir_transacao(
        data.get('pessoa'),
        data.get('tipo'),
        data.get('valor'),
        data.get('categoria'),
        data.get('data')
    )

    return jsonify({"status": "ok"})


# ==========================
# CHATBOT
# ==========================
@app.route('/chat', methods=['POST'])
def chat():
    if 'user' not in session:
        return jsonify({"erro": "não autorizado"}), 401

    data = request.get_json()
    pergunta = data.get('pergunta', '')

    resposta = responder(pergunta)

    return jsonify({"resposta": resposta})


# ==========================
# MÉTRICAS
# ==========================
@app.route('/metrics', methods=['GET'])
def metrics():
    if 'user' not in session:
        return jsonify({"erro": "não autorizado"}), 401

    return jsonify({
        "saldo_total": saldo_total(),
        "gastos_ultimos_30_dias": gastos_ultimos_30_dias(),
        "gastos_mes_atual": gastos_mes_atual(),
        "rendimento_cdi": rendimento_cdi(saldo_total())
    })


# ==========================
# LIMPAR TRANSAÇÕES
# ==========================
@app.route('/clear', methods=['POST'])
def clear():
    if 'user' not in session:
        return jsonify({"erro": "não autorizado"}), 401

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transacoes")
        conn.commit()
        conn.close()
        return jsonify({"status": "ok", "mensagem": "Todas as transações foram apagadas com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# ==========================
# START
# ==========================
if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
