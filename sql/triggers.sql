-- Trigger para automatizar o decremento do estoque de um medicamento após a confirmação de uma compra --

DELIMITER //

CREATE TRIGGER atualizar_estoque
AFTER UPDATE ON compra
FOR EACH ROW
BEGIN
    IF OLD.status_com = 'pendente' AND NEW.status_com = 'confirmada' THEN
        UPDATE medicamento
        SET estoque = estoque - (
            SELECT ic.quantidade
            FROM item_compra ic
            WHERE ic.id_compra = NEW.id_compra AND ic.id_med = medicamento.id_med
        )
        WHERE id_med IN (
            SELECT id_med
            FROM item_compra
            WHERE id_compra = NEW.id_compra
        );
    END IF;
END //

DELIMITER ;
