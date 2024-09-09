import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='farmacia',
            user='root',
            password='root'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
    return None

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        cliente_id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255),
        email VARCHAR(255),
        telefone VARCHAR(50),
        torcedor_flamengo BOOLEAN,
        assiste_one_piece BOOLEAN,
        cidade VARCHAR(255)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        produto_id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        categoria VARCHAR(255),
        preco DECIMAL(10, 2) NOT NULL,
        quantidade_em_estoque INT NOT NULL,
        fabricado_em_mari BOOLEAN
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vendedor (
        vendedor_id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Venda (
        venda_id INT AUTO_INCREMENT PRIMARY KEY,
        cliente_id INT,
        vendedor_id INT,
        data_venda DATE,
        forma_pagamento VARCHAR(50),
        status_pagamento VARCHAR(50),
        desconto_aplicado DECIMAL(10, 2),
        FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor(vendedor_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ItemVenda (
        item_venda_id INT AUTO_INCREMENT PRIMARY KEY,
        venda_id INT,
        produto_id INT,
        quantidade INT,
        preco_unitario DECIMAL(10, 2),
        total_item DECIMAL(10, 2),
        FOREIGN KEY (venda_id) REFERENCES Venda(venda_id),
        FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estoque (
        estoque_id INT AUTO_INCREMENT PRIMARY KEY,
        produto_id INT,
        quantidade_disponivel INT,
        FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
    )
    """)
    connection.commit()

def insert_cliente(connection):
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    torcedor_flamengo = input("É torcedor do Flamengo? (s/n): ").lower() == 's'
    assiste_one_piece = input("Assiste One Piece? (s/n): ").lower() == 's'
    cidade = input("Digite a cidade (ex: Sousa): ")

    cursor = connection.cursor()
    query = """
    INSERT INTO Cliente (nome, endereco, email, telefone, torcedor_flamengo, assiste_one_piece, cidade)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome, endereco, email, telefone, torcedor_flamengo, assiste_one_piece, cidade))
    connection.commit()
    print("Cliente inserido com sucesso!")


def select_produto(connection, nome=None, categoria=None, preco_min=None, preco_max=None):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM Produto WHERE 1=1"
    params = []
    if nome:
        query += " AND nome LIKE %s"
        params.append(f"%{nome}%")
    if categoria:
        query += " AND categoria = %s"
        params.append(categoria)
    if preco_min:
        query += " AND preco >= %s"
        params.append(preco_min)
    if preco_max:
        query += " AND preco <= %s"
        params.append(preco_max)
    cursor.execute(query, params)
    return cursor.fetchall()

def insert_venda(connection, cliente_id, vendedor_id, forma_pagamento, status_pagamento, desconto_aplicado, itens):
    cursor = connection.cursor()
    cursor.execute("START TRANSACTION")
    
    # insert venda
    query_venda = """
    INSERT INTO Venda (cliente_id, vendedor_id, data_venda, forma_pagamento, status_pagamento, desconto_aplicado)
    VALUES (%s, %s, NOW(), %s, %s, %s)
    """
    cursor.execute(query_venda, (cliente_id, vendedor_id, forma_pagamento, status_pagamento, desconto_aplicado))
    venda_id = cursor.lastrowid
    
    # insert itens da venda e atualizar estoque
    for item in itens:
        produto_id = item['produto_id']
        quantidade = item['quantidade']
        
        cursor.execute("SELECT quantidade_em_estoque FROM Produto WHERE produto_id = %s", (produto_id,))
        quantidade_em_estoque = cursor.fetchone()[0]
        
        if quantidade_em_estoque < quantidade:
            print("Estoque insuficiente para o produto", produto_id)
            cursor.execute("ROLLBACK")
            return False
        
        preco_unitario = item['preco_unitario']
        total_item = quantidade * preco_unitario
        
        query_item_venda = """
        INSERT INTO ItemVenda (venda_id, produto_id, quantidade, preco_unitario, total_item)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query_item_venda, (venda_id, produto_id, quantidade, preco_unitario, total_item))
        
        query_update_estoque = """
        UPDATE Produto SET quantidade_em_estoque = quantidade_em_estoque - %s
        WHERE produto_id = %s
        """
        cursor.execute(query_update_estoque, (quantidade, produto_id))
    
    cursor.execute("COMMIT")
    return True

if __name__ == "__main__":
    conn = connect()
    if conn:
        create_tables(conn)
        
        # Exemplo de inserção de cliente
        insert_cliente(conn, "João Silva", "Rua A, 123", "joao@gmail.com", "123456789", True, True, "Sousa")
        
        # Exemplo de consulta de produtos
        produtos = select_produto(conn, nome="Paracetamol")
        print(produtos)
        
        # Exemplo de inserção de venda
        itens = [
            {'produto_id': 1, 'quantidade': 2, 'preco_unitario': 15.00},
            {'produto_id': 2, 'quantidade': 1, 'preco_unitario': 30.00}
        ]
        insert_venda(conn, cliente_id=1, vendedor_id=1, forma_pagamento="Cartão", status_pagamento="Confirmado", desconto_aplicado=5.00, itens=itens)
        
        conn.close()
