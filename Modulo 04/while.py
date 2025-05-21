#Entrada de dados
n = int(input("Digite um  valor para n: "))

#Inicialização de variáveis
soma = 0
cont = 1
#Processamento
while cont <= n:
    soma += cont
    cont += 1
#Saída de dados
print(f"A soma dos 1 a {n} é: {soma}")