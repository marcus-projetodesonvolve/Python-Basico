#Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
# Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos,
#  indicando que podem entrar no bar, e False caso contrário.

# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas as idades são maiores que 17
pode_entrar = idade_juliana > 17 and idade_cris > 17

# Imprime o resultado
print(pode_entrar)