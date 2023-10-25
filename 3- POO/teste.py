class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f'Nome da pessoa é {self.nome} e a idade é {self.idade}'
    
    def andar(self):
        print('A pessoa esta andando...')
        global andar, correr
        andar = 1
        correr = 0
        
    def correr(self):
        print('A pessoa esta correndo...')
        global andar, correr
        andar = 0
        correr = 1
        
    def parar(self):
        if andar == 1:
            print('A pessoa parou de andar.')
        else:
            print('A pessoa parou de correr.')