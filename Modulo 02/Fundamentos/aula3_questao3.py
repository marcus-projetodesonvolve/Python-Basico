#3 - Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. 
# Ou seja, ao final v1 terá o valor de v2, e v2 o valor de v1. 
# Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente. 

v1 = 10
print("O primeiro valor de v1 é:",v1)
v2 = 20
print("O primeiro valor de v2 é:",v2)
# Criando uma variável auxiliar para troca
aux = v1
v1 = v2
v2 = aux
print("O novo valor de v1 é:",v1)
print("O novo valor de v2 é:",v2)