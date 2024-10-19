-- Todas as views (até então) do sistema --
-- Lembre-se de utilizar USE farmacia; antes de criar cada view no schema --

-- View para verificar produtos com estoque disponível --

CREATE VIEW estoque_disponivel AS
SELECT *
FROM medicamento
WHERE estoque > 0;

-- View para verificar produtos com estoque menor que 5 --

CREATE VIEW estoque_baixo AS
SELECT *
FROM medicamento
WHERE estoque < 5;


-- View para verificar apenas produtos com estoque zerado --

CREATE VIEW estoque_zerado AS
SELECT *
FROM medicamento
WHERE estoque = 0;

-- View para verificar vendedores demitidos (status_ven = 0) --

CREATE VIEW vendedor_demitido AS
SELECT id_ven, cpf_ven, nome_ven, email_ven, cidade_ven, telefone_ven
FROM vendedor
WHERE status_ven = 0;

-- View para verificar compras pendentes do cliente logado --

CREATE VIEW compra_pendente AS
SELECT id_compra, id_cli, id_ven, forma_pagamento, valor_total
FROM compra
WHERE status_com = 'pendente';
