n = int(input("Digite o valor de Participantes: "))
idade = 0
cont = 1
soma = 0
while cont <= n:
    idade = int(input("Digite a idade do participante: "))
    soma = soma + idade
    cont = cont + 1
media = soma / n
print(f"A média de idade dos participantes é: {media:.2f}")