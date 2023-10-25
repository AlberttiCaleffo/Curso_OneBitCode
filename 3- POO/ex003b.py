from exercicio3 import Trip

trip0 = Trip('São Paulo')
trip1 = Trip('Rio de Janeiro')
trip2 = Trip('Gramado')
trip3 = Trip('Santa Catarina')
trip4 = Trip('Caldas Novas')

print('Eai viajante. Temos algumas ofertas para você.')
traveler = input('Digite o seu nome para começar\n')
print(f'{traveler} temos 5 destinos que combinam com você'
    '''
    
      [0] - São Paulo
      [1] - Rio de Janeiro
      [2] - Gramado
      [3] - Santa Catarina
      [4] - Caldas Novas
      
    '''
    )

choice = int(input('Selecione o destino da viagem\n'))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >= 5:
        print('Esta opção não esta incluida em nossos destinos')
        break
    else:
        print(f'{traveler} sua viagem para {list_trip[choice].destiny} está marcada')
        print('Boa Viagem!')
        break