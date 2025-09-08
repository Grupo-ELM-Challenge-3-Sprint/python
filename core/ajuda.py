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
        print("2. No horário, clique no link para entrar.")
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