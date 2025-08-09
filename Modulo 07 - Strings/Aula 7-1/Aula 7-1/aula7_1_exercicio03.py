#Escreva um script que dado uma frase conta os espaços em branco.

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Conta os espaços em branco
quantidade_espacos = frase.count(" ")

# Exibe o resultado
print("Número de espaços em branco:", quantidade_espacos)