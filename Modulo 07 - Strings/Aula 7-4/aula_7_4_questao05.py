# Abrindo o arquivo CSV para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escrevendo os títulos da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo os dados dos livros
    arquivo.write("O Senhor dos Anéis,J.R.R. Tolkien,1954,1178\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("Harry Potter e a Pedra Filosofal,J.K. Rowling,1997,223\n")
    arquivo.write("O Código Da Vinci,Dan Brown,2003,489\n")
    