from conexao import conectar_banco
import bcrypt


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))


def login_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute(
        "SELECT id_ven, cpf_ven, nome_ven, senha_ven FROM vendedor WHERE email_ven = %s", (email,))
    vendedor = cursor.fetchone()

    if vendedor:
        id_ven = vendedor[0]
        cpf_ven = vendedor[1]
        nome_ven = vendedor[2]
        senha_hash = vendedor[3]

        if verificar_senha(senha, senha_hash):
            print("\n=== Login bem-sucedido ===")
            print(f"ID: {id_ven}")
            print(f"CPF: {cpf_ven}")
            print(f"Bem-vindo(a), {nome_ven}!")
            return id_ven
        else:
            print("Senha incorreta!")
            return None
    else:
        print("Email inexistente!")
        return None

    cursor.close()
    db.close()
