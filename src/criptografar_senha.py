import bcrypt


def gerar_senha_criptografada(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')


senha = 'poderosochefao1'
senha_criptografada = gerar_senha_criptografada(senha)
print("Senha criptografada:", senha_criptografada)
