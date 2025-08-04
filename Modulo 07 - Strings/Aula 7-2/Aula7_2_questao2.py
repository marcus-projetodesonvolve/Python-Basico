def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    nova_frase = ""
    for caractere in frase:
        if caractere in vogais:
            nova_frase += "*"
        else:
            nova_frase += caractere
    return nova_frase

# Exemplo de uso
frase_usuario = input("Digite uma frase: ")
frase_alterada = substituir_vogais(frase_usuario)
print("Frase com vogais substituídas:", frase_alterada)