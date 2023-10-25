# Aumento salário funcionário

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
# 15%.

salario = float(input('Digite o salario do funcionario: '))

if salario > 1250:
    print(f'O aumento do salario sera de 10% encima de {salario}. O valor total ficara em {(salario * 0.10) + salario}')
else:
    print(f'O aumento do salario sera de 15% encima de {salario}. O valor total ficara em {(salario * 0.15) + salario}')

