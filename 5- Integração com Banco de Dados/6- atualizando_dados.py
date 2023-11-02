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
id = int(input('Informe o id do filme que deseja atualizar\n'))
name = input('Informe o novo nome do filme\n')

# 4 - Atualizando Dados
cursor.execute('''
        UPDATE movies set name = ?
        WHERE id = ?
               ''', (name, id))
connection.commit()
print('Dados Atualizados com sucesso!')

# 5 - Fechando conexão
connection.close()