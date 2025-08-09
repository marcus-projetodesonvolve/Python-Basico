import re

# Caminho do arquivo
arquivo = "estomago.txt"

# Abrir o arquivo para leitura
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. Imprimir as primeiras 25 linhas
print(" Primeiras 25 linhas do roteiro:\n")
for linha in linhas[:25]:
    print(linha.strip())

# 2. Número total de linhas
num_linhas = len(linhas)
print(f"\n📏 Número total de linhas: {num_linhas}")

# 3. Linha com maior número de caracteres
linha_maior = max(linhas, key=lambda l: len(l))
print(f"\n Linha com mais caracteres ({len(linha_maior.strip())} caracteres):\n{linha_maior.strip()}")

# 4. Contagem de menções aos personagens
texto_completo = "".join(linhas)

# Regex para encontrar "Nonato" e "Íria" com variações de maiúsculas/minúsculas
nonato_count = len(re.findall(r"\bnonato\b", texto_completo, re.IGNORECASE))
iria_count = len(re.findall(r"\bíria\b", texto_completo, re.IGNORECASE))

print(f"\n Menções aos personagens:")
print(f"– Nonato: {nonato_count}")
print(f"– Íria: {iria_count}")