from agenda import Agenda

while True:
    contato = Agenda(input('Qual o nome: '), int(input('Qual o numero? ')))
    contato.adicionar()
    contato.listar()
    contato.remover(input('Gostaria de remover todos os contato? '))
    contato.listar()
    continuar = input('Continuar adicionando? [S/N] ').upper()   
    if continuar in 'N':
        break
        
