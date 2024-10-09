-- Todas as tabelas (até então) utilizadas no sistema --
-- Lembre-se de utilizar USE farmacia; antes de criar cada tabela no schema --

-- Tabela medicamento --

CREATE TABLE `medicamento` (
  `id_med` int NOT NULL AUTO_INCREMENT,
  `nome_med` varchar(50) DEFAULT NULL,
  `fabricante` varchar(50) DEFAULT NULL,
  `estoque` int DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_med`),
  UNIQUE KEY `idMedicamento_UNIQUE` (`id_med`)
)

-- Tabela cliente --

CREATE TABLE `cliente` (
  `id_cli` int NOT NULL AUTO_INCREMENT
  `cpf_cli` varchar(11) NOT NULL,
  `nome_cli` varchar(255) NOT NULL,
  `email_cli` varchar(255) NOT NULL,
  `senha_cli` varchar(255) NOT NULL,
  `telefone_cli` varchar(20) DEFAULT NULL,
  `cidade_cli` varchar(100) NOT NULL,
  `torce_flamengo` tinyint(1) NOT NULL,
  `assiste_one_piece` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_cli`),
  UNIQUE KEY `email_cli` (`email_cli`),
  UNIQUE KEY `cpf_cli_UNIQUE` (`cpf_cli`)
)

-- Tabela vendedor --

CREATE TABLE `vendedor` (
  `id_ven` int NOT NULL AUTO_INCREMENT
  `cpf_ven` varchar(11) NOT NULL,
  `nome_ven` varchar(255) NOT NULL,
  `email_ven` varchar(255) NOT NULL,
  `senha_ven` varchar(255) NOT NULL,
  `telefone_ven` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_ven`),
  UNIQUE KEY `email_ven` (`email_ven`),
  UNIQUE KEY `cpf_ven_UNIQUE` (`cpf_ven`)
)

CREATE TABLE IF NOT EXISTS compra (
  `id_compra` INT AUTO_INCREMENT PRIMARY KEY,
  `id_cli` INT,
  `id_ven` INT,
  `data_compra` DATE,
  `forma_pagamento` VARCHAR(50),
  `status_pagamento` VARCHAR(50),
  `desconto_aplicado` DECIMAL(10, 2),
  FOREIGN KEY (`id_cli`) REFERENCES cliente(`id_cli`),
  FOREIGN KEY (`id_ven`) REFERENCES vendedor(`id_ven`)
)

CREATE TABLE IF NOT EXISTS itemcompra (
  `item_id_compra` INT AUTO_INCREMENT PRIMARY KEY,
  `id_compra` INT,
  `id_med` INT,
  `quantidade` INT,
  `preco_unitario` DECIMAL(10, 2),
  `total_item` DECIMAL(10, 2),
  FOREIGN KEY (`id_compra`) REFERENCES compra(`id_compra`),
  FOREIGN KEY (`id_med`) REFERENCES medicamento(`id_med`)
)
