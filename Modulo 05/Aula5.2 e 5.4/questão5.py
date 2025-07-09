#Você está desenvolvendo um programa para auxiliar em cálculos de geometria básica. Crie as seguintes funções:
#A função calcula_perimetro_triangulo() que recebe três inteiros correspondentes aos lados de um triângulo e retorna o perímetro do triângulo, ou seja, a soma dos seus lados.
#A função calcula_perimetro_circulo() que recebe um inteiro referente ao raio do círculo e retorna o perímetro do círculo, dado por. 
#Use a constante da biblioteca math.
#A função calcula_perimetro_retangulo() que possui um parâmetro obrigatório lado1 e um opcional lado2, ambos inteiros. Se o valor opcional não for fornecido, significa que se trata de um quadrado. Sua função deve calcular e retornar o perímetro do retângulo, ou seja, a soma de seus lados.
#No programa principal apresente um menu com as opções disponíveis do seu sistema e uma quarta opção Sair. Solicite ao usuário a opção desejada, solicite as entradas correspondentes à opção escolhida, invoque a respective função e apresente o seu retorno. Seu programa deve retornar ao menu até que o usuário escolha a opção Sair

import math

def calcula_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=None):
    if lado2 is None:
        return 4 * lado1  # Quadrado
    else:
        return 2 * (lado1 + lado2)  # Retângulo

# Programa principal
while True:
    print("\n=== MENU DE CÁLCULOS GEOMÉTRICOS ===")
    print("1 - Calcular perímetro do triângulo")
    print("2 - Calcular perímetro do círculo")
    print("3 - Calcular perímetro do retângulo/quadrado")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        a = int(input("Digite o lado 1 do triângulo: "))
        b = int(input("Digite o lado 2 do triângulo: "))
        c = int(input("Digite o lado 3 do triângulo: "))
        resultado = calcula_perimetro_triangulo(a, b, c)
        print(f"O perímetro do triângulo é: {resultado:.2f}")

    elif opcao == "2":
        raio = int(input("Digite o raio do círculo: "))
        resultado = calcula_perimetro_circulo(raio)
        print(f"O perímetro do círculo é: {resultado:.2f}")

    elif opcao == "3":
        lado1 = int(input("Digite o lado 1: "))
        lado2 = input("Digite o lado 2 (pressione Enter se for um quadrado): ")
        if lado2 == "":
            resultado = calcula_perimetro_retangulo(lado1)
        else:
            resultado = calcula_perimetro_retangulo(lado1, int(lado2))
        print(f"O perímetro calculado é: {resultado:.2f}")

    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")