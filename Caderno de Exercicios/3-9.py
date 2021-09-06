'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

import math
t = int(input('Tempo(dias)'))
print(f'Posição (x,y) = ({400000*math.cos((2*math.pi)*t/27):5.0f},{400000*math.sin((2*math.pi)*t/27):5.0f}  )')
