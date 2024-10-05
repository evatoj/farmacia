from conexao import conectar_banco
import bcrypt


def gerar_senha_criptografada(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')


def cadastrar_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    cpf = input("Digite o CPF do vendedor (somente números): ")
    nome = input("Digite o nome do vendedor: ")
    email = input("Digite o email do vendedor: ")
    senha = input("Digite a senha do vendedor: ")
    telefone = input("Digite o telefone do vendedor: ")

    senha_criptografada = gerar_senha_criptografada(senha)

    cursor.execute("""
        INSERT INTO vendedor (cpf_ven, nome_ven, email_ven, senha_ven, telefone_ven)
        VALUES (%s, %s, %s, %s, %s)
    """, (cpf, nome, email, senha_criptografada, telefone))

    db.commit()
    print("Vendedor contratado com sucesso!")

    cursor.close()
    db.close()
