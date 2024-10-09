from conexao import conectar_banco


def tela_cliente(email):
    while True:
        print("\n=== Área do Cliente ===")
        print("1. Ver dados cadastrais")
        print("2. Ver Medicamentos Disponíveis")
        print("3. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_dados_cadastrais(email)
        elif opcao == '2':
            ver_medicamentos_disponiveis()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")


def ver_dados_cadastrais(email):
    db = conectar_banco()
    cursor = db.cursor()

    cursor.execute(
        "SELECT cpf_cli, nome_cli, email_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece "
        "FROM cliente WHERE email_cli = %s", (email,))
    cliente = cursor.fetchone()

    if cliente:
        print("\n=== Dados Cadastrais ===")
        print(f"CPF: {cliente[0]}")
        print(f"Nome: {cliente[1]}")
        print(f"Email: {cliente[2]}")
        print(f"Telefone: {cliente[3]}")
        print(f"Cidade: {cliente[4]}")

        if cliente[5]:
            print("Torce para o Flamengo: Sim")
        else:
            print("Torce para o Flamengo: Não")

        if cliente[6]:
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
            print(f"ID: {id_med}, Nome: {nome_med}, Fabricante: {
                  fabricante}, Estoque: {estoque}, Preço: R${preco:.2f}")
    else:
        print("Nenhum medicamento disponível.")
    cursor.close()
    db.close()
