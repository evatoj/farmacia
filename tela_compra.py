from conexao import conectar_banco

def tela_compra(email_cliente, carrinho):
    print("\n=== Confirmação de Compra ===")
    print("Itens no carrinho:")
    for id_med, quantidade in carrinho.items():
        print(f"ID: {id_med}, Quantidade: {quantidade}")

    opcao = input("\nDeseja confirmar a compra? (s/n): ").lower()
    
    if opcao == 's':
        nome_vendedor = input("Digite o nome do vendedor: ")
        processar_compra(email_cliente, carrinho, nome_vendedor)
    elif opcao == 'n':
        print("Compra cancelada.")
    else:
        print("Opção inválida. Retornando ao menu anterior.")

def processar_compra(email_cliente, carrinho, nome_vendedor):
    db = conectar_banco()
    cursor = db.cursor()

    try:
        # Obter o nome do cliente a partir do email
        cursor.execute("SELECT nome_cli FROM cliente WHERE email_cli = %s", (email_cliente,))
        cliente = cursor.fetchone()
        if not cliente:
            print("Cliente não encontrado.")
            return
        nome_cliente = cliente[0]

        # Para cada item no carrinho, atualize o estoque e registre a compra
        for id_med, quantidade in carrinho.items():
            cursor.execute("SELECT estoque FROM medicamento WHERE id_med = %s", (id_med,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0] >= quantidade:
                # Atualiza o estoque do medicamento
                cursor.execute("UPDATE medicamento SET estoque = estoque - %s WHERE id_med = %s", (quantidade, id_med))

                # Registrar a compra na tabela "compra"
                cursor.execute("""
                    INSERT INTO compra (nome_vendedor, nome_cliente, medicamento, quantidade)
                    VALUES (%s, %s, %s, %s)
                """, (nome_vendedor, nome_cliente, id_med, quantidade))
                
                print(f"Compra de {quantidade}x do medicamento ID {id_med} registrada com sucesso.")
            else:
                print(f"Estoque insuficiente para o medicamento ID {id_med}. Compra abortada.")
                db.rollback()
                return

        db.commit()
        print("Compra efetuada com sucesso!")
    except Exception as e:
        db.rollback()
        print(f"Erro durante o processamento da compra: {e}")
    finally:
        cursor.close()
        db.close()
