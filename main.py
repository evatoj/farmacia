from cadastrar_cliente import cadastrar_cliente
from login_cliente import login_cliente
from login_vendedor import login_vendedor
from login_gerente import login_gerente
from tela_vendedor import tela_vendedor
from tela_anonima import tela_anonima
from tela_cliente import tela_cliente
from tela_gerente import tela_gerente


def main():
    while True:
        print("=== Farmácia Drogue-CI ===")
        print("1. Cadastrar Cliente")
        print("2. Login Cliente")
        print("3. Login Vendedor")
        print("4. Login Gerente")
        print("5. Navegação Anônima")
        print("6. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("=== Cadastro de Cliente ===")
            cadastrar_cliente()
        elif opcao == '2':
            print("=== Login do Cliente ===")
            email_cliente = login_cliente()
            if email_cliente:
                tela_cliente(email_cliente)
        elif opcao == '3':
            print("=== Login do Vendedor ===")
            if login_vendedor():
                tela_vendedor()
        elif opcao == '4':
            print("=== Login do Gerente ===")
            if login_gerente():
                tela_gerente()
        elif opcao == '5':
            tela_anonima()
        elif opcao == '6':
            print("Agradecemos pela sua preferência :D\nEncerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
