# Cálculo da Distância

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,35 para viagens mais longas.

km_a_percorrer = float(input('Digite a distancia a ser percorrido: '))

if km_a_percorrer <= 200:
    print(f'O valor cobrado por km rodado é R$ 0,50 e o valor total fica em R$ {km_a_percorrer * 0.50:,.2f}'.replace('.', ','))
else: 
    print(f'O valor cobrado por km rodado é R$ 0,35 e o valor total fica em R$ {km_a_percorrer * 0.35:,.2f}'.replace('.', ','))