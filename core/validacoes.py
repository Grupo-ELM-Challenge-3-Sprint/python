import re

# Função para validar se o CPF contém apenas números e tem 11 dígitos
def validar_cpf(cpf):
    """Verifica se o CPF contém apenas números e tem 11 dígitos."""
    if cpf.isdigit() and len(cpf) == 11:
        return True
    return False

# Função para validar se o email está em um formato básico correto
def validar_email(email):
    """Verifica um formato básico de email."""
    # Regex simples para validação de email
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(padrao, email):
        return True
    return False

# Função para validar se o número de celular está correto (10 ou 11 dígitos, só números)
def validar_celular(celular):
    """Verifica se o celular contém apenas números e tem entre 10 e 11 dígitos (considerando DDD)."""
    if celular.isdigit() and 10 <= len(celular) <= 11:
        return True
    return False

# Função para validar nome completo (mínimo 2 palavras e >= 5 caracteres totais)
def validar_nome(nome: str) -> bool:
    if not nome:
        return False
    nome_limpo = nome.strip()
    if len(nome_limpo) < 2:
        return False
    total_alpha = sum(1 for ch in nome_limpo if ch.isalpha())
    return total_alpha >= 2

# Função para validar senha (mínimo 6 chars; recomenda letras e números)
def validar_senha(senha: str) -> bool:
    """Senha mínima de 6 caracteres; ideal conter letras e números."""
    if not senha or len(senha) < 6:
        return False
    return True