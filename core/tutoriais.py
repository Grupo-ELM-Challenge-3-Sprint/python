
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





# =======================================================================================================


def tutorial_agendas(nome_usuario, modo_guia_ativo):
    # Tutorial de como acessar agendas de consultas e exames
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
    # Tutorial de como acessar teleconsultas
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
    # Tutorial de como acessar e editar dados pessoais
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
            print("\nQueremos que sua experiência seja a mais tranquila e fácil possível!")
        elif opcao_ajuda == '0':
            break
        else:
            print("\nOpção de ajuda inválida. Por favor, escolha um número válido do menu.")
        input("\nPressione Enter para continuar na Ajuda ou '0' para voltar ao Menu Principal...")

