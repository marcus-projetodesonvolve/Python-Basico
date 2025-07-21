#Solicite uma frase do usuário e usando compreensão de listas imprima:
#A lista de vogais da frase, ordenada alfabeticamente
#A lista de consoantes da frase (remova espaços em branco)


# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = sorted([letra for letra in frase if letra in 'aeiou'])

# Lista de consoantes (remove espaços e ignora vogais)
consoantes = [letra for letra in frase if letra.isalpha() and letra not in 'aeiou']

# Exibindo os resultados
print("Vogais ordenadas:", vogais)
print("Consoantes:", consoantes)