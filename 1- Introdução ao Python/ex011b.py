from time import sleep

dados_times = {}
jogadores = []

def menu():
    print('1- Adicionar time\n'
          '2- Remover um time\n'
          '3- Listar times\n'
          '4- Adicionar jogador em um time\n'
          '5- Remover jogador de um time\n'
          '6- Listar jogadores de um time\n'
          '7- Fim da operação\n')
 
def visu_dados():
    print('Indice', ' Time', '         Jogadores')
    linhas()
    for c, k in enumerate(dados_times.keys()):
        print(f'{c:<7} {k:<13}', end=' ')
        for v in dados_times[k]:
            print(f'{v}', end= ' ')
            if v == dados_times[k][-1]:
                print()
    linhas()
    
def linhas():
    print('-' * 50)    
  
while True:
    time = input('Digite um time: ').title().strip()
    while True:
        jogadores.append(input('Coloque um jogador no time: ').title())
        continuar = input('Quer continuar? [S/N] ').lower()
        if continuar == 'n':
            break
    dados_times[time] = jogadores[:]
    jogadores.clear()
    visu_dados()
    while True:
        menu()
        declaracao = int(input('Qual das opções: '))
        if declaracao == 1:
            break
        if declaracao == 2:
            remover = input('Qual time gostaria de remover? ').title().strip()
            del dados_times[remover]
            print('Deletando...')
            sleep(1)
            visu_dados()
        elif declaracao == 3:
            linhas()
            print('Time(s)\n')
            for k in dados_times.keys():
                print(k)
            linhas()
        elif declaracao == 4:
            jogadores.append(input('Qual jogador? ').title())
            time = input('Qual o time? ').title()
            dados_times[time] += jogadores
            print(dados_times)
            jogadores.clear()
            visu_dados()
        elif declaracao == 5:
            time = input('Qual time? ').title()
            jogadores = input('Qual jogador gostaria de eliminar do time? ').title()
            dados_times[time].remove(jogadores)
            visu_dados()
        elif declaracao == 6:
            time = input('Qual time você gostaria de apresentar os jogadores? ').title()
            linhas()
            print(time, '\n')
            for j in dados_times[time]:
                print(j)
            linhas()
        elif declaracao == 7:
            break
        else:
            print('Opção invalida!')
    if declaracao == 7:
        break