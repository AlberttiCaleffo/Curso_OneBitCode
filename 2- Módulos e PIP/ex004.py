from random import randint
from time import sleep

def linha():
    print('-' * 30)

n = int(input('Digite um numero contra a maquina: '))
maquina = randint(1, 10)
contador = 1

linha()
print('A maquina esta escolhendo um numero...')
sleep(1)
linha()

if n != maquina:
    while n != maquina:
        sleep(1)
        print(f'A maquina escolheu {maquina} e você {n}. A maquina venceu!')
        linha()
        sleep(1)
        n = input('Tente novamente: ')
        maquina = randint(1, 10)
        contador += 1
    else:
        print(f'Você venceu a maquina! Numeros de tentativas: {contador}')