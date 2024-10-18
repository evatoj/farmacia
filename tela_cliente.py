from decimal import Decimal
from conexao import conectar_banco
from prettytable import PrettyTable
from enum import Enum


class FormaPagamento(Enum):
    CARTAO = 'a'
    BOLETO = 'b'
    PIX = 'c'
    BERRIES = 'd'


def tela_cliente(email):
    while True:
        print("\n=== Área do Cliente ===")
        print("1. Ver dados cadastrais")
        print("2. Buscar Medicamentos")
        print("3. Realizar Compra")
        print("4. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_dados_cadastrais(email)
        elif opcao == '2':
            buscar_medicamentos()
        elif opcao == '3':
            realizar_compra(email)
        elif opcao == '4':
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
        print("1. Listar Todos os Medicamentos Cadastrados")
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
        "SELECT id_med, nome_med, fabricante, estoque, preco FROM medicamento")
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


def realizar_compra(email):
    db = conectar_banco()
    cursor = db.cursor()

    cursor.execute("SELECT id_cli FROM cliente WHERE email_cli = %s", (email,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente não encontrado.")
        cursor.close()
        db.close()
        return

    id_cliente = cliente[0]

    cursor.execute(
        "SELECT torce_flamengo, cidade_cli, assiste_one_piece FROM cliente WHERE id_cli = %s", (id_cliente,))
    dados_cliente = cursor.fetchone()

    torce_flamengo, cidade, assiste_one_piece = dados_cliente

    cursor.execute(
        "SELECT id_ven, nome_ven FROM vendedor WHERE status_ven = 1")
    vendedores = cursor.fetchall()

    if not vendedores:
        print("Não há vendedores disponíveis.")
        cursor.close()
        db.close()
        return

    print("\n=== Vendedores Disponíveis ===")
    for ven in vendedores:
        print(f"ID: {ven[0]}, Nome: {ven[1]}")

    id_vendedor = int(input("Escolha o ID do vendedor: "))

    itens_compra = []
    while True:
        cursor.execute(
            "SELECT id_med, nome_med, estoque, preco FROM medicamento WHERE estoque > 0")
        produtos = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Estoque", "Preço (R$)"]

        for produto in produtos:
            id_med, nome_med, estoque, preco = produto
            table.add_row([id_med, nome_med, estoque, preco])
        print("\n=== Medicamentos Disponíveis ===")
        print(table)

        id_med = int(input("Digite o ID do medicamento que deseja comprar: "))

        cursor.execute(
            "SELECT estoque, preco FROM medicamento WHERE id_med = %s", (id_med,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Este medicamento não existe.")
            continue

        estoque_disponivel, preco_unitario = resultado
        if estoque_disponivel <= 0:
            print("Este medicamento está indisponível no momento.")
            continue

        quantidade = int(input("Digite a quantidade: "))

        if quantidade > estoque_disponivel:
            print("Quantidade solicitada excede o estoque disponível.")
            continue

        itens_compra.append((id_med, quantidade, preco_unitario))
        print("Item adicionado à compra.")

        continuar = input("Deseja adicionar mais itens? (s/n): ")
        if continuar.lower() != 's':
            break

    print("\n=== Formas de Pagamento ===")
    for forma in FormaPagamento:
        print(f"{forma.value} - {forma.name.capitalize()}")

    forma_pagamento_input = input("Escolha a forma de pagamento (a/b/c/d): ")

    try:
        forma_pagamento = FormaPagamento(forma_pagamento_input)
    except ValueError:
        print("Forma de pagamento inválida.")
        cursor.close()
        db.close()
        return

    valor_total = sum(Decimal(qtd) * Decimal(preco)
                      for _, qtd, preco in itens_compra)

    desconto = Decimal('0.0')
    if torce_flamengo == 1 or cidade == "Sousa" or assiste_one_piece == 1:
        desconto = valor_total * Decimal('0.10')

    valor_total_com_desconto = valor_total - desconto

    cursor.execute("INSERT INTO compra (id_cli, id_ven, forma_pagamento, valor_total) VALUES (%s, %s, %s, %s)",
                   (id_cliente, id_vendedor, forma_pagamento.value, valor_total_com_desconto))
    id_compra = cursor.lastrowid

    for id_med, quantidade, preco_unitario in itens_compra:
        cursor.execute(
            "INSERT INTO item_compra (id_compra, id_med, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
            (id_compra, id_med, quantidade, preco_unitario))

    db.commit()
    print(f"Compra realizada com sucesso! Valor total: R$ {
          valor_total_com_desconto:.2f} (Desconto aplicado: R$ {desconto:.2f})\nAguarde até que seu vendedor confirme sua compra.")

    cursor.close()
    db.close()
