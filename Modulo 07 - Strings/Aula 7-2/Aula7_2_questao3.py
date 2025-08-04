import string

def eh_palindromo(frase):
    # Remove espaços e pontuações, e transforma tudo em minúsculas
    frase_limpa = ''.join(
        caractere.lower() for caractere in frase
        if caractere.isalnum()
    )
    return frase_limpa == frase_limpa[::-1]

# Loop principal
while True:
    entrada = input("Digite uma frase (ou 'Fim' para encerrar): ")
    if entrada.strip().lower() == "fim":
        print("Programa encerrado.")
        break
    if eh_palindromo(entrada):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")