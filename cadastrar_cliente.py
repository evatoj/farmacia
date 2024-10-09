from conexao import conectar_banco
import bcrypt
import re


def gerar_senha_criptografada(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')


def solicitar_input_valido(pergunta):
    while True:
        resposta = input(pergunta).lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Entrada inválida! Por favor, digite 's' para sim ou 'n'.")


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
    cursor.execute("SELECT cpf_cli FROM cliente WHERE cpf_cli = %s", (cpf,))
    if cursor.fetchone():
        print("Este CPF já está cadastrado.")
        return False
    return True


def email_unico(cursor, email):
    cursor.execute(
        "SELECT email_cli FROM cliente WHERE email_cli = %s", (email,))
    if cursor.fetchone():
        print("Este email já está cadastrado.")
        return False
    return True


def cadastrar_cliente():
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        cpf = input("Digite o CPF do cliente (somente números): ")
        if validar_cpf(cpf) and cpf_unico(cursor, cpf):
            break

    while True:
        email = input("Digite o email do cliente: ")
        if validar_email(email) and email_unico(cursor, email):
            break

    nome = input("Digite o nome do cliente: ")
    senha = input("Digite a senha do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cidade = input("Digite a cidade do cliente: ")

    torce_flamengo = solicitar_input_valido(
        "O cliente torce para o Flamengo? (s/n): ")
    assiste_one_piece = solicitar_input_valido(
        "O cliente assiste One Piece? (s/n): ")

    senha_criptografada = gerar_senha_criptografada(senha)

    cursor.execute("""
        INSERT INTO cliente (cpf_cli, nome_cli, email_cli, senha_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (cpf, nome, email, senha_criptografada, telefone, cidade, torce_flamengo, assiste_one_piece))

    db.commit()
    print("Cliente cadastrado com sucesso!")

    cursor.close()
    db.close()
