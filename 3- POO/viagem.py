class Viagem:
    def __init__(self, nome):
        self.nome = nome
        
    def destino(self):
        print('Qual destino você gostaria: \n'
              '1 - São Paulo\n'
              '2 - Rio de Janeiro')
    
    @staticmethod
    def escolha(opcao= input('Qual das opções? ')):
        while True:
            if opcao.isnumeric():
                return opcao
            else:
                print('Dado incorreto, digite novamente: ')