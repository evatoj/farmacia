from cadastrar_cliente import cadastrar_cliente
from cadastrar_vendedor import cadastrar_vendedor
from login_cliente import login_cliente
from login_vendedor import login_vendedor
from tela_vendedor import tela_vendedor
from tela_anonima import tela_anonima


def main():
    while True:
        print("=== Farmácia Drogue-CI ===")
        print("1. Cadastrar Cliente")
        print("2. Contratar Vendedor")
        print("3. Login Cliente")
        print("4. Login Vendedor")
        print("5. Navegação Anônima")
        print("6. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_vendedor()
        elif opcao == '3':
            login_cliente()
        elif opcao == '4':
            if login_vendedor():
                tela_vendedor()
        elif opcao == '5':
            tela_anonima()
        elif opcao == '6':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
