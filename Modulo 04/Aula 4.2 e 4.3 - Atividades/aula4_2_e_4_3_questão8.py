#Vamos fazer uma calculadora que aceita expressões aritméticas de qualquer tamanho até que o usuário digite a palavra "Fim". Sua calculadora executa apenas as operações "+", "-".
n1, n2 = 0, 0
soma = 0
subtracao = 0
print("Bem-vindo à calculadora de expressões aritméticas!")
print("Digite 'Fim' para encerrar.")
while True:
    expressao = input("Digite a expressão (Soma ou Subtracao): ")
    if expressao == "Fim":
        print("Encerrando a calculadora. Até logo!")
        break
    elif expressao == "Soma":
        print("Operação de soma selecionada.")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))    
        soma = n1 + n2
        print(f"A soma é: {soma}")
    elif expressao == "Subtracao":
        print("Operação de subtração selecionada.")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))    
        subtracao = n1 - n2
        print(f"A subtração é: {subtracao}")
    else:
        print("Operação inválida. Por favor, digite 'Soma', 'Subtracao'ou 'Fim'.")
        continue


