names = []

with open('Manipulando Arquivos/names.txt', 'r', encoding= 'UTF-8') as file:
    for line in file:
        names.append(line.rstrip().title())
        
for name in sorted(names):
    print(name)