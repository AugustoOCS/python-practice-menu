import random

# ==========================
# 1. Alerta de risco para São Paulo (simples)
# ==========================
def alerta_sp_simples():
    print("\n--- 1. Alerta Simples para São Paulo ---")
    chuva = int(input("Qual a quantidade de chuva prevista pra São Paulo? (mm): "))
    if chuva >= 100:
        print("ALERTA: Risco alto de inundação")
    else:
        print("Nível de risco normal")

# ==========================
# 2. Classificação de risco com três níveis
# ==========================
def classificar_risco(chuva):
    if chuva < 50:
        return "Baixo"
    elif 50 <= chuva <= 100:
        return "Médio"
    else:
        return "Alto"

def alerta_sp_classificado():
    print("\n--- 2. Alerta Classificado para São Paulo ---")
    chuva = int(input("Qual a quantidade de chuva prevista pra São Paulo? (mm): "))
    print(f"{chuva:.2f} mm => Risco {classificar_risco(chuva)}")

# ==========================
# 3. Cidades e risco alto de inundação (dicionário)
# ==========================
chuvas = {
    "Mumbai": 120,
    "Delhi": 45,
    "Chennai": 80,
    "Kolkata": 130,
    "Jaipur": 30
}

def imprimir_cidades_com_risco_alto():
    print("\n--- 3. Cidades com Risco Alto ---")
    for cidade, mm in chuvas.items():
        if classificar_risco(mm) == "Alto":
            print(f"{cidade} => {mm} mm => RISCO ALTO")

# ==========================
# 4. Geração de temperaturas extremas
# ==========================
def gerar_temperaturas_extremas(qtd):
    temperaturas = []
    for _ in range(qtd):
        if random.choice([True, False]):
            temp = random.randint(-40, -20)
        else:
            temp = random.randint(30, 45)
        temperaturas.append(temp)
    return temperaturas

def mostrar_temperaturas():
    print("\n--- 4. Temperaturas Extremas ---")
    qtd = 5
    temps = gerar_temperaturas_extremas(qtd)
    print(f"Temperaturas extremas geradas: {temps}")
    print(f"Maior temperatura: {max(temps)} °C")
    print(f"Menor temperatura: {min(temps)} °C")

# ==========================
# 5. Envio de alertas para cidades
# ==========================
ccd = ["Mumbai", "Kolkata", "Patna"]

def enviar_alertas(cidades):
    print("\n--- 5. Envio de Alertas ---")
    for cidade in cidades:
        print(f"Enviando alerta para {cidade}: risco alto de inundação!")

# ==========================
# 6. Geração aleatória de chuvas para vários dias
# ==========================
def gerar_quantidade_chuva(qtd):
    mm = []
    for _ in range(qtd):
        chuvas = random.randint(0, 200)
        mm.append(chuvas)
    return mm

def analisar_chuvas():
    print("\n--- 6. Análise de Chuvas ---")
    qtd = 7
    dias_chuvosos = gerar_quantidade_chuva(qtd)
    total = sum(dias_chuvosos)
    media = total / qtd
    print(f"Quantidade em mm que choveu em uma semana: {total}mm")
    print(f"Média de chuva por dia: {media:.2f}mm")
    if media > 90:
        print("Semana crítica! Monitoramento intensivo necessário")

# ==========================
# 7. Monitoramento de onda de calor
# ==========================
def monitorar_onda_calor():
    print("\n--- 7. Monitoramento da Onda de Calor ---")
    contagem_dias = 1
    while True:
        try:
            temp = float(input(f"Digite a Temperatura do Dia {contagem_dias} (°C): "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        if temp < 35:
            print(f"A onda de calor acabou no dia {contagem_dias} com temperatura de {temp}°C.")
            break
        print(f"Hoje foi um dia de calor extremo ({contagem_dias}) com {temp}°C.")
        contagem_dias += 1

# ==========================
# 8. Validação de nome de cidade
# ==========================
def validar_cidade(nome):
    return len(nome) > 3 and nome[0].isupper()

def solicitar_validacao_cidade():
    print("\n--- 8. Validação de Nome de Cidade ---")
    cidade = input("Digite o nome da cidade: ")
    valido = validar_cidade(cidade)
    print(f"O Nome digitado é válido? {valido}")

# ==========================
# 9. Lista e impressão de cidades com risco alto
# ==========================
def lista_cidades():
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

    cidades_alto_risco = [cidade for cidade in cidades if cidade["risco"] == "alto"]

    print("\n--- 9. Cidades com risco alto de enchente ---")
    for cidade in cidades_alto_risco:
        print(f"- {cidade['nome']}")
    return cidades_alto_risco

# ==========================
# 10. Verificação do nível do rio
# ==========================
def nivel_rio():
    print("\n--- 10. Verificação do Nível do Rio ---")
    try:
        nivel = float(input("Qual é o nível atual do rio (metros): "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return
    if nivel > 5:
        print("EVACUAR A ÁREA!")
    else:
        print("Segurança controlada.")

# ==========================
# Menu para escolher qual parte executar
# ==========================
def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Alerta simples São Paulo")
        print("2 - Alerta classificado São Paulo")
        print("3 - Cidades com risco alto")
        print("4 - Temperaturas extremas")
        print("5 - Enviar alertas para cidades")
        print("6 - Analisar chuvas semanais")
        print("7 - Monitorar onda de calor")
        print("8 - Validar nome de cidade")
        print("9 - Listar cidades de risco alto")
        print("10 - Verificar nível do rio")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            alerta_sp_simples()
        elif escolha == "2":
            alerta_sp_classificado()
        elif escolha == "3":
            imprimir_cidades_com_risco_alto()
        elif escolha == "4":
            mostrar_temperaturas()
        elif escolha == "5":
            enviar_alertas(ccd)
        elif escolha == "6":
            analisar_chuvas()
        elif escolha == "7":
            monitorar_onda_calor()
        elif escolha == "8":
            solicitar_validacao_cidade()
        elif escolha == "9":
            lista_cidades()
        elif escolha == "10":
            nivel_rio()
        elif escolha == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
