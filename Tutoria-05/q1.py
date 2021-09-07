'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
import math

def calcular(x , y):
    if (x + y) % 2 == 0:
        val = 1 / (x * y) + math.sin(x + y)
    elif (x*y) % 2 != 0:
        val = math.sqtr( y**2 - 4*x)
    else:
        val = (x + y) ** (1/3)
    return val

print('x/y |',end='')
for i in range(3,25,3):
    print(f'\t{i:.0f}   ',end='' )
print()
print('--------------------------------------------------------------------')

for x in range(2,31,2):
    print(f'{x:3.0f} |',end='')
    for y in range(3,25,3):
        h = calcular(x,y)
        if h > 0:
            print(f'  {calcular(x,y):3.2f}  ',end='')
        else:
            print(f' {calcular(x,y):3.2f}  ',end='')
    print()
