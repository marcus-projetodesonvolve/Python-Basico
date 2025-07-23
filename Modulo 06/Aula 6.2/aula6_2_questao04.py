#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
#Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

# Receber a primeira lista do usuário
entrada1 = input("Digite os números da primeira lista, separados por espaço: ")
lista1 = [int(num) for num in entrada1.split()]

# Receber a segunda lista do usuário
entrada2 = input("Digite os números da segunda lista, separados por espaço: ")
lista2 = [int(num) for num in entrada2.split()]

# Combinar alternadamente as listas
lista_combinada = []
tam1 = len(lista1)
tam2 = len(lista2)
menor_tam = min(tam1, tam2)

# Intercalar até o final da menor lista
for i in range(menor_tam):
    lista_combinada.append(lista1[i])
    lista_combinada.append(lista2[i])

# Adicionar o restante da lista maior
if tam1 > tam2:
    lista_combinada.extend(lista1[menor_tam:])
elif tam2 > tam1:
    lista_combinada.extend(lista2[menor_tam:])

# Exibir o resultado
print("Lista combinada alternada:")
print(lista_combinada)