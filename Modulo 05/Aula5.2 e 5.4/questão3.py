#Crie uma função em Python chamada soma_digitos que recebe um número inteiro como parâmetro e retorna a soma dos seus dígitos. Por exemplo, para o número 123, a função deve retornar 6,
#O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas
#No programa principal solicite ao usuário que insira um número e utilize a função soma_digitos para calcular e exibir a soma dos seus dígitos.

def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10  # Obtém o último dígito
        soma += digito        # Adiciona o dígito à soma
        numero //= 10         # Remove o último dígito do número
    return soma

# Programa principal
numero = int(input("Digite um número inteiro: "))
resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é {resultado}.")
