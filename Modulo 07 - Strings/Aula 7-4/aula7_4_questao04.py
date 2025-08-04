palavras = [
    "abacaxi",
    "girassol",
    "paralelepipedo",
    "computador",
    "maratona",
    "bicicleta",
    "historia",
    "borboleta",
    "espaguete",
    "pipoca"
]

with open("gabarito_forca.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")