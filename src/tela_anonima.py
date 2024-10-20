from conexao import conectar_banco
from prettytable import PrettyTable


def tela_anonima():
    while True:
        print("\n=== Navegação Anônima ===")
        print("1. Listar Medicamentos Disponíveis")
        print("2. Consultar Produtos")
        print("3. Listar Clientes")
        print("4. Listar Vendedores")
        print("5. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_medicamentos_disponiveis()
        elif opcao == '2':
            consultar_produtos()
        elif opcao == '3':
            listar_clientes()
        elif opcao == '4':
            listar_vendedores()
        elif opcao == '5':
            print("Retornando ao Menu Inicial...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")


def listar_medicamentos_disponiveis():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_med, nome_med, fabricante, estoque, preco FROM estoque_disponivel")
    produtos = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Fabricante",
                         "Estoque", "Preço (R$)"]

    if produtos:
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            table.add_row([id_med, nome_med, fabricante, estoque, preco])
        print("\n=== Medicamentos Disponíveis ===")
        print(table)
    else:
        print("Nenhum medicamento disponível.")

    cursor.close()
    db.close()


def consultar_produtos():
    while True:
        print("\n=== Consultar Produtos ===")
        print("1. Consultar por Nome")
        print("2. Consultar por Preço Máximo")
        print("3. Consultar por Fabricante")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_produto = input(
                "Digite o nome do produto que deseja consultar: ")
            db = conectar_banco()
            cursor = db.cursor()
            cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE nome_med LIKE %s",
                           ('%' + nome_produto + '%',))
            produtos = cursor.fetchall()

            table = PrettyTable()
            table.field_names = ["ID", "Nome", "Fabricante",
                                 "Estoque", "Preço (R$)"]

            if produtos:
                for produto in produtos:
                    id_med, nome_med, fabricante, estoque, preco = produto
                    table.add_row(
                        [id_med, nome_med, fabricante, estoque, preco])
                print("\n=== Produtos Encontrados ===")
                print(table)
            else:
                print("Nenhum produto encontrado.")

            cursor.close()
            db.close()

        elif opcao == '2':
            preco_maximo = float(input("Digite o preço máximo: "))
            db = conectar_banco()
            cursor = db.cursor()
            cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE preco <= %s",
                           (preco_maximo,))
            produtos = cursor.fetchall()

            table = PrettyTable()
            table.field_names = ["ID", "Nome", "Fabricante",
                                 "Estoque", "Preço (R$)"]

            if produtos:
                for produto in produtos:
                    id_med, nome_med, fabricante, estoque, preco = produto
                    table.add_row(
                        [id_med, nome_med, fabricante, estoque, preco])
                print("\n=== Produtos Encontrados ===")
                print(table)
            else:
                print("Nenhum produto encontrado com o preço máximo informado.")

            cursor.close()
            db.close()

        elif opcao == '3':
            fabricante = input("Digite o fabricante que deseja consultar: ")
            db = conectar_banco()
            cursor = db.cursor()
            cursor.execute("SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento WHERE fabricante LIKE %s",
                           ('%' + fabricante + '%',))
            produtos = cursor.fetchall()

            table = PrettyTable()
            table.field_names = ["ID", "Nome", "Fabricante",
                                 "Estoque", "Preço (R$)"]

            if produtos:
                for produto in produtos:
                    id_med, nome_med, fabricante, estoque, preco = produto
                    table.add_row(
                        [id_med, nome_med, fabricante, estoque, preco])
                print("\n=== Produtos Encontrados ===")
                print(table)
            else:
                print("Nenhum produto encontrado do fabricante informado.")

            cursor.close()
            db.close()

        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


def listar_clientes():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_cli, nome_cli, email_cli, cidade_cli, telefone_cli FROM cliente")
    clientes = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Email", "Cidade", "Telefone"]

    if clientes:
        for cliente in clientes:
            table.add_row(cliente)
        print("\n=== Clientes Cadastrados ===")
        print(table)
    else:
        print("Nenhum cliente cadastrado.")

    cursor.close()
    db.close()


def listar_vendedores():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id_ven, nome_ven, email_ven, cidade_ven, telefone_ven FROM vendedor")
    vendedores = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "Nome", "Email", "Cidade", "Telefone"]

    if vendedores:
        for vendedor in vendedores:
            table.add_row(vendedor)
        print("\n=== Vendedores Cadastrados ===")
        print(table)
    else:
        print("Nenhum vendedor cadastrado.")

    cursor.close()
    db.close()
