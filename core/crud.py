import core.validacoes as validacoes
from database.dados import _dados_de_usuarios

# Lista para armazenar os dados dos usuários
lista_de_usuarios = _dados_de_usuarios

# =============================================================================
# FUNÇÕES CRUD ADMINISTRATIVAS
# =============================================================================


# Verifica se o usuário logado é administrador 
def verificar_se_eh_admin(usuario_logado):
    try:
        return usuario_logado.get("admin", False)
    except Exception as e:
        print(f"Erro ao verificar permissão de administrador: {e}")
        return False

#Menu Listar Usuários CRUD
def listar_usuarios():
    # Lista todos os usuários cadastrados no sistema
    try:
        if not lista_de_usuarios:
            print("\n❌ Nenhum usuário cadastrado no sistema.")
            return
        
        print("\n" + "=" * 80)
        print("📋 LISTA DE USUÁRIOS CADASTRADOS")
        print("=" * 80)
        
        for i, usuario in enumerate(lista_de_usuarios, 1):
            status_admin = "👑 ADMIN" if usuario.get("admin", False) else "👤 USUÁRIO"
            print(f"\n{i}. {usuario['nome']} ({status_admin})")
            print(f"   CPF: {usuario['cpf']}")
            print(f"   Email: {usuario['email']}")
            print(f"   Celular: {usuario['celular']}")
            print("-" * 50)
        
        print(f"\nTotal de usuários: {len(lista_de_usuarios)}")
        
    except Exception as e:
        print(f"❌ Erro ao listar usuários: {e}")
    finally:
        input("\nPressione Enter para continuar...")


#Menu Criar Novo Usuário CRUD
def criar_usuario_admin():
    # Cria um novo usuário através do painel administrativo
    print("\n" + "=" * 50)
    print("👤 CRIAR NOVO USUÁRIO")
    print("=" * 50)
    
    try:
        print("Digite 0 para cancelar a criação\n")
        
        # Nome completo com validação
        while True:
            nome = input("Nome Completo: ")
            if nome == '0':
                print("Criação de usuário cancelada.")
                return
            if validacoes.validar_nome(nome):
                break
            print("Nome inválido. Digite ao menos 2 letras.")
        
        # CPF com validação e verificação de duplicata
        while True:
            cpf = input("CPF (apenas 11 números): ")
            if cpf == '0':
                print("Criação de usuário cancelada.")
                return
            if not validacoes.validar_cpf(cpf):
                print("CPF inválido. Deve conter 11 números.")
                continue
            if any(usuario["cpf"] == cpf for usuario in lista_de_usuarios):
                print("Usuário com este CPF já cadastrado. Informe outro CPF.")
                continue
            break
        
        # Email com validação
        while True:
            email = input("Email: ")
            if email == '0':
                print("Criação de usuário cancelada.")
                return
            if validacoes.validar_email(email):
                break
            print("Email inválido. Formato esperado: nome@dominio.com")
        
        # Celular com validação
        while True:
            celular = input("Número de Celular (com DDD, apenas números): ")
            if celular == '0':
                print("Criação de usuário cancelada.")
                return
            if validacoes.validar_celular(celular):
                break
            print("Número de celular inválido. Deve conter 10 ou 11 números.")
        
        # Senha com validação
        while True:
            senha = input("Crie uma senha (mín. 6 caracteres): ")
            if senha == '0':
                print("Criação de usuário cancelada.")
                return
            if not validacoes.validar_senha(senha):
                print("Senha fraca. Use ao menos 6 caracteres.")
                continue
            confirmar_senha = input("Confirme a senha: ")
            if senha == confirmar_senha:
                break
            print("As senhas não coincidem. Tente novamente.")
        
        # Pergunta se é administrador
        while True:
            eh_admin = input("Este usuário será administrador? (s/n): ").lower()
            if eh_admin in ['s', 'sim', 'n', 'não', 'nao']:
                break
            print("Digite 's' para sim ou 'n' para não.")
        
        admin = eh_admin in ['s', 'sim']
        
        # Cria o novo usuário
        novo_usuario = {
            "cpf": cpf, 
            "nome": nome, 
            "email": email, 
            "celular": celular, 
            "senha": senha,
            "admin": admin
        }
        
        lista_de_usuarios.append(novo_usuario)
        
        status = "👑 ADMINISTRADOR" if admin else "👤 USUÁRIO"
        print(f"\n✅ Usuário {nome} criado com sucesso! ({status})")
        
    except Exception as e:
        print(f"❌ Erro ao criar usuário: {e}")
    finally:
        input("\nPressione Enter para continuar...")


#Menu Atualizar dados dos usuários CRUD
def atualizar_usuario():
    # Atualiza dados de um usuário existente
    print("\n" + "=" * 50)
    print("✏️ ATUALIZAR USUÁRIO")
    print("=" * 50)
    
    try:
        if not lista_de_usuarios:
            print("❌ Nenhum usuário cadastrado no sistema.")
            return
        
        # Lista usuários para seleção
        print("Usuários disponíveis:")
        for i, usuario in enumerate(lista_de_usuarios, 1):
            status = "👑 ADMIN" if usuario.get("admin", False) else "👤 USUÁRIO"
            print(f"{i}. {usuario['nome']} ({status}) - CPF: {usuario['cpf']}")
        
        while True:
            try:
                escolha = input("\nDigite o número do usuário para atualizar (0 para cancelar): ")
                if escolha == '0':
                    print("Atualização cancelada.")
                    return
                
                indice = int(escolha) - 1
                if 0 <= indice < len(lista_de_usuarios):
                    break
                print("Número inválido. Escolha um número da lista.")
            except ValueError:
                print("Digite um número válido.")
        
        usuario = lista_de_usuarios[indice]
        print(f"\nAtualizando dados de: {usuario['nome']}")
        
        # Atualiza nome
        while True:
            novo_nome = input(f"Nome atual: {usuario['nome']}\nNovo nome (Enter para manter): ")
            if novo_nome == '':
                break
            if validacoes.validar_nome(novo_nome):
                usuario['nome'] = novo_nome
                break
            print("Nome inválido. Digite ao menos 2 letras.")
        
        # Atualiza email
        while True:
            novo_email = input(f"Email atual: {usuario['email']}\nNovo email (Enter para manter): ")
            if novo_email == '':
                break
            if validacoes.validar_email(novo_email):
                # Verifica se o email já existe em outro usuário
                if any(u["email"] == novo_email and u != usuario for u in lista_de_usuarios):
                    print("Email já está em uso por outro usuário.")
                    continue
                usuario['email'] = novo_email
                break
            print("Email inválido. Formato esperado: nome@dominio.com")
        
        # Atualiza celular
        while True:
            novo_celular = input(f"Celular atual: {usuario['celular']}\nNovo celular (Enter para manter): ")
            if novo_celular == '':
                break
            if validacoes.validar_celular(novo_celular):
                usuario['celular'] = novo_celular
                break
            print("Número de celular inválido. Deve conter 10 ou 11 números.")
        
        # Atualiza status de administrador
        while True:
            status_atual = "Administrador" if usuario.get("admin", False) else "Usuário comum"
            mudar_admin = input(f"Status atual: {status_atual}\nAlterar status de administrador? (s/n): ").lower()
            if mudar_admin in ['s', 'sim']:
                novo_admin = input("Tornar administrador? (s/n): ").lower()
                if novo_admin in ['s', 'sim', 'n', 'não', 'nao']:
                    usuario['admin'] = novo_admin in ['s', 'sim']
                    break
            elif mudar_admin in ['n', 'não', 'nao']:
                break
            print("Digite 's' para sim ou 'n' para não.")
        
        print(f"\n✅ Usuário {usuario['nome']} atualizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar usuário: {e}")
    finally:
        input("\nPressione Enter para continuar...")


#Menu Deletar CRUD
def deletar_usuario():
    # Remove um usuário do sistema
    print("\n" + "=" * 50)
    print("🗑️ DELETAR USUÁRIO")
    print("=" * 50)
    
    try:
        if not lista_de_usuarios:
            print("❌ Nenhum usuário cadastrado no sistema.")
            return
        
        # Lista usuários para seleção
        print("Usuários disponíveis:")
        for i, usuario in enumerate(lista_de_usuarios, 1):
            status = "👑 ADMIN" if usuario.get("admin", False) else "👤 USUÁRIO"
            print(f"{i}. {usuario['nome']} ({status}) - CPF: {usuario['cpf']}")
        
        while True:
            try:
                escolha = input("\nDigite o número do usuário para deletar (0 para cancelar): ")
                if escolha == '0':
                    print("Exclusão cancelada.")
                    return
                
                indice = int(escolha) - 1
                if 0 <= indice < len(lista_de_usuarios):
                    break
                print("Número inválido. Escolha um número da lista.")
            except ValueError:
                print("Digite um número válido.")
        
        usuario = lista_de_usuarios[indice]
        
        # Confirmação de exclusão
        print(f"\n⚠️ ATENÇÃO: Você está prestes a deletar o usuário:")
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Email: {usuario['email']}")
        
        while True:
            confirmar = input("\nTem certeza que deseja deletar este usuário? (s/n): ").lower()
            if confirmar in ['s', 'sim']:
                # Remove o usuário da lista
                usuario_removido = lista_de_usuarios.pop(indice)
                
                print(f"\n✅ Usuário {usuario_removido['nome']} deletado com sucesso!")
                break
            elif confirmar in ['n', 'não', 'nao']:
                print("Exclusão cancelada.")
                break
            else:
                print("Digite 's' para sim ou 'n' para não.")
        
    except Exception as e:
        print(f"❌ Erro ao deletar usuário: {e}")
    finally:
        input("\nPressione Enter para continuar...")


#Menu Exibir Opções CRUD
def menu_administrativo(usuario_logado):
    # Menu principal do painel administrativo
    if not verificar_se_eh_admin(usuario_logado):
        print("\n❌ Acesso negado! Você não tem permissão de administrador.")
        input("Pressione Enter para continuar...")
        return
    
    while True:
        print("\n" + "=" * 60)
        print("👑 PAINEL ADMINISTRATIVO")
        print("=" * 60)
        print("1. Listar Usuários")
        print("2. Criar Novo Usuário")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Voltar ao Menu Principal")
        print("=" * 60)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            criar_usuario_admin()
        elif opcao == '3':
            atualizar_usuario()
        elif opcao == '4':
            deletar_usuario()
        elif opcao == '0':
            print("Retornando ao menu principal...")
            break
        else:
            print("❌ Opção inválida. Escolha uma opção do menu.")
            input("Pressione Enter para tentar novamente...")
