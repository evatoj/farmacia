class Vendedor:
    def __init__(self, id_ven, cpf_ven, nome_ven, email_ven, senha_ven, telefone_ven, cidade_ven):
        self.id_ven = id_ven
        self.cpf_ven = cpf_ven
        self.nome_ven = nome_ven
        self.email_ven = email_ven
        self.senha_ven = senha_ven
        self.telefone_ven = telefone_ven
        self.cidade_ven = cidade_ven

    def __str__(self):
        return f"Vendedor: {self.nome_ven} - Email: {self.email_ven} - Cidade: {self.cidade_ven}"

    def vender_medicamento(self, medicamento, quantidade):
        if medicamento.estoque >= quantidade:
            medicamento.atualizar_estoque(-quantidade)
            print(f"Vendido {quantidade}x {medicamento.nome_med}.")
        else:
            print(f"Estoque insuficiente de {medicamento.nome_med}.")
