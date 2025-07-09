#Crie uma função lambda para verificar se um número é par ou ímpar. 
#Em seguida, solicite ao usuário um número indefinidos de valores (até que o usuário digite 0). Para cada valor de entrada, informe se é par ou ímpar.

# Função lambda para verificar se é par ou ímpar
verifica_paridade = lambda x: "Par" if x % 2 == 0 else "Ímpar"

# Programa principal
print("Digite números inteiros (digite 0 para encerrar):")
while True:
    numero = int(input("Número: "))
    if numero == 0:
        print("Encerrando o programa.")
        break
    resultado = verifica_paridade(numero)
    print(f"{numero} é {resultado}")