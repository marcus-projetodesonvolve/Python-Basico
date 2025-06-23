#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais.

from datetime import datetime
data_atual = datetime.now()
hora_atual = datetime.now().time()
data_hoje = data_atual.strftime('%d/%m/%Y')
hora_hoje = hora_atual.strftime('%H:%M:%S')
print (data_hoje)
print (hora_hoje)