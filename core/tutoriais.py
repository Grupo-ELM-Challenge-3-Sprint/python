# =============================================================================
# FUNÇÕES DE TUTORIAIS
# =============================================================================

def tutorial_cadastro(modo_guia_ativo):
    # Tutorial de como se cadastrar no Portal do Paciente HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║  TUTORIAL: CADASTRO NO PORTAL DO PACIENTE HC ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n📝 PASSO A PASSO PARA CADASTRO:")
    print("1. No app Portal do Paciente HC, clique em 'Acessar Portal'")
    print("2. Em seguida, clique em 'Cadastrar senha'")
    print("3. Preencha seus dados pessoais:")
    print("   • Nome completo (ex: João Silva Santos)")
    print("   • CPF com 11 números (ex: 12345678901)")
    print("   • Email válido (ex: joao@email.com)")
    print("   • Celular com DDD (ex: 11987654321)")
    print("   • Crie uma senha segura")
    print("4. Ao terminar de preencher, clique em 'Cadastrar Senha'")
    print("5. Em seguida, irá aparecer uma tela de Senha Cadastrada com sucesso")
    print("6. E ao final, clique em 'Acessar Agora'")
    
    if modo_guia_ativo:
        print("\n[Guia]: 💡 DICAS IMPORTANTES:")
        print("• Tenha seus documentos por perto")
        print("• Use um email que você acessa frequentemente")
        print("• Escolha uma senha que você consiga lembrar")
        print("• Anote seus dados em local seguro")
    
    print("\n✅ Após o cadastro, você poderá acessar serviços do HC: resultados, receitas, agendamentos e teleconsultas.")

def tutorial_login(modo_guia_ativo):
    # Tutorial de como fazer login no Portal do Paciente HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║    TUTORIAL: LOGIN NO PORTAL DO PACIENTE HC  ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n🔐 PASSO A PASSO PARA LOGIN:")
    print("1. No app Portal do Paciente HC, clique em 'Acessar Portal'")
    print("2. Em seguida, digite seu CPF (apenas os 11 números)")
    print("3. E digite sua senha")
    print("4. Pressione 'Acessar' para entrar no Portal do Paciente HC")
    
    if modo_guia_ativo:
        print("\n[Guia]: 💡 DICAS DE SEGURANÇA:")
        print("• Nunca compartilhe sua senha com ninguém")
        print("• Certifique-se de que ninguém está vendo sua tela")
        print("• Se esquecer a senha, contate o suporte")
        print("• Sempre faça logout quando terminar")
    
    print("\n✅ Se os dados estiverem corretos, você entra no Portal e pode usar os serviços do HC.")

def tutorial_esqueci_senha(modo_guia_ativo):
    # Tutorial de como recuperar senha no Portal do Paciente HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║      TUTORIAL: ESQUECI MINHA SENHA (HC)      ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n🔑 COMO RECUPERAR SUA SENHA:")
    print("1. Na tela de login do Portal do Paciente HC")
    print("2. Clique em 'Esqueci minha senha'")
    print("3. Digite seu CPF")
    print("4. Digite sua data de nascimento")
    print("5. Em seguida, clique em Localizar Paciente")

    if modo_guia_ativo:
        print("\n[Guia]: 💡 DICAS IMPORTANTES:")
        print("• Use o mesmo email que cadastrou no Portal")
        print("• Verifique a caixa de spam se não receber o email")
        print("• O email pode demorar alguns minutos para chegar")
        print("• Se não receber, contate o suporte do HC")
        print("• Crie uma senha forte e anote em local seguro")

    print("\n✅ Após recuperar, você poderá fazer login normalmente no Portal!")

def tutorial_resultados(modo_guia_ativo):
    # Tutorial de como acessar resultados de exames no HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║     TUTORIAL: ACESSAR RESULTADOS DE EXAMES   ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n🔬 COMO ACESSAR SEUS RESULTADOS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Meus Resultados'")
    print("3. Selecione e Visualize os Resultados de Exames de Laboratório ou Imagem")
    print("4. Visualize os Resultados de Exames com data, descrição e status do laudo")
    
    if modo_guia_ativo:
        print("\n[Guia]: 📋 INFORMAÇÕES IMPORTANTES:")
        print("• Os resultados ficam disponíveis 24h por dia")
        print("• Você pode acessar de qualquer lugar")
        print("• Os dados são atualizados quando liberados pelos setores do HC")
        print("• Em caso de dúvidas sobre o laudo, consulte seu médico assistente")
    
    print("\n✅ Seus resultados estão sempre seguros e acessíveis!")

def tutorial_receitas(modo_guia_ativo):
    # Tutorial de como acessar receitas médicas no HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║      TUTORIAL: ACESSAR RECEITAS MÉDICAS      ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n💊 COMO ACESSAR SUAS RECEITAS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Minhas Receitas'")
    print("3. Veja a lista de prescrições com medicamentos, dosagens e validade")
    print("4. Visualize prescrições ativas/Inativas e, quando aplicável, instruções de uso")
    
    if modo_guia_ativo:
        print("\n[Guia]: ⚠️ CUIDADOS IMPORTANTES:")
        print("• Siga exatamente as instruções do médico")
        print("• Respeite os horários e quantidades")
        print("• Em caso de dúvidas, consulte seu farmacêutico")
        print("• Guarde as receitas em local seguro")
    
    print("\n✅ Suas receitas ficam sempre disponíveis para consulta!")

def tutorial_agendas(modo_guia_ativo):
    # Tutorial de como acessar agendas de consultas e exames no HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║          TUTORIAL: ACESSAR AGENDAS           ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n📅 COMO ACESSAR SUAS AGENDAS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Minhas Agendas'")
    print("3. Consulte data, hora, local e especialidade dos atendimentos")
    print("4. Verifique orientações específicas do exame/consulta, quando houver")
    
    if modo_guia_ativo:
        print("\n[Guia]: ⏰ LEMBRETES ÚTEIS:")
        print("• Chegue com 15 minutos de antecedência")
        print("• Leve documentos e exames anteriores")
        print("• Em caso de desistência, cancele com antecedência")
        print("• Mantenha seus dados sempre atualizados")
    
    print("\n✅ Nunca perca um compromisso médico importante!")

def tutorial_teleconsulta(modo_guia_ativo):
    # Tutorial de como acessar teleconsultas do HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║        TUTORIAL: ACESSAR TELECONSULTAS       ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n💻 COMO ACESSAR TELECONSULTAS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Teleconsultas'")
    print("3. Verifique se há teleconsultas agendadas na sua agenda")
    print("4. No horário marcado, acesse o link informado para a consulta online")
    
    if modo_guia_ativo:
        print("\n[Guia]: 🎥 PREPARAÇÃO PARA TELECONSULTA:")
        print("• Teste sua internet antes do horário")
        print("• Use fones de ouvido para melhor áudio")
        print("• Escolha um local calmo e bem iluminado")
        print("• Tenha seus documentos por perto")
        print("• Teste câmera e microfone")
    
    print("\n✅ A teleconsulta é uma forma prática e segura de cuidar da sua saúde!")

def tutorial_solicitacao_exames(modo_guia_ativo):
    # Tutorial de como solicitar/exibir solicitações de exames no HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║     TUTORIAL: SOLICITAÇÃO DE EXAMES (HC)     ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n🧪 SOLICITAÇÃO DE EXAMES PELO PORTAL:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Solicitação de Exames'")
    print("3. Verifique orientações: alguns exames exigem guia médica e agendamento")
    print("4. Acompanhe solicitações e, após a coleta/realização, consulte 'Resultados'")

    if modo_guia_ativo:
        print("\n[Guia]: Dúvidas sobre preparo de exames? Consulte as orientações exibidas na tela do Portal.")
        print("[Guia]: Nem todos os exames podem ser solicitados diretamente pelo paciente; siga a prescrição médica.")

    print("\n✅ Utilize o Portal para acompanhar o status e conferir resultados quando liberados.")


def tutorial_solicitacao_documentos(modo_guia_ativo):
    # Tutorial de como solicitar documentos/prontuário no HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║        TUTORIAL: MEUS DOCUMENTOS (HC)        ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n📄 COMO SOLICITAR DOCUMENTOS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Documentos'")
    print("3. Em seguida clique em 'Meus Documentos'")

    if modo_guia_ativo:
        print("\n[Guia]: Documentos do prontuário podem exigir identificação e prazos legais para entrega.")
        print("[Guia]: Verifique no Portal os canais de contato/retirada informados pela unidade do HC.")

    print("\n✅ Agora pode visualizar os seus Documentos.")

def tutorial_meus_dados(modo_guia_ativo):
    # Tutorial de como acessar e editar dados pessoais no Portal do HC
    print("\n╔══════════════════════════════════════════════╗")
    print("║       TUTORIAL: ACESSAR MEUS DADOS           ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n👤 COMO ACESSAR SEUS DADOS:")
    print("1. Faça login no Portal do Paciente HC, em seguida clique em 'Menu'")
    print("2. No menu do Portal, clique na opção 'Meus Dados'")
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



# Isso aparece no tutoriais do usuário SEM LOGAR, no início do programa
def mostrar_menu_ajuda_principal():
    while True:
        print("\n╔═════════════════════════════════════════╗")
        print("║      AJUDA E INFORMAÇÕES GERAIS         ║")
        print("╚═════════════════════════════════════════╝\n")
        print("Bem-vindo à Central de Ajuda do SimplesHC!")
        print("Aqui você encontra informações para usar nosso sistema.\n")
        print("1. Como faço para me CADASTRAR no sistema?")
        print("2. Como faço para fazer LOGIN (entrar) no sistema?")
        print("3. Sobre o SISTEMA: o que ele oferece.")
        print("4. SUPORTE ADICIONAL: conheça o Assistente Virtual e os Guias Interativos.")
        print("0. VOLTAR ao Menu Principal.")
        print("=" * 45)
        opcao_ajuda = input("Escolha uma opção de ajuda (digite o número): ")

        if opcao_ajuda == '1':
            print("\n╔═════════════════════════════════════════╗")
            print("║      Como se cadastrar no SimplesHC?    ║")
            print("╚═════════════════════════════════════════╝\n")
            print("1. No Menu Principal, escolha a opção '1. Cadastro de Novo Usuário'.")
            print("2. Você precisará informar alguns dados pessoais:")
            print("   - Nome Completo.")
            print("   - CPF (apenas os 11 números, sem pontos ou traços).")
            print("   - Email válido (onde você recebe mensagens).")
            print("   - Número de Celular (com DDD, apenas números).")
            print("   - Criar uma Senha (guarde-a em local seguro!).")
            print("\nDica: Tenha seus documentos por perto para facilitar!")

        elif opcao_ajuda == '2':
            print("\n╔═════════════════════════════════════════╗")
            print("║      Como fazer login no SimplesHC?     ║")
            print("╚═════════════════════════════════════════╝\n")
            print("1. No Menu Principal, escolha a opção '2. Login (Entrar no Sistema)'.")
            print("2. Informe seu CPF (o mesmo que usou no cadastro).")
            print("3. Digite a Senha que você criou.")
            print("\nProblemas para entrar? Verifique se digitou o CPF e a senha corretamente.")

        elif opcao_ajuda == '3':
            print("\n╔═════════════════════════════════════════╗")
            print("║            Sobre o SimplesHC!           ║")
            print("╚═════════════════════════════════════════╝\n")
            print("Este sistema foi criado para facilitar seu acesso aos serviços de saúde do Hospital HC.")
            print("\nNosso objetivo é que a tecnologia seja uma aliada no seu cuidado!")

        elif opcao_ajuda == '4':
            print("\n╔═════════════════════════════════════════╗")
            print("║   Alguns recursos extras do SimplesHC!  ║")
            print("╚═════════════════════════════════════════╝\n")
            print("Sabemos que usar novas tecnologias pode gerar dúvidas. Por isso, oferecemos:")
            
            print("\n1. ASSISTENTE VIRTUAL (Chatbot):")
            print("   - Após o login, na seção 'Ajuda e Suporte', você pode conversar com nosso assistente.")
            print("   - Ele responde perguntas comuns como 'Onde vejo meus exames?' ou 'Como acesso a teleconsulta?'.")
            print("   - É como um tira-dúvidas rápido, disponível a qualquer hora!")

            print("\n2. GUIAS INTERATIVOS (Modo de Ajuda Visual):")
            print("   - Se precisar de mais ajuda para navegar nas telas, ative os 'Guias Interativos'.")
            print("   - Essa opção também fica em 'Ajuda e Suporte' após o login.")
            print("   - Com os guias ativos, o sistema mostra dicas ([Guia]: ...) e explicações extras")
            print("     para cada passo, ajudando você a entender melhor onde clicar e o que fazer.")
            print("   - Você pode ligar e desligar essa ajuda quando quiser!")
            print("\nQueremos que sua experiência seja a mais tranquila e fácil possível!")
        elif opcao_ajuda == '0':
            break
        else:
            print("\nOpção de ajuda inválida. Por favor, escolha um número válido do menu.")
        input("\nPressione Enter para continuar na Ajuda ou '0' para voltar ao Menu Principal...")
