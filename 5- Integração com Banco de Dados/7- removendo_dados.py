import sqlite3 as sq

# 1 - Conectando no BD
connection = sq.connect('5- Integração com Banco de Dados/title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os regristros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitando Dados do Usuario
id = int(input('Informe o id do filme que deseja remover\n'))

# 4 - Removendo Dados
cursor.execute('''
        DELETE FROM movies
        WHERE id = ?
               ''', (id,))
connection.commit()
print('Filme removido com sucesso!')

# 6 - Fechando conexão
connection.close()