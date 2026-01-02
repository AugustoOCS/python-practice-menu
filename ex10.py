# Função que verifica o nível do rio e avisa se há risco de enchente
def nivel_rio():
    # Solicita ao usuário que informe o nível atual do rio (em metros) e converte para float
    nivel = float(input("Qual é o nível atual do rio (metros): "))
    
    # Se o nível for maior que 5 metros, emite alerta para evacuação da área
    if nivel > 5:
        print("EVACUAR A ÁREA!")
    else:
        # Se o nível for menor ou igual a 5 metros, indica que está seguro
        print("Segurança controlada.")

# Chama a função para executar a verificação
nivel_rio()
