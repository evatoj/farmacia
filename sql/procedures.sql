-- Stored Procedure para gerar relatório de vendas de um vendedor --

CREATE DEFINER=`root`@`localhost` PROCEDURE `relatorio_venda`(IN idVendedor INT)
BEGIN
    DECLARE total_vendas INT;
    DECLARE total_valor DECIMAL(10, 2);
    DECLARE total_clientes INT;

    SELECT COUNT(*) INTO total_vendas FROM compra
    WHERE id_ven = idVendedor AND status_com = 'confirmada';
    
    SELECT COALESCE(SUM(valor_total), 0) INTO total_valor FROM compra
    WHERE id_ven = idVendedor AND status_com = 'confirmada';

    SELECT COUNT(DISTINCT id_cli) INTO total_clientes FROM compra
    WHERE id_ven = idVendedor AND status_com = 'confirmada';

    SELECT total_vendas, total_valor, total_clientes;

    SELECT forma_pagamento, COUNT(*) AS quantidade
    FROM compra
    WHERE id_ven = idVendedor AND status_com = 'confirmada'
    GROUP BY forma_pagamento;
END