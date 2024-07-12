import json
import os

ARQUIVO_DADOS = 'medicamentos.json'


def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)
    return []


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def gerar_novo_id(dados):
    if not dados:
        return 1
    else:
        return max(medicamento['id'] for medicamento in dados) + 1


def inserir_medicamento():
    nome = input("Insira o nome do medicamento: ").strip().lower()
    fabricante = input("Insira o fabricante: ").strip().lower()
    try:
        quantidade = int(input("Insira a quantidade em estoque: "))
        preco = float(input("Insira o preço: "))
    except ValueError:
        print("Quantidade e preço devem ser numéricos.")
        return

    dados = carregar_dados()

    for medicamento in dados:
        if medicamento['nome'] == nome and medicamento['fabricante'] == fabricante:
            medicamento['quantidade'] += quantidade
            salvar_dados(dados)
            print("Quantidade atualizada para o medicamento existente.")
            return

    novo_medicamento = {
        'id': gerar_novo_id(dados),
        'nome': nome,
        'fabricante': fabricante,
        'quantidade': quantidade,
        'preco': preco
    }
    dados.append(novo_medicamento)
    salvar_dados(dados)
    print("Medicamento adicionado.")


def editar_medicamento():
    try:
        id = int(input("Insira o ID do medicamento a ser editado: "))
    except ValueError:
        print("ID inválido.")
        return

    dados = carregar_dados()
    for medicamento in dados:
        if medicamento['id'] == id:
            medicamento['nome'] = input(
                "Insira o novo nome do medicamento: ").strip().lower()
            medicamento['fabricante'] = input(
                "Insira o novo fabricante: ").strip().lower()
            try:
                medicamento['quantidade'] = int(
                    input("Insira a nova quantidade em estoque: "))
                medicamento['preco'] = float(input("Insira o novo preço: "))
            except ValueError:
                print("Quantidade e preço devem ser numéricos.")
                return

            salvar_dados(dados)
            print("Medicamento atualizado.")
            return
    print("Medicamento não encontrado.")


def atualizar_preco():
    nome = input("Insira o nome do medicamento: ").strip().lower()
    fabricante = input("Insira o fabricante: ").strip().lower()
    try:
        novo_preco = float(input("Insira o novo preço: "))
    except ValueError:
        print("O preço deve ser numérico.")
        return

    dados = carregar_dados()
    for medicamento in dados:
        if medicamento['nome'] == nome and medicamento['fabricante'] == fabricante:
            medicamento['preco'] = novo_preco
            salvar_dados(dados)
            print("Preço atualizado.")
            return

    print("Medicamento não encontrado.")


def atualizar_estoque():
    nome = input("Insira o nome do medicamento: ").strip().lower()
    fabricante = input("Insira o fabricante: ").strip().lower()
    try:
        nova_quantidade = int(input("Insira a nova quantidade em estoque: "))
    except ValueError:
        print("A quantidade deve ser numérica.")
        return

    dados = carregar_dados()
    for medicamento in dados:
        if medicamento['nome'] == nome and medicamento['fabricante'] == fabricante:
            medicamento['quantidade'] = nova_quantidade
            salvar_dados(dados)
            print("Estoque atualizado.")
            return

    print("Medicamento não encontrado.")


def pesquisar_por_nome():
    nome = input(
        "Insira o nome do medicamento a ser pesquisado: ").strip().lower()
    dados = carregar_dados()
    resultados = [
        medicamento for medicamento in dados if medicamento['nome'] == nome]
    if resultados:
        for medicamento in resultados:
            print(f"ID: {medicamento['id']}, Nome: {medicamento['nome'].title()}, Fabricante: {
                  medicamento['fabricante'].title()}, Quantidade: {medicamento['quantidade']}, Preço: R$ {medicamento['preco']}")
    else:
        print("Nenhum medicamento encontrado com esse nome.")


def remover_medicamento():
    try:
        id = int(input("Insira o ID do medicamento a ser removido: "))
    except ValueError:
        print("ID inválido.")
        return

    dados = carregar_dados()
    novos_dados = [
        medicamento for medicamento in dados if medicamento['id'] != id]
    if len(novos_dados) == len(dados):
        print("Medicamento não encontrado.")
    else:
        salvar_dados(novos_dados)
        print("Medicamento removido.")


def exibir_todos():
    dados = carregar_dados()
    if not dados:
        print("Nenhum medicamento cadastrado ainda.")
    else:
        for medicamento in dados:
            print(f"ID: {medicamento['id']}, Nome: {medicamento['nome'].title()}, Fabricante: {
                  medicamento['fabricante'].title()}, Quantidade: {medicamento['quantidade']}, Preço: R$ {medicamento['preco']}")


def exibir_um():
    try:
        id = int(input("Insira o ID do medicamento a ser exibido: "))
    except ValueError:
        print("ID inválido.")
        return

    dados = carregar_dados()
    for medicamento in dados:
        if medicamento['id'] == id:
            print(f"ID: {medicamento['id']}, Nome: {medicamento['nome'].title()}, Fabricante: {
                  medicamento['fabricante'].title()}, Quantidade: {medicamento['quantidade']}, Preço: R$ {medicamento['preco']}")
            return
    print("Medicamento não encontrado.")


def menu():
    while True:
        print("\n1. Inserir Medicamento")
        print("2. Editar Medicamento")
        print("3. Atualizar Preço")
        print("4. Atualizar Estoque")
        print("5. Pesquisar por Nome")
        print("6. Remover Medicamento")
        print("7. Exibir Todos os Medicamentos")
        print("8. Buscar Medicamento por ID")
        print("9. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir_medicamento()
        elif escolha == '2':
            editar_medicamento()
        elif escolha == '3':
            atualizar_preco()
        elif escolha == '4':
            atualizar_estoque()
        elif escolha == '5':
            pesquisar_por_nome()
        elif escolha == '6':
            remover_medicamento()
        elif escolha == '7':
            exibir_todos()
        elif escolha == '8':
            exibir_um()
        elif escolha == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
