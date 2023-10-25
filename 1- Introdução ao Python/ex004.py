# Substituindo caractere repetido

# Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

# Ex:

# abc xyz → xyc abz

inicial = input('Digite uma palavra: ')
final = input('Digite outra palavra: ')
inicial_2 = inicial.replace(inicial[-1], final[-1])
final_2 = final.replace(final[-1], inicial[-1])

print(f'{final_2} {inicial_2}')
print(f'{final} {inicial}')