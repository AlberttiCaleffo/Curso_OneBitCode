# Contagem Regressiva

# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
# O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

from time import sleep

for c in range(10, -1, -1):
    print(c, end= ' ', flush= True)
    sleep(1)