DROP TABLE IF EXISTS `medicamentos`;

CREATE TABLE farmacia.medicamentos (
  idMedicamento INT NOT NULL AUTO_INCREMENT,
  nome_medicamento VARCHAR(45) NULL,
  fabricante VARCHAR(45) NULL,
  quantidade INT NULL,
  valor DECIMAL(10,2) NULL,
  PRIMARY KEY (idMedicamento)
  UNIQUE KEY `idMedicamento` (`idMedicamento`));