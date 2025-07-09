#Crie a função inverteValor() que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas operações aritméticas 
# Crie a função verificaInverso() que recebe o valor original e o valor invertido e retorna verdadeiro se ambos forem igualmente par ou igualmente ímpar. Retorne falso caso contrário. 
#No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.


def inverteValor(n):
    n = abs(n)  # Garante que o número seja positivo
    invertido = 0
    while n > 0:
        digito = n % 10
        invertido = invertido * 10 + digito
        n = n // 10
    return invertido

def verificaInverso(original, invertido):
    return (original % 2 == invertido % 2)

# Programa principal
numero = int(input("Digite um número inteiro: "))

valor_invertido = inverteValor(numero)
verificacao = verificaInverso(numero, valor_invertido)

print(f"Valor invertido: {valor_invertido}")
print(f"Os dois números têm mesma paridade (par ou ímpar)? {verificacao}")