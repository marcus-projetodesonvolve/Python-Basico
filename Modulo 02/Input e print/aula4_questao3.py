#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. 
# Note no exemplo a seguir que:
#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)
#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
#Digite o nome do produto 1:calça
#Digite o preço unitário do produto 1:199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2:camisa
#Digite o preço unitário do produto 2:49.95
#Digite a quantidade do produto 2:10
#Digite o nome do produto 3:cinto
#Digite o preço unitário do produto 3:25
#Digite a quantidade do produto 3:3

#Entrada:
produto1 = input("Digite o nome do produto 1: ") #Lê o nome do produto 1
valor_unitario1 = float(input("Digite o preço unitário do produto 1: ")) #Lê o preço unitário do produto 1 e converte para ponto flutuante
quantidade1 = int(input("Digite a quantidade do produto 1: ")) #Lê a quantidade do produto 1 e converte para inteiro
produto2 = input("Digite o nome do produto 2: ") #Lê o nome do produto 2
valor_unitario2 = float(input("Digite o preço unitário do produto 2: ")) #Lê o preço unitário do produto 2 e converte para ponto flutuante
quantidade2 = int(input("Digite a quantidade do produto 2: ")) #Lê a quantidade do produto 2 e converte para inteiro
produto3 = input("Digite o nome do produto 3: ") #Lê o nome do produto 3
valor_unitario3 = float(input("Digite o preço unitário do produto 3: ")) #Lê o preço unitário do produto 3 e converte para ponto flutuante
quantidade3 = int(input("Digite a quantidade do produto 3: ")) #Lê a quantidade do produto 3 e converte para inteiro
#Processamento:
preco_total1 = valor_unitario1 * quantidade1 #Calcula o preço total do produto 1
preco_total2 = valor_unitario2 * quantidade2 #Calcula o preço total do produto 2
preco_total3 = valor_unitario3 * quantidade3 #Calcula o preço total do produto 3
#Saida:
print(f'Total: R${preco_total1 + preco_total2 + preco_total3:,.2f}') #Imprime o preço total da compra formatado com separador de milhar e duas casas decimais
print(f'O Produto 1 é: {produto1}, e o preço unitário é:, {valor_unitario1}, o valor total do item é: {preco_total1}') #Imprime o nome e o preço unitário do produto 1
print(f'O Produto 2 é: {produto2}, e o preço unitário é:, {valor_unitario2}, o valor total do item é: {preco_total2}') #Imprime o nome e o preço unitário do produto 2
print(f'O Produto 3 é: {produto3}, e o preço unitário é:, {valor_unitario3}, o valor total do item é: {preco_total3}') #Imprime o nome e o preço unitário do produto 3
#produto2 = input("Digite o nome do produto 2: ") #Lê o nome do produto 2

