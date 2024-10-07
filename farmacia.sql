CREATE DATABASE IF NOT EXISTS farmacia;
USE farmacia;
CREATE TABLE  IF NOT EXISTS cliente (
  id_cli int NOT NULL AUTO_INCREMENT
  cpf_cli varchar(11) NOT NULL,
  nome_cli varchar(255) NOT NULL,
  email_cli varchar(255) NOT NULL,
  senha_cli varchar(255) NOT NULL,
  telefone_cli varchar(20) DEFAULT NULL,
  cidade_cli varchar(100) NOT NULL,
  torce_flamengo tinyint(1) NOT NULL,
  assiste_one_piece tinyint(1) NOT NULL,
  PRIMARY KEY (id_cli),
  UNIQUE KEY email_cli (email_cli)
);
USE farmacia;
CREATE TABLE IF NOT EXISTS medicamento (
  id_med int NOT NULL AUTO_INCREMENT,
  nome_med varchar(50) DEFAULT NULL,
  fabricante varchar(50) DEFAULT NULL,
  estoque int DEFAULT NULL,
  preco decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (id_med),
  UNIQUE KEY idMedicamento_UNIQUE (id_med)
);
USE farmacia;
CREATE TABLE IF NOT EXISTS vendedor (
  id_ven int NOT NULL AUTO_INCREMENT
  cpf_ven varchar(11) NOT NULL,
  nome_ven varchar(255) NOT NULL,
  email_ven varchar(255) NOT NULL,
  senha_ven varchar(255) NOT NULL,
  telefone_ven varchar(20) DEFAULT NULL,
  PRIMARY KEY (id_ven),
  UNIQUE KEY email_ven (email_ven)
);

-- stored procedure para relatorio mensal do vendedor
DELIMITER //
CREATE PROCEDURE relatorio_mensal_vendedor(IN vendedor_id INT, IN ano_mes VARCHAR(7))
BEGIN
    SELECT 
        v.id_ven,
        ven.nome_ven AS nome_ven,
        DATE_FORMAT(v.data_venda, '%Y-%m') AS mes_venda,
        COUNT(v.id) AS total_vendas,
        SUM(iv.quantidade) AS total_itens_vendidos,
        SUM(iv.quantidade * iv.preco_unitario) AS total_valor
    FROM vendas v
    JOIN vendedor ven ON v.id_ven = ven.id_ven
    JOIN itens_venda iv ON iv.venda_id = v.id
    WHERE v.id_ven = id_ven AND DATE_FORMAT(v.data_venda, '%Y-%m') = ano_mes
    GROUP BY v.id_ven, mes_venda;
END //
DELIMITER ;
