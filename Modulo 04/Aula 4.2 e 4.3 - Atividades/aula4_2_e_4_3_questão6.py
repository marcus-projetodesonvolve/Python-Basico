#Escreva um programa que lê uma quantidade indefinida de valores e informa o maior e o menor valor digitados. A leitura é encerrada quando o usuário digitar o valor 0 (zero).

#Definindo Variaveis
maior = float('-inf')  # Inicializa com o menor valor possível
menor = float('inf')  # Inicializa com o maior valor possível

while True:
    valor = float(input("Digite um valor (0 para encerrar): "))
    
    if valor == 0: break  # Encerra o loop se o valor for 0
        
    if valor > maior:
            maior = valor  # Atualiza o maior valor se o atual for maior
    
    if valor < menor:
            menor = valor  # Atualiza o menor valor se o atual for menor

# Exibe os resultados
print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")