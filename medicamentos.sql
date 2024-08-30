# Criação da tabela "medicamentos" e suas respectivas colunas
DROP TABLE IF EXISTS `medicamentos`;

CREATE TABLE `medicamentos` (
  `idMedicamento` int NOT NULL AUTO_INCREMENT,
  `nome_medicamento` varchar(50) DEFAULT NULL,
  `fabricante` varchar(50) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idMedicamento`),
  UNIQUE KEY `idMedicamento_UNIQUE` (`idMedicamento`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci