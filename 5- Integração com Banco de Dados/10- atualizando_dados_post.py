from conexao_post import conn

cursor_obj = conn.cursor()

sql = '''
    UPDATE game
    SET year = %s
    WHERE id = %s
'''

cursor_obj.execute(sql, (2020, 1))
conn.commit()
print('Dados atualizados com sucesso')
conn.close()