# Lista números pares e ímpares de uma lista

# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

def par_impar(* n):
    par = []
    impar = []
    for c in n:
        if c % 2 == 0:
            par.append(c)
        else:
            impar.append(c)
    return par, impar

print(par_impar(4, 6, 2, 3, 19, 15))