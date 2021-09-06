'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
def valida_input():
    i = input('Deseja sair? (s/S/n/N): ')
    x = i.lower()
    comp = x == 's' or x == 'n'
    while comp == False  :
        print(f'ERRO: Resposta inválida: {i} ')
        i = input('Deseja sair? (s/S/n/n): ')
        x = i.lower()
        comp = x == 's' or x == 'n'
    if x == 'n' or x == 'N':
        comp = True
    else :
        comp = False
    return comp


def calcular( x , y):
    if x == y:
        val = x * y/(x + y)
    elif (x + y) % 2 != 0:
        val = x ** 2 + y ** 2
    else:
        val = x + y
    return val


print('TABELA DA FUNÇÃO')
print('x/y',end='')
for i in range (1,9):
    print(f'\t    {i}',end='')
print()
print('    ------------------------------------------------------------------')
for x in range(1,9):
    print(f'{x}  | ',end='')
    for y in range (1,x+1):
        print(f'  {calcular(x , y ):4.1f}  ',end='')
    print()
