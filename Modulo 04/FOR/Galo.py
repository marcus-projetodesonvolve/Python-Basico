n = int(input("Digite Quantos Jogos o Galo Disputou: "))
soma_vitoria, soma_derrota, soma_empate = 0, 0, 0

for jogo in range(n):
    gols_galo = int(input(f"Digite Quantos Gols Do Galo jogo {jogo}: "))
    gols_adversario = int(input(f"Digite Quantos Gols Do Adversario jogo {jogo}: "))
    if gols_galo > gols_adversario:
        print("Galo Venceu")
        soma_vitoria += 1
    elif gols_galo < gols_adversario:
        print("Galo Perdeu")
        soma_derrota += 1
    else:
        print("Galo Empatou")
        soma_empate += 1
print("Galo Venceu ", soma_vitoria, "Partidas")
print("Galo Perdeu ", soma_derrota, "Partidas")
print("Galo Empatou ", soma_empate, "Partidas")
pontos = (soma_vitoria * 3) + (soma_empate * 1)
print("Pontos: ", pontos)