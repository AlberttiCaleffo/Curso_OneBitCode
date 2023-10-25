dados_times = {}
contador = 0

def linhas():
    print('-' * 50)
    
def org_time(time, ** jogadores):
    dados_times[time] = jogadores
  
while True:  
    org_time(input('Insira um time: ').title(), jogadores = [input('Digite o nome do jogador: ').title()])
    continuar = input('Quer continuar? [S/N] ').lower()
    if continuar == 'n':
        break

def visu_dados():
    print('Times', '          Jogadores')
    linhas()
    for k, v in dados_times.items():
        print(f'{k:<15}', end= ' ')
        print(v['jogadores'][0])
    linhas()
        
visu_dados()

while True:
    print('Quais das opções gostaria de solicitar:\n',
          'Qual time você quer remover? ', end= '')

    declaracao = input().title().strip()

    for k in set(dados_times.keys()):
        if k == declaracao:
            del dados_times[k]
    visu_dados()
    
    if 