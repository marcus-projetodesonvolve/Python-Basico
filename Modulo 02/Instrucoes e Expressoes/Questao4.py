#Você é um treinador de corrida e deseja calcular a velocidade média que um atleta precisa manter para completar a Maratona Internacional de São Silvestre, 
# que tem uma distância total de 42.195 km. A fórmula para calcular a velocidade média: (v_media), é dada por: v_media = distancia / tempo)
#Escreva um programa em Python para calcular a velocidade média necessária para completar a maratona em 3 horas.
#Calcule e imprima o resultado em metros/segundo, ou seja, converta a distância de quilômetros para metros  (metro = km /1000) e velocidade de horas para segundos (segundo = hora / 3600).

#Valores:
distancia = 42.195
tempo = 3

v_media = distancia / tempo
print("A velocidade média necessária para completar a maratona é:", v_media, "km/h")

#calcular o resultado em metros/segundo

distancia_metros = distancia / 1000  # Convertendo km para metros
tempo_segundos = tempo / 3600  # Convertendo horas para segundos
v_media_metros_segundo = distancia_metros / tempo_segundos  # Calculando a velocidade média em m/s
print("A velocidade média necessária para completar a maratona é:", v_media_metros_segundo, "m/s")

