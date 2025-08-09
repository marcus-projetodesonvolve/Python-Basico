# Abrir o arquivo com encoding 'latin-1'
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    # Ler todas as linhas
    linhas = arquivo.readlines()

# Imprimir as cinco primeiras linhas
for linha in linhas[:5]:
    print(linha.strip())