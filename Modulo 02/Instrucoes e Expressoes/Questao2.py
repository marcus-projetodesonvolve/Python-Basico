#Q2
#Altere o programa anterior para a partir dos valores de horas trabalhadas por semana e salário por hora, calcular em somente duas instruções:

#Salário semanal bruto
#Salário semanal líquido com todos os descontos. Para a segunda instrução, realize todos os cálculos aritméticos em uma expressão composta.

# Definindo as variáveis

s_b = 20 * 40  # Salário semanal bruto
print("Salário semanal bruto:R$", (s_b))
s_l = s_b - (s_b * 0.10) - (s_b * 0.05)  # Salário semanal líquido (Bruto - Descontos)
print("Salário semanal líquido: R$", (s_l))
