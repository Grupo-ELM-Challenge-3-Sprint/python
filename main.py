from core.cadastro_login_senha import cadastrar_usuario, fazer_login, recuperar_senha
from core.menu import *

# Loop principal do sistema
# Executa o menu principal e direciona para as funções conforme a escolha do usuário
if __name__ == "__main__":
    while True:
        opcao_principal = mostrar_menu_principal()

        if opcao_principal == '1':
            cadastrar_usuario()

        elif opcao_principal == '2':
            usuario_logado = fazer_login()
            if usuario_logado:
                menu_usuario_logado(usuario_logado)
            else:  # Login falhou PRECISAMOS ARRUMAR ESSE LOGIN... POIS ELE PARA O LOGIN SE INSERIR UM CPF COM 11 DÍGITOS QUE NÃO EXISTE
                input("\nPressione Enter para voltar ao menu principal...")

        elif opcao_principal == '3':
            recuperar_senha()

        elif opcao_principal == '4':
            mostrar_menu_ajuda_principal()

        elif opcao_principal == '0':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção do menu.")
            input("\nPressione Enter para tentar novamente...")
