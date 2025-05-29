#Escreva um programa que lê uma quantidade indefinida de valores e informa o produto dos valores positivos digitados. 
# A leitura é encerrada quando o usuário digitar o valor 0 (zero).

# Definindo Variável
produto = 1

while True:
    valor = float(input("Digite um valor (0 para encerrar): "))
    
    if valor == 0: break  # Encerra o loop se o valor for 0
    
    if valor > 0:
        produto *= valor  # Multiplica o produto pelos valores positivos
print(f"Produto dos valores positivos digitados: {produto}")