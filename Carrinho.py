class Carrinho:
    def __init__(self):
        self.itens = {}  # Dicionário para armazenar medicamentos e suas quantidades

    def adicionar_medicamento(self, medicamento, quantidade):
        if medicamento.nome in self.itens:
            self.itens[medicamento.nome]["quantidade"] += quantidade
        else:
            self.itens[medicamento.nome] = {"medicamento": medicamento, "quantidade": quantidade}
        print(f"Adicionado {quantidade}x {medicamento.nome} ao carrinho.")

    def remover_medicamento(self, medicamento, quantidade):
        if medicamento.nome in self.itens:
            if self.itens[medicamento.nome]["quantidade"] > quantidade:
                self.itens[medicamento.nome]["quantidade"] -= quantidade
                print(f"Removido {quantidade}x {medicamento.nome} do carrinho.")
            elif self.itens[medicamento.nome]["quantidade"] == quantidade:
                del self.itens[medicamento.nome]
                print(f"{medicamento.nome} removido do carrinho.")
            else:
                print(f"Não é possível remover {quantidade}x {medicamento.nome}, quantidade insuficiente.")
        else:
            print(f"{medicamento.nome} não está no carrinho.")

    def consultar_medicamentos(self):
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            print("Medicamentos no carrinho:")
            for item in self.itens.values():
                medicamento = item["medicamento"]
                quantidade = item["quantidade"]
                print(f"{quantidade}x {medicamento}")

    def valor_total(self):
        total = sum(item["medicamento"].preco * item["quantidade"] for item in self.itens.values())
        return total