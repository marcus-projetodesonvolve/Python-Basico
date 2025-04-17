#2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. 
# Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:
#86 graus Fahrenheit são 30 graus Celsius.

#Entrada:
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: ")) #Lê a temperatura em graus Fahrenheit e converte para inteiro
#Processamento:
celsius = (fahrenheit - 32) * (5/9) #Calcula a temperatura em graus Celsius
#Saida:
print(f'{fahrenheit}ºf graus Fahrenheit são {int(celsius)}ºc graus Celsius') #Imprime a temperatura em graus Fahrenheit e Celsius formatada