from conexao import conectar_banco


def tela_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        print("\n=== Tela do Vendedor ===")
        print("1. Inserir Medicamento")
        print("2. Alterar Preço")
        print("3. Exibir Medicamento por ID")
        print("4. Listar Todos os Medicamentos")
        print("5. Remover Medicamento")
        print("6. Atualizar Estoque")
        print("7. Tela Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do medicamento: ")
            fabricante = input("Digite o fabricante: ")
            estoque = int(input("Digite a quantidade em estoque: "))
            preco = float(input("Digite o preço: "))

            cursor.execute("""
                INSERT INTO medicamento (nome_med, fabricante, estoque, preco)
                VALUES (%s, %s, %s, %s)
            """, (nome, fabricante, estoque, preco))
            db.commit()
            print("Medicamento inserido com sucesso!")

        elif opcao == '2':
            id_med = int(input("Digite o ID do medicamento: "))
            novo_preco = float(input("Digite o novo preço: "))
            cursor.execute("""
                UPDATE medicamento SET preco = %s WHERE id_med = %s
            """, (novo_preco, id_med))
            db.commit()
            print("Preço atualizado com sucesso!")

        elif opcao == '3':
            id_med = int(input("Digite o ID do medicamento: "))
            cursor.execute(
                "SELECT * FROM medicamento WHERE id_med = %s", (id_med,))
            medicamento = cursor.fetchone()
            if medicamento:
                print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {
                      medicamento[2]}, Estoque: {medicamento[3]}, Preço: {medicamento[4]}")
            else:
                print("Medicamento não encontrado!")

        elif opcao == '4':
            cursor.execute("SELECT * FROM medicamento")
            medicamentos = cursor.fetchall()
            for medicamento in medicamentos:
                print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {
                      medicamento[2]}, Estoque: {medicamento[3]}, Preço: {medicamento[4]}")

        elif opcao == '5':
            id_med = int(
                input("Digite o ID do medicamento que deseja remover: "))
            cursor.execute(
                "DELETE FROM medicamento WHERE id_med = %s", (id_med,))
            db.commit()
            print("Medicamento removido com sucesso!")

        elif opcao == '6':
            id_med = int(
                input("Digite o ID do medicamento para atualizar o estoque: "))
            novo_estoque = int(input("Digite a nova quantidade em estoque: "))
            cursor.execute("""
                UPDATE medicamento SET estoque = %s WHERE id_med = %s
            """, (novo_estoque, id_med))
            db.commit()
            print("Estoque atualizado com sucesso!")

        elif opcao == '7':
            print("Saindo da tela do vendedor.")
            break
        else:
            print("Opção inválida! Tente novamente.")

    cursor.close()
    db.close()
