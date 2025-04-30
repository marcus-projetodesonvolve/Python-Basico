

# Solicita informações ao usuário
idade = int(input("Digite sua idade: "))  # Entrada entrada de dados
jogou_mais_3 = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")  # Entrada de dado
jogou_mais_3 = jogou_mais_3 == "true"
vezes_vencido = int(input("Quantas vezes você venceu um jogo de tabuleiro? "))  # Entrada de dados

# Verifica as condições para admissão no clube
pode_ingressar = (16 <= idade <= 18) and jogou_mais_3 and vezes_vencido >= 1

# Imprime o resultado
print(pode_ingressar)  # Impressão em branco