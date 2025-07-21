#Escreva um script python que use compreensão de listas para criar as seguintes listas:
#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
#Todos os números entre 1 e 100 que sejam divisíveis por 7
#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar'])


# Lista de todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]

# Quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

# "par" ou "ímpar" para valores em range(0,30,3)
paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]

# Exibindo os resultados
print("Pares entre 20 e 50:", pares_20_50)
print("Quadrados de 1 a 9:", quadrados)
print("Divisíveis por 7 entre 1 e 100:", divisiveis_por_7)
print("Paridade de range(0,30,3):", paridade)