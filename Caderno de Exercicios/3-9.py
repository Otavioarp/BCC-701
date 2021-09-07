'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

import math
t = int(input('Tempo(dias)'))
print(f'Posição (x,y) = ({400000*math.cos((2*math.pi)*t/27):5.0f},{400000*math.sin((2*math.pi)*t/27):5.0f}  )')
