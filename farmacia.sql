CREATE DATABASE IF NOT EXISTS farmacia;
USE farmacia;

CREATE TABLE IF NOT EXISTS medicamento (
  medicamento_id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  categoria VARCHAR(255),
  preco DECIMAL(10, 2) NOT NULL,
  quantidade_em_estoque INT NOT NULL,
  fabricado_em_mari BOOLEAN
)

CREATE TABLE IF NOT EXISTS cliente (
  cliente_id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255),
  email VARCHAR(255),
  telefone VARCHAR(50),
  torcedor_flamengo BOOLEAN,
  assiste_one_piece BOOLEAN,
  cidade VARCHAR(255)
)

CREATE TABLE IF NOT EXISTS vendedor (
  vendedor_id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255)
)

CREATE TABLE IF NOT EXISTS venda (
  venda_id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  vendedor_id INT,
  data_venda DATE,
  forma_pagamento VARCHAR(50),
  status_pagamento VARCHAR(50),
  desconto_aplicado DECIMAL(10, 2),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id),
  FOREIGN KEY (vendedor_id) REFERENCES vendedor(vendedor_id)
)

CREATE TABLE IF NOT EXISTS itemVenda (
  item_venda_id INT AUTO_INCREMENT PRIMARY KEY,
  venda_id INT,
  medicamento_id INT,
  quantidade INT,
  preco_unitario DECIMAL(10, 2),
  total_item DECIMAL(10, 2),
  FOREIGN KEY (venda_id) REFERENCES venda(venda_id),
  FOREIGN KEY (medicamento_id) REFERENCES medicamento(medicamento_id)
)

CREATE TABLE IF NOT EXISTS estoque (
  estoque_id INT AUTO_INCREMENT PRIMARY KEY,
  medicamento_id INT,
  quantidade_disponivel INT,
  FOREIGN KEY (medicamento_id) REFERENCES medicamento(medicamento_id)
)
