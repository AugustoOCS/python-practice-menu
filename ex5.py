# Lista com nomes de cidades que receberão alertas
ccd = ["Mumbai", "Kolkata", "Patna"] 

# Definição da função 'enviar_alertas' que recebe uma lista de cidades
def enviar_alertas(cidades):
    # Para cada cidade na lista recebida como argumento
    for cidade in cidades:
        # Exibe uma mensagem informando que está enviando um alerta para aquela cidade
        print(f"Enviando alerta para {cidade}: risco alto de inundação!")

# Chama a função 'enviar_alertas' passando a lista 'ccd' como argumento
enviar_alertas(ccd)
