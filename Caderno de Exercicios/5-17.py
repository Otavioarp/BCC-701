'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

n = int(input('Dimensão do tabuleiro: '))

if 0 < n < 100:
    print('    ',end='')
    for c in range (0,n):
        print(f' {c+1}',end='')
    print()

    for i in range (0,n):
        h = '+'
        print(f'   {i+1}',end='')
        for j in range(0,i+1):
            if i % 2 != 0:
                if h == '+':
                    h = '#'
                else :
                    h = '+'
                print(f' {h}',end='')
            else :
                print(' x',end='')
        print()






else:
    print('Entrada inválida ')
