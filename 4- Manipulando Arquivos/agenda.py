class Agenda:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero  
    
    def adicionar(self):
        with open('agenda.txt', 'a') as agenda:
            agenda.write(f'{self.nome} - {self.numero}\n')
    
    def listar(self):
        with open('agenda.txt', 'r') as agenda:
            for a in agenda:
                print(f'{a.strip()}')
    
    def remover(self, apagar):
        if apagar == 's':
            with open('agenda.txt', 'w') as agenda:
                agenda.write('')
        else:
            pass
            
