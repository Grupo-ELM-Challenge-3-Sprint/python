from database.dados import _dados_de_usuarios
from core.cadastro_login_senha import cadastrar_usuario, fazer_login, recuperar_senha
from core.crud import submenu_crud_agendas
from core import guia_interativo_e_ia
from core.tutoriais import *


# Lista para armazenar os dados dos usuários (referência aos dados do módulo 'dados')
lista_de_usuarios = _dados_de_usuarios

modo_guia_interativo_ativo = False


# Função para exibir o menu principal do sistema
# Mostra opções de cadastro, login, ajuda e sair
# Também exibe dicas se o modo guia estiver ativo
# Menu Principal
def mostrar_menu_principal():
    global modo_guia_interativo_ativo
    print("\n" + "=" * 42)
    print("    BEM-VINDO AO SIMPLESHC      ")
    print("=" * 42)
    print("1. Cadastro de Novo Usuário")
    print("2. Login (Entrar no Sistema)")
    print("3. Recuperar Senha")
    print("4. Ajuda e Informações Gerais")
    print("0. Sair do Sistema")
    print("=" * 42)

    escolha = input("Escolha uma opção: ")

    return escolha


# Chamar tutoriais:

# =============================================================================
# FUNÇÃO PRINCIPAL DO MENU DO USUÁRIO
# =============================================================================

# Função para exibir o menu do usuário após login
# Permite acessar tutoriais, ajuda e suporte
# Menu Usuário
def menu_usuario_logado(usuario_logado):
    global modo_guia_interativo_ativo
    nome_usuario = usuario_logado["nome"]
    email_usuario = usuario_logado["email"]

    while True:
        print("\n╔══════════════════════════════════════════════╗")
        print(f"║  MENU DO USUÁRIO: {nome_usuario[:20]:<26} ║")
        if modo_guia_interativo_ativo:
            print("║         ⭐ Modo Guia Interativo ATIVO ⭐        ║")
        print("╚══════════════════════════════════════════════╝\n")
        
        print("1. Tutorial de como cadastrar no App HC")
        print("2. Tutorial de como logar no App HC")
        print("3. Tutorial Esqueci minha Senha no App HC")
        print("4. Tutorial de como acessar Resultados de Exames")
        print("5. Tutorial de como acessar Receitas Médicas")
        print("6. Tutorial de como acessar Minhas Agendas (Consultas/Exames Marcados)")
        print("7. Tutorial de como acessar as Teleconsulta")
        print("8. Tutorial de como acessar Solicitação de Exames")
        print("9. Tutorial de como acessar Solicitação de Documentos")
        print("10. Tutorial de como acessar os Meus Dados")
        print("11. IA e Guia Interativo")
        print("12. CRUD - Minhas Agendas")
        print("0. Sair (Logout)")
        print("=" * 46)

        opcao_login = input("Digite o número da opção desejada e pressione Enter: ")

        # Cada bloco abaixo trata uma opção do menu do usuário
        if opcao_login == '1':  # Tutorial de Cadastro
            tutorial_cadastro(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '2':  # Tutorial de Login
            tutorial_login(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '3':  # Tutorial Esqueci Senha
            tutorial_esqueci_senha(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '4':  # Tutorial de Resultados
            tutorial_resultados(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '5':  # Tutorial de Receitas
            tutorial_receitas(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '6':  # Tutorial de Agendas
            tutorial_agendas(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '7':  # Tutorial de Teleconsulta
            tutorial_teleconsulta(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '8':  # Solicitação de Exames (HC)
            tutorial_solicitacao_exames(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '9':  # Solicitação de Documentos (HC)
            tutorial_solicitacao_documentos(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '10':  # Meus Dados
            tutorial_meus_dados(modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '11':  # IA e Guia Interativo
            modo_guia_interativo_ativo = guia_interativo_e_ia.guia_interativo_e_ia(modo_guia_interativo_ativo)

        elif opcao_login == '12':  # CRUD Agendas
            submenu_crud_agendas(email_usuario)

        elif opcao_login == '0':
            print(f"\nSaindo do seu usuário... Até logo, {nome_usuario}!")
            break
        
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida do menu.")
            if modo_guia_interativo_ativo:
                print("[Guia]: Certifique-se de digitar apenas o número da opção desejada (ex: 3, 4, 5...).")


# Loop principal do sistema
# Executa o menu principal e direciona para as funções conforme a escolha do usuário
if __name__ == "__main__":
    while True:
        opcao_principal = mostrar_menu_principal()

        if opcao_principal == '1':
            cadastrar_usuario()
            input("\nPressione Enter para voltar ao menu principal...")

        elif opcao_principal == '2':
            usuario_logado = fazer_login()
            if usuario_logado:
                menu_usuario_logado(usuario_logado)
            else:  # Login falhou
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
