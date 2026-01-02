# Solicita ao usuário que informe a quantidade de chuva prevista para São Paulo, em milímetros.
chuva = int(input("Qual a quantidade de chuva prevista pra São Paulo? (mm): "))

# Verifica se a quantidade de chuva é maior ou igual a 100 mm.
if(chuva >= 100):
    # Se for, exibe uma mensagem de alerta para risco alto de inundação.
    print("ALERTA: Risco alto de inundação")
else:
    # Se for menor que 100 mm, informa que o nível de risco é normal.
    print("Nível de risco normal")
