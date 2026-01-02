# Dicionário que contém as cidades e a respectiva quantidade de chuva prevista, em milímetros.
chuvas = {     
    "Mumbai": 120, 
    "Delhi": 45, 
    "Chennai": 80, 
    "Kolkata": 130, 
    "Jaipur": 30 
} 

# Função que classifica o nível de risco com base na quantidade de chuva.
def classificar_risco(chuva):
    # Se a chuva for menor que 50 mm, o risco é considerado baixo.
    if chuva < 50:
        return "Baixo"
    # Se a chuva estiver entre 50 e 100 mm, inclusive, o risco é considerado médio.
    elif 50 <= chuva <= 100:
        return "Médio"
    # Se a chuva for maior que 100 mm, o risco é considerado alto.
    else:
        return "Alto"

# Função que percorre todas as cidades e imprime apenas aquelas com risco alto.
def imprimir_cidades_com_risco_alto(chuvas):
    # Laço que percorre cada par cidade e quantidade de chuva.
    for cidade, mm in chuvas.items():
        # Verifica se a classificação do risco é "Alto".
        if classificar_risco(mm) == "Alto":
            # Exibe a cidade, a quantidade de chuva e o nível de risco.
            print(f"{cidade} => {mm} mm => RISCO ALTO")

# Chamada da função para imprimir as cidades com risco alto.
imprimir_cidades_com_risco_alto(chuvas)
