from conexao import conectar_banco


def tela_vendedor():
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        print("\n=== Área do Vendedor ===")
        print("1. Manipular Estoque")
        print("2. Buscar Medicamento por ID")
        print("3. Listar Medicamentos com Estoque Baixo")
        print("4. Listar Medicamentos sem Estoque Disponível")
        print("5. Listar Todos os Medicamentos")
        print("6. Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            while True:
                print("\n=== Manipular Estoque ===")
                print("1. Inserir Medicamento")
                print("2. Alterar Preço")
                print("3. Remover Medicamento")
                print("4. Atualizar Estoque")
                print("5. Voltar")

                opcao_estoque = input("Escolha uma opção: ")

                if opcao_estoque == '1':
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

                elif opcao_estoque == '2':
                    id_med = int(input("Digite o ID do medicamento: "))
                    novo_preco = float(input("Digite o novo preço: "))
                    cursor.execute("""
                        UPDATE medicamento SET preco = %s WHERE id_med = %s
                    """, (novo_preco, id_med))
                    db.commit()
                    print("Preço atualizado com sucesso!")

                elif opcao_estoque == '3':
                    id_med = int(
                        input("Digite o ID do medicamento que deseja remover: "))
                    cursor.execute(
                        "DELETE FROM medicamento WHERE id_med = %s", (id_med,))
                    db.commit()
                    print("Medicamento removido com sucesso!")

                elif opcao_estoque == '4':
                    id_med = int(
                        input("Digite o ID do medicamento para atualizar o estoque: "))
                    novo_estoque = int(
                        input("Digite a nova quantidade em estoque: "))
                    cursor.execute("""
                        UPDATE medicamento SET estoque = %s WHERE id_med = %s
                    """, (novo_estoque, id_med))
                    db.commit()
                    print("Estoque atualizado com sucesso!")

                elif opcao_estoque == '5':
                    break
                else:
                    print("Opção inválida! Tente novamente.")

        elif opcao == '2':
            id_med = int(input("Digite o ID do medicamento: "))
            cursor.execute(
                "SELECT * FROM medicamento WHERE id_med = %s", (id_med,))
            medicamento = cursor.fetchone()
            if medicamento:
                print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {medicamento[2]}, Estoque: {medicamento[3]}, Preço: R${medicamento[4]:.2f}")
            else:
                print("Medicamento não encontrado!")

        elif opcao == '3':
            cursor.execute("SELECT * FROM estoque_baixo")
            medicamentos_baixo_estoque = cursor.fetchall()
            if medicamentos_baixo_estoque:
                print("Medicamentos com menos de 5 unidades no estoque:")
                for medicamento in medicamentos_baixo_estoque:
                    print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {medicamento[2]}, Estoque: {medicamento[3]}, Preço: R${medicamento[4]:.2f}")
            else:
                print("Nenhum medicamento com estoque baixo.")

        elif opcao == '4':
            cursor.execute("SELECT * FROM estoque_zerado")
            medicamentos_zerados = cursor.fetchall()
            if medicamentos_zerados:
                print("Medicamentos com estoque zerado:")
                for medicamento in medicamentos_zerados:
                    print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {medicamento[2]}, Preço: R${medicamento[3]:.2f}")
            else:
                print("Nenhum medicamento com estoque zerado.")

        elif opcao == '5':
            cursor.execute("SELECT * FROM medicamento")
            medicamentos = cursor.fetchall()
            for medicamento in medicamentos:
                print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {medicamento[2]}, Estoque: {medicamento[3]}, Preço: R${medicamento[4]:.2f}")

        elif opcao == '6':
            print("Retornando ao Menu Inicial...\n")
            break

        else:
            print("Opção inválida! Tente novamente.")

    cursor.close()
    db.close()
