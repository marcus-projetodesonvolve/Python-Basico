#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
# Anagramas são palavras com os mesmos caracteres rearranjados.

# Importa o módulo necessário
from collections import Counter

# Função para encontrar anagramas
def encontrar_anagramas(texto, palavra_objetivo):
    resultado = []
    tamanho = len(palavra_objetivo)
    contador_objetivo = Counter(palavra_objetivo)

    for i in range(len(texto) - tamanho + 1):
        trecho = texto[i:i + tamanho]
        if Counter(trecho) == contador_objetivo:
            resultado.append(trecho)

    return resultado

# Entrada do usuário
texto = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Chamada da função e exibição do resultado
anagramas = encontrar_anagramas(texto, palavra_objetivo)
print("Anagramas encontrados:", anagramas)