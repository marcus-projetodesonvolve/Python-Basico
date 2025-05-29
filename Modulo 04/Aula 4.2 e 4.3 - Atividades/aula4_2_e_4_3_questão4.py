#Você vai criar um sistema que registra os resultados dos jogos do Atlético MG ao longo de um campeonato. 
# Seu sistema vai receber os resultados de todos os jogos do Galo, e deve calcular a pontuação do time sabendo que vitórias valem 3 pontos, empates 1 ponto e derrotas 0 pontos.

n = int(input("Digite Quantos Jogos o Galo ja disputou: "))
pontos = 0
vitoria = 0
derrota = 0
empate = 0
for jogo in range(n):
    gols_galo = int(input("Digite Quantos Gols Do Galo: "))
    gols_adversario = int(input("Digite Quantos Gols Do Adversario: "))
    if gols_galo > gols_adversario:
        print("Galo Venceu")
        pontos = pontos + 3
        vitoria = vitoria + 1
    elif gols_galo < gols_adversario:
        print("Galo Perdeu")
        derrota = derrota + 1
    else:
        print("Galo Empatou")
        pontos = pontos + 1
        empate += 1
print("Galo Venceu ", vitoria, "Partidas")
print("Galo Perdeu ", derrota, "Partidas")
print("Galo Empatou ", empate, "Partidas")
print("Pontos: ", pontos)
