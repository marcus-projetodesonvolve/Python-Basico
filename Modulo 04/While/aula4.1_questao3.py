n1, n2, n3 = int(input("Digite a primeira nota: ")), int(input("Digite a segunda nota: ")), int(input("Digite a terceira nota: "))
m = (n1 + n2 + n3) / 3
if m>=60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
elif m < 40:
    print("Reprovado")
print(f"A média é: {m:.2f}")
print("FIM!")