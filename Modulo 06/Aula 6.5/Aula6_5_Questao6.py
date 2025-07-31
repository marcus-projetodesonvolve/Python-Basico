def dividir_em_blocos(lista, tamanho_bloco):
    resultado = []
    for i in range(0, len(lista), tamanho_bloco):
        sublista = lista[i:i + tamanho_bloco]
        resultado.append(sublista)
    return resultado

# Exemplo de uso
lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tamanho = 4

sublistas = dividir_em_blocos(lista_exemplo, tamanho)
print("Sublistas:", sublistas)