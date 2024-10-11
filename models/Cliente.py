class Cliente:
    def __init__(self, id_cli, cpf_cli, nome_cli, email_cli, senha_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece):
        self.id_cli = id_cli
        self.cpf_cli = cpf_cli
        self.nome_cli = nome_cli
        self.email_cli = email_cli
        self.senha_cli = senha_cli
        self.telefone_cli = telefone_cli
        self.cidade_cli = cidade_cli
        self.torce_flamengo = torce_flamengo
        self.assiste_one_piece = assiste_one_piece

    def __str__(self):
        return f"Cliente: {self.nome_cli} - Email: {self.email_cli} - Cidade: {self.cidade_cli}"

    def verificar_preferencias(self):
        flamengo = "torce" if self.torce_flamengo else "não torce"
        one_piece = "assiste" if self.assiste_one_piece else "não assiste"
        return f"O cliente {flamengo} para o Flamengo e {one_piece} One Piece."
