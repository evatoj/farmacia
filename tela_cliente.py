from conexao import conectar_banco

def tela_cliente(email):
    while True:
        print("\n=== Área do Cliente ===")
        print("1. Ver dados cadastrais")
        print("2. Visualizar medicamentos disponíveis")
        print("3. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_dados_cadastrais(email)
        elif opcao == '3':
            break
        elif opcao == '2':
            compra()

        else:
            print("Opção inválida. Tente novamente.")

def compra():
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
        id_medicamento = int(input("Digite o ID do medicamento que deseja comprar."))
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

    confirmar = input("Deseja confirmar a compra? (s/n): ").strip().lower()
    if confirmar == 's':
        novo_estoque = estoque_atual - quantidade
        cursor.execute("UPDATE medicamento SET estoque = %s WHERE id = %s", (novo_estoque, id_medicamento))
        cursor.execute("INSERT INTO vendas (id_cliente, id_medicamento, quantidade, valor_total) VALUES (%s, %s, %s, %s)", 
                         (id_cliente, id_medicamento, quantidade, valor_total))
        db.commit()

        print(f"Compra realizada com sucesso! {quantidade} unidade(s) de {nome_med} foram compradas.")
    else:
        print("Compra cancelada.")
    cursor.close()
    db.close()


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
