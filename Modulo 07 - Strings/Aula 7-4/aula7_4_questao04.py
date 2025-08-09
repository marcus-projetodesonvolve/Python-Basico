import random

# Função para carregar palavras
def carregar_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
    return palavras

# Função para carregar estágios do enforcado
def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        estagios = conteudo.strip().split("\n\n")  # separa por blocos
    return estagios

# Função para imprimir o enforcado
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Função principal do jogo
def jogar_forca():
    palavras = carregar_palavras()
    estagios = carregar_enforcado()
    palavra = random.choice(palavras)
    progresso = ["_" for _ in palavra]
    letras_usadas = set()
    erros = 0
    max_erros = 6

    print("Bem-vindo ao jogo da forca!")
    print(" ".join(progresso))

    while erros < max_erros and "_" in progresso:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    progresso[i] = letra
            print("Acertou!")
        else:
            erros += 1
            print("Errou!")
            imprime_enforcado(erros, estagios)

        print(" ".join(progresso))
        print(f"Erros: {erros}/6")

    if "_" not in progresso:
        print("Parabéns! Você venceu! 🎉")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

# Executa o jogo
jogar_forca()