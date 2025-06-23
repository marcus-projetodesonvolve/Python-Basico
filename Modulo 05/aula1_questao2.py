#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n
#Biblioteca random: Função randint()
#Biblioteca math:  Função sqrt()

import random
import math

n = int(input("Digite a Quantidade de valores:"))
soma = 0
for i in range(n):
    valor = random.randint(0, 100)
    print(valor)
    soma += valor
print(soma)
print(f"A Raiz Quadrada da soma é: {math.sqrt(soma):.2f}")
