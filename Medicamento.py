class Medicamento:
    def __init__(self, nome, fabricante, preco):
        self.nome = nome
        self.fabricante = fabricante
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({self.fabricante}) - R${self.preco:.2f}"