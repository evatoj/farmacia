CREATE DATABASE IF NOT EXISTS farmacia;

USE farmacia;
CREATE TABLE IF NOT EXISTS `medicamento` (
  `id_med` int NOT NULL AUTO_INCREMENT,
  `nome_med` varchar(50) DEFAULT NULL,
  `fabricante` varchar(50) DEFAULT NULL,
  `estoque` int DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_med`),
  UNIQUE KEY `idMedicamento_UNIQUE` (`id_med`)
);

-- Tabela cliente --
USE farmacia;
CREATE TABLE IF NOT EXISTS `cliente` (
  `id_cli` int NOT NULL AUTO_INCREMENT,
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
  UNIQUE KEY `cpf_cli_UNIQUE` (`cpf_cli`),
  UNIQUE KEY `id_cli_UNIQUE` (`id_cli`)
);

-- Tabela vendedor --
USE farmacia;
CREATE TABLE IF NOT EXISTS `vendedor` (
  `id_ven` int NOT NULL AUTO_INCREMENT,
  `cpf_ven` varchar(11) NOT NULL,
  `nome_ven` varchar(255) NOT NULL,
  `email_ven` varchar(255) NOT NULL,
  `senha_ven` varchar(255) NOT NULL,
  `telefone_ven` varchar(20) DEFAULT NULL,
  `cidade_ven` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ven`),
  UNIQUE KEY `email_ven` (`email_ven`),
  UNIQUE KEY `cpf_ven_UNIQUE` (`cpf_ven`),
  UNIQUE KEY `id_ven_UNIQUE` (`id_ven`)
);

-- Tabela gerente --
USE farmacia;
CREATE TABLE IF NOT EXISTS `gerente` (
  `id_ger` int NOT NULL AUTO_INCREMENT,
  `cpf_ger` varchar(11) NOT NULL,
  `nome_ger` varchar(255) NOT NULL,
  `email_ger` varchar(255) NOT NULL,
  `senha_ger` varchar(255) NOT NULL,
  `cidade_ger` varchar(100) NOT NULL,
  `telefone_ger` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_ger`),
  UNIQUE KEY `id_ger_UNIQUE` (`id_ger`),
  UNIQUE KEY `cpf_ger_UNIQUE` (`cpf_ger`),
  UNIQUE KEY `email_ger_UNIQUE` (`email_ger`)
);

USE farmacia;
CREATE TABLE IF NOT EXISTS `compra` (
  `id_compra` INT AUTO_INCREMENT PRIMARY KEY,
  `id_cli` INT,
  `id_ven` INT,
  `data_compra` DATE,
  `id_med` INT,
  `desconto_aplicado` DECIMAL(10, 2),
  `valor_total` DECIMAL(10,2),
  `forma_pagamento` tinyint(1),
  `status_pagamento` tinyint(1),
  FOREIGN KEY (`id_cli`) REFERENCES cliente(`id_cli`),
  FOREIGN KEY (`id_ven`) REFERENCES vendedor(`id_ven`),
  FOREIGN KEY (`id_med`) REFERENCES medicamento(`id_med`)
);
