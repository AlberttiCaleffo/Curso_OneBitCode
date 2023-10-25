class Movie:
    platform = 'OneBitFilmes'
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluator = 0

    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f'Plataforma: {Movie.platform}')
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.totalEvaluation}")
        print(f"Duração Filme: {self.durationMinutes}")
        print(f'Total Avaliadores: {self.evaluator}\n')
         
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluator += 1
    
    def average(self):
        print(f'Média do filme: {self.name}: {self.totalEvaluation / self.evaluator}')

Movie.platform = 'OneBitCode Pro'
mario = Movie('Super Mario Bros', 2023, False, 135)
avatar = Movie('Avatar', 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.technical_sheet()
mario.average()
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.technical_sheet()
avatar.average()
