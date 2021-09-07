
'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''


import math
def calculaF(x , y):
    if x < 31 :
        f_x = x**2 + 2*y-3
    elif x < 61:
        f_x = math.sin(0.0175 * x) * math.cos(0.0175 * y)
    elif x < 91:
        f_x = 1 / (x**-2) + y
    else:
        f_x = math.pi
    return f_x

ini = int(input('Valor inicial: '))
while ini <-150 or ini >50:
    ini = int(input('Valor inicial: '))

fim = int(input('Valor final: '))
while  fim <= ini :
    fim = int(input('Valor final: '))

passo = int(input('Passo: '))
while passo < 1:
    passo = int(input('Passo:'))

print('x \ y |    ',end='')
for c in range (ini,fim+1,passo):
    print(f'   {c:3d}    ',end='')
print('\n---------------------------------------------------------')

for i in range(ini,fim+1,passo):
    print(f'  {i:3.0f} |  ',end='')
    for j in range (ini , fim+1 ,passo):
        print(f'{calculaF( i , j ):8.2f}  ',end='')
    print()
