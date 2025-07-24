import random

# Gerar lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# Encontrar o intervalo com mais números negativos
max_negativos = 0
inicio_max = 0
fim_max = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]
        negativos = [num for num in sublista if num < 0]
        if len(negativos) > max_negativos:
            max_negativos = len(negativos)
            inicio_max = i
            fim_max = j

# Apagar o intervalo da lista
del lista[inicio_max:fim_max]

print("Lista após remover intervalo com mais negativos:", lista)