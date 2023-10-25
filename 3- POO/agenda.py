class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
              
class ContactBook(Contact):
    def __init__(self, name, phone, email, bancoDeDados= []):
        super().__init__(name, phone, email)
        self.bancoDeDados = bancoDeDados
    
    def adicionar(self):
        self.bancoDeDados += [[self.name, self.phone, self.email]]
        print('Adicionado com sucesso!')
    
    def listar(self):
        for e, lista in enumerate(self.bancoDeDados):
            print(f'{e + 1} - {lista}')
    
    def buscar(self):
        indice = int(input('Digite o numero do indice: '))
        print(self.bancoDeDados[indice - 1])
    
    def remover(self):
        indice = int(input('Digit o numero do indice para deletar: '))
        self.bancoDeDados.pop(indice - 1)
    