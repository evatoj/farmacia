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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- Tabela cliente --

CREATE TABLE `cliente` (
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- Tabela vendedor --

CREATE TABLE `vendedor` (
  `id_ven` int NOT NULL AUTO_INCREMENT,
  `cpf_ven` varchar(11) NOT NULL,
  `nome_ven` varchar(255) NOT NULL,
  `email_ven` varchar(255) NOT NULL,
  `senha_ven` varchar(255) NOT NULL,
  `telefone_ven` varchar(20) DEFAULT NULL,
  `cidade_ven` varchar(100) NOT NULL,
  `salario_ven` decimal(10,2) NOT NULL,
  `status_ven` tinyint DEFAULT '1',
  PRIMARY KEY (`id_ven`),
  UNIQUE KEY `email_ven` (`email_ven`),
  UNIQUE KEY `cpf_ven_UNIQUE` (`cpf_ven`),
  UNIQUE KEY `id_ven_UNIQUE` (`id_ven`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- Tabela gerente --

CREATE TABLE `gerente` (
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci