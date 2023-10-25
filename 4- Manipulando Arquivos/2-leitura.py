with open('Manipulando Arquivos/names.txt', 'r', encoding= 'UTF-8') as file:
    for line in file:
        print(f'{line.rstrip()}')