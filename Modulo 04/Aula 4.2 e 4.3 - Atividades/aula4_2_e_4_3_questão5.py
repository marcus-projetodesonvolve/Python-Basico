'''Faça um programa que lê dois inteiros N e M, e imprime na tela um campo de batalha naval. O tabuleiro deve possuir N linhas e M colunas. 
A primeira linha é composta por um espaço em branco e o cabeçalho das colunas, ou seja, valores de 1 a M. 
As N linhas seguintes iniciam com o cabeçalho da linha, ou seja, seu número, seguido de M caracteres "/" (barra) indicando uma possível posição jogável.'''

def gerar_tabuleiro(n, m):
    # Imprime cabeçalho das colunas
    print("  ", end=" ")
    for coluna in range(1, m + 1):
        print(coluna, end=" ")
    print()

    # Imprime as linhas do tabuleiro
    for linha in range(1, n + 1):
        print(linha, end=" ")
        for _ in range(m):
            print("/", end=" ")
        print()

# Entrada dos valores de N e M
n = int(input("Digite o número de linhas (N): "))
m = int(input("Digite o número de colunas (M): "))

# Gera e imprime o tabuleiro
gerar_tabuleiro(n, m)