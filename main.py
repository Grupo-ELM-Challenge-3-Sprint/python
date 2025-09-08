from database.dados import _dados_de_usuarios, _dados_usuarios_servicos
from core.cadastro_e_login import cadastrar_usuario, fazer_login
import core.validacoes as validacoes
import core.ajuda as ajuda 
from core.tutoriais import *
from core.ajuda import menu_ajuda_usuario
from core.crud import submenu_crud_agendas

# Lista para armazenar os dados dos usuários (referência aos dados do módulo 'dados')
lista_de_usuarios = _dados_de_usuarios

# Variável global para controlar o modo guia interativo
modo_guia_interativo_ativo = False


# Função para exibir o menu principal do sistema
# Mostra opções de cadastro, login, ajuda e sair
# Também exibe dicas se o modo guia estiver ativo
# Menu Principal
def mostrar_menu_principal():
    global modo_guia_interativo_ativo  # Para exibir status do guia
    print("\n" + "=" * 42)
    print("    BEM-VINDO AO PORTAL DO PACIENTE HC      ")
    if modo_guia_interativo_ativo:
        print("   Modo Guia Interativo ATIVO ")
        print("  (Mais dicas e ajuda visual ao navegar)")
    print("=" * 42)
    print("1. Cadastro de Novo Usuário")
    print("2. Login (Entrar no Sistema)")
    print("3. Ajuda e Informações Gerais")
    print("0. Sair do Sistema")
    print("=" * 42)

    escolha = input("Escolha uma opção: ")

    #Vamos precisar mudar o GUIA INTERATIVO para outra pasta... dentro de codigo/guia_interativo
    if modo_guia_interativo_ativo and escolha:
        # Dicas básicas para cada opção
        if escolha == '1':
            print("[Guia]: Você escolheu 'Cadastro'. Prepare seu CPF, email e celular.")
        elif escolha == '2':
            print("[Guia]: Você escolheu 'Login'. Tenha em mãos seu CPF e senha.")
        elif escolha == '3':
            print("[Guia]: Você escolheu 'Ajuda'. Aqui você encontrará informações sobre o sistema.")
        elif escolha == '0':
            print("[Guia]: Você escolheu 'Sair'. O sistema será encerrado.")
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
        
        print("1. Tutorial de como cadastrar no app HC")
        print("2. Tutorial de como logar no App HC")
        print("3. Tutorial de como acessar Resultados de Exames")
        print("4. Tutorial de como acessar Receitas Médicas")
        print("5. Tutorial de como acessar Minhas Agendas (Consultas/Exames Marcados)")
        print("6. Tutorial de como acessar as Teleconsulta")
        print("7. Tutorial de como acessar os Meus Dados")
        print("8. Ajuda e Suporte ao Usuário")
        print("9. CRUD - Minhas Agendas (Listar/Adicionar/Atualizar/Excluir)")
        print("0. Sair (Logout)")
        print("=" * 46)

        prompt_text = "Escolha uma opção: "
        if modo_guia_interativo_ativo:
            prompt_text = "[Guia] Digite o número da opção desejada e pressione Enter: "
        opcao_login = input(prompt_text)

        # Cada bloco abaixo trata uma opção do menu do usuário
        if opcao_login == '1':  # Tutorial de Cadastro
            tutorial_cadastro(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '2':  # Tutorial de Login
            tutorial_login(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '3':  # Tutorial de Resultados
            tutorial_resultados(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '4':  # Tutorial de Receitas
            tutorial_receitas(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '5':  # Tutorial de Agendas
            tutorial_agendas(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '6':  # Tutorial de Teleconsulta
            tutorial_teleconsulta(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '7':  # Tutorial de Meus Dados
            tutorial_meus_dados(nome_usuario, modo_guia_interativo_ativo)
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '8':  # Ajuda e Suporte
            modo_guia_interativo_ativo = menu_ajuda_usuario(modo_guia_interativo_ativo)
        elif opcao_login == '9':  # CRUD Agendas
            submenu_crud_agendas(email_usuario)

        elif opcao_login == '0':
            print(f"\nSaindo do seu usuário... Até logo, {nome_usuario}!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida do menu.")
            if modo_guia_interativo_ativo:
                print("[Guia]: Certifique-se de digitar apenas o número da opção desejada (ex: 3, 4, 5...).")




# Função para exibir o menu de ajuda principal (antes do login)
# Mostra informações sobre cadastro, login, sistema e suporte
# Função para o Menu de Ajuda Principal (Antes do Login)

# A gente vai usar isso:

#PARTE DE AJUDA E INFORMAÇÕES, 2° AJUDA do sistema







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
            mostrar_menu_ajuda_principal()

        elif opcao_principal == '0':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção do menu.")
            if modo_guia_interativo_ativo:
                print("[Guia]: Use os números 0, 1, 2 ou 3 para escolher uma opção do menu principal.")
            input("\nPressione Enter para tentar novamente...")
