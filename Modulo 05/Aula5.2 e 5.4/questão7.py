#Escreva um programa que pergunte ao usuário qual operação ele deseja: maior ou menor. 
# Em seguida leia uma quantidade indefinida de valores do usuário, até que o usuário digite o valor zero. 
# Apresente ao final o maior ou menor dos valores digitados de acordo com a escolha do usuário.
#Sua solução deve incluir pelo menos uma função lambda

# Escolha da operação
operacao = input("Digite a operação desejada ('maior' ou 'menor'): ").strip().lower()

# Função lambda para selecionar a operação
selecao = lambda lista: max(lista) if operacao == "maior" else min(lista)

# Lista para armazenar os valores
valores = []

print("Digite os valores (0 para encerrar):")
while True:
    num = int(input("Número: "))
    if num == 0:
        break
    valores.append(num)

if valores:
    resultado = selecao(valores)
    print(f"O {operacao} valor digitado foi: {resultado}")
else:
    print("Nenhum valor foi digitado.")