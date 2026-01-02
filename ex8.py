# Função que valida se o nome da cidade atende aos critérios:
# - Ter mais de 3 caracteres
# - Começar com letra maiúscula
def validar_cidade(nome):
    return len(nome) > 3 and nome[0].isupper()

# Solicita ao usuário que digite o nome da cidade
cidade = input("Digite o nome da cidade: ")

# Chama a função validar_cidade e armazena o resultado (True ou False)
validacao = validar_cidade(cidade)

# Imprime se o nome digitado é válido ou não
print(f"O Nome digitado é válido? {validacao}")
