import glob, os, zipfile

# 1 - Diretório de trabalho atual
os.getcwd()

# 2 - listar todos os arquivos .txt
for file in glob.glob('*.txt'):
    print(file)
    
# 3 - listar todos os arquivos .csv
for file in glob.glob('*.csv'):
    print(file)
    
# 4 - Compactar arquivos .txt
with zipfile.ZipFile('name.zip', 'w') as zip:
    for file in glob.glob('*.txt'):
        zip.write(file)
        
# 5 - Compactar arquivos .csv
with zipfile.ZipFile('name2.zip', 'w') as zip:
    for file in glob.glob('*.csv'):
        zip.write(file)        
        
# 6 - Compactar todos os arquivos
with zipfile.ZipFile('tudo.zip', 'w') as zip:
    for file in glob.glob('*'):
        zip.write(file)    