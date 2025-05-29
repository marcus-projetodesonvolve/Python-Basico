#Dado um número inteiro positivo informado pelo usuário, crie um programa em Python que utilize o comando for para calcular e exibir a soma dos números de 1 até o número informado.

# Crie um programa em Python que utilize o comando for para calcular e exibir a soma dos números de 1 até o número informado pelo usuário.
numero = int(input("Informe um número inteiro positivo: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print(f"A soma dos números de 1 até {numero} é: {soma}")
