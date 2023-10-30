import sqlite3 as sq

# 1 - Conectando no BD
connection = sq.connect('5- Integração com Banco de Dados/title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os regristros em um BD
'''

cursor = connection.cursor()

# 3 - Criando a Tabela
cursor.execute('''
CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
        );
               ''')

# 4 - Fechando a Conexão 
print('Tabela criada com sucesso!')
connection.close()