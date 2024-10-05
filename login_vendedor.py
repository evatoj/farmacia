from conexao import conectar_banco
import bcrypt


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))


def login_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute("SELECT * FROM vendedor WHERE email_ven = %s", (email,))
    vendedor = cursor.fetchone()

    if vendedor:
        senha_hash = vendedor[3]
        if verificar_senha(senha, senha_hash):
            print(f"Login bem-sucedido! Bem-vindo(a), {vendedor[1]}")
            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Login inexistente!")
        return False

    cursor.close()
    db.close()
