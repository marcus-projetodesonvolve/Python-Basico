#4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. 
# As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

# #Entrada:
valor = int(input("Digite o valor em reais: ")) #Lê o valor em reais e converte para inteiro
# #Processamento:
notas_100 = valor // 100 #Calcula a quantidade de notas de 100
valor = valor % 100 #Calcula o restante do valor após retirar as notas de 100

notas_50 = valor // 50 #Calcula a quantidade de notas de 50
valor = valor % 50 #Calcula o restante do valor após retirar as notas de 50 

notas_20 = valor // 20 #Calcula a quantidade de notas de 20
valor = valor % 20 #Calcula o restante do valor após retirar as notas de 20

notas_10 = valor // 10 #Calcula a quantidade de notas de 10
valor = valor % 10 #Calcula o restante do valor após retirar as notas de 10

notas_5 = valor // 5 #Calcula a quantidade de notas de 5
valor = valor % 5 #Calcula o restante do valor após retirar as notas de 5

notas_2 = valor // 2 #Calcula a quantidade de notas de 2
valor = valor % 2 #Calcula o restante do valor após retirar as notas de 2

notas_1 = valor // 1 #Calcula a quantidade de notas de 1
valor = valor % 1 #Calcula o restante do valor após retirar as notas de 1

# #Saida:
print(f'{notas_100} notas de 100')
print(f'{notas_50} notas de 50') 
print(f'{notas_20} notas de 20') 
print(f'{notas_10} notas de 10') 
print(f'{notas_5} notas de 5') 
print(f'{notas_2} notas de 2')
print(f'{notas_1} notas de 1') #Imprime a quantidade de notas necessárias para pagar o valor