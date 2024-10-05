from conexao import conectar_banco
import bcrypt


def gerar_senha_criptografada(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash.decode('utf-8')


def solicitar_input_valido(pergunta):
    while True:
        resposta = input(pergunta).lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Entrada inválida! Por favor, digite 's' para sim ou 'n' para não.")


def cadastrar_cliente():
    db = conectar_banco()
    cursor = db.cursor()

    cpf = input("Digite o CPF do cliente (somente números): ")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    senha = input("Digite a senha do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cidade = input("Digite a cidade do cliente: ")

    torce_flamengo = solicitar_input_valido(
        "O cliente torce para o Flamengo? (s/n): ")
    assiste_one_piece = solicitar_input_valido(
        "O cliente assiste One Piece? (s/n): ")

    senha_criptografada = gerar_senha_criptografada(senha)

    cursor.execute("""
        INSERT INTO cliente (cpf_cli, nome_cli, email_cli, senha_cli, telefone_cli, cidade_cli, torce_flamengo, assiste_one_piece)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (cpf, nome, email, senha_criptografada, telefone, cidade, torce_flamengo, assiste_one_piece))

    db.commit()
    print("Cliente cadastrado com sucesso!")

    cursor.close()
    db.close()
