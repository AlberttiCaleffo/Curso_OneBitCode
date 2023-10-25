def inverter(string):
    return string[::-1]

def par_indice(string):
    return string[::2]
    
# def impar_indice(string):
#    for c in range(len(string)):
#        if c % 2 == 1:
#            print(string[c], end= '')
#        if c == len(string) - 1:
#            print()

def impar_indice(string):
    return string[1::2]