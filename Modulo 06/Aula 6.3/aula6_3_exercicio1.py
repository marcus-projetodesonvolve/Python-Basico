# Inicializa a lista de números
numeros = []

print("Digite pelo menos 4 números inteiros. Quando terminar, digite 'fim'.")

# Loop para coletar números do usuário
while True:
    entrada = input("Número (ou 'fim' para terminar): ")
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números antes de finalizar.")
    else:
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Saídas usando fatiamento
print("\n🔢 Lista original:", numeros)
print("🥇 3 primeiros elementos:", numeros[:3])
print("🏁 2 últimos elementos:", numeros[-2:])
print("🔄 Lista invertida:", numeros[::-1])
print("📍 Elementos de índice par:", numeros[::2])
print("📍 Elementos de índice ímpar:", numeros[1::2])