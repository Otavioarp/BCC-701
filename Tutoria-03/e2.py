'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
n = int(input('CÁLCULO DAS MÉDIAS ARITMÉTICA E GEOMÉTICA\nQUANTIDADE DE NÚMEROS: '))
while n <= 0:
    n = int(input('QUANTIDADE DE NÚMEROS: '))

ma , mg =  0 , 1
for i in range ( 0 , n , 1 ):
    x = float(input(f'ITERAÇÃO {i + 1}:\nDIGITE UM NÚMERO REAL (MAIOR QUE ZERO):  '))
    while x <= 0:
        x = float(input('NÚMERO INVÁLIDO!\nDIGITE UM NÚMERO (MAIOR QUE ZERO):  '))
    ma += x
    mg = mg * x
    i += 1
print(f'IMPRESSÃO DOS RESULTADOS:\nMÉDIA ARITMÉTICA: {ma / n :.2f}\nMÉDIA GEOMÉTRICA: {mg ** ( 1 / n ) :.5f}')
