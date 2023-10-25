class Movie:
    name = ''
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro Filme #
movie = Movie() 
movie.name = 'Super Mario Bros'
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130
print('##Dados do Filme##')
print(f'Nome do filme: {movie.name} \n Ano de Lançamento: {movie.yearLaunch}')

# Segundo Filme #
movie = Movie()
movie.name = 'John Wick 3'
movie.yearLaunch = 2023
movie.includedPlan = True
movie.note = 7.5
movie.durationMinutes = 203
print('##Dados do Filme##')
print(f'Nome do filme: {movie.name} \n Ano de Lançamento: {movie.yearLaunch}')