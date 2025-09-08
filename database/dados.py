# Lista de usuários cadastrados no sistema
# Cada usuário é um dicionário com nome, cpf, email, celular e senha
_dados_de_usuarios = [
    {
        "nome": "Lucas Barros",
        "cpf": "12345678912",
        "email": "lucas.barros@gmail.com",
        "celular": "21987654321",
        "senha": "123@mudar"
    },
    {
        "nome": "Enzo Okuizumi",
        "cpf": "12345678911",
        "email": "enzo.okuizumi@gmail.com",
        "celular": "11955005657",
        "senha": "123@mudar"
    }
]

# Dicionário que armazena os serviços de cada usuário (resultados, receitas, agendas)
# A chave é o email do usuário
_dados_usuarios_servicos = {
    "lucas.barros@gmail.com": {
        "agendas": [
            "Consulta Ortopedista - 22/07/2024 14:00",
            "Retorno Clínico - 05/08/2024 09:30"
        ]
    },
    "enzo.okuizumi@gmail.com": {
        "agendas": [
            "Consulta Dermatologista - 05/08/2025 16:30",
            "Exame de sangue - 02/08/2025 08:00"
        ]
    }
}