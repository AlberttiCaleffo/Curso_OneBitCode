import sqlite3 as sq

# 1 - Conectando no BD
connection = sq.connect('5- Integração com Banco de Dados/title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os regristros em um BD
'''

cursor = connection.cursor()

# 3 - Lendo Dados da tabela
data = cursor.execute('''
        SELECT name, year, score FROM movies              
                      ''')
print(data.fetchall())

# 4 - Iterando os Dados
for row in cursor.execute('SELECT * FROM movies'):
    print(f'{row}\n')

# 5 - Ordenando os Dados pelo Score
for row in cursor.execute('SELECT * FROM movies ORDER BY score desc'):
    print(f'{row}')

# 6 - Fechando conexão
connection.close()