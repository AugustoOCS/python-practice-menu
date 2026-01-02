contagem_dias = 1  # Inicializa o contador de dias começando no dia 1

while True:  # Inicia um loop infinito que só para com o comando 'break'
    # Solicita ao usuário que digite a temperatura do dia atual, convertendo para float
    onda_calor = float(input(f"Digite a Temperatura do Dia {contagem_dias} (°C): "))
    
    # Verifica se a temperatura digitada é menor que 35°C
    if onda_calor < 35:
        # Se for menor que 35, significa que a onda de calor acabou
        print(f"A onda de calor acabou no dia {contagem_dias} com temperatura de {onda_calor}°C.")
        break  # Sai do loop
    
    # Se a temperatura for 35 ou mais, indica que o dia foi de calor extremo
    print(f"Hoje foi um dia de calor extremo ({contagem_dias}) com {onda_calor}°C.")
    contagem_dias += 1  # Incrementa o contador para o próximo dia
