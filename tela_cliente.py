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
            compra(email)
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

def compra(email):
    db = conectar_banco()
    cursor = db.cursor()

    cursor.execute("SELECT id_med, nome_med, estoque, preco FROM medicamento WHERE estoque > 0")
    medicamentos = cursor.fetchall()

    if not medicamentos:
        print("Nenhum medicamento disponível para compra.")
        cursor.close()
        db.close()
        return

    print("Medicamentos disponíveis:")
    for med in medicamentos:
        print(f"ID: {med[0]} | Nome: {med[1]} | Estoque: {med[2]} | Preço: {med[3]}")

    try:
        id_medicamento = int(input("Digite o ID do medicamento que deseja comprar: "))
    except ValueError:
        print("ID inválido.")
        cursor.close()
        db.close()
        return

    cursor.execute("SELECT nome_med, estoque, preco FROM medicamento WHERE id_med = %s", (id_medicamento,))
    medicamento = cursor.fetchone()

    if medicamento is None:
        print("Medicamento não encontrado.")
        cursor.close()
        db.close()
        return

    nome_med = medicamento[0]
    estoque_atual = medicamento[1]
    preco = medicamento[2]

    print(f"Você escolheu {nome_med}. Preço: R$ {preco}. Estoque disponível: {estoque_atual}")

    try:
        quantidade = int(input(f"Quantas unidades de {nome_med} você deseja comprar? "))
    except ValueError:
        print("Quantidade inválida.")
        cursor.close()
        db.close()
        return

    if quantidade > estoque_atual:
        print("Quantidade solicitada é maior do que o estoque disponível.")
        cursor.close()
        db.close()
        return

    valor_total = quantidade * preco
    print(f"O valor total da compra é: R$ {valor_total}")
    
    cursor.execute("SELECT id_ven, nome_ven FROM vendedor")
    vendedores = cursor.fetchall()

    print("Vendedores disponíveis:")
    for vendedor in vendedores:
        print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}")

    try:
        id_vendedor = int(input("Digite o ID do vendedor que vai efetivar a compra: "))
    except ValueError:
        print("ID de vendedor inválido.")
        cursor.close()
        db.close()
        return

    # Verificar se o vendedor existe
    cursor.execute("SELECT id_ven FROM vendedor WHERE id_ven = %s", (id_vendedor,))
    vendedor_existe = cursor.fetchone()

    if vendedor_existe is None:
        print("Vendedor não encontrado.")
        cursor.close()
        db.close()
        return
    
    formas_pagamento = [1, 2, 3, 4] # 1- cartao, 2- boleto, 3- pix, 4- berries
    forma_pagamento = int(input("Escolha a forma de pagamento: \n1- cartão \n2- boleto \n3- pix \n4- berries: "))

    if forma_pagamento not in formas_pagamento:
        print("Forma de pagamento inválida.")
        cursor.close()
        db.close()
        return

    # Definir o status de pagamento (a confirmar para essas formas de pagamento)
    # status_pagamento = 'pendente' if forma_pagamento in [1, 2, 3, 4]

    confirmar = input("Deseja confirmar a compra? (s/n): ").strip().lower()
    if confirmar == 's':
        cursor.execute("SELECT id_cli, cpf_cli, nome_cli, email_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece "
        "FROM cliente WHERE email_cli = %s", (email,))
        cliente = cursor.fetchone()

        novo_estoque = estoque_atual - quantidade
        cursor.execute("UPDATE medicamento SET estoque = %s WHERE id_med = %s", (novo_estoque, id_medicamento))
        cursor.execute("INSERT INTO compra (id_cli, id_med, valor_total, status_pagamento, forma_pagamento) VALUES (%s, %s, %s, %s, %s)", 
                         (cliente[0], id_medicamento, valor_total, 0, 0))
        db.commit()

        print(f"Compra realizada com sucesso! {quantidade} unidade(s) de {nome_med} foram compradas.")
    else:
        print("Compra cancelada.")
    cursor.close()
    db.close()
