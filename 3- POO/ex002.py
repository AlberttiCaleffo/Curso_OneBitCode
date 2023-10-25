## Classe Produto e método desconto

# Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:
# 1- Cada produto deve ter um preço e um nome.
# 2- A classe deve ter um método construtor e o método dundle str.
# 3- A classe deve ter um método para desconto. 
# O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def __str__(self):
        return f'Nome do produto: {self.nome}\nValor: {self.valor}'
    
    def dados(self):
        print(f'Nome do produto: {self.nome}')
        print(f'Valor: R${float(self.valor):.2f}')
    
    def desconto(self, porcentagem):
        print(f'Desconto: {porcentagem}%')
        print(f'Valor após o desconto R${self.valor - (porcentagem / 100 * self.valor):.2f}\n')
        
        
produto1 = Produto('Verdura', 2.5)
produto2 = Produto('Beterraba', 0.98)
produto3 = Produto('Cenoura', 2)
produto1.dados()
produto1.desconto(50)
produto2.dados()
produto2.desconto(3)
produto3.dados()