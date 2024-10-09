from conexao import conectar_banco
import bcrypt
import re


def gerar_senha_criptografada(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')


def validar_cpf(cpf):
    if len(cpf) != 11:
        print("O CPF deve conter exatamente 11 dígitos.")
        return False
    if not cpf.isdigit():
        print("O CPF deve conter apenas números.")
        return False
    return True


def validar_email(email):

    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(padrao_email, email):
        print("Formato de email inválido.")
        return False
    return True


def cpf_unico(cursor, cpf):
    cursor.execute("SELECT cpf_ven FROM vendedor WHERE cpf_ven = %s", (cpf,))
    if cursor.fetchone():
        print("Este CPF já está cadastrado.")
        return False
    return True


def email_unico(cursor, email):
    cursor.execute(
        "SELECT email_ven FROM vendedor WHERE email_ven = %s", (email,))
    if cursor.fetchone():
        print("Este email já está cadastrado.")
        return False
    return True


def cadastrar_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        cpf = input("Digite o CPF do vendedor (somente números): ")
        if validar_cpf(cpf) and cpf_unico(cursor, cpf):
            break

    while True:
        email = input("Digite o email do vendedor: ")
        if validar_email(email) and email_unico(cursor, email):
            break

    nome = input("Digite o nome do vendedor: ")
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
