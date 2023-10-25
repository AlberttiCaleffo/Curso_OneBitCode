# Substituindo caractere repetido

# Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências 
# de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
# Ex:
# fifa 23 → fi#a 23
# restart→ resta#t

# texto = 'paralelepipedo'
# texto2 = 'restart'

# print(f'{texto[0]}{texto[1:].replace("p", "$")}')
# print(f'{texto2[0]}{texto2[1:].replace("r", "$")}')

palavra = input('Digite uma palavra: ').lower()
letra_inicial = palavra[0]
restante = palavra[1:].replace(palavra[0], '$')

print(f'{letra_inicial}{restante}')
print(letra_inicial + restante)