n = int(input("Digite o valor de Experimentos Registrados: "))
qtn_sapo = 0
qtn_rato = 0
qtn_coelho = 0
cont = 1
while cont <= n:
    tipo = input("Digite o tipo de animal (Sapo, Rato ou Coelho): ")
    qtn = int(input("Digite a quantidade de animais: "))
    if tipo == "S":
        qtn_sapo += qtn
    elif tipo == "R":
        qtn_rato += qtn
    elif tipo == "C":
        qtn_coelho += qtn
    cont += 1
total = qtn_sapo + qtn_rato + qtn_coelho
print("Total de animais:", qtn_sapo + qtn_rato + qtn_coelho)
print(f"Total de Sapos: {qtn_sapo}")
print(f"Total de Ratos: {qtn_rato}")
print(f"Total de Coelhos: {qtn_coelho}")
print(f"Percentual de Sapos: {qtn_sapo / total * 100:.2f}%")
print(f"Percentual de Ratos: {qtn_rato / total * 100:.2f}%")
print(f"Percentual de Coelhos: {qtn_coelho / total * 100:.2f}%")
