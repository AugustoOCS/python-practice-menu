import random  # Importa o módulo random para gerar números aleatórios

# Função que gera uma lista com temperaturas extremas (muito frias ou muito quentes)
def gerar_temperaturas_extremas(qtd):
    temperaturas = []  # Lista vazia para armazenar as temperaturas geradas
    
    for i in range(qtd):  # Loop que vai gerar 'qtd' temperaturas
        # Sorteia True ou False para decidir se a temperatura será fria ou quente
        if random.choice([True, False]):
            # Se True, gera temperatura fria entre -40 e -20 graus Celsius
            temp = random.randint(-40, -20)
        else:
            # Se False, gera temperatura quente entre 30 e 45 graus Celsius
            temp = random.randint(30, 45)
        
        temperaturas.append(temp)  # Adiciona a temperatura gerada na lista
    
    return temperaturas  # Retorna a lista de temperaturas geradas

# Exemplo de uso da função
qtd_temperaturas = 5  # Quantidade de temperaturas a serem geradas
temperaturas_geradas = gerar_temperaturas_extremas(qtd_temperaturas)  # Chama a função

# Calcula a maior temperatura da lista gerada
maior_temp = max(temperaturas_geradas)
# Calcula a menor temperatura da lista gerada
menor_temp = min(temperaturas_geradas)

# Imprime as temperaturas geradas e seus valores extremos
print(f"Temperaturas extremas geradas: {temperaturas_geradas}")
print(f"Maior temperatura: {maior_temp} °C")
print(f"Menor temperatura: {menor_temp} °C")
