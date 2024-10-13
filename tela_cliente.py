from conexao import conectar_banco
from prettytable import PrettyTable


def tela_cliente(email):
    while True:
        print("\n=== Área do Cliente ===")
        print("1. Ver dados cadastrais")
        print("2. Buscar Medicamentos")
        print("3. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_dados_cadastrais(email)
        elif opcao == '2':
            buscar_medicamentos()
        elif opcao == '3':
            print("Retornando ao Menu Inicial...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")


def ver_dados_cadastrais(email):
    db = conectar_banco()
    cursor = db.cursor()

    cursor.execute(
        "SELECT id_cli, cpf_cli, nome_cli, email_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece "
        "FROM cliente WHERE email_cli = %s", (email,))
    cliente = cursor.fetchone()

    if cliente:
        print("\n=== Dados Cadastrais ===")
        print(f"ID: {cliente[0]}")
        print(f"CPF: {cliente[1]}")
        print(f"Nome: {cliente[2]}")
        print(f"Email: {cliente[3]}")
        print(f"Telefone: {cliente[4]}")
        print(f"Cidade: {cliente[5]}")

        if cliente[6]:
            print("Torce para o Flamengo: Sim")
        else:
            print("Torce para o Flamengo: Não")

        if cliente[7]:
            print("Assiste One Piece: Sim")
        else:
            print("Assiste One Piece: Não")
    else:
        print("Cliente não encontrado.")

    cursor.close()
    db.close()


def buscar_medicamentos():
    while True:
        print("\n=== Buscar Medicamentos ===")
        print("1. Listar Todos os Medicamentos Disponíveis")
        print("2. Buscar por Nome")
        print("3. Buscar por Preço Máximo")
        print("4. Buscar por Fabricante")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_todos_medicamentos()
        elif opcao == '2':
            nome_produto = input(
                "Digite o nome do produto que deseja buscar: ")
            buscar_por_nome(nome_produto)
        elif opcao == '3':
            preco_maximo = float(input("Digite o preço máximo: "))
            buscar_por_preco(preco_maximo)
        elif opcao == '4':
            fabricante = input("Digite o fabricante que deseja buscar: ")
            buscar_por_fabricante(fabricante)
        elif opcao == '5':
            print("Retornando à área do cliente...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")


def listar_todos_medicamentos():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_med, nome_med, fabricante, estoque, preco FROM estoque_disponivel")
    produtos = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]

    if produtos:
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            table.add_row([id_med, nome_med, fabricante, estoque, preco])
        print("\n=== Todos os Medicamentos Disponíveis ===")
        print(table)
    else:
        print("Nenhum medicamento disponível.")

    cursor.close()
    db.close()


def buscar_por_nome(nome_produto):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE nome_med LIKE %s",
                   ('%' + nome_produto + '%',))
    produtos = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]

    if produtos:
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            table.add_row([id_med, nome_med, fabricante, estoque, preco])
        print("\n=== Produtos Encontrados ===")
        print(table)
    else:
        print("Nenhum produto encontrado.")

    cursor.close()
    db.close()


def buscar_por_preco(preco_maximo):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE preco <= %s",
                   (preco_maximo,))
    produtos = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]

    if produtos:
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            table.add_row([id_med, nome_med, fabricante, estoque, preco])
        print("\n=== Produtos Encontrados com Preço Máximo ===")
        print(table)
    else:
        print("Nenhum produto encontrado com o preço máximo informado.")

    cursor.close()
    db.close()


def buscar_por_fabricante(fabricante):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE fabricante LIKE %s",
                   ('%' + fabricante + '%',))
    produtos = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]

    if produtos:
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            table.add_row([id_med, nome_med, fabricante, estoque, preco])
        print("\n=== Produtos Encontrados por Fabricante ===")
        print(table)
    else:
        print("Nenhum produto encontrado para o fabricante informado.")

    cursor.close()
    db.close()
