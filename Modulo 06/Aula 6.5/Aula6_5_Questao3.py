def ordena_por_comprimento(lista):
    return sorted(lista, key=lambda s: len(s))

# Exemplo de uso
nomes = ["Ana", "Beatriz", "João", "Alexandre", "Lu"]
ordenados = ordena_por_comprimento(nomes)

print(ordenados)