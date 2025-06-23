#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. 
#Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

n1 = float(input("Digite o primeiro numero: "))
n2 =  float(input("Digite o segundo numero:"))

diferenca = round(abs(n1-n2),2)

print(f"A diferença absoluta entre os numeros é: {diferenca}")