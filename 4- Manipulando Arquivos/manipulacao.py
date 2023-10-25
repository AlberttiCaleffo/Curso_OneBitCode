def manipulacaoTexto(arquivo, linhas):
    with open(f'{arquivo}.txt', 'r', encoding= 'UTF-8') as file:
        for e, line in enumerate(file):
            print(f'{line.rstrip().title()}')
            if e == linhas - 1:
                break
            