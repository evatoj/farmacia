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
