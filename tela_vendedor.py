from conexao import conectar_banco
from prettytable import PrettyTable


def tela_vendedor(id_vendedor):
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        print("\n=== Área do Vendedor ===")
        print("1. Manipular Estoque")
        print("2. Buscar Medicamentos")
        print("3. Listar Medicamentos com Estoque Baixo")
        print("4. Listar Medicamentos sem Estoque Disponível")
        print("5. Confirmar Compras dos Clientes")
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

                    try:
                        cursor.execute("""
                            INSERT INTO medicamento (nome_med, fabricante, estoque, preco)
                            VALUES (%s, %s, %s, %s)""", (nome, fabricante, estoque, preco))
                        db.commit()
                        print("Medicamento inserido com sucesso!")
                    except Exception as e:
                        print(f"Erro ao inserir medicamento: {e}")

                elif opcao_estoque == '2':
                    id_med = int(input("Digite o ID do medicamento: "))
                    novo_preco = float(input("Digite o novo preço: "))
                    try:
                        cursor.execute("""
                            UPDATE medicamento SET preco = %s WHERE id_med = %s""",
                                       (novo_preco, id_med))
                        db.commit()
                        print("Preço atualizado com sucesso!")
                    except Exception as e:
                        print(f"Erro ao atualizar preço: {e}")

                elif opcao_estoque == '3':
                    id_med = int(
                        input("Digite o ID do medicamento que deseja remover: "))
                    try:
                        cursor.execute(
                            "DELETE FROM medicamento WHERE id_med = %s", (id_med,))
                        db.commit()
                        print("Medicamento removido com sucesso!")
                    except Exception as e:
                        print(f"Erro ao remover medicamento: {e}")

                elif opcao_estoque == '4':
                    id_med = int(
                        input("Digite o ID do medicamento para atualizar o estoque: "))
                    novo_estoque = int(
                        input("Digite a nova quantidade em estoque: "))
                    try:
                        cursor.execute("""
                            UPDATE medicamento SET estoque = %s WHERE id_med = %s""",
                                       (novo_estoque, id_med))
                        db.commit()
                        print("Estoque atualizado com sucesso!")
                    except Exception as e:
                        print(f"Erro ao atualizar estoque: {e}")

                elif opcao_estoque == '5':
                    break
                else:
                    print("Opção inválida! Tente novamente.")

        elif opcao == '2':
            while True:
                print("\n=== Buscar Medicamentos ===")
                print("1. Buscar por ID")
                print("2. Buscar por Nome")
                print("3. Buscar por Fabricante")
                print("4. Buscar por Faixa de Preço Máximo")
                print("5. Listar Todos os Medicamentos")
                print("6. Voltar")

                opcao_busca = input("Escolha uma opção: ")

                if opcao_busca == '1':
                    id_med = int(input("Digite o ID do medicamento: "))
                    cursor.execute(
                        "SELECT * FROM medicamento WHERE id_med = %s", (id_med,))
                    medicamento = cursor.fetchone()
                    if medicamento:
                        print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Fabricante: {
                              medicamento[2]}, Estoque: {medicamento[3]}, Preço: R${medicamento[4]:.2f}")
                    else:
                        print("Medicamento não encontrado!")

                elif opcao_busca == '2':
                    nome_med = input("Digite o nome do medicamento: ")
                    cursor.execute(
                        "SELECT * FROM medicamento WHERE nome_med LIKE %s", ('%' + nome_med + '%',))
                    medicamentos = cursor.fetchall()
                    if medicamentos:
                        table = PrettyTable()
                        table.field_names = [
                            "ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]
                        for medicamento in medicamentos:
                            table.add_row(
                                [medicamento[0], medicamento[1], medicamento[2], medicamento[3], medicamento[4]])
                        print(table)
                    else:
                        print("Nenhum medicamento encontrado com esse nome.")

                elif opcao_busca == '3':
                    fabricante = input("Digite o fabricante: ")
                    cursor.execute(
                        "SELECT * FROM medicamento WHERE fabricante LIKE %s", ('%' + fabricante + '%',))
                    medicamentos = cursor.fetchall()
                    if medicamentos:
                        table = PrettyTable()
                        table.field_names = [
                            "ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]
                        for medicamento in medicamentos:
                            table.add_row(
                                [medicamento[0], medicamento[1], medicamento[2], medicamento[3], medicamento[4]])
                        print(table)
                    else:
                        print("Nenhum medicamento encontrado para esse fabricante.")

                elif opcao_busca == '4':
                    faixa_preco = float(input("Digite o preço máximo: "))
                    cursor.execute(
                        "SELECT * FROM medicamento WHERE preco <= %s", (faixa_preco,))
                    medicamentos = cursor.fetchall()
                    if medicamentos:
                        table = PrettyTable()
                        table.field_names = [
                            "ID", "Nome", "Fabricante", "Estoque", "Preço (R$)"]
                        for medicamento in medicamentos:
                            table.add_row(
                                [medicamento[0], medicamento[1], medicamento[2], medicamento[3], medicamento[4]])
                        print(table)
                    else:
                        print(
                            "Nenhum medicamento encontrado dentro dessa faixa de preço.")

                elif opcao_busca == '5':
                    cursor.execute("SELECT * FROM medicamento")
                    medicamentos = cursor.fetchall()
                    table = PrettyTable()
                    table.field_names = ["ID", "Nome",
                                         "Fabricante", "Estoque", "Preço (R$)"]
                    for medicamento in medicamentos:
                        table.add_row(
                            [medicamento[0], medicamento[1], medicamento[2], medicamento[3], medicamento[4]])
                    print(table)

                elif opcao_busca == '6':
                    break
                else:
                    print("Opção inválida! Tente novamente.")

        elif opcao == '3':
            cursor.execute("SELECT * FROM estoque_baixo")
            medicamentos_baixo_estoque = cursor.fetchall()
            if medicamentos_baixo_estoque:
                print("Medicamentos com menos de 5 unidades no estoque:")
                table = PrettyTable()
                table.field_names = ["ID", "Nome",
                                     "Fabricante", "Estoque", "Preço (R$)"]
                for medicamento in medicamentos_baixo_estoque:
                    table.add_row([medicamento[0], medicamento[1],
                                  medicamento[2], medicamento[3], medicamento[4]])
                print(table)
            else:
                print("Nenhum medicamento com estoque baixo.")

        elif opcao == '4':
            cursor.execute("SELECT * FROM estoque_zerado")
            medicamentos_zerados = cursor.fetchall()
            if medicamentos_zerados:
                print("Medicamentos com estoque zerado:")
                table = PrettyTable()
                table.field_names = ["ID", "Nome", "Fabricante", "Preço (R$)"]
                for medicamento in medicamentos_zerados:
                    table.add_row([medicamento[0], medicamento[1],
                                  medicamento[2], medicamento[3]])
                print(table)
            else:
                print("Nenhum medicamento com estoque zerado.")

        elif opcao == '5':
            cursor.execute("SELECT id_ven FROM vendedor WHERE id_ven = %s", (id_vendedor,))
            vendedor = cursor.fetchone()

            if vendedor:
                id_vendedor = vendedor[0]  # Extrai o valor de 'id_ven' da tupla
                print(id_vendedor)
                confirmar_compras(id_vendedor)
            else:
                print("Vendedor não encontrado.")


        elif opcao == '6':
            print("Retornando ao Menu Inicial...\n")
            break

        else:
            print("Opção inválida! Tente novamente.")

    cursor.close()
    db.close()

def confirmar_compras(id_vendedor):
    db = conectar_banco()
    cursor = db.cursor()

    while True:
        print("\n=== Confirmar Compras ===")
        cursor.execute(
            "SELECT * FROM compra WHERE id_ven = %s AND status_pagamento = 'pendente'", (id_vendedor,))
        compras_pendentes = cursor.fetchall()


        if compras_pendentes:
            print("Compras pendentes:")
            table = PrettyTable()
            table.field_names = ["ID Compra", "ID Cliente", "Data", "Status"]
            for compra in compras_pendentes:
                table.add_row([compra[0], compra[1], compra[2], compra[3]])
            print(table)

            id_compra = int(input("Digite o ID da compra que deseja confirmar (ou 0 para voltar): "))
            if id_compra == 0:
                break

            try:
                # Corrige a query para buscar as colunas necessárias
                cursor.execute("SELECT id_med, quantidade FROM compra WHERE id_compra = %s", (id_compra,))
                dados_compra = cursor.fetchone()

                if dados_compra:  # Verifica se a compra existe
                    id_medicamento = dados_compra[0]  # id_med é o primeiro
                    quantidade = dados_compra[1]  # quantidade é o segundo

                    # Atualiza o status da compra para 'confirmada'
                    cursor.execute(
                        "UPDATE compra SET status_pagamento = 'confirmada' WHERE id_compra = %s AND id_ven = %s",
                        (id_compra, id_vendedor,)
                    )

                    # Atualiza o estoque do medicamento
                    cursor.execute(
                        "UPDATE medicamento SET estoque = estoque - %s WHERE id_med = %s",
                        (quantidade, id_medicamento,)
                    )

                    db.commit()
                    print("Compra confirmada com sucesso!")
                else:
                    print("Compra não encontrada ou já confirmada.")

            except Exception as e:
                print(f"Erro ao confirmar compra: {e}")
                db.rollback()  # Desfaz alterações em caso de erro

        else:
            print("Não há compras pendentes.")
            break

    cursor.close()
    db.close()
