from typing import List, Dict
from database.dados import _dados_usuarios_servicos
import core.validacoes as validacoes


def obter_agendas_por_email(email: str) -> List[str]:
    return _dados_usuarios_servicos.get(email, {}).get("agendas", [])


def listar_agendas(email: str) -> None:
    agendas = obter_agendas_por_email(email)
    print("\nMinhas Agendas:")
    if not agendas:
        print("(sem itens)")
        return
    for indice, item in enumerate(agendas, start=1):
        print(f"{indice}. {item}")


def criar_agenda(email: str, descricao: str) -> bool:
    try:
        if not descricao or len(descricao.strip()) < 5:
            raise ValueError("Descrição deve ter ao menos 5 caracteres.")
        servicos = _dados_usuarios_servicos.setdefault(email, {"resultados": [], "receitas": [], "agendas": []})
        servicos["agendas"].append(descricao.strip())
        print("Item adicionado com sucesso.")
        return True
    except Exception as exc:
        print(f"Erro ao adicionar: {exc}")
        return False


def atualizar_agenda(email: str, indice: int, nova_descricao: str) -> bool:
    try:
        if indice <= 0:
            raise IndexError("Índice deve iniciar em 1.")
        if not nova_descricao or len(nova_descricao.strip()) < 5:
            raise ValueError("Nova descrição deve ter ao menos 5 caracteres.")
        agendas = obter_agendas_por_email(email)
        agendas[indice - 1] = nova_descricao.strip()
        print("Item atualizado com sucesso.")
        return True
    except IndexError:
        print("Índice inválido para atualização.")
        return False
    except Exception as exc:
        print(f"Erro ao atualizar: {exc}")
        return False
    finally:
        pass


def excluir_agenda(email: str, indice: int) -> bool:
    try:
        if indice <= 0:
            raise IndexError("Índice deve iniciar em 1.")
        agendas = obter_agendas_por_email(email)
        removido = agendas.pop(indice - 1)
        print(f"Item removido: {removido}")
        return True
    except IndexError:
        print("Índice inválido para exclusão.")
        return False
    except Exception as exc:
        print(f"Erro ao excluir: {exc}")
        return False
    finally:
        pass


def submenu_crud_agendas(email: str) -> None:
    while True:
        print("\n╔══════════════════════════════════════════════╗")
        print("║            CRUD - MINHAS AGENDAS             ║")
        print("╚══════════════════════════════════════════════╝")
        print("1. Listar agendas")
        print("2. Adicionar agenda")
        print("3. Atualizar agenda")
        print("4. Excluir agenda")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            listar_agendas(email)
            input("\nEnter para continuar...")
        elif opcao == '2':
            descricao = input("Descrição (ex: Consulta Dermatologista - 10/10/2025 14:00): ")
            criar_agenda(email, descricao)
            input("\nEnter para continuar...")
        elif opcao == '3':
            listar_agendas(email)
            try:
                indice = int(input("Número do item a atualizar: "))
                nova = input("Nova descrição: ")
                atualizar_agenda(email, indice, nova)
            except ValueError:
                print("Digite um número válido para o índice.")
            finally:
                input("\nEnter para continuar...")
        elif opcao == '4':
            listar_agendas(email)
            try:
                indice = int(input("Número do item a excluir: "))
                excluir_agenda(email, indice)
            except ValueError:
                print("Digite um número válido para o índice.")
            finally:
                input("\nEnter para continuar...")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

