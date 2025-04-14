#Q3
#Você está desenvolvendo um software de conversão de moeda e precisa calcular o valor equivalente em yuan chinês a partir de uma quantia em real. 
#A taxa de câmbio é de 0.69 BRL (real) para 1 CNY (yuan). 
#Escreva um programa que define em uma variável uma quantia em reais (BRL) e calcula o valor equivalente em yuan (CNY). Imprima o resultado.

# Definindo a taxa de câmbio
valor_br = 0.69  # 1 CNY = 0.69 BRL
quantia_br = 500  # Exemplo
convertido = quantia_br / valor_br  # Convertendo de BRL para CNY
print("Valor em CNY:", (convertido))