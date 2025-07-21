#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. 
# Regras:
#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. 
# Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)


import random

def encrypt(lista_de_nomes):
    # Gera a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in lista_de_nomes:
        nome_criptografado = ""
        for caractere in nome:
            codigo = ord(caractere)
            if 33 <= codigo <= 126:
                novo_codigo = codigo + chave
                # Garante que permanece no intervalo visível (33–126)
                if novo_codigo > 126:
                    novo_codigo = 33 + (novo_codigo - 127)
                nome_criptografado += chr(novo_codigo)
            else:
                # Mantém caracteres fora do intervalo como estão
                nome_criptografado += caractere
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave