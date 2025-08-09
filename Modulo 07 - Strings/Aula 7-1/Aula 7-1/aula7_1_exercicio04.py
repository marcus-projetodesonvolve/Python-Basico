#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. 
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. 
# Adicione o separador "-" na sua impressão.

# Solicita o número do celular
numero = input("Digite o número de celular (sem separadores): ")

# Verifica o tamanho e faz os ajustes
if len(numero) == 8:
    numero = "9" + numero
    print("Número ajustado:", numero[:5] + "-" + numero[5:])
elif len(numero) == 9:
    if numero[0] == "9":
        print("Número válido:", numero[:5] + "-" + numero[5:])
    else:
        print("Número inválido: o primeiro dígito deve ser 9.")
else:
    print("Entrada inválida. O número deve ter 8 ou 9 dígitos.")