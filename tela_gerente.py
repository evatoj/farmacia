from conexao import conectar_banco
import bcrypt
import re


def tela_gerente():
    while True:
        print("\n=== Área do Gerente ===")
        print("1. Listar Vendedores Ativos")
        print("2. Listar Vendedores Demitidos")
        print("3. Listar Clientes")
        print("4. Contratar Vendedor")
        print("5. Demitir Vendedor")
        print("6. Recontratar Vendedor")
        print("7. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_vendedores_ativos()
        elif opcao == '2':
            listar_vendedores_demitidos()
        elif opcao == '3':
            listar_clientes()
        elif opcao == '4':
            cadastrar_vendedor()
        elif opcao == '5':
            demitir_vendedor()
        elif opcao == '6':
            recontratar_vendedor()
        elif opcao == '7':
            print("Retornando ao Menu Inicial...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")


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
        print("Este CPF já está cadastrado como vendedor.")
        return False

    cursor.execute("SELECT cpf_cli FROM cliente WHERE cpf_cli = %s", (cpf,))
    if cursor.fetchone():
        print("Este CPF já está cadastrado como cliente.")
        return False

    return True


def email_unico(cursor, email):
    cursor.execute(
        "SELECT email_ven FROM vendedor WHERE email_ven = %s", (email,))
    if cursor.fetchone():
        print("Este email já está cadastrado como vendedor.")
        return False

    cursor.execute(
        "SELECT email_cli FROM cliente WHERE email_cli = %s", (email,))
    if cursor.fetchone():
        print("Este email já está cadastrado como cliente.")
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
    cidade = input("Digite a cidade do vendedor: ")

    senha_criptografada = gerar_senha_criptografada(senha)

    cursor.execute(""" 
        INSERT INTO vendedor (cpf_ven, nome_ven, email_ven, senha_ven, telefone_ven, cidade_ven, status_ven) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) 
    """, (cpf, nome, email, senha_criptografada, telefone, cidade, 1))  # status_ven = 1 (ativo)

    db.commit()
    print("Vendedor contratado com sucesso!")

    cursor.close()
    db.close()


def demitir_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    id_ven = input("Digite o ID do vendedor a ser demitido: ")

    cursor.execute(
        "SELECT * FROM vendedor WHERE id_ven = %s AND status_ven = 1", (id_ven,))
    vendedor = cursor.fetchone()

    if vendedor:
        cursor.execute(
            "UPDATE vendedor SET status_ven = 0 WHERE id_ven = %s", (id_ven,))
        db.commit()
        print("Vendedor demitido com sucesso!")
    else:
        print("Vendedor não encontrado ou já demitido.")

    cursor.close()
    db.close()


def recontratar_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    id_ven = input("Digite o ID do vendedor a ser recontratado: ")

    cursor.execute(
        "SELECT * FROM vendedor WHERE id_ven = %s AND status_ven = 0", (id_ven,))
    vendedor = cursor.fetchone()

    if vendedor:
        cursor.execute(
            "UPDATE vendedor SET status_ven = 1 WHERE id_ven = %s", (id_ven,))
        db.commit()
        print("Vendedor recontratado com sucesso!")
    else:
        print("Vendedor não encontrado ou já está ativo.")

    cursor.close()
    db.close()


def listar_vendedores_ativos():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_ven, nome_ven, email_ven, cidade_ven, telefone_ven FROM vendedor WHERE status_ven = 1")
    vendedores = cursor.fetchall()

    print("\nLista de Vendedores Ativos:")
    if vendedores:
        for vendedor in vendedores:
            print(f"ID: {vendedor[0]}, Nome: {vendedor[1]}, Email: {
                  vendedor[2]}, Cidade: {vendedor[3]}, Telefone: {vendedor[4]}")
    else:
        print("Nenhum vendedor ativo cadastrado.")

    cursor.close()
    db.close()


def listar_vendedores_demitidos():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_ven, nome_ven, email_ven, cidade_ven, telefone_ven FROM vendedor WHERE status_ven = 0")
    vendedores = cursor.fetchall()

    print("\nLista de Vendedores Demitidos:")
    if vendedores:
        for vendedor in vendedores:
            print(f"ID: {vendedor[0]}, Nome: {vendedor[1]}, Email: {
                  vendedor[2]}, Cidade: {vendedor[3]}, Telefone: {vendedor[4]}")
    else:
        print("Nenhum vendedor demitido.")

    cursor.close()
    db.close()


def listar_clientes():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_cli, nome_cli, email_cli, cidade_cli, telefone_cli FROM cliente")
    clientes = cursor.fetchall()

    print("\nLista de Clientes:")
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {
                  cliente[2]}, Cidade: {cliente[3]}, Telefone: {cliente[4]}")
    else:
        print("Nenhum cliente cadastrado.")

    cursor.close()
    db.close()
