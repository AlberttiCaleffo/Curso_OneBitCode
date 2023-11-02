import psycopg2

conn = psycopg2.connect(
    database = 'Fliperama',
    user = 'postgres',
    password = 'Gao426710',
    host = 'localhost',
    port = '5432'
)