import sqlite3 as sq

# 1 - Criando o BD
connection = sq.connect('5- Integração com Banco de Dados/title.db')

# 2 - Verifica se houve alteração na base de dados
print(connection.total_changes)