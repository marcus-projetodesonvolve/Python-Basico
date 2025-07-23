#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
#Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random

# Gerar 20 valores inteiros aleatórios entre -100 e 100
lista_original = [] 
for i in range(20):
    valor = random.randint(-100, 100)
    lista_original.append(valor)  


# Criar uma lista ordenada sem modificar a original
lista_ordenada = sorted(lista_original)

# Encontrar os índices do maior e menor valor
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

# Exibir os resultados
print("Lista ordenada (sem modificar a original):")
print(lista_ordenada)

print("Lista original:")
print(lista_original)

print("Índice do maior valor: ", ({max(lista_original)}))
print("Índice do menor valor: ", ({min(lista_original)}))