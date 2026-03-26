# ==========================
# auth.py (LOGIN SIMPLES)
# ==========================

usuarios = {
    "carlos": "admin123",
    "camilly": "admin123"
}


def validar_login(username, password):
    if username in usuarios and usuarios[username] == password:
        return True
    return False