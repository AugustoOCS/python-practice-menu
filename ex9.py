# Função que retorna uma lista de cidades com risco alto de enchente
def lista_cidades():
    # Lista de dicionários, onde cada dicionário representa uma cidade e seu nível de risco
    cidades = [
        {"nome": "São Paulo", "risco": "médio"},
        {"nome": "Rio de Janeiro", "risco": "alto"},
        {"nome": "Fortaleza", "risco": "alto"},
        {"nome": "Manaus", "risco": "alto"},
        {"nome": "Porto Alegre", "risco": "médio"},
        {"nome": "Recife", "risco": "alto"},
        {"nome": "Salvador", "risco": "médio"},
        {"nome": "Belo Horizonte", "risco": "baixo"},
        {"nome": "Curitiba", "risco": "baixo"},
        {"nome": "Belém", "risco": "alto"}
    ]

    # Filtra as cidades com risco "alto" usando list comprehension
    cidades_alto_risco = [cidade for cidade in cidades if cidade["risco"] == "alto"]

    # Imprime as cidades com risco alto
    print("Cidades com risco alto de enchente")
    for cidade in cidades_alto_risco:
        print(f"- {cidade['nome']}")

    # Retorna a lista das cidades de alto risco
    return cidades_alto_risco

# Chama a função e armazena a lista de cidades críticas em uma variável
cidades_criticas = lista_cidades()
