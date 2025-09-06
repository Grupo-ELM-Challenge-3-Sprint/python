from assets.dados_cadastro_login.dados import _dados_de_usuarios, _dados_usuarios_servicos
from assets.dados_cadastro_login.cadastro_e_login import cadastrar_usuario, fazer_login
import assets.dados_cadastro_login.validacoes as validacoes

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

    prompt_menu_principal = "Escolha uma opção: "
    if modo_guia_interativo_ativo:
        prompt_menu_principal = "[Guia] Digite o número da opção e pressione Enter: "

    escolha = input(prompt_menu_principal)

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


# =============================================================================
# FUNÇÕES DE TUTORIAIS
# =============================================================================

def tutorial_cadastro(nome_usuario, modo_guia_ativo):
    """Tutorial de como cadastrar no app HC"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║        TUTORIAL: COMO SE CADASTRAR          ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender passo a passo como se cadastrar no sistema!")
    
    print("\n📝 PASSO A PASSO PARA CADASTRO:")
    print("1. No menu principal, escolha a opção '1. Cadastro de Novo Usuário'")
    print("2. Preencha seus dados pessoais:")
    print("   • Nome completo (ex: João Silva Santos)")
    print("   • CPF com 11 números (ex: 12345678901)")
    print("   • Email válido (ex: joao@email.com)")
    print("   • Celular com DDD (ex: 11987654321)")
    print("   • Crie uma senha segura")
    print("3. Confirme sua senha")
    print("4. Aguarde a confirmação de cadastro")
    
    if modo_guia_ativo:
        print("\n[Guia]: 💡 DICAS IMPORTANTES:")
        print("• Tenha seus documentos por perto")
        print("• Use um email que você acessa frequentemente")
        print("• Escolha uma senha que você consiga lembrar")
        print("• Anote seus dados em local seguro")
    
    print("\n✅ Após o cadastro, você poderá fazer login e acessar todos os serviços!")

def tutorial_login(nome_usuario, modo_guia_ativo):
    """Tutorial de como fazer login no app HC"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║         TUTORIAL: COMO FAZER LOGIN           ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como entrar no sistema de forma segura!")
    
    print("\n🔐 PASSO A PASSO PARA LOGIN:")
    print("1. No menu principal, escolha a opção '2. Login (Entrar no Sistema)'")
    print("2. Digite seu CPF (apenas os 11 números)")
    print("3. Digite sua senha")
    print("4. Pressione Enter para confirmar")
    
    if modo_guia_ativo:
        print("\n[Guia]: 💡 DICAS DE SEGURANÇA:")
        print("• Nunca compartilhe sua senha com ninguém")
        print("• Certifique-se de que ninguém está vendo sua tela")
        print("• Se esquecer a senha, contate o suporte")
        print("• Sempre faça logout quando terminar")
    
    print("\n✅ Se os dados estiverem corretos, você será direcionado ao menu do usuário!")

def tutorial_resultados(nome_usuario, modo_guia_ativo):
    """Tutorial de como acessar resultados de exames"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║     TUTORIAL: ACESSAR RESULTADOS DE EXAMES   ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como visualizar seus exames médicos!")
    
    print("\n🔬 COMO ACESSAR SEUS RESULTADOS:")
    print("1. Faça login no sistema")
    print("2. No menu do usuário, escolha a opção '3. Tutorial de como acessar Resultados de Exames'")
    print("3. Seus exames aparecerão listados com data e descrição")
    print("4. Você pode visualizar todos os resultados disponíveis")
    
    if modo_guia_ativo:
        print("\n[Guia]: 📋 INFORMAÇÕES IMPORTANTES:")
        print("• Os resultados ficam disponíveis 24h por dia")
        print("• Você pode acessar de qualquer lugar")
        print("• Os dados são atualizados automaticamente")
    print("• Em caso de dúvidas, consulte seu médico")
    
    print("\n✅ Seus resultados estão sempre seguros e acessíveis!")

def tutorial_receitas(nome_usuario, modo_guia_ativo):
    """Tutorial de como acessar receitas médicas"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║      TUTORIAL: ACESSAR RECEITAS MÉDICAS      ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como consultar suas prescrições médicas!")
    
    print("\n💊 COMO ACESSAR SUAS RECEITAS:")
    print("1. Faça login no sistema")
    print("2. No menu do usuário, escolha a opção '4. Tutorial de como acessar Receitas Médicas'")
    print("3. Suas receitas aparecerão listadas com medicamentos e dosagens")
    print("4. Você pode visualizar todas as prescrições ativas")
    
    if modo_guia_ativo:
        print("\n[Guia]: ⚠️ CUIDADOS IMPORTANTES:")
        print("• Siga exatamente as instruções do médico")
        print("• Respeite os horários e quantidades")
        print("• Em caso de dúvidas, consulte seu farmacêutico")
        print("• Guarde as receitas em local seguro")
    
    print("\n✅ Suas receitas ficam sempre disponíveis para consulta!")

def tutorial_agendas(nome_usuario, modo_guia_ativo):
    """Tutorial de como acessar agendas de consultas e exames"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║    TUTORIAL: ACESSAR AGENDAS E CONSULTAS     ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como gerenciar seus compromissos médicos!")
    
    print("\n📅 COMO ACESSAR SUAS AGENDAS:")
    print("1. Faça login no sistema")
    print("2. No menu do usuário, escolha a opção '5. Tutorial de como acessar Minhas Agendas'")
    print("3. Suas consultas e exames aparecerão com data, hora e especialidade")
    print("4. Você pode visualizar todos os agendamentos futuros")
    
    if modo_guia_ativo:
        print("\n[Guia]: ⏰ LEMBRETES ÚTEIS:")
        print("• Chegue com 15 minutos de antecedência")
        print("• Leve documentos e exames anteriores")
        print("• Em caso de desistência, cancele com antecedência")
        print("• Mantenha seus dados sempre atualizados")
    
    print("\n✅ Nunca perca um compromisso médico importante!")

def tutorial_teleconsulta(nome_usuario, modo_guia_ativo):
    """Tutorial de como acessar teleconsultas"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║        TUTORIAL: ACESSAR TELECONSULTAS       ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como participar de consultas online!")
    
    print("\n💻 COMO ACESSAR TELECONSULTAS:")
    print("1. Faça login no sistema")
    print("2. No menu do usuário, escolha a opção '6. Tutorial de como acessar as Teleconsulta'")
    print("3. Verifique se há teleconsultas agendadas")
    print("4. Acesse o link fornecido no horário marcado")
    
    if modo_guia_ativo:
        print("\n[Guia]: 🎥 PREPARAÇÃO PARA TELECONSULTA:")
        print("• Teste sua internet antes do horário")
        print("• Use fones de ouvido para melhor áudio")
        print("• Escolha um local calmo e bem iluminado")
        print("• Tenha seus documentos por perto")
        print("• Teste câmera e microfone")
    
    print("\n✅ A teleconsulta é uma forma prática e segura de cuidar da sua saúde!")

def tutorial_meus_dados(nome_usuario, modo_guia_ativo):
    """Tutorial de como acessar e editar dados pessoais"""
    print("\n╔══════════════════════════════════════════════╗")
    print("║       TUTORIAL: ACESSAR MEUS DADOS           ║")
    print("╚══════════════════════════════════════════════╝")
    
    if modo_guia_ativo:
        print("\n[Guia]: Vamos aprender como gerenciar suas informações pessoais!")
    
    print("\n👤 COMO ACESSAR SEUS DADOS:")
    print("1. Faça login no sistema")
    print("2. No menu do usuário, escolha a opção '7. Tutorial de como acessar os Meus Dados'")
    print("3. Visualize todas as suas informações cadastrais")
    print("4. Edite os dados que precisam ser atualizados")
    
    if modo_guia_ativo:
        print("\n[Guia]: 🔒 SEGURANÇA DOS DADOS:")
        print("• Mantenha sempre seus dados atualizados")
        print("• Use senhas seguras e únicas")
        print("• Nunca compartilhe informações pessoais")
        print("• O CPF não pode ser alterado por segurança")
        print("• Em caso de mudanças, atualize imediatamente")
    
    print("\n✅ Dados atualizados garantem melhor atendimento!")

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
            while True:
                print("\n╔══════════════════════════════════════════════╗")
                print("║            AJUDA E SUPORTE AO USUÁRIO        ║")
                
                if modo_guia_interativo_ativo:
                    print("║         ⭐ Modo Guia Interativo ATIVO ⭐     ║")

                print("╚══════════════════════════════════════════════╝\n")
                print("Olá! Esta é a sua Central de Ajuda e Suporte.")
                print("Selecione um tópico para saber mais:")

                print("\n--- Entendendo as Funcionalidades do Sistema ---")
                print("  1. Como usar 'Resultados', 'Receitas' e 'Agendas'.")
                print("  2. Tudo sobre 'Teleconsultas': como participar e dicas.")

                print("\n--- Suporte Inteligente e Guiado ---")
                print("  3. Falar com o Assistente Virtual (para Perguntas Frequentes).")
                print(f"  4. Modo Guia Interativo: [{'DESATIVAR' if modo_guia_interativo_ativo else 'ATIVAR'}] Ajuda visual passo a passo.")

                print("\n  0. Voltar ao menu do usuário.")
                print("=" * 50)

                prompt_ajuda = "Escolha uma opção de ajuda (digite o número): "
                if modo_guia_interativo_ativo:
                    prompt_ajuda = "[Guia] Digite o número da ajuda que precisa (1, 2, 3, 4 ou 0): "
                escolha_ajuda = input(prompt_ajuda)

                if escolha_ajuda == '1':
                    print("\n--- Usando 'Resultados', 'Receitas' e 'Agendas' ---")
                    print("- 'Meus Resultados de Exames': Aqui você acessa os resultados dos seus exames médicos.")
                    print("- 'Minhas Receitas Médicas': Consulte as receitas e prescrições feitas pelo seu médico.")
                    print("- 'Minhas Agendas': Veja todas as suas consultas e exames futuros marcados.")
                    
                    if modo_guia_interativo_ativo:
                        print("\n[Guia]: Essas seções ajudam você a manter seu histórico de saúde organizado e acessível!")
                
                elif escolha_ajuda == '2':
                    print("\n--- Tudo sobre 'Teleconsultas' ---")
                    print("Teleconsultas são atendimentos médicos feitos online, por vídeo.")
                    print("1. Verifique data e hora em 'Minhas Agendas'.")
                    #REMOVER
                    #  print("2. Um link de acesso será enviado (SMS, Telegram, ou aqui no sistema).")
                    print("3. No horário, clique no link para entrar.")
                    print("\nDicas para uma boa experiência:")
                    print("  - Tenha boa conexão de internet.")
                    print("  - Use fones de ouvido, se possível.")
                    print("  - Escolha um local calmo e com privacidade.")
                    print("  - Se precisar, peça ajuda para acessar o link.")
                    
                    if modo_guia_interativo_ativo:
                        print("\n[Guia]: As teleconsultas são uma forma prática de cuidar da sua saúde sem sair de casa!")
                
                elif escolha_ajuda == '3':
                    print("\n--- Assistente Virtual (Simulação) ---")
                    print("[Assistente Virtual]: Olá! Sou o assistente virtual do HC. Estou aqui para ajudar com perguntas comuns.")
                    print("  Por exemplo, você pode perguntar:")
                    print("    'Como vejo meus exames?'")
                    print("    'Esqueci minha senha, e agora?'")
                    print("    'Como funciona a teleconsulta?'")
                    user_query = input("Digite sua pergunta (ou 'sair' para voltar): ").lower()
                    if "exames" in user_query or "resultados" in user_query:
                        print("[Assistente Virtual]: Para ver seus exames, vá ao Menu do Usuário e escolha a opção '3. Tutorial de como acessar Resultados de Exames'.")
                    elif "senha" in user_query:
                        print("[Assistente Virtual]: Se esqueceu sua senha, na tela de login principal, deveria haver uma opção 'Esqueci minha senha'.")
                        print("  (Esta funcionalidade ainda será implementada). Por enquanto, contate o suporte do hospital se não conseguir logar.")
                    elif "teleconsulta" in user_query:
                        print("[Assistente Virtual]: Para teleconsultas, verifique 'Minhas Agendas' (opção 5) para datas e horários.")
                        print("  O link de acesso geralmente é enviado perto da data. Veja também a opção '6. Tutorial de como acessar as Teleconsulta'.")
                    elif user_query == 'sair':
                        print("[Assistente Virtual]: Entendido! Se precisar de mais algo, é só chamar.")
                    else:
                        print("[Assistente Virtual]: Desculpe, ainda estou aprendendo. Para essa dúvida, sugiro consultar as outras opções de ajuda ou contatar o suporte humano do hospital.")
                elif escolha_ajuda == '4':
                    modo_guia_interativo_ativo = not modo_guia_interativo_ativo
                    if modo_guia_interativo_ativo:
                        print("\n⭐ Modo Guia Interativo ATIVADO! ⭐")
                        print("   A partir de agora, você verá mais dicas e explicações ([Guia]: ...) ao usar o sistema.")
                        print("   Isso pode ajudar a entender melhor cada passo.")
                    else:
                        print("\nModo Guia Interativo DESATIVADO.")
                        print("   As dicas extras ([Guia]: ...) não serão mais exibidas.")
                    print("Você pode ativar ou desativar este modo quando quiser.")
                elif escolha_ajuda == '0':
                    break
                else:
                    print("Opção de ajuda inválida. Por favor, escolha um número válido do menu.")
                input("\nPressione Enter para continuar na Ajuda ou '0' para voltar ao menu do usuário...")

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
def mostrar_menu_ajuda_principal():
    while True:
        print("\n╔═════════════════════════════════════════╗")
        print("║      AJUDA E INFORMAÇÕES GERAIS         ║")
        print("╚═════════════════════════════════════════╝\n")
        print("Bem-vindo à Central de Ajuda do Portal do Paciente HC!")
        print("Aqui você encontra informações para usar nosso sistema.\n")
        print("1. Como faço para me CADASTRAR no sistema?")
        print("2. Como faço para fazer LOGIN (entrar) no sistema?")
        print("3. Sobre o SISTEMA: o que ele oferece e como funciona o TELEATENDIMENTO.")
        print("4. SUPORTE ADICIONAL: conheça o Assistente Virtual e os Guias Interativos.")
        print("0. VOLTAR ao Menu Principal.")
        print("=" * 45)
        opcao_ajuda = input("Escolha uma opção de ajuda (digite o número): ")

        if opcao_ajuda == '1':
            print("\n--- Como se Cadastrar ---")
            print("1. No Menu Principal, escolha a opção '1. Cadastro de Novo Usuário'.")
            print("2. Você precisará informar alguns dados pessoais:")
            print("   - Nome Completo.")
            print("   - CPF (apenas os 11 números, sem pontos ou traços).")
            print("   - Email válido (onde você recebe mensagens).")
            print("   - Número de Celular (com DDD, apenas números).")
            print("   - Criar uma Senha (guarde-a em local seguro!).")
            print("\nDica: Tenha seus documentos por perto para facilitar!")

        elif opcao_ajuda == '2':
            print("\n--- Como Fazer Login (Entrar no Sistema) ---")
            print("1. No Menu Principal, escolha a opção '2. Login (Entrar no Sistema)'.")
            print("2. Informe seu CPF (o mesmo que usou no cadastro).")
            print("3. Digite a Senha que você criou.")
            print("\nProblemas para entrar? Verifique se digitou o CPF e a senha corretamente.")
            print("  (Em breve: opção 'Esqueci minha senha' para ajudar a recuperar o acesso).")

        elif opcao_ajuda == '3':
            print("\n--- Sobre o Sistema e o Teleatendimento ---")
            print("Este sistema foi criado para facilitar seu acesso aos serviços de saúde do HC.")
            print("Com ele, depois de fazer login, você pode:")
            print("  - Ver seus resultados de exames.")
            print("  - Acessar suas receitas médicas.")
            print("  - Consultar seus agendamentos (consultas, exames).")
            print("  - Obter informações e participar de TELECONSULTAS (atendimento médico online).")
            print("\nO TELEATENDIMENTO permite que você converse com profissionais de saúde sem sair de casa,")
            print("  usando seu computador ou celular com internet. É prático e seguro!")
            print("\nNosso objetivo é que a tecnologia seja uma aliada no seu cuidado!")

        elif opcao_ajuda == '4':
            print("\n--- Suporte Adicional: Facilitando seu Uso ---")
            print("Sabemos que usar novas tecnologias pode gerar dúvidas. Por isso, oferecemos:")
            print("1. ASSISTENTE VIRTUAL (Chatbot):")
            print("   - Após o login, na seção 'Ajuda e Suporte', você pode conversar com nosso assistente.")
            print("   - Ele responde perguntas comuns como 'Onde vejo meus exames?' ou 'Como acesso a teleconsulta?'.")
            print("   - É como um tira-dúvidas rápido, disponível a qualquer hora!")
            print("\n2. GUIAS INTERATIVOS (Modo de Ajuda Visual):")
            print("   - Se precisar de mais ajuda para navegar nas telas, ative os 'Guias Interativos'.")
            print("   - Essa opção também fica em 'Ajuda e Suporte' após o login.")
            print("   - Com os guias ativos, o sistema mostra dicas ([Guia]: ...) e explicações extras")
            print("     para cada passo, ajudando você a entender melhor onde clicar e o que fazer.")
            print("   - Você pode ligar e desligar essa ajuda quando quiser!")
            # REMOVER
            # print("\n3. COMUNICAÇÃO PROATIVA VIA TELEGRAM:")
            # print("   - Se você autorizar no cadastro, podemos enviar lembretes de consultas e outras")
            # print("     informações importantes diretamente no seu Telegram.")
            print("\nQueremos que sua experiência seja a mais tranquila e fácil possível!")
        elif opcao_ajuda == '0':
            break
        else:
            print("\nOpção de ajuda inválida. Por favor, escolha um número válido do menu.")
        input("\nPressione Enter para continuar na Ajuda ou '0' para voltar ao Menu Principal...")


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
