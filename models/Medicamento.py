class Medicamento:
    def __init__(self, id_med, nome_med, fabricante, estoque, preco):
        self.id_med = id_med
        self.nome_med = nome_med
        self.fabricante = fabricante
        self.estoque = estoque
        self.preco = preco

    def __str__(self):
        return f"Medicamento: {self.nome_med} - Fabricante: {self.fabricante} - Preço: R${self.preco:.2f}"
