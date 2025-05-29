N = int(input("Digite a Quantidade de Pessoas: "))
i = 0
soma = 0
cont_30 = 0 #um contador de para pessoas acimda de 30 anos
while i < N:
    i += 1
    peso = int(input("Digite o peso %d: " %i))
    idade = int(input("Digite a idade %d: " %i))
    if idade <= 30:
        continue
    soma += peso
    cont_30 += 1
print("A média de peso das pessoas acima de 30 anos é: %.2f" % (soma / cont_30))