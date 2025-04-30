# Solicita as informações do usuário
genero = input("Digite seu gênero (M ou F): ")  # Entrada 
idade = int(input("Digite sua idade: "))  # Entrada 
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))  # Entrada 

# Verifica os critérios de aposentadoria
genero == "F"
pode_aposentar = idade > 60 or tempo_servico >= 30 or (idade == 60 and tempo_servico >= 25)
genero == "M"
pode_aposentar = idade > 65 or tempo_servico >= 30 or (idade == 60 and tempo_servico >= 25)
pode_aposentar = False  # Caso o gênero seja inválido

# Imprime o resultado
print(pode_aposentar)  # Impressão em branco
