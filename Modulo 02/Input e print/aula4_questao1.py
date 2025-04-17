#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. 
# Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:
#O terreno possui 250m2 e custa R$512,490.50
# Comente na linha acima de cada instrução uma breve descrição da instrução.
#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2

#Entrada:
comprimento = int(input("Digite o comprimento do terreno em metros: ")) #Lê o comprimento do terreno em metros e converte para inteiro
largura = int(input("Digite a largura do terreno em metros: ")) #Lê a largura do terreno em metros e converte para inteiro
preco_m2 = float(input("Digite o preço do metro quadrado: ")) #Lê o preço do metro quadrado e converte para ponto flutuante
area_m2 = comprimento * largura #Calcula a área do terreno em metros quadrados
preco_total = preco_m2 * area_m2 #Calcula o preço total do terreno
#Saida:
print(f'O terreno possui {area_m2}m2 e custa R${preco_total:.2f}') #Imprime a área do terreno e o preço total formatado com duas casas decimais