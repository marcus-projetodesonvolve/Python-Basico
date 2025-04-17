#nome = input("Digite seu nome: ")
#print ('Seu Nome é:', nome)

#nome = input("Digite seu nome: ")
#print (type(nome))
#idade = input("Digite sua idade: ")
#print (type(idade))
#print ('Seu Nome é:', nome,'e sua idade é:', idade)
#print (2023-idade)
#Dessa forma a idade é uma string, e não um número inteiro, então não podemos fazer operações matemáticas com ela.
# Para resolver isso, podemos converter a string para um número inteiro usando a função int()

#idade1 = input("Digite sua idade: ")
#idade2 = input("Digite a idade de outra pessoa: ")
#print (idade1+idade2)
#Dessa forma a idade é uma string, e ele faz apenas a concatenação deles.

#nome = input("Digite seu nome: ")
#print (type(nome))
#idade = int(input("Digite sua idade: "))
#print (type(idade))
#print ('Seu Nome é:', nome,'e sua idade é:', idade)
#print ('Voce Nasceu em:', 2025-idade)
#peso = float(input("Digite seu peso: "))
#print (type(peso))
#print ('Seu peso é:', peso,'kg')

#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#peso = float(input("Digite seu peso: "))
#print (f'Seu Nome é: {nome}, sua idade é: {idade}, e seu peso é: {peso}, kg')
#Dessa forma, podemos usar a formatação de strings para imprimir os valores de forma mais legível e organizada.

#kmh = int(input())
#print (f'{kmh} km/h é igual a {kmh/3.6} m/s')
#Dessa forma o valor em m/ sem formatar a quantidade de casas decimais, mas podemos usar a formatação de strings para limitar o número de casas decimais.

#kmh = int(input())
#print (f'{kmh} km/h é igual a {kmh/3.6:2.0f} m/s')
#Dessa forma, o valor em m/s é formatado para ter não ter casas decimais,caso queira apresentar as casas decimais a expressão ficaria assim:
#print (f'{kmh} km/h é igual a {kmh/3.6:.2f} m/s'), onde seria apresentada duas casas decimais apos a vírgula. 

saldo = 123430.35
print (f'Seu saldo é: {saldo:.4f}')
#Dessa forma, o valor em reais é formatado para ter 4 casas decimais,caso queira apresentar as casas decimais a expressão ficaria assim:
codigo = 14
print (f'Seu código é: {codigo:05d}')
#Dessa forma, o valor do saldo é formatado para ter 4 casas decimais e o código é formatado para ter 5 dígitos, com zeros à esquerda se necessário.
#Isso é útil para garantir que os valores sejam apresentados de forma consistente e legível.