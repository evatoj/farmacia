import mysql.connector


def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='#umdoistres',
        database='farmacia'
    )


def criar_medicamento(cursor, nome_medicamento, fabricante, quantidade, valor):
    comando = f'INSERT INTO medicamentos (nome_medicamento, fabricante, quantidade, valor) VALUES ("{
        nome_medicamento}", "{fabricante}", {quantidade}, {valor})'
    cursor.execute(comando)
    print('Medicamento cadastrado com sucesso!')


def alterar_valor(cursor, id_medicamento, valor):
    comando = f'UPDATE medicamentos SET valor = {
        valor} WHERE idMedicamento = {id_medicamento}'
    cursor.execute(comando)
    print('Valor atualizado com sucesso!')


def pesquisar_por_id(cursor, id_medicamento):
    comando = f'SELECT * FROM medicamentos WHERE idMedicamento = {
        id_medicamento}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado:
        for medicamento in resultado:
            print(medicamento)
    else:
        print('Medicamento não encontrado.')


def remover_medicamento(cursor, id_medicamento):
    comando = f'DELETE FROM medicamentos WHERE idMedicamento = {
        id_medicamento}'
    cursor.execute(comando)
    print('Medicamento removido com sucesso!')


def exibir_todos(cursor):
    comando = 'SELECT * FROM medicamentos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado:
        for medicamento in resultado:
            print(medicamento)
    else:
        print('Nenhum medicamento encontrado.')


def exibir_um(cursor, id_medicamento):
    comando = f'SELECT * FROM medicamentos WHERE idMedicamento = {
        id_medicamento}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado:
        for medicamento in resultado:
            print(medicamento)
    else:
        print('Medicamento não encontrado.')


def main():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    while True:
        print("\nEscolha uma operação:")
        print("1. Inserir Medicamento")
        print("2. Alterar Preço")
        print("3. Buscar por ID")
        print("4. Remover Medicamento")
        print("5. Exibir Todos")
        print("6. Exibir Um Medicamento")
        print("7. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '1':
            nome_medicamento = input("Nome do medicamento: ")
            fabricante = input("Fabricante: ")
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor: "))
            criar_medicamento(cursor, nome_medicamento,
                              fabricante, quantidade, valor)
            conexao.commit()

        elif escolha == '2':
            id_medicamento = int(input("ID do medicamento: "))
            valor = float(input("Novo valor: "))
            alterar_valor(cursor, id_medicamento, valor)
            conexao.commit()

        elif escolha == '3':
            id_medicamento = int(input("ID do medicamento: "))
            pesquisar_por_id(cursor, id_medicamento)

        elif escolha == '4':
            id_medicamento = int(input("ID do medicamento a ser removido: "))
            remover_medicamento(cursor, id_medicamento)
            conexao.commit()

        elif escolha == '5':
            exibir_todos(cursor)

        elif escolha == '6':
            id_medicamento = int(input("ID do medicamento: "))
            exibir_um(cursor, id_medicamento)

        elif escolha == '7':
            print("Saindo...")
            break

        else:
            print("Deixe de ser burro, escolha uma opção VÁLIDA.")

    cursor.close()
    conexao.close()


if __name__ == "__main__":
    main()
