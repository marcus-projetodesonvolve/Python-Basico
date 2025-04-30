# Solicita os dados da ficha do personagem
classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").lower()  # Entrada em laranja
forca = int(input("Digite os pontos de Força: "))  # Entrada 
magia = int(input("Digite os pontos de Magia: "))  # Entrada 

# Verifica os requisitos de acordo com a classe escolhida
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = 5 < forca <= 15 and 5 < magia <= 15
else:
    valido = False  # Caso a classe seja inválida

# Imprime o resultado
print(valido)  # Impressão em branco