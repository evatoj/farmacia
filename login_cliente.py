from conexao import conectar_banco
import bcrypt


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))


def login_cliente():
    db = conectar_banco()
    cursor = db.cursor()

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute("SELECT * FROM cliente WHERE email_cli = %s", (email,))
    cliente = cursor.fetchone()

    if cliente:
        senha_hash = cliente[3]
        if verificar_senha(senha, senha_hash):
            print(f"Login bem-sucedido! Bem-vindo(a), {cliente[1]}")

            if cliente[5] == "Sousa" or cliente[6] or cliente[7]:
                print(
                    "Você é cliente especial e terá 10% de desconto nas suas compras :)!")

            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Login inexistente!")
        return False

    cursor.close()
    db.close()
