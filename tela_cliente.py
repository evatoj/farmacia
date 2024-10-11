from conexao import conectar_banco


def tela_cliente(email):
    while True:
        print("\n=== Área do Cliente ===")
        print("1. Ver dados cadastrais")
        print("2. Ver medicamentos disponíveis")
        print("3. Adicionar medicamentos ao carrinho")
        print("4. Retirar medicamentos do carrinho")
        print("5. Efetuar compra")
        print("6. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_dados_cadastrais(email)
        elif opcao == '2':
            ver_medicamentos_disponiveis()
        elif opcao == '3':
            adicionar_med_carrinho()
        elif opcao == '4':
            retirar_med_carrinho()
        elif opcao == '5':
            efetuar_compra()
        elif opcao == '6':
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


def ver_medicamentos_disponiveis():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM estoque_disponivel")
    produtos = cursor.fetchall()
    if produtos:
        print("\n=== Medicamentos Disponíveis ===")
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            print(f"ID: {id_med}, Nome: {nome_med}, Fabricante: {fabricante}, Estoque: {estoque}, Preço: R${preco:.2f}")
    else:
        print("Nenhum medicamento disponível.")
    cursor.close()
    db.close()

def adicionar_med_carrinho():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM estoque_disponivel")
    produtos = cursor.fetchall()
    produto_compra = ()
    print(produtos)
    if produtos:
        id_compra = input("Escolha um produto a partir do ID: ")
        for produto in produtos:
            if produto[0] == id_compra:
                produto_compra = produto
                # Adicionar tratamento de erro caso o id não exista na tabela.
        print(produto_compra)
        id_med, nome_med, fabricante, estoque, preco = produto_compra
        quantidade_compra = input(f"Quantas unidades de {nome_med} você deseja comprar? ")
        if quantidade_compra <= estoque:
            resposta = input(f"Você deseja inserir {quantidade_compra} unidades de {nome_med} no seu carrinho?(s/n)")
            if resposta.lower() == "n":
                cursor.close()
                db.close()
                return
            elif resposta.lower() == "s":
                pass
            else:
                print("Resposta inválida")
                cursor.close()
                db.close()
                return
        else:
            print(f"Não há estoque suficiente! Só temos {estoque} unidades de {nome_med}")
    else:
        print("Nenhum medicamento disponível.")
    cursor.close()
    db.close()
    return

def retirar_med_carrinho():
    pass

def efetuar_compra():
    pass
