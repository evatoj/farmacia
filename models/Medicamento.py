class Medicamento:
    def __init__(self, id_med, nome_med, fabricante, estoque, preco):
        self.id_med = id_med
        self.nome_med = nome_med
        self.fabricante = fabricante
        self.estoque = estoque
        self.preco = preco

    def __str__(self):
        return f"Medicamento: {self.nome_med} - Fabricante: {self.fabricante} - Preço: R${self.preco:.2f}"
    
    def atualizar_estoque(self, quantidade):
        if quantidade < 0 and abs(quantidade) > self.estoque:
            print(f"Não há estoque suficiente de {self.nome_med}.")
        else:
            self.estoque += quantidade
            print(f"Estoque de {self.nome_med} atualizado para {self.estoque}.")
