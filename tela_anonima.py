from conexao import conectar_banco


def tela_anonima():
    while True:
        print("\n=== Navegação Anônima ===")
        print("1. Visualizar Produtos")
        print("2. Consultar Produtos")
        print("3. Listar Clientes")
        print("4. Listar Vendedores")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            visualizar_produtos()
        elif opcao == '2':
            consultar_produtos()
        elif opcao == '3':
            listar_clientes()
        elif opcao == '4':
            listar_vendedores()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


def visualizar_produtos():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamento")
    produtos = cursor.fetchall()
    for produto in produtos:
        id_med, nome_med, fabricante, estoque, preco = produto
        print(f"ID: {id_med}, Nome: {nome_med}, Fabricante: {
              fabricante}, Estoque: {estoque}, Preço: R${preco:.2f}")
    cursor.close()
    db.close()


def consultar_produtos():
    nome_produto = input("Digite o nome do produto que deseja consultar: ")
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamento WHERE nome_med LIKE %s",
                   ('%' + nome_produto + '%',))
    produtos = cursor.fetchall()
    if produtos:
        for produto in produtos:

            id_med, nome_med, fabricante, estoque, preco = produto
            print(f"ID: {id_med}, Nome: {nome_med}, Fabricante: {
                  fabricante}, Estoque: {estoque}, Preço: R${preco:.2f}")
    else:
        print("Nenhum produto encontrado.")
    cursor.close()
    db.close()


def listar_clientes():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(
        "SELECT nome_cli, email_cli, telefone_cli, cidade_cli FROM cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    cursor.close()
    db.close()


def listar_vendedores():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT nome_ven, email_ven, telefone_ven FROM vendedor")
    vendedores = cursor.fetchall()
    for vendedor in vendedores:
        print(vendedor)
    cursor.close()
    db.close()
