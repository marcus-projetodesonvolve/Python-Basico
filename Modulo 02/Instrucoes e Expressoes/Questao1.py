#Q1
#Faça um programa que armazene o valor de 20 reais de salário por hora de um trabalhador, e o número de 40 horas trabalhadas na semana. Com essas informações, calcule e imprima:

#Salário semanal bruto
#Valor descontado por semana INSS (10% do bruto)
#Valor descontado por semana pelo sindicato (5% do bruto)
#Salário semanal líquido (Bruto - Descontos)"""

# Definindo as variáveis

s_h = 20  # Salário por hora
n_h = 40  # Número de horas trabalhadas na semana
s_b = s_h * n_h  # Salário semanal bruto
print("Salário semanal bruto:R$", (s_b))
desconto_inss = s_b * 0.10  # Desconto do INSS (10% do bruto)
print("Valor descontado por semana INSS: R$", (desconto_inss));
desconto_sindicato = s_b * 0.05  # Desconto do sindicato (5% do bruto) 
print("Valor descontado por semana pelo sindicato: R$", (desconto_sindicato));
s_l = s_b - desconto_inss - desconto_sindicato  # Salário semanal líquido (Bruto - Descontos)
print("Salário semanal líquido: R$", (s_l))