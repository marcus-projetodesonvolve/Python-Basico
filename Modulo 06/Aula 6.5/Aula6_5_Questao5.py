def pares_unicos(lista, soma_alvo):
    vistos = set()
    pares = set()

    for numero in lista:
        complemento = soma_alvo - numero
        if complemento in vistos:
            # Usa tuple ordenada para garantir unicidade independente da ordem
            pares.add(tuple(sorted((numero, complemento))))
        vistos.add(numero)

    return list(pares)

# Exemplo de uso
numeros = [1, 3, 2, 2, 4, 5, 0, 6]
alvo = 6
resultado = pares_unicos(numeros, alvo)

print(resultado)