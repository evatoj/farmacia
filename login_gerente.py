from conexao import conectar_banco
import bcrypt


def validar_login(email, senha):
    db = conectar_banco()
    cursor = db.cursor()

    try:
        cursor.execute(
            "SELECT senha_ger FROM gerente WHERE email_ger = %s", (email,))
        resultado = cursor.fetchone()

        if resultado:
            senha_armazenada = resultado[0]
            print(senha)
            print(senha_armazenada)
            # if bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada.encode('utf-8')):
            #     return True
            if senha == senha_armazenada:
                return True
        return False
    finally:
        cursor.close()
        db.close()


def login_gerente():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if validar_login(email, senha):
        print(f"Login bem-sucedido! Bem-vindo, Boss")
        return True
    else:
        print("Email ou senha inválidos.")
        return False
