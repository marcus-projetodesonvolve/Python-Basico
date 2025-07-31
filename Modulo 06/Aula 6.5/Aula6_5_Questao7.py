def avalia_tabuleiro(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            print(linha[0])
            return

    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            print(tabuleiro[0][i])
            return

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        print(tabuleiro[0][0])
        return
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        print(tabuleiro[0][2])
        return

    # Se ninguém ganhou
    print("Empate")