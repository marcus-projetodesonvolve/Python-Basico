#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. 
#Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random

numero = random.randint(1,10)

while True:

    palpite = int(input("Adivinhe o numero entre 1 e 10"))
    if palpite < numero:
        print("Muito Baixo! Tente novamente!")
    elif palpite > numero:
        print("Muito Alto! Tente novamente")
    else:
        print("Parabens! Você Acertou!")
        break