class Gerente:
    def __init__(self, id_ger, cpf_ger, nome_ger, email_ger, senha_ger, cidade_ger, telefone_ger):
        self.id_ger = id_ger
        self.cpf_ger = cpf_ger
        self.nome_ger = nome_ger
        self.email_ger = email_ger
        self.senha_ger = senha_ger
        self.cidade_ger = cidade_ger
        self.telefone_ger = telefone_ger

    def __str__(self):
        return f"Gerente: {self.nome_ger} - Email: {self.email_ger} - Cidade: {self.cidade_ger}"

    def atualizar_preco_medicamento(self, medicamento, novo_preco):
        medicamento.preco = novo_preco
        print(f"Preço do medicamento {medicamento.nome_med} atualizado para R${novo_preco:.2f}.")
