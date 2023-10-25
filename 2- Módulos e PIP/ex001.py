# Modulos de strings
# Escreva um módulo em python para tratar algumas strings e que possua as seguintes
# funcionalidades:

# 1. Inverter uma string de trás pra frente.
# 2. Retornar apenas letras com indice par.
# 3. Retornar apenas letras com indice ímpar.

import str

texto = input('Digite algo: ')

print(str.inverter(texto))
print(str.par_indice(texto))
print(str.impar_indice(texto))