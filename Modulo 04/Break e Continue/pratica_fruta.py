fruta = "Banana"
for i in range(5):
    palpite = input("Digite o palpite: ")
    if palpite == fruta:
        print("Você acertou!")
        break
    else:
        print("Você errou!")
        if i == 4:
            print("Você perdeu!")
            break
print("Fim do jogo!")