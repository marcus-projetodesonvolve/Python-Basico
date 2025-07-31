def cria_matriz(n):
    matriz = [[linha * coluna for coluna in range(n)] for linha in range(n)]
    return matriz

# Exemplo de uso
n = int(input("Digite o tamanho da matriz: "))
matriz_gerada = cria_matriz(n)

for linha in matriz_gerada:
    print(linha)