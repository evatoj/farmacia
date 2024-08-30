# Criação da tabela "medicamentos" e suas respectivas colunas
DROP TABLE IF EXISTS `medicamentos`;

CREATE TABLE farmacia.medicamentos (
  idMedicamento INT NOT NULL AUTO_INCREMENT,
  nome_medicamento VARCHAR(50) NULL,
  fabricante VARCHAR(50) NULL,
  quantidade INT NULL,
  valor DECIMAL(10,2) NULL,
  PRIMARY KEY (idMedicamento)
  UNIQUE KEY `idMedicamento` (`idMedicamento`));