#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
# O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

#Solicita a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega em quilômetros: "))
#Solicita o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote em quilogramas: "))
#Inicializa o valor do frete
frete = 0
#Verifica a distância e calcula o valor do frete
if distancia <= 100:
    frete = peso * 1
if 101 <= distancia <= 300:
    frete = peso * 1.50
if distancia > 300:
    frete = peso * 2   
#Verifica se o peso do pacote é superior a 10 kg e acrescenta a taxa
if peso > 10:
    frete += 10
#Imprime o valor do frete
print(f"O valor do frete é: R${frete:.2f}")
