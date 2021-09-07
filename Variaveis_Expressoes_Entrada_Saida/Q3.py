'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''


import math

l=float(input('Forneça o comprimento do fio:  '))
p=float(input('Forneça a força peso: '))
m=float(input('Forneça a massa:  '))
print(f'A aceleração da gravidade é {p/m:.3f}  ')
print(f'O período do pêndulo é {2*3.14*(l/(p/m))**(1/2):.3f}  ')#usando a função math.pi o resultado da diferente do exercicio
