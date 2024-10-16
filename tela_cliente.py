from conexao import conectar_banco

# Carrinho de compras do cliente (dicionário com ID do medicamento e quantidade)
carrinho = {}

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

    if produtos:
        print("\n=== Adicionar Medicamentos ao Carrinho ===")
        for produto in produtos:
            id_med, nome_med, fabricante, estoque, preco = produto
            print(f"ID: {id_med}, Nome: {nome_med}, Fabricante: {fabricante}, Estoque: {estoque}, Preço: R${preco:.2f}")

        id_med = int(input("\nDigite o ID do medicamento que deseja adicionar: "))
        quantidade = int(input("Digite a quantidade desejada: "))

        # Verifica se o medicamento existe e tem estoque suficiente
        cursor.execute("SELECT estoque FROM medicamento WHERE id_med = %s", (id_med,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] >= quantidade:
            if id_med in carrinho:
                carrinho[id_med] += quantidade
            else:
                carrinho[id_med] = quantidade
            print(f"{quantidade} unidades adicionadas ao carrinho.")
        else:
            print("Estoque insuficiente ou medicamento não encontrado.")

    else:
        print("Nenhum medicamento disponível.")
    cursor.close()
    db.close()


def retirar_med_carrinho():
    print("\n=== Remover Medicamentos do Carrinho ===")
    if carrinho:
        print("Itens no carrinho:")
        for id_med, quantidade in carrinho.items():
            print(f"ID: {id_med}, Quantidade: {quantidade}")

        id_med = int(input("Digite o ID do medicamento que deseja remover: "))
        if id_med in carrinho:
            quantidade_remover = int(input("Digite a quantidade a remover: "))
            if quantidade_remover >= carrinho[id_med]:
                del carrinho[id_med]
                print("Medicamento removido do carrinho.")
            else:
                carrinho[id_med] -= quantidade_remover
                print(f"{quantidade_remover} unidades removidas do carrinho.")
        else:
            print("Esse medicamento não está no carrinho.")
    else:
        print("O carrinho está vazio.")


def efetuar_compra():
    if not carrinho:
        print("Seu carrinho está vazio. Adicione medicamentos antes de comprar.")
        return

    db = conectar_banco()
    cursor = db.cursor()

    for id_med, quantidade in carrinho.items():
        # Verifica estoque diretamente na tabela 'medicamento', pois a view não pode ser atualizada
        cursor.execute("SELECT estoque FROM medicamento WHERE id_med = %s", (id_med,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] >= quantidade:
            # Atualiza o estoque na tabela 'medicamento' diretamente
            cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE id_med = %s", (quantidade, id_med))
            print(f"Compra de {quantidade}x do medicamento ID {id_med} realizada.")
        else:
            print(f"Estoque insuficiente para o medicamento ID {id_med}.")
            db.rollback()
            cursor.close()
            db.close()
            return

    db.commit()  # Confirma todas as atualizações
    cursor.close()
    db.close()
    carrinho.clear()
    print("Compra efetuada com sucesso!")
