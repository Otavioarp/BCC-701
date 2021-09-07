'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

n1 = int(input('Digite o número de linhas: '))
n2 = int(input('Digite o número de colunas: '))
x , y = 1 , 1
if n1 > 0 and n2 > 0:
    for j in range(0,n1):
        print(f'\t',end='')
        if j % 2 == 0:
            for i in range(1,n2+1):
                print(f'{i} ',end='')
            print()
        else:
            for i in range(n2,0,-1):
                print(f'{i} ',end='')
            print()
else:
    print('Dados de entrada inválidos ')
