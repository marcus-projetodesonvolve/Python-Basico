import math

# Lista de raios
raios = [1, 2.5, 3.7, 4]

# Usando map e lambda para calcular as áreas
areas = list(map(lambda r: round(math.pi * (r ** 2), 2), raios))

print(areas)