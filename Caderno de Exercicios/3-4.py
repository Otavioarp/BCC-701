'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

import math

s1 = int(input('Digite o lado 1 do triângulo (m): '))
s2 = int(input('Digite o lado 2 do triângulo (m): '))
s3 = int(input('Digite o lado 3 do triângulo (m): '))

p=s1+s2+s3
s=p/2

print(f'Perímetro do triângulo = {p} m')
print(f'Área do triângulo =  {math.sqrt(s*(s-s1)*(s-s2)*(s-s3)):.4f}  m^2')
