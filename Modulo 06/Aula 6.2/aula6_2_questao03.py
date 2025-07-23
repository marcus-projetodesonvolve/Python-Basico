#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
#Atenção, a lista de intersecções não pode ter duplicatas.

import random
from collections import Counter

# Gerar duas listas com 20 valores aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar os valores que aparecem em ambas as listas
intersecao = sorted(set(lista1) & set(lista2))

# Contar a frequência dos elementos nas listas
frequencia1 = Counter(lista1)
frequencia2 = Counter(lista2)

# Exibir os resultados
print("Lista 1:")
print(lista1)

print("Lista 2:")
print(lista2)

print("Lista de interseção (ordenada):")
print(intersecao)

print("Frequência dos elementos na Lista 1:")
for elemento in intersecao:
    print(f"{elemento}: {frequencia1[elemento]} vez(es)")

print("Frequência dos elementos na Lista 2:")
for elemento in intersecao:
    print(f"{elemento}: {frequencia2[elemento]} vez(es)")