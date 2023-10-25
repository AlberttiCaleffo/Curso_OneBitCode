# Conta letras maiúsculas e minúsculas

# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

def str_count(frase):
    tipo = {'maiuscula': 0, 'minuscula': 0}
    for letra in frase:
        if letra.isupper():
            tipo['maiuscula'] += 1
        elif letra.islower():
            tipo['minuscula'] += 1
        else:
            continue
    print(f'Temos {tipo["maiuscula"]} maiusculas e {tipo["minuscula"]} minusculas.')

str_count(input('Digite uma frase: '))