import random

def embaralhar_palavra(palavra):
    if len(palavra) <= 3:
        return palavra  # palavras muito curtas não precisam ser embaralhadas

    primeira, meio, ultima = palavra[0], list(palavra[1:-1]), palavra[-1]
    random.shuffle(meio)
    return primeira + ''.join(meio) + ultima

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(p) for p in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
entrada = input("Digite uma frase: ")
resultado = embaralhar_palavras(entrada)
print("Frase embaralhada:", resultado)