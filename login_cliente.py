from conexao import conectar_banco
import bcrypt


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))


def login_cliente():
    db = conectar_banco()
    cursor = db.cursor()

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute("SELECT id_cli, cpf_cli, nome_cli, email_cli, senha_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece FROM cliente WHERE email_cli = %s", (email,))
    cliente = cursor.fetchone()

    if cliente:
        senha_hash = cliente[4]
        if verificar_senha(senha, senha_hash):

            print(f"Login bem-sucedido! Bem-vindo(a), {cliente[2]}")

            if cliente[6] == "Sousa" or cliente[7] or cliente[8]:
                print(
                    "Você é cliente especial e terá 10% de desconto nas suas compras :)!")
            return email
        else:
            print("Senha incorreta!")
            return None
    else:
        print("Login inexistente!")
        return None

    cursor.close()
    db.close()
