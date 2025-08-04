'''Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt",
removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha.
 Ao final, imprima o conteúdo do arquivo "palavras.txt".'''

import re

# Nome dos arquivos
arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

# Lê o conteúdo do arquivo original
with open(arquivo_origem, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Remove espaços em branco extras e caracteres não alfabéticos
palavras = re.findall(r'\b[a-zA-ZáéíóúãõâêôàçÁÉÍÓÚÃÕÂÊÔÀÇ]+\b', conteudo)

# Salva cada palavra em uma linha no novo arquivo
with open(arquivo_destino, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# Lê e imprime o conteúdo do novo arquivo
with open(arquivo_destino, "r", encoding="utf-8") as f:
    print(f.read())