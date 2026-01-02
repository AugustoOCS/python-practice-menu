import random  # Importa o módulo random para gerar números aleatórios

# Função para gerar uma lista com quantidades de chuva em mm para uma certa quantidade de dias
def gerar_quantidade_chuva(qtd):
    mm = []  # Lista vazia para armazenar os valores de chuva em mm

    for i in range(qtd):  # Loop que vai gerar a quantidade de chuvas para 'qtd' dias
        chuvas = random.randint(0, 200)  # Gera um valor aleatório entre 0 e 200 mm para o dia
        mm.append(chuvas)  # Adiciona o valor gerado à lista
    
    return mm  # Retorna a lista com as quantidades de chuva geradas

qtd_chuvas = 7  # Define o número de dias para os quais queremos gerar os dados (uma semana)
dias_chuvosos = gerar_quantidade_chuva(qtd_chuvas)  # Gera a lista de chuvas para os 7 dias

total_chuva = sum(dias_chuvosos)  # Soma todas as chuvas para obter o total da semana
media_chuva = total_chuva / qtd_chuvas  # Calcula a média diária de chuva

# Imprime o total de chuva da semana e a média diária formatada com 2 casas decimais
print(f"Quantidade em mm que choveu em uma semana: {total_chuva}mm")
print(f"Média de chuva por dia: {media_chuva:.2f}mm")

# Condição para avisar se a média diária ultrapassar 90mm
if media_chuva > 90:
    print("Semana crítica! Monitoramento intensivo necessário")

