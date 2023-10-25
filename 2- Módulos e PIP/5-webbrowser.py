import webbrowser

done = False

while not done:
    print('O que você deseja fazer?')
    print('1. Aprender Python')
    print('2. Aprender sobre módulos.')
    print('3. Aprender Python, Fullstack JS, Inglês e No Code')
    print('4. Sair')
    
    choice = int(input('>'))
    
    if choice == 1:
        webbrowser.open('http://www.python.org')
    elif choice == 2:
        webbrowser.open('docs.python.org/3/py-modindex.html')
    elif choice == 3:
        webbrowser.open('pages.onebitcode.com')
    elif choice == 4:
        done = True
    else:
        print('Opção invalida. Escolha uma opção entre 1 a 4.')