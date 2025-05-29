#Escreva um programa que lê 10 valores inteiros positivos do usuário e ao final imprime a média dos valores digitados com duas casas decimais

valor = int(input("Informe um valor inteiro positivo: "))
s = 0
for i in range(1, 11):
    while valor < 0:
        print("Valor inválido. Informe um valor inteiro positivo.")
        valor = int(input("Informe um valor inteiro positivo: "))
    s += valor
    if i < 10:
        valor = int(input("Informe um valor inteiro positivo: "))
media = s / 10
print(f"A média dos valores digitados é: {media:.2f}")