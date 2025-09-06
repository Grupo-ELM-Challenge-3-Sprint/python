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


# Função para exibir o menu do usuário após login
# Permite acessar resultados, receitas, agendas, dados, ajuda, etc.
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

        print("2. Tutorial de como cadastrar no app HC")
        print("1. Tutorial de como logar no App HC")
        print("3. Tutorial de como acessar Resultados de Exames")
        print("4. Tutorial de como acessar Receitas Médicas")
        print("5. Tutorial de como acessar Minhas Agendas (Consultas/Exames Marcados)")
        print("6. Tutorial de como acessar as Teleconsulta")
        print("7. Tutorial de como acessar os Meus Dados")
        print("8. Ajuda e Suporte ao Usuário")
        print("9. Sair (Logout)")
        print("=" * 46)

        prompt_text = "Escolha uma opção: "
        if modo_guia_interativo_ativo:
            prompt_text = "[Guia] Digite o número da opção desejada e pressione Enter: "
        opcao_login = input(prompt_text)

        # Cada bloco abaixo trata uma opção do menu do usuário
        if opcao_login == '3':  # Meus Resultados
            print(f"\n--- Meus Resultados de Exames: {nome_usuario} ---")
            if modo_guia_interativo_ativo:
                print("[Guia]: Aqui você pode ver os resultados dos seus exames.")
            # Exibe resultados se houver
            if email_usuario in _dados_usuarios_servicos and _dados_usuarios_servicos[email_usuario]["resultados"]:
                for resultado in _dados_usuarios_servicos[email_usuario]["resultados"]:
                    print(f"- {resultado}")
            else:
                print("Você não possui resultados de exames cadastrados no momento.")
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '4':  # Minhas Receitas
            print(f"\n--- Minhas Receitas Médicas: {nome_usuario} ---")
            if modo_guia_interativo_ativo:
                print("[Guia]: Aqui você encontra suas receitas médicas.")
            # Exibe receitas se houver
            if email_usuario in _dados_usuarios_servicos and _dados_usuarios_servicos[email_usuario]["receitas"]:
                for receita in _dados_usuarios_servicos[email_usuario]["receitas"]:
                    print(f"- {receita}")
            else:
                print("Você não possui receitas médicas cadastradas no momento.")
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '5':  # Minhas Agendas
            print(f"\n--- Minhas Agendas (Consultas/Exames Marcados): {nome_usuario} ---")
            if modo_guia_interativo_ativo:
                print("[Guia]: Veja aqui seus próximos agendamentos.")
            # Exibe agendas se houver
            if email_usuario in _dados_usuarios_servicos and _dados_usuarios_servicos[email_usuario]["agendas"]:
                for agenda in _dados_usuarios_servicos[email_usuario]["agendas"]:
                    print(f"- {agenda}")
            else:
                print("Você não possui agendamentos cadastrados no momento.")

            # REMOVER
            # # Simulação de lembrete via Telegram
            # if usuario_logado.get('telegram_notifications', False):
            #     print(
            #         f"\n[Lembrete Simulado via Telegram]: Olá, {nome_usuario.split(' ')[0]}! Como você autorizou, enviaremos lembretes")
            #     print(f"  sobre seus agendamentos importantes para o número {usuario_logado.get('celular', 'N/A')}.")
            #     print(f"  Fique atento às mensagens para não perder seus compromissos!")
            # else:
            #     print(f"\n[Info]: Para receber lembretes de agendamentos via Telegram, você pode")
            #     print(f"  autorizar essa opção durante o cadastro. Se já é cadastrado,")
            #     print(f"  (Em breve: poderá ativar em 'Meus Dados Cadastrais').")
            # print("   Dica: Mantenha seu número de celular sempre atualizado em 'Meus Dados Cadastrais'.")
            # input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '6':  # Teleconsulta
            print(f"\n--- Informações sobre Teleconsulta para {nome_usuario} ---")
            print("A teleconsulta é um atendimento médico realizado à distância, usando a tecnologia.")

            if modo_guia_interativo_ativo:
                print("\n[Guia Interativo ATIVO]: Orientações para sua Teleconsulta:")
                print("  PASSO 1: Verifique a data e hora da sua teleconsulta na seção '5. Minhas Agendas'.")
                print("  PASSO 2: Geralmente, um link ou instruções de acesso são enviados perto da data.")
                print("           (Pode ser por SMS, Telegram, ou aparecer aqui no sistema). Fique de olho!")
                print("  PASSO 3: No horário marcado, acesse o link fornecido para entrar na sala virtual.")
                print("\n  DICAS IMPORTANTES para uma boa teleconsulta:")
                print("    - Internet: Certifique-se de ter uma boa conexão.")
                print("    - Áudio e Vídeo: Use fones de ouvido, se possível, e verifique sua câmera e microfone.")
                print("    - Ambiente: Escolha um local calmo e bem iluminado.")
                print("    - Ajuda: Se sentir dificuldade, não hesite em pedir ajuda a alguém de confiança")
                print("           ou contatar nosso suporte (veja Opção 8. Ajuda e Suporte).")

            tem_agenda_teleconsulta = False  # Simula verificação de teleconsultas
            if email_usuario in _dados_usuarios_servicos and _dados_usuarios_servicos[email_usuario]["agendas"]:
                for agenda_item in _dados_usuarios_servicos[email_usuario]["agendas"]:
                    if "teleconsulta" in agenda_item.lower() or "online" in agenda_item.lower():
                        tem_agenda_teleconsulta = True
                        print(f"\nLembrete: Você tem um agendamento que pode ser uma teleconsulta: {agenda_item}")
                        break

            if tem_agenda_teleconsulta:
                print("\nO link para sua teleconsulta (simulado) poderia ser: https://portal.teleconsulta.hc/salaXYZ")
                print("Verifique suas mensagens (SMS/Telegram) ou esta seção perto da data agendada.")
            else:
                print("\nNo momento, não identificamos teleconsultas em sua agenda.")
                print("Quando uma teleconsulta for agendada, as instruções e o link de acesso aparecerão aqui.")

            print("\nPara mais detalhes ou se tiver dúvidas, acesse '8. Ajuda e Suporte ao Usuário'.")
            input("\nPressione Enter para voltar ao menu do usuário...")

        elif opcao_login == '7':  # Meus Dados
            # Exibe e permite alterar dados cadastrais do usuário
            print("\n--- Meus Dados Cadastrais ---")
            if modo_guia_interativo_ativo:
                print("[Guia]: Aqui você pode ver e atualizar suas informações pessoais.")

            print(f"Nome: {usuario_logado['nome']}")
            print(f"CPF: {usuario_logado['cpf']}")
            print(f"Email: {usuario_logado['email']}")
            print(f"Celular: {usuario_logado['celular']}")
            print(f"Senha: {usuario_logado['senha']}")
            # REMOVER
            # if 'telegram_notifications' in usuario_logado:
            #     status_telegram = "ATIVADAS" if usuario_logado['telegram_notifications'] else "DESATIVADAS"
            #     print(f"Notificações por Telegram: {status_telegram}")

            while True:
                print("\n╔══════════════════════════════════════════════╗")
                print(f"║           MEUS DADOS: {nome_usuario[:20]:<20}   ║")
                if modo_guia_interativo_ativo:
                    print("║         ⭐ Modo Guia Interativo ATIVO ⭐      ║")
                print("╚══════════════════════════════════════════════╝")
                print(f"1. Nome: {usuario_logado['nome']}")
                print(f"2. CPF: {usuario_logado['cpf']} (Não pode ser alterado)")
                print(f"3. Email: {usuario_logado['email']}")
                print(f"4. Celular: {usuario_logado['celular']}")
                print(f"5. Senha: {usuario_logado['senha']}")

                # REMOVER
                # if 'telegram_notifications' in usuario_logado:
                #     status_telegram = "ATIVADAS" if usuario_logado['telegram_notifications'] else "DESATIVADAS"
                #     print(f"6. Notificações por Telegram: {status_telegram} (Alterar aqui - Em breve)")

                print("0. Voltar ao menu do usuário")
                print("=" * 46)

                escolha_dado_prompt = "Digite o número do dado que deseja alterar ou 0 para voltar: "
                if modo_guia_interativo_ativo:
                    escolha_dado_prompt = "[Guia] Escolha o que alterar (Ex: 1 para Nome) ou 0 para voltar: "
                escolha_dado = input(escolha_dado_prompt)

                if escolha_dado == '1':
                    novo_nome = input("Digite o novo nome completo: ")
                    usuario_logado['nome'] = novo_nome
                    for user in lista_de_usuarios:
                        if user['cpf'] == usuario_logado['cpf']:
                            user['nome'] = novo_nome
                            break
                    nome_usuario = novo_nome
                    print("Nome alterado com sucesso!")
                elif escolha_dado == '3':
                    novo_email = input("Digite o novo email: ")
                    if validacoes.validar_email(novo_email):
                        email_existente = False
                        for user in lista_de_usuarios:
                            if user['email'] == novo_email and user['cpf'] != usuario_logado['cpf']:
                                email_existente = True
                                break
                        if email_existente:
                            print("Este email já está cadastrado por outro usuário.")
                        else:
                            if usuario_logado['email'] in _dados_usuarios_servicos:
                                dados_servicos_antigos = _dados_usuarios_servicos.pop(usuario_logado['email'])
                                _dados_usuarios_servicos[novo_email] = dados_servicos_antigos
                            usuario_logado['email'] = novo_email
                            for user in lista_de_usuarios:
                                if user['cpf'] == usuario_logado['cpf']:
                                    user['email'] = novo_email
                                    break
                            email_usuario = novo_email
                            print("Email alterado com sucesso!")
                    else:
                        print("Email inválido.")
                elif escolha_dado == '4':
                    novo_celular = input("Digite o novo número de celular (com DDD): ")
                    if validacoes.validar_celular(novo_celular):
                        usuario_logado['celular'] = novo_celular
                        for user in lista_de_usuarios:
                            if user['cpf'] == usuario_logado['cpf']:
                                user['celular'] = novo_celular
                                break
                        print("Celular alterado com sucesso!")
                    else:
                        print("Número de celular inválido.")
                elif escolha_dado == '5':
                    while True:
                        nova_senha = input("Digite a nova senha: ")
                        confirmar_nova_senha = input("Confirme a nova senha: ")
                        if nova_senha == confirmar_nova_senha:
                            usuario_logado['senha'] = nova_senha
                            for user in lista_de_usuarios:
                                if user['cpf'] == usuario_logado['cpf']:
                                    user['senha'] = nova_senha
                                    break
                            print("Senha alterada com sucesso!")
                            break
                        else:
                            print("As senhas não coincidem. Tente novamente.")
                #REMOVER
                #  elif escolha_dado == '6':
                #     print("A opção de alterar preferências de Telegram por aqui será implementada em breve.")
                #     print(
                #         f"Atualmente, suas notificações por Telegram estão: {'ATIVADAS' if usuario_logado.get('telegram_notifications') else 'DESATIVADAS (ou não definidas)'}")

                elif escolha_dado == '0':
                    break
                else:
                    print("Opção inválida.")
                input("\nPressione Enter para continuar...")


        elif opcao_login == '8':  # Ajuda e Suporte (Usuário logado)
            while True:
                print("\n╔══════════════════════════════════════════════╗")
                print("║            AJUDA E SUPORTE AO USUÁRIO        ║")
                
                if modo_guia_interativo_ativo:
                    print("║         ⭐ Modo Guia Interativo ATIVO ⭐     ║")

                print("╚══════════════════════════════════════════════╝\n")
                print("Olá! Esta é a sua Central de Ajuda e Suporte.")
                print("Selecione um tópico para saber mais:")

                print("\n--- Entendendo as Funcionalidades do Sistema ---")
                print("  a. Como usar 'Resultados', 'Receitas' e 'Agendas'.")
                print("  b. Tudo sobre 'Teleconsultas': como participar e dicas.")

                print("\n--- Suporte Inteligente e Guiado ---")
                print("  c. Falar com o Assistente Virtual (para Perguntas Frequentes).")
                print(f"  d. Modo Guia Interativo: [{'DESATIVAR' if modo_guia_interativo_ativo else 'ATIVAR'}] Ajuda visual passo a passo.")

                print("\n  v. Voltar ao menu do usuário.")
                print("=" * 50)

                prompt_ajuda = "Escolha uma opção de ajuda (digite a letra): "
                if modo_guia_interativo_ativo:
                    prompt_ajuda = "[Guia] Digite a letra da ajuda que precisa (a, b, c, d ou v): "
                escolha_ajuda = input(prompt_ajuda).lower()

                if escolha_ajuda == 'a':
                    print("\n--- Usando 'Resultados', 'Receitas' e 'Agendas' ---")
                    print("- 'Meus Resultados de Exames': Aqui você acessa os resultados dos seus exames médicos.")
                    print("- 'Minhas Receitas Médicas': Consulte as receitas e prescrições feitas pelo seu médico.")
                    print("- 'Minhas Agendas': Veja todas as suas consultas e exames futuros marcados.")
                    
                    if modo_guia_interativo_ativo:
                        print("\n[Guia]: Essas seções ajudam você a manter seu histórico de saúde organizado e acessível!")
                
                elif escolha_ajuda == 'b':
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
                
                elif escolha_ajuda == 'c':
                    print("\n--- Assistente Virtual (Simulação) ---")
                    print("[Assistente Virtual]: Olá! Sou o assistente virtual do HC. Estou aqui para ajudar com perguntas comuns.")
                    print("  Por exemplo, você pode perguntar:")
                    print("    'Como vejo meus exames?'")
                    print("    'Esqueci minha senha, e agora?'")
                    print("    'Como funciona a teleconsulta?'")
                    user_query = input("Digite sua pergunta (ou 'sair' para voltar): ").lower()
                    if "exames" in user_query or "resultados" in user_query:
                        print("[Assistente Virtual]: Para ver seus exames, vá ao Menu do Usuário e escolha a opção '3. Meus Resultados de Exames'.")
                    elif "senha" in user_query:
                        print("[Assistente Virtual]: Se esqueceu sua senha, na tela de login principal, deveria haver uma opção 'Esqueci minha senha'.")
                        print("  (Esta funcionalidade ainda será implementada). Por enquanto, contate o suporte do hospital se não conseguir logar.")
                    elif "teleconsulta" in user_query:
                        print("[Assistente Virtual]: Para teleconsultas, verifique 'Minhas Agendas' (opção 5) para datas e horários.")
                        print("  O link de acesso geralmente é enviado perto da data. Veja também a opção '6. Informações sobre Teleconsulta'.")
                    elif user_query == 'sair':
                        print("[Assistente Virtual]: Entendido! Se precisar de mais algo, é só chamar.")
                    else:
                        print("[Assistente Virtual]: Desculpe, ainda estou aprendendo. Para essa dúvida, sugiro consultar as outras opções de ajuda ou contatar o suporte humano do hospital.")
                elif escolha_ajuda == 'd':
                    modo_guia_interativo_ativo = not modo_guia_interativo_ativo
                    if modo_guia_interativo_ativo:
                        print("\n⭐ Modo Guia Interativo ATIVADO! ⭐")
                        print("   A partir de agora, você verá mais dicas e explicações ([Guia]: ...) ao usar o sistema.")
                        print("   Isso pode ajudar a entender melhor cada passo.")
                    else:
                        print("\nModo Guia Interativo DESATIVADO.")
                        print("   As dicas extras ([Guia]: ...) não serão mais exibidas.")
                    print("Você pode ativar ou desativar este modo quando quiser.")
                elif escolha_ajuda == 'v':
                    break
                else:
                    print("Opção de ajuda inválida. Por favor, escolha uma das letras do menu.")
                input("\nPressione Enter para continuar na Ajuda ou 'v' para voltar ao menu do usuário...")

        elif opcao_login == '9':
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
        print("A. Como faço para me CADASTRAR no sistema?")
        print("B. Como faço para fazer LOGIN (entrar) no sistema?")
        print("C. Sobre o SISTEMA: o que ele oferece e como funciona o TELEATENDIMENTO.")
        print("D. SUPORTE ADICIONAL: conheça o Assistente Virtual e os Guias Interativos.")
        print("V. VOLTAR ao Menu Principal.")
        print("=" * 45)
        opcao_ajuda = input("Escolha uma opção de ajuda (digite a letra): ").upper()

        if opcao_ajuda == 'A':
            print("\n--- Como se Cadastrar ---")
            print("1. No Menu Principal, escolha a opção '1. Cadastro de Novo Usuário'.")
            print("2. Você precisará informar alguns dados pessoais:")
            print("   - Nome Completo.")
            print("   - CPF (apenas os 11 números, sem pontos ou traços).")
            print("   - Email válido (onde você recebe mensagens).")
            print("   - Número de Celular (com DDD, apenas números).")
            print("   - Criar uma Senha (guarde-a em local seguro!).")
            # REMOVER
            # print("3. Você também poderá escolher se deseja receber notificações via Telegram.")
            print("\nDica: Tenha seus documentos por perto para facilitar!")
        elif opcao_ajuda == 'B':
            print("\n--- Como Fazer Login (Entrar no Sistema) ---")
            print("1. No Menu Principal, escolha a opção '2. Login (Entrar no Sistema)'.")
            print("2. Informe seu CPF (o mesmo que usou no cadastro).")
            print("3. Digite a Senha que você criou.")
            print("\nProblemas para entrar? Verifique se digitou o CPF e a senha corretamente.")
            print("  (Em breve: opção 'Esqueci minha senha' para ajudar a recuperar o acesso).")
        elif opcao_ajuda == 'C':
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
        elif opcao_ajuda == 'D':
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
        elif opcao_ajuda == 'V':
            break
        else:
            print("\nOpção de ajuda inválida. Por favor, escolha uma das letras do menu.")
        input("\nPressione Enter para continuar na Ajuda ou 'v' para voltar ao Menu Principal...")


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
