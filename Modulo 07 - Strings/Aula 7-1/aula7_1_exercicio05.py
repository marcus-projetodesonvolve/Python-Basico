#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou". Exemplo:

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Inicializa variáveis
vogais = "aeiouAEIOU"
quantidade = 0
indices = []

# Percorre a frase verificando cada caractere
for i in range(len(frase)):
    if frase[i] in vogais:
        quantidade += 1
        indices.append(i)

# Exibe os resultados
print("Quantidade de vogais:", quantidade)
print("Índices das vogais:", indices)