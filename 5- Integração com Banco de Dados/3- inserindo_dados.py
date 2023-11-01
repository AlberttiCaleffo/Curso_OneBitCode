import sqlite3 as sq

# 1 - Conectando no BD
connection = sq.connect('5- Integração com Banco de Dados/title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os regristros em um BD
'''

cursor = connection.cursor()

# 3 - Inserindo Dados

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Super Mario Bros", 2023, 10)           
               ''')

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Avatar", 2023, 9.5)           
               ''')

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Velozes & Furiosos 10", 2023, 8.0)           
               ''')

# 4 - Gravando Dados no BD
connection.commit()
print('Dados Inseridos com Sucesso')

# 5 - Fechando conexão
connection.close()