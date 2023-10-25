# Tabuada

# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário

numero = int(input('Digite o numero para receber a tabuada: '))
inicio = int(input('De: '))
final = int(input('Até: '))
contador = 0

print(f'Tabuada de {numero}:')
for c in range(inicio, final + 1):
    print(f'{numero:<2} x {c:<2} = {numero * c:<2}')