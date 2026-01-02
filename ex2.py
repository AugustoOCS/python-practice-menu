# Solicita ao usuário que informe a quantidade de chuva prevista para São Paulo, em milímetros.
chuva = int(input("Qual a quantidade de chuva prevista pra São Paulo? (mm): "))

# Define uma função para classificar o nível de risco baseado na quantidade de chuva.
def classificar_risco(chuva):
    # Se a chuva for menor que 50 mm, o risco é considerado baixo.
    if chuva < 50:
        return "Baixo"
    # Se a chuva for entre 50 mm e 100 mm, inclusive, o risco é considerado médio.
    elif 50 <= chuva <= 100:
        return "Médio"
    # Se a chuva for maior que 100 mm, o risco é considerado alto.
    else:
        return "Alto"

# Exibe a quantidade de chuva (formatada com duas casas decimais) e a classificação de risco correspondente.
print(f"{chuva:.2f} mm => Risco {classificar_risco(chuva)}")
