'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
def disPontos(xa,ya,xb,yb):
    return math.sqrt((xb-xa)**2+(yb-ya)**2)
print('Cálculo da distância entre dois pontos ')
x1=int(input('Informe XA: '))
y1=int(input('Informe YA: '))
x2=int(input('Informe XB: '))
y2=int(input('informe YB: '))
print(f'Distância entre (1, 1) e (4, 5) : {disPontos(x1,y1,x2,y2):.0f} ')
    