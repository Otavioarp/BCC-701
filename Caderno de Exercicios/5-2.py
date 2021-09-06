'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
ce=float(input('Entre com o comprimento do encanamento (m) ou 0 para fim: '))
while ce > 0:
      c1 = int(input('Total de canos tipo C1 (1.7m): '))
      c2 = int(input('Total de canos tipo C2 (2.3m): '))
      if c1 * 1.7 + c2 * 2.3 - ce == 0:
          print('Acertou na mosca, não sobra nem falta cano! ')
      elif c1 * 1.7 + c2 * 2.3 - ce < 0:
          print(f'Vai faltar {abs(c1 * 1.7 + c2 * 2.3 - ce):.1f} metros de cano ')
      else:
          print(f'Vai sobrar {c1 * 1.7 + c2 * 2.3 - ce:.1f} metros de cano')
      ce=float(input('Entre com o comprimento do encanamento (m) ou 0 para fim: '))
