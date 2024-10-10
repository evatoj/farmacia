from conexao import conectar_banco
import bcrypt


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))


def login_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    try:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        cursor.execute(
            "SELECT id_ven, cpf_ven, nome_ven, senha_ven, status_ven FROM vendedor WHERE email_ven = %s", (email,))
        vendedor = cursor.fetchone()

        if vendedor:
            id_ven = vendedor[0]
            cpf_ven = vendedor[1]
            nome_ven = vendedor[2]
            senha_hash = vendedor[3]
            status_ven = vendedor[4]

            if status_ven == 0:
                print("Este vendedor foi demitido e não pode acessar o sistema.")
                return None

            if verificar_senha(senha, senha_hash):
                print(f"Login bem-sucedido! Bem-vindo(a), vendedor {nome_ven}")
                return id_ven
            else:
                print("Senha incorreta!")
                return None
        else:
            print("Login inexistente!")
            return None
    finally:
        cursor.close()
        db.close()
