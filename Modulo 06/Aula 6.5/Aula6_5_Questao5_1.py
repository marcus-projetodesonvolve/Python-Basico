from collections import Counter

def diferenca_listas(lista1, lista2):
    contagem1 = Counter(lista1)
    contagem2 = Counter(lista2)
    
    # Subtrai os contadores para manter os elementos únicos e suas quantidades
    resultado = contagem1 - contagem2
    
    # Expande o resultado em uma lista
    diferenca = list(resultado.elements())
    return diferenca

# Exemplo de uso
lista_a = [1, 2, 2, 3, 4, 4, 4]
lista_b = [2, 4, 4]

print("Diferença:", diferenca_listas(lista_a, lista_b))