from agenda import ContactBook

contato = ContactBook('Albertti', 11991975691, 'mopixstories@gmail.com')
contato2 = ContactBook('Fred', 11345536574, 'Fred43@gmail.com')
contato2.adicionar()
contato.adicionar()
contato.listar()
contato.buscar()
contato2.remover()
contato2.listar()